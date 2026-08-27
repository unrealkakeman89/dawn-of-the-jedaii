# Arc III Integrated Guide Stress-Test Plan

**Status:** `PLANNING_BASELINE_APPROVED` / `PLANNING_AUTHORIZED_ONLY` — **Arc III migration NOT AUTHORIZED**  
**Authority:** Kakeman89 Arc I disposition 2026-08-27 (`ACCEPT_WITH_REVISIONS`); Kakeman89 Arc III planning baseline approval 2026-08-27  
**Operational — not campaign canon**  
**Date:** 2026-08-27

**Parent migration plan:** [`ai/plans/2026-08-26-integrated-gm-guide-migration.md`](2026-08-26-integrated-gm-guide-migration.md)  
**Decision record:** [`ai/plans/2026-08-26-campaign-decision-record.md`](2026-08-26-campaign-decision-record.md)  
**Architecture:** [`ai/PROJECT_ARCHITECTURE.md`](../PROJECT_ARCHITECTURE.md)  
**Acceptance:** [`reports/audits/arc-i-pilot-acceptance.md`](../../reports/audits/arc-i-pilot-acceptance.md)  
**Crosswalk:** [`reports/audits/integrated-guide-content-crosswalk.yaml`](../../reports/audits/integrated-guide-content-crosswalk.yaml)  
**Findings:** [`reports/audits/2026-08-26-findings-register.yaml`](../../reports/audits/2026-08-26-findings-register.yaml)

---

## 1. Executive summary

This plan defines a **complete, reviewable stress-test procedure** for Arc III (*Survive & Contact*, Sessions 7–11) under the integrated Act → Session → Scene model accepted (with revisions) for Arc I.

**Why Arc III second:** Audit finding **F-G-002** — runnable Arc III depth lives mainly in the approved companion (`gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md` `# 7 — The Path Ahead` / `## Arc III — Survive & Contact (Sessions 7–11)`), while the primary guide (`dawn-of-the-jedaii-campaign-guide.md` `# 17 — Arc III: Survive & Contact (Sessions 7–11)`) is largely beat titles. Crosswalk row **CW-006** maps Arc III as `act_overview` with companion overlap marked presentation-only.

**This document is the approved Arc III planning baseline** (`PLANNING_BASELINE_APPROVED` / `PLANNING_AUTHORIZED_ONLY`). It does **not** authorize Arc III migration, an Arc III candidate file, campaign prose, F-H-001 eight Calling → Speaker → Kesh assignments, Foundry/GMB generation, or authority cutover.

**Key locked operational statuses (2026-08-27):**

| Item | Status |
|------|--------|
| Arc I architecture | `ACCEPT_WITH_REVISIONS` / `ACCEPTED_WITH_REVISIONS` |
| Arc I candidate | `PROVISIONAL_NON_AUTHORITATIVE` |
| Arc III plan | `PLANNING_BASELINE_APPROVED` / `PLANNING_AUTHORIZED_ONLY` — migration **NOT** authorized |
| Sessions 7–11 outline | `PROVISIONAL_OPERATIONAL_STRUCTURE` (not preexisting campaign canon); scene/session names provisional until separate candidate authorization |
| Omen of the Moons default | Arc III Session 9; alternate = closing Arc II; do not rerun if already completed |
| Map 3 Silent Desert | Optional, **in-scope**; not required for Arc III completion |
| Map 4 Kwa Gate | Optional **advanced**; not required path; must not replace social-contact focus |
| Counting Quarrel | Complete quarrel primarily **Arc IV**; Arc III may **seed** only |
| F-H-001 design model | Prefer Model B (recommended casting); do not assume fixed 1:1; mappings **not** assigned |
| Companion Arc III procedures | Required migration candidates for Local Completeness (when migration authorized) |
| F-H-001 mappings | `DEFERRED_TO_ARC_III` — **do not assign** |
| F-K-002 production sync | `KEEP_CANDIDATE_ONLY_UNTIL_AUTHORITY_TRANSITION` |
| Archive B1 fixed party size | `SUPERSEDED_BY_KAKEMAN89` |
| Four-level Tho Yor Foundry plan | Provisional spatial organization — **not** Legends lore |

---

## 2. Purpose of the stress test

Validate whether the Arc I–accepted integrated structure can absorb material whose **best runnable depth is unevenly split** between primary guide and companion, without:

1. Promoting companion atmosphere into unsupported campaign canon
2. Losing character/Speaker texture during consolidation
3. Failing Local Completeness (Scene Cards, mechanics, contacts, factions, clues, consequences at point of use)
4. Breaking dual campaign-guide + GM-workbook usability
5. Creating unmanageable controlled repetition
6. Collapsing player agency into a mandatory screenplay
7. Leaving Calling → Speaker → Kesh design unexamined when Arc III actually requires sister-ship contact
8. Breaking Foundry mixed-hierarchy assumptions for a socially complex Act
9. Revealing template refinements Arc I did not expose
10. Hiding Arc III–specific weaknesses (contact casting, Omen timing flexibility, optional moon road)

**Success of this plan** = a reviewable outline + procedures + gates. **Success of a future Arc III pilot** (separately authorized) = candidate that preserves depth without becoming authoritative until cutover.

---

## 3. Current architecture and authority

Per [`ai/PROJECT_ARCHITECTURE.md`](../PROJECT_ARCHITECTURE.md):

1. **Primary authority:** `dawn-of-the-jedaii-campaign-guide.md`
2. **Approved companion:** `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md`
3. On **factual conflict**, the primary guide controls unless Kakeman89 explicitly supersedes
4. Differences in voice, detail, organization, atmosphere, or emphasis are **not** automatically factual conflicts
5. Files under `ai/`, `.cursor/`, and `reports/` are **operational** — not campaign canon
6. Arc I candidate at `ai/migration-workspace/arc-i-integrated-candidate.md` remains **provisional / non-authoritative**
7. **No authority transition** until Kakeman89 separately authorizes cutover
8. Generated outputs (`gmbinder/dawn-of-the-jedaii-gmbinder.md`, `foundry/dawn-of-the-jedaii.journal.json`) must not be hand-edited as sources

Until cutover, primary + companion remain the operating architecture.

---

## 4. Arc I lessons carried forward

From Arc I disposition ([`ai/plans/2026-08-26-campaign-decision-record.md`](2026-08-26-campaign-decision-record.md) Addendum 2026-08-27; [`reports/audits/arc-i-pilot-acceptance.md`](../../reports/audits/arc-i-pilot-acceptance.md)):

| Lesson | Carry into Arc III planning |
|--------|------------------------------|
| Act → Session → Scene | Required organization axis |
| Guide-workbook hybrid | Combined campaign guide + GM workbook presentation |
| Point-of-use Scene Cards | Local completeness; concise central refs |
| Controlled repetition | Allow local summaries; avoid full-chapter duplication |
| Source traceability | Every block → primary / companion / archive / connective |
| Variable party size | No fixed PC count; scalable scene guidance |
| Archive B1 | `SUPERSEDED_BY_KAKEMAN89` — not canon |
| Clear read-aloud | Concrete, restrained metaphor; separate from GM Notes |
| SW5e mechanics language | Verified ability/proficiency names; labeled campaign mechanics |
| Four-level Tho Yor | Provisional Foundry spatial plan for **ship** Acts — **not** Legends lore; Arc III is primarily surface/social (reuse only if Gate/ship return scenes need it) |
| Template flexibility | Guides, not mandatory empty forms |
| F-K-002 | Staged Tython reveal remains decided; production App C sync deferred until authority transition |
| F-H-001 | Direction decided; eight mappings **not invented** in Arc I; deferred here |
| Candidate posture | Future Arc III candidate must stay provisional/non-authoritative |

