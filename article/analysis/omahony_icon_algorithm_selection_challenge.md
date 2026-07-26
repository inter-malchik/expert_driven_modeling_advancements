Paper A (Gindullina et al., Expert-Guided PINN) compares three off-the-shelf LLMs on an ad hoc battery of four qualitative criteria—MAE thresholds 700 and 1100 chosen empirically, twenty launches per model at temperature 1.0, and a primary “Compliance with the comment” score judged without formalised rubrics. Paper B (Kotthoff, Hurley, and O’Sullivan, 2017, *The ICON Challenge on Algorithm Selection*) addresses the same meta-problem in algorithm selection: before ICON, “evaluations often use different data sets, different performance measures, and different experimental setups,” so “the results are not directly comparable.” ICON’s response was shared infrastructure (ASlib scenarios), mandatory source code, bootstrap train/test splits, and a **normalised score** where 0 is oracle per-instance algorithm choice and 1 is always picking the single best solver—making gaps to perfection explicit.

The comparative payoff is methodological, not domain-identical: Paper A’s pipeline implicitly **selects** among LLM backends and loss modifications per expert comment, yet evaluates that selection loop without a public benchmark, without an oracle ceiling, and without separating instruction-following from forecast quality on held-out epidemic data (Comparative inference). Paper B shows that even after standardisation, the winning system (zilla, score 0.366) remains **far from oracle** while still beating the single-best baseline—an honest reporting template Paper A could mirror by publishing joint success rates, confidence intervals, and epidemiological proper scores (Cluster 3: algorithm/portfolio selection; Cluster 4: evaluation rigour).

---

## 1. The incomparability problem Paper B was built to fix

> **Quote (Kotthoff et al.):** *«While the majority of these have been evaluated empirically in the literature, such evaluations often use different data sets, different performance measures, and different experimental setups. The results are not directly comparable and do not provide a clear picture of the state of the art.»*

> **Quote (Kotthoff et al.):** *«The ICON Challenge on Algorithm Selection provided the first comprehensive, objective evaluation of several state-of-the-art approaches. Its results gave an overview of the state of the art at the time of the competition, highlighting the strengths and weaknesses of different approaches.»*

Paper A introduces its own evaluation precisely because no standard exists for semantic forecast–comment alignment:

> **Quote (Gindullina et al.):** *«Due to the lack of standardized numerical metrics for assessing the semantic correspondence of a forecast to an expert’s textual commentary, a system of qualitative validation criteria was developed.»*

That admission is Author-stated. The gap is that Paper A stops at bespoke criteria rather than contributing a **reusable benchmark** the way ASlib does for solvers (Comparative inference). Future validation at the Smorodintsev Institute is planned, but no pre-registered evaluation package accompanies the proof-of-concept (Author-stated).

---

## 2. Shared benchmark library versus single-site ad hoc runs

ICON anchored all entrants to ASlib release 1.0:

> **Quote (Kotthoff et al.):** *«The challenge leveraged the ASlib benchmark library for algorithm selection (Bischl et al. 2016). We used thirteen scenarios, drawn from prominent publications, in release 1.0. They represent a number of important AI application areas, including SAT, CSP, QBF, ASP, and heuristic search.»*

> **Quote (Kotthoff et al.):** *«All submissions were required to provide the full source code, with instructions on how to run the system. The submissions, full details of the challenge, along with detailed results and all data used in the evaluation, are available at http://challenge.icon-fet.eu/.»*

Paper A releases code on GitHub but evaluates on **one** St Petersburg COVID wave (359 days), one PINN architecture, and comment scenarios that are not packaged as a downloadable scenario set with fixed train/test splits (Author-stated from methodology). Cross-paper replication of “25% vs 27% DeepSeek vs Llama-70B” is therefore as hard as pre-ICON comparisons of SATzilla variants—exactly the problem ICON eliminated for combinatorial solvers (Comparative inference).

---

## 3. Bootstrap protocol and small-sample instability

ICON trained on bootstrap resamples and tested on held-out portions:

> **Quote (Kotthoff et al.):** *«Since the ASlib dataset is public and was available to contestants before they submitted their system, the submissions were trained on ten different bootstrap samples of a scenario and evaluated on the remaining data.»*

Paper A reports **twenty launches** at temperature 1.0 (Fig. 3–5) and applies a Nemenyi post-hoc test only to **TSED** code similarity—not to “Compliance with the comment” (Author-stated). At n≈20 and success rate ≈0.25, binomial uncertainty is wide; treating 25% versus 27% as meaningful model ranking mirrors pre-ICON papers that declared winners without shared splits (Comparative inference; cf. dinara_comprehensive_review.md §2). ICON’s bootstrap design explicitly guards against **split luck**; Paper A has no analogous resampling for comment instances.

