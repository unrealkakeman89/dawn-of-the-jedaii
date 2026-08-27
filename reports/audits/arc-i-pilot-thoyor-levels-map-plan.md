# Arc I Pilot — Tho Yor Multi-Level Map & Foundry Levels Plan

**Status:** Operational recommendation — **PROVISIONAL spatial design**  
**Date:** 2026-08-27  
**Authority:** Kakeman89 table-usability review (Arc I pilot revision)  
**Not:** LEGENDS_VERIFIED lore · established campaign canon · production Foundry scene pack

**Related:** `ai/migration-workspace/arc-i-integrated-candidate.md` · `foundry/arc-i-pilot.journal.json` (pilot journal only)

---

## Classification key

| Label | Meaning |
|-------|---------|
| **Recommended design** | Suggested Foundry / prep layout for table use |
| **Established campaign fact** | Supported by primary guide / companion |
| **Provisional spatial arrangement** | Pilot recommendation; may change after Kakeman89 review |
| **Foundry implementation suggestion** | Tooling approach; not lore |

---

## 1. Recommended number of Tho Yor Levels

**Recommendation: four Foundry Levels** (provisional spatial arrangement).

Rationale (table usability, not lore):

1. Separates arrival/social pressure (Threshold) from living/civic space (Pilgrim).
2. Groups Force-facing wonder (Contemplation) above restricted builder/Kwa material (Restricted).
3. Matches Session 1 → 2 → 3 beat progression without one flat megamap.
4. Keeps Map 1 as a **detailed encounter map** inside Level 1 rather than equating it to the whole ship.

**Established campaign fact:** The Tho Yor contains playable zones listed in Ch04 (Threshold, Dormitories, Galleries, Meditation Cores, Machine-Spirit Interfaces, Sealed Vaults, Confluence Amphitheater, Disembarkation Spines). Relative vertical stacking of those zones is **not** established as fixed architecture in the primary guide.

---

## 2. Four-level design (recommended provisional)

| Level | Name | Approx. elevation (provisional) | Contents | Primary sessions |
|-------|------|----------------------------------|----------|------------------|
| 1 | **Threshold Level** | Entry / mid-low | Threshold Halls; central dais; Call-door (sealed); sealed northern door; W approach to Dormitories; E approach toward Galleries (stair/passage up); social-contact area; optional panicked-creature / brawl area | Session 1 arrival |
| 2 | **Pilgrim Level** | Living mid | Dormitories of the Called; sleeping niches; privacy weaves; relic shelves; communal ration/craft spaces; Confluence Amphitheater; null-corridor access; service passages | Session 1 bonding; Session 3 council |
| 3 | **Contemplation Level** | Upper wonder | Observation Galleries; Meditation Core; vision/devotional alcoves; overlooks; vertical connections; access toward Machine-Spirit | Session 2 |
| 4 | **Restricted Level** | Deep / sealed | Machine-Spirit Interface; Kwa mural corridor; Sealed Vaults; Gate antechamber threshold; guardian-presence area; locked route toward Disembarkation Spines; maintenance/null corridors | Session 2 restricted; Arc II transition |

**Map 1 note:** Map 1 — Tho Yor: Threshold Crossroads (Ch23; 35×35) is a **detailed encounter map within Level 1**, not a full-vessel diagram.

---

## 3. Alternative three-level version

Collapse if asset budget is tight:

| Level | Merge |
|-------|--------|
| A — Entry & Living | Threshold + Dormitories + Confluence |
| B — Contemplation | Galleries + Meditation Core |
| C — Restricted | Machine-Spirit + Vaults + Gate approach |

**Trade-off:** Session 3 council shares space with Session 1 dormitories — higher visual clutter; simpler inter-level pins.

---

## 4. When five or more levels are justified

Consider additional levels only if Kakeman89 later authorizes:

- Separate **Disembarkation Spines** as its own Level (Arc II)
- Separate **A2 Chamber of First Calling** upper floor (if authorized into sources)
- Distinct **null-corridor maze** with combat grids
- Separate **sister-ship silhouette gallery** as a travel cutaway

Do not add levels merely because Foundry supports them.

---

## 5. Location-to-level mapping

| Location | Level | Dedicated map? | Shares map? | Combat grid | Exploration | Social | Theater of the Mind OK? | Needed for Arc I now? |
|----------|-------|----------------|--------------|-------------|-------------|--------|-------------------------|------------------------|
| Threshold Halls / Map 1 Crossroads | 1 | **Yes** (Map 1) | May extend to dormitory approach | High | High | High | Partial | **Yes** |
| Dormitories of the Called | 2 | Recommended | Can share Level 2 parent with Confluence | Low–med | Med | High | Often yes | Optional detail map |
| Observation Galleries | 3 | Optional | Can share Level 3 | Low | High | Med | Often yes | Optional |
| Meditation Core | 3 | Optional | Can share Level 3 | Low | Med | High (trial) | **Usually yes** | Optional |
| Machine-Spirit Interface | 4 | Recommended | Shares Restricted with Vault corridor | Med | High | Low | Partial | Recommended if skill challenge uses tokens |
| Sealed Vaults | 4 | Optional | Shares Restricted | Low | Med | Low | **Usually yes** | Optional (glimpse) |
| Confluence Amphitheater | 2 | Recommended | Can share Level 2 | Med (brawl) | Low | **High** | Partial | Recommended for Session 3 |
| Disembarkation Spines | 4→surface / Arc II | Arc II Map 2 | Transition from Level 4 | High (Arc II) | Med | Med | No for landing | **Deferred** (Arc II) |

