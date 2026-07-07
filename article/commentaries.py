"""Literature commentaries imported from expert_guided_pinn_annotated.html."""

from __future__ import annotations

from typing import TypedDict


class CommentarySource(TypedDict, total=False):
    text: str
    url: str | None
    verified: bool


class Commentary(TypedDict):
    id: str
    section: str
    category: str
    category_label: str
    marker: str
    title: str
    body: str
    filenote: str
    tagline: str
    anchor_preview: str
    sources: list[CommentarySource]


COMMENTARIES: list[Commentary] = [
    {
        'id': 'n1',
        'section': '1. Introduction',
        'category': 'reliability',
        'category_label': 'LLM Reliability',
        'marker': '¶',
        'title': 'A named risk, now with a taxonomy',
        'body': 'Alansari & Luqman\'s faithfulness taxonomy — instruction, context, and logical inconsistency — explains exactly how "compliance with epidemic logic" hits 90–100% while "compliance with the comment" sits at 6–27% in the same runs. The Fig. 4c case (quadrupling a boundary weight when growth was requested) is instruction inconsistency with locally coherent ODE penalties; the 700-day outbreak blends context and logical inconsistency. The survey\'s own mitigations — Structured CoT for code, semantic-entropy filtering across samples, HalluTree-style claim decomposition — are three concrete builds of the "LLM-loss-semantic-checker" the paper names but doesn\'t implement.',
        'filenote': '08_alansari_survey_hallucination.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A published faithfulness taxonomy already explains how epidemic-logic can pass while comment-compliance fails.',
        "sources": [
            {
                "text": 'LLM Hallucination: A Comprehensive Survey — arXiv:2510.06265',
                "url": 'https://arxiv.org/abs/2510.06265',
                "verified": True,
            },
        ],
    },
    {
        'id': 'n2',
        'section': '1. Introduction',
        'category': 'epixai',
        'category_label': 'Epi-XAI Pipeline',
        'marker': '‖',
        'title': 'A training-time patch on top of a five-stage gap',
        'body': "Khalili & Wimmer's PRISMA review of 26 epidemiology+XAI studies proposes a six-stage pipeline — preprocessing, feature engineering, tuning, training, evaluation, explanation — and explicitly flags PINNs as absent from the reviewed literature, naming them for future work this paper is an early instance of. But nearly all of its expert intervention happens at one stage (training, via the loss penalty), leaving data preprocessing, NPI feature engineering, and uncertainty quantification untouched — consistent with the review's broader thesis that pipeline-stage omissions, not any single weak component, are what caps systems like this below deployment readiness.",
        'filenote': '05_towardsImprovedXaiBasedEpidemiologicalResearch.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A 26-study epi-XAI review flags PINNs as absent from the literature it surveyed — and names a six-stage pipeline this paper only touches at one stage.',
        "sources": [
            {
                "text": 'Khalili & Wimmer (2024), Towards Improved XAI-Based Epidemiological Research into the Next Potential Pandemic',
                "url": None,
                "verified": False,
            },
        ],
    },
    {
        'id': 'n3',
        'section': '1. Introduction',
        'category': 'architecture',
        'category_label': 'Agent Architecture',
        'marker': '‡',
        'title': 'Lab-in-the-loop: validate the trajectory, not the conjecture',
        'body': 'Möltner et al. build the same expert-comment-to-simulation-code loop for multibody dynamics and tested two validation strategies: the LLM judging its own generated code by conjecture (abandoned — "largely erroneous results, ... disconnect between the generation of the conjecture and the actual simulation model") versus running the actual simulation and having a separate LLM call judge the numerical trajectory ("significantly more reliable"). The PINN Customizer currently does the abandoned version — one LLM invents the loss weights and implicitly judges plausibility, with no trajectory audit before the expert sees the plot — exactly the gap that let the 700-day outbreak compile cleanly.',
        'filenote': '04_moeltner_lab_in_the_loop.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A near-identical loop for simulation code found that judging your own generated code by conjecture fails; judging the resulting trajectory works.',
        "sources": [
            {
                "text": 'Möltner et al. (2026), Creation, Evaluation and Self-Validation of Simulation Models with LLMs',
                "url": None,
                "verified": False,
            },
        ],
    },
    {
        'id': 'n4',
        'section': '2. Methodology',
        'category': 'evaluation',
        'category_label': 'Evaluation Epistemics',
        'marker': '§',
        'title': 'Naming the statistics already being done',
        'body': 'Lin\'s contextualist-centrism spectrum gives formal vocabulary for what this decomposition already does without naming it: $L_{data}$ is likelihood/frequentist pressure, the LLM-generated expert penalty is a subjective structural prior, and the epidemic-logic/MAE checks are frequentist filters on a process that is neither pure Bayesian nor pure frequentist. Read this way, edits that are "effectively random rather than logically justified" are Lin\'s bad-prior pathology in a nonparametric weight space — and the planned class-subclass templates are, in Lin\'s terms, a search for an admissible, coherent prior family.',
        'filenote': '12_lin_frequentist_or_bayesian.md',
        'tagline': 'Literature comparison',
        'anchor_preview': "This decomposition already is a statistical position — it just isn't named as one.",
        "sources": [
            {
                "text": 'Lin (2024), To Be a Frequentist or Bayesian?',
                "url": None,
                "verified": False,
            },
        ],
    },
    {
        'id': 'n5',
        'section': '2. Methodology',
        'category': 'architecture',
        'category_label': 'Agent Architecture',
        'marker': '‡',
        'title': 'Single-shot is the baseline this architecture was built to beat',
        'body': 'One prompt, one LLM call, a full code artifact in a single pass is exactly the "Single-Shot" configuration Yu et al. test as their weakest baseline for hardware codegen — and it fails all three of their test cases outright. Their working alternative — pseudocode → Python → C++ with a Coder/Verifier pair at each stage, plus a four-branch Reflection agent that can reopen the original instructions rather than just regenerate code — is a tested architecture for the exact gap this paper names but doesn\'t build. Their ablations (removing Understanding, Reflection, or progressive coding one at a time) are also the controlled experiment this paper\'s three-model comparison never runs: it can separate model from architecture; the PINN Customizer can\'t.',
        'filenote': '03_yu_2025_spec2rtl_agent.md',
        'tagline': 'Literature comparison',
        'anchor_preview': "This is the exact 'Single-Shot' configuration a hardware-codegen agent tested as its weakest baseline — and it failed every test case.",
        "sources": [
            {
                "text": 'Yu et al. (2025), Spec2RTL-Agent: Automated Hardware Code Generation from Complex Specifications',
                "url": None,
                "verified": False,
            },
        ],
    },
    {
        'id': 'n6',
        'section': '2.2. Hierarchical text classifier',
        'category': 'explanation',
        'category_label': 'Explanation Theory',
        'marker': '*',
        'title': "The expert already asks contrastive questions — the system doesn't ask back",
        'body': 'Miller\'s survey argues people explain contrastively — fact versus foil, "why P rather than Q" — and socially, not via full causal dumps. The paper\'s successful example ("after the peak there should be a sharper decline") is already exactly this structure, with Table A.2 targeting only the difference, not a full rewrite. The gap Miller predicts and the paper\'s own failures confirm: foils are often implicit, and when the Conversational Agent doesn\'t elicit one explicitly, the LLM guesses wrong — the peak-shift request that produced the 700-day outbreak.',
        'filenote': '13_explanationInArtificialIntelligence.md',
        'tagline': 'Literature comparison',
        'anchor_preview': "The paper's successful example is already a textbook contrastive explanation — the system just doesn't ask for the foil explicitly.",
        "sources": [
            {
                "text": 'Explanation in AI: Insights from the Social Sciences — doi:10.1016/j.artint.2018.07.007',
                "url": 'https://doi.org/10.1016/j.artint.2018.07.007',
                "verified": True,
            },
        ],
    },
    {
        'id': 'n7',
        'section': '2.2. Hierarchical text classifier',
        'category': 'formalization',
        'category_label': 'Formalization & Ontology',
        'marker': '†',
        'title': 'A content ontology without a representation ontology',
        'body': 'Gruber\'s 1993 Ontolingua work solved the identical translation problem three decades early — expressive declarative knowledge (KIF) into restricted executable targets (Loom, Epikit, KEE) — via idiom recognition into a canonical Frame Ontology, then deterministic back-end translators, with no step left to free generation. This paper built the first layer (a four-class comment hierarchy) but skipped the second: "add penalty to term2" is natural-language documentation, not a machine-readable idiom with typed operators and ranges — precisely why two different models can both "honor" the same rule and produce opposite forecasts (weakening vs. quadrupling the same boundary term).',
        'filenote': '11_gruber_ontolingua_portable_ontology.md',
        'tagline': 'Literature comparison',
        'anchor_preview': "An ontology architecture from 1993 solved this exact translation problem — with a canonical intermediate form this paper's rules skip.",
        "sources": [
            {
                "text": 'Gruber (1993), A Translation Approach to Portable Ontology Specifications',
                "url": None,
                "verified": False,
            },
        ],
    },
    {
        'id': 'n8',
        'section': '2.3. PINN Customizer',
        'category': 'reliability',
        'category_label': 'LLM Reliability',
        'marker': '¶',
        'title': 'The compiler catches the minority of errors',
        'body': 'Wang et al.\'s empirical study of HumanEval failures found that 84.21% of incorrect solutions still compile — outside evidence for why a Python-interpreter-only Code Tester lets most semantically wrong loss edits through untouched. Their taxonomy names failures this paper\'s own error list matches almost line for line: Wang et al.\'s «Garbage Code» category (unused variables/constants), «Constant Value Error» (literal numeric insertion, worse in larger models — matching Llama-70B\'s behavior), and errors needing multi-hunk repair, not single-line fixes. Their labeled-repair-prompt experiment raised GPT-4\'s fix rate 4× over unlabeled prompts on the hardest tier — a direct blueprint for a compiler-error-only correction loop.',
        'filenote': '02_wang_code_generation_errors.md',
        'tagline': 'Literature comparison',
        'anchor_preview': '84% of incorrect solutions in a benchmark study still compile — the compiler catches only a minority of the errors that matter.',
        "sources": [
            {
                "text": 'Wang et al. (2025), Towards Understanding the Characteristics of Code Generation Errors Made by LLMs',
                "url": None,
                "verified": False,
            },
        ],
    },
    {
        'id': 'n9',
        'section': '2.4. Evaluation Approach',
        'category': 'evaluation',
        'category_label': 'Evaluation Epistemics',
        'marker': '§',
        'title': 'Confirmation, not verification',
        'body': 'Oreskes et al.\'s classic argument — verification/validation of open natural-system models is logically impossible, only partial confirmation is available, and "a faulty model may appear to be correct" — reframes these four thresholds as confirmation heuristics, a more defensible stance than the abstract\'s language of "confirming feasibility." Multiple loss edits at temperature=1.0 producing visually similar curves with different physics is exactly Oreskes\'s non-uniqueness/underdetermination point, empirically demonstrated in the paper\'s own run-to-run variance.',
        'filenote': '06_oreskes_verification_validation.md',
        'tagline': 'Literature comparison',
        'anchor_preview': "Verification is the wrong goal for open natural-system models — and the paper's own multiple-loss-edits-same-plot pattern is exactly the underdetermination this predicts.",
        "sources": [
            {
                "text": 'Verification, Validation and Confirmation... — doi:10.1126/science.263.5147.641',
                "url": 'https://doi.org/10.1126/science.263.5147.641',
                "verified": True,
            },
        ],
    },
    {
        'id': 'n10',
        'section': '2.4. Evaluation Approach',
        'category': 'evaluation',
        'category_label': 'Evaluation Epistemics',
        'marker': '§',
        'title': 'A patch without an explanation is still soliloquy',
        'body': 'Chakraborti et al.\'s Model Reconciliation framework formalizes exactly what "compliance with the comment" is trying to measure informally: whether a plan — here, the modified forecast — is optimal in the human\'s updated mental model, scored against four named properties: completeness, conciseness, monotonicity, computability. Table A.2\'s "add penalty to term2, other components prohibited" is a Plan Patch Explanation in their terms — it names where to edit, not why that edit reconciles the expert\'s mental model with the PINN\'s, which is exactly why the 700-day outbreak stays inexplicable to the expert even after it compiles.',
        'filenote': '07_chakraborti_model_reconciliation.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A formal framework for exactly this kind of patch already exists, with four scoreable properties instead of a visual read.',
        "sources": [
            {
                "text": 'Plan Explanations as Model Reconciliation — arXiv:1701.08317',
                "url": 'https://arxiv.org/abs/1701.08317',
                "verified": True,
            },
        ],
    },
    {
        'id': 'n11',
        'section': '2.4. Evaluation Approach',
        'category': 'architecture',
        'category_label': 'Agent Architecture',
        'marker': '‡',
        'title': 'The small model was never given a fair fight',
        'body': 'Kreikemeyer et al. solve the same shape of problem — free text to formal DSL, for chemical reaction networks — and get a 7B model to 84.5% accuracy (vs. 99% for GPT-4o) using three tools Llama-3.1-8B never receives here: LoRA fine-tuning on a synthetic corpus, curated few-shot examples, and optional grammar-constrained decoding. Their own "raw" 8B baseline, given only good few-shot examples, reaches 72.5% — roughly twelve times the 6% reported here for the same size class. That reframes the 8B collapse from "a limit of scale" into an artifact of testing every model size with identical, unaided prompting.',
        'filenote': '01_kreikemeyer_2025_llm_reaction_networks.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A 7B model given LoRA fine-tuning, few-shot examples, and grammar-constrained decoding reached 84.5% on a structurally identical task — the small model here got none of those three tools.',
        "sources": [
            {
                "text": 'Kreikemeyer et al. (2025), Using (Not-So) Large Language Models to Generate Simulation Models in a Formal DSL',
                "url": None,
                "verified": False,
            },
        ],
    },
    {
        'id': 'n12',
        'section': '2.4. Evaluation Approach',
        'category': 'reliability',
        'category_label': 'LLM Reliability',
        'marker': '¶',
        'title': 'Prototyping at maximum entropy, deployed at low temperature',
        'body': 'Huang et al.\'s survey ties elevated sampling temperature directly to hallucination risk: more uniform token distributions increase tail-token sampling, exactly the mechanism behind the paper\'s own catalog of spurious variables and broken physics at T=1.0. Two of the survey\'s cited mitigations map onto data already produced at no extra cost: self-consistency scoring across the multiple T=1.0 samples per comment (currently discarded after one is shown to the expert), and LMvLM-style cross-examination — an examiner LLM questioning the generator — as a working instantiation of the paper\'s own proposed "LLM-expert-evaluator."',
        'filenote': '09_huang_survey_hallucination.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'Higher temperature is directly tied to hallucination risk — and the multiple samples this already produces are a free reward-model dataset, currently discarded.',
        "sources": [
            {
                "text": 'Huang et al. (2024), A Survey on Hallucination in Large Language Models',
                "url": None,
                "verified": False,
            },
        ],
    },
    {
        'id': 'n13',
        'section': '3.3. Working with the framework',
        'category': 'alignment',
        'category_label': 'Alignment / RLHF',
        'marker': '⁂',
        'title': "The reward-model dataset already exists — it's being discarded",
        'body': "InstructGPT's core finding is that a model bigger at pretraining but never aligned to instructions loses to a much smaller aligned one — a near match for DeepSeek-V3.1 (671B) topping out at 27% compliance while Ouyang et al.'s 1.3B aligned model beat 175B raw GPT-3. As a proposed extension (not a claim in either paper): two of the three ingredients their reward-model training needs already exist here — multiple candidate loss edits per comment (from T=1.0 sampling) and a three-level expert verdict that is a ready-made ordinal preference signal. The missing step would be saving every candidate and its verdict instead of keeping one and discarding the rest — turning 20-launch prototyping data into training data for a fine-tuned generator the paper does not yet have.",
        'filenote': '15_ouyang_2022_instructgpt.md',
        'tagline': 'Literature comparison (proposed extension)',
        'anchor_preview': 'This three-level rating, over multiple sampled candidates, is already two of the three ingredients a reward-model dataset needs.',
        "sources": [
            {
                "text": 'Training LMs to Follow Instructions (InstructGPT) — arXiv:2203.02155',
                "url": 'https://arxiv.org/abs/2203.02155',
                "verified": True,
            },
        ],
    },
    {
        'id': 'n14',
        'section': '4. Limitations and Future work',
        'category': 'formalization',
        'category_label': 'Formalization & Ontology',
        'marker': '†',
        'title': 'Before writing templates, test which representation wins',
        'body': "Pillay's controlled hyper-heuristic experiment found linear, sequential rule representations beat hierarchical, simultaneously-applied ones on 7 of 8 exam-timetabling benchmarks, and cost far less to search. Table A.2 declares flat, linear rules but hands the LLM free-form Python generation — full hierarchical expressiveness with none of the sequential structure Pillay's result favors. Before building the class-subclass templates already proposed as future work, Pillay's protocol argues for running the same linear-vs-hierarchical ablation on the paper's own 20 comments, rather than picking a representation by default.",
        'filenote': '10_burke_heuristic_combination_structure.md — filed under "Burke" in the corpus; the actual source is Pillay (2010)',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A controlled hyper-heuristic experiment found linear rule representations beat hierarchical ones on 7 of 8 benchmarks — this paper declares linear rules but hands the LLM full hierarchical freedom.',
        "sources": [
            {
                "text": 'Pillay (2010), An Empirical Study into the Structure of Heuristic Combinations in an EA Hyper-Heuristic for Examination Timetabling',
                "url": None,
                "verified": False,
            },
        ],
    },
    {
        'id': 'n15',
        'section': '4. Limitations and Future work',
        'category': 'explanation',
        'category_label': 'Explanation Theory',
        'marker': '*',
        'title': 'Evaluating for researchers, not for epidemiologists',
        'body': 'Miller\'s "inmates running the asylum" critique — that AI researchers build explanatory systems evaluated by researchers, not intended users — matches the MAE thresholds, n=20, T=1.0, and author-judged compliance here almost point for point. Broekens\' empirically supported finding that different action types need different explanations gives a concrete fix: type the reverse explanation by comment class ("because you cited containment timing") rather than showing only a code diff. Longo\'s physics-versus-biology argument reframes the whole exercise usefully: epidemic policy shifts reshape the effective phase space rather than adding noise inside a fixed SIRD manifold — a stronger, less apologetic reason expert intervention is necessary at all, not a workaround for a model that should otherwise stand alone.',
        'filenote': '14_bewareOfInmates_doYouGetIt_howFutureDepends.md — Miller, Broekens & Longo, read together',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A classic XAI critique argues researchers evaluate explanatory systems for themselves, not their intended users — and this evaluation setup matches that pattern closely.',
        "sources": [
            {
                "text": 'Miller et al., Beware of Inmates Running the Asylum',
                "url": None,
                "verified": False,
            },
            {
                "text": 'Broekens et al., Do You Get It? User-Evaluated Explainable BDI Agents',
                "url": None,
                "verified": False,
            },
            {
                "text": 'Longo, How the Future Depends on the Past and Rare Events in Systems of Life',
                "url": None,
                "verified": False,
            },
        ],
    },
]


def commentaries_by_section() -> dict[str, list[Commentary]]:
    grouped: dict[str, list[Commentary]] = {}
    for commentary in COMMENTARIES:
        grouped.setdefault(commentary["section"], []).append(commentary)
    return grouped


ANNOTATED_SECTIONS: list[str] = list(commentaries_by_section().keys())
