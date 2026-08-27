# Integrated GM Guide Migration Plan

**Status:** Planning only — **migration NOT AUTHORIZED**  
**Branch context:** Revised on `split/blocker-generator-governance-audits` (2026-08-27); does not alter `main` at `0034be2`  
**Authority:** Kakeman89 Phase 10 decisions 2026-08-26 (Option C — planning direction)  
**Operational — not campaign canon**

**Parent:** [`reports/audits/2026-08-26-phase10-kakeman89-review.md`](../../reports/audits/2026-08-26-phase10-kakeman89-review.md)  
**Architecture:** [`ai/PROJECT_ARCHITECTURE.md`](../PROJECT_ARCHITECTURE.md)  
**Crosswalk:** [`reports/audits/integrated-guide-content-crosswalk.yaml`](../../reports/audits/integrated-guide-content-crosswalk.yaml)  
**Critique:** [`reports/audits/2026-08-26-dawn-of-the-jedaii-project-critique.md`](../../reports/audits/2026-08-26-dawn-of-the-jedaii-project-critique.md)

---

## 1. Executive summary

This plan defines a **complete, reviewable procedure** for transforming the current **primary-guide + approved-companion** architecture into one **integrated authoritative GM guide** organized **Act → Session → Scene** for point-of-use table use.

**Phase 10 direction (Option C) is decided for planning:** controlled Act-by-Act migration, **Arc I pilot first**, **Arc III second stress test**.

**This document authorizes nothing by itself.** No manuscript merge, no companion retirement, no skill creation, no generator regen, no commit, no push.

**Current blockers and deferrals incorporated:**

| Finding | Status | Migration impact |
|---------|--------|------------------|
| F-M-002 (GMB Ch22) | closed | Generator trust restored; Faces exportable |
| F-M-003 (pagination) | **deferred** (`DEFERRED_PARTIAL`) | Layout phase after structure stabilizes |
| F-N-001 (Foundry IDs) | open | Disposable-world import gate for Arc I |
| F-M-001 (Koorivar) | needs_decision | Licensing boundary; do not copy external inject |
| F-K-002 (Tython reveal) | closed decision / prose pending | Spoiler policy in pilot crosswalk |
| F-H-001 (Calling→Speaker→Kesh) | direction decided; mappings TBD | Separate design gate; not Arc I blocker unless mappings needed |

GM Binder pagination optimization **stopped at Kakeman89's direction** with `overall_pass: false` (115 raw overflow, 106 semantic-block overflow, 4 failing pages). Validator infrastructure is **preserved**, not abandoned.

---

## 2. Current repository and branch state

| Item | Value |
|------|-------|
| Primary authority | `dawn-of-the-jedaii-campaign-guide.md` |
| Approved companion | `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md` |
| Generated GMB | `gmbinder/dawn-of-the-jedaii-gmbinder.md` |
| Generated Foundry | `foundry/dawn-of-the-jedaii.journal.json` |
| Pagination config | `tools/gmbinder_pagination.json` |
| Render validation | `reports/audits/gmbinder-render-validation.json` |
| Planning branch | `split/blocker-generator-governance-audits` (three-commit reconstruction) |
| Published `main` | `0034be2` — monolithic tooling/governance/audit commit |

Both manuscripts remain **unchanged** during planning and during any future pilot unless Kakeman89 separately authorizes prose edits.

---

## 3. Current authority model

During planning and throughout any future pilot:

1. **`dawn-of-the-jedaii-campaign-guide.md`** remains primary campaign authority.
2. **`gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md`** remains approved narrative and GM-facing companion.
3. On **factual conflict**, the primary guide controls unless Kakeman89 explicitly supersedes.
4. Differences in **voice, detail, organization, atmosphere, or emphasis** are not automatically factual conflicts.
5. Files under `ai/`, `.cursor/`, and `reports/` are **operational** and are not campaign canon.
6. The integrated candidate does **not** become authoritative merely because it is generated.
7. **No authority transition** occurs until Kakeman89 accepts the pilot and separately authorizes cutover.

---

## 4. Selected architecture direction

**Option C (Phase 10):** Create one integrated authoritative GM guide through a **controlled Act-by-Act migration**.

The intended final book prioritizes **table use** over purely encyclopedic organization. The GM should not bounce among unrelated chapters merely to locate Scene Cards, mechanics, NPC guidance, factions, clues, revelations, secrets, transitions, consequences, prep requirements, and Foundry assets for a single scene.

**Organization axis:** Act → Session → Scene (point-of-use spine) with centralized reference layers for reusable material.

---

## 5. Migration goals

1. **Point-of-use completeness** — runnable scenes contain what is needed at the table (Local Completeness Principle).
2. **Controlled local repetition** — prevent lookup friction without duplicating entire reference chapters.
3. **Source traceability** — every migrated block traces to primary, companion, archive, or labeled connective text.
4. **Player agency preservation** — no mandatory screenplay; document alternates, bypasses, failures.
5. **Legends discipline** — preserve classifications; no silent canon promotion.
6. **GM/player knowledge boundaries** — especially F-K-002 staged Tython reveal.
7. **Pilot-first validation** — Arc I proves structure before broader migration.
8. **Arc III stress test** — validate companion-heavy runnable depth (F-G-002).
9. **Generated output parity** — Foundry and GMB reflect integrated structure when authorized.
10. **Rollback safety** — original manuscripts retained until explicit cutover.

---

## 6. Non-goals

This plan does **not** authorize:

- Manuscript consolidation, merge, or deletion
- Companion retirement or archival
- Creating `.cursor/skills/integrated-guide-migration/SKILL.md`
- Generator changes or GMB/Foundry regeneration (except in future authorized phases)
- ChatGPT archive Tier A/B **implementation**
- F-K-002 prose implementation
- F-H-001 eight Calling→Speaker→Kesh assignments
- GM Binder pagination optimization (F-M-003 remains deferred)
- Overwriting the saved remote GM Binder document
- Modifying the personal Foundry game
- Commit / push
- Full-book rewrite in one pass
- Treating historical ChatGPT discussion as automatic canon