---

## 5. Arc III source inventory

**Planning inventory only — no migration.** Session applicability for Ch17 is **not** individually numbered in the primary guide; session IDs below are **proposed stress-test outline IDs** (see §10–§11), justified from arc goals + companion procedures.

### 5.1 Primary guide — Arc III spine and dependencies

| File | Heading / anchor | Authority | Arc III function | Proposed session IDs | Notes |
|------|------------------|-----------|------------------|----------------------|-------|
| `dawn-of-the-jedaii-campaign-guide.md` | `# 17 — Arc III: Survive & Contact (Sessions 7–11)` | Primary | Act overview | S7–S11 | CW-006; beat list |
| same | `## Goals` | Primary | Act goals | Act | Map wild; contact; resource conflict; omen crisis |
| same | `## Exploration loop` | Primary | Session engine | S7+ | scout → discovery → camp consequence |
| same | `## Contact scenarios` (1–4) | Primary | Contact menu | S8–S11 | Trade & mistrust; Resource war; Joint rite; Moon road optional |
| same | `## Mid-arc crisis — Omen of the Moons` | Primary | Mid-arc / bridge crisis | S9 default; Arc II alternate | Default Arc III S9; alternate end Arc II; no double-run (Kakeman89 2026-08-27) |
| same | `## End of arc` | Primary | Exit conditions | S11 | Map, ally+rival, scars, Level 11 |
| same | `# 06 — Power Groups & Factions` | Primary | Factions / rivals | S7–S11 | Listening Circle, Spear Lodge, Open Hand, Chasm Inquiry, Green Kin; antagonists; Reth Var, Sister Luma, Kresh, Yen-Ti |
| same | `# 08 — The Kwa Gate` | Primary | Optional moon road | S10–S11 optional | Activation rules; Map 4 |
| same | `# 09 — Calendar of the First Year` → `## Scene — The Counting Quarrel` | Primary | Seed only in Arc III | Arc IV primary; Arc III seed | Complete quarrel primarily Arc IV; Arc III may seed calendar incompatibilities only (Kakeman89 2026-08-27) |
| same | `# 10 — SW5e Campaign Rules` → `### Party Tho Yor calling (required)` | Primary | Calling → Kesh table | Design gate F-H-001 | Science→Anil … Skill→Vur Tepe; Balance/Akar not choosable |
| same | `# 14 — Adventure Path — Arc Overview` → `## Arc map` | Primary | Level / session band | Act | Arc III sessions 7–11; Level 11 |
| same | `# 16 — Arc II: Arrival & First Landing (Sessions 4–6)` → Session 6 bridge | Primary | Omen preview | Bridge | Bridge to Arc III / Omen preview |
| same | `# 05 — Tython Gazetteer` → continents / temple seeds | Primary | Exploration geography | S7+ | Continent play notes; do not name temples early |
| same | `# 21 — Great GM Scene Craft` Scene Cards: Tython camp at night; Force Storm (arrival); Ashla/Bogan surface; Silent Desert / temple seeds as needed | Primary | Point-of-use cards | As used | Exact titles under `## Description bank — campaign pillars` |
| same | `# 22 — Faces of the First Migration` → `## A. Eight Tho Yor Speakers` | Primary | Contact Arc III+ | S8+ | Speakers + rivals |
| same | `# 23 — Random Encounter Map Briefs` → `## Map 3 — Silent Desert: Mouth of the Cavern`; `## Map 4 — Kwa Gate Antechamber & Moon Threshold` | Primary | Maps | Optional S9–S11 | Map 3 / Map 4 |
| same | `# 02 — The Tython System Catalog` → `## Twin moons (later Ashla and Bogan)` | Primary | Naming timeline | Omen | Pre/post naming vocabulary |
| same | `# 10` → `## Optional: Imbalance Storm Clock` | Primary | Repeated mechanic | Act | Storm Clock |

### 5.2 Companion — Arc III runnable depth

| File | Heading / anchor | Authority | Arc III function | Notes |
|------|------------------|-----------|------------------|-------|
| `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md` | `# 5 — Faces in the Song` | Companion | Speaker texture; Arc III contact silhouettes | Defers full toolkits to Guide Ch 22 |
| same | `# 6 — The Green World` | Companion | Omen / continents / Storm-Scar context | Force Storm; Storm-Scar Clearing; First night / Omen; Continents as sensory tours; Kwa Gate sidebar |
| same | `# 7 — The Path Ahead` → `## Arc III — Survive & Contact (Sessions 7–11)` | Companion | **Primary runnable depth** for contact procedures | Exploration loop texture; four contact stories with Speaker recommendations; Omen speech order; End of Arc III |

### 5.3 Operational / audit sources

| Path | Role |
|------|------|
| `reports/audits/integrated-guide-content-crosswalk.yaml` | CW-006 Arc III mapped |
| `reports/audits/2026-08-26-findings-register.yaml` | F-G-002, F-H-001, F-K-002 |
| `reports/audits/2026-08-26-dawn-of-the-jedaii-project-critique.md` | Consolidation evidence |
| `reports/audits/2026-08-26-chatgpt-archive-vs-repo-gap-report.md` | Archive A6 related to F-H-001; not auto-canon |
| `ai/plans/2026-08-26-chatgpt-archive-content-pr-scope.md` | Archive treatment classes |
| `ai/migration-workspace/arc-i-integrated-candidate.md` | Structural precedent only — **do not modify** for this plan |
| `.cursor/rules/10-legends-continuity.mdc` | Legends authority order |
| `.cursor/rules/source-and-canon-control.mdc` | Source discipline (when researching lore) |

### 5.4 Inventory field checklist (required for future crosswalk rows)

For each source block, future Arc III crosswalk work must record (schema-compatible with existing crosswalk):

file; heading/anchor; current authority; Arc III function; Session applicability; Scene applicability; operational vs atmosphere content; mechanics; characters; factions; locations; clues; revelations; secrets; consequences; player-visible vs GM-only; overlap; factual conflict vs presentation-only; Legends classification; unresolved decision; proposed integrated destination; terminal treatment (§26).

**Do not invent missing locations.** Mark gaps `NEEDS_SOURCE` or `TBD`.

### 5.5 Speakers inventory (contact Arc III+) — mappings TBD

From `# 22 — Faces of the First Migration` / `## A. Eight Tho Yor Speakers` (companion `# 5` echoes):

| Speaker | Epithet (ship) | Notes |
|---------|----------------|-------|
| Senn-Vora | Quiet Peak | Party ship default |
| Horruhn | Green Deep | |
| Numa’Shar | Dancing Heat | Companion recommends for Trade & mistrust diplomacy |
| Iil / Vorr | Tide Law | Companion recommends for Resource war law path |
| Sari Tor | Open Plain | Companion recommends if honor is currency |
| Kael Rind | Broken Banner | |
| Yen-Ti | Counting Dark | Also rival Architect path |
| Sister Luma | White Vow | Rival Speaker path |

Rivals (Ch06 / Ch22): **Reth Var**, **Kresh the Red** (and related pressures).

**F-H-001:** Calling ↔ Speaker ↔ Kesh **unmapped**. Do not fill.

