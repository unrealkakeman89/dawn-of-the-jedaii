#!/usr/bin/env python3
"""Console helper: paste into disposable GM Binder preview DevTools to scan layout."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_JS = ROOT / "tools" / "gmbinder_browser_scan.js"


def main() -> None:
    js = SCAN_JS.read_text(encoding="utf-8")
    snippet = f"""// GM Binder rendered-layout scan — disposable preview only
// Run in browser console after preview stabilizes.
const result = ({js})({{ tolerance: 2 }});
copy(JSON.stringify(result, null, 2));
console.log('Scan copied to clipboard:', result.page_count, 'pages');
result;
"""
    print(snippet)


if __name__ == "__main__":
    main()
