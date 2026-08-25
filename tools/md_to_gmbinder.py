#!/usr/bin/env python3
"""Build a paste-ready GM Binder source from the master campaign guide."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "dawn-of-the-jedaii-campaign-guide.md"
OUT = ROOT / "gmbinder" / "dawn-of-the-jedaii-gmbinder.md"
KOORIVAR = Path(
    r"C:\Users\ckauble\OneDrive - Riverside Bank of Dublin"
    r"\Documents\GitHub\SW5e Docs\species\Koorivar.md"
)

COVER = """# Dawn of the Je'daii

The player characters are not joining the Jedi Order. The Jedi do not exist yet.

They are among the first pilgrims called by a **Tho Yor**—an ancient pyramidal temple-ship. Across the campaign they explore the ship, survive Tython’s living Force storms, invent the philosophy of **Balance** between **Ashla** and **Bogan**, name the **Je'daii Order**, and seed the temples that will one day define it.

> **GM Campaign Guide** · **36,453 BBY / 0 TYA** · **Foundry VTT + SW5e** · Party starts at **level 9**

Paste this entire document into [GM Binder](https://www.gmbinder.com). The plain Markdown source of truth remains `dawn-of-the-jedaii-campaign-guide.md` (Foundry journal export).
"""

CH22_INTRO = """# 22 — Species Spotlight: Koorivar

Playable SW5e species for this campaign (and reusable elsewhere). Worksheet budget **23 points**.

## Era note (36,453 BBY)

At Tho Yor Pickup, the **lost Koorivar homeworld** still exists as their native land (the later lease/purchase of **Kooriva** is centuries ahead). Proto-corporate culture, horn-status hierarchies, and gesture-rich speech are already alive. A Koorivar PC’s approved homeland is typically **Lost Koorivar homeworld** (Ch 08 / Ch 21)—species is not required to match planet for other characters, but this spotlight is for playing a Koorivar.

**Force:** Koorivar are **not** innately Force-Sensitive. You still must satisfy Chapter 08 paths A–D (Forcecasting class, Force archetype, Force-Sensitive feat, etc.) to board the Tho Yor.
"""


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
    # Drop trailing blank-line padding before style; keep footnote
    return species, css


def extract_ch22_tail(body: str) -> str:
    """Keep Campaign hooks + Point budget from master Ch 22 body."""
    hooks = re.search(
        r"(?ms)^## Campaign hooks\n.*?(?=^## Point budget|^---|\Z)",
        body,
    )
    budget = re.search(r"(?ms)^## Point budget \(worksheet\)\n.*", body)
    chunks: list[str] = []
    if hooks:
        chunks.append(hooks.group(0).rstrip())
    if budget:
        # Strip trailing --- separators
        text = budget.group(0).rstrip()
        text = re.sub(r"\n---\s*$", "", text)
        chunks.append(text)
    return "\n\n".join(chunks) + ("\n" if chunks else "")


def build() -> None:
    master = MASTER.read_text(encoding="utf-8")
    chapters = split_h1_chapters(master)
    species_block, css = extract_koorivar_species_and_css(KOORIVAR)

    out_parts: list[str] = [COVER.rstrip() + "\n"]

    for title, body in chapters:
        out_parts.append("\n\\page\n\n")

        if title.startswith("22 —"):
            tail = extract_ch22_tail(body)
            chapter = (
                CH22_INTRO.rstrip()
                + "\n\n"
                + species_block.rstrip()
                + "\n\n"
                + tail.rstrip()
                + "\n"
            )
            out_parts.append(chapter)
            continue

        # Soften Foundry-only companion blurb for binder readers
        if title.startswith("00 —"):
            body = re.sub(
                r"(?ms)^## Companion Foundry journal\n.*?(?=^---|\Z)",
                "## Companion files\n\n"
                "Plain Markdown source of truth: `dawn-of-the-jedaii-campaign-guide.md`. "
                "Foundry VTT v13 journal: `foundry/dawn-of-the-jedaii.journal.json`. "
                "This file is the GM Binder print/PDF source—paste the whole document into GM Binder.\n\n",
                body,
                count=1,
            )

        out_parts.append(f"# {title}\n{body}")
        if not body.endswith("\n"):
            out_parts.append("\n")

    out_parts.append("\n\n")
    out_parts.append(css)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(out_parts), encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes, {len(chapters)} chapters + cover)")


if __name__ == "__main__":
    build()
