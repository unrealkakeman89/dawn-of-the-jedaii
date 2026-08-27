# ChatGPT Archive vs Repo — Gap Report

**Status:** Operational audit finding (not campaign canon)  
**Date:** 2026-08-26  
**Authority:** Comparison only — does **not** authorize guide edits, asset creation, regeneration, commit, or push  
**Sources compared:**

- ChatGPT conversation-derived project archive (through 2026-08-26), provided by Kakeman89
- Current repository working tree, especially `dawn-of-the-jedaii-campaign-guide.md`

**Related plans:**

- [`ai/plans/2026-08-26-chatgpt-archive-content-pr-scope.md`](../../ai/plans/2026-08-26-chatgpt-archive-content-pr-scope.md) — Tier A/B backlog as a separate PR scope (plan only)
- [`ai/plans/2026-08-26-campaign-decision-record.md`](../../ai/plans/2026-08-26-campaign-decision-record.md) — F-K-002 / F-H-001 and other open decisions
- [`ai/plans/2026-08-26-blocker-generator-reliability-correction.md`](../../ai/plans/2026-08-26-blocker-generator-reliability-correction.md) — separate generator reliability work
- [`ai/plans/2026-08-26-integrated-gm-guide-migration.md`](../../ai/plans/2026-08-26-integrated-gm-guide-migration.md) — separate integrated-guide planning

---

## Verdict

The ChatGPT archive and the repo agree on the **core locked campaign spine**: Legends / SW5e / level 9 / start aboard a gathering Tho Yor / eight callings with Balance reserved / Force requirement / origin-world list / Ashla→Bogan discovery order / Maps 1–4 / opening crawl.

The failed ChatGPT PR attempt (`chatgpt/repo-recommendations`, GitHub 403) never landed the remaining gaps. Those gaps are catalogued here for Cursor-local work under separate Kakeman89 authorization.

Primary SoT remains `dawn-of-the-jedaii-campaign-guide.md`. Generated `gmbinder/` and `foundry/` outputs must be regenerated **after** authorized guide edits — not hand-edited as the fix.

The conversation archive is **WORKING memory for gaps**, not a second source of truth. Authority order remains: Kakeman89 decisions → primary guide → companion (non-conflict) → designated sources → Legends.

---

## Already in the repo (archive parity OK)

| Archive item | Repo evidence |
|--------------|---------------|
| Level 9, SW5e, Legends, 36,453 BBY / 0 TYA, start aboard Tho Yor | Guide intro + Ch 10 |
| Species free; Force required; approved homeland list (16 worlds) | Ch 10; Manaan sector still `(unspecified)` |
| Eight callings → Kesh; Balance / ninth Tho Yor reserved | Ch 10 + Ch 07 |
| Akar Kesh = ninth / Great Tho Yor site (“already waiting”) | Ch 05 / Ch 07 |
| Eight interior zones | Ch 04 |
| Ashla/Bogan concepts aboard → moon names after landing | Ch 02 / Ch 07 |
| Opening crawl + App C primer package | App C |
| Foundry map briefs 1–4 | Ch 23 |
| Foundry journal + GM Binder pipelines | `tools/`, `foundry/`, `gmbinder/` |
| Companion narrative book | `gm-narrative/` |

---

## Needs updating — prioritized backlog

### Tier A — High

| # | Gap | Status in repo | Notes / overlap |
|---|-----|----------------|-----------------|
| A1 | Player Tython spoiler clash (archive §16) | **PARTIAL / CONFLICT** | Crawl withholds name; App C primer names Tython (~L2538); Ch 10 calling announce names Tython (~L904). Same text in generated GMB/Foundry. Audit **F-K-002**. Open in campaign-decision record. Archive preference: remove name until earned. |
| A2 | Chamber of First Calling + Map 5 (archive §10 / §26 / §29) | **ABSENT** | No upper floor, Seal Hall, Triune Reliquary, or Map 5 brief. Working concept: ~100×100 ft; three PC-specific reliquaries; high-DC Ashla/Bogan/Balance seal; fourth alcove seeds “something beneath”; does not replace Session 0 boons. |
| A3 | Tython GM hex-base Map 6 + cartography standards (archive §11 / §26) | **ABSENT** | No Map 6; no locked 16:9 top-down / no labels / no markers / no hex / polar caps / paper-cartographer spec. |
| A4 | Talss / Moon Channel / Seven Moon Islands reconstruction (archive §12–13) | **ABSENT / PARTIAL** | Guide has Thyr / Masara / Kato Zakar + most Kesh seed notes; no Talss-named continent block, Moon Channel, or Seven Moon Islands. Kaleth geography thinner than peers (F-I-001 deferred). |
| A5 | `assets/` art pipeline (archive §20–22 / §26) | **ABSENT** | No `assets/`, `ART-DIRECTION.md`, or asset manifest. Locked Republic / Clone Wars comic aesthetic lives only in the archive. |
| A6 | Calling → Speaker → Kesh default crosswalk | **PARTIAL** | Calling→Kesh and Speakers exist; joint crosswalk absent. Phase 10 **F-H-001**: direction decided; eight mappings require separate design — do not invent. |

