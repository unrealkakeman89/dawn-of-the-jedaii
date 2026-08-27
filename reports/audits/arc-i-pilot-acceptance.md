# Arc I Integrated GM Guide — Pilot Acceptance Package

**Status:** Operational review package — **NOT ACCEPTED** (Kakeman89 decision required)  
**Date:** 2026-08-27  
**Branch:** split/blocker-generator-governance-audits  
**Candidate:** `ai/migration-workspace/arc-i-integrated-candidate.md`

---

## 1. Executive summary

Arc I pilot implementation complete for all safely executable work. A provisional integrated candidate organizes Sessions 0–3 and eight ship Scene Cards under Act → Session → Scene structure with point-of-use scene templates, crosswalk traceability, pilot Foundry/GMB outputs, and audit evidence. Source manuscripts unchanged. F-N-001 disposable-world gate and F-K-002 source prose remain open.

**Pilot recommendation:** **ACCEPT_WITH_REVISIONS** — structure and table usability validated offline; Kakeman89 table test, F-N-001 live import, and F-K-002 source harmonization required before broader migration authorization.

---

## 2. Candidate path

`ai/migration-workspace/arc-i-integrated-candidate.md`

---

## 3. Candidate status

| Property | Value |
|----------|-------|
| Authority | **Non-authoritative provisional pilot** |
| Scope | Arc I only (Sessions 0–3 + 8 ship Scene Cards) |
| Lines | ~716 |
| Production generator input | **No** — not wired to `md_to_foundry_journal.py` / `md_to_gmbinder.py` |

---

## 4. Arc I table of contents

```
# Arc I: Aboard the Tho Yor (Sessions 0–3)
  ## Act at a Glance
  ## Session 0
    ### Session Overview … Possible State Updates
    ### Scenes: Calling Lock · Boon Visions · Table Contract
  ## Session 1 — The Call Completed
    ### Map 1 — Threshold Crossroads
    ### Scene — Threshold Halls
    ### Scene — Dormitories
  ## Session 2 — Song of the Ship
    ### Scene — Observation Galleries
    ### Scene — Meditation Core
    ### Scene — Machine-Spirit Interface
    ### Scene — Sealed Vaults (glimpse)
  ## Session 3 — Confluence & Approach
    ### Scene — Confluence Amphitheater
    ### Scene — Approach Finale
    ### Scene — Disembarkation Spines (Arc II reference)
  ## Player-Facing Handouts (Pilot)
  ## Central Reference Summaries
  ## Arc I Success Snapshot
```

---

## 5. Source inventory

See migration plan §10 and crosswalk CW-001–CW-026.

---

## 6. Crosswalk coverage

| Metric | Value |
|--------|-------|
| Arc I primary blocks mapped | 100% |
| Companion Arc I blocks | Synthesized (CW-003, CW-020) |
| Archive items classified | B1–B3 adopted; A2 placeholder; A3/A4/A6/B4–B6 excluded |
| Terminal migration statuses | All Arc I rows have status |
| Silent losses | None identified |

---

## 7. Material from primary guide

Ch04 zones, Ch11 boons/wiring, Ch13 checklists, Ch15 Sessions 0–3, Ch21 eight ship Scene Cards, Ch23 Map 1, App C (with candidate F-K-002 fix for handouts).

---

## 8. Material from companion

Ch4 Living aboard atmosphere (barter examples, null-corridor, routines, Eden/level-load framing) synthesized into connective text — not wholesale copied.

---

## 9. Material from ChatGPT archive

| ID | Treatment |
|----|-----------|
| B1 | 3 PCs LOCKED in Session 0 |
| B2 | Ninth Tho Yor planet-hop clarification |
| B3 | Spoiler-safe calling grid handout spec |
| A1 | F-K-002 candidate primer fix (not source) |

---

## 10. Original connective material

CW-024: cold-open agency table, failure/partial-success rows, session connective beats, Map 1 inline spec formatting. Classified ORIGINAL_CAMPAIGN_MATERIAL (migration connective).

---

## 11. Excluded material

A3 Map 6, A4 geography, A6 Speaker mappings, B4 flora, B5 Ganks, B6 Manaan sector, post-Arc-I Ch21 cards, Arc II–VI content.

---

## 12. Consolidated duplicates

Threshold (CW-002+003), Living aboard (Ch04+companion), Scene Card read-alouds merged with companion atmosphere in scene RP Guidance fields.

---

## 13. Unresolved conflicts

| Item | Status |
|------|--------|
| App C primer names Tython | Source conflict vs F-K-002; candidate fix only |
| F-H-001 eight mappings | Blocked — not invented |
| A2 Chamber of First Calling | Not in repo — placeholder only |

---

## 14. Point-of-use evaluation

**PASS (offline).** Sessions 1–3 runnable from session pages without external chapter lookup for operational beats. Ch22 full NPC bios remain central reference (local Senn-Vora summary provided).

---

## 15. Local Completeness evaluation

**PASS (spot-check).** Threshold, Meditation Core, and Confluence scenes contain read-aloud, mechanics, clues, alternates, transitions locally. Storm Clock and full boon text summarized + referenced.

---

## 16. Controlled-repetition evaluation

**PASS.** 31.5-hour clock, economy, Ashla/Bogan concept rules repeated consistently across scenes. No factual contradictions in repeated summaries.

---

## 17. Player-agency evaluation

**PASS.** See `arc-i-pilot-player-agency-audit.md`. Cold opens, council, and Core trial document bypass/failure paths.

