# Dawn of the Jedaii — Master Critique Report

**Date:** 2026-08-26  
**Head reviewed:** `6ac41f4d3450c0bc18c133fba2d29c0b37a1aff4`  
**Authority:** Findings are operational proposals for Kakeman89. **Not campaign canon.**  
**Auto-fixes:** None applied. Manuscript consolidation: **not approved / not performed.**

Supporting artifacts:

- [`2026-08-26-findings-register.yaml`](2026-08-26-findings-register.yaml)
- [`2026-08-26-pilot-findings-register.yaml`](2026-08-26-pilot-findings-register.yaml)
- [`integrated-guide-content-crosswalk.yaml`](integrated-guide-content-crosswalk.yaml)
- [`2026-08-26-phase8-reconciliation.md`](2026-08-26-phase8-reconciliation.md)
- [`audit-manifest.yaml`](audit-manifest.yaml)
- [`../../ai/PROJECT_ARCHITECTURE.md`](../../ai/PROJECT_ARCHITECTURE.md)

---

## Executive summary

The repository is a coherent **primary campaign guide + approved Living Force companion + generated dual outputs** project with strong founding spine (Session 0 calling → ship life → Tython → Order naming), clear Appendix D provenance practice, and useful Scene Card / checklist tooling.

The most urgent **technical** defect is **GM Binder Ch22 desync** (Faces chapter replaced by a second Koorivar inject). The most urgent **design-integration** gap is **Speaker ↔ calling ↔ Kesh unmapped**. The most important **strategic** open item remains whether to later consolidate into one Act→Session→Scene integrated GM guide (**NEEDS DECISION**).

---

## Strongest existing aspects (preserve)

1. Primary-guide authority with companion deference on factual conflict  
2. Appendix D Legends vs table-fiction split  
3. Chapter 00 spoiler / handout policy  
4. Ashla/Bogan teaching lock (concepts before moon names)  
5. Session 0 Party Tho Yor calling → destined Kesh spine  
6. Scene Card Inspiration vs short read-aloud discipline  
7. Ch24 timeline tagging culture (`[L]` / `[T]` / `[GM]`)  
8. Foundry export chapter coverage + GM-only ownership  
9. Intentional Builder / Vault mysteries left open  
10. Arc I operational density (checklists + cards + maps)

---

## Most consequential risks

| Priority | Finding | Why |
|----------|---------|-----|
| 1 | **F-M-002** GMB Ch22 Faces overwritten | Print/PDF source wrong; Speakers missing from binder |
| 2 | **F-N-001** Foundry non-deterministic `_id`s | Regen/import fragility |
| 3 | **F-H-001** Speakers ↔ callings unmapped | Session 0 / Arc III cast integration hole |
| 4 | **F-G-002** Arc III depth in companion only | Guide-alone playability gap |
| 5 | **F-M-001** External Koorivar absolute path | Portability + licensing + crash on missing file |

---

## Verified defects vs subjective critique

**Verified / technical / structural (act first):** F-M-002, F-N-001, F-M-001, F-O-001, F-O-002, F-H-001, F-K-002, F-K-003, F-G-004, F-G-006, F-E-001  

**Point-of-use (improve without assuming merge):** F-G-001, F-G-002, F-G-003, F-G-005, F-I-001  

**Craft / voice policy:** F-K-001 (named-author style bible)  

**Provenance follow-ups:** F-B-002, F-C-001, F-C-002  

**Subjective / future-placement (not present defects by themselves):** F-P-001, F-P-002  

**KEEP / positive:** F-N-002, F-A-002, F-B-001, F-K-004, F-F-001  

---

## Continuity and Legends

- No audited **guide↔companion factual war**; depth and prose overlap dominate.  
- App D practice is strong; refine Ashla/Bogan gloss (F-B-002).  
- Pickup-table and Shekk-Arra rows need per-item source labeling (F-C-001/002) — absence from App D alone is not proof of unsupported lore.

---

## GM usability and Local Completeness

| Arc | Descriptor |
|-----|------------|
| I | Mostly locally complete with reference jumps |
| II | Mostly locally complete; Session 6 thin |
| III | Reference-dependent |
| IV | Climax mostly local; rising action reference-dependent |
| V–VI | Scaffold / montage-heavy |

**Local Completeness Principle:** Partial fit as a *design target*. Do **not** rewrite the books during this audit to enforce it.

---

## Template recommendation (Act / Session / Scene) — recommend only

