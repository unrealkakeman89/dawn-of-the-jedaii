# Phase 10 — Kakeman89 Review Package & Correction Backlog

**Date:** 2026-08-26  
**Status:** Kakeman89 decisions recorded 2026-08-26 (see Decision log)  
**Operational — not campaign canon**

This package closed the *agent* work for Phase 10 by preparing review materials. Recorded decisions authorize **plan creation only** where stated below. They do **not** authorize implementation, manuscript consolidation, companion retirement, generator execution, commit, or push unless a later authorization says so.

Master critique: [`2026-08-26-dawn-of-the-jedaii-project-critique.md`](2026-08-26-dawn-of-the-jedaii-project-critique.md)  
Findings: [`2026-08-26-findings-register.yaml`](2026-08-26-findings-register.yaml)  
Pilot findings: [`2026-08-26-pilot-findings-register.yaml`](2026-08-26-pilot-findings-register.yaml)  
Reconciliation: [`2026-08-26-phase8-reconciliation.md`](2026-08-26-phase8-reconciliation.md)

---

## Review checklist for Kakeman89

- [x] Architecture matrix in `ai/PROJECT_ARCHITECTURE.md` accepted for ongoing work (operating under recorded decisions)
- [x] Primary guide + approved companion arrangement remains in force until a later migration is separately authorized
- [x] Integrated-guide consolidation: **approve planning** (Option C — plan only; no merge)
- [x] Allow tool fix for GMB Ch22 matcher (F-M-002)? **Yes — in blocker plan only; implementation not yet authorized**
- [x] Allow regen of `gmbinder/` after tool fix? **Yes as part of F-M-002 Option A when implementation is later authorized**
- [x] Foundry ID strategy: **investigate import behavior first** (F-N-001 Option A); deterministic IDs only if gate passes
- [ ] Koorivar dependency: path config / vendor / submodule / remove inject / other — **F-M-001 needs four-axis review; vendoring not presumed**
- [x] Speakers↔callings: **create default Calling→Speaker→Kesh crosswalk** (recommended casting; GM substitution allowed unless fixed canon); eight mappings require separate design — not invented in record-only phase
- [ ] App C Tython naming posture — captured for campaign-decision record; prose edits not authorized
- [ ] Named-author style bible rewrite — deferred with general medium backlog
- [ ] Which MEDIUM point-of-use expansions to prioritize — deferred except migration inputs
- [x] Whether to authorize a **separate** Integrated GM Guide Migration Plan — **Yes (plan creation only)**
- [x] Whether/when companion might become archival — **not authorized; not implied**

---

## Correction backlog (proposals only — not authorized)

| Priority | ID | Proposed action | Canon change? | Auth needed |
|----------|-----|-----------------|---------------|-------------|
| P0 | F-M-002 | Fix GMB `22 —` matcher to preserve Faces; stop duplicate Koorivar as Ch22; fix stale Ch08/21 cites in inject intro | No (tool) | Yes |
| P0 | F-M-002 follow-up | Regenerate `gmbinder/` after fix | Generated only | Yes |
| P1 | F-N-001 | Design deterministic Foundry page IDs from chapter keys | No (tool) | Yes |
| P1 | F-H-001 | Add calling→Speaker→Kesh table or explicit agnostic rule | Maybe | Yes |
| P1 | F-K-002 | Harmonize App C crawl vs primer on Tython name | Player-facing | Yes |
| P2 | F-K-001 | Rewrite Ch21 style bible without named authors | Craft text | Yes |
| P2 | F-K-003 | Fix Storm Clock citation to Ch10/App B only | No | Yes |
| P2 | F-E-001 | Clarify Episode 1 vs Arc II Session 6 | No | Yes |
| P2 | F-G-004 | Assign Omen must-play owner chapter/checkbox | No | Yes |
| P2 | F-G-006 | Single landing milestone rule | Yes (advancement) | Yes |
| P2 | F-B-002 | Split App D Legends end-state vs campaign teaching order | Classification | Yes |
| P3 | F-G-002/003/005 | Expand Arc III / S6 / first-trial operational hooks | Yes | Yes |
| P3 | F-I-001 | Kaleth continent play note | Yes | Yes |
| P3 | F-H-002 | Yen-Ti mode-by-arc line | No | Yes |
| P3 | F-C-001/002 | Source-label pickup rows / Shekk-Arra | Classification | Yes |
| P3 | F-O-001 | Dry-run/backup for write tools | No (tool) | Yes |
| P3 | F-O-002 | Document or quarantine reorder script | No | Yes |
| P4 | F-A-001 | Generated-file notices strategy | Tooling | Yes |
| P4 | F-M-001 | Koorivar four-axis decision | Tooling/licensing | Yes |
| — | F-P-002 | Separate migration plan | Process | Yes — only if consolidation path chosen |

**Do not execute this backlog without per-item or per-batch Kakeman89 authorization.**

---

## Explicit non-actions

- No manuscript merge  
- No companion retirement  
- No `integrated-guide-migration` skill created  
- No automatic content corrections from this audit  
- No commit / push from this phase  

---

## Phase 10 completion criteria (agent)

