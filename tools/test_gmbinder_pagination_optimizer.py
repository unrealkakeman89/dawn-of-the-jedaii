#!/usr/bin/env python3
"""Tests for pagination v3 schema and optimizer helpers."""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from gmbinder_geometry import overflow_metrics  # noqa: E402
from gmbinder_pagination_io import (  # noqa: E402
    add_derived_break,
    is_protected_break,
    load_pagination_file,
    mark_break_obsolete,
    migrate_pre_validator_classification,
    normalize_break_entry,
    pagination_state_hash,
)
from gmbinder_semantic import inject_trace_markers  # noqa: E402


class PaginationSchemaTests(unittest.TestCase):
    def test_legacy_pinned_becomes_unvalidated_seed(self):
        raw = {
            "id": "x",
            "chapter": "04 — The Tho Yor",
            "before_heading": "### 6. Sealed Vaults",
            "break": "pagebreak",
            "selection_method": "pinned",
            "browser_validated": False,
        }
        entry = normalize_break_entry(raw, 0)
        self.assertEqual(entry["selection_method"], "unvalidated_seed")
        self.assertFalse(entry["human_pinned"])

    def test_human_pinned_preserved(self):
        raw = {
            "id": "x",
            "chapter": "04 — The Tho Yor",
            "before_heading": "### X",
            "break": "pagebreak",
            "selection_method": "pinned",
            "human_pinned": True,
            "browser_validated": False,
        }
        entry = normalize_break_entry(raw, 0)
        self.assertEqual(entry["selection_method"], "human_pinned")
        self.assertTrue(entry["human_pinned"])

    def test_obsolete_removal(self):
        data = {
            "version": 3,
            "breaks": [
                {
                    "id": "seed1",
                    "chapter_key": "04 — The Tho Yor",
                    "chapter": "04 — The Tho Yor",
                    "before_heading": "### A",
                    "directive": "pagebreak",
                    "selection_method": "unvalidated_seed",
                    "human_pinned": False,
                    "browser_validated": False,
                }
            ],
            "obsolete_breaks": [],
        }
        self.assertTrue(mark_break_obsolete(data, "seed1", "superseded"))
        self.assertEqual(len(data["breaks"]), 0)
        self.assertEqual(len(data["obsolete_breaks"]), 1)
        self.assertEqual(data["obsolete_breaks"][0]["selection_method"], "obsolete")

    def test_protected_human_pinned(self):
        entry = {"human_pinned": True, "browser_validated": False, "selection_method": "human_pinned"}
        self.assertTrue(is_protected_break(entry))

    def test_state_hash_cycle_detection(self):
        a = {"breaks": [{"id": "1", "chapter": "A", "before_heading": "## H", "directive": "pagebreak", "obsolete": False}]}
        b = copy.deepcopy(a)
        self.assertEqual(pagination_state_hash(a), pagination_state_hash(b))


class OverflowDedupTests(unittest.TestCase):
    def test_dedup_table_descendants(self):
        from gmbinder_geometry import OverflowFinding, PageStatus, ElementRect, deduplicate_overflow_findings

        el = ElementRect("TD", "cell", 1900, 2100, 10, 20, gmb_src="k|h3|t", nearest_heading="H")
        findings = [
            OverflowFinding(1, PageStatus.FAIL_RIGHT_CLIPPING, "TD", "a", 10, "r", "k|h3|t", "H", el, 0, 840, 0, 1080),
            OverflowFinding(1, PageStatus.FAIL_RIGHT_CLIPPING, "TD", "b", 10, "r", "k|h3|t", "H", el, 0, 840, 0, 1080),
        ]
        self.assertEqual(len(deduplicate_overflow_findings(findings)), 1)
        metrics = overflow_metrics(findings)
        self.assertEqual(metrics["raw_overflow_count"], 2)
        self.assertEqual(metrics["semantic_block_overflow_count"], 1)


class TraceNeutralityTests(unittest.TestCase):
    def test_heading_on_own_line_after_marker(self):
        body = "### Title\n\nPara\n"
        out = inject_trace_markers("04 — The Tho Yor", body)
        self.assertIn("\n### Title\n", out)
        self.assertNotIn("</span>### Title", out)


if __name__ == "__main__":
    unittest.main()
