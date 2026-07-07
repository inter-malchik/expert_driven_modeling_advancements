"""Registry for full-text literature comparison pages."""

from __future__ import annotations

import re
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import urlencode

if TYPE_CHECKING:
    from article.commentaries import Commentary

ANALYSIS_DIR = Path(__file__).resolve().parent / "analysis"


def analysis_slug_from_filenote(filenote: str) -> str | None:
    if not filenote:
        return None
    name = filenote.split(" — ")[0].strip()
    if name.endswith(".md"):
        return name[:-3]
    return None


def analysis_url(slug: str, *, commentary_id: str | None = None) -> str:
    params: dict[str, str] = {"analysis": slug}
    if commentary_id:
        params["from"] = commentary_id
    return f"/?{urlencode(params)}"


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


def commentary_for_slug(slug: str) -> dict[str, str] | None:
    commentary = commentary_by_slug(slug)
    if not commentary:
        return None
    return {
        "id": commentary["id"],
        "title": commentary["title"],
        "section": commentary["section"],
    }


def commentary_by_slug(slug: str) -> Commentary | None:
    from article.commentaries import COMMENTARIES
    from article.commentary_links import enrich_commentary_sources

    for commentary in COMMENTARIES:
        if analysis_slug_from_filenote(commentary["filenote"]) == slug:
            return enrich_commentary_sources(commentary)
    return None