---

## 7. Required inputs

| Input | Path |
|-------|------|
| Architecture | [`ai/PROJECT_ARCHITECTURE.md`](../PROJECT_ARCHITECTURE.md) |
| This plan | `ai/plans/2026-08-26-integrated-gm-guide-migration.md` |
| Arc III stress-test plan | [`ai/plans/2026-08-27-arc-iii-integrated-guide-stress-test.md`](2026-08-27-arc-iii-integrated-guide-stress-test.md) — **planning only**; migration not authorized |
| Campaign decisions | [`ai/plans/2026-08-26-campaign-decision-record.md`](2026-08-26-campaign-decision-record.md) |
| Archive PR scope | [`ai/plans/2026-08-26-chatgpt-archive-content-pr-scope.md`](2026-08-26-chatgpt-archive-content-pr-scope.md) |
| Blocker plan | [`ai/plans/2026-08-26-blocker-generator-reliability-correction.md`](2026-08-26-blocker-generator-reliability-correction.md) |
| Phase 10 review | [`reports/audits/2026-08-26-phase10-kakeman89-review.md`](../../reports/audits/2026-08-26-phase10-kakeman89-review.md) |
| Project critique | [`reports/audits/2026-08-26-dawn-of-the-jedaii-project-critique.md`](../../reports/audits/2026-08-26-dawn-of-the-jedaii-project-critique.md) |
| Archive gap | [`reports/audits/2026-08-26-chatgpt-archive-vs-repo-gap-report.md`](../../reports/audits/2026-08-26-chatgpt-archive-vs-repo-gap-report.md) |
| Crosswalk | [`reports/audits/integrated-guide-content-crosswalk.yaml`](../../reports/audits/integrated-guide-content-crosswalk.yaml) |
| Findings register | [`reports/audits/2026-08-26-findings-register.yaml`](../../reports/audits/2026-08-26-findings-register.yaml) |
| Audit manifest | [`reports/audits/audit-manifest.yaml`](../../reports/audits/audit-manifest.yaml) |
| Blocker report | [`reports/audits/2026-08-26-blocker-implementation-report.md`](../../reports/audits/2026-08-26-blocker-implementation-report.md) |
| Foundry ID investigation | [`reports/audits/2026-08-26-foundry-id-investigation.md`](../../reports/audits/2026-08-26-foundry-id-investigation.md) |
| Koorivar review | [`reports/audits/2026-08-26-koorivar-dependency-review.md`](../../reports/audits/2026-08-26-koorivar-dependency-review.md) |
| Browser closeout | [`reports/audits/2026-08-26-blocker-closeout-browser-validation.md`](../../reports/audits/2026-08-26-blocker-closeout-browser-validation.md) |
| Pagination audit | [`reports/audits/2026-08-26-gmbinder-pagination-layout-audit.md`](../../reports/audits/2026-08-26-gmbinder-pagination-layout-audit.md) |
| Render validation | [`reports/audits/gmbinder-render-validation.json`](../../reports/audits/gmbinder-render-validation.json) |
| GMB validation workflow | [`tools/GMBINDER_RENDER_VALIDATION.md`](../../tools/GMBINDER_RENDER_VALIDATION.md) |
| Rules | `.cursor/rules/**` |
| Skills | `.cursor/skills/**` (excluding future migration skill) |
| Primary guide | `dawn-of-the-jedaii-campaign-guide.md` |
| Companion | `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md` |
| Generators | `tools/md_to_gmbinder.py`, `tools/md_to_foundry_journal.py` |

---

## 8. Audit findings driving migration

| ID | Severity | Status | Migration role |
|----|----------|--------|----------------|
| **F-P-002** | needs_decision | Pilot = Arc I; Arc III second test | **Pilot scope** |
| **F-G-001** | open | Arc I multi-chapter navigation | Local summary vs central reference |
| **F-G-002** | open | Arc III companion-heavy | Second stress test |
| **F-P-001** | open | Threshold Ch21↔companion §4 overlap | Consolidation with traceability |
| **F-M-003** | HIGH | **deferred** | Publication layout after structure stable |
| **F-N-001** | HIGH | open | Arc I Foundry acceptance gate |
| **F-M-001** | HIGH | needs_decision | Koorivar licensing boundary |
| **F-K-002** | MEDIUM | closed (decision); prose pending | Spoiler policy in pilot |
| **F-H-001** | MEDIUM | open (direction decided) | Separate mapping gate |
| **F-M-002** | BLOCKER | **closed** | Prerequisite satisfied |
| **F-O-001/002** | HIGH | closed | Generator safety in place |

**Crosswalk rows (initial):** CW-001 … CW-008 in [`integrated-guide-content-crosswalk.yaml`](../../reports/audits/integrated-guide-content-crosswalk.yaml). Note: CW-007 `gmbinder_dependency: MISSING (F-M-002)` is **stale** post–F-M-002 close.

---

## 9. ChatGPT archive treatment

Archive work is a **separate PR scope** ([`2026-08-26-chatgpt-archive-content-pr-scope.md`](2026-08-26-chatgpt-archive-content-pr-scope.md)). Migration may **consume** approved archive material but must not assume all archive content belongs in the integrated guide.

**Every archive item considered for migration must be classified as one of:**

| Classification | Meaning |
|----------------|---------|
| already represented | Present in primary or companion |
| superseded | Replaced by repo content |
| approved campaign decision | Recorded in decision register |
| useful migration source | Candidate for future adoption |
| Act-specific material | Belongs under Act overview |
| Session-specific material | Belongs under Session |
| Scene-specific material | Belongs under Scene |
| reusable reference material | Part IV / central reference |
| asset candidate | `assets/` or art direction (no invented binaries) |
| provenance-only evidence | Audit record only |
| conflicting proposal | Do not adopt without resolution |
| needs Kakeman89 decision | Hold |
| exclude from migration | Out of scope |

**Arc I–relevant archive items (planning inventory):**

