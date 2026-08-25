#!/usr/bin/env python3
"""Split dawn-of-the-jedaii-campaign-guide.md into a Foundry VTT v13 Journal Entry JSON.

Foundry import does not compile Markdown → HTML. Pages with only text.markdown
appear blank (especially under Monk's Enhanced Journal). This exporter writes
both markdown and pre-rendered text.content HTML.
"""

from __future__ import annotations

import json
import re
import secrets
import sys
from pathlib import Path

try:
    import markdown as md_lib
except ImportError:
    sys.exit(
        "Missing dependency: markdown\n"
        "Install with: pip install -r requirements.txt"
    )

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "dawn-of-the-jedaii-campaign-guide.md"
OUT = ROOT / "foundry" / "dawn-of-the-jedaii.journal.json"

MD_EXTENSIONS = [
    "markdown.extensions.tables",
    "markdown.extensions.fenced_code",
    "markdown.extensions.nl2br",
    "markdown.extensions.sane_lists",
]


def make_id(length: int = 16) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(secrets.choice(alphabet) for _ in range(length))


def split_chapters(text: str) -> list[tuple[str, str]]:
    lines = text.splitlines()
    chapters: list[tuple[str, str]] = []
    current_title: str | None = None
    current_body: list[str] = []

    def flush() -> None:
        nonlocal current_title, current_body
        if current_title is None:
            return
        body = "\n".join(current_body).strip() + "\n"
        chapters.append((current_title, body))
        current_title = None
        current_body = []

    for line in lines:
        if line.startswith("# "):
            flush()
            current_title = line[2:].strip()
            current_body = [line]
        elif current_title is not None:
            current_body.append(line)

    flush()
    return chapters


def page_name(title: str) -> str:
    # Prefer short names for Foundry sidebar
    title = re.sub(r"\s*\(Sessions[^)]*\)\s*", "", title).strip()
    return title


def strip_leading_h1(body: str) -> str:
    """Drop the chapter `# Title` line; sheet chrome already shows page.name."""
    lines = body.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    return "\n".join(lines).rstrip() + "\n"


def html_from_markdown(body: str) -> str:
    display_md = strip_leading_h1(body)
    return md_lib.markdown(display_md, extensions=MD_EXTENSIONS)


def build_journal(chapters: list[tuple[str, str]]) -> dict:
    pages = []
    for i, (title, body) in enumerate(chapters):
        pages.append(
            {
                "_id": make_id(),
                "name": page_name(title),
                "type": "text",
                "title": {"show": True, "level": 1},
                "image": {},
                "text": {
                    "format": 2,  # CONST.JOURNAL_ENTRY_PAGE_FORMATS.MARKDOWN
                    "markdown": body,
                    "content": html_from_markdown(body),
                },
                "video": {"controls": True, "volume": 0.5},
                "src": None,
                "system": {},
                "sort": i * 100000,
                "ownership": {"default": 0},
                "flags": {
                    "core": {
                        "sheetClass": "core.MarkdownJournalPageSheet"
                    }
                },
            }
        )

    return {
        "name": "Dawn of the Je'daii — GM Guide",
        "pages": pages,
        "ownership": {"default": 0},
        "flags": {},
    }


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Missing source: {SRC}")
    text = SRC.read_text(encoding="utf-8")
    chapters = split_chapters(text)
    if len(chapters) < 30:
        raise SystemExit(f"Expected at least 30 chapters/appendices, found {len(chapters)}")
    journal = build_journal(chapters)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(journal, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} with {len(chapters)} pages")


if __name__ == "__main__":
    main()
