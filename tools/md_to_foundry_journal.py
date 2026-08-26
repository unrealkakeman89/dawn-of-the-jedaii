#!/usr/bin/env python3
"""Split dawn-of-the-jedaii-campaign-guide.md into a Foundry VTT v13 Journal Entry JSON.

Foundry import does not compile Markdown → HTML. Pages with only text.markdown
appear blank (especially under Monk's Enhanced Journal). This exporter writes
both markdown and pre-rendered text.content HTML.

Page and journal `_id` values are deterministic hashes of stable semantic keys
so repeated generation with unchanged inputs yields the same IDs. Live Foundry
Import Data update-vs-duplicate behavior must still be confirmed manually in a
world (see reports/audits/2026-08-26-foundry-id-investigation.md).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime, timezone
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

ID_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
JOURNAL_ID_KEY = "journal:dawn-of-the-jedaii-gm-guide"


def make_deterministic_id(key: str, length: int = 16) -> str:
    """Foundry DocumentIdField: 16 alphanumeric characters."""
    digest = hashlib.sha256(f"dawn-of-the-jedaii:{key}".encode("utf-8")).digest()
    n = int.from_bytes(digest, "big")
    chars: list[str] = []
    for _ in range(length):
        chars.append(ID_ALPHABET[n % 62])
        n //= 62
    return "".join(chars)


def page_id_key(title: str) -> str:
    """Stable semantic key from chapter/appendix title (not sort index alone)."""
    slug = re.sub(r"\s+", " ", title.strip().lower())
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return f"page:{slug}"


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
    title = re.sub(r"\s*\(Sessions[^)]*\)\s*", "", title).strip()
    return title


def strip_leading_h1(body: str) -> str:
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
    seen_ids: dict[str, str] = {}

    journal_id = make_deterministic_id(JOURNAL_ID_KEY)
    seen_ids[journal_id] = JOURNAL_ID_KEY

    for i, (title, body) in enumerate(chapters):
        key = page_id_key(title)
        page_id = make_deterministic_id(key)
        if page_id in seen_ids:
            raise RuntimeError(
                f"ID collision: {page_id!r} for {key!r} and {seen_ids[page_id]!r}"
            )
        seen_ids[page_id] = key
        pages.append(
            {
                "_id": page_id,
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
                    },
                    "dawn-of-the-jedaii": {
                        "pageKey": key,
                    },
                },
            }
        )

    return {
        "_id": journal_id,
        "name": "Dawn of the Je'daii — GM Guide",
        "pages": pages,
        "ownership": {"default": 0},
        "flags": {
            "dawn-of-the-jedaii": {
                "journalKey": JOURNAL_ID_KEY,
                "idStrategy": "sha256-base62-16",
            }
        },
    }


def backup_output(path: Path) -> Path | None:
    if not path.exists():
        return None
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = path.with_name(f"{path.name}.bak-{stamp}")
    shutil.copy2(path, backup)
    return backup


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
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    print(f"Input guide:   {SRC}")
    print(f"Output journal:{OUT}")

    if not SRC.exists():
        print(f"Missing source: {SRC}", file=sys.stderr)
        return 1

    text = SRC.read_text(encoding="utf-8")
    chapters = split_chapters(text)
    if len(chapters) < 30:
        print(
            f"Expected at least 30 chapters/appendices, found {len(chapters)}",
            file=sys.stderr,
        )
        return 1

    try:
        journal = build_journal(chapters)
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return 1

    payload = json.dumps(journal, ensure_ascii=False, indent=2) + "\n"

    if args.dry_run:
        print(
            f"DRY-RUN OK: would write {len(chapters)} pages "
            f"({len(payload)} bytes) to {OUT} (no write performed)"
        )
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    backup = None if args.no_backup else backup_output(OUT)
    if backup:
        print(f"Backup:        {backup}")

    tmp = OUT.with_suffix(OUT.suffix + ".tmp")
    try:
        tmp.write_text(payload, encoding="utf-8")
        tmp.replace(OUT)
    except Exception:
        if tmp.exists():
            tmp.unlink(missing_ok=True)
        raise

    print(f"Wrote {OUT} with {len(chapters)} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
