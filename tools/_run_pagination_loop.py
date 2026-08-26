#!/usr/bin/env python3
"""Temporary pagination loop runner (CDP + gmbinder_one_iteration)."""

from __future__ import annotations

import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import websocket

ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = Path.home() / ".cursor" / "browser-logs"
PAGINATION = ROOT / "tools" / "gmbinder_pagination.json"
RELOAD_SCAN = r"""(async () => {
  const t = await (await fetch("http://127.0.0.1:8765/dawn-of-the-jedaii-gmbinder.md")).text();
  const e = ace.edit(document.querySelector('.ace_editor')); e.setValue(t,-1); e.clearSelection();
  await new Promise(r=>setTimeout(r,3500));
  return { reloaded: true, bytes: t.length };
})()"""

SCAN_ONLY = r"""(function(){
  const scanFn=(function(o){const T=(o&&o.tolerance)||2;const sel="h1,h2,h3,h4,h5,h6,p,li,td,th,blockquote,table,pre,code,.note,.descriptive,.spell,.monster,.classFeature";function nh(el){let n=el;while(n&&n!==document.body){if(/^H[1-6]$/.test(n.tagName))return(n.innerText||"").trim();n=n.previousElementSibling||n.parentElement}return null}function gs(el){if(el.getAttribute&&el.getAttribute("data-gmb-src"))return el.getAttribute("data-gmb-src");const m=el.closest?el.closest("[data-gmb-src]"):null;if(m)return m.getAttribute("data-gmb-src");let p=el.previousElementSibling;while(p){if(p.getAttribute&&p.getAttribute("data-gmb-src"))return p.getAttribute("data-gmb-src");p=p.previousElementSibling}return null}const pages=Array.from(document.querySelectorAll(".phb"));const out=[];pages.forEach((page,i)=>{const pr=page.getBoundingClientRect();const bounds={left:pr.left,right:pr.right,top:pr.top,bottom:pr.bottom,width:pr.width,height:pr.height};const elements=[];for(const el of Array.from(page.querySelectorAll(sel))){const r=el.getBoundingClientRect();if(r.width===0&&r.height===0)continue;const text=(el.innerText||"").trim().replace(/\s+/g," ");if(!text)continue;elements.push({tag:el.tagName,text:text.slice(0,200),left:r.left,right:r.right,top:r.top,bottom:r.bottom,gmb_src:gs(el),nearest_heading:nh(el)})}out.push({page_index:i,bounds,elements})});return{scanned_at:new Date().toISOString(),page_selector:".phb",content_selectors:sel,tolerance_px:T,page_count:pages.length,pages:out}});return scanFn({tolerance:2});
})()"""


def cdp_targets() -> list[dict]:
    with urllib.request.urlopen("http://127.0.0.1:9334/json/list", timeout=5) as r:
        return json.loads(r.read().decode())


GMB_PAGE = "https://editor.gmbinder.com/documents/edit/-P-z1_qX839q83W58N1m"


def cdp_send(ws_url: str, method: str, params: dict | None = None) -> dict:
    ws = websocket.create_connection(ws_url, timeout=900, suppress_origin=True)
    msg_id = 1
    ws.send(json.dumps({"id": msg_id, "method": method, "params": params or {}}))
    while True:
        data = json.loads(ws.recv())
        if data.get("id") == msg_id:
            ws.close()
            return data
    raise RuntimeError(f"CDP {method} failed")


def cdp_eval(ws_url: str, expression: str) -> dict:
    ws = websocket.create_connection(ws_url, timeout=900, suppress_origin=True)
    msg_id = 1
    ws.send(
        json.dumps(
            {
                "id": msg_id,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": expression,
                    "awaitPromise": True,
                    "returnByValue": True,
                },
            }
        )
    )
    while True:
        data = json.loads(ws.recv())
        if data.get("id") == msg_id:
            ws.close()
            return data
    raise RuntimeError("CDP evaluate failed")


def save_cdp_log(scan: dict) -> Path:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y-%m-%dT%H-%M-%S", time.gmtime()) + f"-{int(time.time() * 1000) % 1000:03d}Z"
    path = LOG_DIR / f"cdp-response-Runtime.evaluate-{ts}.json"
    path.write_text(json.dumps({"result": {"type": "object", "value": scan}}, indent=2) + "\n", encoding="utf-8")
    return path


