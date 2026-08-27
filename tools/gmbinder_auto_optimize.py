#!/usr/bin/env python3
"""Autonomous GM Binder pagination optimizer (geometry-driven)."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import md_to_gmbinder as gen  # noqa: E402
from gmbinder_geometry import (  # noqa: E402
    PageStatus,
    analyze_document_scan,
    classify_occupancy,
    deduplicate_overflow_findings,
    first_failing_page,
    first_overflow_finding,
    overflow_metrics,
)
from gmbinder_pagination_io import (  # noqa: E402
    add_derived_break,
    breaks_for_generator,
    is_protected_break,
    load_pagination_file,
    mark_all_browser_validated,
    mark_break_obsolete,
    migrate_pre_validator_classification,
    pagination_state_hash,
    save_pagination_file,
)
from gmbinder_semantic import candidate_break_keys_for_overflow  # noqa: E402
from optimize_gmbinder_pagination import block_key_to_break, choose_break_from_finding  # noqa: E402

MASTER = ROOT / "dawn-of-the-jedaii-campaign-guide.md"


def load_pagination_blocks():
    from gmbinder_semantic import all_blocks_for_pagination
    from md_to_gmbinder import extract_koorivar_species_and_css, resolve_koorivar_path

    guide = MASTER.read_text(encoding="utf-8")
    try:
        species, _ = extract_koorivar_species_and_css(resolve_koorivar_path(None))
    except FileNotFoundError:
        species = None
    return all_blocks_for_pagination(guide, species)
PAGINATION = ROOT / "tools" / "gmbinder_pagination.json"
GMB_OUT = ROOT / "gmbinder" / "dawn-of-the-jedaii-gmbinder.md"
LOG_PATH = ROOT / "reports" / "audits" / "gmbinder-pagination-optimization-log.json"
BLOCKED_PATH = ROOT / "reports" / "audits" / "gmbinder-pagination-blocked.json"


@dataclass
class CandidateAction:
    kind: str  # add_break | remove_break
    description: str
    break_id: str | None = None
    chapter: str | None = None
    before_heading: str | None = None
    before_block_key: str | None = None


def guide_hash() -> str:
    return hashlib.sha256(MASTER.read_bytes()).hexdigest()


def gmb_hash() -> str:
    return hashlib.sha256(GMB_OUT.read_bytes()).hexdigest() if GMB_OUT.is_file() else ""


def regenerate(data: dict[str, Any]) -> None:
    breaks = breaks_for_generator(data)
    text, _ = gen.build_document(gen.resolve_koorivar_path(None), breaks, inject_trace_markers_flag=True)
    GMB_OUT.write_text(text, encoding="utf-8")


def score_scan(scan: dict[str, Any]) -> dict[str, Any]:
    analyses, findings = analyze_document_scan(scan)
    metrics = overflow_metrics(findings)
    fp = first_failing_page(analyses)
    first_fail_idx = fp.page_index if fp else None
    underfill = sum(1 for a in analyses if a.status == PageStatus.WARNING_UNDERFILLED)
    occupancy_warnings = [
        {
            "page_index": a.page_index,
            "occupancy_ratio": a.occupancy_ratio,
            "classification": classify_occupancy(a.occupancy_ratio),
        }
        for a in analyses
        if a.occupancy_ratio is not None and classify_occupancy(a.occupancy_ratio) != "ok"
    ]
    return {
        **metrics,
        "first_failing_page_index": first_fail_idx,
        "underfill_warning_count": underfill,
        "occupancy_warnings": occupancy_warnings,
        "break_count": None,
    }


def compare_scores(a: dict[str, Any], b: dict[str, Any]) -> int:
    """Return negative if a is better than b."""
    keys = [
        ("raw_overflow_count", -1),
        ("semantic_block_overflow_count", -1),
        ("failing_page_count", -1),
        ("first_failing_page_index", -1),
    ]
    for key, direction in keys:
        av = a.get(key)
        bv = b.get(key)
        if av is None and bv is None:
            continue
        if av is None:
            return 1
        if bv is None:
            return -1
        if av != bv:
            return direction * (1 if av < bv else -1)
    return 0


def block_index(blocks, chapter: str, heading: str) -> int | None:
    for i, b in enumerate(blocks):
        if b.chapter == chapter and b.heading_line == heading:
            return i
    return None


def enumerate_candidates(
    scan: dict[str, Any],
    data: dict[str, Any],
) -> list[CandidateAction]:
    blocks = load_pagination_blocks()
    _, findings = analyze_document_scan(scan)
    fo = first_overflow_finding(findings)
    if not fo:
        return []
    candidates: list[CandidateAction] = []

    keys = candidate_break_keys_for_overflow(
        blocks, fo.gmb_src, fo.nearest_heading or fo.text_excerpt
    )
    for key in keys:
        hit = block_key_to_break(blocks, key)
        if hit:
            ch, heading, bkey = hit
            candidates.append(
                CandidateAction(
                    kind="add_break",
                    description=f"add pagebreak before {heading!r}",
                    chapter=ch,
                    before_heading=heading,
                    before_block_key=bkey,
                )
            )
    fallback = choose_break_from_finding(fo, blocks)
    if fallback:
        ch, heading, bkey = fallback
        if not any(c.before_heading == heading for c in candidates if c.kind == "add_break"):
            candidates.append(
                CandidateAction(
                    kind="add_break",
                    description=f"add pagebreak before {heading!r} (fallback)",
                    chapter=ch,
                    before_heading=heading,
                    before_block_key=bkey,
                )
            )

    # Remove unvalidated seeds on failing page chapter or superseded by earlier break
    fail_chapters = {f.nearest_heading for f in findings[:50]}
    for b in data.get("breaks", []):
        if is_protected_break(b):
            continue
        if b.get("selection_method") != "unvalidated_seed":
            continue
        candidates.append(
            CandidateAction(
                kind="remove_break",
                description=f"remove unvalidated seed {b['id']}",
                break_id=b["id"],
            )
        )

    # Superseded: earlier derived break in same chapter makes later seed redundant
    chapter_breaks = {}
    for b in data.get("breaks", []):
        chapter_breaks.setdefault(b["chapter"], []).append(b)
    for chapter, blist in chapter_breaks.items():
        indexed = []
        for b in blist:
            idx = block_index(blocks, chapter, b["before_heading"])
            if idx is not None:
                indexed.append((idx, b))
        indexed.sort(key=lambda x: x[0])
        for i, (_, earlier) in enumerate(indexed):
            for _, later in indexed[i + 1 :]:
                if earlier.get("selection_method") == "derived" and later.get(
                    "selection_method"
                ) in {"unvalidated_seed", "derived"}:
                    if not is_protected_break(later):
                        candidates.append(
                            CandidateAction(
                                kind="remove_break",
                                description=(
                                    f"remove superseded break {later['id']} "
                                    f"(earlier: {earlier['id']})"
                                ),
                                break_id=later["id"],
                            )
                        )
    # De-duplicate candidate list
    seen: set[str] = set()
    unique: list[CandidateAction] = []
    for c in candidates:
        sig = f"{c.kind}|{c.break_id}|{c.before_heading}"
        if sig in seen:
            continue
        seen.add(sig)
        unique.append(c)
    return unique


def apply_candidate(data: dict[str, Any], c: CandidateAction) -> dict[str, Any]:
    branch = copy.deepcopy(data)
    if c.kind == "add_break" and c.chapter and c.before_heading:
        add_derived_break(
            branch,
            chapter=c.chapter,
            before_heading=c.before_heading,
            before_block_key=c.before_block_key or "",
            reason=f"optimizer: {c.description}",
            source_revision=guide_hash(),
            browser_validated=False,
        )
    elif c.kind == "remove_break" and c.break_id:
        if not mark_break_obsolete(branch, c.break_id, c.description):
            raise RuntimeError(f"cannot remove protected break {c.break_id}")
    else:
        raise RuntimeError(f"unknown candidate {c}")
    return branch


def apply_ch04_regression(data: dict[str, Any]) -> dict[str, Any]:
    """Remove superseded Ch04 seed before Sealed Vaults; keep derived Section 5 break."""
    branch = copy.deepcopy(data)
    mark_break_obsolete(
        branch,
        "ch04-sealed-vaults",
        "superseded by geometry-derived break before ### 5. Machine-Spirit Interfaces",
    )
    return branch


def migrate_and_reclassify() -> dict[str, Any]:
    data = load_pagination_file(PAGINATION)
    info = migrate_pre_validator_classification(data)
    save_pagination_file(data, PAGINATION)
    return info


def initial_ch04_cleanup() -> dict[str, Any]:
    data = load_pagination_file(PAGINATION)
    removed = mark_break_obsolete(
        data,
        "ch04-sealed-vaults",
        "Ch04 regression: superseded by derived break before Section 5",
    )
    save_pagination_file(data, PAGINATION)
    regenerate(data)
    return {"ch04_sealed_vaults_removed": removed}


def pick_best_candidate_offline(
    scan: dict[str, Any],
    data: dict[str, Any],
    *,
    include_ch04_cleanup: bool = False,
) -> tuple[dict[str, Any] | None, CandidateAction | None, dict[str, Any]]:
    """Pick best candidate using current scan as baseline (offline scoring proxy).

    Browser loop must re-verify after apply. When multiple add/remove candidates exist,
    prefer remove superseded seeds first if they reduce break count without known harm.
    """
    baseline = score_scan(scan)
    candidates = enumerate_candidates(scan, data)
    if include_ch04_cleanup:
        ch04 = apply_ch04_regression(data)
        if pagination_state_hash(ch04) != pagination_state_hash(data):
            candidates.insert(
                0,
                CandidateAction(
                    kind="remove_break",
                    description="Ch04 remove ch04-sealed-vaults",
                    break_id="ch04-sealed-vaults",
                ),
            )

    best_data: dict[str, Any] | None = None
    best_action: CandidateAction | None = None
    best_score = baseline

    # Offline cannot re-render; use heuristic: prefer add_break at first overflow,
    # else remove superseded seed
    fo = first_overflow_finding(analyze_document_scan(scan)[1])
    if fo:
        for c in candidates:
            if c.kind == "add_break":
                branch = apply_candidate(data, c)
                # Heuristic score: assume add helps
                proxy = dict(baseline)
                proxy["raw_overflow_count"] = max(0, baseline["raw_overflow_count"] - 5)
                proxy["semantic_block_overflow_count"] = max(
                    0, baseline["semantic_block_overflow_count"] - 1
                )
                if compare_scores(proxy, best_score) < 0 or best_action is None:
                    best_data = branch
                    best_action = c
                    best_score = proxy
                break

    if best_action is None:
        for c in candidates:
            if c.kind == "remove_break" and "superseded" in c.description.lower():
                try:
                    branch = apply_candidate(data, c)
                except RuntimeError:
                    continue
                best_data = branch
                best_action = c
                break

    if best_action is None and candidates:
        c = candidates[0]
        try:
            best_data = apply_candidate(data, c)
            best_action = c
        except RuntimeError:
            pass

    return best_data, best_action, baseline


def apply_best_from_browser_scores(
    baseline_score: dict[str, Any],
    candidate_results: list[tuple[CandidateAction, dict[str, Any], dict[str, Any]]],
) -> tuple[CandidateAction | None, dict[str, Any] | None]:
    best: tuple[CandidateAction | None, dict[str, Any] | None] = (None, None)
    best_score = baseline_score
    for action, branch, score in candidate_results:
        if compare_scores(score, best_score) < 0:
            best = (action, branch)
            best_score = score
    if compare_scores(best_score, baseline_score) >= 0:
        return None, None
    return best


def append_log(entry: dict[str, Any]) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    log: dict[str, Any] = {"iterations": []}
    if LOG_PATH.is_file():
        log = json.loads(LOG_PATH.read_text(encoding="utf-8"))
    log.setdefault("iterations", []).append(entry)
    LOG_PATH.write_text(json.dumps(log, indent=2) + "\n", encoding="utf-8")


def cmd_migrate(_: argparse.Namespace) -> int:
    info = migrate_and_reclassify()
    data = load_pagination_file(PAGINATION)
    ch04 = initial_ch04_cleanup()
    print(json.dumps({**info, **ch04, "state_hash": pagination_state_hash(data)}, indent=2))
    return 0


def cmd_plan(args: argparse.Namespace) -> int:
    scan = json.loads(Path(args.scan_json).read_text(encoding="utf-8"))
    data = load_pagination_file(PAGINATION)
    baseline = score_scan(scan)
    cands = enumerate_candidates(scan, data)
    print(
        json.dumps(
            {
                "baseline": baseline,
                "candidates": [c.__dict__ for c in cands[:30]],
                "state_hash": pagination_state_hash(data),
            },
            indent=2,
        )
    )
    return 0


def cmd_apply(args: argparse.Namespace) -> int:
    data = load_pagination_file(PAGINATION)
    action = CandidateAction(
        kind=args.kind,
        description=args.description or args.kind,
        break_id=args.break_id,
        chapter=args.chapter,
        before_heading=args.before_heading,
        before_block_key=args.before_block_key,
    )
    branch = apply_candidate(data, action)
    save_pagination_file(branch, PAGINATION)
    regenerate(branch)
    print(json.dumps({"applied": action.__dict__, "state_hash": pagination_state_hash(branch)}, indent=2))
    return 0


def cmd_score(args: argparse.Namespace) -> int:
    scan = json.loads(Path(args.scan_json).read_text(encoding="utf-8"))
    print(json.dumps(score_scan(scan), indent=2))
    return 0


def cmd_finalize_pass(args: argparse.Namespace) -> int:
    data = load_pagination_file(PAGINATION)
    mark_all_browser_validated(data, guide_hash())
    save_pagination_file(data, PAGINATION)
    print("all breaks marked browser_validated")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("migrate", help="Reclassify seeds and Ch04 cleanup").set_defaults(func=cmd_migrate)
    sp = sub.add_parser("plan", help="List candidates for scan")
    sp.add_argument("--scan-json", required=True)
    sp.set_defaults(func=cmd_plan)
    sp = sub.add_parser("score", help="Score a scan JSON")
    sp.add_argument("--scan-json", required=True)
    sp.set_defaults(func=cmd_score)
    sp = sub.add_parser("apply", help="Apply one candidate action")
    sp.add_argument("--kind", required=True, choices=["add_break", "remove_break"])
    sp.add_argument("--break-id")
    sp.add_argument("--chapter")
    sp.add_argument("--before-heading")
    sp.add_argument("--before-block-key")
    sp.add_argument("--description")
    sp.set_defaults(func=cmd_apply)
    sub.add_parser("finalize-pass", help="Mark all breaks browser validated").set_defaults(
        func=cmd_finalize_pass
    )
    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
