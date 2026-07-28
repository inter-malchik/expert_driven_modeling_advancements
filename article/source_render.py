"""HTML rendering helpers for commentary source lists."""

from __future__ import annotations

import html

from article.commentaries import CommentarySource
from article.source_registry import resolve_source_url


def render_sources_html(
    sources: list[CommentarySource],
    *,
    list_class: str = "paper-commentary-sources",
    link_class: str = "paper-commentary-source-link",
) -> str:
    if not sources:
        return ""

    items = []
    for source in sources:
        text = html.escape(source["text"])
        status = "verified" if source.get("verified") or resolve_source_url(source) else "pending"
        url = resolve_source_url(source)
        if url:
            link = html.escape(url)
            items.append(
                f'<li class="{status}"><a class="{link_class}" '
                f'href="{link}" target="_blank" rel="noopener">{text}</a></li>'
            )
        else:
            items.append(f'<li class="{status}">{text}</li>')
    return f'<ul class="{list_class}">{"".join(items)}</ul>'
