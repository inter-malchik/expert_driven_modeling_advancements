from __future__ import annotations

import streamlit as st

from article.app_shell import query_param, set_sidebar_visible, sync_sidebar_state
from article.analysis_view import render_analysis
from article.commentaries import COMMENTARIES, commentaries_by_section
from article.sections import render_body, render_header, render_references, section_slug
from article.styles import PAPER_CSS

st.set_page_config(
    page_title="Expert-guided forecasting of epidemic ARI incidence",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)


sidebar_visible = sync_sidebar_state()

st.markdown(f"<style>{PAPER_CSS}</style>", unsafe_allow_html=True)
if not sidebar_visible:
    st.markdown('<div id="sidebar-state-hidden" aria-hidden="true"></div>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="sidebar-show-bar">', unsafe_allow_html=True)
        if st.button("Show navigation", key="sidebar_show", help="Show the commentary sidebar"):
            set_sidebar_visible(True)
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

analysis_slug = query_param("analysis") or query_param("slug")
from_commentary = query_param("from")

has_commentaries = bool(COMMENTARIES)
if has_commentaries and not analysis_slug and sidebar_visible:
    with st.sidebar:
        st.header("Possibilities to advance the research")
        show_commentaries = st.toggle(
            "Show commentaries",
            value=True,
            help="Display literature commentaries above annotated sections.",
        )
        if show_commentaries:
            st.caption(f"{len(COMMENTARIES)} commentaries")
            for section, items in commentaries_by_section().items():
                st.markdown(
                    f'**<a href="#section-{section_slug(section)}">{section}</a>** '
                    f"({len(items)})",
                    unsafe_allow_html=True,
                )
                for commentary in items:
                    st.markdown(
                        f'&nbsp;&nbsp;• <a href="#commentary-{commentary["id"]}">'
                        f'{commentary["marker"]} {commentary["title"]}</a>',
                        unsafe_allow_html=True,
                    )
        st.divider()
        if st.button("Hide navigation", key="sidebar_hide", use_container_width=True):
            set_sidebar_visible(False)
            st.rerun()
else:
    show_commentaries = has_commentaries and sidebar_visible

if analysis_slug:
    render_analysis(slug=analysis_slug, from_commentary=from_commentary)
else:
    render_header()
    render_body(show_commentaries=show_commentaries)
    render_references()

    if st.query_params.get("dev") == "true":
        st.divider()
        st.info(
            "Это страница проекта Expert-Guided PINN. "
            "Функционал форума временно перенесен в `[TODO] persistence/forum_draft.py`."
        )
