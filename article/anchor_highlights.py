"""Highlight anchor passages in the article body."""

from __future__ import annotations

import html
from typing import TypedDict

from article.commentaries import Commentary
from article.commentary_anchors import ANCHOR_TEXTS
from article.commentary_colors import palette_for
from article.anchor_matching import find_anchor_span


class AnchorMatch(TypedDict):
    start: int
    end: int
    commentary_id: str
    marker: str


class AnchorCluster(TypedDict):
    start: int
    end: int
    matches: list[AnchorMatch]


def _cluster_matches(matches: list[AnchorMatch]) -> list[AnchorCluster]:
    if not matches:
        return []

    ordered = sorted(matches, key=lambda item: (item["start"], item["end"]))
    clusters: list[AnchorCluster] = []

    for match in ordered:
        if not clusters or match["start"] >= clusters[-1]["end"]:
            clusters.append(
                {
                    "start": match["start"],
                    "end": match["end"],
                    "matches": [match],
                }
            )
            continue

        clusters[-1]["end"] = max(clusters[-1]["end"], match["end"])
        clusters[-1]["matches"].append(match)

    return clusters


def inject_anchor_highlights(body_html: str, commentaries: list[Commentary]) -> str:
    matches: list[AnchorMatch] = []

    for commentary in commentaries:
        commentary_id = commentary["id"]
        anchor_text = ANCHOR_TEXTS.get(commentary_id, "")
        if not anchor_text:
            continue
        found = find_anchor_span(body_html, anchor_text)
        if not found:
            continue
        start, end = found
        matches.append(
            {
                "start": start,
                "end": end,
                "commentary_id": commentary_id,
                "marker": commentary["marker"],
            }
        )

    clusters = _cluster_matches(matches)
    clusters.sort(key=lambda item: item["start"], reverse=True)

    for cluster in clusters:
        primary_id = cluster["matches"][0]["commentary_id"]
        palette = palette_for(primary_id)
        original = body_html[cluster["start"] : cluster["end"]]
        anchor_targets = "".join(
            f'<span id="anchor-{match["commentary_id"]}" class="paper-anchor-target" aria-hidden="true"></span>'
            for match in cluster["matches"]
        )
        marker_links = "".join(
            f'<a class="paper-anchor-marker-link" href="#commentary-{match["commentary_id"]}">'
            f'{html.escape(match["marker"])}</a>'
            for match in cluster["matches"]
        )
        wrapped = (
            f'<span class="paper-anchor paper-anchor--{primary_id}" '
            f'style="--anchor-accent:{palette["accent"]};'
            f'--anchor-highlight:{palette["highlight"]};'
            f'--anchor-border:{palette["highlight_border"]};">'
            f"{anchor_targets}"
            f"{original}"
            f'<sup class="paper-anchor-marker">{marker_links}</sup>'
            f"</span>"
        )
        body_html = body_html[: cluster["start"]] + wrapped + body_html[cluster["end"] :]

    return body_html
