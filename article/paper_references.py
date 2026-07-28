"""References rendering helpers for the paper view."""

from __future__ import annotations

import streamlit as st

from article.paper_injection import format_references
from article.references_html import REFERENCES_HTML


def render_references() -> None:
    references = format_references(REFERENCES_HTML)
    st.markdown(
        f'<div class="paper-shell"><div class="paper-references"><h2>References</h2>{references}</div></div>',
        unsafe_allow_html=True,
    )
