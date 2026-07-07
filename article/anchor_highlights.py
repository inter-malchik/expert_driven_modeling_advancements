"""Highlight anchor passages in the article body."""

from __future__ import annotations

import html
import re

from article.commentaries import Commentary
from article.commentary_anchors import ANCHOR_TEXTS
from article.commentary_colors import palette_for


def _normalize_apostrophes(text: str) -> str:
    return (
        text.replace("’", "'")
        .replace("‘", "'")
        .replace("“", '"')
        .replace("”", '"')
        .replace("–", "–")
    )


def _find_anchor_span(body_html: str, anchor_text: str) -> tuple[int, int] | None:
    for candidate in (anchor_text, _normalize_apostrophes(anchor_text)):
        start = body_html.find(candidate)
        if start >= 0:
            return start, start + len(candidate)

    normalized_html = _normalize_apostrophes(body_html)
    normalized_anchor = _normalize_apostrophes(anchor_text)
    start = normalized_html.find(normalized_anchor)
    if start >= 0:
        return start, start + len(normalized_anchor)

    plain = re.sub(r"<[^>]+>", "", normalized_anchor)
    pattern = re.escape(plain)
    pattern = pattern.replace(r"\ ", r"\s+")
    match = re.search(pattern, normalized_html, flags=re.I | re.S)
    if match:
        return match.start(), match.end()
    return None


def inject_anchor_highlights(body_html: str, commentaries: list[Commentary]) -> str:
    spans: list[tuple[int, int, str, str]] = []

    for commentary in commentaries:
        commentary_id = commentary["id"]
        anchor_text = ANCHOR_TEXTS.get(commentary_id, "")
        if not anchor_text:
            continue
        found = _find_anchor_span(body_html, anchor_text)
        if not found:
            continue
        start, end = found
        spans.append((start, end, commentary_id, commentary["marker"]))

    spans.sort(key=lambda item: item[0], reverse=True)
    for start, end, commentary_id, marker in spans:
        palette = palette_for(commentary_id)
        original = body_html[start:end]
        wrapped = (
            f'<a class="paper-anchor paper-anchor--{commentary_id}" '
            f'id="anchor-{commentary_id}" href="#commentary-{commentary_id}" '
            f'style="--anchor-accent:{palette["accent"]};'
            f'--anchor-highlight:{palette["highlight"]};'
            f'--anchor-border:{palette["highlight_border"]};">'
            f"{original}"
            f'<sup class="paper-anchor-marker">{html.escape(marker)}</sup>'
            f"</a>"
        )
        body_html = body_html[:start] + wrapped + body_html[end:]

    return body_html
