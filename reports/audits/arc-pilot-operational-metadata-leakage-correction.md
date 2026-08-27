# Arc I / Arc III Pilot — Operational Metadata Leakage Correction

**Date:** 2026-08-27  
**Authority:** Operational audit correction — not campaign canon  
**Rule:** `.cursor/rules/operational-metadata-not-in-guide-prose.mdc`

## Problem

Internal migration and casting classifications (for example `SOURCE_SUPPORTED_SCENARIO_CAST`) appeared in readable provisional candidates and regenerated into pilot Foundry / GM Binder pages.

## Scope corrected

- `ai/migration-workspace/arc-i-integrated-candidate.md`
- `ai/migration-workspace/arc-iii-integrated-candidate.md`
- `foundry/arc-i-pilot.journal.json`
- `foundry/arc-iii-pilot.journal.json`
- `gmbinder/arc-i-pilot-gmbinder.md`
- `gmbinder/arc-iii-pilot-gmbinder.md`
- `.cursor/skills/integrated-guide-migration/SKILL.md`
- Pilot Foundry generators (publication strip of HTML comments and Development Decisions)

## Visible labels removed from readable prose

Casting enums, finding IDs, crosswalk IDs, Source Traceability Scene Card rows, Legends/campaign classification enums, and status enums such as `SUPERSEDED_BY_KAKEMAN89` / `REQUIRES_KAKEMAN89` / `LEGENDS_VERIFIED`.

## Natural GM-facing replacements

| Was | Now |
|-----|-----|
| `SOURCE_SUPPORTED_SCENARIO_CAST` | Suggested Speaker |
| `RECOMMENDED_SUBSTITUTABLE_CAST` | Alternative Speaker |
| `INDEPENDENT_OF_CALLING` | This role does not need to match the party’s calling. |
| Finding IDs in prose | Natural decision language; IDs only in development comments / reports |
| Source Traceability table rows | `<!-- SOURCE-TRACE: ... -->` comments |

## Traceability retained

- `reports/audits/integrated-guide-content-crosswalk.yaml`
- Change manifests and acceptance packages under `reports/audits/`
- Non-rendered `SOURCE-TRACE` HTML comments in candidates
- `## Development Decisions Still Required` (excluded from publication exports)

## Validation

Post-correction searches of candidates (visible prose only) and pilot outputs found **no** prohibited operational labels. Scenario casting remains understandable via Suggested / Alternative Speaker tables. Calling-to-Speaker mappings remain unapproved. Source manuscripts and production outputs unchanged.

## Recommendation impact

Does not change Arc I or Arc III acceptance recommendations. This is a presentation/boundary correction only.
