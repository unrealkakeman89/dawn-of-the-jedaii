---
name: legends-source-audit
description: Verifies Star Wars Legends lore and repository provenance for campaign claims. Use when checking characters, planets, cultures, factions, technology, history, Force traditions, timelines, Appendix D coverage, mechanics sources, or unsupported claims.
disable-model-invocation: true
---

# Legends Source Audit

Combines Legends verification and repository provenance. Enforces Legends continuity and source-and-canon rules. Does not rewrite approved content.

## Workflow

1. Read applicable project rules and `ai/PROJECT_ARCHITECTURE.md`.
2. Identify exact lore or mechanics claims.
3. Check Appendix D **where it covers** the claim.
4. If absent from Appendix D, search remaining approved repository content (primary guide, companion, READMEs, Kakeman89-approved notes) before `NEEDS_SOURCE`.
5. Classify each claim:
   - `LEGENDS_VERIFIED`
   - `CAMPAIGN_APPROVED`
   - `CAMPAIGN_ADAPTATION`
   - `ORIGINAL_CAMPAIGN_MATERIAL`
   - `NEEDS_SOURCE`
   - `CONTINUITY_CONFLICT`
6. Check continuity-specific versions (Legends vs Disney shared names — not interchangeable).
7. Check era appropriateness (36,453 BBY / 0 TYA).
8. Check compatibility with established campaign material.
9. Record source path or provenance when available.
10. Cover mechanics provenance (SW5e) separately from lore.
11. Paraphrase copyrighted material; do not reproduce long passages.
12. Report conflicts without choosing a silent rewrite.
13. Do not import Disney-canon to fill Legends gaps.
14. Do not modify authoritative campaign prose unless the task explicitly authorizes it.

## Output per claim

- Claim
- Classification
- Supporting source or repository path
- Era compatibility
- Campaign compatibility
- Conflict, if any
- Recommended treatment
- Files potentially affected

If verification is incomplete, use `NEEDS_SOURCE`. Never guess.
