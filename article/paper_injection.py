"""Helpers that inject commentary and reference markup into paper HTML."""

from __future__ import annotations

import re

from article.commentaries import Commentary
from article.commentary_links import enrich_commentaries
from article.commentary_render import commentary_group_html
from article.section_ids import section_slug


def inject_commentaries(body_html: str, grouped: dict[str, list[Commentary]]) -> str:
    if not grouped:
        return body_html

    for heading, items in grouped.items():
        if not items:
            continue

        enriched_items = enrich_commentaries(items)
        commentary_block = commentary_group_html(enriched_items)
        section_id = section_slug(heading)

        for tag in ("h2", "h3"):
            pattern = rf"<{tag}>{re.escape(heading)}</{tag}>"
            replacement = (
                f'<div class="paper-section-block" id="section-{section_id}">'
                f"{commentary_block}"
                f"<{tag}>{heading}</{tag}>"
                f"</div>"
            )
            body_html, count = re.subn(pattern, lambda _match: replacement, body_html, count=1)
            if count:
                break

    return body_html


def linkify_urls(html_text: str) -> str:
    return re.sub(
        r"(https?://[^\s<]+)",
        r'<a href="\1">\1</a>',
        html_text,
    )


def format_references(html_text: str) -> str:
    entries = re.findall(r"<p>(.*?)</p>", html_text, flags=re.S)
    formatted = []
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
        formatted.append(f'<div class="paper-ref-entry">{linkify_urls(entry)}</div>')
    return "\n".join(formatted)