| Tier | ID | Topic | Gate |
|------|-----|-------|------|
| A | A1 | Tython spoiler / F-K-002 | Decision recorded; prose not implemented |
| A | A2 | Chamber of First Calling + Map 5 | Content auth; Arc I ship secrets |
| A | A3 | Map 6 Tython hex base | Post-ship; **out of Arc I pilot** |
| A | A6 | Calling→Speaker→Kesh crosswalk | F-H-001 design complete |
| B | B1 | Locked 3 PCs | Session 0 framing |
| B | B2 | Great Tho Yor did not planet-hop | Founding spine |
| B | B3 | Spoiler-safe Tho Yor selection handout | Session 0 |

**Trace requirement:** Every adopted archive item must record archive source, destination, classification, approval basis, related guide/companion material, and whether it changes campaign canon.

**Do not implement Tier A/B during planning.**

---

## 10. Arc I source inventory

**Pilot scope:** Arc I = aboard the Tho Yor, **Sessions 1–3**, plus Session 0 prep wiring that Arc I depends on. Session 0 play itself is prep, not Arc I play (per Ch15).

### 10.1 Primary guide — Arc I and dependencies

| Path | Heading / section | Role in pilot |
|------|---------------------|---------------|
| `dawn-of-the-jedaii-campaign-guide.md` | `# 00 — Introduction & How to Use` (spoiler policy) | Foundations / knowledge boundaries |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 04 — The Tho Yor` — `### 1. Threshold Halls` … playable zones | Setting context; links to Ch21 cards |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 11 — Session 0 Boons of the Tho Yor` — `## Arc I wiring` | Boon placement; Storm Clock deps |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 13 — GM Checklists: Session 0 & Episode 1` | Prep checklists |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 15 — Arc I: Aboard the Tho Yor (Sessions 1–3)` | **Act overview + Sessions 1–3** |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 15` — `## Session 0 (before Arc I)` | Prep boundary note |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 15` — `## Session 1 — The Call Completed` | Session 1 beats |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 15` — `## Session 2 — Song of the Ship` | Session 2 beats |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 15` — `## Session 3 — Confluence & Approach` | Session 3 council |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 21 — Great GM Scene Craft` — `## The Scene Card` | Scene Card template |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 21` — `### Scene Card — Threshold Halls (first boarding)` | **Scene** |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 21` — `### Scene Card — Dormitories of the Called` | **Scene** |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 21` — `### Scene Card — Observation Galleries` | **Scene** |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 21` — `### Scene Card — Meditation Core` | **Scene** |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 21` — `### Scene Card — Machine-Spirit Interface` | **Scene** |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 21` — `### Scene Card — Sealed Vaults` | **Scene** |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 21` — `### Scene Card — Confluence Amphitheater` | **Scene** |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 21` — `### Scene Card — Disembarkation Spines` | **Scene** (Arc I finale approach) |
| `dawn-of-the-jedaii-campaign-guide.md` | `# 23 — Random Encounter Map Briefs` — `## Map 1 — Tho Yor: Threshold Crossroads` | Map brief |
| `dawn-of-the-jedaii-campaign-guide.md` | `# Appendix C — Handouts & Player Primer` | F-K-002 touchpoints |
| `dawn-of-the-jedaii-campaign-guide.md` | Ch10 Storm Clock / calling mechanics (as cited by CW-001) | Mechanics dependency — summarize + reference |

**Ch21 Scene Cards out of Arc I pilot scope** (post-Arc I): Tython camp, Force Storm arrival, Ashla/Bogan surfaces, temple seeds, capstone scenes.

**Ch15 Sessions 4–6** (`# 16 — Arc II`) are **out of Arc I pilot scope**.

### 10.2 Companion — Arc I material

| Path | Heading | Role |
|------|---------|------|
| `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md` | `# 4 — Aboard the Tho Yor` | Act atmosphere / living-aboard frame |
| `gm-narrative/...` | `## Living aboard` | Narrative prep |
| `gm-narrative/...` | `## Threshold Halls` | Overlaps CW-003 / CW-002 |
| `gm-narrative/...` | `## Dormitories of the Called` | Room atmosphere |
| `gm-narrative/...` | `## Observation Galleries` | Room atmosphere |
| `gm-narrative/...` | `## Meditation Cores` | Room atmosphere |
| `gm-narrative/...` | `## Machine-Spirit Interfaces` | Room atmosphere |
| `gm-narrative/...` | `## Sealed Vaults` | Room atmosphere |
| `gm-narrative/...` | `## Confluence Amphitheater` | Room atmosphere |
| `gm-narrative/...` | `## Disembarkation Spines` | Room atmosphere |
| `gm-narrative/...` | `# 7 — The Path Ahead` — Arc I subsection (H3) | Path framing |

Companion `# 5 — Faces in the Song` points to Ch22 for full NPC toolkits — **reference centrally**, not full migration in Arc I unless scene-relevant walk-ons are locally required.

### 10.3 Generated outputs (regen targets for future phases only)

| Output | Current Arc I–related journal pages |
|--------|-------------------------------------|
| `foundry/dawn-of-the-jedaii.journal.json` | `04 — The Tho Yor`, `11 — Session 0 Boons`, `13 — GM Checklists`, `15 — Arc I`, `21 — Great GM Scene Craft`, `23 — Random Encounter Map Briefs` |
| `gmbinder/dawn-of-the-jedaii-gmbinder.md` | Corresponding chapter pages |

### 10.4 Threshold duplicate / overlap

| Source A | Source B | Status |
|----------|----------|--------|
| Guide Ch21 Threshold Scene Card | Companion §4 Threshold Halls | CW-002 / CW-003 — presentation overlap, consolidate with traceability |
| Guide Ch04 zone 1 | Ch21 Threshold card | Reference link, not duplicate prose |

---

## 11. Arc I crosswalk requirements

Before Arc I implementation, **complete crosswalk coverage** for every source block in §10.

**Expand** [`reports/audits/integrated-guide-content-crosswalk.yaml`](../../reports/audits/integrated-guide-content-crosswalk.yaml) (or add `reports/audits/arc-i-crosswalk.yaml` sibling) using schema in [`CROSSWALK-SCHEMA.md`](../../reports/audits/CROSSWALK-SCHEMA.md).