---

## 18. Legends evaluation

**PASS.** See `arc-i-pilot-legends-audit.md`. No Disney canon; no new unsupported lore.

---

## 19. Continuity evaluation

**PASS.** See `arc-i-pilot-continuity-audit.md`. F-K-002 source conflict documented; candidate boundaries correct.

---

## 20. Staged Tython reveal evaluation

| Touchpoint | Candidate |
|------------|-----------|
| Opening crawl | Verbatim correct (no Tython) |
| Pilot primer | **Fixed** — no Tython name |
| Scene read-alouds | No Tython / no moon names |
| GM Act at a Glance | Tython OK |
| Source App C | **Unchanged** — conflict remains |

---

## 21. Calling/Speaker/Kesh impact

Arc I uses Senn-Vora default Speaker. F-H-001 mappings **not invented**. Generic guidance preserves GM substitution. Design gate remains for A6 / Ch10 crosswalk.

---

## 22. Foundry result

| Item | Value |
|------|-------|
| Output | `foundry/arc-i-pilot.journal.json` |
| Pages | 6 (Act overview, Sessions 0–3, Player Handouts) |
| Static JSON | Valid |
| Deterministic IDs | Stable across regen |
| GM-only default | ownership.default = 0 on GM pages |
| Player handouts page | ownership.default = 2 |
| Production journal | **Unchanged** |

---

## 23. Disposable-world result

**INCOMPLETE (F-N-001 open).** No disposable Foundry world available in this session.

### Manual test instructions

1. Create a **new empty Foundry world** (not Kakeman89's personal campaign).
2. Import `foundry/arc-i-pilot.journal.json` via Import Data.
3. Record page count and IDs created.
4. Re-import **unchanged** JSON.
5. Confirm update-in-place (no duplicate pages).
6. Verify hierarchy: Act overview + Sessions 0–3 + Player Handouts.
7. Confirm GM pages not visible to players; handout page permissions reviewed.
8. Record evidence in `reports/audits/` addendum.

---

## 24. GM Binder result

| Item | Value |
|------|-------|
| Output | `gmbinder/arc-i-pilot-gmbinder.md` |
| Content | All Sessions 0–3, 8 Scene Cards, handouts |
| Production GMB | **Unchanged** |
| Remote saved GMB | **Not touched** |
| Pagination | DEFERRED_PARTIAL — not optimized |

---

## 25. Content-loss check

No unique primary or companion Arc I operational block identified as lost. Ch22 full NPC entries referenced centrally by design.

---

## 26. Source-manuscript comparison

| Manuscript | Diff |
|------------|------|
| `dawn-of-the-jedaii-campaign-guide.md` | **None** |
| `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md` | **None** |

---

## 27. Remaining decisions (Kakeman89)

1. Accept Arc I pilot structure (Act/Session/Scene templates)
2. F-K-002: authorize source App C primer edit vs candidate-only handouts
3. F-H-001: complete eight Calling→Speaker→Kesh mappings
4. A2: authorize Chamber of First Calling content
5. B1/B2: authorize LOCKED lines in primary guide
6. F-N-001: run disposable-world import test
7. Table usability test (Sessions 1–3 from candidate)
8. Arc III stress test authorization (future)

---

## 28. Risks

| Risk | Mitigation |
|------|------------|
| Candidate mistaken for authority | Prominent headers; under `ai/` |
| F-K-002 player leak via source App C | Candidate fix + decision on source edit |
| Foundry duplicate pages | F-N-001 gate |
| Scope creep to full book | Pilot scope locked to Arc I |

---

## 29. Rollback

Delete `ai/migration-workspace/arc-i-integrated-candidate.md`, `foundry/arc-i-pilot.journal.json`, `gmbinder/arc-i-pilot-gmbinder.md`; mark crosswalk pilot rows deferred. Source manuscripts unaffected.

---

## 30. Recommendation

**ACCEPT_WITH_REVISIONS**

Accept provisional structure and point-of-use layout pending:

- Kakeman89 table test
- F-N-001 disposable-world validation
- Resolution of F-K-002 source vs candidate handout policy
- Optional tightening of Ch22 local portrayal depth

**Does not authorize:** authority cutover, companion retirement, Arc II+ migration, or production output replacement.

---

## Phase 0 classifications (record)

| Item | Classification |
|------|----------------|
| Arc I pilot scope | ALREADY_DECIDED (Phase 10 / migration plan) |
| Candidate path | ALREADY_DECIDED |
| Act/Session/Scene templates | ALREADY_DECIDED |
| F-M-003 pagination | ALREADY_DECIDED deferred |
| F-M-002 GMB Ch22 | RESOLVABLE — closed |
| F-N-001 live Foundry | REQUIRES_KAKEMAN89 (disposable world test) |
| F-K-002 staged reveal | ALREADY_DECIDED — candidate implements; source pending |
| F-H-001 mappings | REQUIRES_KAKEMAN89 |
| B1/B2/B3 archive | SAFE_REVERSIBLE_DEFAULT in candidate |
| A2 Chamber | REQUIRES_KAKEMAN89 / NOT_IN_REPO |
| A3/A4/A6/B4–B6 | NOT_APPLICABLE_TO_ARC_I or deferred |
| 3 PCs LOCKED | SAFE_REVERSIBLE_DEFAULT (candidate) |
| Arc III stress test | NOT_APPLICABLE_TO_ARC_I (future) |

---

*Kakeman89 pilot acceptance still required.*