### 5.6 Calling → Kesh table (Ch10 — established; Speakers not attached)

| Calling | Future Kesh |
|---------|-------------|
| Science | Anil Kesh |
| Art | Bodhi |
| Healing | Mahara Kesh |
| Knowledge | Kaleth |
| Teaching | Padawan Kesh |
| Body | Stav Kesh |
| Mind | Qigong Kesh |
| Skill | Vur Tepe |

Balance / Akar Kesh **not choosable** (ninth Tho Yor already on Tython).

---

## 6. Audit findings driving the test

| ID | Status | Role in Arc III stress test |
|----|--------|-----------------------------|
| **F-G-002** | open | Core driver — companion holds runnable contact depth |
| **F-H-001** | deferred / `DEFERRED_TO_ARC_III` | Design procedure in §9 (Models A/B/C; prefer B); **mappings not assigned** |
| **CW-006** | mapped | Arc III act overview; companion richer procedures |
| **F-K-002** | decided; production `KEEP_CANDIDATE_ONLY_UNTIL_AUTHORITY_TRANSITION` | Player/GM knowledge — world already landed by Arc III, but primer/history must not silently rewrite |
| **F-P-002** | decided (pilot Arc I; Arc III second) | Sequencing authority |
| Archive **A6** | partial / related | Calling→Speaker→Kesh — consume only after F-H-001 design + Kakeman89 review |
| Archive **B1** | `SUPERSEDED_BY_KAKEMAN89` | Do not reintroduce fixed party size of 3 |

---

## 7. Arc III scope

**In scope for this plan:**

- Source inventory and proposed Act → Session → Scene outline (planning IDs)
- Companion-integration and point-of-use policies for Arc III
- F-H-001 **design procedure** (empty mapping table)
- Map / Foundry / GMB **planning** (no assets created)
- Crosswalk procedure and validation gates
- Future candidate path recommendation (file **not** created)
- Phased implementation outline for a **later** authorization

**Arc III dramatic band (repository):** Sessions **7–11**; milestone **Level 11** after first major inter-camp crisis (`# 14` Arc map; Ch17 End of arc).

---

## 8. Explicit exclusions

This plan does **not** authorize:

- Creating `ai/migration-workspace/arc-iii-integrated-candidate.md`
- Migrating Arc III content into any candidate or manuscript
- Editing `dawn-of-the-jedaii-campaign-guide.md` or `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md`
- Assigning the eight Calling → Speaker → Kesh mappings
- Modifying the Arc I candidate
- Implementing A2 Chamber content
- Foundry generation / personal Foundry game edits
- GM Binder generation / saved remote GMB overwrite
- GM Binder pagination optimization (F-M-003 remains deferred)
- Marking Arc III implementation authorized
- Commit / push / PR of this plan unless separately authorized
- Fabricating scene prose, read-aloud drafts, or invented map assets
- Completing the Counting Quarrel in Arc III (seed only; complete quarrel primarily Arc IV unless future play + Kakeman89 authorization)

---

## 9. Calling → Speaker → Kesh design procedure

**Finding:** F-H-001 — Speakers not crosswalked to Session 0 callings / Kesh.  
**Status:** `DEFERRED_TO_ARC_III` / design deferred; **mappings remain unassigned**. No mapping becomes campaign canon in this plan.

### 9.1 Direction already decided (do not reopen)

From [`ai/plans/2026-08-26-campaign-decision-record.md`](2026-08-26-campaign-decision-record.md):

- Create an explicit **default** Calling → Speaker → Kesh crosswalk
- Treat as **recommended** casting arrangement
- Allow **GM substitution** unless later fixed as campaign canon
- **Do not invent** the eight mappings in decision-only or planning-only phases without a separate design + Kakeman89 review

### 9.1a Design models (Kakeman89 2026-08-27) — do NOT assume fixed 1:1

Future F-H-001 analysis must compare these models. **Do not manufacture evidence.** Empty §9.6 table stays empty until a separately authorized design draft.

| Model | Description | Role in analysis |
|-------|-------------|------------------|
| **A — Fixed triple** | Each Calling locks permanently to one Speaker and one destined Kesh | Evaluate when strong primary-guide evidence supports a fixed campaign relationship |
| **B — Recommended casting** | Default Calling → Speaker → Kesh recommendation; GM may substitute unless later fixed as canon | **Kakeman89 preferred direction** for design analysis |
| **C — Independent systems** | Calling, Speaker contact casting, and Kesh destiny treated as loosely coupled; no forced 1:1 | Analysis may recommend Model C for **specific Speakers** when repository evidence is insufficient for A or B |

**Rules:**

- Prefer Model B as the working design posture for the crosswalk as a whole.
- Per-Speaker or per-Calling cells may recommend Model C when evidence is thin — mark `unresolved` / Model C, do not invent links.
- Scenario casting hints (companion Trade / Resource war Speakers) are **not** F-H-001 resolutions.
- No mapping enters primary-guide prose or becomes canon from this plan alone.

### 9.2 Evaluation criteria (required for every future proposed mapping)

Each candidate assignment must be evaluated against **all** of:

1. The eight approved Callings (Ch10 table)
2. Corresponding future Kesh identities (Ch10 / Ch05 / Ch07 fold crosswalk)
3. Each Speaker’s established epithet (Ch22)
4. Each Speaker’s established personality / want–fear–lever (Ch22)
5. Established culture or species (Ch03 culture cards; Ch22)
6. Philosophical alignment (Ashla/Bogan/Balance posture as portrayed — not forced)
7. Dramatic function in Arc III+ contact scenarios
8. Relevant Arc III contacts (companion four stories; Ch17 contact menu)
9. Existing clues / hooks in repository
10. Existing **primary-guide** evidence
11. Approved **companion** evidence
12. Legends compatibility (do not invent Legends “facts”)
13. Campaign flexibility (recommended vs fixed)

### 9.3 Relationship classes (required labels)

Every future cell must use one of:

| Label | Meaning |
|-------|---------|
| fixed campaign relationship | Canon lock after Kakeman89 approval |
| recommended default relationship | Default casting; GM may substitute |
| interchangeable GM option | Explicitly swappable |
| unresolved | Insufficient evidence |
| contradictory | Sources conflict — stop |
| unsupported | Would require invention |

### 9.4 Anti-superficial-matching rule

**Prohibit** matching on epithet wordplay alone.

Example (from brief): an epithet that *sounds* scholarly must **not** automatically receive the **Knowledge** calling without additional campaign evidence (personality, hooks, continental affinity, Arc III contact function, Ch06 faction adjacency, etc.).

Require a **written mapping rationale** for every proposed assignment citing repository headings.

### 9.5 Review gate

**Kakeman89 review required** before any mapping becomes campaign canon or enters primary-guide prose.

### 9.6 Empty mapping table (do not fill in this plan)

| Calling | Recommended Speaker | Destined Kesh | Relationship class | Rationale | Notes |
|---------|---------------------|---------------|--------------------|-----------|-------|
| Science | TBD | Anil Kesh | unresolved | Design step required | Do not invent |
| Art | TBD | Bodhi | unresolved | Design step required | Do not invent |
| Healing | TBD | Mahara Kesh | unresolved | Design step required | Do not invent |
| Knowledge | TBD | Kaleth | unresolved | Design step required | Do not invent |
| Teaching | TBD | Padawan Kesh | unresolved | Design step required | Do not invent |
| Body | TBD | Stav Kesh | unresolved | Design step required | Do not invent |
| Mind | TBD | Qigong Kesh | unresolved | Design step required | Do not invent |
| Skill | TBD | Vur Tepe | unresolved | Design step required | Do not invent |