**Per source block, record:**

| Field | Required |
|-------|----------|
| source file | yes |
| source heading or anchor | yes |
| current authority | yes |
| content category | yes |
| Act / Session / Scene | when applicable |
| overlap | yes |
| factual conflict vs presentation-only | yes |
| player-visible status | yes |
| GM-only status | yes |
| mechanics dependency | when applicable |
| Legends classification | when applicable |
| archive relationship | when applicable |
| proposed destination | yes |
| proposed treatment | yes |
| locally required | yes |
| centrally reusable | yes |
| preserve verbatim (only when authorized) | when applicable |
| consolidate / summarize locally / retain centrally / exclude | yes |
| needs Kakeman89 decision | when applicable |
| migration status | pending → mapped → validated |
| validation status | pending |

**Minimum new rows required (beyond CW-001–003):**

- Each Ch21 Arc I Scene Card (8 scenes)
- Ch15 Sessions 1, 2, 3 as session_overview rows
- Ch11 Arc I wiring, Ch13 checklists (prep)
- Ch23 Map 1
- Companion §4 room H2s (8 rooms) — may consolidate with guide rows
- App C F-K-002 touchpoints
- Ch10 mechanics dependencies (Storm Clock, calling)

**No source block may disappear because another block covers similar material.**

---

## 12. Proposed final book structure

**Recommended default** (deviations require justification in crosswalk / Kakeman89 review):

### Part I — Campaign Foundations

- How to use this book
- Campaign premise and themes
- Legends and campaign classifications
- Historical situation and GM truth
- Player assumptions and spoiler boundaries
- Campaign arcs overview
- Session 0 framing (central reference; not Arc I play)

### Part II — World and Powers

- Locations, cultures, peoples
- Factions and organizations
- Force traditions, technology, travel
- Personalities, artifacts, recurring mysteries
- **Central reference bank** — full NPC bios, faction histories, long tables

### Part III — The Campaign

```
Act I — Aboard the Tho Yor
  Session 1 — The Call Completed
    Scene — Threshold Halls
    Scene — Dormitories
    ...
  Session 2 — Song of the Ship
    ...
  Session 3 — Confluence & Approach
    ...
Act II — ...
```

Each **Scene** is the primary point-of-use unit.

### Part IV — GM Reference

- Character index
- Faction index
- Location index
- Chronology
- Clue and revelation index
- Artifact index
- Reusable mechanics (Storm Clock, boons, etc.)
- Encounter and travel tools
- Campaign-state / session-update procedures
- Cross-reference tables
- Appendix D provenance (or successor)
- Foundry / GMB export map

**Deviation note:** Part II may shrink if Local Completeness pushes more reference into Part IV indexes only; pilot will test balance.

---

## 13. Act template

| Field | Classification | Notes |
|-------|----------------|-------|
| Act at a Glance | **required** | One-screen summary |
| Act Purpose | **required** | Dramatic/engine purpose |
| Starting State | **required** | What table state enters Act |
| Central Dramatic Question | **recommended** | Optional for very short Acts |
| Active Factions | **recommended** | Summaries + Part IV refs |
| Important Characters | **recommended** | Scene-relevant + index refs |
| Important Locations | **recommended** | Ship zones / planet refs |
| Revelations | **recommended** | What players may learn |
| GM Secrets | **required** | GM-only truths |
| Repeated Act Mechanics | **optional** | Only if Act-wide rules exist |
| Expected Developments | **recommended** | Default path, not railroad |
| Alternate Developments | **required** | Player agency |
| Possible End States | **required** | Including partial success |
| State-Carryover Notes | **required** | What carries to next Act |
| Required Preparation | **required** | Checklists, maps, assets |
| Foundry Package | **recommended** | Page links / package name |

**Do not include empty boilerplate sections when a field is irrelevant.**

---

## 14. Session template

| Field | Classification | Notes |
|-------|----------------|-------|
| Session Purpose | **required** | |
| Starting Situation | **required** | |
| Required Preparation | **required** | |
| Active Characters | **recommended** | |
| Active Factions | **optional** | |
| Essential Clues | **required** when clues exist | |
| Optional Discoveries | **recommended** | |
| Suggested Flow | **recommended** | Default, not mandatory |
| Alternate Flow | **required** | |
| Session Scenes | **required** | Links to Scene sections |
| Failure and Partial Success | **required** | |
| End States | **required** | |
| Possible State Updates | **recommended** | Campaign-state hooks |
| Foundry Assets | **recommended** | |
| GM Binder Considerations | **optional** | Layout notes only |

---

## 15. Scene template

| Field | Classification | Notes |
|-------|----------------|-------|
| Scene Purpose | **required** | |
| Trigger | **required** | Activation conditions |
| Immediate Situation | **required** | |
| Read-Aloud | **recommended** | Player-facing; F-K-002 gated |
| Scene Card | **required** for operational scenes | Ch21 format preserved |
| Location | **required** | |
| Present Characters | **required** | |
| Objectives | **required** | PC and NPC |
| Opposition and Pressure | **required** | |
| Mechanics | **required** when mechanics apply | Summarize + Part IV ref |
| Clues and Discoveries | **required** when applicable | |
| Roleplaying Guidance | **recommended** | |
| Developments | **recommended** | |
| Failure and Partial Success | **required** | |
| Alternate Approaches | **required** | |
| Transition | **required** | To next scene/session |
| Consequences | **required** | |
| Possible Continuity Updates | **recommended** | |
| Foundry Assets | **recommended** | |
| Source Traceability | **required** (operational) | Crosswalk ID; not in GM-facing prose |

---

## 16. Local Completeness Principle

**Design principle (test in Arc I pilot):**

A runnable scene chapter should contain **all information required to understand, prepare, and adjudicate that scene**, except:

- universally reused mechanics (Part IV reference + local summary)
- full-length reference entries (Part II / Part IV + local summary)
- material whose controlled separation serves a clear purpose

### Include locally