---

## 4. Oracle-normalised scoring versus empirical MAE thresholds

ICON’s leaderboard used a transparent scale:

> **Quote (Kotthoff et al.):** *«Scores were aggregated over all scenarios and samples, with 0 corresponding to perfect predictions where on each problem instance the optimal algorithm is chosen (oracle) and 1 corresponding to a static predictor that chooses the overall best algorithm on each problem instance (single best).»*

Winner zilla scored **0.36603**—substantially better than single-best (1.0 scale anchor) yet far from oracle (0.0) (Empirically shown).

Paper A uses empirically chosen MAE cut-offs:

> **Quote (Gindullina et al.):** *«A value of 1100 was empirically chosen as the threshold for successfully meeting this criterion»* for matching training data, and *«MAE greater than 700»* for “forecast has changed,” both *«determined empirically using test data»* (§2.4).

There is no **oracle** row (perfect comment satisfaction on all instances), no **single-best LLM** normalisation across the comment suite, and no published **joint** conjunction of all four criteria—only marginal bars in Fig. 5 (Comparative inference; dinara_comprehensive_review.md §B.5). A ICON-style report might read: “DeepSeek 0.27 on primary metric; oracle 1.0; best single-metric marginal 0.85 on ‘forecast changed’”—making the feasibility gap legible (Speculative extension).

---

## 5. Beating the baseline is not enough—and Paper A says so

ICON emphasises remaining headroom:

> **Quote (Kotthoff et al.):** *«All submissions achieve significant performance improvements over always choosing a single algorithm.»*

> **Quote (Kotthoff et al.):** *«Nevertheless, there is scope for improvement. Even the best approach is still far away from being a perfect predictor.»*

> **Quote (Kotthoff et al.):** *«Especially the industrial SAT scenarios turned out to be challenging, with many systems not even achieving the performance of the single best solver.»*

Paper A’s tone is parallel but its metrics obscure the ceiling:

> **Quote (Gindullina et al.):** *«The key result is confirmation of the fundamental feasibility of integrating expert knowledge through LLM into PINN, with a success rate of 25-27% for the best models (Figure 5). These results should be considered proof-of-concept»* (§3.4).

Feasibility is Author-stated; the **distance to oracle** is not quantified. Meanwhile 80–85% on “forecast has changed” (Fig. 5) can suggest competence while primary compliance stays near 0.25—analogous to ICON entrants that beat single-best on average yet fail on hard industrial SAT scenarios (Comparative inference). Hard “scenarios” in Paper A include peak-shift and post-peak shape comments (Fig. 4); they are illustrated qualitatively, not scored as a structured scenario library.

---

## 6. Algorithm selection without the algorithm-selection evaluation stack

ICON situates itself in Rice’s algorithm selection problem and portfolio literature, citing O’Mahony et al. (2008) among precursors (Author-stated in Paper B). Paper A **selects** among Llama-8B, Llama-70B, and DeepSeek-V3.1 per run and among loss edits per comment class, but does not frame the task as **instance-level selection** (comment features → LLM / template / loss operator) nor release ASlib-style **instance features** and labels.

> **Quote (Gindullina et al.):** *«To empirically evaluate the impact of model scale on the quality of expert comment interpretation and the generation of correct loss functions, three models with different parameter sizes were selected»* (§2.4).

That is a **model-scale ablation**, not a portfolio selector evaluated under bootstrap with an oracle bound (Comparative inference). A SATzilla-like meta-learner over comment embeddings, class/subclass, and compile-history could be benchmarked on the same splits ICON uses—if Paper A first defined the splits (Speculative extension).

---

## 7. Subjective primary metric versus challenge-grade objectivity

Paper A’s Limitations acknowledge evaluation weakness:

> **Quote (Gindullina et al.):** *«The proposed approach to evaluating results has a significant subjective component, particularly in the "Compliance with the comment" criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results.»*

ICON’s primary scores are **runtime-based** and aggregated automatically from solver schedules—no human judge per instance. Paper A proposes a future LLM evaluator but does not implement it:

> **Quote (Gindullina et al.):** *«An LLM-expert-evaluator could quantify forecast compliance with the original comment; low confidence scores could trigger automatic loss regeneration»* (Future work).

That roadmap mirrors moving from idiosyncratic paper metrics to **challenge infrastructure**, but without meta-validation against human experts it risks replacing one subjective layer with another—ICON avoided this by fixing the scoring function upfront (Comparative inference; Cluster 3 LLM-as-judge literature in dinara_comprehensive_review.md).

---

## 8. Evaluation protocol includes cost—and production config

ICON allowed entrants to trade feature cost against performance:

