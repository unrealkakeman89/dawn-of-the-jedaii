#!/usr/bin/env python3
"""HISTORICAL one-shot chapter reorder for dawn-of-the-jedaii-campaign-guide.md.

DANGER: This script rewrites the PRIMARY campaign guide in place using a fixed
old→new chapter map from a prior Living Force restructure. Re-running it against
the current guide will corrupt chapter numbering and citations.

Default behavior is dry-run / refuse-to-write. An explicit dual confirmation is
required to write. Prefer not to run this at all unless recovering a pre-reorder
snapshot under Kakeman89 authorization.

See F-O-002.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "dawn-of-the-jedaii-campaign-guide.md"

# old chapter number (int) -> new chapter number (int)
OLD_TO_NEW = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 10,   # SW5e rules
    9: 14,   # Arc overview
    10: 15,  # Arc I
    11: 16,  # Arc II
    12: 17,  # Arc III
    13: 18,  # Arc IV
    14: 19,  # Arc V
    15: 20,  # Arc VI
    16: 21,  # Scene craft
    17: 11,  # Boons
    18: 8,   # Kwa Gate
    19: 22,  # NPCs
    20: 23,  # Maps
    21: 24,  # Timelines
    22: 12,  # Koorivar
    23: 9,   # Calendar
    24: 13,  # Checklists
}

# Final order of old chapter numbers (appendices keep letter keys)
FINAL_ORDER_OLD = [
    0, 1, 2, 3, 4, 5, 6, 7,
    18, 23,  # Kwa Gate, Calendar
    8, 17, 22, 24,  # Rules, Boons, Species, Checklists
    9, 10, 11, 12, 13, 14, 15,  # Overview + Arcs
    16, 19, 20,  # Scene, NPCs, Maps
    21,  # Timelines
    "A", "B", "C", "D", "E",
]

NEW_TOC = """## What this book contains

| Part | Chapters | Use |
|------|----------|-----|
| **I — Setting & Mysteries** | 01–09 | Era, Tython catalog, peoples, Tho Yor, gazetteer, factions, Je'daii founding, Kwa Gate, calendar |
| **II — Campaign Rules & Session 0** | 10–13 | SW5e chargen, boons, species spotlight, GM checklists |
| **III — Adventure Path** | 14–20 | Arc overview + Arcs I–VI (Episode 1 = Arc I–II through disembark) |
| **IV — Table Tools** | 21–23 | Scene Cards, NPC cast, map briefs |
| **V — Continuity** | 24 | GM & player timelines through Tho Yor Pickup |
| **Appendices** | A–E | NPC index, tables, player primer, canon notes, Foundry page map |
"""

NEW_SPOILER = """## Spoiler & handout policy