def main() -> int:
    targets = cdp_targets()
    page = next(
        (t for t in targets if "editor.gmbinder.com/documents/edit" in t.get("url", "") and t.get("type") == "page"),
        None,
    )
    if not page:
        page = next(
            (t for t in targets if "gmbinder.com" in t.get("url", "") and t.get("type") == "page"),
            None,
        )
    if not page:
        page = next((t for t in targets if t.get("type") == "page"), targets[0])
    ws_url = page["webSocketDebuggerUrl"]
    if GMB_PAGE not in page.get("url", ""):
        cdp_send(ws_url, "Page.navigate", {"url": GMB_PAGE})
        for _ in range(12):
            time.sleep(5)
            chk = cdp_eval(
                ws_url,
                "({url:location.href,hasAce:!!document.querySelector('.ace_editor')})()",
            )
            val = chk.get("result", {}).get("result", {}).get("value") or {}
            if val.get("hasAce"):
                break

    pag = json.loads(PAGINATION.read_text(encoding="utf-8"))
    start_breaks = len([b for b in pag.get("breaks", []) if not b.get("obsolete")])

    start_overflow: int | None = None
    end_overflow: int | None = None
    end_failing: int | None = None
    overall_pass = False
    iterations = 0
    stalled_streak = 0
    last_breaks_added: list[str] = []
    stop_reason = "max_iter"

    for i in range(1, 51):
        iterations = i
        resp = cdp_eval(ws_url, RELOAD_SCAN)
        if "exceptionDetails" in resp:
            print(json.dumps({"error": "cdp_reload_exception", "iteration": i, "details": resp["exceptionDetails"]}))
            stop_reason = "cdp_error"
            break
        reload_val = resp.get("result", {}).get("result", {}).get("value")
        if not isinstance(reload_val, dict) or not reload_val.get("reloaded"):
            print(json.dumps({"error": "bad_reload", "iteration": i, "value": reload_val}))
            stop_reason = "bad_reload"
            break
        resp = cdp_eval(ws_url, SCAN_ONLY)
        if "exceptionDetails" in resp:
            print(json.dumps({"error": "cdp_exception", "iteration": i, "details": resp["exceptionDetails"]}))
            stop_reason = "cdp_error"
            break
        value = resp.get("result", {}).get("result", {}).get("value")
        if not isinstance(value, dict) or "page_count" not in value:
            print(json.dumps({"error": "bad_scan", "iteration": i, "value": value}))
            stop_reason = "bad_scan"
            break
        save_cdp_log(value)

        r = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "gmbinder_one_iteration.py")],
            capture_output=True,
            text=True,
        )
        try:
            out = json.loads(r.stdout)
        except json.JSONDecodeError:
            print(json.dumps({"error": "bad_iteration_output", "iteration": i, "stdout": r.stdout, "stderr": r.stderr}))
            stop_reason = "iteration_error"
            break

        overflow = out.get("overflow_total")
        failing = out.get("failing_pages")
        overall_pass = bool(out.get("overall_pass"))
        action = out.get("step", {}).get("action")
        if start_overflow is None:
            start_overflow = overflow
        end_overflow = overflow
        end_failing = failing

        cand = out.get("step", {}).get("candidate") or {}
        if action == "applied" and cand.get("kind") == "add_break":
            heading = cand.get("before_heading")
            if heading:
                last_breaks_added.append(heading)
            stalled_streak = 0
        elif action == "stalled":
            stalled_streak += 1
        else:
            stalled_streak = 0

        print(
            json.dumps(
                {
                    "iteration": i,
                    "action": action,
                    "overflow_total": overflow,
                    "failing_pages": failing,
                    "overall_pass": overall_pass,
                    "stalled_streak": stalled_streak,
                }
            ),
            flush=True,
        )

        if overall_pass or overflow == 0 or action == "done":
            stop_reason = "pass" if overall_pass else ("zero_overflow" if overflow == 0 else "done")
            break
        if stalled_streak >= 3:
            stop_reason = "stalled_x3"
            break

    end_breaks = len(
        [b for b in json.loads(PAGINATION.read_text(encoding="utf-8")).get("breaks", []) if not b.get("obsolete")]
    )
    summary = {
        "iterations": iterations,
        "start_overflow": start_overflow,
        "end_overflow": end_overflow,
        "end_failing_pages": end_failing,
        "overall_pass": overall_pass,
        "break_count": end_breaks,
        "breaks_added_this_run": end_breaks - start_breaks,
        "last_10_breaks_added": last_breaks_added[-10:],
        "stop_reason": stop_reason,
    }
    print("SUMMARY:" + json.dumps(summary, indent=2))
    return 0 if overall_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
