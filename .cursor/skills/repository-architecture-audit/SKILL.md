---
name: repository-architecture-audit
description: Audits repository source-of-truth boundaries, generated outputs, tool I/O paths, and overwrite risks. Use when mapping architecture, confirming edit boundaries, or before full content audits.
disable-model-invocation: true
---

# Repository Architecture Audit

## Read first

- `ai/PROJECT_ARCHITECTURE.md`
- Root `README.md`, `foundry/README.md`, `gm-narrative/README.md`
- All `tools/*.py`
- Guide Ch00 / Appendices D–E; GMB cover if present

## Workflow

1. Confirm primary authority vs approved companion vs generated outputs.
2. Document or verify tool read/write paths.
3. Identify protected files and dangerous scripts.
4. Record integrated-guide consolidation as **NEEDS DECISION** (do not merge).
5. Flag overwrite and sync risks (Foundry IDs, external Koorivar path, missing notices).
6. Write findings using the shared findings schema when auditing.
7. Update `ai/PROJECT_ARCHITECTURE.md` only when Kakeman89 authorized that update.

## May change (when authorized)

- `ai/PROJECT_ARCHITECTURE.md`
- Architecture notes under `ai/plans/` or `reports/audits/` only

## Never change

- Campaign manuscripts, generated GMB/Foundry content, live Foundry worlds

## Stop if

Write-path ambiguity is unresolved, or the task would require merging manuscripts.
