"""Canonical URLs and source enrichment helpers for commentary citations."""

from __future__ import annotations

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
    "LLM Hallucination: A Comprehensive Survey — arXiv:2510.06265": "https://arxiv.org/abs/2510.06265",
    "Explanation in AI: Insights from the Social Sciences — doi:10.1016/j.artint.2018.07.007": "https://doi.org/10.1016/j.artint.2018.07.007",
    "Verification, Validation and Confirmation... — doi:10.1126/science.263.5147.641": "https://doi.org/10.1126/science.263.5147.641",
    "Plan Explanations as Model Reconciliation — arXiv:1701.08317": "https://arxiv.org/abs/1701.08317",
    "Training LMs to Follow Instructions (InstructGPT) — arXiv:2203.02155": "https://arxiv.org/abs/2203.02155",
    "Ma et al. (2023). Eureka: Human-Level Reward Design via Coding Large Language Models.": "https://arxiv.org/abs/2310.12931",
    "Zwirn & Delahaye, Unpredictability and Computational Irreducibility": "https://arxiv.org/abs/1111.4121",
    "Scott and De Jong (2016), Landscape Features for Computationally Expensive Evaluation Functions: Revisiting the Problem of Noise": "https://doi.org/10.1007/978-3-319-45823-6_89",
    "Ochoa and Veerapen, 2016, *Deconstructing the Big Valley Search Space Hypothesis*": "https://doi.org/10.1007/978-3-319-30698-8_5",
    "Kotthoff, Hurley, and O’Sullivan, 2017, *The ICON Challenge on Algorithm Selection*": "https://doi.org/10.1609/aimag.v38i2.2722",
    "Akazan et al. (2025), RRaPINNs: Residual Risk-Aware Physics Informed Neural Networks": "https://arxiv.org/abs/2511.18515",
    "Han et al. (2022), Residual-Quantile Adjustment for Adaptive Training of Physics-informed Neural Network": "https://arxiv.org/abs/2209.05315",
    "Malan et al. (gradient), Walk nn landscapes": "https://dl.acm.org/doi/10.1145/3205651.3208247",
    "Bedau, 1997, *Weak Emergence*": "https://doi.org/10.1111/0029-4624.31.s11.17",
    "Wu et al. (2026), Exdiff: a modular and explainable framework combining network simulation and graph neural networks for diffusion modeling": "https://doi.org/10.1007/s13278-025-01556-2",
    "Steiner et al. (2026), On Integrating Resilience and Human Oversight into LLM-Assisted Modeling Workflows for Digital Twins": "https://arxiv.org/abs/2603.25898",
    "Malek et al. (2009), MAS with Generator and Adviser is ready": "https://www.seage.org/data/malek09specstudy.pdf",
    "Dashtbayaz et al. (2024), Minimizing Residual Loss with Wide Networks and Effective Activations": "https://arxiv.org/abs/2405.01680",
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