Party-ship default remains **Senn-Vora / Quiet Peak** with generic substitution guidance until mapping design completes (Ch22; Arc I precedent).

### 9.7 Companion Speaker recommendations (contact casting — not calling maps)

Companion `# 7` suggests Speakers for **scenarios**, not Calling locks:

- Trade & mistrust → Numa’Shar (diplomacy) or Sari Tor (honor currency)
- Resource war → Reth Var (raid pressure); Iil and Vorr (law first)

These are **scenario casting hints**, not F-H-001 resolutions.

---

## 10. Proposed Act structure

**Note:** Primary `# 17` does **not** number Sessions 7–11 individually. Sessions 7–11 below are **Kakeman89-approved provisional operational structure** (2026-08-27) — not preexisting campaign canon. Scene/session names remain **provisional** until a future candidate is separately authorized. Scene names below are **planning IDs**, not authored prose.

### Act at a Glance (planning)

| Field | Content |
|-------|---------|
| Act | Arc III — Survive & Contact (Sessions 7–11) |
| Level band | Exit at **Level 11** |
| Central dramatic question | Can strangers who share a sky become neighbors without conquest or erasure? |
| Starting state | Post–Arc II named camp near Session 0 calling seed; Level 10; sister ships as smoke/silhouettes; moons may or may not yet be named (Omen default = S9; alternate = closing Arc II) |
| Active factions (crystallizing) | Listening Circle; Spear Lodge; Open Hand Healers; Chasm Inquiry; Green Kin (Ch06) |
| Important characters | Eight Speakers (Ch22); rivals Reth Var, Sister Luma, Kresh, Yen-Ti |
| Important locations | Party camp; scouted near wild; optional Silent Desert (Map 3, in-scope); optional Kwa Gate (Map 4, advanced); continent seeds described as wonder without Kesh names early (Ch05) |
| Revelations | Sister Speakers as people; Ashla/Bogan locked for speech + moon names (if Omen runs); faction flags; optional moon-road proof |
| GM secrets | Builder/Kwa ambiguities remain open (Ch04/Ch08); temple names withheld until earned |
| Repeated mechanics | Exploration loop; Storm Clock; optional Gate activation; faction pressure |
| Expected developments | Scout discoveries → trade/mistrust contact → Omen (default S9) → Resource War **or** Joint Rite (S10 by prior state) → scars + Level 11 |
| Alternate developments | Skip optional Map 3/4; run Omen at Arc II end (then Resource War as primary S9); seed Counting Quarrel only; refuse Gate |
| Possible end states | Ally+rival camps; incomplete map; failed contact; purge scars; Gate never opened (valid completion) or opened/sealed if advanced path used |
| State carryover | Sketch map; allied/rival flags; Storm Clock; moon vocabulary lock; Speaker debts; Level 11 → Arc IV |
| Required preparation | Ch17 + companion Arc III; Ch06 playbooks; Ch22 Speakers; Ch21 camp/Omen cards; Map 3/4 if used |
| Foundry package | Provisional mixed hierarchy (§23) — planning only; do not generate |

---

## 11. Proposed Session structure

**Operational default (Kakeman89 2026-08-27):** Sessions 7–11 approved as provisional operational structure. Scene/session names remain provisional until candidate implementation is separately authorized.

### Session 7 — Scout loop, first discoveries, camp consequences

| Field | Planning content |
|-------|------------------|
| Purpose | Prove the wild can be scouted; establish exploration loop |
| Starting situation | Post-landing neighborhood; camp claimed (Arc II Session 6) |
| Required preparation | Ch17 Exploration loop; Ch05 near geography for calling seed; Ch21 Tython camp at night |
| Active characters / factions | Camp NPCs; optional distant smoke (Spear Lodge / Green Kin markers) |
| Essential clues | Food/poison/rival smoke/temple-seed landmark (wonder only) |
| Optional discoveries | Ruined pre-pilgrim traces (Ch17) |
| Suggested flow | Scout → discovery → return → camp consequence |
| Alternate flow | Short scout if Omen already pending; Theater of the Mind valleys |
| Scenes (IDs) | **Scout Valley**; **Rival Smoke Ridge**; **Camp Return Consequence** |
| Failure / partial | Lost scouts; predator follow; ration fight without full map |
| End states | Partial sketch map; first consequence scar |
| State updates | Map notes; Storm Clock tick TBD by play |

### Session 8 — Trade and mistrust contact

| Field | Planning content |
|-------|------------------|
| Purpose | First sister-camp contact without conquest |
| Starting situation | Border between camps; language friction |
| Required preparation | Ch17 Contact scenario 1; Ch22 Speaker toolkit; companion contact story 1 |
| Active characters | One+ Speaker (casting TBD — Numa’Shar or Sari Tor recommended by companion for *scenario*, not calling map); party Speaker Senn-Vora as local default |
| Essential clues | Gift = intelligence; stolen tool ambiguous meaning |
| Suggested flow | Language montage → gift exchange → crisis of mistrust → PC broker |
| Alternate flow | Hostile first meeting; honor duel path (Sari Tor) |
| Scenes (IDs) | **Border Trade**; **Stolen Tool Diplomacy** |
| Failure / partial | Trade fails; insult escalates; temporary truce only |
| End states | Soft ally, wary neighbor, or open rivalry seed |

### Session 9 — Omen of the Moons (DEFAULT)

| Field | Planning content |
|-------|------------------|
| Purpose | Mid-arc crisis: vocabulary lock + purge stop (**default** Arc III placement) |
| Starting situation | Dual moons clear; Speakers ready to declare |
| Required preparation | Ch17 Mid-arc crisis; Ch02 moon timeline; Ch21 camp read-alouds; companion Omen order |
| Active characters | Speakers; Sister Luma / Kresh pressure as applicable |
| Suggested flow (DEFAULT) | Speakers declare Ashla/Bogan for Force speech → name moons → emotions spike → **Purge Stop** |
| Alternate — Omen already ran closing Arc II | **Do not rerun Omen.** Use **Resource War** as primary Session 9 content; preserve Omen consequences and vocabulary. Session 10 then uses Joint Rite / faction crystallization / approved contact consequence |
| Alternate — Omen deferred to Arc II close only | Sources allow Omen at end of Arc II; if so, apply the “already ran” branch above for Arc III |
| Scenes (IDs) | **Omen Night Speech**; **Purge Stop**; **or** (if Omen already done) **Spring Claim** / Resource War scenes |
| Failure / partial | Purge partially succeeds; Storm Clock advances; (Resource War branch) spring poisoned / contested |
| End states | Vocabulary locked; scars; or (Resource War branch) spring treaty/war seed |

### Session 10 — Resource War OR Joint Rite (selected by prior campaign state)

