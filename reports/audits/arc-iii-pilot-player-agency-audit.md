# Arc III Pilot - Player Agency Audit

**Date:** 2026-08-27  
**Scope:** All runnable Arc III scenes in `ai/migration-workspace/arc-iii-integrated-candidate.md`

## Method

Verified each major Arc III beat includes some combination of:

- more than one approach
- bypass, deferral, or alternate branch support where applicable
- failure or partial-success handling
- consequences that preserve play instead of dead-ending it

## Results

| Scene / beat | Entry alt | Bypass / defer | Failure | Partial | Alternate approach | Status |
|--------------|-----------|----------------|---------|---------|--------------------|--------|
| `Scout Valley` | Different camp need or rumor | Retreat early with only a partial read | Yes | Yes | Harvest, sample, meditate, split roles | PASS |
| `Rival Smoke Ridge` | Bearings, spoor, wrong smoke, or claim-signs | Observe only and withdraw | Yes | Yes | Token, envoy, peace signal, hidden mapping | PASS |
| `Camp Return Consequence` | Public or quiet debrief | Split truth by audience | Yes | Yes | Report by token, map, witness, or partial truth | PASS |
| `Border Trade` | Controlled meet from either camp | Labor, meal, or witness-first exchange | Yes | Yes | Envoy, crafter lead, shared watch, visible gifts | PASS |
| `Stolen Tool Diplomacy` | Theft, debt, insult, or alliance test | Leave with named grievance instead of settlement | Yes | Yes | Gift return, witness ruling, expose third party, accept challenge logic | PASS |
| `Omen Night Speech` | PC-led or Speaker-led naming moment | Alternate branch if Omen already ran in Arc II | Yes | Yes | Shared chant, proclamation, oath, translated repetition | PASS |
| `Purge Stop` | Social first, tactical if needed | Protect and evacuate instead of fight-to-finish | Yes | Yes | Crowd turn, witness line, ritual pause, command cost | PASS |
| `Alternate Session 9: Resource War` | Activated only if Arc II already used the Omen | Entire Omen replay is blocked by design | Yes | Yes | Scarcity-first continuation | PASS |
| `Spring Claim` | Resource point can be spring, ford, grove, or similar | Shared-law, witness pact, or duel route | Yes | Yes | Find more water, use healers, accept compromise burden | PASS |
| `Joint Rite` | Meditation, labor, healing line, or local custom | Can become the main Session 10 path or be skipped for the other path | Yes | Yes | Shared labor, confession circle, watch exchange | PASS |
| `Faction Flag Camp` | Observe or intervene | Scene itself is optional | Yes | Yes | Shared meal, symbol choice, camp walk | PASS |
| `Map 3 Approach` | Rumor, curiosity, Qigong pull, or blank map line | Full non-visit path is valid | Yes | Yes | Map and leave, meditate, split relay positions | PASS |
| `Map 4 Moon Road` | Myth pull, Yen-Ti pressure, Omen fallout, or proof-seeking | Never-open completion is explicitly valid | Yes | Yes | Decode and leave, guard in secret, limited trial, defer until later | PASS |
| `Scar Council` | Public council or small-circle pre-council | Honest ally/rival deficit recording is allowed | Yes | Yes | Witness objects, split memory/ruling phases, child or crafter truth-teller | PASS |
| `Neighborhood Map Review` | Public drawing or reveal of private draft | Honest blanks are allowed | Yes | Yes | Tokens, different witness layers, contested-site adjudication only if needed | PASS |

## Flagged sequence dependencies

| Beat | Mandatory? | Candidate treatment |
|------|------------|--------------------|
| One complete scout loop | Structural Arc III beat | Required in Session 7 with multiple discovery and consequence routes |
| First meaningful sister-camp contact | Structural Arc III beat | Session 8 requires contact but allows peace, honor, or failure outcomes |
| Omen of the Moons | Conditional structural beat | Default Session 9 only if not already used at Arc II close |
| Session 10 main pressure path | Structural Arc III beat | Choose `Resource War` or `Joint Rite`; optional maps do not replace the main path |
| Session 11 scar and map close | Structural Arc III beat | Requires public inventory, but honest deficits and unresolved blanks are allowed |
| Map 3 | Optional | Fully skippable |
| Map 4 | Optional advanced | Fully skippable; never-open path counts as completion |
| Full Counting Quarrel workshop | Not part of default Arc III | Seed only; full quarrel remains Arc IV-primary |

## Recommendation

PASS - no mandatory screenplay detected. The candidate enforces source-backed structural beats but preserves alternate branches, optional map paths, failure consequences, and honest incomplete outcomes.
