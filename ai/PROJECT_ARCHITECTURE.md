# Dawn of the Jedaii — Project Architecture

**Status:** Operational document (not campaign canon)  
**Authority:** Kakeman89  
**Last updated:** 2026-08-26  
**Gate:** Architecture Confirmed (Phase 1)

This file documents the **current** source-of-truth matrix, edit boundaries, tool I/O, and authority hierarchy. It is operational configuration under `ai/` and must not silently override campaign prose.

---

## Authority hierarchy (campaign content)

1. Explicit decisions approved by Kakeman89
2. Primary campaign guide: `dawn-of-the-jedaii-campaign-guide.md`
3. Approved companion where it does not factually conflict: `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md`
4. Repository-designated sources (Appendix D where it covers a claim; future `sources/` only if authorized)
5. Verified Star Wars Legends continuity
6. Clearly labeled campaign adaptation / original campaign material

**Factual conflict rule:** When the companion and primary guide conflict on facts, the **primary guide controls**, unless Kakeman89 explicitly approved the companion version as superseding.

Differences in voice, detail, organization, presentation, or emphasis are **not** automatically continuity defects.

---

## Integrated-guide consolidation — PLANNING DIRECTION SELECTED

Kakeman89 selected **Option C** (2026-08-26): plan toward one integrated authoritative GM guide via controlled Act-by-Act migration (Act → Session → Scene).

| Status | Meaning |
|--------|---------|
| **PLANNING AUTHORIZED** | Migration **plan** may exist (`ai/plans/2026-08-26-integrated-gm-guide-migration.md`) |
| **CONSOLIDATION NOT AUTHORIZED** | Do **not** merge, migrate content, retire, archive, or rewrite either manuscript without a later explicit phase authorization |
| Pilot (planning) | Arc I first; Arc III second stress test — **execution not authorized** by plan creation alone |

### Addendum — 2026-08-27 — Arc I pilot disposition (operational)

| Item | Status |
|------|--------|
| Arc I architecture | ACCEPTED_WITH_REVISIONS (working model) |
| Arc I candidate | PROVISIONAL_NON_AUTHORITATIVE — not cutover |
| Arc III | PLANNING_AUTHORIZED_ONLY — no content migration started |
| Primary + companion | Remain operating authority until separate cutover authorization |

Decision detail: [`ai/plans/2026-08-26-campaign-decision-record.md`](plans/2026-08-26-campaign-decision-record.md) · Acceptance: [`reports/audits/arc-i-pilot-acceptance.md`](../reports/audits/arc-i-pilot-acceptance.md)

### Addendum — 2026-08-27 — Arc III planning baseline (operational)

| Item | Status |
|------|--------|
| Arc III plan | PLANNING_BASELINE_APPROVED / PLANNING_AUTHORIZED_ONLY |
| Arc III migration | NOT AUTHORIZED — no candidate; no content migration |
| F-H-001 mappings | Still empty — Model B preferred for future design analysis; mappings not approved |

Plan: [`ai/plans/2026-08-27-arc-iii-integrated-guide-stress-test.md`](plans/2026-08-27-arc-iii-integrated-guide-stress-test.md) · Decisions: [`ai/plans/2026-08-26-campaign-decision-record.md`](plans/2026-08-26-campaign-decision-record.md)

### Addendum — 2026-08-27 — BBEG and Imbalance integration (direction approved; not implemented)

| Item | Status |
|------|--------|
| BBEG / Imbalance plan | DIRECTION_APPROVED / PLANNING_ONLY — [`ai/plans/2026-08-27-bbeg-and-imbalance-campaign-integration.md`](plans/2026-08-27-bbeg-and-imbalance-campaign-integration.md) |
| BBEG identity / Dark Side pool | UNDECIDED — not invented; not implemented |
| Imbalance Storm Clock | MANDATORY (conversion planned; Ch10 still reads Optional in manuscripts) |
| Force Storms as adventure engine | MANDATORY (design planned; not implemented) |
| Arc I / Arc III candidates | Unchanged; remain PROVISIONAL_NON_AUTHORITATIVE |
| Manuscripts / production Foundry/GMB | Unchanged; cutover not authorized |

### Addendum — 2026-08-27 — Kwa Gate early discovery + reciprocal Ashla/Bogan (direction approved; not implemented)

