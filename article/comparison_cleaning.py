"""Cleaning rules for analysis markdown before rendering."""

from __future__ import annotations

import re

READING_GUIDE = """\
> **How to read this comparison**
>
> - **Paper A** denotes Gindullina et al. (Expert-Guided PINN); **Paper B** denotes the cited source paper.
> - Quoted passages are taken from the papers named in the comparison.
> - Interpretive links between papers are argued explicitly; they are not claims made by either author team.
> - Sections titled **Proposed direction** suggest possible follow-up work. They are engineering ideas, not reported results.

"""

EPISTEMIC_TAG = re.compile(
    r"\s*\((?:Comparative inference|Author-stated|Empirically shown|Speculative extension)"
    r"[^)]*\)",
    re.IGNORECASE,
)
STANDALONE_TAG_LINE = re.compile(
    r"^\s*\((?:Comparative inference|Author-stated|Empirically shown|Speculative extension)"
    r"[^)]*\)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
SELF_REPORT = re.compile(r"\n\*\*Self-report:\*\*.*\Z", re.DOTALL)
SRC_LINK_LINE = re.compile(
    r"^\s*>\s*\*\*Source in\s*`src/`\s*:\*\*.*(?:\n|$)",
    re.MULTILINE,
)
DIRECTION_HEADING = re.compile(r"^## Direction ", re.MULTILINE)
MULTI_SPACE = re.compile(r"  +")
SPACE_BEFORE_PUNCT = re.compile(r"\s+([,.;:!?])")


def clean_comparison_prose(text: str) -> str:
    text = EPISTEMIC_TAG.sub("", text)
    text = STANDALONE_TAG_LINE.sub("", text)
    text = SELF_REPORT.sub("", text)
    text = SRC_LINK_LINE.sub("", text)
    text = DIRECTION_HEADING.sub("## Proposed direction ", text)
    text = SPACE_BEFORE_PUNCT.sub(r"\1", text)
    text = MULTI_SPACE.sub(" ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def prepare_comparison_markdown(text: str) -> str:
    cleaned = clean_comparison_prose(text)
    if cleaned.startswith("> **How to read this comparison**"):
        return cleaned
    return READING_GUIDE + "\n" + cleaned
