"""HTML rendering helpers for commentary cards."""

from __future__ import annotations

import html
import re

from article.analysis_links import analysis_slug_from_filenote, analysis_url
from article.commentaries import Commentary
from article.commentary_colors import palette_for
from article.commentary_links import render_sources_html

CATEGORY_COLORS = {
    "reliability": "#6B4271",
    "architecture": "#2E6E8E",
    "alignment": "#A6772C",
    "formalization": "#45527A",
    "evaluation": "#2F6B62",
    "explanation": "#6B6B2C",
    "epixai": "#8A5A3F",
    "optimization": "#2E8B57",
    "pathology": "#B22222",
    "argumentation": "#4E6B3F",
}

RELEVANCE_WEIGHTS = {
    "Method Fit": 0.40,
    "Transferability": 0.25,
    "Actionability": 0.15,
    "Expansion Value": 0.20,
}


def commentary_style(commentary_id: str) -> str:
    palette = palette_for(commentary_id)
    return (
        f"--commentary-accent:{palette['accent']};"
        f"--commentary-bg:{palette['bg']};"
        f"--commentary-border:{palette['border']};"
        f"--commentary-highlight:{palette['highlight']};"
    )


def _format_inline_markdown(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    return escaped


def commentary_body_html(body: str) -> str:
    paragraphs = [chunk.strip() for chunk in re.split(r"\n\s*\n", body.strip()) if chunk.strip()]
    if not paragraphs:
        return ""
    rendered = []
    for paragraph in paragraphs:
        lines = "<br>".join(_format_inline_markdown(line.strip()) for line in paragraph.splitlines() if line.strip())
        rendered.append(f"<p>{lines}</p>")
    return "".join(rendered)


def _score_stars(score: int) -> str:
    safe_score = max(1, min(5, score))
    return "★" * safe_score + "☆" * (5 - safe_score)


def _relevance_scores(commentary: Commentary) -> dict[str, int] | None:
    keys = {
        "Method Fit": "relevance_method_fit",
        "Transferability": "relevance_transferability",
        "Actionability": "relevance_actionability",
        "Expansion Value": "relevance_expansion_value",
    }
    scores: dict[str, int] = {}
    for label, key in keys.items():
        value = commentary.get(key)
        if not isinstance(value, int):
            return None
        scores[label] = max(1, min(5, value))
    return scores


def _weighted_relevance_basis(scores: dict[str, int]) -> float:
    return sum(scores[label] * weight for label, weight in RELEVANCE_WEIGHTS.items())


def _relevance_assessment(scores: dict[str, int]) -> str:
    method_fit = scores["Method Fit"]
    transferability = scores["Transferability"]
    actionability = scores["Actionability"]
    expansion_value = scores["Expansion Value"]

    clauses: list[str] = []
    if method_fit >= 5:
        clauses.append("This claim is tightly coupled to Dinara's methodological core rather than to a peripheral framing issue.")
    elif method_fit >= 4:
        clauses.append("This claim addresses the methodology of Paper A directly enough to matter beyond background commentary.")
    else:
        clauses.append("This claim has a real methodological link, but it does not anchor itself in the core of the pipeline strongly enough to feel indispensable.")

    if transferability >= 5:
        clauses.append("The transfer path into Paper A is unusually direct and needs little interpretive bridging.")
    elif transferability >= 4:
        clauses.append("The transfer into Paper A is concrete and can plausibly be turned into a design move or evaluation change.")
    else:
        clauses.append("The bridge is plausible, but it still needs an extra adaptation layer before it becomes a clean methodological import.")

    if actionability >= 4:
        clauses.append("It also points toward a next step that is concrete enough to guide implementation or experimental redesign.")
    elif actionability == 3:
        clauses.append("It suggests a usable direction, but the next step still needs additional operationalization.")
    else:
        clauses.append("Its practical next step remains under-specified, which limits immediate leverage.")

    if expansion_value >= 5:
        clauses.append("Expansion value is especially high because the claim opens a larger future design space for the system.")
    elif expansion_value >= 4:
        clauses.append("It expands the future system in a meaningful way instead of only sharpening the current critique.")
    else:
        clauses.append("Its expansion value is present, but comparatively modest.")

    return " ".join(clauses)


def _relevance_verdict(scores: dict[str, int], final_score: int) -> tuple[str, str]:
    penalties: list[str] = []
    if scores["Method Fit"] < 5:
        penalties.append("it is not fully central to the methodological core")
    if scores["Transferability"] < 5:
        penalties.append("the transfer still requires some bridging work")
    if scores["Actionability"] < 4:
        penalties.append("the next step is not yet operational enough")
    if scores["Expansion Value"] < 5:
        penalties.append("its expansion payoff is strong but not maximal")

    if final_score >= 5 and not penalties:
        return (
            "Why 5/5",
            "It combines methodological centrality, credible transfer, actionable follow-up, and strong expansion value with no major constraint under the current rubric.",
        )

    if not penalties:
        penalties.append("editorial caution keeps it below the maximum")

    verdict = penalties[0].capitalize()
    if len(penalties) > 1:
        verdict += "; " + "; ".join(penalties[1:]) + "."
    else:
        verdict += "."
    return ("Why not 5/5", verdict)


def _relevance_html(commentary: Commentary) -> tuple[str, str]:
    final_score = commentary.get("relevance_score")
    if not isinstance(final_score, int):
        return "", ""
    final_score = max(1, min(5, final_score))
    scores = _relevance_scores(commentary)
    if scores is None:
        return "", ""

    stars = _score_stars(final_score)
    weighted_basis = _weighted_relevance_basis(scores)
    assessment = html.escape(_relevance_assessment(scores))
    verdict_title, verdict_text = _relevance_verdict(scores, final_score)

    summary_html = (
        f'<span class="paper-commentary-relevance-summary" '
        f'title="Overall relevance">{stars} {final_score}/5</span>'
    )

    items_html = "".join(
        f'<p class="paper-commentary-relevance-item"><strong>{html.escape(label)} '
        f'({int(RELEVANCE_WEIGHTS[label] * 100)}%)</strong>: {score}/5</p>'
        for label, score in scores.items()
    )
    grading_html = (
        f'<details class="paper-commentary-sources-details paper-commentary-relevance-details">'
        f'<summary class="paper-commentary-sources-summary">Relevance Grading</summary>'
        f'<div class="paper-commentary-relevance-box">'
        f'<p class="paper-commentary-relevance-overall"><strong>Overall relevance:</strong> '
        f'{stars} {final_score}/5 <span class="paper-commentary-relevance-basis">'
        f'(Weighted basis: {weighted_basis:.2f}/5)</span></p>'
        f'<div class="paper-commentary-relevance-metrics">{items_html}</div>'
        f'<p class="paper-commentary-relevance-text"><strong>Assessment:</strong> {assessment}</p>'
        f'<p class="paper-commentary-relevance-text"><strong>{html.escape(verdict_title)}:</strong> '
        f'{html.escape(verdict_text)}</p>'
        f"</div>"
        f"</details>"
    )
    return summary_html, grading_html


def commentary_html(commentary: Commentary) -> str:
    commentary_id = commentary["id"]
    marker = html.escape(commentary["marker"])
    title = html.escape(commentary["title"])
    category_label = html.escape(commentary["category_label"])
    anchor_preview = html.escape(commentary["anchor_preview"])
    relevance_summary_html, relevance_grading_html = _relevance_html(commentary)

    proposed_update = commentary.get("proposed_update")
    update_details = commentary.get("update_details")
    update_html = ""
    if proposed_update:
        help_icon = ""
        if update_details:
            help_icon = (
                f'<span class="paper-commentary-help-icon">?'
                f'<span class="paper-commentary-tooltip">{html.escape(update_details)}</span>'
                f"</span>"
            )
        update_html = (
            f'<div class="paper-commentary-update-box">'
            f'<span class="paper-commentary-update-label">Proposed update:</span>'
            f'<span class="paper-commentary-update-text">{html.escape(proposed_update)}</span>'
            f"{help_icon}"
            f"</div>"
        )

    sources_html = ""
    if commentary["sources"]:
        inner_sources = render_sources_html(commentary["sources"])
        sources_html = (
            f'<details class="paper-commentary-sources-details">'
            f'<summary class="paper-commentary-sources-summary">Sources & Evidence</summary>'
            f"{inner_sources}"
            f"</details>"
        )

    filenote_html = ""
    analysis_slug = analysis_slug_from_filenote(commentary["filenote"])
    if analysis_slug:
        link = html.escape(analysis_url(analysis_slug, commentary_id=commentary["id"]))
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
    # Вместо немедленного рендера тела комментария в HTML вставляем плейсхолдер.
    # Он будет заменён на Markdown через st.markdown на этапе финального рендера,
    # чтобы корректно отработал парсер формул ($...$) и Markdown.
    body_placeholder = f"__COMMENTARY_BODY_{commentary_id}__"

    return (
        f'<details class="paper-commentary paper-commentary--{commentary_id}" '
        f'id="commentary-{commentary_id}" style="{commentary_style(commentary_id)}">'
        f'<summary class="paper-commentary-summary">'
        f'<div class="paper-commentary-head">'
        f'<span class="paper-commentary-marker">{marker}</span>'
        f'<span class="paper-commentary-label">Comparative Claim <span class="paper-commentary-id">#{commentary_id}</span></span>'
        f"{relevance_summary_html}"
        f'<span class="paper-commentary-category">{category_label}</span>'
        f'<button class="paper-commentary-hidden-toggle" title="Toggle hidden" '
        f'onclick="event.preventDefault(); event.stopPropagation(); '
        f'const card = this.closest(\'.paper-commentary\'); const isHidden = card.classList.toggle(\'is-hidden\'); localStorage.setItem(\'hidden_card_\' + \'{commentary_id}\', isHidden);">✕</button>'
        f"</div>"
        f'<p class="paper-commentary-title"><strong>{title}</strong></p>'
        f"</summary>"
        f'<div class="paper-commentary-body">'
        f"{preview_html}"
        f"{body_placeholder}"
        f"{update_html}"
        f"{filenote_html}"
        f"{sources_html}"
        f"{relevance_grading_html}"
        f"</div>"
        f"</details>"
    )


def commentary_group_html(items: list[Commentary]) -> str:
    blocks = "".join(commentary_html(item) for item in items)
    return f'<div class="paper-commentary-group">{blocks}</div>'
