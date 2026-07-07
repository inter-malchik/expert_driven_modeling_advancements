from __future__ import annotations

import base64
import html
import re
from pathlib import Path

import streamlit as st

from article.analysis_index import analysis_slug_from_filenote, analysis_url
from article.anchor_highlights import inject_anchor_highlights
from article.body_html import BODY_HTML
from article.commentaries import COMMENTARIES, Commentary, commentaries_by_section
from article.commentary_colors import palette_for
from article.commentary_links import enrich_commentaries, render_sources_html
from article.references_html import REFERENCES_HTML

FIGURES_DIR = Path(__file__).resolve().parent.parent / "assets" / "figures"

HALF_WIDTH_FIGURES = {"FIG1", "FIG3"}

FIGURE_CAPTIONS = {
    "FIG1": (
        "fig1.png",
        "<strong>Fig. 1.</strong> Schematic of Expert-Guided PINN. The expert enters a comment "
        "that will help them correctly structure the conversational agent. Next, a class and "
        "subclass are defined for the comment, for which rules for generating modifications to "
        "the current loss function will be defined. After generating the loss function and "
        "checking its compilability, the PINN training process begins. The user then receives "
        "a new prediction, which they can then decide whether it satisfies their comment or not.",
    ),
    "FIG2": (
        "fig2.png",
        "<strong>Fig. 2.</strong> Workflow of the PINN Customizer: (a) a prompt containing a task, "
        "comment, and rules, (b) scheme of PINNs, (c) PINN Customizer, (d) Code tester, "
        "(e) User interface.",
    ),
    "FIG3": (
        "fig3.png",
        "<strong>Fig. 3.</strong> (a) Comparative Performance of LLMs in loss function generation "
        "tasks (temperature=1.0, 20 launches); (b) Comparison of TSED Score for LLMs.",
    ),
    "FIG4": (
        "fig4.png",
        "<strong>Fig. 4.</strong> (a) Example of a successful result: a sharper decline in the "
        "number of cases after the peak, as requested by the expert; (b) Example of an unsuccessful "
        "result: unrealistically long epidemic duration when the expert requests a 7–10 day shift "
        "of the peak; (c) Example of an ambiguous result: stabilization of case counts instead of "
        "continued growth for two additional weeks, and an atypically flat epidemic curve.",
    ),
    "FIG5": (
        "fig5.png",
        "<strong>Fig. 5.</strong> LLMs Performance Comparison (temperature=1.0). Evaluated on: "
        "(a) Matching training data, (b) Forecast has changed, (c) Compliance with the epidemic "
        "logic, (d) Compliance with the comment.",
    ),
    "FIGA6": (
        "figA6.png",
        "<strong>Fig. A.6.</strong> Hierarchical Structure of Expert Comment Classes and Subclasses.",
    ),
    "FIGA7": (
        "figA7.png",
        "<strong>Fig. A.7.</strong> User navigation pathway.",
    ),
}