### Tier B — Medium

| # | Gap | Status in repo | Notes |
|---|-----|----------------|-------|
| B1 | Party size = 3 PCs (archive LOCKED) | **ABSENT** | Never stated; only level-9 founders framing. |
| B2 | Explicit “Great Tho Yor did not planet-hop” | **PARTIAL** | Intent covered by “already waiting”; archive’s hard correction sentence not present. |
| B3 | Spoiler-safe Tho Yor selection handout | **ABSENT** | Calling table exists; silhouette + calling-word grid / handout spec missing. |
| B4 | Heart Berry Tree + Ak Tree flora | **ABSENT** | No entries; do not invent mechanics. |
| B5 | Ganks era ruling (archive OPEN) | **ABSENT** | Keep OPEN until Legends verification. |
| B6 | Manaan sector | **FLAGGED** | Still `(unspecified)`; fill only with verified Legends sector or leave marked. |

### Tier C — Low / operational

| # | Item | Notes |
|---|------|-------|
| C1 | ChatGPT PR never applied | Obsolete; continue in this Cursor repo. |
| C2 | Foundry map **images** for Maps 1–4 | Briefs exist; binary scenes not shipped (expected). |
| C3 | Separate audit/migration work | Blocker-generator and integrated-guide plans remain separate scopes. |

---

## Checklist detail (archive § vs repo)

| Archive theme | Result |
|---------------|--------|
| Core identity (level 9, SW5e, Legends, era, start aboard) | **PRESENT** (party size 3 **ABSENT**) |
| Character creation (species, Force, origin world) | **PRESENT** |
| Approved origin worlds (16) | **PRESENT** |
| Eight callings + Balance / ninth / Akar | **PRESENT** |
| Calling → future Kesh table | **PRESENT** |
| Tho Yor eight zones | **PRESENT** |
| Chamber of First Calling / Map 5 | **ABSENT** |
| Tython Map 6 / cartography standards | **ABSENT** |
| Talss / Moon Channel / Seven Moon Islands | **ABSENT** |
| Kesh placement geography | **PARTIAL** |
| Ashla/Bogan discovery order | **PRESENT** |
| Player Tython spoiler policy | **PARTIAL / CONFLICT** |
| Opening crawl | **PRESENT** |
| Ganks ruling | **ABSENT / OPEN** |
| Heart Berry / Ak Tree | **ABSENT** |
| assets / ART-DIRECTION / manifest | **ABSENT** |
| Maps 1–4 | **PRESENT**; Maps 5–6 **ABSENT** |
| Speaker ↔ Calling crosswalk | **ABSENT** (direction recorded only) |
| Republic / Clone Wars comic art direction | **ABSENT** from repo docs |

---

## Evidence snippets (spoiler clash)

App C primer (player-facing), primary guide:

> You have not yet walked the world called **Tython**.

Opening crawl in the same appendix withholds the destination name. Ch 10 player-facing calling announce also names Tython. Generated GM Binder and Foundry journal currently mirror the primer wording.

---

## Authorization boundary

This report:

- **Does** catalogue archive-vs-repo gaps and preferred implementation order
- **Does not** authorize manuscript edits, `assets/` creation, flora invention, Speaker mappings, generator runs, regeneration, commit, or push
- **Does not** elevate the ChatGPT archive above Kakeman89 decisions or the primary guide

---

## Recommended next authorizations (Kakeman89)

1. Resolve **F-K-002** (and optionally B1 party size / B2 planet-hop wording).  
2. Authorize the ChatGPT-archive content PR scope plan for Tier A±B implementation (separate from blocker-generator work).  
3. After authorized guide edits land: regenerate GM Binder + Foundry; validate; do not hand-edit generated output.
