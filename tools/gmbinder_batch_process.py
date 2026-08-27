#!/usr/bin/env python3
"""Run N reload-scan + optimize iterations using latest CDP log between steps.

Browser CDP reload+scan must be executed separately (MCP or DevTools) before each
call when --require-fresh-scan is set.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = Path.home() / ".cursor" / "browser-logs"


def latest_log_mtime() -> float:
    logs = sorted(LOG_DIR.glob("cdp-response-Runtime.evaluate-*.json"), key=lambda p: p.stat().st_mtime)
    return logs[-1].stat().st_mtime if logs else 0.0


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--count", type=int, default=1)
    p.add_argument("--min-log-age", type=float, default=0.0)
    args = p.parse_args()
    last_mtime = latest_log_mtime()
    results = []
    for i in range(args.count):
        mtime = latest_log_mtime()
        if mtime <= last_mtime:
            print(json.dumps({"iteration": i + 1, "error": "no fresh CDP scan log"}))
            return 2
        last_mtime = mtime
        r = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "gmbinder_one_iteration.py")],
            capture_output=True,
            text=True,
        )
        lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
        if not lines:
            print(r.stdout, r.stderr)
            return 1
        entry = json.loads(lines[-1])
        results.append(entry)
        print(json.dumps({"iteration": i + 1, **{k: entry.get(k) for k in ("overflow_total", "failing_pages", "overall_pass")}, "action": entry.get("step", {}).get("action")}))
        if entry.get("overall_pass"):
            break
        if entry.get("step", {}).get("action") == "stalled":
            break
    return 0 if results and results[-1].get("overall_pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
