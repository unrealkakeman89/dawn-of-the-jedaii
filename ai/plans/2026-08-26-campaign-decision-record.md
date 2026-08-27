# Campaign Decision Record

**Status:** Decision capture only — **campaign prose edits NOT AUTHORIZED**  
**Authority:** Kakeman89 Phase 10 decisions 2026-08-26  
**Parent:** [`reports/audits/2026-08-26-phase10-kakeman89-review.md`](../../reports/audits/2026-08-26-phase10-kakeman89-review.md)

This record captures campaign-facing decisions and open design gates. It is operational (`ai/`), not campaign canon, until Kakeman89 authorizes prose updates into the primary guide.

---

## Included finding IDs

| ID | Topic | Decision status |
|----|-------|-----------------|
| **F-H-001** | Calling → Speaker → Kesh | Direction decided; eight mappings **DEFERRED_TO_ARC_III** (2026-08-27) — not assigned |
| **F-G-006** | Landing milestone stacking | Open — needs Kakeman89 choice |
| **F-K-002** | App C Tython naming / staged reveal | **DECIDED** staged reveal; production sync **PENDING_AUTHORITY_TRANSITION** (candidate-only until cutover) |
| **F-B-002** | App D Ashla/Bogan gloss vs teaching order | Open — needs Kakeman89 choice |
| **F-C-001** | Ch24 pickup `[L]`/`[T]` labeling | Open — source-label pass not authorized yet |
| **F-C-002** | Shekk-Arra era labeling | Open — source-label pass not authorized yet |
| **Arc I pilot** | Integrated GM guide pilot disposition | **ACCEPT_WITH_REVISIONS** (2026-08-27) — candidate remains provisional/non-authoritative |

## Explicitly excluded

- Inventing the eight Calling→Speaker→Kesh assignments in this record
- Editing `dawn-of-the-jedaii-campaign-guide.md` or companion prose
- Generator or migration work
- Commit / push

---

## F-H-001 — Calling → Speaker → Kesh

### Decided (2026-08-26)

- Create an **explicit default** Calling → Speaker → Kesh crosswalk.
- Treat the mapping as the **recommended** campaign casting arrangement.
- Allow **GM substitution** unless a specific assignment is later established as **fixed campaign canon**.
- The **actual eight mappings** require a **separate design and review step**.
- Mappings must **not** be invented during this record-only phase.

### Still required before prose implementation

1. Design draft of eight recommended mappings with evidence from Ch10 / Ch22 / App A.  
2. Kakeman89 review of each mapping (recommended vs fixed canon).  
3. Separate authorization to write the crosswalk into the primary guide.

### Placeholder table (empty — do not fill without design auth)

| Calling | Recommended Speaker | Destined Kesh | Recommended vs fixed | Notes |
|---------|---------------------|---------------|----------------------|-------|
| _TBD_ | _TBD_ | _TBD_ | recommended | Design step required |
| _TBD_ | _TBD_ | _TBD_ | recommended | Design step required |
| _TBD_ | _TBD_ | _TBD_ | recommended | Design step required |
| _TBD_ | _TBD_ | _TBD_ | recommended | Design step required |
| _TBD_ | _TBD_ | _TBD_ | recommended | Design step required |
| _TBD_ | _TBD_ | _TBD_ | recommended | Design step required |
| _TBD_ | _TBD_ | _TBD_ | recommended | Design step required |
| _TBD_ | _TBD_ | _TBD_ | recommended | Design step required |

---

## Open decisions (need Kakeman89 answers; no prose edits yet)

### F-G-006 — Landing milestones

- [ ] Single landing milestone only  
- [ ] Allow both Arc I optional +1 and Arc II camp milestone  
- [ ] Other: ________  

### F-K-002 — Appendix C Tython naming

- [ ] Name Tython in crawl  
- [x] Remove Tython name from primer until earned  
- [x] Other spoiler posture: **Staged Tython reveal** (see decision below)

#### Decision — 2026-08-26 — Staged Tython reveal (DECIDED; prose NOT implemented)

