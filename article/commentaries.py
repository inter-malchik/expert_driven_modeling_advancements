"""Literature commentaries imported from expert_guided_pinn_annotated.html."""

from __future__ import annotations

from typing import TypedDict, NotRequired


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
    proposed_update: NotRequired[str]
    update_details: NotRequired[str]


COMMENTARIES: list[Commentary] = [
    {
        'id': 'n1',
        'section': '1. Introduction',
        'category': 'reliability',
        'category_label': 'LLM Reliability',
        'marker': '¶',
        'title': 'A named risk, now with a taxonomy',
        'body': 'Alansari & Luqman\'s faithfulness taxonomy — instruction, context, and logical inconsistency — explains exactly how "compliance with epidemic logic" hits 90–100% while "compliance with the comment" sits at 6–27% in the same runs. The Fig. 4c case (quadrupling a boundary weight when growth was requested) is instruction inconsistency with locally coherent ODE penalties; the 700-day outbreak blends context and logical inconsistency. The survey\'s own mitigations — Structured CoT for code, semantic-entropy filtering across samples, HalluTree-style claim decomposition — are three concrete builds of the "LLM-loss-semantic-checker" the paper names but doesn\'t implement.',
        'filenote': 'alansari_survey_hallucination.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A published faithfulness taxonomy already explains how epidemic-logic can pass while comment-compliance fails.',
        'proposed_update': 'Apply faithfulness taxonomy for error classification.',
        'update_details': 'Classify LLM failures using Alansari & Luqman\'s categories (instruction, context, logical). Use this taxonomy to refine the Code Tester, targeting "Constant Value Errors" and "Garbage Code" specifically in the verification stage.',
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
        'filenote': 'towardsImprovedXaiBasedEpidemiologicalResearch.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A 26-study epi-XAI review flags PINNs as absent from the literature it surveyed — and names a six-stage pipeline this paper only touches at one stage.',
        'proposed_update': 'Expand expert intervention across the full epi-XAI pipeline.',
        'update_details': 'Extend expert-guided adjustments beyond training-time loss penalties to include data preprocessing and feature engineering. This addresses the six-stage gap identified by Khalili & Wimmer, improving deployment readiness.',
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
        'filenote': 'moeltner_lab_in_the_loop.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A near-identical loop for simulation code found that judging your own generated code by conjecture fails; judging the resulting trajectory works.',
        'proposed_update': 'Implement trajectory-based numerical validation.',
        'update_details': 'Instead of letting the LLM judge its own code "by conjecture," run the simulation and have a separate specialized LLM call (the "Adviser") evaluate the resulting numerical trajectory for epidemiological plausibility.',
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
        'filenote': 'lin_frequentist_or_bayesian.md',
        'tagline': 'Literature comparison',
        'anchor_preview': "This decomposition already is a statistical position — it just isn't named as one.",
        'proposed_update': 'Adopt a formal contextualist-centrism statistical framework.',
        'update_details': 'Reframe PINN loss components ($L_{data}$ vs. $L_{phys}$) as a mix of frequentist likelihoods and subjective structural priors. Use this formal vocabulary to guide the search for an admissible and coherent prior family for expert interventions.',
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
        'filenote': 'yu_2025_spec2rtl_agent.md',
        'tagline': 'Literature comparison',
        'anchor_preview': "This is the exact 'Single-Shot' configuration a hardware-codegen agent tested as its weakest baseline — and it failed every test case.",
        'proposed_update': 'Replace single-shot generation with a multi-stage Coder/Verifier pair.',
        'update_details': 'Move away from one-prompt pass. Implement a progressive architecture: pseudocode → Python → PINN loss, with Reflection agents at each stage to verify against original expert instructions, as proven effective in hardware codegen.',
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
        'filenote': 'explanationInArtificialIntelligence.md',
        'tagline': 'Literature comparison',
        'anchor_preview': "The paper's successful example is already a textbook contrastive explanation — the system just doesn't ask for the foil explicitly.",
        'proposed_update': 'Elicit explicit foils for contrastive reasoning.',
        'update_details': 'Modify the Conversational Agent to explicitly ask experts for "foils" (why P rather than Q). This enables contrastive explanation as defined by Miller, reducing the likelihood of LLMs guessing the intended forecast shift incorrectly.',
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
        'filenote': 'gruber_ontolingua_portable_ontology.md',
        'tagline': 'Literature comparison',
        'anchor_preview': "An ontology architecture from 1993 solved this exact translation problem — with a canonical intermediate form this paper's rules skip.",
        'proposed_update': 'Implement a canonical Frame Ontology for deterministic translation.',
        'update_details': 'Introduce a machine-readable intermediate representation between natural language comments and executable code. Use typed operators and idiom recognition to ensure deterministic translation, eliminating "interpretation" variance between models.',
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
        'filenote': 'wang_code_generation_errors.md',
        'tagline': 'Literature comparison',
        'anchor_preview': '84% of incorrect solutions in a benchmark study still compile — the compiler catches only a minority of the errors that matter.',
        'proposed_update': 'Enhance the Code Tester with semantic-entropy filtering.',
        'update_details': 'Supplement simple compilation checks with semantic-entropy analysis to detect "Garbage Code" and "Constant Value Errors." Use labeled-repair prompts for iterative correction when semantic mismatches are detected.',
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
        'filenote': 'oreskes_verification_validation.md',
        'tagline': 'Literature comparison',
        'anchor_preview': "Verification is the wrong goal for open natural-system models — and the paper's own multiple-loss-edits-same-plot pattern is exactly the underdetermination this predicts.",
        'proposed_update': 'Shift from "feasibility proof" to "confirmation heuristics."',
        'update_details': 'Position the Expert-Guided PINN as an instrument for "disciplining political dialogue" (Epstein) rather than a truth-machine. Acknowledge and document the non-uniqueness of loss edits that produce similar forecasts.',
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
        'filenote': 'chakraborti_model_reconciliation.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A formal framework for exactly this kind of patch already exists, with four scoreable properties instead of a visual read.',
        'proposed_update': 'Score modifications against Model Reconciliation properties.',
        'update_details': 'Evaluate all PINN patches against Chakraborti\'s four properties: completeness, conciseness, monotonicity, and computability. This ensures the expert understands *why* an edit reconciles their mental model with the model\'s output.',
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
        'filenote': 'kreikemeyer_2025_llm_reaction_networks.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A 7B model given LoRA fine-tuning, few-shot examples, and grammar-constrained decoding reached 84.5% on a structurally identical task — the small model here got none of those three tools.',
        'proposed_update': 'Fine-tune small models (Llama-8B) for DSL generation.',
        'update_details': 'Apply LoRA fine-tuning on a synthetic dataset of expert-comment-to-DSL pairs. Supplement this with grammar-constrained decoding to ensure that even small models achieve high accuracy in generating valid PINN loss modifications.',
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
        'filenote': 'huang_survey_hallucination.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'Higher temperature is directly tied to hallucination risk — and the multiple samples this already produces are a free reward-model dataset, currently discarded.',
        'proposed_update': 'Implement self-consistency scoring and cross-examination.',
        'update_details': 'Reduce sampling temperature for deployment. Use self-consistency scoring across multiple T=1.0 samples during development to filter out low-probability hallucinations, and introduce an examiner LLM to critique the generator\'s output.',
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
        'filenote': 'ouyang_2022_instructgpt.md',
        'tagline': 'Literature comparison (proposed extension)',
        'anchor_preview': 'This three-level rating, over multiple sampled candidates, is already two of the three ingredients a reward-model dataset needs.',
        'proposed_update': 'Utilize expert feedback for RLHF-based alignment.',
        'update_details': 'Save all candidate modifications and their associated expert verdicts. Use this data as an ordinal preference signal to train a reward model, aligning the generator more closely with expert intent via Reinforcement Learning from Human Feedback (RLHF).',
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
        'filenote': 'burke_heuristic_combination_structure.md — filed under "Burke" in the corpus; the actual source is Pillay (2010)',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A controlled hyper-heuristic experiment found linear rule representations beat hierarchical ones on 7 of 8 benchmarks — this paper declares linear rules but hands the LLM full hierarchical freedom.',
        'proposed_update': 'Test linear vs. hierarchical rule representations.',
        'update_details': 'Conduct ablation studies to determine if linear, sequential rule representations (as favored by Pillay\'s benchmarks) improve reliability over the current hierarchical free-form Python generation for epidemic loss modifications.',
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
        'filenote': 'bewareOfInmates_doYouGetIt_howFutureDepends.md — Miller, Broekens & Longo, read together',
        'tagline': 'Literature comparison',
        'anchor_preview': 'A classic XAI critique argues researchers evaluate explanatory systems for themselves, not their intended users — and this evaluation setup matches that pattern closely.',
        'proposed_update': 'Redesign evaluation around epidemiologist user needs.',
        'update_details': 'Move beyond researcher-judged compliance. Implement explanation types based on action categories (e.g., "because you cited containment timing") and use epidemiologist-driven validation to ensure the system meets actual public health decision-making requirements.',
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
    {
        'id': 'n16',
        'section': '2.3. PINN Customizer',
        'category': 'pathology',
        'category_label': 'Loss Landscape Pathology',
        'marker': 'Σ',
        'title': 'Features under noise',
        'body': 'Paper A (Gindullina et al., «Expert-guided forecasting of epidemic ARI incidence based on physics-informed neural networks and large language models») evaluates success of loss modifications against four qualitative criteria with MAE thresholds of 700 and 1100, chosen empirically, and against subjective compliance with the comment at n=20 and temperature=1.0. Each iteration includes expensive PINN retraining, and the authors do not separate retraining noise from the effect of the LLM edit.',
        'filenote': 'abell_landscape_features_under_noise.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Scott and De Jong, 2016, «Landscape Features for Computationally Expensive Evaluation Functions: Revisiting the Problem of Noise»',
                "url": None,
                "verified": False,
            }
        ],
    },
    {
        'id': 'n17',
        'section': '2.2. Hierarchical text classifier',
        'category': 'argumentation',
        'category_label': 'Argumentation Theory',
        'marker': '⊗',
        'title': 'Undercutting',
        'body': 'Gindullina et al. (hereafter **Paper A**) ship Appendix A / Table A.2 as soft English “add penalty…” guidelines that the LLM may ignore while still compiling. Documented failure modes include unused constants, literal numeric insertion, and a Fig. 4b case where a peak-shift comment weakened a terminal boundary condition and produced a 700+ day outbreak.',
        'filenote': 'amgoud_2015_undercutting.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Amgoud et al. (2015), Undercutting',
                "url": 'https://doi.org/10.1007/978-3-319-23540-0_18',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n18',
        'section': '4. Limitations and Future work',
        'category': 'argumentation',
        'category_label': 'Argumentation Theory',
        'marker': '⊗',
        'title': 'Explanatory dialogues',
        'body': 'Gindullina et al. (hereafter **Paper A**) list four components—Conversational Agent, hierarchical classifier, PINN Customizer, LLM—yet report metrics only for classifier accuracy (0.811) and post-rewrite forecast criteria (compliance 25%/27%/6%). Component 1 has no dialogue metrics; Future work gestures at multi-agent evaluators without store-level success conditions.',
        'filenote': 'arioua_2015_explanatory_dialogues.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Arioua et al. (2015), Explanatory dialogues',
                "url": 'https://doi.org/10.1007/978-3-319-23540-0_19',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n19',
        'section': '2.4. Evaluation Approach',
        'category': 'argumentation',
        'category_label': 'Argumentation Theory',
        'marker': '⊗',
        'title': 'Dual process argument',
        'body': 'Gindullina et al. (hereafter **Paper A**) treat “Compliance with the comment” as a binary, author-judged primary success metric (25%/27%/6% for Llama-70B / DeepSeek / Llama-8B) and plan a future LLM-expert-evaluator without modeling *who* accepts an edit or *how deeply* they check it. Limitations already flag subjectivity; Future work still averages success as if all expert judgments were interchangeable.',
        'filenote': 'bisquert_2015_dual_process_argument.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Bisquert et al. (2015), Dual process argument',
                "url": 'https://doi.org/10.1007/978-3-319-23540-0_20',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n20',
        'section': '2.1. Conversational Agent',
        'category': 'argumentation',
        'category_label': 'Argumentation Theory',
        'marker': '⊗',
        'title': 'Bipolar change',
        'body': 'Gindullina et al. (hereafter **Paper A**) evaluate Expert-Guided PINN largely as single-shot comment → classify → rewrite → retrain loops (~20 launches, Fig. 5). The Conversational Agent gates concreteness/certainty/objectivity but does not log how successive expert moves *attack* or *support* prior warrants, nor how those moves change the set of acceptable loss edits. Multi-comment sessions—and Future work’s multi-agent evaluator/checker—therefore lack a dynamics vocabulary: each new comment is concatenated or restarted, not characterized as an update.',
        'filenote': 'cayrol_2015_bipolar_change.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Cayrol et al. (2015), Bipolar change',
                "url": 'https://doi.org/10.1007/978-3-319-23540-0_21',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n21',
        'section': '2.3. PINN Customizer',
        'category': 'pathology',
        'category_label': 'Loss Landscape Pathology',
        'marker': 'Σ',
        'title': 'Big valley',
        'body': 'Paper A (Gindullina et al., Expert-Guided PINN) closes each expert-in-the-loop iteration by **further training** a SIRD-PINN from the current weight state under an LLM-modified composite loss, then showing the expert a new forecast. The authors report that 15–28% of runs produce no meaningful forecast change despite a new loss, and that interactive sessions are sequential—each round starts from the model produced by the previous one.',
        'filenote': 'clark_deconstructing_big_valley.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Ochoa and Veerapen, 2016, *Deconstructing the Big Valley Search Space Hypothesis*',
                "url": None,
                "verified": False,
            }
        ],
    },
    {
        'id': 'n22',
        'section': '3.4. Framework performance',
        'category': 'pathology',
        'category_label': 'Loss Landscape Pathology',
        'marker': 'Σ',
        'title': 'Fractal boundaries of the PINN loss landscape',
        'body': "Figure 4b and 4c highlight erratic behavior when tweaking boundary conditions. Daza's basin entropy metrics explain that such boundaries often feature fractal structures. The LLM's edit pushes the weights across a chaotic boundary, resulting in a 700-day outbreak. This is a topological pathology of the loss landscape, not a failure of language interpretation.",
        'filenote': 'daza_2016_basin_entropy.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'Boundary condition tweaks push the optimization into chaotic, fractal regions of the loss space.',
        "sources": [
            {
                "text": 'Daza et al. (2016), Fractal boundaries of the PINN loss landscape',
                "url": 'https://doi.org/10.1038/srep31416',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n23',
        'section': '4. Limitations and Future work',
        'category': 'argumentation',
        'category_label': 'Argumentation Theory',
        'marker': '⊗',
        'title': 'Possibilistic inconsistency',
        'body': 'Gindullina et al. (hereafter **Paper A**) encode expert guidance as a stratified class/subclass rule table (Appendix A / Table A.2): permitted “add penalty…” edits with hard prohibitions on other loss components. When comments or rules conflict—or when successive edits pull the loss in incompatible directions—the pipeline has only crude options: accept the LLM rewrite if it compiles, or reject and retry.',
        'filenote': 'dubois_2015_possibilistic_inconsistency.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Dubois et al. (2015), Possibilistic inconsistency',
                "url": 'https://doi.org/10.1007/978-3-319-23540-0_23',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n24',
        'section': '3.2. Code correctness',
        'category': 'evaluation',
        'category_label': 'Evaluation Epistemics',
        'marker': '§',
        'title': '27% vs 25% is noise; use Anderson-Darling',
        'body': "Paper A compares 25% to 27% at n=20 and concludes DeepSeek is superior. Eftimov's eDSC method demonstrates that this difference is well within statistical noise. Proper Anderson-Darling tests with Bonferroni correction are required to claim superiority across algorithm selection tasks. Without this, the model selection relies on random variation.",
        'filenote': 'eftimov_2019_edsc_statistical_comparison.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'Statistical significance is missing; 27% vs 25% at n=20 is indistinguishable from noise.',
        "sources": [
            {
                "text": 'eDSC',
                "url": 'https://doi.org/10.1016/j.ins.2019.03.049',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n25',
        'section': '5. Conclusion',
        'category': 'evaluation',
        'category_label': 'Evaluation Epistemics',
        'marker': '§',
        'title': 'Prediction is just one goal; discipline the dialogue',
        'body': "Paper A evaluates compliance but claims to improve forecasting. Epstein's 'Why Model?' argues prediction is only one of 17 reasons to build models. If compliance (25-27%) is the true goal, the system should be reframed around 'disciplining the dialogue' between expert and machine, rather than strictly chasing MAE.",
        'filenote': 'epstein_2008_why_model.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'The framework actually disciplines dialogue rather than improving raw predictive accuracy.',
        "sources": [
            {
                "text": 'Epstein',
                "url": 'https://jasss.soc.surrey.ac.uk/11/4/12.html',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n26',
        'section': '1. Introduction',
        'category': 'architecture',
        'category_label': 'Agent Architecture',
        'marker': '‡',
        'title': 'Interactive inductive',
        'body': 'Gindullina et al. (hereafter **Paper A**) run an expert-in-the-loop PINN cycle: free-text comment → Conversational Agent → hierarchical class/subclass → PINN Customizer prompt → LLM rewrite of the entire SIRD loss → compile check only → retrain. Best “Compliance with the comment” is only 25–27% (DeepSeek / Llama-70B) vs 6% (Llama-8B) at temperature 1.0 (~20 launches). Documented pathologies include literal insertion of numeric cues from the comment into the loss, unused code, and a boundary-condition weight edit that produced a >700-day outbreak.',
        'filenote': 'hadjimichael_1993_interactive_inductive.md',
        'tagline': 'Literature comparison (proposed extension)',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Hadjimichael et al. (1993), Interactive inductive',
                "url": 'https://doi.org/10.1006/imms.1993.1008',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n27',
        'section': '1. Introduction',
        'category': 'explanation',
        'category_label': 'Explanation Theory',
        'marker': '*',
        'title': 'Was the edit the cause of the shift?',
        'body': "When the LLM makes an edit, the expert visually judges the new curve. Halpern and Pearl's actual cause framework asks: Was the specific edit the actual cause of the curve shift, or just retraining noise? The pipeline provides no mechanism to isolate the causal effect of the text instruction from Adam optimization variance.",
        'filenote': 'halpern_pearl_2005_causes_and_explanations.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'The system cannot distinguish the causal effect of the edit from simple retraining noise.',
        "sources": [
            {
                "text": 'Halpern et al. (pearl), Was the edit the cause of the shift?',
                "url": 'https://arxiv.org/abs/cs/0011012',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n28',
        'section': '4. Limitations and Future work',
        'category': 'explanation',
        'category_label': 'Explanation Theory',
        'marker': '*',
        'title': 'Policy explanation',
        'body': 'Gindullina et al. (hereafter **Paper A**) close the Expert-Guided PINN loop with a plot and a subjective “Compliance with the comment” judgment (25%/27%/6% for Llama-70B / DeepSeek / Llama-8B). After the LLM rewrites the SIRD loss, the expert sees a curve—not a reason. Limitations admit that Appendix A’s coarse “Add penalty to term2” rules fail to ensure “semantic transparency and explainability of the changes made,” and Future work still names templates and checkers without an interaction language for *why* an edit fired.',
        'filenote': 'hayes_2017_policy_explanation.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Hayes et al. (2017), Policy explanation',
                "url": 'https://doi.org/10.1145/2909824.3020223',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n29',
        'section': '4. Limitations and Future work',
        'category': 'formalization',
        'category_label': 'Formalization & Ontology',
        'marker': '†',
        'title': 'Templates as grammars, but beware losing diversity',
        'body': "Future work proposes modification templates, which are essentially grammars. Hidalgo's work on Grammatical Evolution shows that while templates prevent syntactic garbage, they can drastically reduce solution diversity. The challenge isn't just restricting operators, but doing so without preventing novel, valid epidemiological adjustments.",
        'filenote': 'hidalgo_2018_glucose_grammatical_evolution.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'Modification templates restrict garbage but also risk eliminating diverse, valid solutions.',
        "sources": [
            {
                "text": 'Hidalgo et al. (2018), Templates as grammars, but beware losing diversity',
                "url": 'https://doi.org/10.1007/978-3-319-74718-7_55',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n30',
        'section': '3.4. Framework performance',
        'category': 'evaluation',
        'category_label': 'Evaluation Epistemics',
        'marker': '§',
        'title': 'Algorithm selection survey',
        'body': "Gindullina et al. (hereafter **Paper A**) evaluate three LLMs (Llama-3.1-8B, Llama-3.3-70B, DeepSeek-V3.1) across the same 20 comments and report per-LLM aggregate compliance rates of 6% / 25% / 27%. The paper's implicit conclusion — «DeepSeek-V3.1 is best» at 27% — treats LLM selection as a per-set decision: pick one algorithm and apply it to all instances. No per-comment analysis, no attempt to route different comment classes to different LLMs, no measurement of what the best-per-comment (oracle) LLM would achieve, and no discussion of instance features that could support per-comment routing — even though Paper A's own class/subclass ontology (Appendix A) is exactly such a feature set.",
        'filenote': 'kerschke_2019_algorithm_selection_survey.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Kerschke et al. (2019), Algorithm selection survey',
                "url": 'https://doi.org/10.1162/evco_a_00242',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n31',
        'section': '2. Methodology',
        'category': 'pathology',
        'category_label': 'Loss Landscape Pathology',
        'marker': 'Σ',
        'title': 'Fig 4b,c are fractal basins, not LLM errors',
        'body': "The failures shown in Figure 4b and 4c are interpreted as LLM reasoning errors, but Malan's survey on loss landscapes shows these are typical fractal basins of attraction. When the PINN is retrained from the previous weight state, it's trapped in a disconnected funnel. The error lies in the optimization geometry, not just the LLM's prompt adherence.",
        'filenote': 'malan_2021_landscape_analysis_survey.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'What looks like an LLM error is often just a fractal basin in the PINN loss landscape.',
        "sources": [
            {
                "text": 'Malan et al. (2021), Fig 4b,c are fractal basins, not LLM errors',
                "url": 'https://doi.org/10.3390/a14020040',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n32',
        'section': '2. Methodology',
        'category': 'pathology',
        'category_label': 'Loss Landscape Pathology',
        'marker': 'Σ',
        'title': 'Walk nn landscapes',
        'body': 'Work A (Gindullina et al., «Expert-guided forecasting of epidemic ARI incidence based on physics-informed neural networks and large language models») translates expert commentary into modifications of the PINN **composite loss** ($L = L_{data} + L_{IC} + L_{ODE}$) and retrains the network with fixed Adam hyperparameters. The failures in Fig. 4b,c—weakening or fourfold strengthening of the zero boundary condition in response to requests about peak shift and continued growth—the authors explain by the lack of LLM control and «architectural features of PINN», but **do not analyze the geometry of the error landscape** after the edit.',
        'filenote': 'malan_gradient_walk_nn_landscapes.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Malan et al. (gradient), Walk nn landscapes',
                "url": None,
                "verified": False,
            }
        ],
    },
    {
        'id': 'n33',
        'section': '4. Limitations and Future work',
        'category': 'architecture',
        'category_label': 'Agent Architecture',
        'marker': '‡',
        'title': 'MAS with Generator and Adviser is ready',
        'body': "The Future Work section gestures at a multi-agent system. Malek's architecture—Generator, Adviser, and Solution Pool—is the exact blueprint needed here. Instead of a single-shot LLM pass, the Generator should propose edits and the Adviser should evaluate them against the Solution Pool before bothering the expert.",
        'filenote': 'malek_2009_multi_agent_collaboration.md',
        'tagline': 'Literature comparison (proposed extension)',
        'anchor_preview': 'A multi-agent Generator/Adviser architecture is already available to replace the single-shot pass.',
        "sources": [
            {
                "text": 'Malek et al. (2009), MAS with Generator and Adviser is ready',
                "url": None,
                "verified": False,
            }
        ],
    },
    {
        'id': 'n34',
        'section': '2.3. PINN Customizer',
        'category': 'evaluation',
        'category_label': 'Evaluation Epistemics',
        'marker': '§',
        'title': 'Compositional forecasting',
        'body': 'Gindullina et al. (hereafter **Paper A**) score Expert-Guided PINN with four criteria: MAE ≤ 1100 on training fit, MAE ≥ 700 as “forecast changed,” hard epidemic-logic checks on SIRD compartments, and a subjective primary—“Compliance with the comment” at 25–27% best. SIRD outputs are *shares of a closed population* evolving in time, yet evaluation never treats them as compositional time series: no proper forecast MSE on proportions, no residual-correlation diagnostics, no comparison against a proportion-aware baseline.',
        'filenote': 'mehdi_2015_compositional_forecasting.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Mehdi et al. (2015), Compositional forecasting',
                "url": 'https://doi.org/10.1007/978-3-319-23540-0_12',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n35',
        'section': '4. Limitations and Future work',
        'category': 'argumentation',
        'category_label': 'Argumentation Theory',
        'marker': '⊗',
        'title': 'Asp rules of thumb',
        'body': "Gindullina et al.'s work (hereafter **Paper A**) constrains LLM edits to a PINN loss with a coarse class/subclass rule table (Appendix A / Table A.2: mostly “add penalty to term\\(k\\); other components prohibited”), then accepts any compilable rewrite that authors visually judge compliant (25–27% best / 6% for 8B). Future work promises class-subclass **modification templates** with admissible operators and numeric ranges, but offers no calibration design for those ranges.",
        'filenote': 'merhej_2015_asp_rules_of_thumb.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Merhej et al.',
                "url": 'https://doi.org/10.1007/978-3-319-23540-0_25',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n36',
        'section': '4. Limitations and Future work',
        'category': 'explanation',
        'category_label': 'Explanation Theory',
        'marker': '*',
        'title': 'The system never asks for a contrastive foil',
        'body': "Experts naturally provide contrastive explanations (why P rather than Q). However, the Conversational Agent never explicitly elicits a contrastive foil. Without asking 'compared to what?', the LLM guesses the intended difference, leading directly to the 700-day outbreak anomaly shown in the results.",
        'filenote': 'miller_2020_contrastive_explanation.md',
        'tagline': 'Literature comparison',
        'anchor_preview': "The conversational agent fails to ask the most important question: 'compared to what?'",
        "sources": [
            {
                "text": 'Miller',
                "url": 'https://arxiv.org/abs/1811.03163',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n37',
        'section': '2.2. Hierarchical text classifier',
        'category': 'formalization',
        'category_label': 'Formalization & Ontology',
        'marker': '†',
        'title': 'Ad hoc Table A.2 lacks competency questions',
        'body': 'The Table A.2 rules represent a brittle ad hoc ontology. Noy and McGuinness formalized ontology development via competency questions, which are entirely absent here. Without a formal intermediate representation (Frame Ontology), the pipeline maps directly from text to code, ensuring varying and uninterpretable loss edits.',
        'filenote': 'noy_2001_ontology_development_101.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'Ad hoc tables without competency questions are brittle compared to formal ontologies.',
        "sources": [
            {
                "text": 'Noy et al. (2001), Ad hoc Table A.2 lacks competency questions',
                "url": 'https://protege.stanford.edu/publications/ontology_development/ontology101.pdf',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n38',
        'section': '2.4. Evaluation Approach',
        'category': 'evaluation',
        'category_label': 'Evaluation Epistemics',
        'marker': '§',
        'title': 'Algorithm selection challenge',
        'body': 'Paper A (Gindullina et al., Expert-Guided PINN) compares three off-the-shelf LLMs on an ad hoc battery of four qualitative criteria—MAE thresholds 700 and 1100 chosen empirically, twenty launches per model at temperature 1.0, and a primary “Compliance with the comment” score judged without formalised rubrics. Paper B (Kotthoff, Hurley, and O’Sullivan, 2017, *The ICON Challenge on Algorithm Selection*) addresses the same meta-problem in algorithm selection: before ICON, “evaluations often use different data sets, different performance measures, and different experimental setups,” so “the results are not directly comparable.” ICON’s response was shared infrastructure (ASlib scenarios), mandatory source code, bootstrap train/test splits, and a **normalised score** where 0 is oracle per-instance algorithm choice and 1 is always picking the single best solver—making gaps to perfection explicit.',
        'filenote': 'omahony_icon_algorithm_selection_challenge.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Kotthoff, Hurley, and O’Sullivan, 2017, *The ICON Challenge on Algorithm Selection*',
                "url": None,
                "verified": False,
            }
        ],
    },
    {
        'id': 'n39',
        'section': '2.2. Hierarchical text classifier',
        'category': 'argumentation',
        'category_label': 'Argumentation Theory',
        'marker': '⊗',
        'title': 'Priority probabilistic kb',
        'body': 'Gindullina et al. (hereafter **Paper A**) encode expert intent as flat English rules—“Add penalty to term2… Modification of other function components is **prohibited**”—then let an LLM rewrite the whole PINN loss. Hard epidemiological requirements (non-negativity, cumulative monotonicity, asymptotic SIRD behavior) sit in a separate post-hoc filter (criterion 3), while curve-shape wishes compete as soft penalties with no priority semantics.',
        'filenote': 'potyka_2015_priority_probabilistic_kb.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Potyka et al. (2015), Priority probabilistic kb',
                "url": 'https://doi.org/10.1007/978-3-319-23540-0_9',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n40',
        'section': '2.4. Evaluation Approach',
        'category': 'evaluation',
        'category_label': 'Evaluation Epistemics',
        'marker': '§',
        'title': 'Ela problem space',
        'body': 'Gindullina et al. (hereafter **Paper A**) gate forecast success with empirically chosen MAE thresholds—1100 for “matching training data,” 700 for “forecast has changed”—and treat incidence trajectories from a fixed St. Petersburg window as the evaluation substrate. Those thresholds and any future “instance features” of expert scenarios are expressed in absolute incidence units.',
        'filenote': 'skvorc_2020_ela_problem_space.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Skvorc et al. (2020), Ela problem space',
                "url": 'https://doi.org/10.1016/j.asoc.2020.106138',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n41',
        'section': '4. Limitations and Future work',
        'category': 'architecture',
        'category_label': 'Agent Architecture',
        'marker': '‡',
        'title': 'Steering wheel crn',
        'body': 'Gindullina et al. (hereafter **Paper A**) open an epidemiologist’s free-text comment into a largely unstructured conversational loop, then collapse it—via classifier and Table A.2 rules—into a single LLM rewrite of the entire SIRD PINN loss. Compile check is the only automatic gate; the expert’s success/failure/ambiguous verdict never re-enters the model.',
        'filenote': 'steiner_2024_steering_wheel_crn.md',
        'tagline': 'Literature comparison (proposed extension)',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Steiner et al. (2024), Steering wheel crn',
                "url": 'https://doi.org/10.1038/s41467-024-47997-9',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n42',
        'section': '4. Limitations and Future work',
        'category': 'formalization',
        'category_label': 'Formalization & Ontology',
        'marker': '†',
        'title': 'Knowledge engineering',
        'body': 'Gindullina et al. (hereafter **Paper A**) present Expert-Guided PINN as an interactive NL→loss pipeline: Conversational Agent → hierarchical class/subclass ontology → PINN Customizer → LLM rewrite of a SIRD PINN objective → compile check → retrain. Best “Compliance with the comment” reaches only 25–27% (DeepSeek / Llama-70B) versus 6% (Llama-8B). The manuscript’s “What this paper adds” box frames novelty as formalizing expert knowledge into the PINN objective *via natural language*, against a backdrop of static mathematical constraints or parameter-tuning UIs. Future work still calls for deeper class–subclass *modification templates* and multi-agent checkers—admitting that Appendix A rules “lack sufficient detail.”',
        'filenote': 'studer_1998_knowledge_engineering.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Studer et al. (1998), Knowledge engineering',
                "url": 'https://doi.org/10.1016/S0169-023X(97',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n43',
        'section': '4. Limitations and Future work',
        'category': 'reliability',
        'category_label': 'LLM Reliability',
        'marker': '¶',
        'title': 'Bnsl interaction',
        'body': "Gindullina et al.'s work (hereafter **Paper A**) builds Expert-Guided PINN so that an epidemiologist can reshape a SIRD forecast with natural-language comments: Conversational Agent → BERT class/subclass (~81%) → one-shot LLM loss rewrite → compile check → retrain. Compliance with the comment reaches only 25–27% for the best models and 6% for Llama-3.1-8B; evaluation remains author-judged plots, with no published study on institute epidemiologists.",
        'filenote': 'tonda_2013_bnsl_interaction.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Tonda et al.',
                "url": 'https://doi.org/10.1007/978-3-319-11683-9_17',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n44',
        'section': '1. Introduction',
        'category': 'pathology',
        'category_label': 'Loss Landscape Pathology',
        'marker': 'Σ',
        'title': '',
        'body': 'Paper A (Gindullina et al., Expert-Guided PINN) runs an expert-in-the-loop cycle where an LLM edits SIRD-PINN loss code and the system **must retrain** before anyone can judge the forecast. Paper B (Zwirn & Delahaye, *Unpredictability and Computational Irreducibility*) proves that for computationally irreducible (CIR) systems there is **no shortcut** to the $n^{\\text{th}}$ state faster than stepwise simulation.',
        'filenote': 'unpredictabilityAndComputationalIrreducibility.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Zwirn & Delahaye, *Unpredictability and Computational Irreducibility*',
                "url": None,
                "verified": False,
            }
        ],
    },
    {
        'id': 'n45',
        'section': '3.3. Working with the framework',
        'category': 'explanation',
        'category_label': 'Explanation Theory',
        'marker': '*',
        'title': 'Dialogue explanation',
        'body': 'Gindullina et al. (hereafter **Paper A**) ship a Conversational Agent that validates expert comments for concreteness, certainty, and objectivity, then closes the loop when the expert visually judges “Compliance with the comment” (primary success 25%/27%/6%). Component 1 of four is never evaluated as a dialogue; success of the whole pipeline collapses into a feels-right plot check that Limitations themselves call subjective.',
        'filenote': 'walton_2010_dialogue_explanation.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Walton et al. (2010), Dialogue explanation',
                "url": 'https://doi.org/10.1007/s11229-010-9745-z',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n46',
        'section': '2. Methodology',
        'category': 'pathology',
        'category_label': 'Loss Landscape Pathology',
        'marker': 'Σ',
        'title': '',
        'body': 'Paper A (Gindullina et al., Expert-Guided PINN) lets experts state macroscopic epidemic goals in natural language while an LLM rewrites **micro-level** loss code; the PINN must then be **simulated** (retrained) to reveal the curve. Paper B (Bedau, 1997, *Weak Emergence*) defines macrostates that are derivable from microdynamics **only by simulation**, and warns against illicit «downward causation.» Gindullina’s loop is a worked example of weak-emergence epistemology with an engineered top-down control attempt—explaining why experts and LLMs cannot reliably predict compliance before training and why reverse macro→micro mapping succeeds only ~25–27% (Comparative inference).',
        'filenote': 'weakEmergence.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'This comparison addresses structural and methodological gaps in the framework.',
        "sources": [
            {
                "text": 'Bedau, 1997, *Weak Emergence*',
                "url": None,
                "verified": False,
            }
        ],
    },
    {
        'id': 'n47',
        'section': '3.3. Working with the framework',
        'category': 'optimization',
        'category_label': 'Active Optimization',
        'marker': '∆',
        'title': 'Best-of-N with a surrogate, not one shot at T=1.0',
        'body': "Wei et al.'s DANTE solves exactly the loop this paper builds — free-form intent → expensive black-box evaluation — with two moves this pipeline currently skips: generate k=8/16 candidates per prompt, then use a cheap surrogate quality model to pick the winner before paying for a full PINN retrain. At T=1.0 the Customizer already emits multiple valid loss edits per comment (Fig. 3, 20 launches); discarding all but one is throwing away the sampling budget DANTE's surrogate needs. Ported to this system, Roadmap step 2 predicts compliance 25% → 40–50% without changing the base LLM or the PINN itself.",
        'filenote': 'wei_2024_dante_active_optimization.md',
        'tagline': 'Literature comparison (proposed extension)',
        'anchor_preview': 'A published loop for expensive-evaluation black boxes already runs best-of-k with a surrogate pre-screen.',
        "sources": [
            {
                "text": 'Wei et al. (2024), Best-of-N with a surrogate, not one shot at T=1.0',
                "url": 'https://doi.org/10.1038/s43588-025-00858-x',
                "verified": True,
            }
        ],
    },
    {
        'id': 'n48',
        'section': '4. Limitations and Future work',
        'category': 'evaluation',
        'category_label': 'Evaluation Epistemics',
        'marker': '§',
        'title': 'Bradley-Terry separates following instructions from accuracy',
        'body': 'The Bradley-Terry reward model fundamentally separates adherence to instruction from objective forecast accuracy. Paper A currently conflates subjective visual compliance with metric success. TRM evaluates complex reasoning by comparing pairwise trajectories, precisely addressing the missing evaluation step where experts merely eyeball the curve rather than formalizing the compliance logic.',
        'filenote': 'zhang_2026_trm_complex_reasoning.md',
        'tagline': 'Literature comparison',
        'anchor_preview': 'Subjective visual compliance must be separated from trajectory accuracy using formal reward models.',
        "sources": [
            {
                "text": 'Zhang et al. (2026), Bradley-Terry separates following instructions from accuracy',
                "url": 'https://arxiv.org/abs/2602.08498',
                "verified": True,
            }
        ],
    },
]


def commentaries_by_section() -> dict[str, list[Commentary]]:
    grouped: dict[str, list[Commentary]] = {}
    for commentary in COMMENTARIES:
        grouped.setdefault(commentary["section"], []).append(commentary)
    return grouped


ANNOTATED_SECTIONS: list[str] = list(commentaries_by_section().keys())
