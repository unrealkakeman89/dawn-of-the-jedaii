---
name: output-sync-validator
description: Validates synchronization between the primary campaign guide and generated GM Binder / Foundry outputs. Use for chapter coverage, staleness, permissions defaults, Foundry ID stability, and external Koorivar dependency review.
disable-model-invocation: true
---

# Output Sync Validator

## Read

- `ai/PROJECT_ARCHITECTURE.md`
- Primary guide H1 chapter list
- `gmbinder/dawn-of-the-jedaii-gmbinder.md`
- `foundry/dawn-of-the-jedaii.journal.json` (structure / page names / ownership)
- `tools/md_to_foundry_journal.py`, `tools/md_to_gmbinder.py`
- `foundry/README.md`

## Workflow

1. Compare chapter/page sets across guide, GMB, and Foundry.
2. Spot-check headings and content for staleness (do not hand-edit outputs).
3. Confirm Foundry default ownership remains GM-only (`ownership.default: 0`).
4. Investigate Foundry `_id` determinism (code uses `secrets.choice`; pilot CONFIRMED new IDs each regen — F-N-001):
   - whether regen assigns new IDs (yes in current code)
   - whether Foundry Import Data updates existing pages by `_id` or creates duplicates (needs Kakeman89 Foundry confirmation)
   - whether links, macros, or modules depend on those IDs
   - whether deterministic IDs from stable chapter identifiers are advisable
5. Review external Koorivar dependency on four axes: portability, provenance/licensing, missing-dependency behavior, guide vs GMB divergence. Do not assume vendoring.
6. Note missing generated-file notices as deferred tooling (recommend only).
7. Do not run exporters unless Kakeman89 authorizes.
8. Never “fix” JSON/GMB by hand; recommend upstream edit + regen.

## Output

Findings only. Consolidation-related tooling implications are reports, not migrations.