| Field | Planning content |
|-------|------------------|
| Purpose | Second major contact beat chosen from prior state: resource conflict **or** empirical Balance / joint rite; deepen neighbor politics |
| Starting situation | Post-Omen (or post–Resource War if Omen ran in Arc II); optional hunger for myth |
| Required preparation | Ch17 Contact scenarios 2–3 (and 4 if optional moon road); Ch06 coalitions; optional Ch08 + Map 4; optional Map 3 |
| Active characters / factions | Second Speaker contact; Reth Var / Iil & Vorr for Resource War; Listening Circle / Spear Lodge crystallization for Joint Rite |
| Selection rule | If Omen ran in S9 (default): choose **Resource War** or **Joint Rite** from table state (water conflict pressure vs rite/Balance opportunity). If Omen already ran in Arc II and Resource War filled S9: use **Joint Rite / faction crystallization / approved contact consequence** |
| Suggested flow A (Resource War) | **Spring Claim** → raid vs law → broker water/blood/third camp |
| Suggested flow B (Joint Rite) | **Joint Rite** under local Force weather → faction flag moments |
| Optional advanced | **Map 3** Silent Desert approach; **Map 4** Kwa Gate / moon road (prerequisites, refuse/defer, failure, never-open completion path — see §22) |
| Alternate | Skip Gate; **seed** Counting Quarrel calendar incompatibilities only (do not complete quarrel — Arc IV) |
| Scenes (IDs) | **Spring Claim** and/or **Joint Rite**; **Faction Flag Camp**; optional **Map 3 Approach**; optional **Map 4 Moon Road** |
| Failure / partial | Spring contested; rite fails to calm weather; Gate refuse/defer/fail; calendar seed unresolved |
| End states | Second ally/rival; optional Gate foreshadow paid off or permanently bypassed |

### Session 11 — Crisis resolution, scars, neighborhood map review, Level 11

| Field | Planning content |
|-------|------------------|
| Purpose | Close Arc III victory conditions; inventory scars/alliances/rivalries; review neighborhood map; milestone; hand off to naming politics |
| Starting situation | Unresolved contact debts / scars / map holes |
| Required preparation | Ch17 End of arc; companion End of Arc III; Ch14 Level 11 |
| Suggested flow | Resolve open crisis → inventory scars → neighborhood map review → Level 11 |
| Alternate | Cliff into Arc IV with unfinished Gate or seeded calendar disputes |
| Scenes (IDs) | **Scar Council**; **Neighborhood Map Seal**; optional cleanup of prior IDs |
| Failure / partial | No ally **or** no rival (guide wants at least one each — record deficit); map incomplete |
| End states | Ally+rival; scars; Level 11; factions flagged → Arc IV Balance & the Name |
| State carryover | Document debts, vocabulary lock, Storm Clock, Speaker relationships (still without inventing Calling maps) |

---

## Historical note — pre-approval Session 9/10 framing

Prior draft treated Session 9 as “Omen **or** Resource war (timing flexible)” with Joint Rite primarily in Session 10. That framing is **superseded as operational default** by Kakeman89 2026-08-27 (Omen default = S9; S10 = Resource War OR Joint Rite by prior state; Omen-already-ran branch above). Retained here only as planning history — do not use as current baseline.

## 12. Proposed Scene structure

Use Arc I–accepted Scene template ([migration plan §15](2026-08-26-integrated-gm-guide-migration.md)) with **template flexibility** (no empty sections).

### Planning Scene IDs (not prose)

| Scene ID | Likely session | Primary sources | Companion sources | Map |
|----------|----------------|-----------------|-------------------|-----|
| Scout Valley | S7 | Ch17 Exploration loop; Ch05 | `# 7` exploration loop | Theater / shared |
| Rival Smoke Ridge | S7 | Ch17 discoveries; Ch06 | `# 7` rival smoke | Theater |
| Camp Return Consequence | S7 | Ch17 loop; Ch21 Tython camp at night | `# 6` First night | Camp |
| Border Trade | S8 | Ch17 Contact 1; Ch22 | `# 7` Trade and mistrust | Theater / border |
| Stolen Tool Diplomacy | S8 | Ch17 Contact 1 | `# 7` | Theater |
| Omen Night Speech | S9* | Ch17 Mid-arc crisis; Ch02; Ch21 camp | `# 6` / `# 7` Omen | Camp |
| Purge Stop | S9* | Ch17 Mid-arc crisis | `# 7` party job | Camp |
| Spring Claim | S9* | Ch17 Contact 2; Ch06 | `# 7` Resource war | Theater |
| Joint Rite | S10 | Ch17 Contact 3 | `# 7` Joint rite | Camp / wild |
| Faction Flag Camp | S10 | Ch06 | `# 7` End texture | Camp |
| Map 3 Approach | optional | Ch23 Map 3; Ch21 Qigong / Silent Desert | `# 6` Thyr | Map 3 |
| Map 4 Moon Road | optional | Ch08; Ch23 Map 4; Ch21 Ashla/Bogan surface | `# 6` Kwa sidebar; `# 7` Moon road | Map 4 |
| Scar Council | S11 | Ch17 End of arc | `# 7` End of Arc III | Camp |

\*Omen **default** = Arc III Session 9. Alternate = closing Arc II (Ch16 bridge). If Omen already ran in Arc II: do not place Omen scenes in S9; use Resource War / Spring Claim instead.

### Template field applicability (Arc III social/exploration scenes)

| Field | Typical class for Arc III contact/scout scenes |
|-------|-----------------------------------------------|
| Scene Purpose / Trigger / Immediate Situation | **required** |
| Read-Aloud | **recommended** (use Ch21 where exists; revise to Arc I clarity standard if migrated later) |
| Scene Card | **required** for operational scenes |
| Location / Present Characters / Objectives / Opposition | **required** |
| Mechanics | **required when applicable**; else omit |
| Clues / Discoveries | **required when applicable** |
| Roleplaying Guidance | **recommended** for Speaker scenes |
| Failure / Partial / Alternate Approaches / Transition / Consequences | **required** |
| Foundry Assets | **recommended** when maps exist |
| Source Traceability | **required** operationally |

Unnecessary fields: omit (template flexibility).

**Do not write final Arc III scene prose in this planning task.**

---

## 13. Point-of-use policy

Apply Local Completeness Principle from migration plan §16:

- Runnable Arc III scenes must include what the GM needs to run **that** scene (Speaker want, contact stakes, loop consequence, Omen order, Storm Clock note)
- Full Speaker biographies and complete faction histories → **summarize locally + retain centrally** (Ch22 / Ch06)
- Companion procedural depth (contact stories, Omen speech order) must not remain **only** in companion if a future integrated candidate claims table-runnability — but **integration is not authorized by this plan**
- Cross-references must not replace essential adjudication information

**Stress-test question:** Can Ch17 beat titles + Ch21 cards alone run Arc III, or does F-G-002 force companion consolidation for Local Completeness?

---

## 14. Controlled-repetition policy

Carry forward migration plan §17:

**Allow local repetition** for: scene-relevant NPC wants; short location cues; Omen three-step order; Storm Clock; essential clues; immediate consequences.

**Prefer central reference** for: full Ch22 Speakers; full Ch06 faction playbooks; Ch08 Gate rules; Ch10 calling table; long Ch21 Inspiration blocks.

**Contradiction detection:** If primary and companion disagree on **facts**, primary controls; record conflict. Presentation-only richness (companion texture) is not a defect.

---

## 15. Companion-integration policy

