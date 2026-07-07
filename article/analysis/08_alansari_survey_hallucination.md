> **How to read this comparison**
>
> - **Paper A** denotes Gindullina et al. (Expert-Guided PINN); **Paper B** denotes the cited source paper.
> - Quoted passages are taken from the papers named in the comparison.
> - Interpretive links between papers are argued explicitly; they are not claims made by either author team.
> - Sections titled **Proposed direction** suggest possible follow-up work. They are engineering ideas, not reported results.


Paper A (Gindullina et al., 2026) documents a working Expert-Guided PINN prototype where LLMs rewrite epidemic loss functions from natural-language comments. Syntax repair succeeds (≥80% compilable after iterative correction), but semantic alignment fails: only 25–27% “Compliance with the comment” for the best models. Paper B (Alansari & Luqman, 2025) is a comprehensive hallucination survey that does not mention PINNs, yet it supplies a **lifecycle taxonomy**, a **task-level vulnerability map** (including code generation), and a **mitigation/detection catalogue** that names, explains, and partially pre-implements what Paper A encountered empirically and proposed as future work.

The central thesis: Paper A’s failures are not idiosyncratic integration bugs — they are instances of well-classified LLM hallucination modes (faithful logical inconsistency, instruction–context drift, multi-hop reasoning failure) that Paper B links to specific pipeline stages and hybrid mitigations Paper A has not yet deployed.

---

## 1. Code-generation hallucination as the PINN Customizer failure class

Paper A treats LLM errors as domain-specific noise (unused variables, wrong peak shifts). Paper B classifies the task itself:

> **Quote (Alansari):** *"Code Generation is an NLG task that generates code snippets based on natural language descriptions. This task is highly prone to hallucination, resulting in code that appears plausible but consists of logical, runtime, or syntax errors [34]. Such hallucinated code can lead to software malfunctions or security vulnerabilities if not identified and corrected."*

Paper A’s own error inventory fits this taxonomy:

> **Quote (Gindullina):** *"Adding unused variables and constant terms. Erroneous assumptions about the presence of nonexistent patterns in the data. Incorrect interpretation and use of numerical parameters mentioned in comments."*

The first two are extrinsic/fabrication patterns; the third is instruction–context inconsistency when numeric tokens in the comment are copied into loss terms without mapping to epidemiological meaning. Paper A already cites hallucination risk at design time:

> **Quote (Gindullina):** *"However, direct use of LLM is associated with the risk of hallucinations Cossio (2025) – the generation of incorrect or physically unjustified code, which requires the development of strict control mechanisms."*

Paper B turns that citation into an engineering checklist rather than a background warning.

---

## 2. Faithfulness versus factuality: why “epidemic logic” can pass while comments fail

Paper A reports high “Compliance with epidemic logic” (90–100%) alongside catastrophic semantic misses (6–27% comment compliance). Paper B’s faithfulness taxonomy explains how both can coexist:

> **Quote (Alansari):** *"Faithfulness hallucination occurs when the generated output drifts from the original input or context, violating the user's instructions or violating the logical consistency within the response. This type of hallucination is further categorized into three subtypes: instruction, context, and logical."*

The ambiguous Fig. 4c case — increasing a zero boundary-condition weight when the expert asked for two more weeks of growth — is instruction inconsistency with locally coherent ODE penalties. The 700-day outbreak — weakening a terminal boundary condition when asked to shift a peak — blends context inconsistency (misread measure semantics) with downstream logical inconsistency in the forecast. Paper B’s vocabulary lets Paper A separate **physics-shaped wrong answers** from **comment-faithful answers**, instead of collapsing both into “LLM error”.

| Criterion | Paper A (Expert-Guided PINN) | Paper B (Hallucination Survey) | Takeaway |
|:--- |:--- |:--- |:--- |
| Primary failure surface | Loss-code semantics after compile | NLG tasks with open-ended generation | Code gen is a named high-risk class in B |
| Syntax vs semantics gate | Python interpreter only | Multi-paradigm detection (retrieval, uncertainty, embedding, learning, self-consistency) | A stops at syntax; B targets meaning |
| Success on faithfulness | High epidemic-logic compliance | Faithfulness subtypes explain partial compliance | Passing ODE checks ≠ passing instructions |
| Stated mitigation depth | Iterative compile-fix loop | Hybrid prompt + retrieval + reasoning + model-centric stacks | A uses one mitigation family |

---

## 3. Root causes at inference: multi-hop reasoning and prompt ambiguity

Translating “shift the peak by 7–10 days because restrictions were late” into a boundary-condition edit requires chaining epidemiology, ODE structure, and loss-term semantics — a multi-hop mapping Paper B flags as fragile:

> **Quote (Alansari):** *"LLMs often fail to produce accurate responses in scenarios that require multi-hop reasoning or logical deduction... If the model fails to link the facts properly, it will usually hallucinate when generating responses."*

