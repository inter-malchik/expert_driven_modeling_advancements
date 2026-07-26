> **Paper B — live link:** [https://doi.org/10.3390/a14020040](https://doi.org/10.3390/a14020040)  
> **Source in `src/`:** [`../src/2021 A Survey of Advances in Landscape Analysis for Optimisation.md`](../src/2021%20A%20Survey%20of%20Advances%20in%20Landscape%20Analysis%20for%20Optimisation.md)

Gindullina et al. (hereafter **Paper A**) train a PINN by optimizing a composite loss \(L = L_{data} + L_{IC} + L_{ODE}\), and expose that composite to expert-driven modifications (add penalty, reweight term). Fig. 4b/c document two catastrophic modifications (700-day outbreak from BC-weight reduction; ×4 BC reweighting producing an unrealistic plateau) that the authors describe as «effectively random rather than logically justified by epidemiological reasoning». Paper A cites Cuomo (2022) and Krishnapriyan (2021) for known PINN loss pathologies, and admits that «the use of physics-informed neural networks inherits their systemic limitations». No landscape-analytic diagnostic is applied to the modified loss surfaces themselves — no measurement of ruggedness, no visualization of basins, no comparison of the modification's loss neighborhood to the baseline's.

Malan (2021; hereafter **Paper B**) is a follow-up survey (from 2013) that catalogues 11 new landscape-analysis techniques since her earlier survey and, more consequentially, introduces four new *types* of landscapes: multiobjective, violation, dynamic and coupled, and **error / loss landscapes for neural networks**. Section 2.4 is dedicated to NN loss landscapes; Section 4 (algorithm selection applications) connects landscape features to Kerschke-style per-instance selection. The survey names LON, ELA, length-scale distribution, separability, constrained-landscape metrics, and bag-of-local-features as core techniques ready to apply to any search space with a defined objective and a neighborhood metric.

Paper B is not about PINNs or LLMs; it is a domain-agnostic survey of tools that measure landscape structure. The transferable thesis is sharp: **Paper A's PINN loss \(L = L_{data} + L_{IC} + L_{ODE}\) is a canonical example of the *error landscape* Paper B §2.4 addresses; Paper A's Criterion 3 (epidemic logic) is a *violation landscape* per Paper B §2.2; the LLM → PINN → forecast pipeline is a *coupled landscape* per Paper B §2.3; each of these three landscape types has established diagnostics that would turn Fig. 4b/c from «effectively random» into *predicted* from the loss-surface structure of the modified vs baseline PINN; and integrating those diagnostics gives Paper A a principled failure-mode taxonomy at the cost of running standard techniques on existing data.**

---

## 1. Paper A's PINN loss surface is a canonical error landscape

Paper B §2.4 describes NN error / loss landscapes as an ultra-high-dimensional optimization surface with expensive-to-evaluate objective, and notes Bosman et al.'s work adapting standard fitness-landscape-analysis (FLA) techniques to them. Paper A operates in exactly this regime.

> **Quote (Malan):** *"Analogous to a fitness landscape, the error or loss landscape can be analysed to better understand the nature of a particular NN weight optimisation problem instance. There are, however, some aspects of NN weight optimisation that make it different from most black-box optimisation problems and this affects the way that landscape analysis can be done. Some of the distinguishing characteristics of NN weight optimisation are: ultra high-dimensional search spaces (even small NN models can have thousands of weights), expensive objective evaluation (evaluating the error value of a solution weight vector involves a full run through the training data set)."*

> **Quote (Gindullina et al.):** *"The defining characteristic of the PINN methodology is the optimization of a composite loss function that includes both the data-fitting error and the residual of the equations describing the modeled process. In the context of epidemiological forecasting, the PINN loss function typically includes components corresponding to the observed data, the differential equations of the SIR model and its extensions (e.g., SEIR, SIRD), and the initial/boundary conditions."*

Paper A's loss surface is exactly Malan's «error landscape»: high-dimensional (PINN weights), expensive to evaluate (each retrain), gradient-informed (backprop). Bosman et al.'s work on how basins of attraction change under different loss functions is directly relevant: when the LLM modifies \(L\), it changes the basin structure, and the retrain (from warm start, per essay on `dinara_comprehensive_review.md` §A.2 identifiability) may land in a different basin than intended. This is *the* diagnostic Paper A needs but does not run. (Comparative inference)

---

## 2. Criterion 3 (epidemic logic) is a violation landscape

Paper B §2.2 introduces the violation landscape: a separate surface, over the same decision variables as the fitness landscape, quantifying constraint violation. Paper A's Criterion 3 (non-negativity of compartments, monotonicity of cumulative counts, asymptotic behavior) defines exactly this violation surface.

> **Quote (Malan):** *"A violation landscape is defined using the same elements as a fitness landscape, but the fitness function is replaced by a violation function that quantifies the extent to which a solution violates the constraints defined on the problem. A violation landscape is therefore defined above decision variable space and provides an additional landscape view to the fitness landscape."*

> **Quote (Gindullina et al.):** *"Compliance with the epidemic logic. The criterion verifies whether the modified forecast satisfies the fundamental requirements of the subject area. The verification includes: Non-negativity of all model compartments (SIRD model). Monotonicity of cumulative values. Asymptotic behavior consistent with the underlying epidemiological model."*

Under Paper B, Paper A's Criterion 3 rate (Fig. 5c: 100% for 8B and DeepSeek, 90% for Llama-70B) is a scalar summary of a violation landscape. The 10% violation for Llama-70B reveals *where* in the loss-mod-space Llama-70B tends to place candidates. Paper B's Technique 28 (constrained landscape metrics of Malan et al. 2015) provides the standardized measurement: feasibility ratio, feasibility-boundary crossings, fitness-violation correlation, top-quantile joint feasibility. Applying it to Paper A's 60-launch dataset would characterize *which* LLM tends to produce violation-prone modifications and for *which* comment classes. (Comparative inference)

---

## 3. The pipeline is a coupled landscape

Paper B §2.3 introduces coupled landscapes: two related surfaces that influence each other. Paper A's system operates over three coupled surfaces — LLM-decision-space, PINN-loss-space, forecast-quality-space.

> **Quote (Malan):** *"in the case of coevolution, where landscapes are coupled and influence each other. ... In the context of coevolution, there are two distinct landscapes to consider: the objective landscape (the view of the problem to be solved) and the subjective landscape (the coevolutionary algorithm's view on the problem). It has been suggested that failure of coevolutionary algorithms could be due to disassociation between these two landscapes."*

> **Quote (Gindullina et al.):** *"the module initiates the process of further training of PINN ... Upon completion of the training process, the system visualizes the resulting forecast, calculates metrics"*

Malan's phrase «disassociation between the two landscapes» is the precise diagnosis for Fig. 4b: the LLM's decision landscape (which BC-weight change *seems* to answer «shift peak by 7–10 days») is disassociated from the PINN loss landscape (which basin the modified loss reaches after warm-restart training) and again disassociated from the forecast-quality landscape (the 700-day outbreak is far from the requested outcome). Three surfaces, three points, three disassociations. Framing Paper A this way turns «effectively random» into «three-way coupled-landscape disassociation». (Comparative inference)

---

## 4. Landscape features feed algorithm selection (link to essay 25)

Paper B §4 (algorithm selection applications) is the direct bridge to Kerschke 2019 (essay 25). Landscape features are exactly the instance features a per-instance algorithm selector consumes.

> **Quote (Malan):** *"Landscape analysis has been applied widely for different purposes from the understanding of complex problems and algorithm behaviour, to predicting algorithm performance and automated algorithm selection. ... The extensive use of landscape analysis in a broad range of areas highlights the wide applicability of the techniques."*

> **Quote (Gindullina et al.):** *"The current system of rules for modifying loss functions lacks sufficient detail to provide meaningful control over the generation process."*

For Paper A, the Kerschke selector needs features per comment. Malan's ELA (Technique 24) or bag-of-local-features (Technique 29) computed on the *pre-modification* loss landscape's structure (or on a summary of the LLM's attention patterns on that comment) could feed the Adviser Agent (essay 24) with per-comment features beyond the class/subclass ontology. Even simpler: length-scale distribution (Technique 25) on a small sample of loss values around the baseline PINN measures ruggedness of the current loss neighborhood — a diagnostic Paper A does not report. (Speculative extension)

---

## 5. Loss-surface analysis explains Fig. 4b/c

Paper B repeatedly emphasizes that landscape structure predicts algorithm behavior. Paper A's Fig. 4b (700-day outbreak) is a warm-restart from the baseline PINN with the BC weight reduced — a controlled loss-surface perturbation whose consequences depend on the local basin geometry.

> **Quote (Malan):** *"Choromanska et al. theoretically and empirically analysed the loss surfaces of multilayered neural networks and found that the training and testing error became increasingly de-correlated with the size of the network. The implication of this is that finding the global optimum in the training loss landscape is of limited use, because it will most likely not correspond with the position of the global optimum in the testing loss landscape."*

> **Quote (Gindullina et al.):** *"the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days). ... the modified forecast can be considered an adequate response to the expert's semantic correction."* (referring to Fig. 4a Successful)

Malan's Choromanska-inspired warning applies with special force to Paper A: PINN training loss may be minimized (Criterion 1 «matching training data» at 66-80% for the best models) even when the *testing* forecast is catastrophic (Criterion 4 at 25-27%). Training-vs-testing landscape disassociation predicts exactly this pattern — 25-27% is a consequence of the loss landscape's structure, not just an LLM failure. (Comparative inference)

---

## 6. Length-scale and separability: which loss terms interact?

Paper B's Techniques 25 (length-scale distribution) and 27 (degree of separability) measure how gradient magnitudes vary across the search space and how much variables interact. Applied to PINN loss modifications, they would answer «are the loss terms L_data, L_IC, L_ODE separable, or does modifying one couple to the others?»

> **Quote (Malan):** *"Length scale distribution ... Based on a sample of solutions from a random Levy walk through the search space, the length scale (the absolute difference in fitness over the distance in space) is calculated for each pair of solutions in the sample. ... Degree of separability ... The degree of separability is defined as the average of the absolute values of the Pearson correlation matrix of C ... after discretisation."*

> **Quote (Gindullina et al.):** *"Rules for modifying the loss function based on the class and subclass of the expert comment. Each term represents a specific compartment: term1 (susceptible), term2 (infectious), term3 (dead), term4 (recovered). ... Add penalty to term2. ... Modification of other function components is prohibited."*

Table A.2 assumes term-level separability: modifying term2 doesn't couple to term1 or term4. Paper B's tools would test this assumption directly by computing separability on the PINN loss over training. If separability is low (which is likely — SIRD compartments are coupled by the ODE structure), then «modification of other function components is prohibited» becomes empty: any term2 modification propagates through the ODE residual to affect all four compartments. This would be a substantial diagnostic against Table A.2's implicit design. (Speculative extension)

---

## 7. Sampling + robustness: the missing pre-flight

Paper B stresses robustness of landscape measures under sampling. Paper A's evaluation samples 20 launches per LLM at T=1.0; the loss-landscape structure this samples is never characterized.

> **Quote (Malan):** *"the field of fitness landscape analysis was not very active in the evolutionary computation community ... 'despite extensive research on fitness landscape analysis and a large number of developed techniques, very few techniques are used in practice ... It is hoped that this survey will invoke renewed interest in the field of understanding complex optimisation problems and ultimately lead to better decision making on the use of appropriate metaheuristics.'"*

> **Quote (Gindullina et al.):** *"All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment."*

Malan's own 2013→2021 arc is that landscape analysis was theoretically rich but practically underused. Paper A is a case study of the underuse: it has a loss landscape, a violation landscape, and a coupled pipeline, and it applies zero landscape techniques before running LLM-generated modifications. A pre-flight landscape characterization of each comment class's base-PINN loss surface would (a) predict which modifications are likely to be catastrophic, (b) inform the ontology-slot-facet numeric ranges (essay 22), and (c) support the Adviser Agent's routing decisions (essay 24). (Speculative extension)

---

## 8. Comparison table

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| PINN loss as error landscape | Optimized, not analyzed | §2.4 error landscape framework | Bosman-style analysis directly applies (Comparative inference) |
| Epidemic-logic as violation landscape | Criterion 3 as scalar rate | §2.2 constrained-landscape metrics (Tech 28) | 5-value vector characterization available (Comparative inference) |
| LLM → PINN → forecast coupling | Three surfaces, no coupling analysis | §2.3 coupled landscapes | Fig. 4b/c = three-way disassociation (Comparative inference) |
| Landscape features → AS | Ontology as features (essay 25) | §4 landscape features feed AS | Add ELA/length-scale to feature set (Speculative extension) |
| Training-vs-testing landscape | Not distinguished | Choromanska: increasingly decorrelated | Explains 66-80% Criterion 1 vs 25-27% Criterion 4 (Empirically shown for B) |
| Separability assumption | Table A.2 implicit | Technique 27 measures directly | «Modification of other terms prohibited» is untested (Comparative inference) |
| Landscape techniques applied | Zero | 33 catalogued techniques | Underuse persists (Comparative inference) |

---

## Direction 1. Landscape pre-flight over comment-class-specific loss surfaces

**Pipeline stage.** §2.3 PINN Customizer + Adviser Agent (essay 24 Direction 1).  
**Mechanism.** For each comment class, before LLM invocation, compute a landscape summary of the base PINN loss surface:
- **Ruggedness**: length-scale distribution (Malan Tech 25) over a small sample of nearby weight vectors (~50 samples).
- **Separability**: pairwise correlation matrix (Tech 27) over term-wise gradient contributions.
- **Basin structure**: mini-LON (Tech 23) over local optima reachable by 20 short gradient descents from perturbed initial points.
- **Violation surface**: constrained metrics (Tech 28) evaluating how close the base solution is to non-negativity violation, monotonicity violation, or asymptotic-deviation.

The Adviser Agent uses these features (per comment class × landscape summary) to route to LLM + configure temperature.

**Failure modes addressed.** «Effectively random» framing of Fig. 4b/c — replaced with «high-violation-boundary-crossing surface, expected outcome type». Ontology-slot ranges (essay 22 Direction 2) get evidence-based bounds from landscape structure. (Speculative extension)

---

## Direction 2. Coupled-landscape disassociation as an early-warning diagnostic

**Pipeline stage.** Evaluation loop + Semantic-Checker Agent.  
**Mechanism.** After LLM emits a modification but before full PINN retrain, compute three-way landscape correlations:
1. **LLM-decision-landscape**: sample k=8 modifications for the same comment; compute pairwise TSED (already used in Paper A). Divergence in this landscape = LLM uncertainty.
2. **PINN-loss-landscape shift**: compare loss surface curvature (via Hessian trace approximation on small sample) between baseline and each candidate modification. Large shift = risky basin change.
3. **Forecast-landscape shift** (cheap surrogate): evaluate the modified loss's *baseline forecast* prediction — no retrain, just forward pass on training data — and compare to baseline PINN's prediction. Divergent = modification breaks data-fit.

If landscapes 1–3 are pairwise weakly-correlated on a comment, flag it as high-risk (Fig. 4b/c-type) before the expensive retrain.

**Failure modes addressed.** Fig. 4b/c only discovered *after* expensive retrain. Cheap pre-checks reroute LLM effort. (Speculative extension)

---

## Manuscript placement

- **§4 Limitations «systemic limitations of PINN»:** cite Malan §2.4 (error landscape framework) and Bosman et al. as the canonical NN-loss-landscape literature; frame Fig. 4b/c as coupled-landscape disassociation.
- **§4 Future work:** add landscape pre-flight to the multi-agent architecture (essay 24) — the Adviser Agent uses landscape features (essay 25 Kerschke) computed via Malan's techniques (this essay).
- **§3.3 Discussion of Fig. 4:** relabel «effectively random» as consistent with training-vs-testing landscape decorrelation (Choromanska; Paper B §2.4) — a diagnosable event, not a mystery (clusters **5** loss-weight balancing, **6** identifiability of `dinara_comprehensive_review.md`).

## What not to transfer

Paper B is a survey — do not import all 33 techniques (many are combinatorial-specific: LON for QAP, causal-graph features for AI planning). Only a subset applies to Paper A's continuous PINN weight space: ELA (Tech 24), length-scale distribution (Tech 25), separability (Tech 27), constrained metrics (Tech 28), and error-landscape adaptations from Bosman et al. Do not treat LON as directly applicable to continuous PINN weights — Paper B notes LON extensions to continuous spaces are approximate and non-standard. And do not compute all landscape features on all 20 comments × 3 LLMs × k=8 candidates = 480 landscape summaries — start with one or two techniques on the top-3 highest-priority comment classes, then scale. (Comparative inference)

## Concrete next experiment

**Hypothesis.** On the 20 comments Paper A already has, comparing landscape summaries (length-scale distribution + separability degree) of the baseline PINN loss vs each of the 60 LLM-modified losses will reveal a monotonic relationship between landscape-shift magnitude and Fig. 4b/c-type catastrophic outcomes.

**Protocol.**
1. For each of the 60 modifications (20 comments × 3 LLMs), sample 50 nearby weight vectors from the current PINN weights.
2. Compute length-scale distribution and separability degree on baseline and modified loss.
3. Compute distributional shift (KL divergence between length-scale distributions; L2 shift in separability index).
4. Label each modification as `successful` / `ambiguous` / `unsuccessful` per Paper A's own trichotomy.
5. Fit logistic regression: `outcome ~ landscape_shift`. Report AUC and coefficient sign.

**Expected signal.** Modifications with large landscape shift map to unsuccessful outcomes; small shift maps to no-change (15-28% of Paper A's cases where «forecast unchanged»); moderate shift maps to successful outcomes. If AUC ≥ 0.75, landscape shift is a practical pre-flight filter. If AUC < 0.6, either landscape summaries are insufficient or additional signals are needed (e.g., coupled-landscape from Direction 2).

**Cost.** ~1 hour compute per modification × 60 = 60 hours; feasible with existing infrastructure. (Speculative extension)

## Related essays in this series

- [`11_daza_2016_basin_entropy.md`](11_daza_2016_basin_entropy.md) — basin entropy = a specific landscape uncertainty diagnostic; complementary to Malan's techniques.
- [`16_skvorc_2020_ela_problem_space.md`](16_skvorc_2020_ela_problem_space.md) — ELA for continuous problems; Malan Tech 24 in more detail.
- [`19_wei_2024_dante_active_optimization.md`](19_wei_2024_dante_active_optimization.md) — surrogate over search landscape; Malan's warning that surrogate landscape analysis is «not yet successful» applies here.
- [`25_kerschke_2019_algorithm_selection_survey.md`](25_kerschke_2019_algorithm_selection_survey.md) — landscape features feed the AS pipeline; Kerschke + Malan are complementary.

## Conclusion

Paper B is a 2021 survey of fitness landscape analysis, extended to cover the four new landscape types that most closely fit Paper A's problem: multiobjective (composite loss), violation (epidemic logic), coupled (LLM → PINN → forecast), and error (NN weight optimization). Paper A applies zero landscape techniques to any of these surfaces despite operating over all four. Framing Fig. 4b/c as coupled-landscape disassociation, framing Criterion 3 as a violation landscape metric, and running a lightweight pre-flight landscape summary before LLM invocation transforms Paper A's most-discussed failures from mysteries into diagnosable events. The techniques exist, the tools exist (flacco, R), and the cost is a fraction of the PINN retraining cost. Malan's own thesis in 2013→2021 is that the field is under-applied; Paper A is a case study of that under-application.
