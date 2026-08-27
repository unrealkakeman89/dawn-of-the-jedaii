#!/usr/bin/env python3
"""Orchestrate GM Binder pagination optimization from browser scan JSON."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import md_to_gmbinder as gen  # noqa: E402
from gmbinder_geometry import analyze_document_scan, first_failing_page, first_overflow_finding  # noqa: E402
from gmbinder_pagination_io import (  # noqa: E402
    add_derived_break,
    archive_seeds_from_breaks,
    load_pagination_file,
    save_pagination_file,
)
from gmbinder_render_loop import regenerate_from_pagination  # noqa: E402
from gmbinder_semantic import all_blocks_from_guide, candidate_break_keys_for_overflow  # noqa: E402
from optimize_gmbinder_pagination import block_key_to_break, choose_break_from_finding  # noqa: E402
from validate_gmbinder_render import build_report, static_preflight  # noqa: E402

MASTER = ROOT / "dawn-of-the-jedaii-campaign-guide.md"
GMB_OUT = ROOT / "gmbinder" / "dawn-of-the-jedaii-gmbinder.md"
PAGINATION = ROOT / "tools" / "gmbinder_pagination.json"
SCAN_JS = ROOT / "tools" / "gmbinder_browser_scan.js"
DEFAULT_SCAN = ROOT / "reports" / "audits" / "gmbinder-render-scan.json"
DEFAULT_REPORT = ROOT / "reports" / "audits" / "gmbinder-render-validation.json"
OPT_LOG = ROOT / "reports" / "audits" / "gmbinder-pagination-optimization-log.json"


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_scan_from_cdp_response(cdp_path: Path) -> dict[str, Any]:
    data = json.loads(cdp_path.read_text(encoding="utf-8"))
    return data["result"]["value"]


def save_scan(scan: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(scan, indent=2) + "\n", encoding="utf-8")


def cdp_load_and_scan_js(gmb_path: Path, tolerance: float = 2.0) -> str:
    """Return JS IIFE: set ace editor from base64, wait, scan, return scan object."""
    raw = gmb_path.read_bytes()
    b64 = base64.b64encode(raw).decode("ascii")
    scan_src = SCAN_JS.read_text(encoding="utf-8")
    return f"""
