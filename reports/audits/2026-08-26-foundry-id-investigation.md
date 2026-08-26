# Foundry ID Stability Investigation (F-N-001)

**Status:** Operational investigation (not campaign canon)  
**Date:** 2026-08-26  
**Finding:** F-N-001  
**Authority:** Blocker & Generator Reliability Correction Plan implementation authorization

---

## Pre-implementation behavior

- `tools/md_to_foundry_journal.py` assigned each page `_id` with `secrets.choice` (16 alphanumeric chars).
- Generated `foundry/dawn-of-the-jedaii.journal.json` had **no** top-level Journal Entry `_id`.
- Page ownership defaulted to GM-only (`ownership.default: 0`).
- `foundry/README.md` recommended delete + re-import because IDs were unstable across regenerations.

## Static evidence (no live Foundry world mutated)

1. **Code:** random `make_id()` confirmed non-deterministic across runs.
2. **Artifact:** existing journal pages used opaque random IDs.
3. **Docs:** README preferred delete+reimport, implying update-by-ID was unreliable with random IDs.
4. **Foundry v13 API:** Journal Entry and Journal Entry Page documents are identified by `_id`. Update APIs (`updateDocuments`, embedded updates) key on `_id`. Import Data paths that preserve `_id` can update; new `_id`s create new documents (duplicate risk).

## Gate decision

Investigation supports that **stable semantic IDs improve update/link/duplication behavior** for any import or repair workflow that matches on `_id`.

**Option B authorized by gate:** implement deterministic IDs derived from stable semantic keys (chapter/appendix titles), not from list index alone.

## Implementation

- Journal `_id`: deterministic from key `journal:dawn-of-the-jedaii-gm-guide`
- Page `_id`: deterministic from key `page:<slugified-title>`
- Algorithm: SHA-256 → base62 → 16 chars (Foundry DocumentIdField alphabet)
- Collision detection raises before write
- Repeated generation with unchanged inputs reproduces identical `_id`s (validated offline)

## Live import validation

**Not performed.** No live Foundry world was available or authorized for mutation.

Remaining manual check for Kakeman89:

1. Import regenerated JSON into a disposable test world.
2. Re-import the same JSON onto the same Journal Entry.
3. Confirm pages update in place (same IDs) rather than duplicating.
4. Confirm GM-only ownership remains intact.

Until that manual check, live Import Data update-vs-duplicate behavior is **documented as unverified**, not guessed.

## Status recommendation for F-N-001

- Generator/ID strategy: **RESOLVED** (deterministic generation validated offline)
- Live import behavior: **NEEDS VALIDATION** (manual Foundry follow-up)
