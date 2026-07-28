"""Recover commentary data files from local snapshots and analysis markdown.

This is a best-effort recovery utility for the data-only `commentaries_data`
layer when the directory was overwritten during local experimentation.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLE_ROOT = ROOT / "article"
DATA_ROOT = ARTICLE_ROOT / "commentaries_data"
ANALYSIS_DIR = ARTICLE_ROOT / "analysis"
SNAPSHOT_PATH = ARTICLE_ROOT / "context" / "card_drafts_snapshot.json"

SLUG_TO_ID = {
    "amgoud_2015_undercutting": "n17",
    "arioua_2015_explanatory_dialogues": "n18",
    "bisquert_2015_dual_process_argument": "n19",
    "cayrol_2015_bipolar_change": "n20",
    "abell_landscape_features_under_noise": "n16",
    "clark_deconstructing_big_valley": "n21",
    "daza_2016_basin_entropy": "n22",
    "dubois_2015_possibilistic_inconsistency": "n23",
    "eftimov_2019_edsc_statistical_comparison": "n24",
    "epstein_2008_why_model": "n25",
    "hadjimichael_1993_interactive_inductive": "n26",
    "halpern_pearl_2005_causes_and_explanations": "n27",
    "hayes_2017_policy_explanation": "n28",
    "hidalgo_2018_glucose_grammatical_evolution": "n29",
    "kerschke_2019_algorithm_selection_survey": "n30",
    "malan_2021_landscape_analysis_survey": "n31",
    "malan_gradient_walk_nn_landscapes": "n32",
    "malek_2009_multi_agent_collaboration": "n33",
    "mehdi_2015_compositional_forecasting": "n34",
    "merhej_2015_asp_rules_of_thumb": "n35",
    "miller_2020_contrastive_explanation": "n36",
    "noy_2001_ontology_development_101": "n37",
    "omahony_icon_algorithm_selection_challenge": "n38",
    "potyka_2015_priority_probabilistic_kb": "n39",
    "skvorc_2020_ela_problem_space": "n40",
    "steiner_2024_steering_wheel_crn": "n41",
    "studer_1998_knowledge_engineering": "n42",
    "tonda_2013_bnsl_interaction": "n43",
    "unpredictabilityAndComputationalIrreducibility": "n44",
    "walton_2010_dialogue_explanation": "n45",
    "weakEmergence": "n46",
    "wei_2024_dante_active_optimization": "n47",
    "zhang_2026_trm_complex_reasoning": "n48",
}

SOURCE_OVERRIDES = {
    "abell_landscape_features_under_noise": (
        "Scott and De Jong (2016), Landscape Features for Computationally Expensive Evaluation Functions: Revisiting the Problem of Noise",
        "https://doi.org/10.1007/978-3-319-45823-6_89",
    ),
    "clark_deconstructing_big_valley": (
        "Ochoa and Veerapen, 2016, *Deconstructing the Big Valley Search Space Hypothesis*",
        "https://doi.org/10.1007/978-3-319-30698-8_5",
    ),
    "malan_gradient_walk_nn_landscapes": (
        "Bosman et al. (2018), Progressive Gradient Walk for Neural Network Fitness Landscape Analysis",
        "https://dl.acm.org/doi/10.1145/3205651.3208247",
    ),
    "malek_2009_multi_agent_collaboration": (
        "Malek (2009), Global Optimization through Meta-Heuristic Collaboration in a Multi-Agent System",
        "https://www.seage.org/data/malek09specstudy.pdf",
    ),
    "omahony_icon_algorithm_selection_challenge": (
        "Kotthoff, Hurley, and O’Sullivan, 2017, *The ICON Challenge on Algorithm Selection*",
        "https://doi.org/10.1609/aimag.v38i2.2722",
    ),
    "unpredictabilityAndComputationalIrreducibility": (
        "Zwirn & Delahaye, Unpredictability and Computational Irreducibility",
        "https://arxiv.org/abs/1111.4121",
    ),
    "weakEmergence": (
        "Bedau, 1997, *Weak Emergence*",
        "https://doi.org/10.1111/0029-4624.31.s11.17",
    ),
}

SECTION_DEFAULTS = {
    "1. Introduction": ("architecture", "Architecture Note", "‡"),
    "2. Methodology": ("pathology", "Methodology Note", "Σ"),
    "2.1. Conversational Agent": ("formalization", "Dialog Design", "†"),
    "2.2. Hierarchical text classifier": ("formalization", "Classifier Design", "†"),
    "2.3. PINN Customizer": ("pathology", "PINN Customizer", "Σ"),
    "2.4. Evaluation Approach": ("evaluation", "Evaluation Protocol", "§"),
    "3.2. Code correctness": ("reliability", "Code Correctness", "¶"),
    "3.3. Working with the framework": ("explanation", "Workflow Design", "*"),
    "3.4. Framework performance": ("optimization", "Performance Diagnostics", "Ω"),
    "4. Limitations and Future work": ("architecture", "Future Architecture", "‡"),
    "5. Conclusion": ("evaluation", "Conclusion", "§"),
}

FRONTIER = {
    "n49": {
        "slug": "yu_2025_spec2rtl_agent",
        "section": "2.4. Evaluation Approach",
        "category": "architecture",
        "category_label": "Multi-Agent Loops",
        "marker": "‡",
        "title": "Spec2RTL: Generator-Checker-Reflection Loop",
        "tagline": "Literature comparison (multi-agent extension)",
        "anchor_preview": (
            "A staged Generator -> Verifier -> Reflection loop reduces semantic "
            "failures before the expensive PINN retraining step."
        ),
        "proposed_update": "Adopt a staged Generator -> Verifier -> Reflection workflow.",
        "update_details": (
            "Replace the single-shot Customizer call with a three-stage "
            "intermediate workflow: structured modification plan, constrained "
            "code synthesis, and semantic reflection that can reopen the "
            "instructions rather than only recompiling code."
        ),
        "sources": [
            {
                "text": (
                    "Yu et al. (2025), Spec2RTL-Agent: Automated Hardware Code "
                    "Generation from Complex Specifications"
                ),
                "url": "https://arxiv.org/abs/2506.13905",
            }
        ],
    },
    "n50": {
        "slug": "eshkofti_2025_stacked_residuals",
        "section": "4. Limitations and Future work",
        "category": "architecture",
        "category_label": "Residual Architecture",
        "marker": "‡",
        "title": "Stacked Residual PINNs for Stable Expert Edits",
        "tagline": "Literature comparison (robust architecture)",
        "anchor_preview": (
            "Stacked residual and sequential-correction PINNs stabilize "
            "expert-guided retraining under noisy or stiff loss edits."
        ),
        "proposed_update": "Introduce stacked residual and sequential-correction retraining.",
        "update_details": (
            "Use staged residual refinement with viscosity or smoothing schedules "
            "so each expert-guided loss edit is validated through stable "
            "intermediate trajectories before the final sharp solution is accepted."
        ),
        "sources": [
            {
                "text": (
                    "Eshkofti et al. (2025), Vanishing Stacked-Residual PINN for "
                    "State Reconstruction of Hyperbolic Systems"
                ),
                "url": "https://arxiv.org/abs/2503.14222",
            },
            {
                "text": (
                    "Chiu et al. (2026), Scale-PINN: Learning Efficient "
                    "Physics-Informed Neural Networks Through Sequential Correction"
                ),
                "url": "https://arxiv.org/abs/2602.19475",
            },
        ],
    },
    "n51": {
        "slug": "rathore_2024_loss_landscape",
        "section": "4. Limitations and Future work",
        "category": "optimization",
        "category_label": "Optimizer Hygiene",
        "marker": "Ω",
        "title": "Landscape Stiffness: Adam->L-BFGS as Optimizer Hygiene",
        "tagline": "Literature comparison (Hygiene)",
        "anchor_preview": (
            "The stiffness of PINN loss landscapes requires a transition from "
            "Adam to L-BFGS and specific activation functions to ensure global "
            "convergence."
        ),
        "proposed_update": (
            "Mandate Adam->L-BFGS hybrid training and prefer Softplus/Sine "
            "activations."
        ),
        "update_details": (
            "Two-phase schedule for every expert-guided retraining: Adam warm-up "
            "for basin entry, then L-BFGS for precision; log the optimizer switch "
            "and tolerances so optimization failure is not confused with model "
            "failure."
        ),
        "sources": [
            {
                "text": (
                    "Rathore et al. (2024), Challenges in Training PINNs: A Loss "
                    "Landscape Perspective"
                ),
                "url": "https://arxiv.org/abs/2402.01868",
            },
            {
                "text": (
                    "Dashtbayaz et al. (2024), Minimizing Residual Loss with Wide "
                    "Networks and Effective Activations"
                ),
                "url": "https://arxiv.org/abs/2405.01680",
            },
        ],
    },
    "n52": {
        "slug": "akazan_2025_risk_aware_pinn",
        "section": "2.4. Evaluation Approach",
        "category": "optimization",
        "category_label": "Risk-aware Optimization",
        "marker": "Σ",
        "title": "RRaPINN: Targeting Residual Tail Errors via CVaR",
        "tagline": "Literature comparison (Risk Control)",
        "anchor_preview": (
            "Transitioning from mean residuals to CVaR-based risk-aware "
            "optimization prevents localized failures that global MAE metrics miss."
        ),
        "proposed_update": (
            "Integrate CVaR and Residual-Quantile Adjustment into the loss function."
        ),
        "update_details": (
            "Replace standard mean residual minimization with CVaR-style tail "
            "control and residual-quantile weighting so expert-targeted local "
            "failures are not washed out by the global average."
        ),
        "sources": [
            {
                "text": (
                    "Akazan et al. (2025), RRaPINNs: Residual Risk-Aware Physics "
                    "Informed Neural Networks"
                ),
                "url": "https://arxiv.org/abs/2511.18515",
            },
            {
                "text": (
                    "Han et al. (2022), Residual-Quantile Adjustment for Adaptive "
                    "Training of Physics-informed Neural Network"
                ),
                "url": "https://arxiv.org/abs/2209.05315",
            },
        ],
    },
}

LEGACY_FILENOTES = {
    "n1": "article/analysis/alansari_survey_hallucination.md",
    "n2": "article/analysis/towardsImprovedXaiBasedEpidemiologicalResearch.md",
    "n3": "article/analysis/moeltner_lab_in_the_loop.md",
    "n4": "article/analysis/lin_frequentist_or_bayesian.md",
    "n5": "article/analysis/yu_2025_spec2rtl_agent.md",
    "n6": "article/analysis/explanationInArtificialIntelligence.md",
    "n7": "article/analysis/gruber_ontolingua_portable_ontology.md",
    "n8": "article/analysis/wang_code_generation_errors.md",
    "n9": "article/analysis/oreskes_verification_validation.md",
    "n10": "article/analysis/chakraborti_model_reconciliation.md",
    "n11": "article/analysis/kreikemeyer_2025_llm_reaction_networks.md",
    "n12": "article/analysis/huang_survey_hallucination.md",
    "n13": "article/analysis/ouyang_2022_instructgpt.md",
    "n14": "article/analysis/burke_heuristic_combination_structure.md",
    "n15": "article/analysis/bewareOfInmates_doYouGetIt_howFutureDepends.md",
}


def slugify_section(name: str) -> str:
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "misc"


def normalize_text(value: str) -> str:
    replacements = {
        "\x00": r"\0",
        "\x07": r"\a",
        "\x08": r"\b",
        "\x0b": r"\v",
        "\x0c": r"\f",
    }
    return "".join(replacements.get(char, char) for char in value)


def escape_text(value: str) -> str:
    return normalize_text(value).replace("\\", "\\\\").replace('"', '\\"')


def first_heading(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return path.stem.replace("_", " ")


def parse_source_links(path: Path) -> list[dict[str, str | bool | None]]:
    text = path.read_text(encoding="utf-8")
    links: list[dict[str, str | bool | None]] = []
    for line in text.splitlines()[:6]:
        if "Source links:" not in line and "Paper B" not in line:
            continue
        for label, url in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", line):
            links.append({"text": label, "url": url, "verified": True})
    return links


def first_body_paragraph(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", ">")):
            continue
        return stripped
    return ""


def render_commentary(item: dict) -> str:
    lines = ["+++"]
    for key in (
        "id",
        "section",
        "category",
        "category_label",
        "marker",
        "title",
        "filenote",
        "tagline",
        "anchor_preview",
    ):
        lines.append(f'{key} = "{escape_text(item[key])}"')
    for key in ("proposed_update", "update_details"):
        if item.get(key):
            lines.append(f'{key} = "{escape_text(item[key])}"')
    for source in item.get("sources", []):
        lines.append("")
        lines.append("[[sources]]")
        lines.append(f'text = "{escape_text(source["text"])}"')
        if source.get("url") is not None:
            lines.append(f'url = "{escape_text(source["url"])}"')
        lines.append(f'verified = {str(bool(source.get("verified", False))).lower()}')
    lines.append("+++")
    lines.append(normalize_text(item["body"]))
    lines.append("")
    return "\n".join(lines)


def write_commentary(item: dict) -> None:
    section_dir = DATA_ROOT / slugify_section(item["section"])
    section_dir.mkdir(parents=True, exist_ok=True)
    (section_dir / f'{item["id"]}.md').write_text(
        render_commentary(item),
        encoding="utf-8",
    )


def normalize_legacy_filenotes() -> int:
    updated = 0
    for path in DATA_ROOT.rglob("n*.md"):
        text = path.read_text(encoding="utf-8")
        for commentary_id, filenote in LEGACY_FILENOTES.items():
            if f'id = "{commentary_id}"' not in text:
                continue
            updated_text = re.sub(
                r'^filenote = ".*"$',
                f'filenote = "{filenote}"',
                text,
                flags=re.MULTILINE,
            )
            if updated_text != text:
                path.write_text(updated_text, encoding="utf-8")
                updated += 1
            break
    return updated


def main() -> None:
    snapshot = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
    snapshot_by_slug = {item["slug"]: item for item in snapshot}

    created_count = 0

    for slug, commentary_id in SLUG_TO_ID.items():
        snapshot_item = snapshot_by_slug[slug]
        section = snapshot_item["inferred_section"]
        category, category_label, marker = SECTION_DEFAULTS[section]
        analysis_path = ANALYSIS_DIR / f"{slug}.md"

        sources = parse_source_links(analysis_path)
        if not sources:
            text, url = SOURCE_OVERRIDES[slug]
            sources = [{"text": text, "url": url, "verified": True}]

        item = {
            "id": commentary_id,
            "section": section,
            "category": category,
            "category_label": category_label,
            "marker": marker,
            "title": first_heading(analysis_path),
            "body": snapshot_item["thesis"],
            "filenote": f"article/analysis/{slug}.md",
            "tagline": "Literature comparison",
            "anchor_preview": snapshot_item["anchor_text"],
            "sources": sources,
        }
        write_commentary(item)
        created_count += 1

    for commentary_id, frontier_item in FRONTIER.items():
        analysis_path = ANALYSIS_DIR / f'{frontier_item["slug"]}.md'
        item = {
            "id": commentary_id,
            "section": frontier_item["section"],
            "category": frontier_item["category"],
            "category_label": frontier_item["category_label"],
            "marker": frontier_item["marker"],
            "title": frontier_item["title"],
            "body": first_body_paragraph(analysis_path),
            "filenote": f'article/analysis/{frontier_item["slug"]}.md',
            "tagline": frontier_item["tagline"],
            "anchor_preview": frontier_item["anchor_preview"],
            "proposed_update": frontier_item["proposed_update"],
            "update_details": frontier_item["update_details"],
            "sources": [{**source, "verified": True} for source in frontier_item["sources"]],
        }
        write_commentary(item)
        created_count += 1

    normalized = normalize_legacy_filenotes()
    total_files = len(list(DATA_ROOT.rglob("*.md")))
    print(
        f"Recovered {created_count} commentary files; "
        f"normalized {normalized} legacy filenotes; total now {total_files}."
    )


if __name__ == "__main__":
    main()
