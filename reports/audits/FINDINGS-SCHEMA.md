# Audit Findings Schema

**Operational — not campaign canon.**  
Use for `reports/audits/*-findings-register.yaml` and domain reports.

## Finding object

| Field | Type | Required |
|-------|------|----------|
| `id` | string (e.g. `F-A-001`) | yes |
| `audit_domain` | A–P letter or name | yes |
| `severity` | `BLOCKER` \| `HIGH` \| `MEDIUM` \| `LOW` \| `OBSERVATION` | yes |
| `confidence` | `CONFIRMED` \| `LIKELY` \| `POSSIBLE` \| `UNRESOLVED` | yes |
| `classification` | lore class or finding class string | yes |
| `title` | short string | yes |
| `description` | string | yes |
| `file_path` | repo-relative path | yes |
| `location` | line, heading, key, object id | when available |
| `related_files` | list of paths | no |
| `rule_or_skill` | string | yes |
| `evidence` | string | yes |
| `why_it_matters` | string | yes |
| `effect` | string | yes |
| `recommended_treatment` | see treatments | yes |
| `changes_approved_canon` | boolean | yes |
| `authorization_required` | boolean | yes |
| `dependencies` | list | no |
| `suggested_validation` | string | no |
| `status` | `open` \| `deferred` \| `needs_decision` \| `closed` | yes |
| `finding_kind` | `present_quality` \| `point_of_use` \| `future_placement` \| `future_migration` \| `technical` \| `other` | recommended |

## Treatments

`KEEP` | `CLARIFY` | `EXPAND` | `CONSOLIDATE` | `RESTRUCTURE` | `CORRECT` | `SOURCE` | `RECLASSIFY` | `DEFER` | `REMOVE_CANDIDATE` | `NEEDS_DECISION`

`REMOVE_CANDIDATE` never authorizes deletion.

## Point-of-use descriptors

`locally_complete` | `mostly_locally_complete` | `fragmented` | `reference_dependent` | `missing_operational_information` | `unable_to_determine`

## Lore classifications (when applicable)

`LEGENDS_VERIFIED` | `CAMPAIGN_APPROVED` | `CAMPAIGN_ADAPTATION` | `ORIGINAL_CAMPAIGN_MATERIAL` | `NEEDS_SOURCE` | `CONTINUITY_CONFLICT`
