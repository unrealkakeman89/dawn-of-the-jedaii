#!/usr/bin/env python3
"""Unit tests for GM Binder geometry and semantic modules."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from gmbinder_geometry import (  # noqa: E402
    PageStatus,
    analyze_document_scan,
    classify_element_overflow,
)
from gmbinder_semantic import (  # noqa: E402
    block_key,
    candidate_break_keys_for_overflow,
    inject_trace_markers,
    slugify,
)


class SemanticTests(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify("04 — The Tho Yor"), "04-the-tho-yor")

    def test_block_key(self):
        k = block_key("04 — The Tho Yor", "### 6. Sealed Vaults")
        self.assertIn("04-the-tho-yor", k)
        self.assertIn("h3", k)

    def test_inject_trace_markers(self):
        body = "## Alpha\n\nText\n\n### Beta\n"
        out = inject_trace_markers("04 — The Tho Yor", body)
        self.assertIn('data-gmb-src="04-the-tho-yor|h2|alpha"', out)
        self.assertIn("\n## Alpha\n", out)
        self.assertIn("\n### Beta\n", out)
        self.assertNotIn("</span>## Alpha", out)

    def test_candidate_keys(self):
        from gmbinder_semantic import SemanticBlock

        blocks = [
            SemanticBlock("04 — The Tho Yor", "## Playable zones", 2, "Playable zones", "k1", 0),
            SemanticBlock("04 — The Tho Yor", "### 5. Machine", 3, "5. Machine", "k2", 1),
            SemanticBlock("04 — The Tho Yor", "### 6. Sealed Vaults", 3, "6. Sealed Vaults", "k3", 2),
        ]
        keys = candidate_break_keys_for_overflow(blocks, "k3", None)
        self.assertEqual(keys[0], "k3")


class GeometryTests(unittest.TestCase):
    def test_right_clipping(self):
        from gmbinder_geometry import ElementRect

        el = ElementRect("P", "clip", left=1800, right=2130, top=100, bottom=120)
        status, direction, px = classify_element_overflow(el, 1005, 1845, 0, 1084)
        self.assertEqual(status, PageStatus.FAIL_RIGHT_CLIPPING)
        self.assertGreater(px, 0)

    def test_third_column(self):
        from gmbinder_geometry import ElementRect

        el = ElementRect("H3", "off", left=1850, right=2200, top=100, bottom=130)
        status, _, _ = classify_element_overflow(el, 1005, 1845, 0, 1084)
        self.assertEqual(status, PageStatus.FAIL_THIRD_COLUMN)

    def test_synthetic_scan_third_column(self):
        scan = {
            "pages": [
                {
                    "page_index": 0,
                    "bounds": {"left": 100, "right": 940, "top": 0, "bottom": 1080},
                    "elements": [
                        {
                            "tag": "H3",
                            "text": "6. SEALED VAULTS",
                            "left": 950,
                            "right": 1280,
                            "top": 200,
                            "bottom": 230,
                            "gmb_src": "04-the-tho-yor|h3|6-sealed-vaults",
                        }
                    ],
                }
            ]
        }
        analyses, findings = analyze_document_scan(scan, tolerance=2)
        self.assertEqual(len(findings), 1)
        self.assertEqual(analyses[0].status, PageStatus.FAIL_THIRD_COLUMN)

    def test_ch04_fixture_page(self):
        fixture = ROOT / "tools" / "fixtures" / "gmbinder-ch04-overflow-scan.json"
        if not fixture.is_file():
            self.skipTest("fixture missing")
        scan = json.loads(fixture.read_text(encoding="utf-8"))
        _, findings = analyze_document_scan(scan)
        self.assertGreater(len(findings), 0)
        self.assertTrue(any(f.classification in {PageStatus.FAIL_THIRD_COLUMN, PageStatus.FAIL_RIGHT_CLIPPING} for f in findings))

    def test_ch05_fixture_page(self):
        fixture = ROOT / "tools" / "fixtures" / "gmbinder-ch05-overflow-scan.json"
        if not fixture.is_file():
            self.skipTest("fixture missing")
        scan = json.loads(fixture.read_text(encoding="utf-8"))
        for page in scan.get("pages", []):
            if "overflow_elements" in page and "elements" not in page:
                page["elements"] = page.pop("overflow_elements")
        _, findings = analyze_document_scan(scan)
        self.assertGreater(len(findings), 0)


if __name__ == "__main__":
    unittest.main()
