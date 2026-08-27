---
name: integrated-guide-migration
description: >-
  Controlled Act-by-Act migration from primary guide + approved companion into
  a provisional integrated GM guide candidate. Use only when Kakeman89 has
  authorized a specific migration scope (e.g. Arc I pilot). Never auto-promote
  authority or edit source manuscripts.
disable-model-invocation: true
---

# Integrated Guide Migration

SESSION DOCUMENT PROTECTION: Files under `ai/sessions/**` are append-only historical records. Preserve all existing decisions, criteria, gates, failures, and evidence. Updates may append dated addenda, annotate existing items, or change checkboxes when supported by evidence. Never delete, replace, renumber, condense, or rewrite existing substantive content unless the user explicitly authorizes destructive revision of the identified section.

## Purpose

Migrate **one explicitly authorized scope** at a time from:

1. `dawn-of-the-jedaii-campaign-guide.md` (primary authority)
2. `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md` (approved companion)

into a **provisional, non-authoritative** integrated candidate organized **Act → Session → Scene** for point-of-use table use.

Controlling plan: [`ai/plans/2026-08-26-integrated-gm-guide-migration.md`](../../ai/plans/2026-08-26-integrated-gm-guide-migration.md)

## Trigger conditions

Use this skill only when **all** are true:

1. Kakeman89 authorized the specific migration scope (e.g. Arc I pilot).
2. Phase 0 checklist for that scope is complete or classified.
3. Crosswalk procedure is approved for the scope.
4. Candidate output path is approved (e.g. `ai/migration-workspace/arc-i-integrated-candidate.md`).
5. This skill file exists and is invoked for the authorized scope.

Do **not** use for planning-only tasks, full-book migration without authorization, or any scope beyond the approved Act/Arc.

## Authority hierarchy

1. Explicit Kakeman89 decisions (campaign decision record)
2. Primary campaign guide — **factual authority**
3. Approved companion — atmosphere, presentation, GM guidance where no factual conflict
4. Repository-designated sources (Appendix D where it covers a claim)
5. Verified Star Wars Legends continuity
6. Clearly labeled campaign adaptation / original campaign material

**Factual conflict:** primary guide wins. Stop and report; do not silently resolve.

**Presentation-only differences:** consolidate with traceability; not automatic defects.

**Integrated candidate:** never authoritative by existing. Authority transition requires separate Kakeman89 acceptance + cutover authorization.

## Required inputs

Before migrating:

- [`ai/PROJECT_ARCHITECTURE.md`](../../ai/PROJECT_ARCHITECTURE.md)
- [`ai/plans/2026-08-26-integrated-gm-guide-migration.md`](../../ai/plans/2026-08-26-integrated-gm-guide-migration.md)
- [`ai/plans/2026-08-26-campaign-decision-record.md`](../../ai/plans/2026-08-26-campaign-decision-record.md)
- [`reports/audits/integrated-guide-content-crosswalk.yaml`](../../reports/audits/integrated-guide-content-crosswalk.yaml)
- [`reports/audits/2026-08-26-findings-register.yaml`](../../reports/audits/2026-08-26-findings-register.yaml)
- Applicable `.cursor/rules/` (Legends, source-and-canon, house voice)
- Source manuscripts (read-only)
- Authorized archive scope docs when archive material is in scope

## Source-manuscript protection

**Never:**

- Delete, overwrite, rename, move, archive, or merge source manuscripts
- Edit `dawn-of-the-jedaii-campaign-guide.md` or companion as part of migration
- Treat generated production output (`foundry/dawn-of-the-jedaii.journal.json`, `gmbinder/dawn-of-the-jedaii-gmbinder.md`) as migration source or write target unless separately authorized

**Always:**

- Preserve both manuscripts unchanged
- Record every migrated block in the crosswalk
- Emit a change manifest per run

## Crosswalk requirement

