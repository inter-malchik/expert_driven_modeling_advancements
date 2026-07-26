> **Paper B — live link:** [https://doi.org/10.1162/evco_a_00242](https://doi.org/10.1162/evco_a_00242)  
> **Source in `src/`:** [`../src/2019 Automated Algorithm Selection: Survey and Perspectives.md`](../src/2019%20Automated%20Algorithm%20Selection%3A%20Survey%20and%20Perspectives.md)

Gindullina et al. (hereafter **Paper A**) evaluate three LLMs (Llama-3.1-8B, Llama-3.3-70B, DeepSeek-V3.1) across the same 20 comments and report per-LLM aggregate compliance rates of 6% / 25% / 27%. The paper's implicit conclusion — «DeepSeek-V3.1 is best» at 27% — treats LLM selection as a per-set decision: pick one algorithm and apply it to all instances. No per-comment analysis, no attempt to route different comment classes to different LLMs, no measurement of what the best-per-comment (oracle) LLM would achieve, and no discussion of instance features that could support per-comment routing — even though Paper A's own class/subclass ontology (Appendix A) is exactly such a feature set.

Kerschke, Hoos, Neumann, & Trautmann (2019; hereafter **Paper B**) is the canonical survey of automated algorithm selection (AS). It formalizes the per-instance algorithm selection problem (PIAS) after Rice (1976): given a set of instances \(I\), a set of algorithms \(A\), a metric \(m\), build a selector \(S: I \to A\) that maps each instance to the best algorithm. The survey introduces two reference points — the Virtual Best Solver (VBS, oracle per-instance selection) and the Single Best Solver (SBS, per-set winner) — and shows that state-of-the-art PIAS closes 25–96% of the VBS-SBS gap on combinatorial problems. It catalogues instance features for discrete (SAT, TSP, AI planning) and continuous (BBOB via ELA) problems, situates PIAS among related concepts (schedules, portfolios, configuration, meta-selection), and identifies key open challenges including per-instance algorithm configuration (PIAC).

Paper B is not about PINNs, LLMs, or epidemics; it is a domain-agnostic survey of *when* and *how* to select an algorithm per instance based on features. The transferable thesis is sharp: **Paper A's compliance-vs-LLM comparison (Fig. 5) reports SBS performance (27% for DeepSeek); the untested VBS (best-per-comment LLM) is likely substantially higher; Paper A's own comment ontology (4 classes × 2-4 subclasses) is a ready-made feature set for a PIAS selector; and building even a trivial per-instance LLM selector on top of the existing 60-launch dataset (20 × 3) is a near-zero-cost upgrade that should raise the headline compliance rate without changing the underlying LLMs, PINN, or protocol.**

---

## 1. SBS vs VBS: Paper A's 27% is the SBS, not the ceiling

Paper B is emphatic about the distinction between per-set selection (SBS) and per-instance selection (VBS). Paper A reports the former as its result.

> **Quote (Kerschke et al.):** *"the performance of a (hypothetical) perfect per-instance algorithm selector, often also referred to as an oracle selector or virtual best solver (VBS), provides a lower bound on the performance of any realistically achievable algorithm selector ... the single best solver (SBS), which is the algorithm A₀ with the best performance among all the Aⱼ ∈ A. The SBS is the solution to the closely related per-set algorithm selection problem."*

> **Quote (Gindullina et al.):** *"DeepSeek scores highest at 27%, Llama-3.3-70B is close at 25%, while Llama-3.1-8B drops significantly to 6%."*

DeepSeek at 27% is Paper A's SBS. The VBS is the counterfactual «for each of the 20 comments, use whichever LLM gave the best result on that specific comment». VBS ≥ SBS by definition; if any two of the three LLMs disagree on any single comment, VBS > SBS. Paper A does not compute VBS; it is likely to be substantially higher than 27%. The gap VBS − 27% is the maximum improvement achievable *without any new capability* — purely by selecting the right LLM per comment. (Comparative inference)

---

## 2. Comment class/subclass as instance features (Rice 1976 form)

Paper B's central technical claim is that per-instance selection requires informative, cheaply-computable features that map instances to their most-suitable algorithm. Paper A's 4-class × 2-4-subclass ontology (Appendix A) is exactly such a feature vector.

> **Quote (Kerschke et al.):** *"we cannot hope to efficiently find perfect solutions to the per-instance algorithm selection problem, and instead, we strive to find selectors whose performance is as close as possible to that of a perfect selector on instance set I. This is typically achieved by making use of informative and cheaply computable features f(i) = (f₁(i), ..., f_k(i)) of the given problem instance i. ... features should be informative ... interpretable ... cheaply computable ... generally applicable ... complementary."*

> **Quote (Gindullina et al.):** *"For automatic hierarchical tagging (class/subclass) we applied the BERT+ML method ... The model, based on "bert-base-cased", was fine-tuned on a synthetic dataset of 2000 expert-like commentaries. ... An important aspect of the system is the two-stage classification verification procedure."*

The ontology is (i) informative (comment class strongly correlates with target loss term), (ii) interpretable (four named classes), (iii) cheaply computable (BERT+ML inference is milliseconds per comment), (iv) generally applicable (covers Paper A's stated scope). What is missing is a mapping from `(class, subclass) → LLM_choice`. A PIAS selector could be as simple as a lookup table trained on the existing 60 launches. (Comparative inference)

---

## 3. Performance complementarity: 6% / 25% / 27% aggregate hides per-comment structure

Paper B distinguishes between algorithms that are uniformly dominated and algorithms with complementary strengths. The aggregate 6%/25%/27% suggests Llama-8B is dominated, but per-comment breakdown may show pockets of 8B success where larger models fail.

> **Quote (Kerschke et al.):** *"Performance complementarity has been observed for practically all NP-hard decision and optimisation problems ... For these and many other problems, theoretical results stating which algorithmic strategies work best are restricted to very limited classes of problem instances, so that it is generally unknown a priori which of several algorithms should be used to solve a given instance. ... the VBS-SBS gap is large when the given set A of algorithms shows high performance complementarity on instance set I."*

> **Quote (Gindullina et al.):** *"The Meta-Llama-3.1-8B-Instruct model demonstrated lower compliance with comments (Figure 5)."*

Paper A shows Llama-8B has 100% compliance on Criterion 3 (epidemic logic) — better than Llama-70B's 90%. This is documented performance complementarity: on integrity-preservation, 8B wins; on primary compliance, 70B/DeepSeek win. A per-instance selector could route integrity-critical comments to 8B and free-form structural comments to 70B/DeepSeek. Paper B's survey confirms this pattern is universal: rare is the problem where a single algorithm dominates on every instance and every metric. (Comparative inference)

---

## 4. Portfolios vs schedules vs per-instance selection

Paper B distinguishes multiple ways to exploit performance complementarity. Paper A uses none of them.

> **Quote (Kerschke et al.):** *"Performance complementarity within a set of algorithms can be leveraged in ways that differ from per-instance algorithm configuration. One prominent approach is that of a parallel algorithm portfolio, where each algorithm from a given set A is run in parallel on a given problem instance i. ... Algorithm schedules provide another way of exploiting performance complementarity. The key idea is to run a sequence of algorithms from a given set A, one after the other, each for a given (maximum) time."*

> **Quote (Gindullina et al.):** *"After generating the LLM candidate loss function, its automatic validation is performed"*

Three distinct designs for Paper A: (a) **parallel portfolio** — for each comment, run all 3 LLMs; keep the best-scoring modification; wall-clock same as one call if executed in parallel; (b) **schedule** — try Llama-8B first (cheapest); if compile passes and Semantic-Checker approves, use it; else try 70B; else DeepSeek; (c) **per-instance selection** — trained selector picks one LLM per comment. Each has different cost/latency/quality trade-offs. Paper A's «pick DeepSeek and hope» design corresponds to none of them. (Comparative inference)

---

## 5. VBS-SBS gap as a headline metric Paper A should report

Paper B's key evaluation metric for AS work is the fraction of VBS-SBS gap closed. Paper A does not report anything analogous.

> **Quote (Kerschke et al.):** *"State-of-the-art per-instance algorithm selectors for combinatorial problems have demonstrated to close between 25% and 96% of the VBS-SBS gap."*

> **Quote (Gindullina et al.):** *"The key result is confirmation of the fundamental feasibility of integrating expert knowledge through LLM into PINN, with a success rate of 25-27% for the best models."*

Paper A's 25–27% is the SBS rate. The VBS rate (compute post hoc from the 60 existing launches: for each comment, what fraction of the 3 LLMs succeeded?) would be at most 3× that if the 3 LLMs' successes are disjoint, and at least equal to SBS if all successes are on the same comments. Reporting the pair «SBS 27% / VBS X% / current fraction closed 0%» would honestly frame the paper's headline as «SBS demonstrated; VBS unknown; per-instance selection unattempted». (Comparative inference)

---

## 6. Meta-selection: choosing the AS method itself

Paper B lists per-instance algorithm configuration (PIAC) and meta-selection as open problems. In Paper A's context, this maps to per-comment-class choice of *evaluator* (not just of LLM).

> **Quote (Kerschke et al.):** *"an intriguing direction for future work is the development of algorithm selection techniques for automated algorithm configurators and selectors—meta-selection might be useful for quickly identifying the selection strategy to be used in a particular application context."*

> **Quote (Gindullina et al.):** *"An LLM-expert-evaluator could quantify forecast compliance with the original comment"*

Paper A's Future-work LLM-expert-evaluator itself is a design choice: which reward model, which prompt, which base model. A meta-selector chooses among evaluator implementations per comment class. For structurally-simple comments (Class 3, numerical parameters), a rule-based verifier suffices; for semantically-complex comments (Class 4, peak position), a TRM-style Bradley-Terry model earns its cost. Meta-selection avoids paying reward-model cost when a simpler check works. (Speculative extension)

---

## 7. Algorithm configuration + per-instance selection: choose LLM *and* temperature

Paper B notes that algorithm configuration (choose parameters) generalizes selection (choose one from a set). Per-instance configuration is an open challenge.

> **Quote (Kerschke et al.):** *"Given an algorithm A whose performance (but not semantics) is affected by the settings of parameters p = (p₁, ..., p_k), a set C of possible values for p (called configurations of A), a set of problem instances I and a performance metric m, find a configuration c* ∈ C of A that achieves optimal performance on I according to m. ... The per-instance variant of the algorithm configuration problem, which can be seen as a generalisation of per-instance algorithm selection, largely remains an open challenge."*

> **Quote (Gindullina et al.):** *"All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment. ... For production deployment, a lower temperature setting (e.g., 0 or 0.2) will be applied to ensure result reproducibility and system stability."*

Paper A's global T=1.0 for testing / T≈0.2 for production is a per-set configuration choice. Per-instance configuration would set (LLM_choice, temperature, prompt_template) per comment. E.g., Class 3 (numerical) benefits from low temperature (deterministic); Class 4 (peak position, needs creative interpretation) benefits from higher temperature. Paper A operates in the per-set configuration corner of a 2D space it has not surveyed. (Comparative inference)

---

## 8. Comparison table

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Selection framing | Per-set: pick DeepSeek for all | Per-instance: pick per comment | 27% is SBS, not the ceiling (Comparative inference) |
| Instance features | Comment class/subclass (built but unused for routing) | Feature set is the linchpin | Ready-made PIAS features exist (Comparative inference) |
| Portfolio / schedule / selector | None | Three distinct designs | Choose one; don't stay at «no design» (Comparative inference) |
| Complementarity acknowledged | Only aggregate 6/25/27 reported | 100–96% VBS-SBS gap closed in SOTA | Per-comment-class complementarity untested (Comparative inference) |
| VBS baseline | Not computed | Standard evaluation reference | Add VBS from existing 60-launch data (Speculative extension) |
| Per-instance configuration | T=1.0 fixed | Configuration = choose parameters per instance | Per-class temperature likely helps (Comparative inference) |
| Meta-selection | Single evaluator planned | Meta-selection over evaluators | Match evaluator complexity to comment class (Speculative extension) |

---

## Direction 1. Build a per-instance LLM selector on the existing 60-launch data

**Pipeline stage.** §2.3 PINN Customizer + Future-work multi-agent — Adviser Agent (per essay 24) becomes a Kerschke-style PIAS selector.  
**Mechanism.** Post hoc analysis of the existing 20 comments × 3 LLMs = 60 launches:
1. Compute VBS from the data: for each comment, mark which of the 3 LLMs succeeded (per Paper A's own Criterion 4 compliance). Aggregate the best-per-comment rate.
2. Fit a simple selector (decision tree or nearest-neighbor lookup) on comment `(class, subclass)` → best-observed LLM.
3. Evaluate this selector using leave-one-comment-out cross-validation.
4. Report: current SBS 27%, computed VBS, cross-validated PIAS rate, fraction of VBS-SBS gap closed.

**Failure modes addressed.** Ambiguous framing of «best LLM»; missed complementarity between models; automation-bias risk from a single model.

**Cost.** Zero — uses existing data. Time — hours, not weeks. (Speculative extension)

---

## Direction 2. Portfolio + schedule hybrid: 8B pre-solver + 70B/DeepSeek main solver

**Pipeline stage.** §2.3 PINN Customizer — Algorithm Agent orchestration (essay 24 Direction 1 provides the multi-agent frame).  
**Mechanism.** Static schedule inspired by SATzilla / AutoFolio pre-solving:
1. Llama-8B pre-solving (compile-only): if 8B produces compilable code that passes Semantic-Checker (essay 21 AC1–AC3 approximation) within a small budget, accept. Empirical basis: 8B compile-passing rate ~50%, Criterion 3 (integrity) 100%.
2. If pre-solving fails, run Llama-70B on the comment.
3. If Llama-70B produces suspect output (e.g., large TSED divergence), run DeepSeek-V3.1 in parallel and select via Evaluator Agent.  

**Failure modes addressed.** 6% Llama-8B compliance interpreted as «8B useless» — actually 8B is fine for integrity-preserving simple modifications; 27% DeepSeek as ceiling — actually a schedule can exceed any single-LLM rate. (Speculative extension)

---

## Manuscript placement

- **§3.4 Framework performance discussion:** frame 6/25/27 as SBS distribution over three algorithms; compute and report VBS from the 60-launch data; report fraction of VBS-SBS gap that would be closed by trivial per-instance selection (clusters **1** LLM-as-optimizer, **9** DSL/constrained decoding of `dinara_comprehensive_review.md`; overlaps with essay 19 DANTE and essay 24 Malek).
- **§4 Future work:** name PIAS / per-instance configuration / meta-selection explicitly; the multi-agent architecture (essay 24) provides the natural home for a PIAS-based Adviser Agent.
- **Introduction / novelty framing:** cite Kerschke to place Paper A within the AS literature (Cluster 8 HITL and Cluster 1 LLM-as-optimizer).

## What not to transfer

Paper B is a survey covering discrete (SAT, TSP, AI planning) and continuous (BBOB) optimization; do not import problem-specific feature sets (VCG features for SAT, TSP nearest-neighbor features, ELA for BBOB) — Paper A's LLM selection uses natural-language comment features, not those. Do not treat NFL as guaranteeing per-instance selection will help — Paper B itself warns that NFL is often misapplied and that performance complementarity is what actually matters. Do not build a heavyweight AS system (SATzilla-style) on 20 comments × 3 LLMs = 60 data points — that is far below the training-set size Paper B assumes; use nearest-neighbor or a simple rule. And do not conflate per-instance selection with algorithm configuration — Paper A's temperature=1.0 is a configuration parameter, LLM choice is a selection over the set {8B, 70B, DS}. (Comparative inference)

## Concrete next experiment

**Hypothesis.** On Paper A's existing 20 comments × 3 LLMs = 60-launch dataset, computing VBS and building a nearest-neighbor per-instance LLM selector via leave-one-comment-out cross-validation will yield a cross-validated compliance rate exceeding the reported SBS of 27%.

**Protocol.**
1. Parse the 60 launches into a table: `(comment_id, class, subclass, LLM, compile_pass, MAE_matched, forecast_changed, epidemic_logic_pass, compliance_pass)`.
2. Compute VBS: for each comment_id, VBS_success = OR(compliance_pass for any LLM); aggregate rate.
3. For each comment_id, remove its 3 rows; from remaining 19 × 3 = 57 rows, learn best-LLM per (class, subclass) via majority vote; predict LLM for held-out comment; evaluate.
4. Report: SBS = 27% (DeepSeek), VBS = ?, cross-validated PIAS = ?, VBS-SBS gap fraction closed.

**Expected signal.** VBS likely 40–55% (if Llama-70B and DeepSeek disagree on 4–6 of the 20 comments, VBS = 27% + Δ × complementarity rate). Cross-validated PIAS likely 30–40% — a 3–13 percentage point improvement over SBS at zero new LLM cost. If cross-validated PIAS ≈ VBS, the selector generalizes; if far below VBS, the ontology may not be predictive.

**Ties to other essays.** Provides the empirical basis for essay 24 Direction 2 (LLM collaboration comparison) and essay 26 Direction 1 (Malan FLA on comment landscape). (Speculative extension)

## Related essays in this series

- [`16_skvorc_2020_ela_problem_space.md`](16_skvorc_2020_ela_problem_space.md) — ELA features for continuous optimization; Paper B cites ELA extensively for continuous AS.
- [`19_wei_2024_dante_active_optimization.md`](19_wei_2024_dante_active_optimization.md) — DANTE as a specific AO algorithm that would compete in a Kerschke-style portfolio.
- [`20_zhang_2026_trm_complex_reasoning.md`](20_zhang_2026_trm_complex_reasoning.md) — TRM as a candidate for the evaluator, subject to meta-selection.
- [`24_malek_2009_multi_agent_collaboration.md`](24_malek_2009_multi_agent_collaboration.md) — Adviser Agent = PIAS selector; direct architectural home for this direction.
- [`26_malan_2021_landscape_analysis_survey.md`](26_malan_2021_landscape_analysis_survey.md) — landscape features for algorithm-selector features.

## Conclusion

Paper B is not about PINNs or LLMs; it is a 2019 survey of automated algorithm selection with 40 years of intellectual history behind it. Paper A's 6%/25%/27% is exactly the pattern Paper B is designed to exploit: performance complementarity across a small algorithm set on a class of problem instances that admits cheap, informative features. Paper A already has the features (comment class/subclass). Paper A already has 60 launches of joint (LLM × instance) performance data. What is missing is one experiment — compute VBS, fit a simple per-instance selector, report the fraction of VBS-SBS gap closed — at zero new LLM cost. The Kerschke frame is precisely the frame under which «which LLM is best» becomes «which LLM is best on this specific comment class»; and it is a widely-cited, low-effort upgrade with high probability of raising the headline compliance rate by 3–13 percentage points.