Paper A’s mitigation for ambiguous prompts is structural — conversational validation and BERT classification — but the generative prompt still bundles task context, rules, full loss source, and comment into one LLM call. Paper B links underspecified queries to model-prior reliance rather than user intent:

> **Quote (Alansari):** *"a lack of specificity in user queries prompts LLMs to rely on their own training data... rather than on the user's request"* (inference-stage cause family, Section 4.6).

Paper A’s temperature=1.0 prototyping setting amplifies sampling randomness — another inference-stage cause in Paper B’s lifecycle figure. Together, the papers imply that raising model size (Llama-70B vs 8B) fixes syntax faster than it fixes multi-hop semantic mapping.

---

## 4. Inadequate evaluation metrics as an undetected hallucination source

Paper A acknowledges subjective evaluation:

> **Quote (Gindullina):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the 'Compliance with the comment' criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results."*

Paper B classifies weak metrics as a **development-lifecycle** hallucination cause:

> **Quote (Alansari):** *"Inadequate evaluation metrics are one of the main reasons for undetected hallucination in this stage [21]. Automatic metrics, such as ROUGE [71], BertScore [72], and BLEU [73], are usually used for evaluating LLMs. However, these metrics often fail to assess the factuality and faithfulness of the generated text."*

Paper A’s MAE thresholds (700, 1100) measure distributional change and fit, not instruction faithfulness — analogous to high ROUGE with hidden hallucination in Paper B’s critique. Paper B’s survey of faithfulness metrics and hallucination benchmarks (Sections 8–9) is a direct resource for replacing Paper A’s fourth criterion with claim-level verification.

---

## 5. Compiler-triggered Self-Refine versus semantic refinement

Paper A’s iterative correction is compile-driven:

> **Quote (Gindullina):** *"A critical aspect of the developed framework is the implemented mechanism for iteratively correcting the generated code, which allowed us to increase the overall success rate to at least 80% for all tested models."*

Paper B positions compile-fix loops as a narrow subset of iterative refinement:

> **Quote (Alansari):** *"Self-Refine leverages the concept of LLMs as self-reviewers by using a single LLM that acts as a generator, refiner, and feedback provider, relying solely on prompt designs without the need for fine-tuning. Self-Refine depends on an appropriate LLM and three prompts (for initial response generation, feedback, and refinement)."*

Reflexion adds persistent memory across trials:

> **Quote (Alansari):** *"The Reflexion uses a long-lasting memory that allows an agent to recognize its own mistakes and autonomously derive insights from its mistakes and iteratively adapt its behavior over time."*

Paper A’s 700-day and flat-plateau failures compiled cleanly — so neither Self-Refine nor Reflexion would trigger under a syntax-only evaluator. Paper B’s reasoning-based extensions (CoVE, HaluSearch with MCTS scoring of intermediate steps) target exactly the “wrong but runnable” regime.

---

## 6. Structured CoT for code: a blueprint for Paper A’s modification templates

Paper A’s planned fix for numeric literalism is template-bound generation:

> **Quote (Gindullina):** *"we plan to replace the simple penalty additions by class-subclass-specific modification templates. These templates will explicitly define which loss components and parameters can be altered, which mathematical operators are admissible, and what numerical ranges are permitted."*

Paper B describes a ready-made programming analogue — Structured CoT (SCoT) for code:

> **Quote (Alansari):** *"Li et al. [184] further adapted the SCoT approach specifically for code generation tasks, introducing programming structures, such as sequential, branching, and looping steps, as intermediate representations... This structured reasoning substantially mitigates hallucinations and improves code accuracy, outperforming traditional CoT prompting by a considerable margin across multiple programming benchmarks."*

Mapping BERT subclass → SCoT step skeleton → bounded template instantiation is a concrete fusion of Paper A’s future work with Paper B’s evaluated mitigation pattern.

---

## 7. Multi-agent verification: Paper A’s proposal as a survey-standard architecture

Paper A proposes:

> **Quote (Gindullina):** *"A promising direction is to evolve the system toward a multi-agent architecture, where specialized LLMs enhance autonomy and objectivity. An LLM-expert-evaluator could quantify forecast compliance with the original comment; low confidence scores could trigger automatic loss regeneration or comment refinement. An LLM-loss-semantic-checker could verify alignment between the generated code and modification rules, reducing hallucinations."*

Paper B documents operational analogues. CoNLI:

> **Quote (Alansari):** *"The CoNLI prompting approach uses a hierarchical inference-based framework to detect and mitigate ungrounded hallucinations in LLMs [198]. A detection agent breaks down the baseline response into claims at the sentence and entity levels... A mitigation agent subsequently corrects detected hallucinations by post-editing the baseline output."*

HaluAgent:

> **Quote (Alansari):** *"HaluAgent integrates a multi-stage detection pipeline. The pipeline consists of sentence segmentation, tool-based verification, and reflective reasoning with external resources, such as web search, calculators, and code interpreters."*