Scene purpose, trigger, immediate situation, concise setting, present characters, scene-relevant goals/knowledge, Scene Card, objectives, opposition, scene-specific mechanics, required clues, optional discoveries, RP guidance, alternate approaches, failure/partial outcomes, transitions, consequences, possible state changes, relevant Foundry assets.

### Summarize locally and reference centrally

Recurring NPC histories, complete faction structures, full location histories, reusable mechanics, complete artifact provenance, recurring environmental rules, large random tables, complete stat blocks maintained elsewhere.

**A cross-reference must not replace essential information required to run the current scene.**

---

## 17. Controlled-repetition policy

### Allow local repetition when it prevents table-time lookup

- Scene-relevant goals and knowledge
- Scene-specific mechanics (short form)
- Essential clues
- Immediate consequences
- Short location descriptions
- Short NPC portrayal cues

### Prefer central reference + local summary for

- Full biographies
- Complete faction history
- Broad setting history
- Recurring mechanical systems (Storm Clock, boons)
- Complete artifact lore
- Large tables
- Long stat blocks

### Contradiction detection (post-migration)

1. For each entity (NPC, faction, location, mechanic) appearing in multiple local summaries, crosswalk must list **canonical source authority**.
2. Automated or manual diff: flag when two local summaries assert **different facts** (not wording).
3. Presentation-only differences → consolidate in crosswalk, not treated as conflicts.
4. Unresolved factual duplication → **stop migration** until Kakeman89 resolves.

---

## 18. Player-agency policy

Act → Session → Scene organization must **not** turn the campaign into a mandatory screenplay.

**Each session and scene must document:**

| Requirement | Classification |
|-------------|----------------|
| Activation conditions | required |
| Expected entry points | required |
| Optional entry points | required |
| Player goals | required |
| Antagonist / environmental pressure | required |
| Essential information | required |
| Alternate clue paths | required when clues exist |
| Bypass handling | required |
| Failure handling | required |
| Partial-success handling | required |
| Likely transitions | required |
| Alternate transitions | required |
| Persistent consequences | required |

### Arc I flagged sequence dependency (do not rewrite now)

**Ch15 Session 1** presents cold-open options A vs B (climb vs wake aboard). This is **not** a single mandatory choice but must be validated in pilot that neither path collapses player agency or drops essential beats.

**Ch15 Session 3** council has multiple valid outcomes — pilot must preserve disagreement / split options.

**Resolution required before pilot acceptance:** Document in crosswalk whether any Arc I beat is **structurally mandatory** vs **strongly recommended**; flag for Kakeman89 review at testing point 6.

---

## 19. Legends and provenance policy

Campaign remains **Legends-first**.

**Preserve classifications:**

- LEGENDS_VERIFIED
- CAMPAIGN_APPROVED
- CAMPAIGN_ADAPTATION
- ORIGINAL_CAMPAIGN_MATERIAL
- NEEDS_SOURCE
- CONTINUITY_CONFLICT

**Rules:**

- Do not import Disney-canon to fill gaps.
- Absence from Appendix D does **not** alone prove unsupported material.
- Do not silently convert table fiction → Legends lore, adaptation → Legends, original → established lore, or unresolved mystery → factual contradiction.
- Connective migration text must be labeled **ORIGINAL_CAMPAIGN_MATERIAL** (migration connective).
- Run [`legends-source-audit`](../.cursor/skills/legends-source-audit/SKILL.md) and [`continuity-auditor`](../.cursor/skills/continuity-auditor/SKILL.md) in Phase 6.

---

## 20. GM/player knowledge policy

| Audience | Rule |
|----------|------|
| GM-facing integrated material | May name Tython, Ashla/Bogan as taught, Kwa foreshadow, etc., per primary guide |
| Player-facing handouts / read-alouds | **F-K-002:** pre-reveal material must **not** name Tython; crawl withholds world identity |
| Post-reveal player material | May use Tython when campaign state reaches reveal |

**Arc I pilot must identify exact touchpoints:**

| Touchpoint | Path | F-K-002 class |
|------------|------|---------------|
| Opening crawl | Appendix C | pre-reveal — no Tython name |
| Player primer | Appendix C | **conflict to resolve** — currently names Tython; decision recorded, prose not implemented |
| Ch21 Observation Galleries read-aloud | Ch21 Scene Card | correctly withholds moon names |
| Ch15 Session 3 finale | Ch15 | green world + unnamed companion lights — correct |
| GM Inspiration blocks | various | GM-only — Tython naming OK |

**Do not edit primer/crawl during planning.**

---

## 21. Source-traceability model

**Recommended approach:** Expand YAML crosswalk as **system of record**; integrated candidate uses **stable section IDs** in HTML comments or YAML frontmatter blocks **stripped before publication export**.

| Method | Role |
|--------|------|
| `reports/audits/integrated-guide-content-crosswalk.yaml` (+ Arc I sibling) | **SoT** — every migrated block |
| Stable section IDs (`arc1-s1-threshold-halls`) | Link candidate headings to crosswalk rows |
| Migration connective text | Labeled in crosswalk as `ORIGINAL_CAMPAIGN_MATERIAL` |
| Change manifests per phase | Operational audit trail |

**Do not** put large provenance annotations in normal GM-facing prose.

**Justification:** Crosswalk already exists with schema; publication output generators can strip operational markers; supports rollback and “no block lost” validation.

---

## 22. Pilot candidate strategy

**Proposed path:** `ai/migration-workspace/arc-i-integrated-candidate.md`

| Property | Value |
|----------|-------|
| Location rationale | Under `ai/` = operational, provisional, not campaign top-level |
| Authority | **Non-authoritative** |
| Label | Provisional Arc I pilot; generated/assembled from traceable sources |
| Overwrites sources? | **No** — both manuscripts unchanged |
| Created when? | Phase 2 (future authorization) — **not during planning** |

**Required header block (future):**

```markdown
<!-- MIGRATION-PILOT: Arc I only | NON-AUTHORITATIVE | NOT CAMPAIGN CANON -->
<!-- Sources: primary guide + approved companion | Authority: unchanged -->
```