| Rule | Application |
|------|-------------|
| Factual conflict | Primary guide wins unless Kakeman89 supersedes |
| Atmosphere / procedure depth | Companion may supply Local Completeness candidates |
| **Required operational procedures** | Companion Arc III **operational procedures** are **required migration candidates** for Local Completeness when migration is later authorized — do **not** leave these only in companion |
| Required procedure set (minimum) | Exploration loop; first-contact; trade/mistrust escalation; resource-war alternatives; joint-rite; Omen event order; scene-relevant Speaker motivations; Arc-ending scars/alliances/rivalries |
| Atmospheric prose | **Selective** migration + apply Arc I **clarity standard** (not wholesale atmosphere dump) |
| Classification | Label migrated companion blocks as companion-sourced in crosswalk |
| No silent canon promotion | Atmosphere does not become Legends or fixed canon without review |
| Preserve texture | Speakers’ wants, sensory continents, Omen speech order must not flatten into titles only |
| Stress-test metric | Integrated outline must show where companion depth lands (Act / Session / Scene / central) |
| Authorization | Consolidation into a candidate is **not** authorized by this plan — policy only |

---

## 16. Original-connective-text policy

Future Arc III candidate may need short connective bridges (session stitching). Rules:

- Label as `ORIGINAL_CAMPAIGN_MATERIAL` / connective — not Legends
- Do not invent lore facts, mappings, or mechanics
- Prefer stitching existing Ch17 / companion beats over new plot
- Kakeman89 review before connective text is treated as approved campaign material

---

## 17. Legends policy

Per `.cursor/rules/10-legends-continuity.mdc` and migration plan Legends policy:

- Authority order: Kakeman89 decisions → repository-designated sources → Legends → labeled original
- Do not import Disney canon
- Mark unverified claims `NEEDS_SOURCE`
- **Four-level Tho Yor Foundry structure** = provisional spatial organization for play aids — **not** `LEGENDS_VERIFIED` lore
- Speakers, callings, factions as in approved campaign materials remain campaign authority; do not retroactively rewrite for external Legends variants without reporting conflict first
- Classify new lore claims using required labels (`LEGENDS_VERIFIED`, `CAMPAIGN_APPROVED`, etc.)

---

## 18. GM/player knowledge policy

| Topic | Arc III posture |
|-------|-----------------|
| World identity | By Arc III, table has landed; Tython may be known in play — do not rewind F-K-002 staged reveal for pre-reveal materials |
| F-K-002 production App C | Remains `KEEP_CANDIDATE_ONLY_UNTIL_AUTHORITY_TRANSITION` — do not edit production primer solely for sync during preserved-source period |
| Moon names | Before Omen: twin lights / clean & hungry; after Speakers lock: Ashla/Bogan for Force speech **and** moons (Ch02 / Ch17 / Ch21) |
| Temple / Kesh names | Describe wonder; withhold temple names until earned (Ch17 / companion) |
| Gate / builders | GM-only secrets per Ch08 / Ch04; player discoveries via play |
| Speakers | Player-facing when contacted; full Inspiration GM-only |

---

## 19. Mechanics-language policy

Carry Arc I accepted standards:

- Use DND5e/SW5e-style wording
- Verify SW5e ability and proficiency names against campaign Ch10 / SW5e sources before future drafts
- Clear DCs only where authorized / present in sources — do not invent DCs in planning
- Explicit success and failure results when mechanics exist
- Label **campaign mechanics** (Storm Clock, Gate activation table fiction, boons) as such
- No unnecessary ability checks
- No unsupported conditions, damage, or exhaustion as defaults
- Gate activation: follow `# 08 — The Kwa Gate` (`## Activation key (table fiction)`, travel, Ashla/Bogan trials) — do not invent new rules here

---

## 20. Read-aloud policy

Carry Arc I revision standards:

- Concrete and comprehensible
- Restrained metaphor
- No abstract poetic phrasing that obscures physical meaning
- No dictated player-character emotion
- Clear separation between **Read-Aloud** and **GM Notes / Inspiration**
- Prefer existing Ch21 / companion read-alouds as sources for future migration; revise to clarity standard only when authorized

**Do not draft final Arc III read-alouds in this plan.**

---

## 21. Party-scaling policy

- **No fixed party size**
- Archive B1 (`3 PCs LOCKED`) remains `SUPERSEDED_BY_KAKEMAN89` — not campaign canon
- Scalable scene guidance required for scout teams, contact envoys, and purge intervention
- Boon policy remains Arc I decision (unique starting boons up to six Ch11 cards; no invented boons for large parties)
- Larger parties → more narrative complications / parallel contacts, not automatic roll inflation

---

## 22. Map strategy

| Location / need | Dedicated map | Shared | Theater | Notes |
|-----------------|---------------|--------|---------|-------|
| Party camp / night | Prefer reuse Map 2 region or abstract camp | shared possible | yes | Ch21 Tython camp at night |
| Scout valleys / springs / ridges | optional | — | **default** | Ch17 discoveries |
| Silent Desert approach | **Map 3** | — | fallback | Optional, **in-scope** (Kakeman89 2026-08-27) |
| Kwa Gate / moon road | **Map 4** | — | fallback | Optional **advanced**; not required path |
| Ashla / Bogan surface | optional / Theater | — | often enough | Ch21 Ashla/Bogan surface cards |
| Continent temple seeds | deferred detailed maps | — | yes | Wonder only in Arc III |

### Map 3 — Silent Desert (Kakeman89 2026-08-27)

- **Optional but in-scope** for future Arc III candidate work.
- Future candidate must support: dedicated map; Theater fallback; bypass; **consequences for not visiting**.
- **Not required** for Arc III completion.

### Map 4 — Kwa Gate (Kakeman89 2026-08-27)

- Optional **advanced** content; **not** a required path.
- Must include: prerequisites; refusal/defer; failure handling; consequences; and an Arc III **completion path that never opens the Gate**.
- Must **not** replace the social-contact focus of Arc III.
- Ordinary contact/camp play remains Theater-OK without Map 4.

Per location planning fields (for future work): dedicated vs shared vs Theater; Foundry Scene vs journal-only; Levels only if vertical overlap matters; social/exploration/combat relevance; player-visible vs GM-only; pins; transitions; required/optional/deferred assets.

**Do not create maps or assets in this task.**

---

## 23. Foundry strategy

**Provisional mixed hierarchy (Kakeman89 2026-08-27) — do not generate:**

1. Arc III Overview
2. Session 7
3. Session 8
4. Session 9
5. Session 10
6. Session 11
7. Arc III Contacts and Speakers
8. Player Handouts

**Journal / Scene page rules:**

- **Default:** Anchored Scene headings **inside** Session journal pages.
- **Separate Scene journal page** only when: dedicated map; substantial mechanics; extensive GM-only info; reusable content; or enough material for independent navigation.
- Map 3 / Map 4 **may** get dedicated Foundry Scenes when used.
- Ordinary contact / camp = **Theater OK** (no mandatory dedicated Foundry Scene).

Carry Arc I preference:

- Prefer **linked Foundry Scenes** for major spatial groupings when maps are used (optional Map 3; optional Map 4)
- Use **Levels within a Scene** only when functional vertical overlap matters
- Do not add verticality merely because the module supports it
- Do not create empty final Scenes without usable assets
- Four-level Tho Yor plan remains **ship-centric provisional spatial design** — not assumed for Tython surface Arc III
- F-N-001 disposable-world import gate remains relevant before trusting production Foundry updates

**Do not generate Foundry packages in this task.**

---

## 24. GM Binder treatment

- Future Arc III integrated pages would regenerate from authorized manuscript/candidate via `tools/md_to_gmbinder.py`
- Do not hand-edit `gmbinder/dawn-of-the-jedaii-gmbinder.md`
- Do not overwrite saved remote GM Binder document
- Ch22 Faces must remain intact in generator (F-M-002 closed — preserve)
- Arc III contact depth may increase page count — layout is a later concern

