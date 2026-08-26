#!/usr/bin/env python3
"""Emit CDP Runtime.evaluate expression: reload GMB from CORS + stability scan."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_JS = (ROOT / "tools" / "gmbinder_browser_scan.js").read_text(encoding="utf-8")
GMB_URL = "http://127.0.0.1:8765/dawn-of-the-jedaii-gmbinder.md"

EXPRESSION = f"""
(async () => {{
  const t = await (await fetch({json.dumps(GMB_URL)})).text();
  const ed = document.querySelector('.ace_editor');
  if (!ed) return {{ error: 'no ace editor' }};
  const e = ace.edit(ed);
  e.setValue(t, -1);
  e.clearSelection();
  await new Promise(r => setTimeout(r, 3500));
  const scanFn = {SCAN_JS};
  const s1 = scanFn({{ tolerance: 2 }});
  await new Promise(r => setTimeout(r, 1500));
  const s2 = scanFn({{ tolerance: 2 }});
  let scan = s2;
  if (s1.page_count !== s2.page_count) {{
    await new Promise(r => setTimeout(r, 2000));
    scan = scanFn({{ tolerance: 2 }});
  }}
  return {{
    ...scan,
    gmb_bytes: t.length,
    viewport: {{ width: window.innerWidth, height: window.innerHeight, dpr: window.devicePixelRatio }},
  }};
}})()
""".strip()


def main() -> None:
    out = ROOT / "reports" / "audits" / "gmbinder-cdp-reload-expression.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"expression": EXPRESSION}, indent=2) + "\n", encoding="utf-8")
    print(EXPRESSION)


if __name__ == "__main__":
    main()
