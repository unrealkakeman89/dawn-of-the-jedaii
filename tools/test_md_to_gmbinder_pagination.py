#!/usr/bin/env python3
"""Tests for GM Binder generator pagination (tools/md_to_gmbinder.py)."""

from __future__ import annotations

import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN_PATH = ROOT / "tools" / "md_to_gmbinder.py"
PAGINATION_PATH = ROOT / "tools" / "gmbinder_pagination.json"
GUIDE = ROOT / "dawn-of-the-jedaii-campaign-guide.md"
COMPANION = ROOT / "gm-narrative" / "dawn-of-the-jedaii-living-force-gm-book.md"
FOUNDRY_JSON = ROOT / "foundry" / "dawn-of-the-jedaii.journal.json"
FOUNDRY_TOOL = ROOT / "tools" / "md_to_foundry_journal.py"


def load_gen():
    spec = importlib.util.spec_from_file_location("md_to_gmbinder", GEN_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


class PaginationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_gen()
        cls.koorivar = cls.mod.resolve_koorivar_path(None)
        cls.breaks = cls.mod.load_pagination_config(PAGINATION_PATH)
        cls.text, cls.applied = cls.mod.build_document(cls.koorivar, cls.breaks)

    def test_no_legacy_standalone_page(self):
        self.assertEqual(self.mod.count_legacy_page_directives(self.text), 0)

    def test_chapter_boundaries_use_pagebreak(self):
        guide = GUIDE.read_text(encoding="utf-8")
        chapter_count = len(re.findall(r"(?m)^# ", guide))
        pagebreaks = len(re.findall(r"(?m)^\\pagebreak\s*$", self.text))
        internal = len(self.applied)
        self.assertEqual(pagebreaks, chapter_count + internal)

    def test_configured_internal_breaks_exactly_once(self):
        self.assertEqual(len(self.applied), len(self.breaks))
        ids = [b["id"] for b in self.applied]
        self.assertEqual(len(ids), len(set(ids)))
        for entry in self.breaks:
            token = self.mod.BREAK_TOKENS[entry["break"]]
            pattern = (
                rf"(?m)^{re.escape(token)}\s*\n\n"
                rf"{re.escape(entry['before_heading'])}\s*$"
            )
            self.assertEqual(
                len(re.findall(pattern, self.text)),
                1,
                msg=f"expected one insertion for {entry['id']}",
            )

    def test_chapter_04_internal_break(self):
        """Ch04 uses geometry-derived break before Section 5; obsolete seed before Section 6 removed."""
        idx = self.text.find("### 5. Machine-Spirit Interfaces")
        self.assertGreater(idx, 0)
        self.assertIn("\\pagebreak", self.text[max(0, idx - 40) : idx])
        sealed_idx = self.text.find("### 6. Sealed Vaults")
        self.assertGreater(sealed_idx, 0)
        self.assertNotIn(
            "\\pagebreak",
            self.text[max(0, sealed_idx - 40) : sealed_idx],
            msg="obsolete ch04-sealed-vaults seed must not remain before Section 6",
        )

    def test_missing_heading_reports(self):
        bad = [
            {
                "id": "missing-test",
                "chapter": "04 — The Tho Yor",
                "before_heading": "### 99. Does Not Exist",
                "break": "pagebreak",
                "rationale": "test",
            }
        ]
        with self.assertRaises(self.mod.PaginationError) as ctx:
            self.mod.apply_internal_breaks("04 — The Tho Yor", "## x\n", bad)
        self.assertIn("not found", str(ctx.exception).lower())

    def test_duplicate_heading_reports(self):
        body = "### Twin\n\ntext\n\n### Twin\n\nmore\n"
        bad = [
            {
                "id": "dup-test",
                "chapter": "04 — The Tho Yor",
                "before_heading": "### Twin",
                "break": "pagebreak",
                "rationale": "test",
            }
        ]
        with self.assertRaises(self.mod.PaginationError) as ctx:
            self.mod.apply_internal_breaks("04 — The Tho Yor", body, bad)
        self.assertIn("matches", str(ctx.exception).lower())

    def test_idempotent_generation(self):
        t2, a2 = self.mod.build_document(self.koorivar, self.breaks)
        self.assertEqual(self.text, t2)
        self.assertEqual(
            [b["id"] for b in self.applied],
            [b["id"] for b in a2],
        )

    def test_chapter_12_and_22_regression(self):
        self.assertIn("# 12 — Species Spotlight: Koorivar", self.text)
        self.assertIn("# 22 — Faces of the First Migration", self.text)

    def test_speakers_present(self):
        start = self.text.index("# 22 — Faces of the First Migration")
        m = re.search(r"(?m)^\\pagebreak\s*$", self.text[start + 10 :])
        self.assertIsNotNone(m)
        chunk = self.text[start : start + 10 + m.start()]
        self.assertIn("## A. Eight Tho Yor Speakers", chunk)

    def test_generator_paths_do_not_target_companion_or_foundry(self):
        self.assertEqual(self.mod.MASTER, GUIDE)
        self.assertNotEqual(self.mod.OUT, FOUNDRY_JSON)
        self.assertNotEqual(self.mod.OUT, COMPANION)
        self.assertTrue(COMPANION.is_file())
        self.assertTrue(FOUNDRY_JSON.is_file())

    def test_pagination_config_not_referenced_by_foundry_tool(self):
        foundry_src = FOUNDRY_TOOL.read_text(encoding="utf-8")
        self.assertNotIn("gmbinder_pagination", foundry_src)
        self.assertNotIn("pagebreak", foundry_src)

    def test_failed_generation_does_not_replace_output(self):
        out = self.mod.OUT
        before = out.read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            bad_cfg = Path(tmp) / "bad.json"
            bad_cfg.write_text(
                json.dumps(
                    {
                        "breaks": [
                            {
                                "id": "boom",
                                "chapter": "04 — The Tho Yor",
                                "before_heading": "### NOPE",
                                "break": "pagebreak",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaises(self.mod.PaginationError):
                breaks = self.mod.load_pagination_config(bad_cfg)
                self.mod.build_document(self.koorivar, breaks)
        self.assertEqual(out.read_text(encoding="utf-8"), before)


if __name__ == "__main__":
    unittest.main()