---

## 25. Pagination deferral

- F-M-003 / GM Binder pagination optimization remains **`DEFERRED_PARTIAL`**
- Validator infrastructure preserved
- Arc III stress-test planning does **not** resume pagination work
- Do not optimize layout during Arc III planning or future pilot unless separately authorized

---

## 26. Crosswalk procedure

Extend [`reports/audits/integrated-guide-content-crosswalk.yaml`](../../reports/audits/integrated-guide-content-crosswalk.yaml) schema for Arc III blocks.

**Terminal treatments (every source block must receive one):**

| Treatment | Meaning |
|-----------|---------|
| MIGRATE | Move into integrated spine |
| CONSOLIDATE | Merge overlapping primary+companion |
| SUMMARIZE_LOCALLY | Short local + central full |
| RETAIN_CENTRALLY | Stay in Part II/IV-style reference |
| PRESERVE_DISTINCT | Keep separate on purpose |
| EXCLUDE | Out of Arc III integrated scope |
| DEFER | Later Act or later decision |
| NEEDS_DECISION | Kakeman89 required |

**CW-006** already proposes `CONSOLIDATE_CANDIDATE` for Ch17 with companion overlap — confirm or revise during future crosswalk fill; do not silently drop companion procedures.

Distinguish in notes: factual authority vs companion presentation vs original connective vs archive vs future placement vs current content defect. **Do not** call material defective merely because destination type changes.

**Planning-only:** new Arc III crosswalk rows may be added when authorized as planning updates; this document does not itself invent filled mapping rows for F-H-001.

---

## 27. Source traceability

Every future migrated Arc III block must record:

- Source file + exact heading
- Crosswalk ID
- Authority class (primary / companion / archive / connective)
- Legends / campaign classification when lore-bearing
- Whether player-visible or GM-only

Operational traceability lives in crosswalk / candidate metadata — not dumped into spoken read-alouds.

---

## 28. Candidate strategy

**Recommended future path (do not create now):**

`ai/migration-workspace/arc-iii-integrated-candidate.md`

**Required posture if later authorized:**

- Provisional
- Non-authoritative
- Preserve both source manuscripts
- Source traceability on every block
- Accepted guide-workbook structure
- Preserve player agency (alternates, failures, bypasses)
- Preserve GM/player knowledge boundaries
- **No unsupported F-H-001 mappings**
- No silent Legends changes
- Variable party size; Arc I read-aloud and mechanics standards
- Four-level Tho Yor not mislabeled as Legends

Until creation is authorized, Arc III remains plan-only.

---

## 29. Implementation phases

**Future only — not authorized by this plan.**

| Phase | Name | Intent | Exit gate |
|-------|------|--------|-----------|
| A | Inventory lock | Complete Arc III crosswalk rows for all §5 blocks | Gate 1–2 |
| B | F-H-001 design draft | Fill §9.6 with rationales — still provisional | Gate 3 (Kakeman89) |
| C | Outline approval | Act/Session/Scene IDs approved | Gate 4 |
| D | Candidate build | Create `arc-iii-integrated-candidate.md` under migration skill/auth | Separate auth |
| E | Audits | Agency, Legends, continuity, mechanics, read-aloud, PoU, repetition, content-loss | Gates 5–14 |
| F | Outputs | Foundry/GMB pilot outputs if authorized | Gates 11+ |
| G | Disposition | Accept / revise / reject Arc III pilot | Gate 15 |

No phase auto-starts after plan creation.

---

## 30. Validation gates

| # | Gate | Pass condition |
|---|------|----------------|
| 1 | Arc III source inventory | All §5 blocks listed with exact paths/headings; gaps marked TBD/NEEDS_SOURCE |
| 2 | Arc III crosswalk completeness | Every block has terminal treatment; none silently dropped |
| 3 | Calling → Speaker → Kesh design approval | Kakeman89 reviewed mappings; none invented without rationale |
| 4 | Act/Session/Scene outline approval | Kakeman89 accepts or revises §10–§12 — **planning baseline accepted 2026-08-27**; candidate still not authorized |
| 5 | Companion-depth preservation | F-G-002 addressed — procedures not lost |
| 6 | Player-agency review | Alternates/failures/bypasses documented |
| 7 | Legends review | Classifications correct; four-level Tho Yor not as Legends |
| 8 | Continuity review | Omen timing, moon vocabulary, temple-name withholding intact |
| 9 | Mechanics review | SW5e language; no invented unsupported costs |
| 10 | Read-aloud quality review | Clarity standards applied when prose exists |
| 11 | Map and Foundry review | Map 3/4 optional paths; no empty Scenes |
| 12 | Point-of-use completeness | Local Completeness for contact/Omen/scout scenes |
| 13 | Controlled repetition | No contradictory local facts |
| 14 | Content-loss comparison | Primary+companion coverage matrix |
| 15 | Kakeman89 planning approval | Explicit go/no-go for any later implementation |

**No Arc III implementation begins automatically after this plan exists.**

---

## 31. Rollback

If a future Arc III candidate or outputs are created and then rejected:

1. Delete or quarantine candidate under Kakeman89 direction (do not delete source manuscripts)
2. Leave primary + companion authoritative
3. Revert generated outputs by regenerating from primary guide only
4. Preserve this plan and crosswalk evidence as operational history
5. Do not silently “fix” source manuscripts to match a rejected candidate

---

## 32. Kakeman89 review points

1. Approve this stress-test plan as planning baseline? — **DECIDED 2026-08-27:** `PLANNING_BASELINE_APPROVED` / `PLANNING_AUTHORIZED_ONLY`; migration **NOT** authorized
2. Approve or revise Sessions 7–11 outline (§11) despite Ch17 lacking per-session numbers? — **DECIDED 2026-08-27:** Sessions 7–11 approved as provisional operational structure (see §11); scene/session names remain provisional
3. Authorize F-H-001 design draft session (still no prose)? — **OPEN** (design models A/B/C recorded; Model B preferred; mappings still empty)
4. Which companion procedures are mandatory for Local Completeness vs optional atmosphere? — **DECIDED 2026-08-27:** required operational procedures listed in §15; atmospheric prose selective + clarity standard
5. Omen default timing: prefer Arc II end preview vs Arc III Session 9? — **DECIDED 2026-08-27:** default = Arc III Session 9; alternate = closing Arc II; no rerun if already completed
6. Optional Map 3 / Map 4: in-band for stress-test candidate or explicitly deferred? — **DECIDED 2026-08-27:** Map 3 optional in-scope; Map 4 optional advanced; neither required for completion (see §22)
7. Counting Quarrel: allow late Arc III in candidate or keep Arc IV-primary? — **DECIDED 2026-08-27:** complete quarrel primarily Arc IV; Arc III may seed only
8. When (if ever) create `arc-iii-integrated-candidate.md`? — **OPEN** — creation **not** authorized
9. Any Speakers that must be **fixed** to callings vs all recommended? — **OPEN** — Model B preferred direction; per-Speaker Model C allowed when evidence insufficient; no mappings filled
10. Link updates required in migration plan §28/§37 post-pilot options? — **OPEN**

---

## 33. Remaining decisions

