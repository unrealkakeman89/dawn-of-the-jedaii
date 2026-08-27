#!/usr/bin/env python3
"""Generate Arc I pilot Foundry journal from integrated candidate (mixed hierarchy).

Reads ai/migration-workspace/arc-i-integrated-candidate.md and writes
foundry/arc-i-pilot.journal.json — never overwrites production journal.

Mixed hierarchy: Act overview page + one page per Session; Scenes as H2 in Session pages.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

try:
    import markdown as md_lib
except ImportError:
    sys.exit("Missing dependency: markdown\nInstall with: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "ai" / "migration-workspace" / "arc-i-integrated-candidate.md"
OUT = ROOT / "foundry" / "arc-i-pilot.journal.json"

MD_EXTENSIONS = [
    "markdown.extensions.tables",
    "markdown.extensions.fenced_code",
    "markdown.extensions.nl2br",
    "markdown.extensions.sane_lists",
]

ID_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
JOURNAL_ID_KEY = "journal:arc-i-pilot-integrated-guide"


def make_deterministic_id(key: str, length: int = 16) -> str:
    digest = hashlib.sha256(f"dawn-of-the-jedaii-pilot:{key}".encode("utf-8")).digest()
    n = int.from_bytes(digest, "big")
    return "".join(ID_ALPHABET[(n >> (i * 6)) % 62] for i in range(length))


def html_from_markdown(body: str) -> str:
    return md_lib.markdown(body, extensions=MD_EXTENSIONS)


def strip_operational_header(text: str) -> str:
    """Remove provisional HTML comment block at file start."""
    return re.sub(r"^<!--[\s\S]*?-->\s*", "", text, count=1)


def extract_act_overview(text: str) -> str:
    m = re.search(
        r"(# Arc I:[^\n]*\n[\s\S]*?)(?=^## Session 0\b)",
        text,
        re.MULTILINE,
    )
    return m.group(1).strip() + "\n" if m else "# Arc I Pilot\n"


def extract_session(text: str, session_num: int) -> str:
    stop = rf"(?=^## Session {session_num + 1}\b|^## Player-Facing Handouts|^## Central Reference|^# [^#]|\Z)"
    pattern = rf"^## Session {session_num}\b[\s\S]*?{stop}"
    m = re.search(pattern, text, re.MULTILINE)
    return m.group(0).strip() + "\n" if m else f"## Session {session_num}\n\n(TBD)\n"


def extract_player_handouts(text: str) -> str | None:
    m = re.search(r"^## Player-Facing Handouts \(Pilot\)[\s\S]*", text, re.MULTILINE)
    return m.group(0).strip() + "\n" if m else None


def build_page(name: str, key: str, body: str, sort: int, ownership: int = 0) -> dict:
    return {
        "_id": make_deterministic_id(key),
        "name": name,
        "type": "text",
        "title": {"show": True, "level": 1},
        "image": {},
        "text": {
            "format": 2,
            "markdown": body,
            "content": html_from_markdown(body),
        },
        "video": {"controls": True, "volume": 0.5},
        "src": None,
        "system": {},
        "sort": sort,
        "ownership": {"default": ownership},
        "flags": {
            "core": {"sheetClass": "core.MarkdownJournalPageSheet"},
            "dawn-of-the-jedaii": {"pageKey": key, "pilot": True},
        },
    }


def build_journal(text: str) -> dict:
    pages: list[dict] = []
    sort = 0

    act_body = extract_act_overview(text)
    pages.append(build_page("Arc I — Act Overview", "page:arc-i-act-overview", act_body, sort))
    sort += 100000

    for sn in range(0, 4):
        body = extract_session(text, sn)
        pages.append(
            build_page(
                f"Session {sn}",
                f"page:arc-i-session-{sn}",
                body,
                sort,
            )
        )
        sort += 100000

    handouts = extract_player_handouts(text)
    if handouts:
        pages.append(
            build_page(
                "Player Handouts (Pilot)",
                "page:arc-i-player-handouts",
                handouts,
                sort,
                ownership=2,
            )
        )

    return {
        "_id": make_deterministic_id(JOURNAL_ID_KEY),
        "name": "Arc I Pilot — Integrated GM Guide (PROVISIONAL)",
        "pages": pages,
        "ownership": {"default": 0},
        "flags": {
            "dawn-of-the-jedaii": {
                "journalKey": JOURNAL_ID_KEY,
                "idStrategy": "sha256-base62-16",
                "pilot": True,
                "nonAuthoritative": True,
            }
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not SRC.exists():
        print(f"Missing source: {SRC}", file=sys.stderr)
        return 1

    text = strip_operational_header(SRC.read_text(encoding="utf-8"))
    journal = build_journal(text)
    payload = json.dumps(journal, ensure_ascii=False, indent=2) + "\n"

    if args.dry_run:
        print(f"DRY-RUN OK: {len(journal['pages'])} pages, {len(payload)} bytes -> {OUT}")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(payload, encoding="utf-8")
    print(f"Wrote {OUT} with {len(journal['pages'])} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
