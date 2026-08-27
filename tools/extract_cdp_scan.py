#!/usr/bin/env python3
"""Extract scan JSON from CDP Runtime.evaluate log file."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: extract_cdp_scan.py <cdp-log.json> [out.json]", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "reports" / "audits" / "gmbinder-render-scan.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    scan = data["result"]["value"]
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(scan, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(dst), "page_count": scan.get("page_count")}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
