"""Rendered-layout geometry analysis for GM Binder preview scans."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

# Documented tolerance for borders/antialiasing (pixels).
DEFAULT_TOLERANCE_PX = 2.0

CONTENT_SELECTORS = (
    "h1,h2,h3,h4,h5,h6,p,li,td,th,blockquote,table,pre,code,"
    ".note,.descriptive,.spell,.monster,.classFeature"
)


class PageStatus(str, Enum):
    PASS_NO_CLIPPING = "PASS_NO_CLIPPING"
    PASS_NO_CLIPPING_WITH_JUSTIFIED_WHITESPACE = "PASS_NO_CLIPPING_WITH_JUSTIFIED_WHITESPACE"
    WARNING_UNDERFILLED = "WARNING_UNDERFILLED"
    FAIL_RIGHT_CLIPPING = "FAIL_RIGHT_CLIPPING"
    FAIL_BOTTOM_CLIPPING = "FAIL_BOTTOM_CLIPPING"
    FAIL_THIRD_COLUMN = "FAIL_THIRD_COLUMN"
    FAIL_OVERLAP = "FAIL_OVERLAP"
    FAIL_SPLIT_BLOCK = "FAIL_SPLIT_BLOCK"
    BLOCKED_LAYOUT = "BLOCKED_LAYOUT"
    NEEDS_MANUAL_REVIEW = "NEEDS_MANUAL_REVIEW"


@dataclass
class ElementRect:
    tag: str
    text: str
    left: float
    right: float
    top: float
    bottom: float
    gmb_src: str | None = None
    nearest_heading: str | None = None

    @property
    def width(self) -> float:
        return self.right - self.left

    @property
    def height(self) -> float:
        return self.bottom - self.top


@dataclass
class OverflowFinding:
    page_index: int
    classification: PageStatus
    tag: str
    text_excerpt: str
    overflow_px: float
    overflow_direction: str
    gmb_src: str | None
    nearest_heading: str | None
    element: ElementRect
    page_left: float
    page_right: float
    page_top: float
    page_bottom: float


@dataclass
class PageAnalysis:
    page_index: int
    left: float
    right: float
    top: float
    bottom: float
    status: PageStatus
    overflow_findings: list[OverflowFinding] = field(default_factory=list)
    occupancy_ratio: float | None = None
    content_rect_count: int = 0


def classify_element_overflow(
    el: ElementRect,
    page_left: float,
    page_right: float,
    page_top: float,
    page_bottom: float,
    tolerance: float = DEFAULT_TOLERANCE_PX,
) -> tuple[PageStatus | None, str, float]:
    """Return (status, direction, overflow_px) or (None, '', 0) if no failure."""
    if el.width <= 0 and el.height <= 0:
        return None, "", 0.0

    if el.left >= page_right - tolerance:
        px = el.left - page_right
        return PageStatus.FAIL_THIRD_COLUMN, "left_off_page", px

    if el.right > page_right - tolerance:
        px = el.right - page_right
        return PageStatus.FAIL_RIGHT_CLIPPING, "right", px

    if el.bottom > page_bottom - tolerance:
        px = el.bottom - page_bottom
        return PageStatus.FAIL_BOTTOM_CLIPPING, "bottom", px

    return None, "", 0.0


def analyze_page_scan(
    page_index: int,
    page_bounds: dict[str, float],
    elements: list[dict[str, Any]],
    tolerance: float = DEFAULT_TOLERANCE_PX,
    underfill_threshold: float = 0.35,
) -> PageAnalysis:
    pl = float(page_bounds["left"])
    pr = float(page_bounds["right"])
    pt = float(page_bounds["top"])
    pb = float(page_bounds["bottom"])

    findings: list[OverflowFinding] = []
    visible_rects: list[tuple[float, float, float, float]] = []

    for raw in elements:
        el = ElementRect(
            tag=str(raw.get("tag", "")),
            text=str(raw.get("text", ""))[:200],
            left=float(raw["left"]),
            right=float(raw["right"]),
            top=float(raw["top"]),
            bottom=float(raw["bottom"]),
            gmb_src=raw.get("gmb_src"),
            nearest_heading=raw.get("nearest_heading"),
        )
        if not el.text.strip():
            continue

        # Only measure elements that intersect the page horizontally at all
        if el.right < pl + tolerance or el.left > pr + tolerance:
            if el.left >= pr - tolerance:
                pass  # third column candidate
            else:
                continue

        status, direction, px = classify_element_overflow(el, pl, pr, pt, pb, tolerance)
        if status:
            findings.append(
                OverflowFinding(
                    page_index=page_index,
                    classification=status,
                    tag=el.tag,
                    text_excerpt=el.text[:80],
                    overflow_px=px,
                    overflow_direction=direction,
                    gmb_src=el.gmb_src,
                    nearest_heading=el.nearest_heading,
                    element=el,
                    page_left=pl,
                    page_right=pr,
                    page_top=pt,
                    page_bottom=pb,
                )
            )
        else:
            # inside page bounds
            il = max(el.left, pl)
            ir = min(el.right, pr)
            it = max(el.top, pt)
            ib = min(el.bottom, pb)
            if ir > il and ib > it:
                visible_rects.append((il, it, ir, ib))

    if findings:
        # Worst classification wins
        priority = [
            PageStatus.FAIL_THIRD_COLUMN,
            PageStatus.FAIL_RIGHT_CLIPPING,
            PageStatus.FAIL_BOTTOM_CLIPPING,
        ]
        status = findings[0].classification
        for p in priority:
            if any(f.classification == p for f in findings):
                status = p
                break
    else:
        status = PageStatus.PASS_NO_CLIPPING

    occupancy: float | None = None
    page_area = max(1.0, (pr - pl) * (pb - pt))
    if visible_rects and not findings:
        # Approximate union area (simple sum capped — conservative)
        covered = sum((r[2] - r[0]) * (r[3] - r[1]) for r in visible_rects)
        occupancy = min(1.0, covered / page_area)
        if occupancy < underfill_threshold:
            status = PageStatus.WARNING_UNDERFILLED

    return PageAnalysis(
        page_index=page_index,
        left=pl,
        right=pr,
        top=pt,
        bottom=pb,
        status=status,
        overflow_findings=findings,
        occupancy_ratio=occupancy,
        content_rect_count=len(visible_rects),
    )


def analyze_document_scan(
    scan: dict[str, Any],
    tolerance: float = DEFAULT_TOLERANCE_PX,
) -> tuple[list[PageAnalysis], list[OverflowFinding]]:
    pages = scan.get("pages", [])
    analyses: list[PageAnalysis] = []
    all_findings: list[OverflowFinding] = []
    for page in pages:
        pa = analyze_page_scan(
            int(page["page_index"]),
            page["bounds"],
            page.get("elements", []),
            tolerance=tolerance,
        )
        analyses.append(pa)
        all_findings.extend(pa.overflow_findings)
    return analyses, all_findings


def first_failing_page(analyses: list[PageAnalysis]) -> PageAnalysis | None:
    fail_statuses = {
        PageStatus.FAIL_RIGHT_CLIPPING,
        PageStatus.FAIL_BOTTOM_CLIPPING,
        PageStatus.FAIL_THIRD_COLUMN,
        PageStatus.FAIL_OVERLAP,
        PageStatus.BLOCKED_LAYOUT,
    }
    for pa in analyses:
        if pa.status in fail_statuses:
            return pa
    return None


def first_overflow_finding(findings: list[OverflowFinding]) -> OverflowFinding | None:
    if not findings:
        return None
    return min(findings, key=lambda f: (f.page_index, f.element.top, f.element.left))


def semantic_block_key(finding: OverflowFinding) -> str:
    """Deduplication key for optimization decisions."""
    if finding.gmb_src:
        return finding.gmb_src
    heading = (finding.nearest_heading or "").strip().upper()
    return f"p{finding.page_index}|h:{heading}|t:{finding.text_excerpt[:40]}"


def deduplicate_overflow_findings(findings: list[OverflowFinding]) -> list[OverflowFinding]:
    """One representative finding per semantic block."""
    seen: dict[str, OverflowFinding] = {}
    for f in sorted(findings, key=lambda x: (x.page_index, x.element.top, x.element.left)):
        key = semantic_block_key(f)
        if key not in seen:
            seen[key] = f
    return list(seen.values())


def overflow_metrics(findings: list[OverflowFinding]) -> dict[str, int]:
    deduped = deduplicate_overflow_findings(findings)
    fail_pages = {f.page_index for f in findings}
    return {
        "raw_overflow_count": len(findings),
        "semantic_block_overflow_count": len(deduped),
        "failing_page_count": len(fail_pages),
    }


def classify_occupancy(occupancy_ratio: float | None) -> str:
    if occupancy_ratio is None:
        return "unknown"
    pct = occupancy_ratio * 100.0
    if pct < 30.0:
        return "review_required"
    if pct < 45.0:
        return "warning"
    return "ok"
