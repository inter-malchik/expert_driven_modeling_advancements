"""Compatibility facade for paper rendering modules."""

from __future__ import annotations

from article.commentary_render import CATEGORY_COLORS
from article.paper_body import render_body
from article.paper_figures import FIGURE_CAPTIONS, HALF_WIDTH_FIGURES
from article.paper_header import render_header
from article.paper_references import render_references
from article.section_ids import section_slug
