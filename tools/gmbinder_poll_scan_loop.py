#!/usr/bin/env python3
"""Poll for new CDP scan logs and run gmbinder_process_latest_scan.py."""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = Path.home() / ".cursor" / "browser-logs"
SCAN = ROOT / "reports" / "audits" / "gmbinder-render-scan.json"
REPORT = ROOT / "reports" / "audits" / "gmbinder-render-validation.json"
PAGINATION = ROOT / "tools" / "gmbinder_pagination.json"


def latest_log() -> Path | None:
    logs = sorted(LOG_DIR.glob("cdp-response-Runtime.evaluate-*.json"), key=lambda p: p.stat().st_mtime)
    return logs[-1] if logs else None


def score_overflow() -> int:
    sys.path.insert(0, str(ROOT / "tools"))
    from gmbinder_auto_optimize import score_scan

    return score_scan(json.loads(SCAN.read_text(encoding="utf-8")))["raw_overflow_count"]


def process_step(log: Path) -> dict:
    subprocess.check_call(
        [sys.executable, str(ROOT / "tools" / "extract_cdp_scan.py"), str(log), str(SCAN)],
    )
    r = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "gmbinder_optimize_step.py"), "--scan-json", str(SCAN)],
        capture_output=True,
        text=True,
    )
    if not r.stdout.strip():
        raise RuntimeError(r.stderr or "optimize step produced no output")
    return json.loads(r.stdout)


def main() -> int:
    max_iter = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    wait_secs = float(sys.argv[2]) if len(sys.argv) > 2 else 120.0
    start_overflow = score_overflow()
    last_log = latest_log()
    last_mtime = last_log.stat().st_mtime if last_log else 0.0
    iterations = 0
    last_action = "none"
    deadline = time.time() + wait_secs

    while iterations < max_iter and time.time() < deadline:
        log = latest_log()
        if not log or log.stat().st_mtime <= last_mtime:
            time.sleep(2)
            continue
        last_mtime = log.stat().st_mtime
        iterations += 1
        step = process_step(log)
        last_action = step.get("action", "unknown")
        print(json.dumps({"iteration": iterations, "action": last_action, "log": log.name}), flush=True)
        if last_action == "done":
            subprocess.check_call(
                [sys.executable, str(ROOT / "tools" / "gmbinder_auto_optimize.py"), "finalize-pass"]
            )
            break
        if last_action in {"stalled", "blocked"}:
            pag = json.loads(PAGINATION.read_text(encoding="utf-8"))
            seed = next(
                (b["id"] for b in pag.get("breaks", []) if b.get("selection_method") == "unvalidated_seed"),
                None,
            )
            if seed:
                subprocess.check_call(
                    [
                        sys.executable,
                        str(ROOT / "tools" / "gmbinder_auto_optimize.py"),
                        "apply",
                        "--kind",
                        "remove_break",
                        "--break-id",
                        seed,
                    ]
                )
                continue
            break

    end_overflow = score_overflow()
    pag = json.loads(PAGINATION.read_text(encoding="utf-8"))
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "validate_gmbinder_render.py"), "--scan-json", str(SCAN)],
        check=False,
    )
    report = json.loads(REPORT.read_text(encoding="utf-8")) if REPORT.is_file() else {}
    print(
        json.dumps(
            {
                "iterations": iterations,
                "start_overflow": start_overflow,
                "end_overflow": end_overflow,
                "break_count": len(pag.get("breaks", [])),
                "overall_pass": report.get("overall_pass", False),
                "last_action": last_action,
                "blocked": last_action not in {"done"} and not report.get("overall_pass"),
            },
            indent=2,
        )
    )
    return 0 if report.get("overall_pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
