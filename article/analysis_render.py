"""Rendering helpers for analysis pages."""

from __future__ import annotations

import html

import streamlit as st

from article.analysis_links import (
    analysis_slug_from_filenote,
    analysis_url,
    commentary_by_slug,
    commentary_for_slug,
)
from article.analysis_store import load_analysis
from article.commentaries import COMMENTARIES
from article.commentary_links import render_sources_html
from article.comparison_prose import prepare_comparison_markdown
from article.styles import ANALYSIS_CSS


def render_analysis(*, slug: str | None, from_commentary: str | None) -> None:
    st.markdown(f"<style>{ANALYSIS_CSS}</style>", unsafe_allow_html=True)

    if not slug:
        st.markdown('<div class="analysis-shell">', unsafe_allow_html=True)
        st.title("Full comparisons")
        st.write("Open a comparison from a commentary’s “Read full comparison” link.")
        for commentary in COMMENTARIES:
            item_slug = analysis_slug_from_filenote(commentary["filenote"])
            if not item_slug:
                continue
            label = html.escape(f'{commentary["marker"]} {commentary["title"]}')
            href = analysis_url(item_slug, commentary_id=commentary["id"])
            st.markdown(
                f'- <a class="paper-analysis-link" href="{href}" '
                f'target="_blank" rel="noopener noreferrer">{label}</a>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)
        return

    try:
        _title, markdown = load_analysis(slug)
    except FileNotFoundError:
        st.error(f"Comparison not found: {slug}")
        return

    markdown = prepare_comparison_markdown(markdown)

    linked_commentary = commentary_for_slug(slug)
    nav_bits = ['<div class="analysis-nav">', '<a href="/">← Back to paper</a>']
    if from_commentary:
        nav_bits.append(
            f' · <a href="/#commentary-{html.escape(from_commentary)}">'
            f"← Back to commentary</a>"
        )
    elif linked_commentary:
        nav_bits.append(
            f' · <a href="/#commentary-{linked_commentary["id"]}">'
            f'← Commentary: {html.escape(linked_commentary["title"])}</a>'
        )
    nav_bits.append("</div>")
    st.markdown("".join(nav_bits), unsafe_allow_html=True)

    commentary = commentary_by_slug(slug)
    if commentary and commentary["sources"]:
        sources_html = render_sources_html(
            commentary["sources"],
            list_class="analysis-sources",
            link_class="analysis-source-link",
        )
        st.markdown(
            f'<div class="analysis-sources-wrap">'
            f'<p class="analysis-sources-label">Original article(s)</p>'
            f"{sources_html}"
            f"</div>",
            unsafe_allow_html=True,
        )

    st.markdown('<div class="analysis-shell">', unsafe_allow_html=True)
    st.markdown(markdown)
    st.markdown("</div>", unsafe_allow_html=True)