---

## 23. Foundry strategy

### Recommended page model: **mixed hierarchy**

| Level | Foundry page | Content |
|-------|--------------|---------|
| Act | 1 page per Act | Act at a Glance, purpose, secrets, carryover |
| Session | 1 page per Session | Session template fields; Scenes as **H2 sections** |
| Scene | H2 within Session page | Full Scene template |
| Scene-level page | **Only if** Session page too dense after Kakeman89 review | Escalation path |

**Rationale:** Balances navigation (Sessions match table prep) with page count; stable semantic IDs per Act/Session; Scenes remain discoverable within Session context.

### Evaluation criteria ( satisfied by recommendation )

| Criterion | Mixed hierarchy |
|-----------|-----------------|
| Table usability | Strong — open Session page at table |
| Navigation | Good — Act → Session → Scene headings |
| Page count | Moderate — ~4–5 pages for Arc I pilot |
| Stable semantic IDs | Yes — extend `md_to_foundry_journal.py` key scheme |
| Update behavior | Requires F-N-001 disposable-world validation |
| Player permissions | GM-only default; handouts extracted separately |
| Player handouts | Separate pages or linked blocks with ownership review |
| Internal links | Session → Part IV references |
| Future migration stability | Act-by-Act page addition without renumbering |

### F-N-001 gate (Arc I acceptance)

Before accepting Arc I Foundry package:

1. Import provisional Arc I journal into **disposable Foundry world**.
2. Re-import same JSON.
3. Confirm update-in-place (no duplicate pages).
4. Confirm GM-only ownership.
5. Record evidence in `reports/audits/`.

**Do not implement during planning.**

---

## 24. GM Binder strategy

**Status:** F-M-003 **deferred** / `DEFERRED_PARTIAL`

| Metric | Last retained scan |
|--------|-------------------|
| overall_pass | false |
| raw overflow | 115 |
| semantic-block overflow | 106 |
| failing pages | 4 (indices 50, 54, 55, 63) |
| physical pages | 64 |

**During migration planning and Arc I pilot (when authorized):**

- Regenerate GMB **only when authorized** for content presence validation
- Validate heading/chapter mapping and no content loss
- Record layout defects; do **not** require perfect full-book pagination for pilot acceptance
- Do **not** overwrite saved remote GM Binder document
- Do **not** mark F-M-003 resolved

**After manuscript structure stabilizes:** dedicated **publication-layout phase** using existing validator ([`tools/GMBINDER_RENDER_VALIDATION.md`](../../tools/GMBINDER_RENDER_VALIDATION.md)).

**Do not optimize pagination against structure scheduled to change.**

---

## 25. Pagination deferral (explicit)

GM Binder rendered-layout detection and pagination infrastructure are **implemented and preserved**.

The generated publication still contains unresolved rendered overflow. Further pagination optimization is **deferred until after** integrated GM guide structure and manuscript content stabilize, because migration will alter page composition and may invalidate current break placement.

Deferral is **Kakeman89-directed**, not technical impossibility. See pagination audit addendum 2026-08-27 and F-M-003 in findings register.

---

## 26. Koorivar dependency boundary

**F-M-001:** `needs_decision`

| Done | Open |
|------|------|
| CLI/env/repo-candidate/legacy path resolution | Licensing / redistribution |
| Fail-loud if missing | Vendoring vs external reference |
| GMB Ch12 inject (operational) | Copying external species text into integrated manuscript |

**Classify Koorivar-dependent migration work:**

| Class | Action |
|-------|--------|
| repository-owned and safe | Reference Ch12 inject path in crosswalk |
| external reference only | Do not copy SW5e file content into integrated guide |
| requires provenance review | Hold until F-M-001 resolved |
| requires licensing decision | Block content copy |
| exclude pending decision | Default for verbatim species text |

**Arc I pilot:** Does not directly depend on Koorivar species chapter — **F-M-001 does not block Arc I planning** unless pilot scope expands to Ch12.

---

## 27. Migration skill specification (deferred)

**Path (future):** `.cursor/skills/integrated-guide-migration/SKILL.md`

**Do not create during planning.**

### Creation preconditions (all required)

1. This migration plan approved by Kakeman89
2. Arc I TOC approved
3. Act, Session, Scene templates approved
4. Crosswalk procedure approved
5. Pilot candidate path approved
6. Validation and rollback gates approved
7. Kakeman89 **explicitly authorizes** creating the skill

### Future skill behavior

- Migrate **one approved scope** at a time
- Read all controlling `.cursor/rules/` and relevant skills
- Use approved crosswalk as SoT
- Preserve traceability (crosswalk row per block)
- **Stop** on unresolved factual conflicts
- Distinguish migration from new writing
- Label connective text as ORIGINAL_CAMPAIGN_MATERIAL
- Preserve both source manuscripts — never delete source material
- Validate content completeness against crosswalk
- Validate output targets (candidate path only until cutover)
- Produce **change manifest** per run
- Report unresolved decisions — never auto-promote authority
- Never mark integrated candidate authoritative automatically

---

## 28. Phased implementation (future — not authorized)

### Phase 0 — Decisions and prerequisites

| Item | Detail |
|------|--------|
| Intent | Confirm gates before any prose migration |
| Inputs | This plan, findings register, decision record |
| Outputs | Approved Arc I TOC, templates, candidate path, crosswalk method |
| Gate | Kakeman89 sign-off on Phase 0 checklist |
| Rollback | N/A — no migration artifacts yet |

**Checklist:**

- [ ] Arc I scope confirmed (§10)
- [ ] Templates approved (§13–15)
- [ ] Candidate path approved: `ai/migration-workspace/arc-i-integrated-candidate.md`
- [ ] Crosswalk method approved (§21)
- [ ] F-K-002 Arc I touchpoints documented (§20)
- [ ] F-H-001 mapping gate scheduled (only if Arc I needs Speaker assignments)
- [ ] F-N-001 disposable-world test plan accepted
- [ ] F-M-003 remains deferred — acknowledged

### Phase 1 — Arc I crosswalk completion