| Item | Status |
|------|--------|
| Kwa Gate early discovery | REQUIRED early campaign development (planning) — not optional existence |
| Gate mastery | Progressive (foreshadow → discovery → activation → reliable use → institutions) |
| Map 4 | Important Gate site; particular expedition may remain optional; existence/discovery not optional |
| Dark Side pool | On Tython unless later changed; **not** presumed Bogan |
| Reciprocal restoration | Dark→Bogan contemplate Ashla; Light→Ashla contemplate Bogan; Balance + eventual return |
| First Bogan proposer / case | UNDECIDED |
| Plan document | Expanded 61-section integration plan (same path as BBEG plan above) |
| Candidates / manuscripts / outputs | Unchanged; implementation not authorized |

Decisions: [`ai/plans/2026-08-26-campaign-decision-record.md`](plans/2026-08-26-campaign-decision-record.md)

Until cutover is separately authorized, the **primary guide + approved companion** arrangement remains the operating architecture (see matrix below).

Related plans / reports:

- [`ai/plans/2026-08-26-blocker-generator-reliability-correction.md`](plans/2026-08-26-blocker-generator-reliability-correction.md) — plan only  
- [`ai/plans/2026-08-26-campaign-decision-record.md`](plans/2026-08-26-campaign-decision-record.md) — decisions only; no prose edits  
- [`ai/plans/2026-08-26-integrated-gm-guide-migration.md`](plans/2026-08-26-integrated-gm-guide-migration.md) — plan only  
- [`ai/plans/2026-08-26-chatgpt-archive-content-pr-scope.md`](plans/2026-08-26-chatgpt-archive-content-pr-scope.md) — archive Tier A/B content PR scope; plan only  
- [`ai/plans/2026-08-27-arc-iii-integrated-guide-stress-test.md`](plans/2026-08-27-arc-iii-integrated-guide-stress-test.md) — Arc III stress-test plan (planning baseline approved; migration not authorized)  
- [`ai/plans/2026-08-27-bbeg-and-imbalance-campaign-integration.md`](plans/2026-08-27-bbeg-and-imbalance-campaign-integration.md) — BBEG + mandatory Storm Clock / Force Storm integration (direction approved; not implemented)  
- [`reports/audits/2026-08-26-chatgpt-archive-vs-repo-gap-report.md`](../reports/audits/2026-08-26-chatgpt-archive-vs-repo-gap-report.md) — archive vs repo gap report  
- [`reports/audits/arc-i-pilot-acceptance.md`](../reports/audits/arc-i-pilot-acceptance.md) — Arc I pilot acceptance (provisional)

**Last updated:** 2026-08-27 (BBEG/Imbalance + Kwa Gate early discovery + reciprocal Ashla/Bogan direction approved as planning only; manuscripts and candidates unchanged; migration still not authorized)

---

## Source-of-truth matrix (current)

| Path | Role | Direct edit? | Produced by |
|------|------|--------------|-------------|
| `dawn-of-the-jedaii-campaign-guide.md` | **Primary authority** — facts, chronology, structure, approved decisions; generation source | **Yes** | Manual (+ historical `reorder_guide_chapters.py`) |
| `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md` | **Approved companion** — narrative, atmosphere, interpretation, GM guidance | **Yes** | Manual |
| `gm-narrative/README.md` | Ops note (companion vs guide conflict rule) | Yes | Manual |
| `gmbinder/dawn-of-the-jedaii-gmbinder.md` | Generated publication (GM Binder paste source) | **No** — regenerate | `tools/md_to_gmbinder.py` |
| `foundry/dawn-of-the-jedaii.journal.json` | Generated Foundry VTT v13 journal import | **No** — regenerate | `tools/md_to_foundry_journal.py` |
| `foundry/README.md` | Import / regen instructions | Yes | Manual |
| `README.md` | Project overview | Yes | Manual |
| `tools/*.py` | Build / migration scripts | Yes (code only) | Manual |
| `requirements.txt` | Python deps for Foundry HTML export | Yes | Manual |
| `ai/PROJECT_ARCHITECTURE.md` | This operational SoT doc | Yes | Manual |
| `ai/plans/**` | Dated plans | Yes when authorized | Manual |
| `.cursor/rules/**`, `.cursor/skills/**` | Agent governance | Yes when authorized | Manual |
| `reports/**` | Audit findings (operational evidence) | Yes when authorized | Manual / audit skills |
| `sources/`, `state/`, `guide/`, `design/`, `templates/` | **Absent** | Do not invent as authority over prose | — |

