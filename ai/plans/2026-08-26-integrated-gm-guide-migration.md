# Integrated GM Guide Migration Plan

**Status:** Planning only — **migration NOT AUTHORIZED**  
**Authority:** Kakeman89 Phase 10 decisions 2026-08-26 (Option C — planning direction)  
**Parent:** [`reports/audits/2026-08-26-phase10-kakeman89-review.md`](../../reports/audits/2026-08-26-phase10-kakeman89-review.md)  
**Architecture:** [`ai/PROJECT_ARCHITECTURE.md`](../PROJECT_ARCHITECTURE.md)  
**Crosswalk:** [`reports/audits/integrated-guide-content-crosswalk.yaml`](../../reports/audits/integrated-guide-content-crosswalk.yaml)  
**Critique:** [`reports/audits/2026-08-26-dawn-of-the-jedaii-project-critique.md`](../../reports/audits/2026-08-26-dawn-of-the-jedaii-project-critique.md)

---

## Purpose

Define a controlled Act-by-Act path to one **integrated authoritative GM guide** organized **Act → Session → Scene** for point-of-use play, using audit evidence. This plan selects architecture **direction** and pilot scope only.

## Planning direction (decided)

**Option C:** One integrated authoritative GM guide via controlled Act-by-Act migration.

This does **not** authorize:

- Manuscript consolidation or content migration  
- Companion retirement or archival  
- Creating `.cursor/skills/integrated-guide-migration/`  
- Generator changes or regeneration  
- Commit / push  

## Included finding / crosswalk inputs

| ID / artifact | Role |
|---------------|------|
| **F-P-002** | Pilot Act = Arc I; Arc III second stress test |
| **F-G-002** | Arc III depth currently companion-heavy |
| **F-G-001** | Arc I multi-chapter navigation / local summary candidate |
| **F-P-001** | Threshold Ch21↔companion §4 near-duplicate (future placement) |
| **CW-001 … CW-008** | Crosswalk rows (Arc I, Threshold, App D/C, Arc III, Faces, etc.) |

Related prerequisites outside this plan’s implementation:

- Blocker plan: F-M-002 (GMB trust), preferably F-N-001, F-M-001, F-O-001/002  
- Campaign decision record: F-H-001 direction (mappings still TBD)

## Explicitly excluded (until separate auth)

- Merging or deleting either manuscript  
- Retiring the companion  
- Writing the eight Calling→Speaker→Kesh assignments here  
- Full-book rewrite in one pass  
- Creating the migration Agent Skill  
- Any regen of GMB/Foundry as part of “migration”

## Current SoT during planning (unchanged)

- Primary: `dawn-of-the-jedaii-campaign-guide.md`  
- Companion: `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md`  
- Factual conflict: primary controls  
- Generated: `gmbinder/`, `foundry/` — do not hand-edit  

## Target usability principles (test in pilot; do not enforce by rewrite now)

1. **Act → Session → Scene** organization for runnable prep.  
2. **Local Completeness Principle** — a runnable scene chapter should contain what is needed to understand, prepare, and adjudicate that scene, except universally reused mechanics, full-length reference entries, or material whose controlled separation serves a clear purpose.  
3. Controlled local repetition OK; excessive duplication not.  
4. Present-quality findings ≠ future-placement recommendations.  
5. Do not treat useful reference chapters as defective merely because content may later be summarized locally.

## Proposed future book shape (planning sketch)

| Layer | Contents |
|-------|----------|
| Campaign foundations | Premise, spoiler policy, Session 0, advancement |
| Acts | At-a-glance, purpose, factions, revelations, end states |
| Sessions | Purpose, prep, flow, alternates, end states |
| Scenes | Point-of-use fields (Purpose, Trigger, Situation, Read-Aloud, Scene Card, Location, Characters, Objectives, Opposition, Mechanics, Clues, RP, Developments, Failure/Partial, Alternates, Transition, Consequences, Continuity, Foundry assets) |
| Appendices | Provenance, timelines, full reference banks, map library |

Exact TOC requires Kakeman89 approval before any migration execution.

## Pilot — Arc I (authorized as pilot **scope for planning**)

**Goals when a future pilot execution is authorized:**

- Validate Act/Session/Scene structure  
- Test Local Completeness Principle  
- Practice controlled repetition  
- Consolidate Threshold Halls dual prose with traceability (CW-002/CW-003)  
- Prove source traceability to both manuscripts  
- Validate GM Binder and Foundry outputs from the pilot authority  

**Success then enables:** Arc III as second stress test (companion-held runnable depth — F-G-002).

**Pilot execution is not authorized by this document.**

## Recommended phase sequence (future authorizations)

| Phase | Intent | Gate |
|-------|--------|------|
| M0 | Prerequisites: blocker GMB fix; Foundry ID investigation; F-H-001 mapping design started | GMB Ch22 correct; ID policy recorded |
| M1 | Approve integrated TOC + file path for new guide | Kakeman89 sign-off |
| M2 | Arc I pilot migration (copy/consolidate with traceability; **keep both sources**) | Pilot checklist pass |
| M3 | Regen/validate GMB + Foundry from pilot authority | Export parity checks |
| M4 | Arc III stress-test pilot | Contact-play completeness |
| M5 | Remaining Acts | Per-Act auth |
| M6 | Authority cutover + companion disposition | Explicit Kakeman89 decision — **not presumed archival** |

## Files likely affected (execution phases only)

- New integrated guide path (TBD at M1)  
- Possibly `dawn-of-the-jedaii-campaign-guide.md` / companion (read; write only when authorized)  
- `gmbinder/`, `foundry/` after authorized regen  
- Crosswalk updates under `reports/audits/`  

## Validation gates (pilot, when authorized)

- Every migrated scene traces to source heading(s)  
- No unique companion Arc I material silently dropped  
- Threshold not double-maintained without intent  
- GMB/Foundry chapter coverage correct  
- Alternate player paths not collapsed into a railroad  
- Both original manuscripts still present until cutover authorized  

## Rollback

- Keep both manuscripts intact until cutover.  
- Pilot work on a new path or branch so originals remain authoritative.  
- Revert exports from backup/git.

## Authorization boundary

**This document authorizes planning only.**  
Do not migrate content, merge manuscripts, retire the companion, create the migration skill, regenerate outputs, commit, or push without a **separate explicit Kakeman89 authorization** naming the allowed phase.