**Authority:** Kakeman89 blocker-implementation authorization (decision-record only)  
**Status:** **DECIDED** — not **RESOLVED** (guide/App C prose unchanged in this task)

Preserve the staged Tython reveal:

1. Player-facing material provided **before** the characters identify the world must **not** name Tython.
2. Remove or defer the name from the pre-reveal player primer.
3. The opening crawl continues withholding the world’s identity.
4. GM-facing content may identify the world as Tython.
5. After the world is revealed in play, subsequent player-facing material may use the name Tython normally.

**Explicitly not done under this authorization:** edits to the player primer, opening crawl, campaign guide, narrative companion, generated outputs, or campaign assets.

#### Addendum — 2026-08-26 — ChatGPT archive input (superseded as decision; retained as history)

**Source:** ChatGPT conversation archive comparison  
**Report:** [`reports/audits/2026-08-26-chatgpt-archive-vs-repo-gap-report.md`](../../reports/audits/2026-08-26-chatgpt-archive-vs-repo-gap-report.md)

Archive preference aligned with the decided staged-reveal posture (remove Tython from pre-reveal primer). The archive note remains historical evidence; the **Decision** section above is authoritative for status **DECIDED**.

### F-B-002 — Appendix D Ashla/Bogan

- [ ] Split Legends end-state vs campaign teaching-order adaptation in App D  
- [ ] Leave as-is  
- [ ] Other: ________  

### F-C-001 / F-C-002 — Provenance labeling

- [ ] Authorize a source-label pass (no lore invention)  
- [ ] Defer  

---

## Authorization boundary

Recording decisions here does **not** authorize campaign prose edits, manuscript consolidation, or generator changes. Each prose update requires separate Kakeman89 authorization.

---

## Addendum — 2026-08-27 — Arc I pilot disposition and related decisions

**Authority:** Kakeman89  
**Task type:** Decision recording and pilot-status updates only  
**Does not authorize:** campaign prose edits; Arc I candidate revision; pilot output regen; Arc III migration/content; source manuscript edits; production Foundry/GMB edits; commit; push

**Related acceptance record:** [`reports/audits/arc-i-pilot-acceptance.md`](../../reports/audits/arc-i-pilot-acceptance.md)

### 1. Arc I pilot disposition — ACCEPT_WITH_REVISIONS

Structural working model **accepted**:

- Act → Session → Scene organization
- Combined campaign-guide and GM-workbook presentation
- Point-of-use scene information; local Scene Cards; concise central-reference summaries
- Controlled repetition; source traceability
- Variable party size
- Revised clear read-aloud standard
- Provisional multi-level Tho Yor design

**Does not** make the pilot authoritative. **Does not** approve every provisional mechanic as final campaign canon.

### 2. Tho Yor Foundry structure — four linked scenes (provisional)

Accepted provisional organization:

| Level | Name |
|-------|------|
| 1 | Threshold |
| 2 | Pilgrim |
| 3 | Contemplation |
| 4 | Restricted |

- Prefer **four linked Foundry Scenes** under a shared Tho Yor collection.
- The Foundry Levels module may be used **within** an individual Scene when meaningful vertical overlap exists.
- Do **not** assume all four levels must be stacked inside one Scene.
- Map 1 remains a detailed Threshold encounter map, not a complete vessel map.
- Arrangement remains **provisional** until map design establishes exact spatial relationships.
- Not LEGENDS_VERIFIED; not established campaign architectural canon.

### 3. Party-size policy

- No fixed party size.
- Table-determined party size and scalable scene guidance required.
- Archive B1 remains **SUPERSEDED_BY_KAKEMAN89** and is **not** campaign canon.

### 4. Boon scaling

- One unique starting boon vision per player character, up to the six existing Ch11 boons.
- Party &lt; 6: unassigned boons remain aboard.
- Party = 6: each may receive one unique boon.
- Party &gt; 6: do not duplicate or invent boons; do not give multiple starting boons to compensate; GM decides which characters initially receive visions; remaining characters may connect through later play or a separately approved design.