For Paper A, the “code interpreter” is not merely a syntax oracle but a sandbox that evaluates proposed loss edits against SIRD invariants before PINN retraining — precisely the semantic-checker role Paper A names but does not build.

---

## 8. Detection before retrain: semantic entropy and hybrid gates

Paper B argues no single detector suffices:

> **Quote (Alansari):** *"The observed limitations in each category indicate that no single detection paradigm is sufficient in isolation. Hybrid strategies that combine internal confidence signals, consistency checks, and external evidence grounding are increasingly explored."*

Semantic entropy — clustering multiple generations by meaning — flags high-variance paraphrases before deployment:

> **Quote (Alansari):** *"Semantic entropy is computed over the sentence's meaning rather than relying on the words' distribution... A high semantic entropy indicates that the model's answers vary in meaning, indicating a high likelihood of hallucination."*

Applied to Paper A: sample *N* loss rewrites at production temperature (0–0.2, as Paper A plans), cluster by AST/semantic effect on `term1–4`, and block retraining when clusters diverge — addressing Paper A’s 15–28% “forecast unchanged” band as ambiguity, not success.

Contrastive decoding (Paper B, Section 7.4) could bias generation toward in-context SIRD equations versus parametric priors — relevant when LLMs invent nonexistent data patterns.

---

## 9. Explainability of hallucinations: HalluTree versus loss-function opacity

Paper A lacks transparency for generated penalties. Paper B’s grounding explainability section covers claim decomposition:

> **Quote (Alansari):** *"HalluTree, which decomposes summaries into subclaims and organizes verification results into a hierarchical claim tree. Subclaims are categorized as extractive or inferential."*

A PINN-loss variant would decompose each LLM edit into claims (“increase terminal penalty on I”, “shift peak window by Δt”) and verify each against Appendix A rules and SIRD asymptotics before training. Galitsky–Rybalov-style abductive checks in Paper B measure whether a claim’s probability shift is explainable from sources — here, sources are the expert comment plus the original loss, not a web corpus.

Paper B also notes explainability limits Paper A should expect:

> **Quote (Alansari):** *"Explanations often rely on proxy signals such as attention patterns, structural irregularities, or alignments with external evidence, which may not fully capture the underlying model's reasoning."*

So importing HalluTree-like checks is necessary but not sufficient for PINN pathology.

---

## Proposed direction 1. SCoT + template instantiation in PINN Customizer

**Pipeline stage:** PINN Customizer (replaces single-shot code emission).

**Mechanism:** For each confirmed subclass, run Structured CoT steps (select compartment → select operator class → bind numeric range → emit code). Use Paper B’s programming-structure intermediate representation before PyTorch.

**Failure mode addressed:** Literal numeric insertion; aggressive AST edits (TSED failures on Llama-8B).

---

## Proposed direction 2. HaluAgent-style semantic checker with Python + SIRD sandbox

**Pipeline stage:** Between code generation and PINN retrain.

**Mechanism:** Detection agent extracts claims from generated loss; verifier executes short PINN probes or symbolic checks (non-negativity, terminal I→0); mitigation agent regenerates or escalates to expert.

**Failure mode addressed:** Runnable but physically absurd forecasts (700-day outbreak).

---

## Proposed direction 3. Reflexion memory across expert sessions

**Pipeline stage:** Retraining loop / evaluation.

**Mechanism:** Store (comment, class, failed loss, expert verdict) tuples; inject into subsequent prompts as verbal reinforcement learning per Paper B’s Reflexion description.

**Failure mode addressed:** Repeated mistake classes across temperature-sampled runs.

---

## Proposed direction 4. Semantic-entropy gate + formalized comment-compliance metric

**Pipeline stage:** Evaluation protocol.

**Mechanism:** Multiple sampled loss functions; entropy on semantic effect clusters; replace sole subjective compliance with claim-level NLI between comment and predicted curve features (peak day, slope post-peak).

**Failure mode addressed:** Subjective “Compliance with the comment”; inadequate metrics undetected per Paper B’s evaluation-stage analysis.

---

## Proposed direction 5. Contrastive decoding anchored on SIRD context

**Pipeline stage:** LLM inference inside PINN Customizer.

**Mechanism:** Contrast logits with context-stripped prompt so token choices align with provided ODE snippet rather than pretrained epidemic priors.

**Failure mode addressed:** Erroneous assumptions about nonexistent data patterns.

---

## Conclusion

Paper A is a domain-specific **existence proof** that expert-in-the-loop PINN editing works 25–27% of the time; Paper B is the **general theory and mitigation map** for why the other 73–75% fail. The survey validates Paper A’s instincts (templates, multi-agent checkers, stronger evaluation) while showing they are already instantiated in adjacent literatures — SCoT for structured code, CoNLI/HaluAgent for claim verification, semantic entropy for pre-deployment filtering, Reflexion for cross-trial learning. The highest-leverage upgrade is not a larger LLM alone but **moving Paper B’s hybrid detection–reasoning stack upstream of PINN retraining**, where Paper A currently spends its compute budget.
