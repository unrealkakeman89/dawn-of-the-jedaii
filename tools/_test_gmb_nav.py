import json, time, urllib.request, websocket

GMB = "https://editor.gmbinder.com/documents/edit/-P-z1_qX839q83W58N1m"
targets = json.loads(urllib.request.urlopen("http://127.0.0.1:9334/json/list").read())
page = next(t for t in targets if t.get("type") == "page")
print("before", page.get("url", "")[:80])
ws = websocket.create_connection(page["webSocketDebuggerUrl"], timeout=60, suppress_origin=True)
ws.send(json.dumps({"id": 1, "method": "Page.navigate", "params": {"url": GMB}}))
while True:
    d = json.loads(ws.recv())
    if d.get("id") == 1:
        break
ws.close()
time.sleep(10)
targets = json.loads(urllib.request.urlopen("http://127.0.0.1:9334/json/list").read())
page = next(t for t in targets if t.get("type") == "page")
print("after", page.get("url", "")[:120])
ws = websocket.create_connection(page["webSocketDebuggerUrl"], timeout=60, suppress_origin=True)
expr = "(()=>({ace:!!document.querySelector('.ace_editor'),title:document.title,url:location.href}))()"
ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {"expression": expr, "returnByValue": True}}))
while True:
    d = json.loads(ws.recv())
    if d.get("id") == 2:
        print(json.dumps(d.get("result", {}).get("result", {}).get("value")))
        break
ws.close()
