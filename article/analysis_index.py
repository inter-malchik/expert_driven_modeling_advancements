"""Compatibility facade for analysis registry helpers."""

from __future__ import annotations

from article.analysis_links import (
    analysis_slug_from_filenote,
    analysis_url,
    commentary_by_slug,
    commentary_for_slug,
)
from article.analysis_store import ANALYSIS_DIR, list_analysis_slugs, load_analysis
