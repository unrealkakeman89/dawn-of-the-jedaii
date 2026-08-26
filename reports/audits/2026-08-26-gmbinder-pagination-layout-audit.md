# GM Binder full-book pagination / layout audit — 2026-08-26

**Status:** Repository pagination implemented and regenerated; disposable browser after-render validation outstanding  
**Authority:** Kakeman89 authorization for this audit/implementation (no campaign prose edits; no commit/push)  
**Operational only — not campaign canon**

---

## Executive summary

Chapter 04 and other long chapters were confirmed overflowing into a clipped third column in the live GM Binder preview when only chapter-boundary breaks existed. A generator-owned pagination map (`tools/gmbinder_pagination.json`) now inserts exact-heading internal `\pagebreak` directives. Repository output regenerated with **50** `\pagebreak` lines (**30** chapter-boundary + **20** internal). No `\page`, no `\pagebreakNum`. Campaign guide, narrative companion, and Foundry world were not modified by this work. The saved remote GM Binder document was **not** overwritten; pasting the regenerated source into a disposable draft remains required for after-render visual closeout.

---

## Confirmed screenshot defect (Ch 04)

- Chapter begins at top of page.
- Zones 1–5 fill the printable two columns.
- Zones 6–8 (and trailing Set pieces / Secrets) continue into a third column outside the printable area and are clipped.
- Required fix: internal break before `### 6. Sealed Vaults` (complete section boundary), not prose deletion.

---

## Complete chapter-by-chapter pagination audit summary

| Chapter / section | Browser overflow? | Action |
|-------------------|-------------------|--------|
| Cover / front matter | No third-column overflow observed | Chapter-boundary only |
| 00–03 | No off-page heading overflow detected | Chapter-boundary only |
| **04 The Tho Yor** | **Confirmed** (zones 6–8 + Secrets) | Internal `\pagebreak` before `### 6. Sealed Vaults` |
| 05–06 | No off-page heading overflow detected | Chapter-boundary only |
| **07 Je'daii Order** | **Confirmed** (Great Journey) | Before `## The Great Journey (invented late)` |
| 08–09 | No off-page heading overflow detected | Chapter-boundary only |
| **10 SW5e Campaign Rules** | **Confirmed** (multi-column chain) | Four internal breaks (Force manipulation; Tech & gear; Force traditions; Foundry permissions) |
| 11–20 | No off-page heading overflow detected in CDP scan | Chapter-boundary only |
| **21 Great GM Scene Craft** | **Confirmed** (dense Scene Card chain) | Eight internal breaks at Scene Card boundaries |
| **22 Faces of the First Migration** | **Confirmed** (Crafters onward) | Three internal breaks (B / C / E) |
| 23 | No off-page heading overflow detected | Chapter-boundary only |
| **24 Timelines** | **Confirmed** | Three internal breaks (III / Quick reference / Player handout) |
| Appendices A–E | No off-page heading overflow detected in CDP scan | Chapter-boundary only |
| Ch 12 Koorivar | No third-column overflow flagged; CSS inject present | Regression preserved (inject + CSS) |
| Speakers (in Ch 22) | Present; overflow starts at Crafters | Speakers kept with Ch 22; break before B. Crafters |

---

## Chapters requiring internal breaks

04, 07, 10, 21, 22, 24

---

## Exact internal break locations

