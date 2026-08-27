---
name: final-audit-synthesis
description: Deduplicates audit findings, reconciles cross-domain conflicts, verifies manifest and crosswalk completeness, and produces the master critique including Integrated Guide Recommendation.
disable-model-invocation: true
---

# Final Audit Synthesis

## Inputs

- `reports/audits/audit-manifest.yaml`
- `reports/audits/*-findings-register.yaml`
- `reports/audits/integrated-guide-content-crosswalk.yaml`
- Domain reports under `reports/`

## Workflow

1. Deduplicate findings by evidence path + issue identity.
2. Reconcile cross-domain and cross-manuscript conflicts.
3. Verify every manifest row has a terminal status; document skips.
4. Verify crosswalk coverage and unresolved rows.
5. Separate verified defects, likely issues, subjective critique, continuity conflicts, unsupported lore, missing info, structural opportunities, sync risks, Kakeman89 decisions, and preserve-worthy strengths.
6. Write the master critique with executive summary.
7. Include section **Integrated Guide Recommendation** (evidence-based; consolidation remains NEEDS DECISION unless Kakeman89 already decided):
   - whether consolidation is recommended
   - benefits and risks
   - material for integration vs reusable reference
   - content-loss and duplication risks
   - tooling implications
   - recommended architectural direction
   - recommended pilot Act
   - decisions requiring Kakeman89
   - whether a separate migration plan should be created
8. Restate that findings are not campaign canon and do not authorize merges, deletions, or auto-fixes.
9. Never invent findings; mark gaps `UNRESOLVED`.
