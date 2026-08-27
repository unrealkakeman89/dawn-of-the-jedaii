#!/usr/bin/env python3
"""Generate Arc III pilot Foundry journal from integrated candidate (mixed hierarchy).

Reads ai/migration-workspace/arc-iii-integrated-candidate.md and writes
foundry/arc-iii-pilot.journal.json — never overwrites production journal.
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
SRC = ROOT / "ai" / "migration-workspace" / "arc-iii-integrated-candidate.md"
OUT = ROOT / "foundry" / "arc-iii-pilot.journal.json"

MD_EXTENSIONS = [
    "markdown.extensions.tables",
    "markdown.extensions.fenced_code",
    "markdown.extensions.nl2br",
    "markdown.extensions.sane_lists",
]

ID_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
JOURNAL_ID_KEY = "journal:arc-iii-pilot-integrated-guide"


def make_deterministic_id(key: str, length: int = 16) -> str:
    digest = hashlib.sha256(f"dawn-of-the-jedaii-pilot:{key}".encode("utf-8")).digest()
    n = int.from_bytes(digest, "big")
    return "".join(ID_ALPHABET[(n >> (i * 6)) % 62] for i in range(length))


def html_from_markdown(body: str) -> str:
    return md_lib.markdown(body, extensions=MD_EXTENSIONS)


def strip_operational_headers(text: str) -> str:
    return re.sub(r"^(<!--[\s\S]*?-->\s*)+", "", text)


def extract_named_section(text: str, heading: str, stops: list[str]) -> str | None:
    # Match full heading line (Session titles continue after the colon).
    stop = "|".join(re.escape(s) for s in stops)
    pattern = rf"^{re.escape(heading)}[^\n]*\n[\s\S]*?(?=^(?:{stop})|\Z)"
    m = re.search(pattern, text, re.MULTILINE)
    return m.group(0).strip() + "\n" if m else None


def extract_act_overview(text: str) -> str:
    m = re.search(
        r"(# Arc III:[^\n]*\n[\s\S]*?)(?=^## Session 7:)",
        text,
        re.MULTILINE,
    )
    return m.group(1).strip() + "\n" if m else "# Arc III Pilot\n"

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
            "dawn-of-the-jedaii": {"pageKey": key, "pilot": True, "arc": "III"},
        },
    }


def build_journal(text: str) -> dict:
    pages: list[dict] = []
    sort = 0

    pages.append(
        build_page(
            "Arc III Overview",
            "page:arc-iii-act-overview",
            extract_act_overview(text),
            sort,
        )
    )
    sort += 100000

    for sn, heading, stops in [
        (7, "## Session 7:", ["## Session 8:"]),
        (8, "## Session 8:", ["## Session 9:"]),
    ]:
        body = extract_named_section(text, heading, stops) or f"{heading}\n\n(TBD)\n"
        pages.append(build_page(f"Session {sn}", f"page:arc-iii-session-{sn}", body, sort))
        sort += 100000

    s9_main = extract_named_section(
        text, "## Session 9:", ["## Alternate Session 9:", "## Session 10:"]
    )
    s9_alt = extract_named_section(text, "## Alternate Session 9:", ["## Session 10:"])
    s9_body = (s9_main or "## Session 9\n") + "\n" + (s9_alt or "")
    pages.append(build_page("Session 9", "page:arc-iii-session-9", s9_body, sort))
    sort += 100000

    for sn, heading, stops in [
        (10, "## Session 10:", ["## Session 11:"]),
        (11, "## Session 11:", ["## Player-Facing Handouts", "## Source Traceability"]),
    ]:
        body = extract_named_section(text, heading, stops) or f"{heading}\n\n(TBD)\n"
        pages.append(build_page(f"Session {sn}", f"page:arc-iii-session-{sn}", body, sort))
        sort += 100000

    contacts = extract_named_section(
        text,
        "### Speaker scenario casting policy (not Calling maps)",
        [
            "### Calling -> Kesh reminder",
            "### Calling → Kesh reminder",
            "### Calendar seed note",
            "## Session 7:",
        ],
    )
    if contacts:
        pages.append(
            build_page(
                "Arc III Contacts and Speakers",
                "page:arc-iii-contacts-speakers",
                "# Arc III Contacts and Speakers\n\n"
                "Operational scenario casting only. **Not** Calling → Speaker approval.\n\n"
                + contacts,
                sort,
            )
        )
        sort += 100000

    handouts = extract_named_section(
        text,
        "## Player-Facing Handouts (Pilot)",
        ["## Source Traceability Index"],
    )
    if handouts:
        pages.append(
            build_page(
                "Player Handouts",
                "page:arc-iii-player-handouts",
                handouts,
                sort,
                ownership=2,
            )
        )

    return {
        "_id": make_deterministic_id(JOURNAL_ID_KEY),
        "name": "Arc III Pilot — Integrated GM Guide (PROVISIONAL)",
        "pages": pages,
        "ownership": {"default": 0},
        "flags": {
            "dawn-of-the-jedaii": {
                "journalKey": JOURNAL_ID_KEY,
                "idStrategy": "sha256-base62-16",
                "pilot": True,
                "nonAuthoritative": True,
                "arc": "III",
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

    text = strip_operational_headers(SRC.read_text(encoding="utf-8"))
    journal = build_journal(text)
    payload = json.dumps(journal, ensure_ascii=False, indent=2) + "\n"

    names = [p["name"] for p in journal["pages"]]
    print("Pages:", ", ".join(names))

    if args.dry_run:
        print(f"DRY-RUN OK: {len(journal['pages'])} pages, {len(payload)} bytes -> {OUT}")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(payload, encoding="utf-8")
    print(f"Wrote {OUT} with {len(journal['pages'])} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