| Item | Detail |
|------|--------|
| Intent | Map every source block; no prose migration |
| Outputs | Complete Arc I crosswalk YAML |
| Gate | 100% Arc I source blocks mapped; zero `unresolved` factual conflicts without decision |
| Rollback | Delete/supersede crosswalk additions only |

### Phase 2 — Integrated structure skeleton

| Item | Detail |
|------|--------|
| Intent | Create provisional candidate framework with headings |
| Outputs | `ai/migration-workspace/arc-i-integrated-candidate.md` (headings + placeholders only) |
| Gate | TOC matches approved structure; no source edits |
| Rollback | Delete candidate file |

### Phase 3 — Arc I mechanical migration

| Item | Detail |
|------|--------|
| Intent | Move/reproduce operational material (Scene Cards, mechanics, checklists, clues) |
| Outputs | Candidate populated with operational content + crosswalk IDs |
| Gate | Local Completeness spot-check; traceability 100% |
| Rollback | Revert candidate to Phase 2 skeleton via git |

### Phase 4 — Arc I narrative integration

| Item | Detail |
|------|--------|
| Intent | Integrate approved companion atmosphere; presentation-only enrichment |
| Outputs | Candidate narrative sections; crosswalk updated |
| Gate | No unsupported lore; voice per house rules |
| Rollback | Revert narrative commits to candidate |

### Phase 5 — Archive material review

| Item | Detail |
|------|--------|
| Intent | Incorporate **only approved** Tier A/B items relevant to Arc I |
| Outputs | Crosswalk archive rows; candidate updates if authorized |
| Gate | Each item classified per §9; exclusions recorded |
| Rollback | Remove archive-derived blocks from candidate |

### Phase 6 — Continuity and Legends audit

| Item | Detail |
|------|--------|
| Intent | Run audit skills; verify knowledge boundaries, chronology, clues |
| Outputs | Audit addendum in `reports/audits/` |
| Gate | No CONTINUITY_CONFLICT unrecorded; F-K-002 boundaries verified |
| Rollback | Fix candidate or halt |

### Phase 7 — Foundry pilot output

| Item | Detail |
|------|--------|
| Intent | Generate provisional Arc I Foundry package |
| Outputs | `foundry/arc-i-pilot.journal.json` or staged path (TBD at implementation) |
| Gate | **F-N-001 disposable-world validation pass** |
| Rollback | Remove pilot journal file; regen from prior authority |

### Phase 8 — GM Binder pilot output

| Item | Detail |
|------|--------|
| Intent | Generate content output; record layout defects |
| Outputs | Staged GMB pilot; validation JSON |
| Gate | Content presence; heading mapping; F-M-003 **not** required resolved |
| Rollback | Remove pilot GMB; retain deferred pagination state |

### Phase 9 — Pilot acceptance review

| Item | Detail |
|------|--------|
| Intent | Compare candidate vs both sources; usability review |
| Outputs | Pilot acceptance report |
| Gate | See §36 authority-transition criteria (pilot subset) |
| Rollback | Candidate marked rejected; sources unchanged |

### Phase 10 — Pilot disposition

| Outcome | Next step |
|---------|-----------|
| Accept structure | Authorize Arc III stress test planning |
| Accept with revisions | Phase 3–4 iteration |
| Revise and repeat Arc I | New pilot cycle |
| Reject integrated approach | Retain dual-manuscript architecture |
| Defer | No migration |
| Authorize Arc III stress test | Plan Arc III crosswalk |
| Arc III planning document | [`ai/plans/2026-08-27-arc-iii-integrated-guide-stress-test.md`](2026-08-27-arc-iii-integrated-guide-stress-test.md) (created 2026-08-27; **planning only**) |
| Authorize remaining Acts | Per-Act authorization |
| Keep current architecture | Close migration track |

**No outcome retires source manuscripts automatically.**

---

## 29. Proposed file manifest per phase

| Phase | Files created/modified (future) |
|-------|--------------------------------|
| 0 | This plan (approved version), decision record addenda |
| 1 | `reports/audits/integrated-guide-content-crosswalk.yaml` or `arc-i-crosswalk.yaml` |
| 2 | `ai/migration-workspace/arc-i-integrated-candidate.md` |
| 3–4 | Candidate content; crosswalk status updates |
| 5 | Crosswalk archive rows; optional candidate sections |
| 6 | `reports/audits/arc-i-continuity-audit.md` (proposed) |
| 7 | `foundry/arc-i-pilot.journal.json` (proposed staged path) |
| 8 | `gmbinder/arc-i-pilot-gmbinder.md` (proposed staged path); `reports/audits/gmbinder-arc-i-pilot-validation.json` |
| 9 | `reports/audits/arc-i-pilot-acceptance.md` |
| 10 | Decision record addendum |

**Never modify** `dawn-of-the-jedaii-campaign-guide.md` or companion **until explicit cutover authorization**.

---

## 30. Validation gates

### Per-phase gates

See §28 each phase.

### Arc I pilot acceptance gates (subset of §36)

1. Complete Arc I crosswalk coverage
2. No unresolved factual conflict
3. No unique source material lost (companion Arc I prose accounted for)
4. All exclusions approved
5. Arc I runnable from candidate at table (Kakeman89 test)
6. Local Completeness Principle validated on 3 sample scenes
7. Alternate player paths preserved (Session 1 cold opens, Session 3 council)
8. Legends classifications preserved
9. Player/GM boundaries preserved (F-K-002)
10. Foundry pilot passes F-N-001 disposable-world test
11. GMB pilot content validated (pagination may remain deferred)
12. Kakeman89 accepts pilot
13. Rollback demonstrated (delete candidate; sources intact)

**Arc I acceptance ≠ full-book authority.**

---

## 31. Rollback

| Layer | Rollback action |
|-------|-----------------|
| Source manuscripts | **Never modified** during pilot — rollback = do nothing |
| Pilot candidate | Delete `ai/migration-workspace/arc-i-integrated-candidate.md` |
| Crosswalk | Retain history; mark rows `deferred` or `superseded` |
| Generated pilot outputs | Delete staged Foundry/GMB pilot files |
| Change manifests | Retained in `reports/audits/` for audit |
| Companion | No archival during pilot |
| Authority | Remains primary guide |
| Regenerated outputs | Main `gmbinder/` and `foundry/` regen from **primary authority** when needed |

