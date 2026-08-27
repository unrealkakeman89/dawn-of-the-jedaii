# ChatGPT Archive Content — PR Scope Plan

**Status:** Planning only — **implementation NOT AUTHORIZED**  
**Date:** 2026-08-26  
**Authority:** Gap report [`reports/audits/2026-08-26-chatgpt-archive-vs-repo-gap-report.md`](../../reports/audits/2026-08-26-chatgpt-archive-vs-repo-gap-report.md)  
**Architecture:** [`ai/PROJECT_ARCHITECTURE.md`](../PROJECT_ARCHITECTURE.md)

This plan defines a **separately reviewable PR scope** for ChatGPT-archive gaps that are not covered by the blocker/generator reliability plan. Plan creation does **not** authorize guide edits, asset binaries, Speaker mappings, regeneration, commit, or push.

---

## Purpose

Land archive-derived campaign and prep material that is still missing from the primary guide / asset tree, without mixing that work into generator-reliability fixes or integrated-guide migration.

## Separation from other plans

| Plan | Relationship |
|------|----------------|
| [`2026-08-26-blocker-generator-reliability-correction.md`](2026-08-26-blocker-generator-reliability-correction.md) | **Separate.** Do not fold F-M-*/F-N-*/F-O-* tool work into this scope. |
| [`2026-08-26-integrated-gm-guide-migration.md`](2026-08-26-integrated-gm-guide-migration.md) | **Separate.** No manuscript merge or companion retirement here. |
| [`2026-08-26-campaign-decision-record.md`](2026-08-26-campaign-decision-record.md) | **Gate.** F-K-002 and F-H-001 must clear their decision/design steps before related prose lands. |

## Included backlog IDs (from gap report)

### Tier A (high)

| ID | Work | Gate before implement |
|----|------|------------------------|
| **A1** | Harmonize player-facing Tython naming (App C + Ch 10) | Kakeman89 resolves **F-K-002** |
| **A2** | Chamber of First Calling (Ch 04) + Map 5 brief (Ch 23) | Content auth; defer PC-specific relic fill |
| **A3** | Map 6 Tython GM Hex Base brief + cartography standards | Content auth |
| **A4** | Talss / Moon Channel / Seven Moon Islands reconstruction (labeled confidence) | Content auth; mark NEEDS_SOURCE where unverified |
| **A5** | Create `assets/` skeleton + `ART-DIRECTION.md` + manifest README | Content auth; **no invented image binaries** |
| **A6** | Calling → Speaker → Kesh recommended crosswalk into guide | **F-H-001** design + review complete; separate prose auth |

### Tier B (medium)

| ID | Work | Gate |
|----|------|------|
| **B1** | Explicit LOCKED party size: 3 PCs | Content auth |
| **B2** | Explicit “Great Tho Yor did not planet-hop” LOCKED note | Content auth |
| **B3** | Spoiler-safe Tho Yor selection handout / grid specification | Content auth; pairs with A5 |
| **B4** | Heart Berry Tree + Ak Tree flora stubs (no invented mechanics) | Content auth |
| **B5** | Ganks era ruling | Legends verification first; keep OPEN until then |
| **B6** | Manaan sector fill | Verified Legends sector only; else leave `(unspecified)` |

## Explicitly excluded

- Hand-editing `gmbinder/` or `foundry/*.journal.json` as the solution
- Changing generators (F-M-002, F-N-001, F-O-*) under this plan
- Inventing the eight Speaker mappings during planning
- Inventing flora mechanical effects
- Vendoring external assets without licensing review
- Integrated-guide migration / companion retirement
- Commit / push unless separately requested

## Proposed work packages (when implementation later authorized)

### WP-1 — Decision-gated spoiler fix (A1)

1. Confirm F-K-002 posture in the campaign-decision record.  
2. Edit App C primer (and any Ch 10 player-facing announce lines) to match the chosen posture.  
3. Prefer archive default if selected: remove Tython name until earned (e.g. “You have not yet seen the world awaiting you.”).  
4. Do **not** regenerate outputs until WP-1 is reviewed; regen is a later gated step.

### WP-2 — Locked identity polish (B1, B2)

