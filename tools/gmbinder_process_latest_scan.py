#!/usr/bin/env python3
"""Process latest CDP scan log and run one optimization step."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = Path.home() / ".cursor" / "browser-logs"
SCAN = ROOT / "reports" / "audits" / "gmbinder-render-scan.json"


def latest_cdp_log() -> Path | None:
    if not LOG_DIR.is_dir():
        return None
    logs = sorted(LOG_DIR.glob("cdp-response-Runtime.evaluate-*.json"), key=lambda p: p.stat().st_mtime)
    return logs[-1] if logs else None


def main() -> int:
    log = latest_cdp_log()
    if not log:
        print("no cdp log", file=sys.stderr)
        return 2
    subprocess.check_call([sys.executable, str(ROOT / "tools" / "extract_cdp_scan.py"), str(log), str(SCAN)])
    r = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "gmbinder_optimize_step.py"), "--scan-json", str(SCAN)],
        capture_output=True,
        text=True,
    )
    print(r.stdout)
    if r.returncode != 0:
        print(r.stderr, file=sys.stderr)
    return r.returncode


if __name__ == "__main__":
    raise SystemExit(main())