- **GM-only:** Chapters 04 (secrets), 06–09 (faction/Order/Gate/calendar defaults), 13–23 (checklists, arcs, tools), Chapter 24 GM Master Timeline, Appendices A–B, D.
- **Safe for players:** Appendix C (Player Primer + Player Timeline); Chapter 10 Character Creation Requirements (planet list + Force paths); Chapter 24 Player Timeline Handout; Chapter 11 Session 0 boon *visions* only (not GM effects); Chapter 09 calendar **workshop** once landed (not the default Twin Measure until the table adopts or skips inventing). Optionally share high-level Ch 01–02 flavor after Session 1.
- Do not show players the nine temple end-state list until the campaign earns those discoveries.
"""


def split_document(text: str) -> tuple[str, list[tuple[str, str, str]]]:
    """Return (preamble_unused, [(key, title_rest, body_including_h1)]).

    key is '0'..'24' or 'A'..'E'. First H1 starts chapters; nothing before first H1.
    """
    parts = re.split(r"(?m)^(#{1} )", text)
    # parts[0] may be empty; then pairs of (heading_marker, rest)
    chapters: list[tuple[str, str, str]] = []
    i = 1
    while i < len(parts):
        marker = parts[i]  # "# "
        rest = parts[i + 1]
        i += 2
        first_line, _, body_after = rest.partition("\n")
        title = first_line.strip()
        full = marker + rest
        if title.startswith("Appendix "):
            key = title.split()[1]  # A — ...
            key = key.rstrip("—").strip() if False else title.split()[1][0]
            # "Appendix A — NPC Index" -> A
            m = re.match(r"Appendix ([A-E])\b", title)
            key = m.group(1) if m else title
        else:
            m = re.match(r"(\d+)\s*—", title)
            if not m:
                raise SystemExit(f"Cannot parse chapter title: {title!r}")
            key = str(int(m.group(1)))  # normalize 00 -> 0 for dict? keep as int string without leading zero issues
            key = str(int(m.group(1)))
        chapters.append((key, title, full))
    return "", chapters


def renumber_h1(full: str, new_num: int | str) -> str:
    lines = full.splitlines(keepends=True)
    if not lines:
        return full
    line = lines[0]
    if isinstance(new_num, int):
        # Keep zero-padded for 0-9 style as NN
        pad = f"{new_num:02d}"
        lines[0] = re.sub(r"^# \d+\s*—", f"# {pad} —", line, count=1)
    else:
        # Appendix — leave title as-is
        pass
    return "".join(lines)


def placeholder_citations(text: str) -> str:
    """Replace chapter citations with placeholders to avoid collision."""

    def repl_chapter_word(m: re.Match) -> str:
        n = int(m.group(1))
        return f"Chapter «{n}»"

    def repl_ch(m: re.Match) -> str:
        n = int(m.group(1))
        return f"Ch «{n}»"

    def repl_chapters_range(m: re.Match) -> str:
        a, b = int(m.group(1)), int(m.group(2))
        return f"Chapters «{a}»–«{b}»"

    def repl_ch_range(m: re.Match) -> str:
        a, b = int(m.group(1)), int(m.group(2))
        return f"Ch «{a}»–«{b}»"

    # Ranges first
    text = re.sub(r"Chapters?\s+(\d+)\s*[–-]\s*(\d+)", repl_chapters_range, text)
    text = re.sub(r"\bCh\s+(\d+)\s*[–-]\s*(\d+)", repl_ch_range, text)
    text = re.sub(r"\bChapter\s+(\d+)\b", repl_chapter_word, text)
    text = re.sub(r"\bCh\s+(\d+)\b", repl_ch, text)
    # H1 22 style in App E
    text = re.sub(r"`H1 (\d+)", r"`H1 «\1»", text)
    return text


def apply_placeholders(text: str) -> str:
    def sub_one(m: re.Match) -> str:
        n = int(m.group(1))
        new = OLD_TO_NEW.get(n, n)
        return f"«{new}»"

    # Replace «old» with «new» then strip brackets in a second pass
    text = re.sub(r"«(\d+)»", sub_one, text)

    def format_num(n: int) -> str:
        return f"{n:02d}" if n < 100 else str(n)

    # Chapter «10» -> Chapter 10 (use unpadded for prose, or padded? Guide uses both "Chapter 08" and "Ch 08")
    # Existing style often uses unpadded or two-digit. Prefer two-digit for consistency with H1s when < 10.
    def expand_chapter(m: re.Match) -> str:
        n = int(m.group(1))
        return f"Chapter {n:02d}"

    def expand_ch(m: re.Match) -> str:
        n = int(m.group(1))
        return f"Ch {n:02d}"

    def expand_chapters(m: re.Match) -> str:
        a, b = int(m.group(1)), int(m.group(2))
        return f"Chapters {a:02d}–{b:02d}"

    def expand_ch_range(m: re.Match) -> str:
        a, b = int(m.group(1)), int(m.group(2))
        return f"Ch {a:02d}–{b:02d}"

    text = re.sub(r"Chapters «(\d+)»–«(\d+)»", expand_chapters, text)
    text = re.sub(r"Ch «(\d+)»–«(\d+)»", expand_ch_range, text)
    text = re.sub(r"Chapter «(\d+)»", expand_chapter, text)
    text = re.sub(r"Ch «(\d+)»", expand_ch, text)
    text = re.sub(r"`H1 «(\d+)»", lambda m: f"`H1 {int(m.group(1)):02d}", text)
    return text


def fix_arc_i_session0(body: str) -> str:
    """Replace Session 0 procedure block inside Arc I with pointer."""
    old = """## Session 0 (before Arc I)