Every phase produces a **change manifest** listing blocks added/moved/classified.

---

## 32. Kakeman89 review points

Test or review **before** broad migration authorization:

| # | Review point |
|---|--------------|
| 1 | Arc I table of contents |
| 2 | Act / Session / Scene templates |
| 3 | Scene Card presentation in integrated layout |
| 4 | Point-of-use completeness (sample scenes) |
| 5 | Amount of local repetition |
| 6 | Player-agency handling (Session 1 opens, Session 3 council) |
| 7 | Staged Tython reveal touchpoints (F-K-002) |
| 8 | Foundry navigation (Session pages) |
| 9 | GM-only vs player-visible separation |
| 10 | GM Binder content organization (not full pagination) |
| 11 | Companion voice preservation vs primary operational clarity |
| 12 | Source-traceability report (crosswalk export) |
| 13 | Authority-transition decision |

---

## 33. Remaining decisions

| ID / topic | Status | Needed for |
|------------|--------|------------|
| F-H-001 eight mappings | TBD | A6 archive; Speaker foreshadow in Arc I (optional) |
| F-K-002 prose | Decision recorded; prose pending | App C primer harmonization |
| F-M-001 Koorivar licensing | needs_decision | Ch12 long-term; not Arc I blocker |
| F-N-001 live Foundry import | open | Arc I Foundry acceptance |
| F-G-006 landing milestones | open | Post-Arc I; not pilot |
| F-B-002 Ashla/Bogan gloss order | open | Reference material |
| F-P-002 pilot scope | planning decided | Confirm at Phase 0 |
| Integrated TOC final shape | TBD | Phase 0 approval |
| Scene-level Foundry pages | TBD | Only if Session pages too dense |
| Authority cutover timing | TBD | After full migration — not Arc I |

---

## 34. Risks

| Risk | Mitigation |
|------|------------|
| Voice loss (companion atmosphere) | Phase 4 explicit; house voice rules; Kakeman89 review point 11 |
| Excessive duplication | Controlled-repetition policy + contradiction detection |
| Railroading | Player-agency policy; mandatory-beat audit before acceptance |
| Unique companion content dropped | Crosswalk completeness; “no block lost” gate |
| Legends drift | Phase 6 audit; classification labels |
| Foundry duplicate pages | F-N-001 gate |
| Pagination churn | F-M-003 deferred until structure stable |
| Koorivar licensing | F-M-001 boundary; no silent copy |
| Scope creep (full book) | Arc I pilot only until acceptance |
| Authority creep | Candidate labeled non-authoritative; separate cutover gate |

---

## 35. Success criteria

**Arc I pilot success (does not equal full migration success):**

1. GM can run Sessions 1–3 from integrated candidate with ≤2 external chapter lookups (target — validate at table)
2. All 8 Arc I ship Scene Cards present and locally complete
3. Threshold consolidation resolved with traceability (CW-002/003)
4. Crosswalk 100% for Arc I sources
5. No factual conflicts unresolved
6. F-N-001 passed for pilot Foundry package
7. Kakeman89 acceptance at review point 13 (pilot subset)

**Full migration success (future):** All Acts migrated; authority transition authorized; Foundry/GMB regen from integrated authority; companion disposition decided separately.

---

## 36. Authority-transition criteria

**Authority states:**

| State | Meaning |
|-------|---------|
| provisional pilot | Candidate exists; sources authoritative |
| accepted pilot structure | TOC/templates approved; still non-authoritative |
| migration in progress | Later Acts being migrated |
| integrated candidate | Full draft exists; not yet authoritative |
| authoritative integrated guide | Kakeman89 cutover authorized |
| legacy source manuscripts | Retained read-only after cutover until disposition decision |

**Full transition gate (future — not Arc I):**

1. Complete book crosswalk coverage
2. No unresolved factual conflict
3. No unique source material lost
4. All exclusions approved
5. Full campaign runnable from integrated candidate (or agreed subset)
6. Local Completeness validated
7. Player agency preserved campaign-wide
8. Legends classifications preserved
9. Player/GM boundaries preserved
10. Foundry output validated (including F-N-001)
11. GM Binder content validated; pagination phase complete or explicitly deferred with acceptance
12. Kakeman89 accepts integrated guide
13. Rollback plan documented
14. Original manuscripts retained

---

## 37. Post-pilot options

See Phase 10 table (§28). Emphasis:

- **Accept structure** → plan Arc III stress test
- **Reject** → retain dual-manuscript architecture indefinitely
- **Defer** → no further migration work
- **No automatic companion retirement** under any outcome

---

## 38. Explicit authorization boundary

**This plan authorizes:**

- Planning and documentation only
- Defining procedures, templates, gates, and inventories

**This plan does NOT authorize:**

- Editing `dawn-of-the-jedaii-campaign-guide.md`
- Editing `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md`
- Creating `ai/migration-workspace/arc-i-integrated-candidate.md`
- Creating `.cursor/skills/integrated-guide-migration/SKILL.md`
- Crosswalk YAML edits (implementation)
- Generator runs or output regen
- Pagination optimization
- Archive Tier A/B implementation
- F-K-002 or F-H-001 prose
- Commit, push, PR, or authority transition

**Each Phase 0–10 step requires separate Kakeman89 authorization.**

---

## Document history

| Date | Change |
|------|--------|
| 2026-08-26 | Initial planning sketch (Option C direction) |
| 2026-08-27 | Comprehensive revision on `split/blocker-generator-governance-audits`: full procedure, templates, Arc I inventory, deferrals, gates |
| 2026-08-27 | Link Arc III stress-test plan (`ai/plans/2026-08-27-arc-iii-integrated-guide-stress-test.md`); Arc III migration still not authorized |

---

*End of plan — migration NOT AUTHORIZED.*
