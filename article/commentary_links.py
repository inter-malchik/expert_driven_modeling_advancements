"""Compatibility facade for commentary citation helpers."""

from __future__ import annotations

from article.source_registry import (
    SOURCE_URLS,
    enrich_commentaries,
    enrich_commentary_sources,
    resolve_source_url,
)
from article.source_render import render_sources_html
