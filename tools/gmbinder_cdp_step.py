#!/usr/bin/env python3
"""Extract latest CDP scan log and run one pagination optimization step."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_gmbinder_pagination_session import (  # noqa: E402
    extract_scan_from_cdp_response,
    process_scan_add_break,
    save_scan,
    write_validation_report,
)

SCAN_OUT = ROOT / "reports" / "audits" / "gmbinder-render-scan.json"
REPORT_OUT = ROOT / "reports" / "audits" / "gmbinder-render-validation.json"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: gmbinder_cdp_step.py <cdp-response.json>", file=sys.stderr)
        return 2
    cdp_path = Path(sys.argv[1])
    scan = extract_scan_from_cdp_response(cdp_path)
    save_scan(scan, SCAN_OUT)
    report = write_validation_report(SCAN_OUT, REPORT_OUT)
    result = process_scan_add_break(scan)
    print(json.dumps({"validation": {"overflow_total": report["overflow_total"], "failing_pages": report["failing_page_count"]}, "step": result}, indent=2))
    return 0 if result.get("action") in {"added_break", "done"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