def _figure_data_uri(filename: str) -> str:
    encoded = base64.b64encode((FIGURES_DIR / filename).read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def _figure_label(caption: str) -> str:
    match = re.search(r"<strong>Fig\.\s*([^<]+)</strong>", caption)
    if match:
        return f"Fig. {match.group(1).strip().rstrip('.')}"
    return "Figure"


def _figure_html(marker: str) -> str:
    filename, caption = FIGURE_CAPTIONS[marker]
    label = html.escape(_figure_label(caption))
    figure_id = marker.lower().replace("fig", "figure-")
    show_label = label.replace("Fig.", "fig.", 1)
    width_class = " paper-figure--half-width" if marker in HALF_WIDTH_FIGURES else ""
    return (
        f'<figure class="paper-figure{width_class}" id="{figure_id}">'
        f'<details class="paper-figure-details">'
        f'<summary class="paper-figure-summary">'
        f'<span class="paper-figure-show-label">Show {show_label}</span>'
        f'<span class="paper-figure-caption">{caption}</span>'
        f"</summary>"
        f'<div class="paper-figure-image">'
        f'<img src="{_figure_data_uri(filename)}" alt="{html.escape(filename)}" />'
        f"</div>"
        f"</details>"
        f"</figure>"
    )


def section_slug(heading: str) -> str:
    return _slugify(heading)


def _slugify(heading: str) -> str:
    slug = heading.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


CATEGORY_COLORS = {
    "reliability": "#6B4271",
    "architecture": "#2E6E8E",
    "alignment": "#A6772C",
    "formalization": "#45527A",
    "evaluation": "#2F6B62",
    "explanation": "#6B6B2C",
    "epixai": "#8A5A3F",
}


def _commentary_style(commentary_id: str) -> str:
    palette = palette_for(commentary_id)
    return (
        f"--commentary-accent:{palette['accent']};"
        f"--commentary-bg:{palette['bg']};"
        f"--commentary-border:{palette['border']};"
        f"--commentary-highlight:{palette['highlight']};"
    )


def _commentary_html(commentary: Commentary) -> str:
    commentary_id = commentary["id"]
    marker = html.escape(commentary["marker"])
    title = html.escape(commentary["title"])
    category_label = html.escape(commentary["category_label"])
    body = html.escape(commentary["body"]).replace("\n\n", "</p><p>")
    tagline = html.escape(commentary["tagline"])
    anchor_preview = html.escape(commentary["anchor_preview"])

    sources_html = ""
    if commentary["sources"]:
        sources_html = render_sources_html(commentary["sources"])

    filenote_html = ""
    analysis_slug = analysis_slug_from_filenote(commentary["filenote"])
    if analysis_slug:
        link = html.escape(
            analysis_url(analysis_slug, commentary_id=commentary["id"])
        )
        filenote_html = (
            f'<p class="paper-commentary-analysis-link">'
            f'<a class="paper-analysis-link" href="{link}" '
            f'target="_blank" rel="noopener noreferrer">Read full comparison</a>'
            f"</p>"
        )
    preview_html = (
        f'<p class="paper-commentary-quote">{anchor_preview}</p>'
        f'<p class="paper-commentary-anchor-link">'
        f'<a href="#anchor-{commentary_id}">Linked passage in text</a>'
        f"</p>"
        if anchor_preview
        else ""
    )

    return (
        f'<details class="paper-commentary paper-commentary--{commentary_id}" '
        f'id="commentary-{commentary_id}" style="{_commentary_style(commentary_id)}">'
        f'<summary class="paper-commentary-summary">'
        f'<div class="paper-commentary-head">'
        f'<span class="paper-commentary-marker">{marker}</span>'
        f'<span class="paper-commentary-label">Commentary</span>'
        f'<span class="paper-commentary-category">{category_label}</span>'
        f"</div>"
        f'<p class="paper-commentary-title"><strong>{title}</strong></p>'
        f"</summary>"
        f'<div class="paper-commentary-body">'
        f"{preview_html}"
        f"<p>{body}</p>"
        f"{filenote_html}"
        f"{sources_html}"
        f'<p class="paper-commentary-tagline">{tagline}</p>'
        f"</div>"
        f"</details>"
    )


def _commentary_group_html(section: str, items: list[Commentary]) -> str:
    blocks = "".join(_commentary_html(item) for item in items)
    return f'<div class="paper-commentary-group">{blocks}</div>'


def _inject_commentaries(body_html: str, grouped: dict[str, list[Commentary]]) -> str:
    if not grouped:
        return body_html

    for heading, items in grouped.items():
        if not items:
            continue

        enriched_items = enrich_commentaries(items)
        commentary_block = _commentary_group_html(heading, enriched_items)
        section_id = _slugify(heading)

        for tag in ("h2", "h3"):
            pattern = rf"<{tag}>{re.escape(heading)}</{tag}>"
            replacement = (
                f'<div class="paper-section-block" id="section-{section_id}">'
                f"{commentary_block}"
                f"<{tag}>{heading}</{tag}>"
                f"</div>"
            )
            body_html, count = re.subn(pattern, replacement, body_html, count=1)
            if count:
                break

    return body_html


def _inject_figures(html: str) -> str:
    for marker in FIGURE_CAPTIONS:
        html = html.replace(f"<!--{marker}-->", _figure_html(marker))
    return html


def _linkify_urls(html: str) -> str:
    return re.sub(
        r"(https?://[^\s<]+)",
        r'<a href="\1">\1</a>',
        html,
    )


def _format_references(html: str) -> str:
    entries = re.findall(r"<p>(.*?)</p>", html, flags=re.S)
    formatted = []
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
        formatted.append(
            f'<div class="paper-ref-entry">{_linkify_urls(entry)}</div>'
        )
    return "\n".join(formatted)


def render_header() -> None:
    st.markdown(
        """
<div class="paper-shell">
<div class="paper-banner">
  <div>
    <p class="paper-meta"><strong>Contents lists available at ScienceDirect</strong></p>
    <p class="paper-journal-title">Expert Systems With Applications</p>
    <p class="paper-meta"><strong>journal homepage:</strong> <a href="https://www.elsevier.com/locate/eswa">www.elsevier.com/locate/eswa</a></p>
  </div>
  <div class="paper-volume">Expert Systems With Applications 315 (2026) 131730</div>
</div>

<p class="paper-title">Expert-guided forecasting of epidemic ARI incidence based on physics-informed neural networks and large language models</p>

<p class="paper-authors">
<strong>Dinara Gindullina</strong><sup>a</sup>,
<strong>Mark Lazutov</strong><sup>a</sup>,
<strong>Kirill Stolyarov</strong><sup>b</sup>,
<strong>Daria Danilenko</strong><sup>b</sup>,
<strong>Vasiliy Leonenko</strong><sup>a,b,*</sup>
</p>

<p class="paper-affiliations">
<sup>a</sup> <em>ITMO University, Kronverksky Pr. 49, Saint Petersburg, 197101, Russia</em><br>
<sup>b</sup> <em>Smorodintsev Research Institute for Influenza, St. Prof. Popova 15/17, Saint Petersburg, 197022, Russia</em>
</p>

<hr class="paper-rule" />

<div class="paper-columns">
<div>
<p class="paper-section-label">ARTICLE INFO</p>
<p class="paper-keywords"><em>Keywords:</em><br>
influenza<br>
SARS-CoV-2<br>
predictive modeling<br>
LLM<br>
PINN
</p>
</div>
<div>
<p class="paper-section-label">ABSTRACT</p>
<p class="paper-abstract">
This paper presents an agent-based AI system that uses large-scale language models (LLMs) to dynamically adapt physically-informed neural networks (PINNs) based on high-quality expert judgment. Our system enables interactive refinement of epidemiological forecasts by translating unstructured expert feedback into structured modifications of the loss function, eliminating the need for prior mathematical formalization. Experimental results confirm the fundamental feasibility of this approach, demonstrating a success rate of 25-27% for the best models and providing a compelling proof-of-concept for using LLMs as core components of interactive decision support systems. This work represents a step toward building robust expert-led forecasting systems for public health problems, while simultaneously highlighting the need to develop more rigorous control mechanisms to ensure full robustness. The code of our system is available at <a href="https://github.com/vnleonenko/Epi_PINN_LLM">https://github.com/vnleonenko/Epi_PINN_LLM</a>.
</p>
</div>
</div>

<hr class="paper-rule" />

<div class="paper-footer-meta">
<p><strong>Corresponding author.</strong> Smorodintsev Research Institute for Influenza, St. Prof. Popova 15/17, Saint Petersburg, 197022, Russia.</p>
<p>E-mail addresses: <a href="mailto:mark.lazutov@gmail.com">mark.lazutov@gmail.com</a> (M. Lazutov), <a href="mailto:vasiliy.leonenko@gmail.com">vasiliy.leonenko@gmail.com</a> (V. Leonenko).</p>
<p>Received 12 December 2025; Received in revised form 2 March 2026; Accepted 3 March 2026</p>
<p>Available online 4 March 2026</p>
<p><a href="https://doi.org/10.1016/j.eswa.2026.131730">https://doi.org/10.1016/j.eswa.2026.131730</a></p>
<p>0957-4174/© 2026 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.</p>
</div>
</div>
        """,
        unsafe_allow_html=True,
    )


def render_body(*, show_commentaries: bool = True) -> None:
    body_html = _inject_figures(BODY_HTML)
    if show_commentaries:
        body_html = inject_anchor_highlights(body_html, COMMENTARIES)
        body_html = _inject_commentaries(body_html, commentaries_by_section())
    st.markdown(
        f'<div class="paper-shell"><div class="paper-body">{body_html}</div></div>',
        unsafe_allow_html=True,
    )
    if show_commentaries:
        st.components.v1.html(
            """
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

  openTargetCommentary();
  bindAnalysisLinks();
  root.addEventListener("hashchange", openTargetCommentary);
})();
</script>
            """,
            height=0,
        )


def render_references() -> None:
    references_html = _format_references(REFERENCES_HTML)
    st.markdown(
        f"""
<div class="paper-shell">
<div class="paper-references">
<h2>References</h2>
{references_html}
</div>
</div>
        """,
        unsafe_allow_html=True,
    )
