# Blocker & Generator Reliability Correction Plan

**Status:** Implementation authorized 2026-08-26 and executed — see [`reports/audits/2026-08-26-blocker-implementation-report.md`](../../reports/audits/2026-08-26-blocker-implementation-report.md)  
**Authority:** Kakeman89 Phase 10 decisions 2026-08-26 + explicit blocker implementation authorization  
**Parent:** [`reports/audits/2026-08-26-phase10-kakeman89-review.md`](../../reports/audits/2026-08-26-phase10-kakeman89-review.md)  
**Architecture:** [`ai/PROJECT_ARCHITECTURE.md`](../PROJECT_ARCHITECTURE.md)

---

## Purpose

Restore trustworthy generated outputs and reduce overwrite risk for write-capable tools, without changing campaign manuscripts or beginning integrated-guide migration.

## Included finding IDs

| ID | Role in this plan |
|----|-------------------|
| **F-M-002** | Primary blocker — GMB Ch22 matcher / Faces overwrite |
| **F-N-001** | Foundry ID stability — investigate first; deterministic IDs only if gate passes |
| **F-M-001** | External Koorivar dependency — four-axis review; no presumed vendoring |
| **F-O-001** | Dry-run / backup for write tools |
| **F-O-002** | Document or quarantine in-place reorder script |

## Explicitly excluded

- Manuscript merge or companion retirement
- Campaign prose edits
- Inventing Calling→Speaker→Kesh mappings
- Creating `integrated-guide-migration` skill
- Integrated-guide content migration
- Hand-editing `gmbinder/` or `foundry/*.journal.json` as the fix for F-M-002
- Changing Foundry ID generation **before** import-behavior investigation gate
- Commit / push

## Prerequisites

- Phase 10 decisions recorded (done)
- Kakeman89 authorization to **implement** this plan (granted 2026-08-26)
- For F-N-001 Option B: written evidence that stable IDs improve update/link/duplication behavior (static investigation recorded; live import still manual)

## Proposed work packages (when implementation later authorized)

### WP-A — F-M-002 GM Binder Ch22 / Faces (Option A)

1. Change `tools/md_to_gmbinder.py` so Koorivar injection targets the **species spotlight chapter** (guide Ch12), not `startswith("22 —")`.
2. Ensure Ch22 **Faces of the First Migration** passes through from the primary guide unchanged.
3. Correct stale injection intro citations (Ch08/Ch21 → current chapter numbers).
4. Regenerate `gmbinder/dawn-of-the-jedaii-gmbinder.md`.
5. Validate: GMB H1 Ch22 = Faces; Ch12 = Koorivar; no duplicate Ch22 Koorivar; App E consistent.

**Campaign content changes?** No.  
**Generated outputs change?** Yes — GMB only (when regen authorized).

### WP-B — F-N-001 Foundry IDs (Option A then conditional B)

1. Investigate Foundry journal Import Data behavior for matching vs differing JournalEntry and page `_id`s (update vs duplicate).
2. Document findings in an addendum to this plan or a short `reports/audits/` note.
3. **Gate:** Only if investigation confirms benefit, implement deterministic IDs from stable semantic chapter/scene keys.
4. Do not change `make_id` / ID generation before the gate.

**Campaign content changes?** No.  
**Generated outputs change?** Only if Option B later authorized and regen run.

### WP-C — F-M-001 Koorivar four-axis review

Review and recommend (no presumed vendoring):

1. Portability  
2. Provenance / licensing / redistribution  
3. Missing-dependency behavior  
4. Guide vs generated-output divergence  

Record recommendation for Kakeman89; do not vendor or path-change without separate auth.

### WP-D — F-O-001 / F-O-002 safety

1. Add dry-run and/or backup behavior to write tools (`md_to_gmbinder.py`, `md_to_foundry_journal.py`, and document `reorder_guide_chapters.py`).
2. Quarantine or clearly mark reorder script as dangerous historical tooling.

## Files likely affected (implementation phase)

- `tools/md_to_gmbinder.py`
- `tools/md_to_foundry_journal.py` (only after F-N-001 gate, if Option B)
- `tools/reorder_guide_chapters.py` (docs/guards only unless further auth)
- `gmbinder/dawn-of-the-jedaii-gmbinder.md` (regen)
- Possibly `foundry/dawn-of-the-jedaii.journal.json` (only if ID change + regen authorized)
- `foundry/README.md` / tool comments as needed

## Validation gate

| Check | Pass criteria |
|-------|----------------|
| F-M-002 | GMB Ch22 is Faces; species inject on correct chapter; App E consistent; no hand-edited “fix” |
| F-N-001 | Investigation note exists; ID code unchanged unless Option B gated and authorized |
| F-M-001 | Four-axis write-up with recommendation; no silent vendoring |
| F-O-001/002 | Dry-run/backup or quarantine documented and, if implemented, demoed |

## Rollback

- Restore prior `gmbinder/` / `foundry/` artifacts from git or backup before regen.
- Revert tool commits if implementation was committed under later auth.
- Primary guide and companion must remain untouched by this plan.

## Authorization boundary

**Original document authorized planning only.**  
Kakeman89 later authorized full implementation of this plan (2026-08-26). Implementation results are recorded in [`reports/audits/2026-08-26-blocker-implementation-report.md`](../../reports/audits/2026-08-26-blocker-implementation-report.md). Commit / push remain unauthorized unless separately requested.