Proposed fields from the plan were tested against Arc I / Threshold Halls:

| Field group | Assessment |
|-------------|------------|
| Act at-a-glance / purpose / factions | Useful; partly present in Ch14–15 |
| Session purpose / prep / end states | Useful; strong in Ch13/15; uneven later |
| Scene Purpose, Trigger, Read-Aloud, Scene Card, Location, Characters, Objectives, Opposition, Mechanics, Clues, RP guidance, Failure/Partial, Alternates, Transition, Consequences, Continuity, Foundry Assets | **Already present** in gold Scene Cards for key ship rooms; **optional** elsewhere; **redundant** if both companion prose and Ch21 card kept verbatim after a future merge |

Do **not** implement the template in manuscripts under this report.

---

## Integrated Guide Recommendation

### Is consolidation recommended?

**Conditional recommendation:** Yes — **evaluate and plan** consolidation into one Act→Session→Scene GM guide **after** Kakeman89 decides, using Arc I as the pilot.  
**Not approved by this report.** Companion must not be deleted or archived by this recommendation.

### Expected benefits

- Reduce Threshold/ship room dual maintenance  
- Colocate Arc III contact play with Speakers and scenes  
- Align print and Foundry exports to a single runnable source  
- Improve point-of-use completeness without losing reference appendices  

### Expected risks

- Loss of companion voice if merged carelessly  
- Excessive local repetition if Scene Cards are inlined everywhere  
- Linear Act/Session structure implying mandatory player paths (railroading)  
- Heading/link/Foundry ID instability during migration  
- Premature archival of unique companion material  

### Material most suitable for integration

- Arc I–II session text + matching Scene Cards  
- Companion §4 ship living prose (as local Inspiration or merged card)  
- Arc III contact scenarios currently companion-heavy  

### Material best kept as reusable reference

- Appendix D provenance  
- Full species spotlight / SW5e rule banks  
- Timeline appendices  
- Map briefs library  
- Faction playbooks (with local summaries at point-of-use)  

### Content-loss risks

- Companion-only Arc III/IV color if migration copies guide beats only  
- Craftsman/Speaker walk-on texture  

### Duplication risks

- Threshold Halls and other Ch21↔§4 pairs  
- Dual Koorivar presentation after tool bug compounds confusion  

### Tooling implications

- Fix GMB Ch22 matcher **before** treating binder as current  
- Stabilize Foundry IDs if journals must update in place  
- Resolve Koorivar dependency without assuming vendoring  
- Add dry-run/backup to write tools  

### Recommended final architectural direction

**NEEDS DECISION:** Prefer a future **single authoritative integrated GM guide** with Act→Session→Scene chapters plus appendices for heavy reference — **if** Kakeman89 accepts migration cost. Until then, **preserve** primary+companion.

### Recommended pilot Act

**Arc I** (Sessions 1–3 / Episode 1 ship half) — highest completeness, clearest duplicate evidence, lowest lore invention need. Stress-test second: Arc III.

### Decisions requiring Kakeman89

See Phase 10 backlog. Critical: consolidation go/no-go; Speakers↔callings mapping policy; GMB tool fix authorization; Foundry ID strategy; Koorivar handling; named-author style bible rewrite; Tython naming in App C.

### Separate migration plan?

**Yes — create only after Phase 10 review if Kakeman89 authorizes.** Do not treat this critique as that plan. Migration skill remains deferred.

---

## Completeness check

| Item | Status |
|------|--------|
| Architecture doc | Present |
| Rules R1–R6 | Present |
| Seven active skills + deferred watcher | Present |
| Manifest + schemas + crosswalk | Present |
| Pilot + full findings | Present |
| Reconciliation | Present |
| Integrated Guide Recommendation | Present |
| Manuscript merge | **Not done** |
| Auto content fixes | **Not done** |

---

## Recommended correction sequence (if later authorized)

1. Fix `md_to_gmbinder.py` Ch22 matcher; regenerate GMB  
2. Clarify Speakers↔callings (or mark Speakers calling-agnostic)  
3. Clarify App C Tython naming; Storm Clock citation; Episode 1 / Arc II boundary; landing milestones; Omen ownership  
4. Replace named-author style bible with anonymous qualities  
5. Expand Arc II S6 / Arc III / Arc IV trial operational hooks as desired  
6. Foundry deterministic IDs + dry-run tooling  
7. Koorivar four-axis decision  
8. Only then: separate integrated-guide migration plan (if approved)