> **Quote (Kotthoff et al.):** *«the problem features they wanted their submission to have access to (feature computation incurs a cost that may reduce overall performance)»* and optional *«presolver for a small amount of time, thereby reducing the overhead of feature computation and the selection process on easy instances.»*

Paper A acknowledges computational cost of iterative compile-fix loops but excludes it from success metrics (Author-stated). It also evaluates at **temperature 1.0** while stating production will use 0–0.2:

> **Quote (Gindullina et al.):** *«All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment. This setting was used exclusively during the testing and prototyping phase»*; *«For production deployment, a lower temperature setting (e.g., 0 or 0.2) will be applied»* (§2.4).

Reporting headline compliance at a non-production configuration without a sweep parallels pre-ICON papers that tuned systems on the test bed—ICON’s fixed protocol prevented such drift (Comparative inference). A challenge-grade evaluation would report compliance–cost–latency jointly, as ICON implicitly does via runtime-based scores.

---

## 9. Comparison table

| Criterion | Paper A (Expert-Guided PINN) | Paper B (ICON Challenge) | Takeaway |
| :--- | :--- | :--- | :--- |
| Evaluation motive | No standard for comment–forecast fit | Prior AS papers incomparable | Both recognise metric crisis; only B standardises |
| Benchmark | Single epidemic series; ad hoc comments | ASlib v1.0; 13 scenarios | A lacks reusable scenario library |
| Sample design | 20 launches; T=1.0 | 10 bootstrap splits per scenario | A vulnerable to split noise |
| Score scale | Binary/percent per criterion; MAE 700/1100 | 0 = oracle, 1 = single-best | B makes optimality gap explicit |
| Best result | 25–27% comment compliance | zilla 0.366 aggregated | Both far from perfection; B quantifies it |
| Code/data | GitHub; data on request | Full submissions + challenge URL | A below ICON reproducibility bar |
| Primary metric | Subjective compliance | Automated runtime score | A’s headline metric is Author-stated weak |

---

## Direction 1. Expert-Comment Benchmark Suite (ECBS)

**Stage:** Evaluation (§2.4) and data release. **Mechanism:** Curate fixed comment instances with expert-authored references (target functionals: peak day shift Δt, post-peak slope sign), train/test split, public JSON like ASlib—released before model comparisons. **Failure mode:** Non-comparable 25% vs 27% claims; irreproducible classifier training (Speculative extension; modeled on Paper B’s ASlib).

## Direction 2. Oracle and single-best anchors on the primary metric

**Stage:** Results reporting (Fig. 5). **Mechanism:** Define oracle (human-written loss or GUI baseline per Sahatova 2023) and single-best LLM per comment class; normalise compliance to [0,1] ICON-style. Report joint success across all four criteria. **Failure mode:** Marginal Fig. 5 bars overstating utility (Comparative inference → Speculative extension).

## Direction 3. Bootstrap evaluation at n≈20

**Stage:** PINN Customizer experiments. **Mechanism:** Resample comment instances with replacement (10× minimum); report mean and 95% CI on compliance; apply Nemenyi or Friedman to **primary** metric, not only TSED. **Failure mode:** Declaring DeepSeek “best” within noise (Empirically motivated gap from dinara_comprehensive_review.md).

## Direction 4. Instance-level LLM portfolio selector

**Stage:** PINN Customizer model choice. **Mechanism:** Train selector on comment features (class, length, numerals) → LLM/backend; evaluate under ICON bootstrap protocol against always-Llama-70B. **Failure mode:** Treating scale as sufficient selection policy (Comparative inference).

## Direction 5. Hold-out epidemic scoring (Forecast Hub alignment)

**Stage:** Retraining loop outcomes. **Mechanism:** Complement instruction-following with WIS or MAE on **future** incidence hold-out (Cluster 4 proper scoring)—parallel to ICON’s runtime penalty beyond solver correctness. **Failure mode:** Instruction-following without forecast improvement (dinara_comprehensive_review.md §C.8) (Speculative extension).

---

## Conclusion

Kotthoff, Hurley, and O’Sullivan’s ICON Challenge did not solve algorithm selection, but it **made progress measurable**: shared scenarios, bootstrap evaluation, open submissions, and oracle-normalised scores that show top systems beating single-best yet remaining far from perfect. Gindullina et al. honestly report proof-of-concept compliance near 25–27% and admit subjective, non-standardised evaluation—but stop short of building the epidemiological analogue of ASlib or ICON. Treating Expert-Guided PINN as a **selection system** (LLM × comment instance → loss edit) without ICON-grade infrastructure reproduces the pre-2017 comparability problem in a new domain. The actionable import is not to run a public competition immediately, but to adopt ICON’s reporting discipline: public scenario libraries, bootstrap uncertainty, oracle baselines, and separation of easy marginal metrics from the hard primary score—before scaling to operational epidemic forecasting.
