"""Semantic block keys for GM Binder source ↔ rendered DOM traceability."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Iterator

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def slugify(text: str) -> str:
    """Normalize heading/chapter text into a stable slug fragment."""
    text = unicodedata.normalize("NFKC", text)
    text = text.lower()
    text = text.replace("'", "'").replace("'", "'")
    text = re.sub(r"[—–\-]+", "-", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "untitled"


def chapter_key(chapter_title: str) -> str:
    """Stable chapter identifier from H1 title (without leading '# ')."""
    return slugify(chapter_title)


def block_key(chapter: str, heading_line: str) -> str:
    """Stable semantic key: chapter|level|heading-slug."""
    m = HEADING_RE.match(heading_line.strip())
    if not m:
        raise ValueError(f"not a markdown heading: {heading_line!r}")
    level = len(m.group(1))
    title = m.group(2).strip()
    return f"{chapter_key(chapter)}|h{level}|{slugify(title)}"


@dataclass(frozen=True)
class SemanticBlock:
    chapter: str
    heading_line: str
    level: int
    title: str
    key: str
    line_index: int  # 0-based line in chapter body (informational)


def iter_semantic_blocks(chapter_title: str, body: str) -> Iterator[SemanticBlock]:
    """Yield heading blocks in document order for one chapter body."""
    for idx, line in enumerate(body.splitlines()):
        stripped = line.strip()
        m = HEADING_RE.match(stripped)
        if not m:
            continue
        level = len(m.group(1))
        title = m.group(2).strip()
        yield SemanticBlock(
            chapter=chapter_title,
            heading_line=stripped,
            level=level,
            title=title,
            key=block_key(chapter_title, stripped),
            line_index=idx,
        )


def trace_marker_html(block_key_str: str) -> str:
    """Layout-neutral trace marker on its own line (display:contents avoids column box)."""
    safe = block_key_str.replace('"', "")
    return (
        f'<span data-gmb-src="{safe}" aria-hidden="true" '
        'style="display:contents"></span>\n'
    )


def inject_trace_markers(chapter_title: str, body: str) -> str:
    """Prefix each markdown heading line with a trace marker."""
    out: list[str] = []
    for line in body.splitlines(keepends=True):
        stripped = line.rstrip("\r\n")
        if HEADING_RE.match(stripped.strip()):
            key = block_key(chapter_title, stripped.strip())
            out.append(trace_marker_html(key))
        out.append(line)
    return "".join(out)


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


def all_blocks_from_guide(text: str) -> list[SemanticBlock]:
    blocks: list[SemanticBlock] = []
    for title, body in split_h1_chapters(text):
        blocks.extend(iter_semantic_blocks(title, body))
    return blocks


def all_blocks_for_pagination(guide_text: str, koorivar_markdown: str | None = None) -> list[SemanticBlock]:
    """Guide blocks plus injected species headings (e.g. Koorivar Traits)."""
    blocks = all_blocks_from_guide(guide_text)
    if not koorivar_markdown:
        return blocks
    species_ch = "12 — Species Spotlight: Koorivar"
    extra = list(iter_semantic_blocks(species_ch, koorivar_markdown))
    # Append injection-only headings after guide ch12 blocks
    ch12_end = 0
    for i, b in enumerate(blocks):
        if b.chapter == species_ch:
            ch12_end = i + 1
    if ch12_end:
        blocks[ch12_end:ch12_end] = extra
    else:
        blocks.extend(extra)
    return blocks


def resolve_heading_from_rendered(
    blocks: list[SemanticBlock],
    nearest_heading: str | None,
    text_excerpt: str | None,
) -> tuple[str, str, str] | None:
    """Map rendered heading text to a pagination break target."""
    if not nearest_heading and not text_excerpt:
        return None
    norm = (nearest_heading or text_excerpt or "").strip().upper()
    for b in blocks:
        if b.title.upper() == norm or norm in b.title.upper() or b.title.upper() in norm:
            return b.chapter, b.heading_line, b.key
    return None


def candidate_break_keys_for_overflow(
    blocks: list[SemanticBlock],
    overflow_block_key: str | None,
    overflow_heading_text: str | None,
) -> list[str]:
    """Ordered candidate break locations (block keys) for a failing page."""
    if not blocks:
        return []

    target_idx: int | None = None
    if overflow_block_key:
        for i, b in enumerate(blocks):
            if b.key == overflow_block_key:
                target_idx = i
                break

    if target_idx is None and overflow_heading_text:
        norm = overflow_heading_text.strip().upper()
        for i, b in enumerate(blocks):
            if b.title.upper() in norm or norm in b.title.upper():
                target_idx = i
                break

    if target_idx is None:
        return []

    target = blocks[target_idx]
    same_chapter = [b for b in blocks if b.chapter == target.chapter]
    idx_in_ch = same_chapter.index(target)

    candidates: list[str] = []
    # Immediately before overflowing block
    candidates.append(target.key)

    # Preceding H3/H2 in same chapter
    for j in range(idx_in_ch - 1, -1, -1):
        b = same_chapter[j]
        if b.level <= 3 and b.key not in candidates:
            candidates.append(b.key)
        if b.level == 2:
            break

    for j in range(idx_in_ch - 1, -1, -1):
        b = same_chapter[j]
        if b.level == 2 and b.key not in candidates:
            candidates.append(b.key)
            break

    return candidates
