"""Helpers for Streamlit query params and sidebar state."""

from __future__ import annotations

import streamlit as st


def query_param(name: str) -> str | None:
    value = st.query_params.get(name)
    if value is None:
        return None
    if isinstance(value, list):
        return value[0] if value else None
    return value or None


def sync_sidebar_state() -> bool:
    sidebar_qp = query_param("sidebar")
    if sidebar_qp in {"hidden", "0", "false"}:
        st.session_state.sidebar_visible = False
    elif sidebar_qp in {"visible", "1", "true"}:
        st.session_state.sidebar_visible = True
    elif "sidebar_visible" not in st.session_state:
        st.session_state.sidebar_visible = True
    return bool(st.session_state.sidebar_visible)


def set_sidebar_visible(visible: bool) -> None:
    st.session_state.sidebar_visible = visible
    if visible:
        st.query_params.pop("sidebar", None)
    else:
        st.query_params["sidebar"] = "hidden"