### 5. Machine-Spirit failure cost (provisional direction)

A failed ability check causes a brief psychic backlash. The character has **disadvantage on the next ability check** the character makes as part of the Machine-Spirit challenge. This consequence **ends when the challenge ends**.

- Do **not** apply damage or exhaustion as the default failure cost.
- Final challenge design must still verify: eligible SW5e abilities/proficiencies; DC; repeat restrictions; success threshold; failure threshold; final failure consequence.

### 6. Observation Galleries awe

- No saving throw solely to determine awe or fear.
- Ask players to describe their characters’ reactions.
- Use an ability check only when a character attempts a concrete action with an uncertain outcome.
- Do not mechanically dictate player-character emotion.

### 7. Machine-Spirit challenge scaling

- Retain **3 successes before 2 failures** as the provisional group-challenge structure.
- Do not automatically increase required successes based on party size.
- Require meaningfully different approaches for repeated checks.
- No character should contribute more than **2** checks unless every participating character has had an opportunity to act.
- Larger parties should create additional narrative opportunities or complications rather than an automatically longer roll sequence.

### 8. F-K-002 — KEEP_CANDIDATE_ONLY_UNTIL_AUTHORITY_TRANSITION

- Arc I candidate correctly withholds Tython from pre-reveal player-facing material.
- Do **not** edit the production campaign guide during the preserved-source migration period solely to synchronize this correction.
- The future authoritative integrated guide must implement the staged Tython reveal.
- Production implementation status: **PENDING_AUTHORITY_TRANSITION** (decision posture unchanged; guide prose still not synchronized).

### 9. F-H-001 — DEFER_UNTIL_ARC_III_STRESS_TEST

- Do not design the eight Calling → Speaker → Kesh mappings yet.
- Arc I may retain: Senn-Vora as provisional party-ship default; generic substitution guidance; explicit notation that the complete mapping remains unresolved.

### 10. A2 Chamber — KEEP_PLACEHOLDER

Do not create Chamber of First Calling content until Kakeman89 approves: campaign purpose; spatial location; clues; relationship to Sealed Vaults; relationship to Kwa material; intended Act.

### 11. Arc III — AUTHORIZE_PLANNING_AFTER_ARC_I ACCEPTANCE RECORD

- Arc III stress-test **planning** is authorized by this acceptance record.
- Create **no** Arc III campaign content in this decision-record task.
- Planning must evaluate whether the integrated structure can absorb companion-heavy runnable material without losing atmosphere, continuity, player agency, or point-of-use usability.
- Status: **PLANNING_AUTHORIZED_ONLY** — migration not started; no Arc III candidate; no Arc III migration skill.

### 12. Template flexibility

- Act, Session, and Scene templates are **guides**, not mandatory empty forms.
- Do not create empty sections when a field is irrelevant.
- Combine closely related fields when that improves table use and does not hide important information.
- Do not allow the guide-workbook structure to become excessively repetitive or mechanical.

### Status summary (operational labels — not finding-schema CLOSED/RESOLVED substitutes for unresolved gates)

| Item | Status |
|------|--------|
| Arc I architecture | ACCEPTED_WITH_REVISIONS |
| Arc I candidate | PROVISIONAL_NON_AUTHORITATIVE |
| Arc I textual acceptance | PENDING_TABLE_REVIEW |
| Arc I Foundry acceptance | PENDING_DISPOSABLE_WORLD_TEST |
| Arc I GM Binder pagination | DEFERRED_PARTIAL |
| Arc III | PLANNING_AUTHORIZED_ONLY |
| F-K-002 production implementation | PENDING_AUTHORITY_TRANSITION |
| F-H-001 mappings | DEFERRED_TO_ARC_III |
| A2 Chamber | PLACEHOLDER_UNAUTHORIZED |

**Explicit non-authorizations:** Arc I not authoritative; Acts II–VI not authorized; no Arc III candidate or migration skill; no cutover; no commit/push under this record.
