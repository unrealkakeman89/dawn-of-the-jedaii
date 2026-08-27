# Arc III Pilot - Map / Foundry Audit

**Status:** Operational - not campaign canon  
**Date:** 2026-08-27  
**Scope:** `ai/migration-workspace/arc-iii-integrated-candidate.md`

## Summary

The Arc III pilot candidate handles maps and Foundry structure as optional support rather than mandatory rails. Map 3 and Map 4 both preserve theater fallback, and Map 4 explicitly keeps a never-open completion path. Pilot Foundry JSON was generated at `foundry/arc-iii-pilot.journal.json` (8 pages). **F-N-001** disposable-world import remains an outstanding validation gate.

## Candidate checks

| Check | Result | Notes |
|------|--------|-------|
| Map 3 optional but in-scope | PASS | Candidate includes local spec, theater fallback, bypass, and non-visit consequence language |
| Map 4 optional advanced path | PASS | Candidate treats Gate play as optional and secondary to the social-contact spine |
| Never-open Map 4 completion path | PASS | Explicitly documented as a valid Arc III outcome |
| Theater-of-the-mind for ordinary contact scenes | PASS | Camp, ridge, border, spring, rite, and council scenes do not require dedicated tactical maps |
| Dedicated map use when justified | PASS | Map 3 and Map 4 are the clearest candidates for separate scenes if assets exist |
| Provisional mixed Foundry hierarchy | PASS | Candidate names `Arc III Overview`, Sessions 7-11, `Arc III Contacts and Speakers`, and `Player Handouts` without claiming production status |
| Empty-scene avoidance | PASS | Candidate says separate scene pages are most justified for Map 3 and Map 4 or unusually large packets |
| Four-level Tho Yor not reused as Tython lore | PASS | Arc III stays surface/social and does not mislabel ship-spatial planning as world canon |
| F-N-001 disposable-world import test | OUTSTANDING | Pilot JSON exists at `foundry/arc-iii-pilot.journal.json` (8 pages; deterministic IDs); disposable-world import not run |

## Map posture by area

| Area | Candidate posture |
|------|-------------------|
| Scout valleys / rival ridges / springs | Theater default |
| Camp-night and council play | Journal-first; map optional |
| `Map 3 Approach` | Optional dedicated scene if assets exist; theater fallback valid |
| `Map 4 Moon Road` | Optional dedicated scene if used; journal-only if discovered or deferred |
| Player-facing near-wild map | Handout blank plus evolving marks |

## Outstanding gate

`F-N-001` is still open at the process level. Pilot journal `foundry/arc-iii-pilot.journal.json` was generated and statically validated (8 pages, unique IDs, Sessions 7–11 + Contacts + Handouts). No disposable-world import test was run. That is not a failure of the candidate's map logic, but it remains an acceptance gate before trusting update-in-place Foundry behavior.

## Recommendation

PASS for Arc III map/Foundry design. Keep the candidate in audit-only status, and treat any later Foundry export as blocked on a disposable-world validation pass before trusting update-in-place behavior.