Run the full **Chapter 24 Session 0 GM Checklist**. At minimum: boon visions from **Chapter 17** (name + look + vision only); assign one boon per PC from the pool of six; deliver the **money is useless** speech (craft or NPC favor only).

Episode 1 (**The Calling**) to-do list also lives in **Chapter 24**—use it from Session 1 through disembark.
"""
    # After citation remap this will have new numbers - run AFTER apply_placeholders
    # Better: match flexibly
    pattern = r"(?ms)^## Session 0 \(before Arc I\)\n\n.*?(?=\n## Session 1)"
    repl = (
        "## Session 0 (before Arc I)\n\n"
        "Session 0 is **not** part of Arc I play. Complete **Chapters 11–13** first "
        "(boons, species if needed, Session 0 checklist). "
        "Episode 1 (**The Calling**) to-do list is in **Chapter 13**—use it from Session 1 through disembark.\n\n"
    )
    new_body, n = re.subn(pattern, repl, body, count=1)
    if n != 1:
        print(f"WARNING: Session 0 block replace count={n}")
    return new_body


def add_episode1_line_to_overview(body: str) -> str:
    """Insert Episode 1 line after Arc map section header content."""
    needle = "## Arc map\n"
    if needle not in body:
        print("WARNING: Arc map not found")
        return body
    if "Episode 1 — The Calling" in body:
        return body
    insert = (
        "## Arc map\n\n"
        "**Episode 1 — The Calling** = Arc I + Arc II through disembark (Sessions 1–5). "
        "Use the Chapter 13 Episode 1 checklist while running it.\n"
    )
    # Replace only the header line to add paragraph after table? Add after ## Arc map\n
    return body.replace(needle, insert, 1)


def rewrite_ch00(body: str) -> str:
    body = re.sub(
        r"(?ms)^## What this book contains\n\n\| Part \|.*?\n\n(?=## )",
        NEW_TOC + "\n",
        body,
        count=1,
    )
    body = re.sub(
        r"(?ms)^## Spoiler & handout policy\n\n.*?(?=\n## )",
        NEW_SPOILER + "\n",
        body,
        count=1,
    )
    # Cold open pointer
    body = re.sub(
        r"See \*\*Chapter [^*]+\*\* for the full Arc I rundown.*?\.",
        "See **Chapter 15** for Arc I, **Chapter 16** for landing, **Chapter 13** for Session 0 / Episode 1 GM checklists, "
        "**Chapter 04** for ship zones, **Chapter 21** for Scene Cards, and **Chapter 11** for Session 0 boons.",
        body,
        count=1,
    )
    return body


def build_appendix_e(chapters_meta: list[tuple[int | str, str]]) -> str:
    rows = []
    sort_i = 0
    for key, title in chapters_meta:
        if isinstance(key, int):
            name = title  # already "NN — Name"
            h1 = f"`H1 {key:02d}"
            # short tag from title
            short = title.split("—", 1)[-1].strip().split("(")[0].strip()
            rows.append(f"| {sort_i} | {name} | `H1 {key:02d} {short.split()[0]}` |")
        else:
            rows.append(f"| {sort_i} | {title} | `H1 Appendix {key}` |")
        sort_i += 1
    table = "\n".join(rows)
    return f"""# Appendix E — Foundry Journal Page Map

Journal Entry name: **Dawn of the Je'daii — GM Guide**

| Sort | Page name | Source H1 |
|------|-----------|-----------|
{table}

Source headings are the matching `#` titles in the master Markdown (same names as the Page name column).

