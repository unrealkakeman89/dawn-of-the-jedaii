#!/usr/bin/env python3
"""Run browser-assisted pagination optimization until terminal condition."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from gmbinder_auto_optimize import (  # noqa: E402
    apply_candidate,
    append_log,
    enumerate_candidates,
    gmb_hash,
    guide_hash,
    migrate_and_reclassify,
    initial_ch04_cleanup,
    regenerate,
    score_scan,
    compare_scores,
    CandidateAction,
)
from gmbinder_geometry import analyze_document_scan, first_overflow_finding  # noqa: E402
from gmbinder_pagination_io import (  # noqa: E402
    load_pagination_file,
    mark_all_browser_validated,
    pagination_state_hash,
    save_pagination_file,
)
from run_gmbinder_pagination_session import extract_scan_from_cdp_response, save_scan  # noqa: E402
from validate_gmbinder_render import build_report, static_preflight  # noqa: E402

MASTER = ROOT / "dawn-of-the-jedaii-campaign-guide.md"
GMB_OUT = ROOT / "gmbinder" / "dawn-of-the-jedaii-gmbinder.md"
PAGINATION = ROOT / "tools" / "gmbinder_pagination.json"
SCAN_OUT = ROOT / "reports" / "audits" / "gmbinder-render-scan.json"
REPORT_OUT = ROOT / "reports" / "audits" / "gmbinder-render-validation.json"
BLOCKED_OUT = ROOT / "reports" / "audits" / "gmbinder-pagination-blocked.json"


def write_report(scan: dict[str, Any], data: dict[str, Any]) -> dict[str, Any]:
    import hashlib

    gmb_h = hashlib.sha256(GMB_OUT.read_bytes()).hexdigest()
    guide_h = hashlib.sha256(MASTER.read_bytes()).hexdigest()
    report = build_report(
        scan,
        gmb_hash=gmb_h,
        guide_hash=guide_h,
        pagination_path=PAGINATION,
        tolerance=2.0,
        browser_note="optimization loop",
    )
    report["static_preflight_errors"] = static_preflight(
        GMB_OUT.read_text(encoding="utf-8"), PAGINATION
    )
    if report["static_preflight_errors"]:
        report["overall_pass"] = False
    report["pagination_state_hash"] = pagination_state_hash(data)
    report["gmb_output_hash"] = gmb_h
    REPORT_OUT.parent.mkdir(parents=True, exist_ok=True)
    REPORT_OUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def process_scan_step(scan_path: Path) -> dict[str, Any]:
    """Score scan and apply best single candidate (offline pick; browser verifies next iter)."""
    scan = json.loads(scan_path.read_text(encoding="utf-8"))
    data = load_pagination_file(PAGINATION)
    baseline = score_scan(scan)
    if baseline["raw_overflow_count"] == 0:
        mark_all_browser_validated(data, guide_hash())
        save_pagination_file(data, PAGINATION)
        write_report(scan, data)
        return {"action": "done", "baseline": baseline}

    candidates = enumerate_candidates(scan, data)
    if not candidates:
        fo = first_overflow_finding(analyze_document_scan(scan)[1])
        blocked = {
            "page_index": fo.page_index if fo else None,
            "classification": fo.classification.value if fo else None,
            "text": fo.text_excerpt if fo else None,
            "reason": "no candidates",
        }
        BLOCKED_OUT.write_text(json.dumps(blocked, indent=2) + "\n", encoding="utf-8")
        return {"action": "blocked", "baseline": baseline, "blocked": blocked}

    add_candidates = [
        c
        for c in candidates
        if c.kind == "add_break"
        and not any(
            b["chapter"] == c.chapter and b["before_heading"] == c.before_heading
            for b in data.get("breaks", [])
        )
    ]

    state_hashes: set[str] = {pagination_state_hash(data)}
    for c in add_candidates:
        try:
            branch = apply_candidate(data, c)
        except RuntimeError:
            continue
        h = pagination_state_hash(branch)
        if h in state_hashes:
            continue
        save_pagination_file(branch, PAGINATION)
        regenerate(branch)
        entry = {
            "action": "applied",
            "candidate": c.__dict__,
            "baseline": baseline,
            "state_hash": h,
            "gmb_hash": gmb_hash(),
        }
        append_log(entry)
        return entry

    # Never remove breaks without a browser-rescan improvement (simplification pass only).
    return {"action": "stalled", "baseline": baseline, "candidate_count": len(candidates)}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--scan-json", type=Path, required=True)
    args = p.parse_args()
    result = process_scan_step(args.scan_json)
    print(json.dumps(result, indent=2))
    return 0 if result.get("action") in {"applied", "removed_break", "done"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
