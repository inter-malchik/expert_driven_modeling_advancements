"""Search helpers for matching commentary anchor text inside article HTML."""

from __future__ import annotations

import re


def normalize_apostrophes(text: str) -> str:
    return (
        text.replace("’", "'")
        .replace("‘", "'")
        .replace("“", '"')
        .replace("”", '"')
        .replace("–", "–")
    )


def find_anchor_span(body_html: str, anchor_text: str) -> tuple[int, int] | None:
    for candidate in (anchor_text, normalize_apostrophes(anchor_text)):
        start = body_html.find(candidate)
        if start >= 0:
            return start, start + len(candidate)

    normalized_html = normalize_apostrophes(body_html)
    normalized_anchor = normalize_apostrophes(anchor_text)
    start = normalized_html.find(normalized_anchor)
    if start >= 0:
        return start, start + len(normalized_anchor)

    plain = re.sub(r"<[^>]+>", "", normalized_anchor)
    pattern = re.escape(plain).replace(r"\ ", r"\s+")
    match = re.search(pattern, normalized_html, flags=re.I | re.S)
    if match:
        return match.start(), match.end()
    return None
