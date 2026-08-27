# Arc III Pilot - Change Manifest

**Date:** 2026-08-27  
**Authority:** Provisional pilot audit package - non-authoritative

## Files created

| Path | Purpose |
|------|---------|
| `ai/migration-workspace/arc-iii-integrated-candidate.md` | Provisional Arc III integrated candidate |
| `tools/md_to_arc_iii_pilot_foundry_journal.py` | Arc III pilot Foundry generator |
| `foundry/arc-iii-pilot.journal.json` | Pilot Foundry journal (8 pages) |
| `gmbinder/arc-iii-pilot-gmbinder.md` | Pilot GM Binder content export |
| `reports/audits/arc-iii-pilot-continuity-audit.md` | Continuity audit |
| `reports/audits/arc-iii-pilot-legends-audit.md` | Legends/source audit |
| `reports/audits/arc-iii-pilot-mechanics-audit.md` | Mechanics language audit |
| `reports/audits/arc-iii-pilot-read-aloud-audit.md` | Read-aloud audit |
| `reports/audits/arc-iii-pilot-player-agency-audit.md` | Player-agency audit |
| `reports/audits/arc-iii-pilot-point-of-use-audit.md` | Point-of-use audit |
| `reports/audits/arc-iii-pilot-controlled-repetition-audit.md` | Controlled-repetition audit |
| `reports/audits/arc-iii-pilot-companion-depth-audit.md` | Companion-depth preservation audit |
| `reports/audits/arc-iii-pilot-content-loss-comparison.md` | Source-to-candidate content-loss comparison |
| `reports/audits/arc-iii-pilot-map-foundry-audit.md` | Map/Foundry design audit |
| `reports/audits/arc-iii-pilot-change-manifest.md` | This manifest |
| `reports/audits/arc-iii-pilot-acceptance.md` | Arc III pilot acceptance package |

## Files modified

| Path | Change |
|------|--------|
| `reports/audits/integrated-guide-content-crosswalk.yaml` | Updated Arc III pilot rows `CW-006`, `CW-029`-`CW-044`; added `CW-001-P-III`; preserved `CW-045`-`CW-050` as deferred / `NEEDS_DECISION` evidence |

## Candidate status

`ai/migration-workspace/arc-iii-integrated-candidate.md` is the subject of this package (created for the stress test). Remains **PROVISIONAL / NON-AUTHORITATIVE**.

## Source manuscripts modified

**None.**

- `dawn-of-the-jedaii-campaign-guide.md`
- `gm-narrative/dawn-of-the-jedaii-living-force-gm-book.md`

## Production outputs modified

**None.**

- `foundry/dawn-of-the-jedaii.journal.json`
- `gmbinder/dawn-of-the-jedaii-gmbinder.md`

## Pilot outputs (non-production)

| Path | Notes |
|------|-------|
| `foundry/arc-iii-pilot.journal.json` | 8 pages; deterministic IDs; never overwrites production |
| `gmbinder/arc-iii-pilot-gmbinder.md` | Content export; pagination `DEFERRED_PARTIAL` |

## Crosswalk migrations (Arc III pilot status)

| ID | Status |
|----|--------|
| `CW-006` | `consolidate_complete`, `pending_kakeman89_acceptance` |
| `CW-029`-`CW-033` | `consolidate_complete`, `pending_kakeman89_acceptance` |
| `CW-034`-`CW-036` | `synthesized`, `pending_kakeman89_acceptance` |
| `CW-037`, `CW-039`, `CW-042` | `migrated`, `pending_kakeman89_acceptance` |
| `CW-038` | `preserved_distinct_in_candidate`, `pending_kakeman89_acceptance` |
| `CW-040`, `CW-041` | `migrated`, `pending_kakeman89_acceptance` |
| `CW-043` | `unresolved_gate_preserved`, `pending_kakeman89_acceptance` |
| `CW-044` | `pilot_executed`, `pending_kakeman89_acceptance` |
| `CW-001-P-III` | `pilot_complete`, `pending_kakeman89_acceptance` |
| `CW-045`-`CW-050` | Deferred / `NEEDS_DECISION`; no mapping approved |

## Validation results

| Audit / gate | Result |
|--------------|--------|
| Continuity | PASS |
| Legends/source | PASS |
| Mechanics language | PASS |
| Read-aloud | PASS |
| Player agency | PASS |
| Point of use | PASS |
| Controlled repetition | PASS |
| Companion depth preservation | PASS |
| Content-loss comparison | PASS |
| Map/Foundry design | PASS |
| F-N-001 disposable-world validation | **INCOMPLETE** - not tested in this package |
| Pagination F-M-003 | `DEFERRED_PARTIAL` - unchanged |

## Outstanding conditions

- Candidate remains provisional and non-authoritative.
- No Calling -> Speaker -> Kesh mapping is approved.
- Scenario-casting labels are present but remain operational only.
- Source manuscripts remain unchanged by process result.
- No production Foundry or GM Binder pilot output was generated or modified in this package.

## Recommendation snapshot

`ACCEPT_WITH_REVISIONS`

Reason: Arc III pilot audit evidence supports the candidate structure, local completeness, branch discipline, and companion-depth preservation. Remaining conditions are Kakeman89 acceptance, F-H-001 non-approval, F-N-001 live Foundry validation if later output is created, and the already-deferred pagination posture.
