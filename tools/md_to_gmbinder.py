#!/usr/bin/env python3
"""Build a paste-ready GM Binder source from the master campaign guide.

Injects the external SW5e Koorivar species block into the Species Spotlight
chapter (guide Ch 12). Chapter 22 Faces of the First Migration passes through
unchanged from the primary guide.

Internal page breaks are driven by tools/gmbinder_pagination.json (generator-
owned). Do not put GM Binder page-break directives in the primary campaign guide.
Regenerate with this tool; do not hand-edit gmbinder output as the fix path.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from gmbinder_pagination_io import (  # noqa: E402
    PaginationConfigError,
    breaks_for_generator,
    load_pagination_file,
)
from gmbinder_semantic import inject_trace_markers  # noqa: E402

MASTER = ROOT / "dawn-of-the-jedaii-campaign-guide.md"
OUT = ROOT / "gmbinder" / "dawn-of-the-jedaii-gmbinder.md"
PAGINATION_CONFIG = ROOT / "tools" / "gmbinder_pagination.json"

# Compatibility only — not the required default. Prefer CLI / env / repo-relative.
LEGACY_KOORIVAR = Path(
    r"C:\Users\ckauble\OneDrive - Riverside Bank of Dublin"
    r"\Documents\GitHub\SW5e Docs\species\Koorivar.md"
)
REPO_KOORIVAR_CANDIDATES = (
    ROOT / "external" / "sw5e-docs" / "species" / "Koorivar.md",
    ROOT / "vendor" / "sw5e-docs" / "species" / "Koorivar.md",
)

COVER = """# Dawn of the Je'daii

The player characters are not joining the Jedi Order. The Jedi do not exist yet.

They are among the first pilgrims called by a **Tho Yor**—an ancient pyramidal temple-ship. Across the campaign they explore the ship, survive Tython’s living Force storms, invent the philosophy of **Balance** between **Ashla** and **Bogan**, name the **Je'daii Order**, and seed the temples that will one day define it.

> **GM Campaign Guide** · **36,453 BBY / 0 TYA** · **Foundry VTT + SW5e** · Party starts at **level 9**

