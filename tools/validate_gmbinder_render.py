#!/usr/bin/env python3
"""Validate GM Binder rendered layout from browser geometry scans."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from gmbinder_geometry import (  # noqa: E402
    DEFAULT_TOLERANCE_PX,
    PageStatus,
    analyze_document_scan,
    deduplicate_overflow_findings,
    first_failing_page,
    first_overflow_finding,
    overflow_metrics,
)
from gmbinder_pagination_io import load_pagination_file  # noqa: E402
from gmbinder_semantic import all_blocks_from_guide, split_h1_chapters  # noqa: E402

MASTER = ROOT / "dawn-of-the-jedaii-campaign-guide.md"
GMB_OUT = ROOT / "gmbinder" / "dawn-of-the-jedaii-gmbinder.md"
PAGINATION = ROOT / "tools" / "gmbinder_pagination.json"
DEFAULT_REPORT = ROOT / "reports" / "audits" / "gmbinder-render-validation.json"
SCAN_JS = ROOT / "tools" / "gmbinder_browser_scan.js"


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def static_preflight(gmb_text: str, pagination_path: Path) -> list[str]:
    errors: list[str] = []
    if re.search(r"(?m)^\\page\s*$", gmb_text):
        errors.append("standalone legacy \\page detected")
    if re.search(r"(?m)^\\pagebreakNum\b", gmb_text):
        pass  # allowed
    unsupported = re.findall(r"(?m)^\\(pagebreak|pagebreakNum|columnbreak|page)\b", gmb_text)
    for token in unsupported:
        if token == "page":
            errors.append("legacy \\page")
    guide = MASTER.read_text(encoding="utf-8")
    chapters = {t for t, _ in split_h1_chapters(guide)}
    cfg = load_pagination_file(pagination_path)
    for b in cfg.get("breaks", []):
        ch = b["chapter"]
        if ch not in chapters:
            errors.append(f"break {b['id']}: chapter not in guide: {ch!r}")
        heading = b["before_heading"]
        count = sum(
            1
            for t, body in split_h1_chapters(guide)
            if t == ch and heading in body.splitlines()
        )
        if count != 1:
            errors.append(f"break {b['id']}: heading match count {count} for {heading!r}")
    return errors


def build_report(
    scan: dict[str, Any],
    *,
    gmb_hash: str,
    guide_hash: str,
    pagination_path: Path,
    tolerance: float,
    browser_note: str = "",
) -> dict[str, Any]:
    analyses, findings = analyze_document_scan(scan, tolerance=tolerance)
    fail_pages = [a for a in analyses if a.status not in {
        PageStatus.PASS_NO_CLIPPING,
        PageStatus.PASS_NO_CLIPPING_WITH_JUSTIFIED_WHITESPACE,
        PageStatus.WARNING_UNDERFILLED,
    }]
    first_fail = first_failing_page(analyses)
    first_of = first_overflow_finding(findings)
    cfg = load_pagination_file(pagination_path)

    page_summaries = []
    for a in analyses:
        page_summaries.append(
            {
                "page_index": a.page_index,
                "status": a.status.value,
                "overflow_count": len(a.overflow_findings),
                "occupancy_ratio": a.occupancy_ratio,
                "bounds": {
                    "left": a.left,
                    "right": a.right,
                    "top": a.top,
                    "bottom": a.bottom,
                },
            }
        )

    overflow_records = []
    for f in findings[:500]:
        overflow_records.append(
            {
                "page_index": f.page_index,
                "classification": f.classification.value,
                "tag": f.tag,
                "text_excerpt": f.text_excerpt,
                "overflow_px": f.overflow_px,
                "overflow_direction": f.overflow_direction,
                "gmb_src": f.gmb_src,
                "nearest_heading": f.nearest_heading,
                "element": {
                    "left": f.element.left,
                    "right": f.element.right,
                    "top": f.element.top,
                    "bottom": f.element.bottom,
                },
            }
        )

    validated_breaks = [b for b in cfg.get("breaks", []) if b.get("browser_validated")]
    unvalidated_breaks = [b for b in cfg.get("breaks", []) if not b.get("browser_validated")]
    metrics = overflow_metrics(findings)

    overall_pass = (
        metrics["raw_overflow_count"] == 0
        and len(fail_pages) == 0
        and not unvalidated_breaks
    )

    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_revision": {
            "guide_sha256": guide_hash,
            "gmbinder_sha256": gmb_hash,
        },
        "browser": {
            "note": browser_note,
            "page_selector": scan.get("page_selector", ".phb"),
            "content_selectors": scan.get("content_selectors"),
            "tolerance_px": tolerance,
            "page_count": scan.get("page_count"),
        },
        "static_preflight_errors": [],
        "overall_pass": overall_pass,
        "first_failing_page_index": first_fail.page_index if first_fail else None,
        "first_overflow": (
            {
                "page_index": first_of.page_index,
                "classification": first_of.classification.value,
                "gmb_src": first_of.gmb_src,
                "nearest_heading": first_of.nearest_heading,
                "text_excerpt": first_of.text_excerpt,
            }
            if first_of
            else None
        ),
        "pages": page_summaries,
        "overflow_elements": overflow_records,
        "overflow_total": metrics["raw_overflow_count"],
        "semantic_block_overflow_total": metrics["semantic_block_overflow_count"],
        "failing_page_count": metrics["failing_page_count"],
        "active_internal_breaks": cfg.get("breaks", []),
        "browser_validated_break_count": len(validated_breaks),
        "unvalidated_break_count": len(unvalidated_breaks),
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--scan-json", type=Path, help="Browser scan JSON from gmbinder_browser_scan.js")
    p.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    p.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE_PX)
    p.add_argument("--static-only", action="store_true")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    gmb_hash = file_sha256(GMB_OUT) if GMB_OUT.is_file() else ""
    guide_hash = file_sha256(MASTER) if MASTER.is_file() else ""
    gmb_text = GMB_OUT.read_text(encoding="utf-8") if GMB_OUT.is_file() else ""
    static_errors = static_preflight(gmb_text, PAGINATION)

    if args.static_only:
        report = {
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "static_only": True,
            "static_preflight_errors": static_errors,
            "overall_pass": not static_errors,
        }
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"Static preflight: {len(static_errors)} error(s)")
        for e in static_errors:
            print(f"  - {e}")
        return 0 if not static_errors else 1

    if not args.scan_json or not args.scan_json.is_file():
        print("ERROR: --scan-json required (run browser scan first)", file=sys.stderr)
        print(f"Scan script: {SCAN_JS}", file=sys.stderr)
        return 2

    scan = json.loads(args.scan_json.read_text(encoding="utf-8"))
    report = build_report(
        scan,
        gmb_hash=gmb_hash,
        guide_hash=guide_hash,
        pagination_path=PAGINATION,
        tolerance=args.tolerance,
        browser_note="scan-json input",
    )
    report["static_preflight_errors"] = static_errors
    if static_errors:
        report["overall_pass"] = False

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Report: {args.report}")
    print(f"Pages: {report['browser']['page_count']}")
    print(f"Overflow total: {report['overflow_total']}")
    print(f"Failing pages: {report['failing_page_count']}")
    print(f"Overall pass: {report['overall_pass']}")
    return 0 if report["overall_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