| Decision | Status |
|----------|--------|
| Eight Calling → Speaker → Kesh mappings | **Unresolved** — empty table §9.6; Model B preferred for analysis; Model C allowed per insufficient evidence; **no mapping approved** |
| Arc III candidate creation | **Not authorized** |
| Companion consolidation depth for Ch17 | **Decided as policy** (§15 required procedures) — migration still **not** authorized |
| Omen default session placement | **Decided** — default S9; alternate Arc II close; no double-run |
| Map 3 / Map 4 in first Arc III candidate | **Decided as scope** (§22) — optional paths; not required; candidate still not authorized |
| Sessions 7–11 provisional structure | **Decided** — operational baseline; names provisional |
| Counting Quarrel | **Decided** — Arc IV primary complete quarrel; Arc III seed only |
| Foundry journal hierarchy | **Decided provisional** (§23) — do not generate |
| F-K-002 production App C sync | `KEEP_CANDIDATE_ONLY_UNTIL_AUTHORITY_TRANSITION` |
| A2 Chamber | Unauthorized (unrelated; keep out) |
| Pagination | Remains deferred |
| Arc III migration skill / phase start | **Not authorized** |
| F-H-001 design draft authorization | **Still required** before filling §9.6 |

---

## 34. Risks

| Risk | Mitigation |
|------|------------|
| Losing companion contact depth (F-G-002) | Explicit CONSOLIDATE treatments; Gate 5 |
| Inventing F-H-001 mappings under schedule pressure | Empty table; Gate 3; anti-epithet rule |
| Railroading contact order | Document alternate flows; agency Gate 6 |
| Omen double-run (Arc II + Arc III) | Timing flexibility note; continuity Gate 8 |
| Optional Gate swallowing social arc | Mark Map 4 optional; skip path required |
| Mislabeling Foundry spatial plans as Legends | Explicit §4 / §17 / Gate 7 |
| Reintroducing fixed party size | B1 superseded; §21 |
| Scope creep into Arc IV Naming | End Arc III at Level 11 scars; Counting Quarrel **seed only** in Arc III; complete quarrel primarily Arc IV |
| Candidate treated as authority | Provisional posture; §28 |

---

## 35. Success criteria

This **plan** succeeds when:

1. All 36 sections are present and reviewable
2. Exact repository paths/headings used; inventing avoided; gaps marked TBD/NEEDS_SOURCE
3. F-H-001 remains unmapped with full design procedure
4. Arc I lessons (variable party, read-aloud/mechanics standards, provisional Tho Yor spatial note) correctly represented
5. Authorization boundary is unambiguous
6. Gates block automatic implementation

A future **Arc III pilot** (separately authorized) succeeds when Gates 1–15 pass and Kakeman89 records disposition — without manuscripts being overwritten without cutover auth.

---

## 36. Authorization boundary

**Authorized now:**

- Existence of this planning document
- Read-only analysis reflected herein
- Planning procedures for inventory, crosswalk, F-H-001 design, maps/Foundry/GMB strategy, gates

**Explicitly NOT authorized by this document:**

- Arc III content migration
- Creation of `ai/migration-workspace/arc-iii-integrated-candidate.md`
- Assignment of eight Calling → Speaker → Kesh mappings
- Campaign prose (primary or companion)
- Arc I candidate modification
- Foundry generation or personal Foundry edits
- GM Binder generation, remote overwrite, or pagination work
- Authority cutover
- Commit/push/PR unless separately instructed

Primary guide + approved companion remain operating authority. Arc III status remains **`PLANNING_BASELINE_APPROVED` / `PLANNING_AUTHORIZED_ONLY`**. Migration, candidate creation, and F-H-001 mappings are **not** authorized.

---

## Document history

| Date | Change |
|------|--------|
| 2026-08-27 | Initial Arc III integrated-guide stress-test plan created (planning only; operational — not campaign canon) |
| 2026-08-27 | Kakeman89 planning baseline approval recorded (see addendum below) |
| 2026-08-27 | Link BBEG / Imbalance integration plan as future Arc III retrofit gate — [`ai/plans/2026-08-27-bbeg-and-imbalance-campaign-integration.md`](2026-08-27-bbeg-and-imbalance-campaign-integration.md); not implemented |
| 2026-08-27 | Planning note: Map 4 “optional advanced” language is superseded for **planning** by early-required Gate discovery vs optional particular expedition (see BBEG plan §45). This stress-test document’s historical Map 4 scope rows are retained; candidate/manuscript edits remain unauthorized. |

---

## Addendum — 2026-08-27 — Kakeman89 planning baseline approval

### Reason

Record Kakeman89 approval of this document as the Arc III planning baseline and lock operational defaults for Sessions 7–11, Omen timing, Map 3/4 scope, Counting Quarrel seeding, companion procedure consolidation policy, F-H-001 design models, and Foundry hierarchy — without authorizing migration.

### Supersedes (operational defaults only)

- Prior draft Session 9 framing as equally “Omen **or** Resource war” without a stated default (see historical note under §11).
- Prior open review items §32.1–2, §32.4–7 on plan approval, session outline, companion procedures, Omen timing, Map 3/4, and Counting Quarrel.
- Prior §33 rows that treated Omen placement, Map 3/4 candidate scope, and companion consolidation depth as fully unresolved.

Superseded planning text is retained above or marked historical; this addendum states the current baseline.

### Revised decision or behavior

1. Plan status: `PLANNING_BASELINE_APPROVED` / `PLANNING_AUTHORIZED_ONLY`. Migration **NOT** authorized. No candidate. No mappings approved.
2. Sessions 7–11: provisional operational structure per §11 (S7 scout loop; S8 trade/mistrust; S9 Omen default; S10 Resource War OR Joint Rite by prior state; S11 crisis/scars/map review/Level 11). Names provisional.
3. Omen: default Arc III S9; alternate closing Arc II; if already ran, do not rerun — Resource War as primary S9; Joint Rite / faction crystallization / approved contact consequence in S10; preserve Omen consequences and vocabulary.
4. Map 3: optional, in-scope; dedicated map / Theater / bypass / non-visit consequences; not required for completion.
5. Map 4: optional advanced; prerequisites, refuse/defer, failure, never-open completion path; must not replace social-contact focus.
6. Counting Quarrel: complete primarily Arc IV; Arc III seed only (calendar incompatibilities, scheduling disputes, cycle naming/length disagreements, practical coordination problems).
7. Companion: required Arc III operational procedures are required Local Completeness migration candidates (§15); atmospheric prose selective + clarity standard.
8. F-H-001: do not assume fixed 1:1; compare Models A/B/C; prefer Model B; Model C allowed for specific Speakers when evidence insufficient; no manufactured evidence; §9.6 remains empty.
9. Foundry: provisional mixed hierarchy in §23 — do not generate.

### Implementation impact

Operational sections of this plan updated: header; locked-status table; §5.1 Counting Quarrel note; §8 exclusions; §9.1a; §10–§11; §12 footnote; §15; §22–§23; §32–§33; §34 risk row; §36 boundary wording. No campaign manuscripts, candidate, Foundry, or GMB outputs created or edited.

### Validation impact

Gate 4 outline approval advanced for **planning baseline** only. Gates for candidate build, F-H-001 filled mappings, and migration remain blocked. Gate 15 implementation go/no-go remains open.

### Status

**PLANNING_BASELINE_APPROVED** / **PLANNING_AUTHORIZED_ONLY** — awaiting separate authorization for any Arc III candidate or migration work.

**End of plan.**