Paste this entire document into [GM Binder](https://www.gmbinder.com). The plain Markdown source of truth remains `dawn-of-the-jedaii-campaign-guide.md` (Foundry journal export).
"""

SPECIES_INTRO = """# 12 — Species Spotlight: Koorivar

Playable SW5e species for this campaign (and reusable elsewhere). Worksheet budget **23 points**.

## Era note (36,453 BBY)

At Tho Yor Pickup, the **lost Koorivar homeworld** still exists as their native land (the later lease/purchase of **Kooriva** is centuries ahead). Proto-corporate culture, horn-status hierarchies, and gesture-rich speech are already alive. A Koorivar PC’s approved homeland is typically **Lost Koorivar homeworld** (Ch 10)—species is not required to match planet for other characters, but this spotlight is for playing a Koorivar.

**Force:** Koorivar are **not** innately Force-Sensitive. You still must satisfy Chapter 10 paths A–D (Forcecasting class, Force archetype, Force-Sensitive feat, etc.) to board the Tho Yor.
"""

SPECIES_CHAPTER_RE = re.compile(
    r"^12\s+[—\-–]\s+Species Spotlight:\s*Koorivar\b",
    re.IGNORECASE,
)
INTRO_CHAPTER_RE = re.compile(r"^00\s+[—\-–]\s+")

BREAK_TOKENS = {
    "pagebreak": "\\pagebreak",
    "pagebreakNum": "\\pagebreakNum",
}


class PaginationError(PaginationConfigError):
    """Configured internal page break could not be applied safely."""


def split_h1_chapters(text: str) -> list[tuple[str, str]]:
    """Return list of (heading_line_without_hash, body) for each top-level # chapter."""
    parts = re.split(r"(?m)^# ", text)
    chapters: list[tuple[str, str]] = []
    for part in parts:
        part = part.strip("\n")
        if not part.strip():
            continue
        lines = part.split("\n", 1)
        title = lines[0].strip()
        body = lines[1] if len(lines) > 1 else ""
        chapters.append((title, body.rstrip() + "\n"))
    return chapters


def extract_koorivar_species_and_css(path: Path) -> tuple[str, str]:
    raw = path.read_text(encoding="utf-8")
    style_match = re.search(r"(?s)(<style>.*</style>\s*)$", raw)
    if not style_match:
        raise SystemExit(f"No <style> block found in {path}")
    css = style_match.group(1).strip() + "\n"
    species = raw[: style_match.start()].rstrip() + "\n"
    return species, css


def extract_species_tail(body: str) -> str:
    """Keep Campaign hooks + Point budget from the master species chapter body."""
    hooks = re.search(
        r"(?ms)^## Campaign hooks\n.*?(?=^## Point budget|^---|\Z)",
        body,
    )
    budget = re.search(r"(?ms)^## Point budget \(worksheet\)\n.*", body)
    chunks: list[str] = []
    if hooks:
        chunks.append(hooks.group(0).rstrip())
    if budget:
        text = budget.group(0).rstrip()
        text = re.sub(r"\n---\s*$", "", text)
        chunks.append(text)
    return "\n\n".join(chunks) + ("\n" if chunks else "")


def resolve_koorivar_path(cli_path: str | None) -> Path:
    """Resolve Koorivar.md without requiring a machine-specific absolute default.

    Order: --koorivar → KOORIVAR_SPECIES_PATH env → repo-relative candidates →
    legacy absolute path if it exists (compatibility only).
    """
    if cli_path:
        path = Path(cli_path).expanduser()
        if not path.is_absolute():
            path = (Path.cwd() / path).resolve()
        return path

    env = os.environ.get("KOORIVAR_SPECIES_PATH", "").strip()
    if env:
        path = Path(env).expanduser()
        if not path.is_absolute():
            path = (ROOT / path).resolve()
        return path

    for candidate in REPO_KOORIVAR_CANDIDATES:
        if candidate.is_file():
            return candidate

    if LEGACY_KOORIVAR.is_file():
        return LEGACY_KOORIVAR

    searched = [
        "--koorivar PATH",
        "env KOORIVAR_SPECIES_PATH",
        *[str(p) for p in REPO_KOORIVAR_CANDIDATES],
        f"legacy path if present: {LEGACY_KOORIVAR}",
    ]
    raise FileNotFoundError(
        "Missing required Koorivar species source.\n"
        "Provide an existing Koorivar.md via --koorivar or KOORIVAR_SPECIES_PATH.\n"
        "Vendoring into the repo is not assumed (see F-M-001 review).\n"
        "Searched:\n  - " + "\n  - ".join(searched)
    )


def backup_output(path: Path) -> Path | None:
    if not path.exists():
        return None
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = path.with_name(f"{path.name}.bak-{stamp}")
    shutil.copy2(path, backup)
    return backup


def load_pagination_config(path: Path | None = None) -> list[dict[str, Any]]:
    """Load internal page-break configuration. Empty list if file is absent."""
    cfg_path = path or PAGINATION_CONFIG
    if not cfg_path.is_file():
        return []
    try:
        data = load_pagination_file(cfg_path)
    except PaginationConfigError as exc:
        raise PaginationError(str(exc)) from exc
    return breaks_for_generator(data)


def apply_internal_breaks(
    chapter_title: str,
    body: str,
    breaks: list[dict[str, Any]],
) -> tuple[str, list[dict[str, Any]]]:
    """Insert configured page breaks before exact heading lines in this chapter.

    Matching is exact against a full markdown heading line within this chapter
    body only (no cross-chapter substring matching).
    """
    chapter_breaks = [b for b in breaks if b["chapter"] == chapter_title]
    if not chapter_breaks:
        return body, []

    lines = body.splitlines(keepends=True)
    heading_index: dict[str, list[int]] = {}
    for idx, line in enumerate(lines):
        stripped = line.rstrip("\r\n")
        if stripped.startswith("#"):
            heading_index.setdefault(stripped, []).append(idx)

    insert_at: dict[int, list[dict[str, Any]]] = {}
    applied: list[dict[str, Any]] = []
    for entry in chapter_breaks:
        heading = entry["before_heading"]
        matches = heading_index.get(heading, [])
        if not matches:
            raise PaginationError(
                f"Pagination break {entry['id']!r}: heading {heading!r} not found "
                f"in chapter {chapter_title!r}"
            )
        if len(matches) > 1:
            raise PaginationError(
                f"Pagination break {entry['id']!r}: heading {heading!r} matches "
                f"{len(matches)} times in chapter {chapter_title!r}"
            )
        line_idx = matches[0]
        insert_at.setdefault(line_idx, []).append(entry)
        applied.append(entry)

    out_lines: list[str] = []
    for idx, line in enumerate(lines):
        if idx in insert_at:
            for entry in insert_at[idx]:
                token = BREAK_TOKENS[entry["break"]]
                if out_lines and out_lines[-1].strip():
                    out_lines.append("\n")
                out_lines.append(f"{token}\n\n")
        out_lines.append(line)
    return "".join(out_lines), applied


def count_legacy_page_directives(text: str) -> int:
    """Count standalone legacy \\page lines (not pagebreak / pagebreakNum)."""
    return len(re.findall(r"(?m)^\\page\s*$", text))


def build_document(
    koorivar: Path,
    pagination_breaks: list[dict[str, Any]] | None = None,
    *,
    inject_trace_markers_flag: bool = True,
) -> tuple[str, list[dict[str, Any]]]:
    """Build GM Binder Markdown and return (text, applied internal breaks)."""
    if not MASTER.is_file():
        raise FileNotFoundError(f"Missing master guide: {MASTER}")
    if not koorivar.is_file():
        raise FileNotFoundError(f"Missing Koorivar species file: {koorivar}")

    if pagination_breaks is None:
        pagination_breaks = load_pagination_config()

    master = MASTER.read_text(encoding="utf-8")
    chapters = split_h1_chapters(master)
    species_block, css = extract_koorivar_species_and_css(koorivar)

    chapter_titles = {title for title, _ in chapters}
    for entry in pagination_breaks:
        if entry["chapter"] not in chapter_titles:
            raise PaginationError(
                f"Pagination break {entry['id']!r}: chapter {entry['chapter']!r} "
                "not found in master guide"
            )

    out_parts: list[str] = [COVER.rstrip() + "\n"]
    injected = 0
    applied_breaks: list[dict[str, Any]] = []

    for title, body in chapters:
        # Chapter-boundary break (project standard: \pagebreak, not legacy \page)
        out_parts.append("\n\\pagebreak\n\n")

        if SPECIES_CHAPTER_RE.match(title):
            tail = extract_species_tail(body)
            intro_lines = SPECIES_INTRO.splitlines()
            h1 = intro_lines[0]
            intro_body = "\n".join(intro_lines[1:]).lstrip("\n")
            species_body = (
                "\n"
                + "\n\n".join(
                    part
                    for part in (
                        intro_body,
                        species_block.rstrip(),
                        tail.rstrip(),
                    )
                    if part
                )
                + "\n"
            )
            if inject_trace_markers_flag:
                species_body = inject_trace_markers(title, species_body)
            species_body, applied = apply_internal_breaks(
                title, species_body, pagination_breaks
            )
            applied_breaks.extend(applied)
            out_parts.append(h1 + "\n" + species_body)
            injected += 1
            continue

        if INTRO_CHAPTER_RE.match(title):
            body = re.sub(
                r"(?ms)^## Companion Foundry journal\n.*?(?=^---|\Z)",
                "## Companion files\n\n"
                "Plain Markdown source of truth: `dawn-of-the-jedaii-campaign-guide.md`. "
                "Foundry VTT v13 journal: `foundry/dawn-of-the-jedaii.journal.json`. "
                "This file is the GM Binder print/PDF source—paste the whole document into GM Binder.\n\n",
                body,
                count=1,
            )

        if inject_trace_markers_flag:
            body = inject_trace_markers(title, body)

        body, applied = apply_internal_breaks(title, body, pagination_breaks)
        applied_breaks.extend(applied)
        out_parts.append(f"# {title}\n{body}")
        if not body.endswith("\n"):
            out_parts.append("\n")

    if injected != 1:
        raise RuntimeError(
            f"Expected exactly one Species Spotlight: Koorivar chapter to inject into, found {injected}"
        )

    applied_ids = [b["id"] for b in applied_breaks]
    expected_ids = [b["id"] for b in pagination_breaks]
    if sorted(applied_ids) != sorted(expected_ids):
        missing = sorted(set(expected_ids) - set(applied_ids))
        extra = sorted(set(applied_ids) - set(expected_ids))
        raise PaginationError(
            f"Pagination application mismatch. missing={missing} extra={extra}"
        )
    if len(applied_ids) != len(set(applied_ids)):
        raise PaginationError("Pagination inserted a duplicate configured break")

    out_parts.append("\n\n")
    out_parts.append(css)
    text = "".join(out_parts)
    if count_legacy_page_directives(text):
        raise RuntimeError("Generated output contains legacy standalone \\page directives")
    return text, applied_breaks


def report_breaks(applied: list[dict[str, Any]], *, dry_run: bool) -> None:
    prefix = "DRY-RUN internal breaks" if dry_run else "Internal breaks applied"
    print(f"{prefix}: {len(applied)}")
    for entry in applied:
        print(
            f"  - {entry['id']}: {entry['break']} before {entry['before_heading']!r} "
            f"in {entry['chapter']!r}"
        )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and print planned I/O; do not write OUT",
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Skip timestamped backup of existing OUT before overwrite",
    )
    parser.add_argument(
        "--koorivar",
        metavar="PATH",
        help="Path to Koorivar.md (overrides env and discovery)",
    )
    parser.add_argument(
        "--pagination",
        metavar="PATH",
        help="Path to gmbinder_pagination.json (default: tools/gmbinder_pagination.json)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        koorivar = resolve_koorivar_path(args.koorivar)
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 1

    pagination_path = Path(args.pagination) if args.pagination else PAGINATION_CONFIG
    if args.pagination and not pagination_path.is_absolute():
        pagination_path = (Path.cwd() / pagination_path).resolve()

    print(f"Input guide:    {MASTER}")
    print(f"Input species:  {koorivar}")
    print(f"Pagination:     {pagination_path}")
    print(f"Output binder:  {OUT}")

    try:
        breaks = load_pagination_config(pagination_path)
        text, applied = build_document(koorivar, breaks)
    except (
        FileNotFoundError,
        RuntimeError,
        OSError,
        PaginationError,
        json.JSONDecodeError,
    ) as exc:
        print(exc, file=sys.stderr)
        return 1

    report_breaks(applied, dry_run=args.dry_run)
    chapter_breaks = len(re.findall(r"(?m)^\\pagebreak\s*$", text))
    print(f"Total \\pagebreak lines: {chapter_breaks}")
    print(f"Legacy \\page lines: {count_legacy_page_directives(text)}")
    print(f"\\pagebreakNum lines: {len(re.findall(r'(?m)^\\\\pagebreakNum\\b', text))}")

    if args.dry_run:
        print(f"DRY-RUN OK: would write {len(text)} bytes to {OUT} (no write performed)")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    backup = None if args.no_backup else backup_output(OUT)
    if backup:
        print(f"Backup:         {backup}")

    tmp = OUT.with_suffix(OUT.suffix + ".tmp")
    try:
        tmp.write_text(text, encoding="utf-8")
        tmp.replace(OUT)
    except Exception:
        if tmp.exists():
            tmp.unlink(missing_ok=True)
        raise

    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