| ID | Chapter | Before heading | Break type |
|----|---------|----------------|------------|
| ch04-sealed-vaults | 04 — The Tho Yor | `### 6. Sealed Vaults` | `\pagebreak` |
| ch07-great-journey | 07 — The Je'daii Order (Founding) | `## The Great Journey (invented late)` | `\pagebreak` |
| ch10-force-manipulation | 10 — SW5e Campaign Rules | `### Force manipulation (mandatory)` | `\pagebreak` |
| ch10-tech-gear | 10 — SW5e Campaign Rules | `## Tech & gear bans / rarities` | `\pagebreak` |
| ch10-force-traditions | 10 — SW5e Campaign Rules | `## Force traditions vs Jedi/Sith labels` | `\pagebreak` |
| ch10-foundry-permissions | 10 — SW5e Campaign Rules | `## Foundry journal permissions` | `\pagebreak` |
| ch21-observation-galleries | 21 — Great GM Scene Craft | `### Scene Card — Observation Galleries` | `\pagebreak` |
| ch21-machine-spirit | 21 — Great GM Scene Craft | `### Scene Card — Machine-Spirit Interface` | `\pagebreak` |
| ch21-confluence | 21 — Great GM Scene Craft | `### Scene Card — Confluence Amphitheater` | `\pagebreak` |
| ch21-tython-camp | 21 — Great GM Scene Craft | `### Scene Card — Tython camp at night` | `\pagebreak` |
| ch21-force-storm | 21 — Great GM Scene Craft | `### Scene Card — Force Storm (arrival)` | `\pagebreak` |
| ch21-temple-akar | 21 — Great GM Scene Craft | `### Scene Card — Temple seed: Akar Kesh approaches` | `\pagebreak` |
| ch21-temple-padawan | 21 — Great GM Scene Craft | `### Scene Card — Temple seed: Padawan Kesh` | `\pagebreak` |
| ch21-capstone-finale | 21 — Great GM Scene Craft | `### Scene Card — Capstone finale tones` | `\pagebreak` |
| ch22-crafters | 22 — Faces of the First Migration | `## B. Crafters (commission loop)` | `\pagebreak` |
| ch22-rivals | 22 — Faces of the First Migration | `## C. Rivals & recurring pressures` | `\pagebreak` |
| ch22-combat-roles | 22 — Faces of the First Migration | `## E. Quick combat roles` | `\pagebreak` |
| ch24-century | 24 — Timelines (GM & Players) | `### III. Century of tightening song (living memory)` | `\pagebreak` |
| ch24-quick-ref | 24 — Timelines (GM & Players) | `## Quick reference — planet → Call image (for Scene Cards)` | `\pagebreak` |
| ch24-player-handout | 24 — Timelines (GM & Players) | `## Player Timeline Handout` | `\pagebreak` |

Exact strings are maintained in `tools/gmbinder_pagination.json` and must match the primary guide headings.

---

## `\pagebreakNum` usage and rationale

**None used.** Browser evidence did not show a page-number presentation requirement that `\pagebreak` fails to satisfy. All chapter-boundary and internal breaks use `\pagebreak`.

---

## Generator design implemented

- **Option B (config file)** + exact heading matching in `tools/md_to_gmbinder.py`
- Config: `tools/gmbinder_pagination.json`
- Exact chapter + exact `before_heading` line match within that chapter only
- Fail loud on missing chapter, missing heading, duplicate heading match, or application mismatch
- Dry-run reports planned internal breaks without writing
- No GM Binder directives inserted into campaign prose

---

## Files modified / created

### Modified
- `tools/md_to_gmbinder.py` — internal pagination support
- `gmbinder/dawn-of-the-jedaii-gmbinder.md` — regenerated
- `.gitignore` — `__pycache__/`, `*.pyc`, `*.bak-*`
- `ai/PROJECT_ARCHITECTURE.md` — tool I/O note for pagination config
- `reports/audits/2026-08-26-findings-register.yaml` — added F-M-003
- `reports/audits/audit-manifest.yaml` — note for this audit (if updated)

### Created
- `tools/gmbinder_pagination.json`
- `tools/test_md_to_gmbinder_pagination.py`
- `reports/audits/2026-08-26-gmbinder-pagination-layout-audit.md` (this file)

### Not modified by this task
- `dawn-of-the-jedaii-campaign-guide.md`
- `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md`
- Personal Foundry world
- ChatGPT archive content / F-K-002 prose / manuscript merge / integrated-guide migration

---

## Commands executed

- Browser CDP overflow scan of live GM Binder preview (before)
- `python tools/md_to_gmbinder.py --dry-run`
- `python tools/md_to_gmbinder.py --no-backup`
- `python -m unittest tools.test_md_to_gmbinder_pagination -v`
- Git status / diff checks (guide/companion unchanged)

---

## Automated tests

12 tests in `tools/test_md_to_gmbinder_pagination.py` — **OK**, covering:

- no legacy `\page`
- chapter-boundary + internal `\pagebreak` counts
- each configured break inserted exactly once
- Ch04 sealed-vaults break
- missing/duplicate heading failures
- idempotent generation
- Ch12 / Ch22 / Speakers regression
- Foundry tool unaffected by pagination config
- failed generation does not replace output

---

## GM Binder browser validation

| Layer | Status |
|-------|--------|
| Repository pagination correctness | **Pass** — 20 internal breaks present; reproducible via generator |
| Browser-rendered pagination (regenerated source) | **Outstanding** — live editor still has chapter-boundary breaks only (30×`\pagebreak`); disposable paste of regenerated source not completed (clipboard focus / editor mutation safety) |
| Unresolved broader layout defects | Dense pages may still look tight after breaks; no prose compression performed. Re-scan after paste. |
| Saved remote GM Binder sync | **Stale / not replaced** — intentional |