1. Add one explicit **3 PCs** LOCKED line near Session 0 / Ch 10 framing.  
2. Add one LOCKED sentence that the Great / ninth Tho Yor did not travel world-to-world gathering pilgrims (align with existing “already waiting” / Akar Kesh language).

### WP-3 — Chamber of First Calling + Map 5 (A2)

1. Add Ch 04 subsection for the secret upper floor (working room list from archive).  
2. State that Session 0 boons remain separate from upper-floor reliquaries.  
3. Leave three reliquary **item** fills as TBD until actual PCs exist.  
4. Add Ch 23 **Map 5 — Tho Yor: Chamber of First Calling** brief.

### WP-4 — Tython cartography (A3, A4)

1. Add Ch 23 **Map 6 — Tython: GM Hex Base** brief (16:9, top-down, polar regions, no labels/markers/hex, paper-cartographer aesthetic).  
2. Add short cartography standards (guide note and/or `assets/` pointer).  
3. Add Talss / Moon Channel / Seven Moon Islands reconstruction with exact / probable / reconstructed labels; do not invent false precision.

### WP-5 — Assets scaffold + art direction (A5, B3)

1. Create:

```text
assets/
├── ART-DIRECTION.md
├── README.md
├── handouts/
├── maps/tython/
├── ships/tho-yor/
├── flora/
├── creatures/
└── npcs/
```

2. Document Republic / Clone Wars comic aesthetic; Tho Yor sacred monumental look; maps as cartographic exception.  
3. Add manifest field schema (Asset, Type, Status, Use, Spoiler level, Notes).  
4. Add spoiler-safe Tho Yor selection-handout specification (silhouette + calling word only).  
5. Do not invent missing image files; placeholder paths / planned status only.

### WP-6 — Flora stubs (B4)

1. Add Heart Berry Tree and Ak Tree reference stubs (appearance, biome, edibility/uses if known, cultural note if established, encounter use, asset ref).  
2. No mechanical effects until campaign establishes them.

### WP-7 — Deferred / evidence-gated (A6, B5, B6)

1. A6: only after F-H-001 mapping design + Kakeman89 review.  
2. B5: Legends source audit for Ganks before any era ruling.  
3. B6: sector fill only with verified Legends citation.

### WP-8 — Regeneration (after guide WPs land)

1. Regenerate GM Binder and Foundry journal from the updated primary guide.  
2. Validate player-facing spoiler text and new chapter/map headings in outputs.  
3. Coordinate with blocker plan if F-M-002 is still open (Faces/Ch22) so regen does not reintroduce known generator defects — **blocker implementation remains a separate authorization**.

## Files likely affected (implementation phase)

| Path | Change type |
|------|-------------|
| `dawn-of-the-jedaii-campaign-guide.md` | Prose: App C, Ch 04, Ch 10, Ch 23, optional geography notes |
| `assets/**` | New scaffold + ART-DIRECTION + README |
| `gmbinder/dawn-of-the-jedaii-gmbinder.md` | Regenerated only after guide auth + WP-8 |
| `foundry/dawn-of-the-jedaii.journal.json` | Regenerated only after guide auth + WP-8 |

Companion edits are out of scope unless a factual conflict is introduced and Kakeman89 authorizes alignment.

## Acceptance criteria (implementation phase)

- [ ] F-K-002 posture applied consistently in player-facing App C / Ch 10 text  
- [ ] Maps 5 and 6 briefs exist in Ch 23  
- [ ] Chamber of First Calling documented without replacing Session 0 boons  
- [ ] Cartography standards and Talss-scale notes use confidence labels  
- [ ] `assets/ART-DIRECTION.md` and manifest README exist  
- [ ] Flora stubs present without invented mechanics  
- [ ] No generator code changes under this plan  
- [ ] Generated outputs updated only via regen after guide review  
- [ ] No commit/push without explicit request  

## Prerequisites before any implementation

1. Kakeman89 authorizes **implementation** of this plan (not granted by plan creation).  
2. F-K-002 resolved for WP-1.  
3. F-H-001 design complete before WP-7/A6 prose.  
4. Prefer landing WP-1–WP-6 as one reviewable PR scope or clearly split PRs that do not mix generator fixes.

## Status

**PLANNING ONLY — AWAITING IMPLEMENTATION AUTHORIZATION**
