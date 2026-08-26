#!/usr/bin/env python3
"""Iteratively optimize GM Binder pagination using rendered-layout geometry."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import md_to_gmbinder as gen  # noqa: E402
from gmbinder_geometry import (  # noqa: E402
    DEFAULT_TOLERANCE_PX,
    PageStatus,
    analyze_document_scan,
    first_failing_page,
    first_overflow_finding,
)
from gmbinder_pagination_io import (  # noqa: E402
    add_derived_break,
    load_pagination_file,
    mark_all_unvalidated,
    save_pagination_file,
)
from gmbinder_semantic import (  # noqa: E402
    all_blocks_from_guide,
    candidate_break_keys_for_overflow,
    split_h1_chapters,
)

MASTER = ROOT / "dawn-of-the-jedaii-campaign-guide.md"
PAGINATION = ROOT / "tools" / "gmbinder_pagination.json"
SCAN_JS = ROOT / "tools" / "gmbinder_browser_scan.js"
OPT_LOG = ROOT / "reports" / "audits" / "gmbinder-pagination-optimization-log.json"


def guide_hash() -> str:
    return hashlib.sha256(MASTER.read_bytes()).hexdigest()


def block_key_to_break(blocks, key: str) -> tuple[str, str, str] | None:
    for b in blocks:
        if b.key == key:
            return b.chapter, b.heading_line, b.key
    return None


def choose_break_from_finding(
    finding,
    blocks,
) -> tuple[str, str, str] | None:
    keys = candidate_break_keys_for_overflow(
        blocks,
        finding.gmb_src,
        finding.nearest_heading or finding.text_excerpt,
    )
    for key in keys:
        hit = block_key_to_break(blocks, key)
        if hit:
            return hit
    # Fallback: map nearest heading across all blocks
    if finding.nearest_heading or finding.text_excerpt:
        from gmbinder_semantic import resolve_heading_from_rendered

        hit = resolve_heading_from_rendered(
            blocks, finding.nearest_heading, finding.text_excerpt
        )
        if hit:
            return hit
    return None


def regenerate(koorivar: Path, pagination_data: dict[str, Any]) -> str:
    breaks = [
        {
            "id": b["id"],
            "chapter": b["chapter"],
            "before_heading": b["before_heading"],
            "break": b["directive"],
            "rationale": b.get("reason", ""),
        }
        for b in pagination_data.get("breaks", [])
    ]
    text, _ = gen.build_document(koorivar, breaks, inject_trace_markers_flag=True)
    gen.OUT.parent.mkdir(parents=True, exist_ok=True)
    gen.OUT.write_text(text, encoding="utf-8")
    return text


def load_scan_js() -> str:
    js = SCAN_JS.read_text(encoding="utf-8")
    return f"({js})({{tolerance: {DEFAULT_TOLERANCE_PX}}})"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--scan-json", type=Path, help="Use existing scan instead of browser")
    p.add_argument("--reset-derived", action="store_true", help="Clear derived breaks; keep pinned only")
    p.add_argument("--max-iterations", type=int, default=80)
    p.add_argument("--dry-run", action="store_true", help="Plan only; do not write pagination")
    p.add_argument("--offline", action="store_true", help="Offline mode: analyze scan-json only")
    return p.parse_args(argv)


def optimize_offline(scan_path: Path, pagination_data: dict[str, Any], max_iter: int) -> dict[str, Any]:
    """Single-pass offline: propose one break from scan (for CI / manual loop)."""
    blocks = all_blocks_from_guide(MASTER.read_text(encoding="utf-8"))
    scan = json.loads(scan_path.read_text(encoding="utf-8"))
    log: dict[str, Any] = {"iterations": [], "guide_hash": guide_hash()}
    for i in range(max_iter):
        analyses, findings = analyze_document_scan(scan)
        fp = first_failing_page(analyses)
        if not fp:
            log["iterations"].append({"iteration": i, "action": "done", "overflow_total": len(findings)})
            break
        fo = first_overflow_finding(findings)
        if not fo:
            break
        choice = choose_break_from_finding(fo, blocks)
        if not choice:
            log["iterations"].append(
                {
                    "iteration": i,
                    "action": "blocked",
                    "reason": "no semantic mapping",
                    "finding": fo.text_excerpt,
                }
            )
            break
        chapter, heading, bkey = choice
        add_derived_break(
            pagination_data,
            chapter=chapter,
            before_heading=heading,
            before_block_key=bkey,
            reason=f"geometry overflow page {fo.page_index}: {fo.classification.value}",
            source_revision=guide_hash(),
            browser_validated=False,
        )
        log["iterations"].append(
            {
                "iteration": i,
                "action": "add_break",
                "chapter": chapter,
                "before_heading": heading,
                "before_block_key": bkey,
                "overflow_before": len(findings),
            }
        )
        # Offline cannot re-render; stop after one proposed break per invocation
        break
    return log


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    koorivar = gen.resolve_koorivar_path(None)
    pagination_data = load_pagination_file(PAGINATION)

    if args.reset_derived:
        pagination_data["breaks"] = [
            b for b in pagination_data.get("breaks", []) if b.get("selection_method") == "pinned"
        ]
        mark_all_unvalidated(pagination_data)

    if args.offline:
        if not args.scan_json:
            print("--scan-json required for --offline", file=sys.stderr)
            return 2
        log = optimize_offline(args.scan_json, pagination_data, args.max_iterations)
        if not args.dry_run:
            save_pagination_file(pagination_data, PAGINATION)
            regenerate(koorivar, pagination_data)
        OPT_LOG.parent.mkdir(parents=True, exist_ok=True)
        OPT_LOG.write_text(json.dumps(log, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(log, indent=2))
        return 0

    print("Browser-integrated optimization requires scan JSON from disposable preview.", file=sys.stderr)
    print("Run browser scan, then:", file=sys.stderr)
    print("  python tools/optimize_gmbinder_pagination.py --offline --scan-json <path>", file=sys.stderr)
    print("  python tools/md_to_gmbinder.py --no-backup", file=sys.stderr)
    print("  reload preview and repeat until overflow_total is 0", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
