"""Paper URLs for commentary citations."""

from __future__ import annotations

import html
import re

from article.commentaries import Commentary, CommentarySource

# Exact source text -> canonical paper URL.
SOURCE_URLS: dict[str, str] = {
    "Khalili & Wimmer (2024), Towards Improved XAI-Based Epidemiological Research into the Next Potential Pandemic": "https://doi.org/10.3390/life14070783",
    "Möltner et al. (2026), Creation, Evaluation and Self-Validation of Simulation Models with LLMs": "https://doi.org/10.1016/j.neucom.2025.132030",
    "Lin (2024), To Be a Frequentist or Bayesian?": "https://doi.org/10.1162/99608f92.9a53b923",
    "Yu et al. (2025), Spec2RTL-Agent: Automated Hardware Code Generation from Complex Specifications": "https://arxiv.org/abs/2506.13905",
    "Gruber (1993), A Translation Approach to Portable Ontology Specifications": "https://doi.org/10.1006/knac.1993.1008",
    "Wang et al. (2025), Towards Understanding the Characteristics of Code Generation Errors Made by LLMs": "https://arxiv.org/abs/2406.08731",
    "Kreikemeyer et al. (2025), Using (Not-So) Large Language Models to Generate Simulation Models in a Formal DSL": "https://arxiv.org/abs/2503.01675",
    "Huang et al. (2024), A Survey on Hallucination in Large Language Models": "https://doi.org/10.1145/3703155",
    "Pillay (2010), An Empirical Study into the Structure of Heuristic Combinations in an EA Hyper-Heuristic for Examination Timetabling": "https://doi.org/10.1145/1899503.1899531",
    "Miller et al., Beware of Inmates Running the Asylum": "https://arxiv.org/abs/1712.00547",
    "Broekens et al., Do You Get It? User-Evaluated Explainable BDI Agents": "https://doi.org/10.1007/978-3-642-16178-0_5",
    "Longo, How the Future Depends on the Past and Rare Events in Systems of Life": "https://doi.org/10.1007/s10699-017-9535-x",
    # Already linked in HTML with shortened labels.
    "LLM Hallucination: A Comprehensive Survey — arXiv:2510.06265": "https://arxiv.org/abs/2510.06265",
    "Explanation in AI: Insights from the Social Sciences — doi:10.1016/j.artint.2018.07.007": "https://doi.org/10.1016/j.artint.2018.07.007",
    "Verification, Validation and Confirmation... — doi:10.1126/science.263.5147.641": "https://doi.org/10.1126/science.263.5147.641",
    "Plan Explanations as Model Reconciliation — arXiv:1701.08317": "https://arxiv.org/abs/1701.08317",
    "Training LMs to Follow Instructions (InstructGPT) — arXiv:2203.02155": "https://arxiv.org/abs/2203.02155",
}


def resolve_source_url(source: CommentarySource) -> str | None:
    if source.get("url"):
        return source["url"]

    text = source["text"]
    if text in SOURCE_URLS:
        return SOURCE_URLS[text]

    arxiv_match = re.search(r"arXiv:([\d.]+)", text, re.I)
    if arxiv_match:
        return f"https://arxiv.org/abs/{arxiv_match.group(1)}"

    doi_match = re.search(r"doi:([\d./]+)", text, re.I)
    if doi_match:
        return f"https://doi.org/{doi_match.group(1)}"

    return None


def enrich_commentary_sources(commentary: Commentary) -> Commentary:
    enriched_sources: list[CommentarySource] = []
    for source in commentary["sources"]:
        url = resolve_source_url(source)
        enriched_sources.append(
            {
                **source,
                "url": url,
                "verified": bool(source.get("verified") or url),
            }
        )
    return {**commentary, "sources": enriched_sources}


def enrich_commentaries(commentaries: list[Commentary]) -> list[Commentary]:
    return [enrich_commentary_sources(item) for item in commentaries]


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
