#!/usr/bin/env python3
"""One browser-assisted pagination iteration: extract CDP log, validate, apply step."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = Path.home() / ".cursor" / "browser-logs"
SCAN = ROOT / "reports" / "audits" / "gmbinder-render-scan.json"
REPORT = ROOT / "reports" / "audits" / "gmbinder-render-validation.json"
GMB = ROOT / "gmbinder" / "dawn-of-the-jedaii-gmbinder.md"


def latest_cdp() -> Path | None:
    if not LOG_DIR.is_dir():
        return None
    logs = sorted(LOG_DIR.glob("cdp-response-Runtime.evaluate-*.json"), key=lambda p: p.stat().st_mtime)
    return logs[-1] if logs else None


def main() -> int:
    log = latest_cdp()
    if not log:
        print(json.dumps({"error": "no cdp log"}))
        return 2
    subprocess.check_call(
        [sys.executable, str(ROOT / "tools" / "extract_cdp_scan.py"), str(log), str(SCAN)]
    )
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "validate_gmbinder_render.py"), "--scan-json", str(SCAN)],
        check=False,
    )
    r = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "gmbinder_optimize_step.py"), "--scan-json", str(SCAN)],
        capture_output=True,
        text=True,
    )
    step = json.loads(r.stdout) if r.stdout.strip().startswith("{") else {"raw": r.stdout}
    report = json.loads(REPORT.read_text(encoding="utf-8")) if REPORT.is_file() else {}
    out = {
        "cdp_log": str(log),
        "step": step,
        "overflow_total": report.get("overflow_total"),
        "failing_pages": report.get("failing_page_count"),
        "overall_pass": report.get("overall_pass"),
        "page_count": report.get("browser", {}).get("page_count"),
        "gmb_hash": hashlib.sha256(GMB.read_bytes()).hexdigest() if GMB.is_file() else None,
    }
    print(json.dumps(out, indent=2))
    return 0 if step.get("action") in {"applied", "removed_break", "done"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
