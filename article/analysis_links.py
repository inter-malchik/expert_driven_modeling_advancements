"""URL and commentary lookup helpers for analysis pages."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import urlencode

if TYPE_CHECKING:
    from article.commentaries import Commentary


def analysis_slug_from_filenote(filenote: str) -> str | None:
    if not filenote:
        return None
    name = filenote.split(" — ")[0].strip()
    if name.endswith(".md"):
        return Path(name).stem
    return None


def analysis_url(slug: str, *, commentary_id: str | None = None) -> str:
    params: dict[str, str] = {"analysis": slug}
    if commentary_id:
        params["from"] = commentary_id
    return f"/?{urlencode(params)}"


def commentary_by_slug(slug: str) -> Commentary | None:
    from article.commentaries import COMMENTARIES
    from article.commentary_links import enrich_commentary_sources

    for commentary in COMMENTARIES:
        if analysis_slug_from_filenote(commentary["filenote"]) == slug:
            return enrich_commentary_sources(commentary)
    return None


def commentary_for_slug(slug: str) -> dict[str, str] | None:
    commentary = commentary_by_slug(slug)
    if not commentary:
        return None
    return {
        "id": commentary["id"],
        "title": commentary["title"],
        "section": commentary["section"],
    }
