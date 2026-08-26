---
name: adventure-and-guide-critique
description: Report-only critique of adventure design, GM guide usability, point-of-use completeness, prose voice, Living Force structure, and integrated-guide feasibility. Never rewrites content or invokes adventure-architect.
disable-model-invocation: true
---

# Adventure and Guide Critique

**Report-only audit skill.** Never invoke `adventure-architect`. Never rewrite, merge, or migrate manuscripts while evaluating them.

## Covers

- Campaign structure, adventure design, characters/factions (critique), setting usability, prose/house voice, GM usability, Living Force-style structure
- Point-of-use completeness (Act / session / scene)
- Avoidable chapter jumping vs reasonable reference lookup
- Domain P — Integrated GM Guide Feasibility (evaluate only)
- Crosswalk entry proposals for `reports/audits/integrated-guide-content-crosswalk.yaml`

## Point-of-use

For representative Acts/sessions/scenes, assess using:

`locally_complete` | `mostly_locally_complete` | `fragmented` | `reference_dependent` | `missing_operational_information` | `unable_to_determine`

Check scene cards, local mechanics, character goals/knowledge, clues/consequences, prep, transitions, alternate approaches, and whether the GM must leave the chapter.

## Local Completeness Principle (test only)

A runnable scene chapter should contain all information required to understand, prepare, and adjudicate that scene, except universally reused mechanics, full-length reference entries, or material whose controlled separation serves a clear purpose.

Test whether this fits the campaign. **Do not** rewrite chapters to enforce it.

## Domain P neutrality

Do not classify existing content as defective merely because it may later be moved, locally summarized, repeated, consolidated, or reformatted. Separate:

- present-content quality findings
- present point-of-use usability findings
- future-placement recommendations
- future migration recommendations

A useful reference chapter is not defective merely because some information may later be summarized locally.

## Template recommendation (do not implement)

Recommend Act / Session / Scene field sets from the project audit plan. Mark each field: already present | useful | optional | redundant | unable to determine.

## Named-author policy

Do not score prose against named authors. If repository craft guidance *instructs* imitation of named authors, file a present-quality finding against house-voice policy (see pilot F-J-001). Recommend anonymous quality language instead.

## Output

Findings only (shared schema) and crosswalk entries. No content edits. No named-author scoring.
