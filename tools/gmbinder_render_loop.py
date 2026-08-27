#!/usr/bin/env python3
"""Browser-assisted render optimization loop helpers."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import md_to_gmbinder as gen  # noqa: E402
from gmbinder_geometry import analyze_document_scan, first_failing_page, first_overflow_finding  # noqa: E402
from gmbinder_pagination_io import (  # noqa: E402
    add_derived_break,
    load_pagination_file,
    save_pagination_file,
)
from gmbinder_semantic import all_blocks_from_guide, candidate_break_keys_for_overflow  # noqa: E402
from optimize_gmbinder_pagination import block_key_to_break, choose_break_from_finding  # noqa: E402
from gmbinder_semantic import candidate_break_keys_for_overflow  # noqa: E402

MASTER = ROOT / "dawn-of-the-jedaii-campaign-guide.md"
PAGINATION = ROOT / "tools" / "gmbinder_pagination.json"
SCAN_JS = ROOT / "tools" / "gmbinder_browser_scan.js"


def guide_hash() -> str:
    return hashlib.sha256(MASTER.read_bytes()).hexdigest()


def regenerate_from_pagination() -> str:
    data = load_pagination_file(PAGINATION)
    breaks = [
        {
            "id": b["id"],
            "chapter": b["chapter"],
            "before_heading": b["before_heading"],
            "break": b["directive"],
            "rationale": b.get("reason", ""),
        }
        for b in data.get("breaks", [])
    ]
    text, _ = gen.build_document(gen.resolve_koorivar_path(None), breaks, inject_trace_markers_flag=True)
    gen.OUT.write_text(text, encoding="utf-8")
    return text


def cdp_set_editor_js(markdown_json_escaped: str) -> str:
    """JS snippet: set ace editor value from JSON string."""
    return f"""
(() => {{
  const ed = document.querySelector('.ace_editor');
  if (!ed) return {{error: 'no ace editor'}};
  const editor = ace.edit(ed);
  const text = {markdown_json_escaped};
  editor.setValue(text, -1);
  editor.clearSelection();
  return {{ok: true, len: text.length}};
}})()
"""


def cdp_scan_js() -> str:
    js = SCAN_JS.read_text(encoding="utf-8")
    return f"({js})({{tolerance: 2}})"


def _all_choices_from_finding(finding, blocks) -> list[tuple[str, str, str]]:
    keys = candidate_break_keys_for_overflow(
        blocks,
        finding.gmb_src,
        finding.nearest_heading or finding.text_excerpt,
    )
    out: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    for key in keys:
        hit = block_key_to_break(blocks, key)
        if hit and hit[2] not in seen:
            out.append(hit)
            seen.add(hit[2])
    fallback = choose_break_from_finding(finding, blocks)
    if fallback and fallback[2] not in seen:
        out.append(fallback)
    return out


def process_scan_add_one_break(scan: dict[str, Any]) -> dict[str, Any]:
    """Analyze scan; add one derived break if needed. Returns action record."""
    blocks = all_blocks_from_guide(MASTER.read_text(encoding="utf-8"))
    analyses, findings = analyze_document_scan(scan)
    fp = first_failing_page(analyses)
    if not fp:
        return {"action": "done", "overflow_total": len(findings), "breaks_added": False}
    fo = first_overflow_finding(findings)
    if not fo:
        return {"action": "done", "overflow_total": 0, "breaks_added": False}
    choices = _all_choices_from_finding(fo, blocks)
    if not choices:
        return {
            "action": "blocked",
            "reason": "no semantic mapping",
            "finding": fo.text_excerpt,
            "page_index": fo.page_index,
        }
    data = load_pagination_file(PAGINATION)
    existing = {(b["chapter"], b["before_heading"]) for b in data.get("breaks", [])}
    for chapter, heading, bkey in choices:
        if (chapter, heading) in existing:
            continue
        before = len(data.get("breaks", []))
        add_derived_break(
            data,
            chapter=chapter,
            before_heading=heading,
            before_block_key=bkey,
            reason=f"rendered geometry page {fo.page_index}: {fo.classification.value}",
            source_revision=guide_hash(),
            browser_validated=False,
        )
        after = len(data.get("breaks", []))
        if after > before:
            save_pagination_file(data, PAGINATION)
            regenerate_from_pagination()
            return {
                "action": "added_break",
                "chapter": chapter,
                "before_heading": heading,
                "before_block_key": bkey,
                "overflow_before": len(findings),
                "break_count": after,
            }
    return {
        "action": "duplicate_skip_all_candidates",
        "overflow_total": len(findings),
        "page_index": fo.page_index,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: gmbinder_render_loop.py process-scan <scan.json>", file=sys.stderr)
        raise SystemExit(2)
    cmd = sys.argv[1]
    if cmd == "process-scan":
        scan = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
        print(json.dumps(process_scan_add_one_break(scan), indent=2))
    elif cmd == "regenerate":
        regenerate_from_pagination()
        print("regenerated")
    else:
        raise SystemExit(f"unknown command {cmd}")
