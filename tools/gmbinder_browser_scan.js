/**
 * GM Binder rendered-layout scan — run in disposable preview via browser CDP or console.
 * Returns JSON-serializable geometry for tools/validate_gmbinder_render.py
 */
(function gmbinderScan(options) {
  const TOL = (options && options.tolerance) || 2;
  const selectors =
    "h1,h2,h3,h4,h5,h6,p,li,td,th,blockquote,table,pre,code,.note,.descriptive,.spell,.monster,.classFeature";

  function nearestHeading(el) {
    let node = el;
    while (node && node !== document.body) {
      if (/^H[1-6]$/.test(node.tagName)) {
        return (node.innerText || "").trim();
      }
      node = node.previousElementSibling || node.parentElement;
    }
    return null;
  }

  function gmbSrc(el) {
    if (el.getAttribute && el.getAttribute("data-gmb-src")) {
      return el.getAttribute("data-gmb-src");
    }
    const marked = el.closest ? el.closest("[data-gmb-src]") : null;
    if (marked) return marked.getAttribute("data-gmb-src");
    // Walk backwards for preceding trace marker
    let prev = el.previousElementSibling;
    while (prev) {
      if (prev.getAttribute && prev.getAttribute("data-gmb-src")) {
        return prev.getAttribute("data-gmb-src");
      }
      prev = prev.previousElementSibling;
    }
    return null;
  }

  const pages = Array.from(document.querySelectorAll(".phb"));
  const outPages = [];

  pages.forEach((page, pageIndex) => {
    const pr = page.getBoundingClientRect();
    const bounds = {
      left: pr.left,
      right: pr.right,
      top: pr.top,
      bottom: pr.bottom,
      width: pr.width,
      height: pr.height,
    };
    const elements = [];
    const nodes = Array.from(page.querySelectorAll(selectors));
    for (const el of nodes) {
      const r = el.getBoundingClientRect();
      if (r.width === 0 && r.height === 0) continue;
      const text = (el.innerText || "").trim().replace(/\s+/g, " ");
      if (!text) continue;
      elements.push({
        tag: el.tagName,
        text: text.slice(0, 200),
        left: r.left,
        right: r.right,
        top: r.top,
        bottom: r.bottom,
        gmb_src: gmbSrc(el),
        nearest_heading: nearestHeading(el),
      });
    }
    outPages.push({ page_index: pageIndex, bounds, elements });
  });

  return {
    scanned_at: new Date().toISOString(),
    page_selector: ".phb",
    content_selectors: selectors,
    tolerance_px: TOL,
    page_count: pages.length,
    pages: outPages,
  };
})
