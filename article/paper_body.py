"""Body rendering for the paper view, including commentary injection."""

from __future__ import annotations
import streamlit as st
import streamlit.components.v1 as components

from article.anchor_highlights import inject_anchor_highlights
from article.body_html import BODY_HTML
from article.commentaries import COMMENTARIES, commentaries_by_section, Commentary
from article.paper_figures import inject_figures
from article.paper_injection import inject_commentaries

_BROWSER_HOOKS = """
<script>
(function () {
  var root = window.parent && window.parent.document ? window.parent : window;

  function openTargetCommentary() {
    var hash = root.location.hash;
    if (!hash || hash.indexOf("#commentary-") !== 0) return;
    var target = root.document.querySelector(hash);
    if (target && target.tagName === "DETAILS") target.open = true;
  }

  function bindAnalysisLinks() {
    root.document.querySelectorAll("a.paper-analysis-link").forEach(function (link) {
      link.addEventListener("click", function (event) {
        event.preventDefault();
        var href = link.getAttribute("href") || "";
        var url = href.charAt(0) === "?" ? "/" + href : href;
        root.open(url, "_blank", "noopener,noreferrer");
      });
    });
  }

  function restoreHiddenState() {
    root.document.querySelectorAll(".paper-commentary").forEach(function (card) {
      var id = card.id.replace("commentary-", "");
      if (localStorage.getItem("hidden_card_" + id) === "true") {
        card.classList.add("is-hidden");
      }
    });
  }

  openTargetCommentary();
  restoreHiddenState();
  bindAnalysisLinks();
  root.addEventListener("hashchange", openTargetCommentary);
})();
</script>
"""
def render_with_commentaries(body_html: str, grouped: dict[str, list[Commentary]]) -> None:
    if not grouped:
        st.markdown(body_html, unsafe_allow_html=True)
        return

    html_with_commentaries = inject_commentaries(body_html, grouped)
    st.markdown(html_with_commentaries, unsafe_allow_html=True)


def render_body(*, show_commentaries: bool = True) -> None:
    body_html = inject_figures(BODY_HTML)
    if show_commentaries:
        body_html = inject_anchor_highlights(body_html, COMMENTARIES)
        render_with_commentaries(
            f'<div class="paper-shell"><div class="paper-body">{body_html}</div></div>',
            commentaries_by_section(),
        )
    else:
        st.markdown(
            f'<div class="paper-shell"><div class="paper-body">{body_html}</div></div>',
            unsafe_allow_html=True,
        )

    if show_commentaries:
        # Встраиваем JS-хуки в страницу через компонент HTML.
        components.html(_BROWSER_HOOKS, height=0)