Regenerate the JSON anytime with:

`python tools/md_to_foundry_journal.py`

See `foundry/README.md` for import steps.
"""


def main() -> tuple[str, list[str]]:
    text = SRC.read_text(encoding="utf-8")
    _, chapters = split_document(text)
    by_key: dict[str, tuple[str, str]] = {k: (t, f) for k, t, f in chapters}

    missing = [k for k in FINAL_ORDER_OLD if str(k) not in by_key and k not in by_key]
    # keys are strings "0".."24" and "A".."E"
    ordered_keys = [str(k) if isinstance(k, int) else k for k in FINAL_ORDER_OLD]
    for k in ordered_keys:
        if k not in by_key:
            raise SystemExit(f"Missing chapter key {k!r}. Have: {sorted(by_key)}")

    out_parts: list[str] = []
    meta: list[tuple[int | str, str]] = []

    for old_key in ordered_keys:
        title, full = by_key[old_key]
        if old_key.isdigit():
            old_n = int(old_key)
            new_n = OLD_TO_NEW[old_n]
            full = renumber_h1(full, new_n)
            # refresh title from first line
            title = full.split("\n", 1)[0][2:].strip()
            meta.append((new_n, title))
        else:
            meta.append((old_key, title))

        # Strip trailing horizontal rules; we re-add separators
        full = re.sub(r"\n---\s*$", "\n", full.rstrip() + "\n")

        # Placeholder citation remap inside this chapter
        full = placeholder_citations(full)
        full = apply_placeholders(full)

        if old_key == "0":
            full = rewrite_ch00(full)
        if old_key == "10":  # old Arc I -> new 15
            full = fix_arc_i_session0(full)
        if old_key == "9":  # old arc overview -> new 14
            full = add_episode1_line_to_overview(full)

        out_parts.append(full.rstrip() + "\n\n---\n\n")

    # Replace Appendix E with regenerated map
    final = "".join(out_parts)
    final = re.sub(
        r"(?ms)^# Appendix E — Foundry Journal Page Map\n.*",
        build_appendix_e(meta).rstrip() + "\n",
        final,
        count=1,
    )

    # Trailing --- cleanup: remove --- before Appendix E end
    final = re.sub(r"\n---\n\n(# Appendix E)", r"\n\n\1", final)
    # Remove final --- after last appendix if present
    final = re.sub(r"\n---\n\s*$", "\n", final)

    return final, ordered_keys


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "HISTORICAL/DANGEROUS: one-shot Living Force chapter reorder. "
            "Defaults to dry-run. Refuses to write without dual confirmation flags."
        )
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Plan only (default). Does not write the primary guide.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Permit writing the primary guide (still requires confirmation flag).",
    )
    parser.add_argument(
        "--i-understand-this-rewrites-the-primary-guide",
        action="store_true",
        help="Required confirmation that this is intentional destructive rewrite.",
    )
    return parser.parse_args(argv)


def cli(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    print(
        "WARNING: reorder_guide_chapters.py is historical migration tooling.\n"
        f"Target primary guide: {SRC}\n"
        "Re-running against the current guide will corrupt numbering/citations."
    )
    if not SRC.exists():
        print(f"Missing guide: {SRC}", file=sys.stderr)
        return 1

    try:
        final, ordered_keys = main()
    except SystemExit as exc:
        print(exc, file=sys.stderr)
        return 1

    write_requested = bool(
        args.write and args.i_understand_this_rewrites_the_primary_guide
    )
    if not write_requested:
        print(
            f"DRY-RUN / REFUSED WRITE: would rewrite {SRC} "
            f"({len(ordered_keys)} top-level sections, {len(final)} bytes).\n"
            "No write performed. To write (NOT recommended): "
            "--write --i-understand-this-rewrites-the-primary-guide"
        )
        return 0

    SRC.write_text(final, encoding="utf-8")
    print(f"Wrote {SRC} with {len(ordered_keys)} top-level sections")
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
