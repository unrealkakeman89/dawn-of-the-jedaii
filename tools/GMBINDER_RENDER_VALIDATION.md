# GM Binder rendered-layout validation workflow

Geometry-based pagination for `gmbinder/dawn-of-the-jedaii-gmbinder.md`. Campaign prose in `dawn-of-the-jedaii-campaign-guide.md` is never edited for layout.

## Root cause

GM Binder uses CSS multi-column layout inside `.phb` page containers. Overflow can create a **third column** beyond the printable page edge. DOM presence, heading counts, and markdown length do **not** prove correct pagination. Only **rendered bounding rectangles** in the disposable browser preview are acceptable evidence.

## Tools

| Tool | Purpose |
|------|---------|
| `tools/gmbinder_browser_scan.js` | Browser scan: page bounds + content element rects |
| `tools/gmbinder_geometry.py` | Pure-Python overflow classification |
| `tools/gmbinder_semantic.py` | Semantic block keys + trace markers |
| `tools/gmbinder_pagination_io.py` | v2 pagination schema (pinned / derived / seeds) |
| `tools/validate_gmbinder_render.py` | Static preflight + scan → JSON report |
| `tools/run_gmbinder_pagination_session.py` | Reset seeds, extract CDP scan, process one break |
| `tools/gmbinder_cdp_step.py` | CDP log → validate + add one derived break |
| `tools/gmbinder_cors_server.py` | Local CORS server to reload GMB into preview |
| `tools/gmbinder_console_scan.py` | Print DevTools console helper |
| `tools/md_to_gmbinder.py` | Regenerate GMB (trace markers + pagination) |

## Discovered selectors (live preview, 2026-08-26)

- **Physical page:** `.phb` (~840×1085 px; left/right ~1005–1845 in test viewport)
- **Content measured:** `h1–h6, p, li, td, th, blockquote, table, pre, code, .note, .descriptive, .spell, .monster, .classFeature`
- **Tolerance:** `2px` (`DEFAULT_TOLERANCE_PX` in `gmbinder_geometry.py`)
- **Trace keys:** invisible `<span data-gmb-src="{chapter-slug}|h{level}|{heading-slug}">` injected at GMB generation only

## Iterative loop (disposable preview only)

1. **Regenerate** (after pagination change):
   ```bash
   python tools/md_to_gmbinder.py --no-backup
   ```

2. **Serve GMB locally** (CORS):
   ```bash
   python tools/gmbinder_cors_server.py --directory gmbinder --port 8765
   ```

3. **Load into disposable GM Binder ace editor** (DevTools or CDP):
   ```javascript
   const t = await (await fetch('http://127.0.0.1:8765/dawn-of-the-jedaii-gmbinder.md')).text();
   ace.edit(document.querySelector('.ace_editor')).setValue(t, -1);
   ```
   Wait ~3s for preview render.

4. **Scan geometry** — paste output of:
   ```bash
   python tools/gmbinder_console_scan.py
   ```
   Save clipboard JSON to `reports/audits/gmbinder-render-scan.json`.

5. **Validate + optimize one break:**
   ```bash
   python tools/validate_gmbinder_render.py --scan-json reports/audits/gmbinder-render-scan.json
   python tools/run_gmbinder_pagination_session.py process-scan --scan-json reports/audits/gmbinder-render-scan.json
   ```

6. Repeat steps 1–5 until `overflow_total == 0` and all active breaks are `browser_validated`.

## Pagination data

- `tools/gmbinder_pagination.json` v2: `breaks` (active), `seeds` (archived unverified guesses)
- Each derived break records `before_block_key`, `selection_method`, `browser_validated`, `reason`, `source_revision`
- Do **not** use standalone `\page`. Use `\pagebreak`, `\pagebreakNum` only when numbered, `\columnbreak` sparingly.

## Acceptance gate

Book passes only when:

- Full-book scan: no `FAIL_RIGHT_CLIPPING`, `FAIL_THIRD_COLUMN`, or `FAIL_BOTTOM_CLIPPING` on body content
- Machine report `reports/audits/gmbinder-render-validation.json` has `overall_pass: true`
- Every active break is browser-validated
- Saved remote GM Binder document **unchanged**

## Current status (2026-08-27)

**Publication layout remains partial / deferred.** Kakeman89 directed that automated pagination optimization stop with `overall_pass: false` (last retained scan: 115 raw overflow / 106 semantic-block overflow / 4 failing pages / 64 physical pages). Validator and pagination infrastructure remain the required tooling. Do not treat deferred overflow as resolved. Resume optimization only after integrated GM guide structure and manuscript content stabilize.

## Regression fixtures

- `tools/fixtures/gmbinder-ch04-overflow-scan.json` — third-column / late-break baseline
- `tools/fixtures/gmbinder-ch05-overflow-scan.json` — Ch05 right-edge clipping baseline

Run: `python -m unittest tools.test_gmbinder_geometry`