System of record: [`reports/audits/integrated-guide-content-crosswalk.yaml`](../../reports/audits/integrated-guide-content-crosswalk.yaml) (schema: [`reports/audits/CROSSWALK-SCHEMA.md`](../../reports/audits/CROSSWALK-SCHEMA.md)).

For every source block in the authorized scope:

1. Create or update a crosswalk row before migrating prose.
2. Record source file, heading, authority, category, Act/Session/Scene, overlap, conflict status, GM/player visibility, Legends classification, treatment, migration status, validation status.
3. No source block may disappear because another block covers similar material.
4. Consolidations must preserve every unique fact, clue, operational instruction, and consequence.

Candidate may use stable section IDs in HTML comments (`<!-- cw:CW-042 -->`); strip before publication export.

## Act → Session → Scene workflow

1. **Phase 0** — Confirm scope, templates, candidate path, gates.
2. **Crosswalk** — Map every source block; resolve or flag conflicts.
3. **Skeleton** — Create candidate headings only (Act, Sessions, Scenes).
4. **Mechanical migration** — Scene Cards, mechanics, checklists, clues, map briefs.
5. **Narrative integration** — Approved companion atmosphere; presentation-only enrichment.
6. **Archive review** — Incorporate only approved, traceable, Arc-applicable archive items.
7. **Continuity / Legends audit** — Run audit skills; fix migration mistakes only.
8. **Pilot outputs** — Foundry/GMB at **pilot-only paths** when authorized.
9. **Acceptance package** — Evidence, recommendation (not acceptance on Kakeman89's behalf).

Migrate **one authorized scope per run**. Do not auto-continue to the next Act.

## Local Completeness Principle

A runnable scene section must contain everything needed to understand, prepare, and adjudicate that scene, except:

- universally reused mechanics (summarize locally + Part IV / central reference)
- full-length reference entries (summarize locally + central reference)
- material whose controlled separation has clear purpose

**Include locally:** purpose, trigger, situation, Scene Card, objectives, opposition, scene mechanics, essential clues, alternates, failure/partial success, transitions, consequences, portrayal cues, Foundry asset refs.

**Summarize + reference:** full NPC bios, faction histories, long tables, complete stat blocks, full artifact provenance.

A cross-reference must not replace information required to adjudicate the current scene.

## Controlled-repetition policy

**Allow concise local repetition** when it prevents table-time lookup: scene goals, scene mechanics, essential clues, immediate consequences, short location/NPC portrayal cues.

**Prefer central reference + local summary** for: full biographies, complete faction history, reusable systems (Storm Clock, boons), large tables, long stat blocks.

Every repeated summary must agree with controlling source, preserve GM/player boundaries, avoid unapproved facts, and reference a crosswalk row operationally.

After migration, run contradiction check across repeated summaries for the same entity.

## Operational metadata boundary (strict)

Operational metadata must **never** leak into readable candidate prose, pilot Foundry content, pilot GM Binder content, or player handouts.

Readable campaign content includes Scene Cards, Act/Session guidance, Read-Aloud, GM Notes, Foundry journal pages, GM Binder pilot pages, and player handouts.

Operational metadata includes finding IDs, crosswalk IDs, migration/treatment/status enums, casting taxonomies (`SOURCE_SUPPORTED_SCENARIO_CAST`, `INDEPENDENT_OF_CALLING`, …), Legends/campaign classification enums, confidence values, validation states, and authorization-state labels.

**Required translation examples:**

| Operational | GM-facing |
|-------------|-----------|
| `SOURCE_SUPPORTED_SCENARIO_CAST` | Suggested Speaker |
| `RECOMMENDED_SUBSTITUTABLE_CAST` | Alternative Speaker |
| `INDEPENDENT_OF_CALLING` | This role does not need to match the party’s calling. |
| `NEEDS_KAKEMAN89` | Omit from normal prose; use `## Development Decisions Still Required` (publication-excluded) |

Keep technical classifications only in crosswalks, manifests, reports, sidecar metadata, or non-rendered HTML comments such as `<!-- SOURCE-TRACE: CW-006 | primary Ch17 | companion Ch7 -->`.

Strip HTML comments and publication-excluded development sections before generating Foundry or GM Binder pilot outputs.

See also `.cursor/rules/operational-metadata-not-in-guide-prose.mdc`.

## Source-traceability procedure

1. Crosswalk row per migrated block (SoT).
2. Candidate HTML comments linking to crosswalk rows (`SOURCE-TRACE`), never visible Scene Card rows of raw CW/F- IDs.
3. Connective text classified as `ORIGINAL_CAMPAIGN_MATERIAL` **in the crosswalk only**, not as a reader-facing badge in guide prose.
4. Change manifest listing blocks added, consolidated, excluded, placeholders.
5. No provenance dumps, finding IDs, or treatment enums in GM-facing prose.

## Legends classifications

Record these **in operational audits/crosswalks only**:

- `LEGENDS_VERIFIED`
- `CAMPAIGN_APPROVED`
- `CAMPAIGN_ADAPTATION`
- `ORIGINAL_CAMPAIGN_MATERIAL`
- `NEEDS_SOURCE`
- `CONTINUITY_CONFLICT`

Do not print these enum strings in readable guide prose. Do not import Disney canon. Do not silently promote table fiction to Legends lore. Run [`legends-source-audit`](../legends-source-audit/SKILL.md) when auditing migrated content.

## Player-visible versus GM-only handling

- GM-facing candidate sections may name Tython, Ashla/Bogan concepts, Kwa foreshadow, GM secrets.
- Pre-reveal **player-facing** material must **not** name Tython (F-K-002).
- Post-reveal player material may use Tython when campaign state reaches reveal.
- Candidate-level F-K-002 fixes do **not** mark source manuscripts as implemented.
- Never leak GM-only secrets into player-facing candidate sections.

## Archive-material classification

Before incorporating ChatGPT archive or gap-report items, classify each as:

`already represented` | `superseded` | `approved campaign decision` | `useful migration source` | `Act/Session/Scene-specific` | `reusable reference` | `asset candidate` | `provenance-only` | `conflicting proposal` | `needs Kakeman89 decision` | `exclude from migration`

Incorporate only: approved, consistent with authority, applicable to scope, useful at point-of-use, traceable.

Do not import entire conversations or unapproved brainstorming.

## Authoring versus migration distinction

**Migration:** reproduce or consolidate existing approved content with traceability.

**Connective text:** minimum prose required for coherent integration only; label `ORIGINAL_CAMPAIGN_MATERIAL`; record in crosswalk.

**Not allowed:** invent campaign canon, Calling→Speaker→Kesh mappings, Disney canon, named-author imitation, or polished facts where a decision placeholder is required.

## Minimum connective-text policy

Add connective text only when:

- a session/scene transition requires one sentence of orientation
- player-agency handling is missing and can be filled with operational GM guidance that does not create new canon
- a cross-reference needs a one-line pointer

Otherwise use explicit decision placeholders:

```markdown
> **MIGRATION PLACEHOLDER — REQUIRES KAKEMAN89:** [decision topic]
```

Placeholders must not read as polished campaign facts.

## Unresolved-conflict stop conditions

**Stop the affected block** (not necessarily the entire scope) when continuing would require:

- factual invention
- source-content loss
- unsupported Legends classification
- GM-only disclosure to players
- destructive modification of sources
- unapproved external-content copying

**Continue independent work** when one optional block is unresolved. Record in change manifest and final report.

## Content-completeness validation

Before marking scope migrated:

1. 100% crosswalk coverage for authorized source blocks
2. Every Scene in scope has required template fields (no empty irrelevant headings)
3. Eight ship Scene Cards present for Arc I (if in scope)
4. Sessions 0–3 present for Arc I (if in scope)
5. No unique fact/clue/instruction lost vs crosswalk inventory
6. Exclusions documented with reason

## Foundry validation

Pilot output only at authorized paths (e.g. `foundry/arc-i-pilot.journal.json`).

**Never overwrite** `foundry/dawn-of-the-jedaii.journal.json` unless separately authorized.

Recommended mixed hierarchy: 1 page per Act overview + 1 page per Session; Scenes as H2 inside Session pages.

Validate:

- static JSON validity
- deterministic semantic IDs
- GM-only ownership defaults
- player handout separation
- hierarchy matches candidate

F-N-001: disposable-world import test required for acceptance; record result or mark gate incomplete with manual instructions.

**Never** mutate Kakeman89's personal Foundry game.

## GM Binder validation

Pilot output only at authorized paths (e.g. `gmbinder/arc-i-pilot-gmbinder.md`).

**Never overwrite** production GMB or saved remote GM Binder document.

Validate content presence, heading mapping, Sessions 0–3, eight ship Scene Cards, player/GM distinctions. F-M-003 pagination remains deferred — record layout defects honestly; do not require full-book pagination pass.

## Change manifest

Each run produces a manifest listing:

- files created/modified
- source blocks migrated (crosswalk IDs)
- consolidations
- local summaries
- connective additions
- archive items adopted/excluded
- placeholders
- pilot outputs generated
- validation results

Path convention: `reports/audits/arc-i-pilot-change-manifest.md` (or scope-specific sibling).

## Rollback

| Layer | Action |
|-------|--------|
| Source manuscripts | Unchanged — rollback = no action |
| Candidate | Delete provisional candidate file |
| Crosswalk | Retain history; mark rows deferred/superseded |
| Pilot outputs | Delete pilot Foundry/GMB files |
| Authority | Remains primary guide |

Every phase retains change manifests as audit evidence.

## Authority-transition prohibition

This skill **never**:

- Declares candidate authoritative
- Retires or archives source manuscripts
- Auto-continues to next Act after pilot acceptance
- Resolves campaign canon silently
- Marks findings resolved in production manuscripts when only candidate was updated

Full authority transition requires separate Kakeman89 cutover authorization per migration plan §36.

## Table-usability quality rules (Kakeman89 2026-08-27)

Apply on every Arc migration after the Arc I pilot revision:

### Party size

- Never lock the campaign to a fixed player-character count unless Kakeman89 explicitly authorizes it.
- Archive fixed-size proposals (e.g. historical B1 “3 PCs”) are evidence only until adopted.
- Scale boons, NPCs, and optional combat using pool limits and GM guidance—do not invent extra boons or automatic duplicates.

### Mechanics language

- Use SW5e-compatible ability-check wording verified against repository sources (e.g. Investigation, Insight, Persuasion, Stealth, tech/Force-lore—not unsupported skill names).
- Prefer `DC N Ability (Skill) check` with On a success / On a failure.
- Label campaign-provisional DCs and failure costs clearly.
- Do not use vague phrases (“generous DC”, “Wis-based”, “exhaustion flavor”) as adjudication.

### Read-aloud

- Clear, concrete, speakable; physical orientation first.
- No player-emotion dictation; no GM secrets in read-aloud.
- Prefer concrete sensory detail over stacked metaphors.
- Separate Read-Aloud from GM Notes.

### Foundry spatial plans

- Multi-level ship layouts are **provisional spatial arrangements** unless sources establish them.
- Do not classify Foundry level counts as LEGENDS_VERIFIED.

## Final reporting

Report:

1. Authorized scope completed
2. Crosswalk coverage %
3. Material incorporated (primary, companion, archive, connective)
4. Exclusions and placeholders
5. Audit results (Legends, continuity, player agency, F-K-002)
6. Foundry/GMB pilot results
7. Gates passed/failed
8. Recommendation (ACCEPT / ACCEPT_WITH_REVISIONS / REVISE_AND_REPEAT / REJECT / DEFER) — **not** acceptance on Kakeman89's behalf
9. Decisions required from Kakeman89
10. Files created/modified; confirmation sources unchanged
