import json, time, urllib.request, websocket

GMB = "https://editor.gmbinder.com/documents/edit/-P-z1_qX839q83W58N1m"
CORS = "http://127.0.0.1:8765/dawn-of-the-jedaii-gmbinder.md"

targets = json.loads(urllib.request.urlopen("http://127.0.0.1:9334/json/list").read())
page = next(t for t in targets if t.get("type") == "page")
print("start", page.get("url", ""))
ws = websocket.create_connection(page["webSocketDebuggerUrl"], timeout=120, suppress_origin=True)
msg = 0


def send(method, params=None, await_promise=False):
    global msg
    msg += 1
    payload = {"id": msg, "method": method, "params": params or {}}
    if method == "Runtime.evaluate":
        payload["params"].setdefault("returnByValue", True)
        if await_promise:
            payload["params"]["awaitPromise"] = True
    ws.send(json.dumps(payload))
    while True:
        d = json.loads(ws.recv())
        if d.get("id") == msg:
            return d


send("Page.navigate", {"url": GMB})
for wait in [5, 8, 12, 15, 20]:
    time.sleep(5)
    r = send(
        "Runtime.evaluate",
        {
            "expression": "({url: location.href, hasAce: !!document.querySelector('.ace_editor'), ace: typeof ace, phb: document.querySelectorAll('.phb').length})",
        },
    )
    v = r["result"]["result"]["value"]
    print(f"t+{wait}s", v)
    if v.get("hasAce"):
        break

r2 = send(
    "Runtime.evaluate",
    {
        "expression": f"""
(async () => {{
  try {{
    const t = await (await fetch({json.dumps(CORS)})).text();
    return {{fetchOk: true, len: t.length}};
  }} catch (e) {{
    return {{fetchOk: false, err: String(e)}};
  }}
}})()
""",
    },
    await_promise=True,
)
print("fetch", r2["result"]["result"].get("value"))
ws.close()
