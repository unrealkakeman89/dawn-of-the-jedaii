# Blocker & Generator Reliability — Implementation Report

**Date:** 2026-08-26  
**Plan:** [`ai/plans/2026-08-26-blocker-generator-reliability-correction.md`](../../ai/plans/2026-08-26-blocker-generator-reliability-correction.md)  
**Status:** Operational record (not campaign canon)

---

## Findings

| ID | Result |
|----|--------|
| **F-M-002** | **RESOLVED** — GMB injects Koorivar into Ch 12; Ch 22 is Faces; Speakers present; App E consistent; regenerated via corrected tool (no hand-edit fix) |
| **F-N-001** | **PARTIAL** — Deterministic IDs implemented + offline stability validated; live Foundry Import Data update-vs-duplicate **not** verified in a world |
| **F-M-001** | **PARTIAL** — Portable discovery + fail-loud missing dependency implemented; licensing/vendoring **not** presumed; four-axis review recorded |
| **F-O-001** | **RESOLVED** — `--dry-run`, backups, staged replace, nonzero failure for GMB + Foundry writers |
| **F-O-002** | **RESOLVED** — Reorder script marked historical; defaults to refuse-write; dual confirmation flags required to write |
| **F-K-002** | **DECIDED** (decision record only) — staged Tython reveal; **prose not implemented** in this task |

## Commands executed (representative)

```text
python tools/md_to_gmbinder.py --dry-run
python tools/md_to_gmbinder.py
python tools/md_to_foundry_journal.py --dry-run
python tools/md_to_foundry_journal.py
python tools/md_to_foundry_journal.py --no-backup   # second run for ID stability
python tools/reorder_guide_chapters.py              # dry-run / refuse write
python -m py_compile tools/md_to_gmbinder.py tools/md_to_foundry_journal.py tools/reorder_guide_chapters.py
```

## Validation highlights

- GMB `# 12 — Species Spotlight: Koorivar` once; `# 22 — Faces of the First Migration` with Speakers section
- App E row 22 = Faces
- Foundry: 30 pages; unique IDs; repeated generation identical `_id`s; ownership default 0
- Primary guide SHA-256 unchanged across reorder dry-run and generator work
- Companion manuscript not modified
- ChatGPT archive content PR scope not implemented
- No commit / push

## Related artifacts

- [`2026-08-26-foundry-id-investigation.md`](2026-08-26-foundry-id-investigation.md)
- [`2026-08-26-koorivar-dependency-review.md`](2026-08-26-koorivar-dependency-review.md)
- [`ai/plans/2026-08-26-campaign-decision-record.md`](../../ai/plans/2026-08-26-campaign-decision-record.md) (F-K-002)
