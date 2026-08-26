# Integrated Guide Content Crosswalk — Schema

**Artifact path:** `reports/audits/integrated-guide-content-crosswalk.yaml`  
**Operational — not campaign canon.** Populate during Phases 5/7/8 without moving content.

## Per-section fields

| Field | Description |
|-------|-------------|
| `id` | Unique crosswalk row id (e.g. `CW-001`) |
| `source_file` | Path to manuscript |
| `source_heading` | Heading text |
| `source_anchor_or_location` | Line range or anchor |
| `content_category` | Short category label |
| `campaign_arc` | When determinable |
| `session` | When determinable |
| `scene` | When determinable |
| `current_authority` | `primary_guide` \| `approved_companion` \| `both` \| `unclear` |
| `overlap_with_other_manuscript` | Description or `none` |
| `conflict_status` | `none` \| `presentation_only` \| `factual` \| `unresolved` |
| `proposed_destination_type` | See destinations |
| `local_use_requirement` | boolean or note |
| `reusable_reference_requirement` | boolean or note |
| `gm_only_status` | boolean or note |
| `player_visible_status` | boolean or note |
| `mechanics_dependency` | note |
| `foundry_dependency` | note |
| `gmbinder_dependency` | note |
| `proposed_treatment` | See treatments |
| `kakeman89_decision_required` | boolean |
| `audit_status` | `pending` \| `mapped` \| `needs_decision` \| `deferred` |

## Destination types

`campaign_foundations` | `world_reference` | `act_overview` | `session_overview` | `scene` | `reusable_gm_reference` | `appendix` | `generated_output_only` | `archive_candidate` | `unresolved`

## Treatments

`KEEP_IN_PLACE_DURING_AUDIT` | `MIGRATE_CANDIDATE` | `CONSOLIDATE_CANDIDATE` | `LOCAL_SUMMARY_CANDIDATE` | `CENTRAL_REFERENCE_CANDIDATE` | `PRESERVE_DISTINCT` | `REMOVE_CANDIDATE` | `NEEDS_DECISION`

`archive_candidate` and `REMOVE_CANDIDATE` never authorize archival or deletion.

## Neutrality

Do not treat a useful reference chapter as defective merely because future placement may change. Separate present quality from future-placement recommendations.
