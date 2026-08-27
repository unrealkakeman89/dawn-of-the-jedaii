"""Load/save GM Binder pagination configuration (v3 schema)."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PAGINATION_PATH = ROOT / "tools" / "gmbinder_pagination.json"

SUPPORTED_DIRECTIVES = frozenset({"pagebreak", "pagebreakNum", "columnbreak"})
VALID_SELECTION_METHODS = frozenset(
    {"human_pinned", "unvalidated_seed", "derived", "browser_validated", "obsolete"}
)
LEGACY_PINNED = "pinned"
PRE_VALIDATOR_SEED_NOTE = (
    "Pre-validator manual heading guess (2026-08-26); not human-pinned unless "
    "human_pinned is explicitly true."
)


class PaginationConfigError(RuntimeError):
    pass


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalize_break_entry(raw: dict[str, Any], index: int) -> dict[str, Any]:
    """Normalize v1/v2/v3 break record."""
    chapter = str(raw.get("chapter_key") or raw.get("chapter", "")).strip()
    before_heading = str(raw.get("before_heading", "")).strip()
    before_block_key = str(raw.get("before_block_key", "")).strip()
    directive = str(raw.get("directive") or raw.get("break", "pagebreak")).strip()
    entry_id = str(raw.get("id", f"break-{index}")).strip()
    if not chapter or not before_heading:
        raise PaginationConfigError(f"break[{index}] missing chapter or before_heading")
    if directive not in SUPPORTED_DIRECTIVES:
        raise PaginationConfigError(f"break[{index}] unsupported directive {directive!r}")

    human_pinned = bool(raw.get("human_pinned", False))
    selection_method = str(raw.get("selection_method", "")).strip()
    if selection_method == LEGACY_PINNED:
        selection_method = "human_pinned" if human_pinned else "unvalidated_seed"
    if selection_method == "seed":
        selection_method = "unvalidated_seed"
    if not selection_method:
        selection_method = "human_pinned" if human_pinned else "derived"
    if selection_method not in VALID_SELECTION_METHODS:
        raise PaginationConfigError(f"break[{index}] invalid selection_method {selection_method!r}")

    browser_validated = bool(raw.get("browser_validated", False))
    if selection_method == "browser_validated":
        selection_method = "derived"
        browser_validated = True

    origin = str(raw.get("origin") or raw.get("seed_note") or "").strip()
    if not origin:
        if selection_method == "human_pinned":
            origin = "human_approved"
        elif selection_method == "unvalidated_seed":
            origin = "pre_validator_manual_guess"
        elif selection_method == "derived":
            origin = "geometry_optimizer"
        else:
            origin = selection_method

    return {
        "id": entry_id,
        "chapter_key": chapter,
        "chapter": chapter,
        "before_block_key": before_block_key,
        "before_heading": before_heading,
        "directive": directive,
        "break": directive,
        "selection_method": selection_method,
        "human_pinned": human_pinned,
        "browser_validated": browser_validated,
        "validation_timestamp": raw.get("validation_timestamp"),
        "source_revision": raw.get("source_revision"),
        "reason": str(raw.get("reason") or raw.get("rationale", "")).strip(),
        "notes": str(raw.get("notes", "")).strip(),
        "origin": origin,
        "obsolete": bool(raw.get("obsolete", selection_method == "obsolete")),
    }


def is_protected_break(entry: dict[str, Any]) -> bool:
    """Breaks that must not be auto-moved/removed without explicit authorization."""
    if entry.get("human_pinned"):
        return True
    if entry.get("selection_method") == "human_pinned":
        return True
    if entry.get("browser_validated") and entry.get("selection_method") != "unvalidated_seed":
        return True
    return False


def pagination_state_hash(data: dict[str, Any]) -> str:
    """Stable hash of active break configuration for cycle detection."""
    active = [
        {
            "id": b["id"],
            "chapter": b["chapter"],
            "before_heading": b["before_heading"],
            "directive": b["directive"],
        }
        for b in sorted(data.get("breaks", []), key=lambda x: (x["chapter"], x["before_heading"]))
        if not b.get("obsolete")
    ]
    payload = json.dumps(active, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def load_pagination_file(path: Path | None = None) -> dict[str, Any]:
    cfg_path = path or DEFAULT_PAGINATION_PATH
    if not cfg_path.is_file():
        return {"version": 3, "breaks": [], "seeds": [], "obsolete_breaks": []}
    data = json.loads(cfg_path.read_text(encoding="utf-8"))
    breaks_raw = data.get("breaks", [])
    if not isinstance(breaks_raw, list):
        raise PaginationConfigError("breaks must be a list")
    breaks = [normalize_break_entry(b, i) for i, b in enumerate(breaks_raw) if not b.get("obsolete")]
    seen_ids: set[str] = set()
    for b in breaks:
        if b["id"] in seen_ids:
            raise PaginationConfigError(f"duplicate break id {b['id']!r}")
        seen_ids.add(b["id"])
    return {
        "version": int(data.get("version", 3)),
        "description": data.get("description", ""),
        "breaks": breaks,
        "seeds": data.get("seeds", []),
        "obsolete_breaks": data.get("obsolete_breaks", []),
    }


def save_pagination_file(data: dict[str, Any], path: Path | None = None) -> None:
    cfg_path = path or DEFAULT_PAGINATION_PATH
    data = dict(data)
    data["version"] = 3
    cfg_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def breaks_for_generator(data: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "id": b["id"],
            "chapter": b["chapter"],
            "before_heading": b["before_heading"],
            "break": b["directive"],
            "rationale": b.get("reason", ""),
        }
        for b in data.get("breaks", [])
        if not b.get("obsolete")
    ]


def migrate_pre_validator_classification(data: dict[str, Any]) -> dict[str, Any]:
    """Reclassify legacy pinned/unvalidated entries per Kakeman89 policy."""
    migrated = 0
    for b in data.get("breaks", []):
        if b.get("human_pinned"):
            continue
        if b.get("browser_validated"):
            continue
        old = b.get("selection_method")
        if old in {LEGACY_PINNED, "seed", "unvalidated_seed", "derived"} and not b.get("human_pinned"):
            if old == LEGACY_PINNED or b.get("origin") == "pre_validator_manual_guess":
                b["selection_method"] = "unvalidated_seed"
                b["human_pinned"] = False
                if not b.get("notes"):
                    b["notes"] = PRE_VALIDATOR_SEED_NOTE
                migrated += 1
    data["version"] = 3
    data["description"] = (
        "Generator-owned pagination v3. selection_method: human_pinned | unvalidated_seed | "
        "derived | obsolete. Only human_pinned breaks are protected from auto-movement."
    )
    return {"migrated_to_unvalidated_seed": migrated}


def mark_break_obsolete(data: dict[str, Any], break_id: str, reason: str) -> bool:
    obsolete = data.setdefault("obsolete_breaks", [])
    kept: list[dict[str, Any]] = []
    removed = False
    for b in data.get("breaks", []):
        if b["id"] == break_id:
            if is_protected_break(b):
                return False
            entry = dict(b)
            entry["selection_method"] = "obsolete"
            entry["obsolete"] = True
            entry["obsolete_reason"] = reason
            entry["obsolete_timestamp"] = _utc_now()
            obsolete.append(entry)
            removed = True
        else:
            kept.append(b)
    if removed:
        data["breaks"] = kept
    return removed


def add_derived_break(
    data: dict[str, Any],
    *,
    chapter: str,
    before_heading: str,
    before_block_key: str,
    reason: str,
    source_revision: str | None = None,
    browser_validated: bool = False,
) -> dict[str, Any]:
    for b in data.get("breaks", []):
        if b["chapter"] == chapter and b["before_heading"] == before_heading:
            return data
    entry_id = f"derived-{before_block_key or chapter}-{len(data['breaks'])}"
    data.setdefault("breaks", []).append(
        {
            "id": entry_id,
            "chapter_key": chapter,
            "chapter": chapter,
            "before_block_key": before_block_key,
            "before_heading": before_heading,
            "directive": "pagebreak",
            "break": "pagebreak",
            "selection_method": "derived",
            "human_pinned": False,
            "browser_validated": browser_validated,
            "validation_timestamp": _utc_now() if browser_validated else None,
            "source_revision": source_revision,
            "reason": reason,
            "notes": "",
            "origin": "geometry_optimizer",
            "obsolete": False,
        }
    )
    return data


def mark_all_unvalidated(data: dict[str, Any]) -> dict[str, Any]:
    for b in data.get("breaks", []):
        if not b.get("human_pinned"):
            b["browser_validated"] = False
            b["validation_timestamp"] = None
    return data


def mark_all_browser_validated(data: dict[str, Any], source_revision: str) -> None:
    now = _utc_now()
    for b in data.get("breaks", []):
        b["browser_validated"] = True
        b["validation_timestamp"] = now
        b["source_revision"] = source_revision


def archive_seeds_from_breaks(data: dict[str, Any], note: str) -> dict[str, Any]:
    seeds = list(data.get("seeds", []))
    for b in data.get("breaks", []):
        seeds.append({**b, "seed_note": note, "browser_validated": False})
    data["seeds"] = seeds
    return data