### Chapter 04 before / after

- **Before (live editor):** third-column clip of zones 6–8 (screenshot evidence).
- **After (repository):** `\pagebreak` immediately before `### 6. Sealed Vaults`.
- **After (browser render):** not yet validated on regenerated paste.

### Chapters 12 / 22 regression (repository)

- Ch12 remains Species Spotlight: Koorivar (inject path preserved).
- Ch22 remains Faces of the First Migration; Speakers section present.

---

## Remaining layout defects / follow-ups

1. **Paste regenerated `gmbinder/dawn-of-the-jedaii-gmbinder.md` into a disposable GM Binder draft** and re-run full-book visual pass.
2. If any chapter still overflows after paste, add/adjust entries in `tools/gmbinder_pagination.json` and regenerate (do not hand-edit GMB).
3. Optional later: CSS/table-width polish — deferred; not solved by deleting prose.
4. Koorivar injected `margin-top` spacer remains in external species CSS — not treated as Ch04 cause; log only if Ch12 shows overflow after paste.

---

## Disposable artifacts

- Removed TEMP inject chunk JSON files
- No `__pycache__` / `*.bak-*` retained for this task

## `.gitignore`

Patterns added/confirmed: `__pycache__/`, `*.pyc`, `*.bak-*`

---

## Commit readiness

Working tree is **not** committed. Pagination + prior blocker changes remain available for the previously proposed commit sequence after Kakeman89 reviews. **No commit / no push performed.**

---

## Addendum — 2026-08-26 — Rendered geometry validation supersedes heading-only acceptance

### Reason

Initial heading-based internal `\pagebreak` fixes and “pass” claims based on generated directives or DOM presence were **insufficient**. Screenshot review and full-book geometry scans exposed **persisted clipped third columns** (313+ overflow elements across 51 pages with only 20 manual breaks). Manual one-heading-at-a-time correction is not maintainable.

### Supersedes

Prior acceptance language in this report implying repository pagination alone closes layout defects, and any “no overflow detected” rows derived from heading-count heuristics rather than rendered bounding rectangles. **Historical content above is retained** as evidence of the earlier approach.

### Revised decision or behavior

**Rendered geometry validation is now the required acceptance method.**

- Physical page container: `.phb` (discovered in live disposable preview)
- Content selectors: `h1–h6, p, li, td, th, blockquote, table, pre, code, .note, .descriptive, .spell, .monster, .classFeature`
- Tolerance: **2px** (`tools/gmbinder_geometry.py`)
- Trace keys: invisible `data-gmb-src` spans injected at GMB generation only (`tools/gmbinder_semantic.py`)
- Validator: `tools/validate_gmbinder_render.py` → `reports/audits/gmbinder-render-validation.json`
- Iterative optimizer: `tools/run_gmbinder_pagination_session.py`, `tools/gmbinder_cdp_step.py`
- Workflow: `tools/GMBINDER_RENDER_VALIDATION.md`

Existing 20 manual breaks were archived to `seeds` in pagination v2; active breaks are being **re-derived** from browser scans. Derived breaks require `browser_validated: true` after a passing full-book scan.

### Implementation impact (2026-08-26 session)

| Artifact | Change |
|----------|--------|
| `tools/gmbinder_*.py`, `tools/validate_gmbinder_render.py`, `tools/run_gmbinder_pagination_session.py` | New geometry/semantic/pagination pipeline |
| `tools/gmbinder_browser_scan.js` | Browser scan script |
| `tools/gmbinder_pagination.json` | v2 schema; seeds + derived breaks |
| `gmbinder/dawn-of-the-jedaii-gmbinder.md` | Regenerated with trace markers |
| `tools/fixtures/gmbinder-ch04-overflow-scan.json` | Regression fixture |
| `tools/fixtures/gmbinder-ch05-overflow-scan.json` | Regression fixture |

### Validation impact

- **Baseline geometry scan (20 manual breaks):** `overflow_total=313`, `overall_pass=false`
- **After partial derived optimization (~26 breaks):** overflow reduced (e.g. 267 on 55-page render); **full-book pass not yet achieved**
- **Saved remote GM Binder:** unchanged
- **Campaign guide / companion / Foundry:** unchanged

### Status

**Implemented (tooling + partial optimization). Full-book rendered pass — IN PROGRESS.**
