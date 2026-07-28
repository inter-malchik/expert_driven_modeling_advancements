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
    def render_math(match: re.Match[str]) -> str:
        tex = match.group(1)
        tex = tex.replace(r"\(", "").replace(r"\)", "")
        tex = re.sub(r"\\text\{([^{}]+)\}", r"\1", tex)
        tex = re.sub(r"\\boldsymbol\{([^{}]+)\}", r"\1", tex)

        # Support the most common inline TeX used in commentary bodies.
        replacements = {
            r"\leq": "≤",
            r"\le": "≤",
            r"\geq": "≥",
            r"\ge": "≥",
            r"\neq": "≠",
            r"\times": "×",
            r"\cdot": "·",
            r"\sim": "∼",
            r"\infty": "∞",
            r"\alpha": "α",
            r"\beta": "β",
            r"\gamma": "γ",
            r"\theta": "θ",
            r"\lambda": "λ",
            r"\epsilon": "ε",
            r"\varepsilon": "ε",
        }
        for source, target in replacements.items():
            tex = tex.replace(source, target)

        tex = re.sub(r"_\{([^{}]+)\}", r"<sub>\1</sub>", tex)
        tex = re.sub(r"\^\{([^{}]+)\}", r"<sup>\1</sup>", tex)
        tex = re.sub(r"_([A-Za-z0-9])", r"<sub>\1</sub>", tex)
        tex = re.sub(r"\^([A-Za-z0-9])", r"<sup>\1</sup>", tex)
        tex = tex.replace("{", "").replace("}", "")
        return f'<span class="paper-commentary-math">{tex}</span>'

    escaped = html.escape(text)
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        escaped,
    )
    escaped = re.sub(r"\$([^$]+)\$", render_math, escaped)
    escaped = re.sub(r"\\\((.+?)\\\)", render_math, escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    return escaped


def commentary_body_html(body: str) -> str:
    lines = body.strip().splitlines()
    if not lines:
        return ""

    rendered: list[str] = []
    list_stack: list[dict[str, int | bool | str]] = []

    def close_lists_to(indent: int) -> None:
        while list_stack and int(list_stack[-1]["indent"]) >= indent:
            current = list_stack.pop()
            if current["li_open"]:
                rendered.append("</li>")
            rendered.append(f'</{current["tag"]}>')

    def special_line(raw_line: str) -> bool:
        stripped = raw_line.strip()
        return bool(
            not stripped
            or stripped.startswith(">")
            or stripped.startswith("#")
            or re.match(r"(\d+[.)]|[-*])\s+", stripped)
        )

    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped:
            i += 1
            continue

        indent = len(raw) - len(raw.lstrip(" "))
        heading_match = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading_match:
            close_lists_to(0)
            level = len(heading_match.group(1))
            text = _format_inline_markdown(heading_match.group(2).strip())
            rendered.append(f'<h{level} class="paper-commentary-heading">{text}</h{level}>')
            i += 1
            continue

        list_match = re.match(r"^(\d+)[.)]\s+(.*)$", stripped)
        list_tag = "ol"
        item_text = ""
        if list_match:
            item_text = list_match.group(2).strip()
        else:
            bullet_match = re.match(r"^[-*]\s+(.*)$", stripped)
            if bullet_match:
                list_tag = "ul"
                item_text = bullet_match.group(1).strip()

        if item_text:
            while list_stack and indent < int(list_stack[-1]["indent"]):
                current = list_stack.pop()
                if current["li_open"]:
                    rendered.append("</li>")
                rendered.append(f'</{current["tag"]}>')
            if list_stack and indent == int(list_stack[-1]["indent"]) and list_tag != list_stack[-1]["tag"]:
                close_lists_to(indent)
            if not list_stack or indent > int(list_stack[-1]["indent"]) or list_tag != list_stack[-1]["tag"]:
                rendered.append(f'<{list_tag} class="paper-commentary-list paper-commentary-list--{list_tag}">')
                list_stack.append({"tag": list_tag, "indent": indent, "li_open": False})
            current = list_stack[-1]
            if current["li_open"]:
                rendered.append("</li>")
            rendered.append("<li>")
            rendered.append(_format_inline_markdown(item_text))
            current["li_open"] = True
            i += 1
            continue

        if stripped.startswith(">"):
            quote_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_lines.append(lines[i].strip()[1:].strip())
                i += 1
            quote_html = "<br>".join(_format_inline_markdown(line) for line in quote_lines if line)
            block = f'<blockquote><p>{quote_html}</p></blockquote>'
            if list_stack and indent > int(list_stack[-1]["indent"]) and list_stack[-1]["li_open"]:
                rendered.append(block)
            else:
                close_lists_to(0)
                rendered.append(block)
            continue

        paragraph_lines = [stripped]
        i += 1
        while i < len(lines) and lines[i].strip() and not special_line(lines[i]):
            paragraph_lines.append(lines[i].strip())
            i += 1
        paragraph_html = "<br>".join(_format_inline_markdown(line) for line in paragraph_lines)
        block = f"<p>{paragraph_html}</p>"
        if list_stack and indent > int(list_stack[-1]["indent"]) and list_stack[-1]["li_open"]:
            rendered.append(block)
        else:
            close_lists_to(0)
            rendered.append(block)

    close_lists_to(0)
    return "".join(rendered)


def _split_sources_evidence(body: str) -> tuple[str, str]:
    match = re.search(r"(?mi)^\s*##\s+Sources\s*&\s*Evidence\s*$", body)
    if not match:
        return body.strip(), ""
    main_body = body[: match.start()].strip()
    evidence_body = body[match.end() :].strip()
    return main_body, evidence_body


def _score_stars(score: int) -> str:
    safe_score = max(1, min(5, score))
    return "★" * safe_score + "☆" * (5 - safe_score)


def _card_type_badge(commentary: Commentary) -> str:
    actionability = commentary.get("relevance_actionability")
    if commentary.get("proposed_update") or (isinstance(actionability, int) and actionability >= 4):
        return '<span class="paper-commentary-type" title="Practical card">⚙️</span>'
    return '<span class="paper-commentary-type" title="Analytical card">📚</span>'


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
    type_badge_html = _card_type_badge(commentary)

    main_body, evidence_body = _split_sources_evidence(commentary.get("body", ""))
    body_html = commentary_body_html(main_body)
    evidence_markdown_html = commentary_body_html(evidence_body) if evidence_body else ""

    proposed_update = commentary.get("proposed_update")
    update_details = commentary.get("update_details")
    update_html = ""
    if proposed_update:
        update_details_html = ""
        if update_details:
            update_details_html = (
                f'<span class="paper-commentary-update-details"> '
                f'{html.escape(update_details)}</span>'
            )
        update_html = (
            f'<div class="paper-commentary-update-box">'
            f'<span class="paper-commentary-update-label">Proposed update:</span>'
            f'<span class="paper-commentary-update-text">{html.escape(proposed_update)}</span>'
            f"{update_details_html}"
            f"</div>"
        )

    sources_html = ""
    source_parts: list[str] = []
    if commentary["sources"]:
        source_parts.append(render_sources_html(commentary["sources"]))
    if evidence_markdown_html:
        source_parts.append(
            f'<div class="paper-commentary-sources-markdown">{evidence_markdown_html}</div>'
        )
    if source_parts:
        sources_html = (
            f'<details class="paper-commentary-sources-details">'
            f'<summary class="paper-commentary-sources-summary">Sources & Evidence</summary>'
            f'<div class="paper-commentary-sources-panel">{"".join(source_parts)}</div>'
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

    return (
        f'<details class="paper-commentary paper-commentary--{commentary_id}" '
        f'id="commentary-{commentary_id}" style="{commentary_style(commentary_id)}">'
        f'<summary class="paper-commentary-summary">'
        f'<div class="paper-commentary-head">'
        f'<span class="paper-commentary-marker">{marker}</span>'
        f"{type_badge_html}"
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
        f"{body_html}"
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