---

## 6. Session-to-level mapping

| Session | Primary levels | Notes |
|---------|----------------|-------|
| 0 | N/A (table) | No ship map required |
| 1 | 1 → 2 | Map 1 start; move W into Pilgrim Level |
| 2 | 3 → 4 | Contemplation then Restricted |
| 3 | 2 → 3 | Council on Pilgrim; Approach return to Galleries |
| Arc II S5 | 4 → exterior | Spines + Map 2 Storm-Scar |

---

## 7. Map coverage status

| Asset | Status |
|-------|--------|
| Map 1 Threshold Crossroads (Ch23) | Spec exists in sources/candidate — **build in Foundry** |
| Map 2 Storm-Scar | Arc II — out of Arc I play |
| Full-vessel level diagrams | **Not created** — provisional plan only |
| Graphical map art | **Deferred** — no binaries this task |

---

## 8. Maps required / optional / deferred (Arc I)

**Required now (spec + Foundry build from Ch23):**

- Map 1 Threshold Crossroads (Level 1 encounter map)

**Optional for Arc I (improve table use):**

- Level 2 overview (Dormitories + Confluence footprint)
- Level 3 overview (Galleries + Core)
- Level 4 Restricted corridor strip (Machine-Spirit → Vaults)

**Deferred:**

- Disembarkation Spines detailed map (Arc II)
- Map 5 Chamber of First Calling (A2 — not in repo)
- Full isometric vessel cutaway art

---

## 9. Foundry Levels strategy (implementation suggestion)

**Preferred approach (maintainability):** One parent Scene Collection **“Tho Yor — Party Ship (Pilot)”** containing **four scenes** (one per Level), linked by labeled stair/passage tokens and journal pins — **not** a single stacked canvas unless the installed Levels module is confirmed and preferred by Kakeman89.

**Alternative:** One scene with Levels module layers (Level 1–4) if the table’s Foundry install includes a maintained Levels module and Kakeman89 prefers vertical stacking. Exact Levels API/data model is **not** assumed here (no repository evidence of module config).

### Implementation checklist (when Kakeman89 authorizes scene build)

1. Create four scenes: `Tho Yor L1 Threshold`, `L2 Pilgrim`, `L3 Contemplation`, `L4 Restricted`.
2. Place Map 1 grid on L1; approximate footprints elsewhere until art exists.
3. Stair/passage endpoints: L1 W → L2 Dormitories; L1 E up → L3 Galleries approach; L2 → L3 service stair; L3 → L4 Machine-Spirit hatch (locked until Session 2).
4. GM-only regions: L4 Vault seal interior; Gate antechamber beyond threshold; GM notes journal.
5. Player-accessible: L1–L3 public decks; L4 only after Session 2 access.
6. Journal pins: Scene Cards + Arc I pilot journal pages (`foundry/arc-i-pilot.journal.json`).
7. Do **not** import into Kakeman89’s personal campaign world for testing — use a disposable world.

### Approximate elevations (provisional labels only)

| Level | Label |
|-------|-------|
| L1 | 0 ft (entry datum) |
| L2 | +20 ft |
| L3 | +45 ft |
| L4 | −15 ft (deep / restricted relative to entry) |

These numbers are **Foundry bookkeeping**, not canon ship dimensions.

---

## 10. Transitions

| From | To | Means (provisional) | Visible to players? |
|------|-----|---------------------|---------------------|
| L1 Threshold | L2 Dormitories | West corridor / stair | Yes |
| L1 Threshold | L3 Galleries | East ascent | Yes |
| L2 Dormitories | L2 Confluence | Horizontal deck | Yes |
| L2/L3 | L4 Machine-Spirit | Hatch / colder corridor | Yes after Session 2 unlock |
| L4 | Spines (Arc II) | Locked route | GM foreshadow only in Arc I |

Teleport/region behavior: use door tiles or manual scene transitions unless Levels module regions are configured later.

---

## 11. GM-only vs player-visible

| Area | Visibility |
|------|------------|
| Threshold, Dormitories, Galleries, Core, Confluence | Player-visible when entered |
| Machine-Spirit lattices + Kwa murals | Player-visible when entered (Session 2) |
| Vault interior / seed map | **GM-only** until intentionally opened (not Arc I) |
| Gate activation | **GM-only** / locked (Ch08) |
| Builder identity answers | **GM-only** (ambiguous by design) |

---

## 12. Asset requirements (future)

- Map 1 Foundry wall/floor tiles matching Ch23 legend
- Optional silhouette gallery backdrop (no Tython name labels for players)
- Restricted corridor “wrong script” mural tokens
- Stair markers between levels
- No invented binary art in this task

---

## 13. Unresolved spatial-canon decisions (Kakeman89)

1. Confirm **four-level** vs **three-level** provisional layout.
2. Confirm whether Contemplation is above Pilgrim or adjacent (horizontal).
3. Confirm Disembarkation Spines attachment (Level 4 exit vs separate Arc II scene only).
4. Authorize A2 upper floor if it should become Level 5 / Level 1 loft.
5. Prefer multi-scene collection vs Levels module stacking for the personal table install.

---

## 14. Explicit non-claims

- This plan does **not** establish Tho Yor deck count as Legends lore.
- This plan does **not** replace Ch04 zone list.
- Map 1 remains the only fully specified Arc I encounter grid in sources.
- Production Foundry journal is unchanged; pilot journal may reference this plan in Act overview only.
