#!/usr/bin/env python3
"""Remove epistemic scaffolding tags from article/analysis/*.md files."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_DIR = ROOT / "article" / "analysis"

sys.path.insert(0, str(ROOT))

from article.comparison_prose import clean_comparison_prose, prepare_comparison_markdown


def main() -> None:
    for path in sorted(ANALYSIS_DIR.glob("*.md")):
        original = path.read_text(encoding="utf-8")
        cleaned = prepare_comparison_markdown(original)
        path.write_text(cleaned, encoding="utf-8")
        print(f"cleaned {path.name}")


if __name__ == "__main__":
    main()