- [x] Review package written  
- [x] Backlog prioritized  
- [x] Decisions listed  
- [x] Kakeman89 responses recorded (2026-08-26)

When Kakeman89 records decisions, append them below without deleting this section.

### Decision log (append-only)

#### 2026-08-26 — Kakeman89 Phase 10 answers

1. **F-M-002:** Option A. Correct the GM Binder generator so Koorivar injection targets the intended species chapter; preserve Faces of the First Migration as Chapter 22; correct stale injection references; regenerate and validate GM Binder output when implementation is later authorized. Do **not** hand-edit generated output as the solution.

2. **F-N-001:** Option A first. Investigate Foundry journal import behavior for matching and differing JournalEntry and page IDs. Proceed to Option B (deterministic IDs from stable semantic chapter/scene keys) **only if** investigation confirms stable IDs improve update, link, or duplication behavior. Do **not** change the ID generator before that gate.

3. **F-H-001:** Create an explicit default Calling → Speaker → Kesh crosswalk. Treat the mapping as the **recommended** campaign casting arrangement while allowing GM substitution unless an assignment is established as fixed campaign canon. The actual eight mappings require a **separate design and review step** and must **not** be invented during a record-only phase.

4. **Integrated guide:** Option **C**. Create one integrated authoritative GM guide through controlled Act-by-Act migration (Act → Session → Scene; point-of-use usability). **Planning direction only.** Does **not** authorize manuscript consolidation, content migration, companion retirement, or generator changes.

5. **Pilot Act:** **Arc I** — validate integrated structure, Local Completeness Principle, controlled repetition, Threshold consolidation, source traceability, GM Binder output, and Foundry output. If Arc I succeeds, use **Arc III** as the second stress test (substantial runnable depth currently in companion).

6. **Authorized for separate correction / planning scopes:**
   - Blocker/generator-reliability plan inputs: F-M-002, F-N-001, F-M-001, F-O-001, F-O-002
   - Campaign-decision record (no prose edits): F-H-001, F-G-006, F-K-002, F-B-002, F-C-001, F-C-002
   - Integrated GM Guide Migration Plan inputs: F-P-002, F-G-002, F-G-001, F-P-001, applicable CW entries

7. **Deferred:** F-I-001 and other LOW/OBSERVATION items not required for blocker or integrated-guide planning. **F-F-001** preserved as intentionally unresolved. General medium/low correction backlog deferred until grouped into separately reviewable scopes.

8. **Needs more evidence:** F-N-001 (Foundry import behavior); F-H-001 (design before eight mappings); F-M-001 (portability, provenance, licensing/redistribution, missing-dependency, guide-vs-generated divergence; vendoring not presumed).

9. **Blocker correction plan:** **Yes** — plan creation only. No implementation, generator execution, regeneration, commit, or push.

10. **Integrated GM Guide Migration Plan:** **Yes** — plan creation only. Do **not** create the integrated-guide-migration skill, migrate content, merge manuscripts, retire the companion, regenerate outputs, commit, or push.

**Follow-on plan paths (created under this authorization):**

- `ai/plans/2026-08-26-blocker-generator-reliability-correction.md`
- `ai/plans/2026-08-26-campaign-decision-record.md`
- `ai/plans/2026-08-26-integrated-gm-guide-migration.md`

#### 2026-08-26 — ChatGPT archive vs repo gap report

Comparison of the ChatGPT conversation archive (through 2026-08-26) against the current repository. **Record only** — no guide prose edits, asset creation, regeneration, commit, or push.

**Artifacts created:**

- `reports/audits/2026-08-26-chatgpt-archive-vs-repo-gap-report.md`
- `ai/plans/2026-08-26-chatgpt-archive-content-pr-scope.md` (plan only; separate from blocker-generator plan)

**F-K-002:** Archive preference recorded on the campaign-decision record (remove Tython name from primer until earned). Decision checkboxes remain **open** pending Kakeman89 selection. Prose edits still not authorized.

**Regeneration:** Not run. Guide edits were not authorized by this comparison.

#### 2026-08-26 — Blocker & generator reliability implementation

Kakeman89 authorized full execution of `ai/plans/2026-08-26-blocker-generator-reliability-correction.md`.

**Results (operational):**

- F-M-002 closed — GMB Ch12 Koorivar inject; Ch22 Faces preserved; regenerated via tool
- F-O-001 / F-O-002 closed — dry-run/backup; reorder refuse-write default
- F-N-001 open (partial) — deterministic IDs offline-validated; live import still manual
- F-M-001 needs_decision (partial) — portable discovery + fail-loud; licensing/vendoring undecided
- F-K-002 **DECIDED** in campaign-decision record (staged Tython reveal); **prose not implemented**

**Report:** `reports/audits/2026-08-26-blocker-implementation-report.md`  
**Not done:** archive content PR scope; manuscript merge; commit/push

#### 2026-08-26 — F-K-002 staged Tython reveal (decision only)

Recorded as **DECIDED** in `ai/plans/2026-08-26-campaign-decision-record.md`. Player primer / crawl / guide prose **not** edited under this authorization.