---

## Protected files and edit boundaries

### Must not hand-edit as sources

- `gmbinder/dawn-of-the-jedaii-gmbinder.md`
- `foundry/dawn-of-the-jedaii.journal.json`

Edit the primary guide, then regenerate when Kakeman89 authorizes a regen run.

### Must preserve during audit (and until migration is separately authorized)

- Both manuscripts (no merge, move, rename, archive, or delete)
- Intentional placeholders, Appendix D ambiguities, compression / `[T]` table fiction
- Companion presentation differences that are not factual conflicts

### Dangerous write tooling

- `tools/reorder_guide_chapters.py` — **historical**; defaults to refuse-write; dual confirmation flags required to rewrite the primary guide
- `tools/md_to_foundry_journal.py` — overwrites Foundry JSON; page/journal `_id`s are now **deterministic** from semantic keys (F-N-001); live import update behavior still needs manual Foundry validation
- `tools/md_to_gmbinder.py` — overwrites GM Binder Markdown; injects Species Spotlight (Ch 12) from external Koorivar path resolved via `--koorivar` / `KOORIVAR_SPECIES_PATH` / repo candidates / legacy path if present (F-M-001/F-M-002)

Supports `--dry-run` and timestamped backups (F-O-001). Do not run write-capable scripts during audit sessions without explicit authorization.

---

## Tool input / output paths

| Script | Reads | Writes | Notes |
|--------|-------|--------|-------|
| `tools/md_to_foundry_journal.py` | `dawn-of-the-jedaii-campaign-guide.md` | `foundry/dawn-of-the-jedaii.journal.json` | Requires `markdown`; one page per `#` H1; **deterministic** `_id`s; `--dry-run` / backup |
| `tools/md_to_gmbinder.py` | Primary guide + external `Koorivar.md` (CLI/env/repo/legacy discovery) + `tools/gmbinder_pagination.json` | `gmbinder/dawn-of-the-jedaii-gmbinder.md` | Injects **Ch 12** species/CSS; Ch 22 Faces passthrough; chapter-boundary + configured internal `\pagebreak`; `--dry-run` / backup |
| `tools/reorder_guide_chapters.py` | Primary guide | Primary guide only if dual write flags set | Historical Living Force chapter reorder; default refuse-write |

**External dependency (not vendored):** Koorivar species Markdown supplied via `--koorivar`, `KOORIVAR_SPECIES_PATH`, optional repo-relative candidates, or legacy author machine path if present. Four-axis review: [`reports/audits/2026-08-26-koorivar-dependency-review.md`](../reports/audits/2026-08-26-koorivar-dependency-review.md). Do not assume vendoring.

---

## Operational trees (not campaign canon)

Files under `ai/`, `.cursor/`, and `reports/` are operational instructions, configuration, plans, or findings. They must not silently override the primary campaign authority. Audit findings do not become approved campaign material without explicit Kakeman89 authorization.

---

## Appendix D and structured state

- Use Appendix D as provenance/classification authority **where it covers** a claim.
- Absence from Appendix D does not by itself prove unsupported; search remaining approved repository content before `NEEDS_SOURCE`.
- Authoritative structured campaign-state YAML remains **deferred**. Audit observations are evidence only.

---

## Content pipeline diagram

```text
dawn-of-the-jedaii-campaign-guide.md  (PRIMARY)
        |                    \
        |                     \-- factual conflict: guide controls
        |                      \
        v                       v
 tools/md_to_*.py          gm-narrative/... (APPROVED COMPANION)
        |
        +---> gmbinder/*.md          (GENERATED)
        +---> foundry/*.journal.json (GENERATED)
```

---

## Gate 1 checklist

- [x] Source-of-truth boundaries documented
- [x] Generated outputs identified
- [x] Protected files identified
- [x] Tool I/O paths documented
- [x] Consolidation recorded as **NEEDS DECISION**
- [x] No unresolved overwrite ambiguity for normal edit workflow (edit guide → regenerate outputs)

---

## Attribution

Where attribution is required in project materials, use **Kakeman89**.
