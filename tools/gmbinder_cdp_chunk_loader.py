#!/usr/bin/env python3
"""Emit chunked CDP JavaScript to load GM Binder markdown into ace editor."""

from __future__ import annotations

import argparse
import base64
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GMB_OUT = ROOT / "gmbinder" / "dawn-of-the-jedaii-gmbinder.md"
SCAN_JS = ROOT / "tools" / "gmbinder_browser_scan.js"
CHUNK_SIZE = 48000


def chunk_b64(path: Path) -> list[str]:
    raw = path.read_bytes()
    b64 = base64.b64encode(raw).decode("ascii")
    return [b64[i : i + CHUNK_SIZE] for i in range(0, len(b64), CHUNK_SIZE)]


def scan_fn_js(tolerance: float = 2.0) -> str:
    return SCAN_JS.read_text(encoding="utf-8")


def build_steps(gmb_path: Path, tolerance: float = 2.0) -> list[dict[str, str]]:
    chunks = chunk_b64(gmb_path)
    steps: list[dict[str, str]] = [
        {
            "name": "init",
            "expression": "window.__gmbB64Chunks = []; window.__gmbLoadResult = null; 'init_ok';",
        }
    ]
    for i, chunk in enumerate(chunks):
        steps.append(
            {
                "name": f"chunk_{i}",
                "expression": f"window.__gmbB64Chunks.push({json.dumps(chunk)}); 'chunk_{i}_ok';",
            }
        )
    scan_src = scan_fn_js()
    assemble = f"""
(async () => {{
  const b64 = window.__gmbB64Chunks.join('');
  const binary = atob(b64);
  const bytes = Uint8Array.from(binary, c => c.charCodeAt(0));
  const text = new TextDecoder('utf-8').decode(bytes);
  const ed = document.querySelector('.ace_editor');
  if (!ed) return {{ error: 'no ace editor' }};
  const editor = ace.edit(ed);
  editor.setValue(text, -1);
  editor.clearSelection();
  await new Promise(r => setTimeout(r, 3000));
  const scanFn = {scan_src};
  const scan = scanFn({{ tolerance: {tolerance} }});
  window.__gmbLoadResult = {{ ok: true, markdown_bytes: bytes.length, scan }};
  return window.__gmbLoadResult;
}})()
"""
    steps.append({"name": "load_and_scan", "expression": assemble.strip()})
    return steps


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--gmb", type=Path, default=GMB_OUT)
    p.add_argument("--out", type=Path, default=ROOT / "reports" / "audits" / "gmbinder-cdp-steps.json")
    args = p.parse_args()
    steps = build_steps(args.gmb)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(steps, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"steps": len(steps), "out": str(args.out), "gmb_bytes": args.gmb.stat().st_size}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
