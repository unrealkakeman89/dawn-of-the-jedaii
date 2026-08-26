/**
 * Reload GMB markdown from local CORS server and scan rendered layout.
 * Served at http://127.0.0.1:8765/reload_and_scan.js for CDP evaluation.
 */
(async function gmbinderReloadAndScan() {
  const GMB = "http://127.0.0.1:8765/dawn-of-the-jedaii-gmbinder.md";
  const SCAN_URL = "http://127.0.0.1:8765/gmbinder_browser_scan.js";

  const t = await (await fetch(GMB)).text();
  const ed = document.querySelector(".ace_editor");
  if (!ed) return { error: "no ace editor" };
  const e = ace.edit(ed);
  e.setValue(t, -1);
  e.clearSelection();
  await new Promise((r) => setTimeout(r, 3500));

  const scanSrc = await (await fetch(SCAN_URL)).text();
  const scanFn = new Function("return " + scanSrc.trim())();
  const s1 = scanFn({ tolerance: 2 });
  await new Promise((r) => setTimeout(r, 1500));
  const s2 = scanFn({ tolerance: 2 });
  if (s1.page_count !== s2.page_count) {
    await new Promise((r) => setTimeout(r, 2000));
    return scanFn({ tolerance: 2 });
  }
  return {
    ...s2,
    gmb_bytes: t.length,
    gmb_sha256_prefix: null,
    viewport: { width: window.innerWidth, height: window.innerHeight, zoom: window.devicePixelRatio },
  };
})();
