# Koorivar External Dependency Review (F-M-001)

**Status:** Operational review (not campaign canon)  
**Date:** 2026-08-26  
**Finding:** F-M-001  
**Authority:** Blocker & Generator Reliability Correction Plan implementation authorization

---

## Axes reviewed

### 1. Build portability

**Before:** `tools/md_to_gmbinder.py` hard-required an absolute OneDrive path under a specific Windows user profile.

**After:** Resolution order is:

1. `--koorivar PATH`
2. `KOORIVAR_SPECIES_PATH` environment variable
3. Repo-relative candidates (`external/sw5e-docs/species/Koorivar.md`, `vendor/sw5e-docs/species/Koorivar.md`)
4. Legacy absolute path **only if that file exists** (compatibility, not required default)

Generation fails loudly with nonzero exit status when no source is found.

### 2. Provenance / licensing / redistribution

- External file currently discovered at the legacy SW5e Docs path on the author’s machine.
- Repository evidence does **not** establish redistribution rights for vendoring that file into this repo.
- **Vendoring is not presumed and was not performed.**

### 3. Missing-dependency behavior

- Missing required species file → clear error, nonzero exit, no overwrite of a good binder with an incomplete book.
- `--dry-run` validates planned I/O without writing.
- Successful writes use a temp file + replace; optional timestamped `.bak-*` backup of prior OUT.

### 4. Guide vs generated GM Binder divergence

- Primary guide Ch 12 remains the campaign’s species spotlight chapter (hooks/budget retained from guide).
- GM Binder Ch 12 injects full SW5e species formatting/CSS from the external file.
- That divergence is **intentional for print layout**, not a silent lore fork, but it means GMB Ch 12 is not a pure guide mirror.
- App E / chapter placement must continue to list Ch 12 as Species Spotlight and Ch 22 as Faces.

## Recommendation

1. Keep external Koorivar outside the repo until Kakeman89 completes a licensing/redistribution decision.
2. Document `KOORIVAR_SPECIES_PATH` / `--koorivar` in README / tool help (done in this implementation wave).
3. Optional later: authorize vendoring under a clear license note — **separate authorization required**.

## Status recommendation for F-M-001

- Portability + missing-dependency fail-loud: **RESOLVED**
- Provenance / licensing / redistribution / vendoring: **NEEDS DECISION** (not resolved; not vendored)
