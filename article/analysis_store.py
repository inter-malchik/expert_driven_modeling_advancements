"""Storage and file-loading helpers for analysis markdown pages."""

from __future__ import annotations

import re
from pathlib import Path

ANALYSIS_DIR = Path(__file__).resolve().parent / "analysis"


def list_analysis_slugs() -> list[str]:
    return sorted(path.stem for path in ANALYSIS_DIR.glob("*.md"))


def load_analysis(slug: str) -> tuple[str, str]:
    path = ANALYSIS_DIR / f"{slug}.md"
    if not path.is_file():
        raise FileNotFoundError(slug)
    text = path.read_text(encoding="utf-8")
    title_match = re.search(r"^#{1,4}\s+(.+)$", text, re.M)
    title = title_match.group(1).strip() if title_match else slug.replace("_", " ")
    return title, text