(async () => {{
  const b64 = {json.dumps(b64)};
  const binary = atob(b64);
  const bytes = Uint8Array.from(binary, c => c.charCodeAt(0));
  const text = new TextDecoder('utf-8').decode(bytes);
  const ed = document.querySelector('.ace_editor');
  if (!ed) return {{ error: 'no ace editor' }};
  const editor = ace.edit(ed);
  editor.setValue(text, -1);
  editor.clearSelection();
  await new Promise(r => setTimeout(r, 2500));
  const scanFn = {scan_src};
  const scan = scanFn({{ tolerance: {tolerance} }});
  return {{ ok: true, markdown_bytes: bytes.length, scan }};
}})()
"""


def cdp_scan_only_js(tolerance: float = 2.0) -> str:
    scan_src = SCAN_JS.read_text(encoding="utf-8")
    return f"({scan_src})({{ tolerance: {tolerance} }})"


def all_choices_from_finding(finding, blocks) -> list[tuple[str, str, str]]:
    keys = candidate_break_keys_for_overflow(
        blocks, finding.gmb_src, finding.nearest_heading or finding.text_excerpt
    )
    out: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    for key in keys:
        hit = block_key_to_break(blocks, key)
        if hit and hit[2] not in seen:
            out.append(hit)
            seen.add(hit[2])
    fallback = choose_break_from_finding(finding, blocks)
    if fallback and fallback[2] not in seen:
        out.append(fallback)
    return out


def process_scan_add_break(scan: dict[str, Any], *, validate_only: bool = False) -> dict[str, Any]:
    blocks = all_blocks_from_guide(MASTER.read_text(encoding="utf-8"))
    analyses, findings = analyze_document_scan(scan)
    fp = first_failing_page(analyses)
    if not fp:
        return {
            "action": "done",
            "overflow_total": len(findings),
            "failing_pages": 0,
            "breaks_added": False,
        }
    fo = first_overflow_finding(findings)
    if not fo:
        return {"action": "done", "overflow_total": 0, "failing_pages": 0, "breaks_added": False}

    choices = all_choices_from_finding(fo, blocks)
    if not choices:
        return {
            "action": "blocked",
            "reason": "no semantic mapping",
            "finding": fo.text_excerpt,
            "page_index": fo.page_index,
            "classification": fo.classification.value,
        }

    data = load_pagination_file(PAGINATION)
    existing = {(b["chapter"], b["before_heading"]) for b in data.get("breaks", [])}
    tried: list[dict[str, Any]] = []

    for chapter, heading, bkey in choices:
        pair = (chapter, heading)
        if pair in existing:
            tried.append(
                {
                    "before_heading": heading,
                    "before_block_key": bkey,
                    "accepted": False,
                    "reason": "duplicate_existing_break",
                }
            )
            continue
        if validate_only:
            return {
                "action": "propose_break",
                "chapter": chapter,
                "before_heading": heading,
                "before_block_key": bkey,
                "overflow_total": len(findings),
                "first_failing_page": fp.page_index,
            }
        before_count = len(data.get("breaks", []))
        add_derived_break(
            data,
            chapter=chapter,
            before_heading=heading,
            before_block_key=bkey,
            reason=f"rendered geometry page {fo.page_index}: {fo.classification.value}",
            source_revision=file_sha256(MASTER),
            browser_validated=False,
        )
        after_count = len(data.get("breaks", []))
        if after_count > before_count:
            save_pagination_file(data, PAGINATION)
            regenerate_from_pagination()
            tried.append(
                {
                    "before_heading": heading,
                    "before_block_key": bkey,
                    "accepted": True,
                    "reason": "added_derived_break",
                }
            )
            return {
                "action": "added_break",
                "chapter": chapter,
                "before_heading": heading,
                "before_block_key": bkey,
                "overflow_before": len(findings),
                "first_failing_page": fp.page_index,
                "first_overflow": fo.text_excerpt[:80],
                "classification": fo.classification.value,
                "candidates_tried": tried,
                "break_count": after_count,
            }
        tried.append(
            {
                "before_heading": heading,
                "before_block_key": bkey,
                "accepted": False,
                "reason": "add_failed",
            }
        )

    return {
        "action": "duplicate_skip_all_candidates",
        "overflow_total": len(findings),
        "first_failing_page": fp.page_index,
        "first_overflow": fo.text_excerpt[:80],
        "classification": fo.classification.value,
        "candidates_tried": tried,
        "hint": "existing breaks may be too late; consider moving earlier or adding columnbreak",
    }


def reset_pagination_seeds(*, clear_active: bool = True) -> dict[str, Any]:
    data = load_pagination_file(PAGINATION)
    archive_seeds_from_breaks(
        data,
        "Pre-geometry manual heading guesses (2026-08-26); unverified until rendered scan passes.",
    )
    if clear_active:
        data["breaks"] = []
    data["version"] = 2
    data["description"] = (
        "Generator-owned pagination. Derived breaks require rendered-layout validation "
        "(tools/validate_gmbinder_render.py)."
    )
    save_pagination_file(data, PAGINATION)
    regenerate_from_pagination()
    return {"seeds": len(data.get("seeds", [])), "active_breaks": len(data.get("breaks", []))}


def write_validation_report(scan_path: Path, report_path: Path) -> dict[str, Any]:
    scan = json.loads(scan_path.read_text(encoding="utf-8"))
    gmb_hash = file_sha256(GMB_OUT)
    guide_hash = file_sha256(MASTER)
    report = build_report(
        scan,
        gmb_hash=gmb_hash,
        guide_hash=guide_hash,
        pagination_path=PAGINATION,
        tolerance=2.0,
        browser_note="disposable GM Binder preview scan",
    )
    report["static_preflight_errors"] = static_preflight(GMB_OUT.read_text(encoding="utf-8"), PAGINATION)
    if report["static_preflight_errors"]:
        report["overall_pass"] = False
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def append_opt_log(entry: dict[str, Any]) -> None:
    OPT_LOG.parent.mkdir(parents=True, exist_ok=True)
    log: list[Any] = []
    if OPT_LOG.is_file():
        log = json.loads(OPT_LOG.read_text(encoding="utf-8"))
        if isinstance(log, dict):
            log = log.get("iterations", [])
    if not isinstance(log, list):
        log = []
    log.append(entry)
    OPT_LOG.write_text(json.dumps({"iterations": log}, indent=2) + "\n", encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "command",
        choices=[
            "reset-seeds",
            "extract-cdp",
            "process-scan",
            "validate",
            "print-cdp-load-js",
            "print-cdp-scan-js",
        ],
    )
    p.add_argument("--scan-json", type=Path, default=DEFAULT_SCAN)
    p.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    p.add_argument("--cdp-response", type=Path, help="CDP Runtime.evaluate JSON log")
    p.add_argument("--keep-breaks", action="store_true", help="reset-seeds: archive only")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.command == "reset-seeds":
        info = reset_pagination_seeds(clear_active=not args.keep_breaks)
        print(json.dumps(info, indent=2))
        return 0
    if args.command == "extract-cdp":
        if not args.cdp_response:
            print("--cdp-response required", file=sys.stderr)
            return 2
        scan = extract_scan_from_cdp_response(args.cdp_response)
        save_scan(scan, args.scan_json)
        print(f"Wrote {args.scan_json} ({scan.get('page_count')} pages)")
        return 0
    if args.command == "process-scan":
        scan = json.loads(args.scan_json.read_text(encoding="utf-8"))
        result = process_scan_add_break(scan)
        append_opt_log(result)
        print(json.dumps(result, indent=2))
        return 0 if result.get("action") != "blocked" else 1
    if args.command == "validate":
        report = write_validation_report(args.scan_json, args.report)
        print(f"Report: {args.report}")
        print(f"overflow_total={report['overflow_total']} overall_pass={report['overall_pass']}")
        return 0 if report["overall_pass"] else 1
    if args.command == "print-cdp-load-js":
        print(cdp_load_and_scan_js(GMB_OUT))
        return 0
    if args.command == "print-cdp-scan-js":
        print(cdp_scan_only_js())
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
