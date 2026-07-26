> **Paper B — live link:** [https://arxiv.org/abs/2602.08498](https://arxiv.org/abs/2602.08498)  
> **Source in `src/`:** [`../src/2026 Characterizing, Evaluating, and Optimizing Complex Reasoning.md`](../src/2026%20Characterizing,%20Evaluating,%20and%20Optimizing%20Complex%20Reasoning.md)

Gindullina et al. (hereafter **Paper A**) score their expert-in-the-loop PINN loss modifications with four qualitative criteria — matching training data, forecast has changed, compliance with epidemic logic, and compliance with the comment — the last of which the authors themselves flag as subjective and lacking a formalized metric. The best-model rate on that primary criterion is 25–27% across 20 launches, and the paper's Future work section names an "LLM-expert-evaluator" and an "LLM-loss-semantic-checker" as the two missing pieces: a scoring model that can rank compliance without human visual inspection, and a semantic checker that goes beyond compilability.

Zhang, Li, Wang et al. (2026; hereafter **Paper B**) present exactly this architecture — trained, evaluated, and integrated into both a test-time selector and an RL loop. Their ME² principle decomposes trace quality along two orthogonal axes (macro/micro × efficiency/effectiveness); reasoning traces are abstracted into DAGs, evaluated pairwise on macro-narrative + dominant-path micro-abstraction, and the resulting 103K-pair TRM-Preference dataset is used to train a Bradley–Terry Thinking Reward Model (TRM) initialized from Llama-3.1-8B-Instruct. Crucially, TRM is trained *only on verified-correct reasoning pairs*, decoupling reasoning quality from answer correctness — the same decoupling Paper A performs verbally ("we assess instruction-following, not impact on forecast accuracy") but never operationalizes.

Paper B is not about PINNs or epidemics; it is about how to make the "was this a good LLM step, judged along multiple objective axes" question scalable, learnable, and usable both at test time and in training. The transferable thesis is sharp: **Paper B is a working implementation of Paper A's Future-work "LLM-expert-evaluator"; ME² supplies an orthogonal-axes rubric that replaces Paper A's subjective "Compliance with the comment"; Fig. 4b is a canonical Macro-Effectiveness failure ("superficially plausible yet invalid") and the "unused code / redundant weighting" catalog is a canonical Micro-Efficiency failure — both are terms of art in Paper B, not novel Paper A pathologies.**

---

## 1. Future-work "LLM-expert-evaluator" is Paper B's TRM

Paper A explicitly names an LLM-based evaluator as the mechanism that would close its own subjectivity gap. Paper B trains one, publishes the dataset, and shows it works both as a selector and as a training signal.

> **Quote (Gindullina et al.):** *"An LLM-expert-evaluator could quantify forecast compliance with the original comment; low confidence scores could trigger automatic loss regeneration or comment refinement."*

> **Quote (Zhang et al.):** *"we construct the TRM-Preference dataset and train a lightweight Thinking Reward Model (TRM) with a Bradley–Terry objective... TRM enables effective test-time scaling by selecting high-quality reasoning traces, yielding gains of up to 19.3%"*

The role is architecturally identical: a small model with a scalar value head, initialized from a general-purpose 8B base, trained on pairwise preferences derived from an ME²-style rubric. Paper A's "low confidence scores could trigger automatic loss regeneration" is exactly Best-of-N over k LLM samples with the reward model as selector — the mechanism validated in Paper B §5.3. (Comparative inference)

---

## 2. Decoupling quality from correctness

Paper A verbally admits its evaluation targets instruction-following, not prognostic value. Paper B builds a training procedure whose entire point is to enforce that decoupling as a data-selection rule.

> **Quote (Gindullina et al.):** *"This study, therefore, assesses the capability for instruction-following, not the impact of the comment on forecast accuracy."*

> **Quote (Zhang et al.):** *"TRM is trained exclusively on verified-correct reasoning preference pairs, decoupling reasoning quality from answer correctness and remaining orthogonal to answer-based verifiable signals provided by rule-based verifiers."*

Under Paper B's protocol, only pairs of loss modifications that *both* produce forecast-accurate PINNs would be admitted into the training set — the reward model would then rank *among correct forecasts* which modification best follows the expert comment, without confounding "the LLM followed instructions" with "the modification improved out-of-sample accuracy." Paper A currently conflates the two signals whenever it reports a 25–27% number. (Comparative inference)

---

## 3. ME² quadrants vs Paper A's four ad hoc criteria

Paper A's four criteria (matching training data, forecast changed, epidemic logic, compliance) were derived pragmatically — thresholds MAE 700 and 1,100 are "empirically chosen," Criterion 3 is 90–100% almost vacuously by SIRD structure, and Criterion 4 is subjective. Paper B's four ME² quadrants are the product of an orthogonal-axes decomposition (macro/micro × efficiency/effectiveness) that generalizes beyond math reasoning.

> **Quote (Gindullina et al.):** *"four qualitative validation criteria... A value of 1100 was empirically chosen as the threshold... A value of 700 was determined empirically using test data."*

> **Quote (Zhang et al.):** *"we introduce $ME^2$ principle to characterize reasoning quality along two orthogonal axes: macro vs. micro (global structural organization vs. local step property) and effectiveness vs. efficiency."*

Mapping across: Paper A's Criterion 2 ("forecast has changed") ≈ a macro-efficiency proxy (did the trace make progress?); Criterion 3 ("epidemic logic") ≈ macro-effectiveness (did it stay on-domain?); Criterion 4 ("compliance") is a subjective mixture that ME² separates cleanly. Missing entirely from Paper A: micro-efficiency (are the specific numeric weights or ops non-redundant?) and micro-effectiveness (are individual added terms internally consistent, e.g., does the penalty use the same units as the state variable?). ME² supplies both. (Comparative inference)

---

## 4. Fig. 4b is a canonical Macro-Effectiveness failure

Paper A's Fig. 4b is a boundary-condition edit that produced a plausibly-shaped but 700+ day epidemic — the LLM technically responded to a peak-shift request, but the response is diagnostically wrong. Paper B has a name for exactly this pattern.

> **Quote (Gindullina et al.):** *"the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days)."*

> **Quote (Zhang et al.):** *"macro-effectiveness degrades when branch objectives are underspecified, topics shift abruptly, or the trace makes illogical shortcuts. Such failures are especially common in hard problems, where superficially plausible yet invalid arguments may emerge (e.g., pseudo-proofs in challenging mathematical tasks)"*

Fig. 4b is a "pseudo-proof" of the peak-shift instruction — the loss modification "looks like" the intent (BC weight adjustment) but produces an epidemiologically invalid trajectory. In ME² terms, this pair (base-loss trace, modified-loss trace) is exactly the kind of macro-effectiveness contrast the reward model is trained to distinguish; a TRM-style evaluator would rank the base loss above the modification on macro-effectiveness. (Comparative inference)

---

## 5. Unused-code / redundant-weighting catalog = Micro-Efficiency degradation

Paper A lists three systematic error modes in generated code — unused variables, spurious pattern assumptions, and literal number insertion. Paper B's Micro-Efficiency axis names each of them as a form of local degradation.

> **Quote (Gindullina et al.):** *"We determined systematic errors in the generated code: Adding unused variables and constant terms. Erroneous assumptions about the presence of nonexistent patterns in the data. Incorrect interpretation and use of numerical parameters mentioned in comments."*

> **Quote (Zhang et al.):** *"micro-efficiency degrades when steps contain redundant statements or wording, unnecessary hedging or modifiers, or looping patterns that repeat prior content without refinement"*

Under a TRM-style evaluator these three failures become tractable local features: an unused term = a leaf that adds no computation to the forward pass (redundant statement); a spurious pattern assumption = an unsupported claim (Micro-Effectiveness degradation, quote below); a literal-number insertion = a numeric edit that does not correspond to a bounded operator over the state variable it modifies. (Comparative inference)

> **Quote (Zhang et al.):** *"micro-effectiveness degrades when steps contain local errors, e.g., contradictions, hallucinations, unsupported claims, or incorrect arithmetic"*

---

## 6. Bradley–Terry pairwise supervision from real experts

Paper A's evaluation is single-author binary. Paper B's data generation is pairwise, subject to position-bias control, and orthogonal to answer correctness — a protocol directly usable at the Smorodintsev Research Institute for Influenza (co-authors of Paper A).

> **Quote (Gindullina et al.):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the "Compliance with the comment" criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results."*

> **Quote (Zhang et al.):** *"we evaluate each pair under both original and reversed orderings to enable robust evaluation, repeating the comparison multiple times and retaining only consistent, non-tied labels."*

Concretely: for each comment in Paper A's 20-launch set, generate k=4 LLM modifications, form pairwise comparisons, ask 2+ epidemiologists per pair for a preference under ME²-quadrant prompts, retain only pairs where both orderings agree. 20 comments × 6 pairs × 2 orderings × 2 experts yields ~500 stable preferences — enough to fine-tune a small reward model on top of a task-specific base. (Comparative inference)

---

## 7. Best-of-N test-time scaling replaces single-shot rewrite

Paper A samples one LLM output per comment and accepts it if it compiles. Paper B shows that sampling N candidates and selecting the highest-reward one raises accuracy monotonically in N.

> **Quote (Gindullina et al.):** *"After generating the LLM candidate loss function, its automatic validation is performed... Iterative correction – if compilation errors are detected"*

> **Quote (Zhang et al.):** *"selecting traces that are more aligned with the $ME^2$ principle consistently improves Best-of-N accuracy as $N$ increases... gains of up to 19.3% (e.g., from 44.7% at $N = 1$ to 64.0% at $N = 16$ on AIME24 with Qwen3-8B)"*

For Expert-Guided PINN, this predicts a concrete lift: at compile-passing rate ≥80% for the top models, sampling k=16 candidates and selecting the highest-TRM one before invoking the expensive PINN retrain should raise compliance well above the single-shot 25–27% number, without touching the underlying LLM. The mechanism costs only k additional LLM calls per comment. (Speculative extension)

---

## 8. RL fine-tuning with gated reward addresses signal plateau

Paper A uses three off-the-shelf LLMs without any fine-tuning. Paper B trains via GRPO with a gated reward that combines binary verifiable reward with the TRM-provided quality signal, and proves both a policy-invariance theorem and a policy-improvement lower bound driven by TRM's reward *variance*.

> **Quote (Gindullina et al.):** *"three models with different parameter sizes were selected: meta-llama/Llama-3.1-8B-Instruct... meta-llama/Llama-3.3-70B-Instruct... deepseek-ai/DeepSeek-V3.1"*

> **Quote (Zhang et al.):** *"verifier-guided RL, despite showing an early improvement in reasoning quality, quickly plateaus, with reasoning behaviors converging in the mid-to-late stages... $D_{\mathrm{TRM}}(\pi_t)$ shows that policy improvement is driven by reward variance, where verifier rewards fail to distinguish answer-correct solutions and TRM provides subtle signals to differentiate verified-correct traces"*

Paper A's binary "compliance vs no-compliance" is exactly the signal plateau Paper B's theorem identifies: once the LLM emits any accepted modification, the reward signal is flat over all other correct-forecast modifications, providing no gradient toward better instruction-following. A TRM-style thinking reward would populate that plateau with rank-order signals over verified-correct-forecast modifications. (Comparative inference)

---

## 9. Comparison table

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Evaluator identity | Human authors, unblinded | Trained scalar-head model (Bradley-Terry) | TRM is a working evaluator, not a proposal (Empirically shown for B) |
| Quality/correctness decoupling | Verbal admission only | Enforced by data-selection rule | Decoupling is operationalized, not left to the reader (Comparative inference) |
| Rubric structure | Four empirical thresholds | Orthogonal-axes ME² (2×2) | ME² catches the two axes Paper A misses entirely (Comparative inference) |
| Pairwise supervision | None (single-author binary) | 103K pairs + position-bias control | Preference elicitation from experts is feasible at Smorodintsev scale (Comparative inference) |
| Test-time selection | Single-shot LLM output | Best-of-N with reward model | k=16 sampling would lift compliance above 25–27% (Speculative extension) |
| Training signal | Zero-shot off-the-shelf LLM | GRPO with gated $r_v · (1-α+α·σ(r_t))$ | Escaping the binary-reward plateau requires a variance-providing signal (Author-stated for B) |
| Fig. 4b framing | "Effectively random modification" | Macro-Effectiveness failure = pseudo-proof | The failure has a name, a metric, and an example set (Comparative inference) |
| Unused-code framing | Systematic error mode #1 | Micro-Efficiency degradation | Existing terminology + validation set already exist (Comparative inference) |

---

## Direction 1. Modification Quality Model (MQM) via ME²-quadrant Bradley–Terry

**Pipeline stage.** Evaluation loop (replace subjective "Compliance with the comment") + PINN Customizer (add Best-of-N selection).  
**Mechanism.** For each of the four ME² quadrants, prompt the LLM (or Smorodintsev experts) to rank pairs of loss modifications: macro-efficiency (does the modification make non-redundant structural progress toward the requested change?); macro-effectiveness (is the modified forecast in-domain, non-degenerate, epidemiologically valid?); micro-efficiency (do individual edits avoid unused terms, redundant reweighting?); micro-effectiveness (are individual edits internally consistent — same units, same compartments as the state variable they modify?). Aggregate via Bradley–Terry into a scalar reward. Initialize the reward-head model from a small base (e.g., Llama-3.1-8B).  
**Failure modes addressed.** Fig. 4b macro-effectiveness pseudo-proof; Fig. 4c reweighting-as-random micro-efficiency; unused-code micro-efficiency; ambiguity between instruction-following and forecast improvement.  
**Measurable acceptance.** MQM pairwise accuracy against held-out expert preferences ≥85%; Best-of-N=16 with MQM selection lifts compliance rate at fixed PINN-retrain budget. (Speculative extension)

---

## Direction 2. RL fine-tuning of the LLM Customizer with gated MQM reward

**Pipeline stage.** LLM Customizer (replace off-the-shelf zero-shot with fine-tuned model) + evaluation.  
**Mechanism.** Apply Paper B's Eq. 1 with $r_v$ = out-of-sample forecast improvement (binary: WIS decreased vs baseline) and $r_t$ = MQM thinking reward. Fine-tune Llama-3.3-70B or Qwen3-8B via GRPO on retrospective (comment, modification, retrain-outcome) triples plus the MQM ranking signal on verified-forecast-accurate modifications. Use α ≈ 0.2 per Paper B ablation.  
**Failure modes addressed.** Binary-reward signal plateau — every correct-forecast modification looks identical under $r_v$ alone; literal numeric insertion — MQM's micro-effectiveness axis penalizes edits whose units/scale do not match target state variables; systematic underperformance of 8B model on compliance (6%) — training signal beyond zero-shot may lift the smaller model closer to 70B compliance.  
**Design caution from Paper B.** Theorem 5.1 requires that the gate does not change the optimal policy set — verify the epidemic analogue empirically before large training runs; the α ≈ 0.2 sweet spot may shift for the forecast domain. (Speculative extension)

---

## Manuscript placement

- **§2.4 Evaluation Approach:** cite ME² as the orthogonal-axes decomposition that supplies the two axes Paper A misses (micro-efficiency, micro-effectiveness) and that reframes existing Criteria 2–3 as macro-axis proxies (clusters **3**/**4** of `dinara_comprehensive_review.md`).
- **§4 Future work "LLM-expert-evaluator":** name TRM as the concrete instantiation; adopt the Bradley–Terry + position-bias + verified-correct-only recipe as the training protocol; commit to the 4-quadrant rubric rather than a single binary head.
- **§3.4 Discussion of Fig. 4b/c:** relabel the two cases with Paper B's terminology (macro-effectiveness pseudo-proof; micro-efficiency reweighting-as-loop) and cite Kalai et al. (2025) via Paper B for the pseudo-proof frame.
- **§5 Conclusion:** connect to automation-bias literature via cluster **10** — a subjective evaluator makes an unreliable "compliance" number more dangerous, not safer.

## What not to transfer

TRM's math-and-STEM training domain (WebInstruct-Verified, AIME24/25, MATH500) does not license direct extrapolation to epidemic forecasting; the 19.3% test-time gain and 3.9% RL gain must be re-measured on the Paper A benchmark before being cited as predicted lift. The DAG-based abstraction of reasoning traces (progression/branching/merging over `\n\n`-partitioned steps) is not the right abstraction for loss-modification code — an AST over PyTorch expressions is closer, and the appropriate structural summarization for a modification is *the changed subtree*, not a dominant path. Do not import the Llama-3.1-8B TRM checkpoint verbatim as an epidemiology-domain reward model — retrain on a domain-specific pairwise preference dataset. And rename the artifact: "Thinking Reward Model" is a math-reasoning brand; in Paper A the natural name is Modification Quality Model (MQM). (Comparative inference)

## Concrete next experiment

**Hypothesis.** A ME²-quadrant Modification Quality Model, trained on ~500 pairwise expert preferences over loss modifications, plus Best-of-N=8 test-time selection, raises the compliance rate on Paper A's 20-comment benchmark by ≥15 percentage points at fixed PINN-retrain budget.

**Protocol.**
1. For each of the 20 existing comments, generate k=8 LLM modifications with Llama-3.3-70B at T=1.0.
2. Retrain PINN on all 160 modifications, retain only those whose out-of-sample forecast passes a WIS threshold (proxy for "verified-correct forecast" à la Paper B's verifier).
3. Ask 2+ Smorodintsev epidemiologists to rank pairs among the retained modifications along each ME² quadrant; enforce both-orderings-agree filter.
4. Train MQM (Llama-3.1-8B + scalar head) on the resulting Bradley–Terry pairs.
5. At test time, sample k=8 modifications, MQM-rank, retrain only top-1, score against expert compliance.

**Metrics.** MQM pairwise accuracy on held-out preferences; compliance rate at k=1 baseline vs k=8 MQM selection; joint success (all four Paper A criteria) instead of marginals (per `dinara_comprehensive_review.md` §B.5).

**Expected signal.** MQM ≥85% pairwise accuracy; ≥15 p.p. improvement in single-criterion compliance; ≥25 p.p. improvement in joint success versus current marginal reporting. (Speculative extension)

## Related essays in this series

- [`04_miller_2020_contrastive_explanation.md`](04_miller_2020_contrastive_explanation.md) — contrastive judgment ⟨P, Q⟩ as an objective substitute for subjective compliance.
- [`06_hayes_2017_policy_explanation.md`](06_hayes_2017_policy_explanation.md) — predicate-language explanation as intermediate DSL for interpretability.
- [`03_tonda_2013_bnsl_interaction.md`](03_tonda_2013_bnsl_interaction.md) — real experts in an interactive loop; template for the Smorodintsev preference-collection step.
- [`14_bisquert_2015_dual_process_argument.md`](14_bisquert_2015_dual_process_argument.md) — engagement-stratified expert responses; caution for how to aggregate the pairwise labels.

## Conclusion

Paper B is not about PINNs, epidemics, or Physics-Informed anything; it is about how to make an LLM-based evaluator that ranks structural quality along orthogonal axes, trained on pairwise preferences from verified-correct outputs only, and usable both to select at test time and to train via RL. Paper A's Future work names exactly this artifact — as unimplemented. Under ME² terminology, the paper's two most damaging documented failures (700-day pseudo-plausible outbreak; ×4 BC reweighting that behaves as random) are canonical macro-effectiveness and micro-efficiency degradations, and the missing evaluator is an off-the-shelf reweighting of Paper B's TRM into a domain-specific Modification Quality Model. Adopting ME² as the rubric, Bradley–Terry over verified-forecast-accurate pairs as the supervision, and Best-of-N + gated GRPO as the two use cases would replace the "significant subjective component" Paper A itself admits — and, per Paper B's variance argument, would restore a gradient to a training signal that is currently binary.
