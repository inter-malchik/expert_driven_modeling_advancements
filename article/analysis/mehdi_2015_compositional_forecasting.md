> **Paper B — live link:** [https://doi.org/10.1007/978-3-319-23540-0_12](https://doi.org/10.1007/978-3-319-23540-0_12)  
> **Source in `src/`:** [`../src/2015 Modeling and Forecasting Time Series of Compositional Data.md`](../src/2015%20Modeling%20and%20Forecasting%20Time%20Series%20of%20Compositional%20Data.md)

Gindullina et al. (hereafter **Paper A**) score Expert-Guided PINN with four criteria: MAE ≤ 1100 on training fit, MAE ≥ 700 as “forecast changed,” hard epidemic-logic checks on SIRD compartments, and a subjective primary—“Compliance with the comment” at 25–27% best. SIRD outputs are *shares of a closed population* evolving in time, yet evaluation never treats them as compositional time series: no proper forecast MSE on proportions, no residual-correlation diagnostics, no comparison against a proportion-aware baseline.

Mehdi, Epaillard, Bouguila, and Bentahar (2015; hereafter **Paper B**) build **GDPSM**—a generalized Dirichlet power steady model for compositional series \(X^t\) that sum to one. They transform GD → \(d\) Beta → unidimensional Dirichlet exponential forms, train on 20 steps / test 980, sweep \(\gamma\), and score with **MSE**, **standardized residuals**, and **lag-0 residual correlations**. Against DPSM, GDPSM often cuts MSE by 2–3× (e.g., 3-class trig \(\gamma=0.001\), Dim1 MSE \(0.166\to 0.067\)) and drives residual correlations near zero (\(-0.4529\to -0.0092\)).

The transferable thesis is sharp: **replace or hard-complement Paper A’s subjective compliance and raw MAE 700/1100 with GDPSM-style proper scoring on SIRD compartment shares—MSE plus residual correlation—so “success” is measurable on proportions, not author impression.**

---

## 1. SIRD compartments are compositional series

Paper A’s PINN is built on SIRD equations; Table A.2 edits term1–term4 (S, I, D, R). Those four trajectories are constrained shares of a population—compositional structure Paper B’s opening already names as the reason standard ARIMA/Kalman fail.

> **Quote (Gindullina et al.):** *"we used a PINN’s architecture based on the SIRD model equations from Abramova and Leonenko (2024)"*

> **Quote (Mehdi et al.):** *"Generally, time series of compositional data are multivariate and denoted by time-dependent vectors of proportions that sum to one… due to the positive nature of the components of compositional data and their sum to one constraint, these techniques are not applicable."*

Treating infected MAE alone as the change gate ignores that a “successful” I-edit can silently break the simplex geometry of \((S,I,R,D)\). (Comparative inference)

---

## 2. Subjective compliance vs MSE of predictions

Paper A’s primary success is visual match of comment to plot. Paper B’s primary quantitative claim is lower prediction MSE on held-out compositional steps—objective, repeatable, and independent of author satisfaction.

> **Quote (Gindullina et al.):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the \"Compliance with the comment\" criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results."*

> **Quote (Mehdi et al.):** *"We evaluate our model by the standardized residuals, the mean squared error (MSE) of the predictions, and the correlations between the residuals at lag 0."*

> **Quote (Mehdi et al.):** *"Table 1 (right) shows the MSE of both GDPSM and DPSM which demonstrate that our model yields more accurate predictions than DPSM for both dimensions."*

An LLM-expert-evaluator that only rephrases visual compliance still inherits subjectivity. MSE on normalized compartment shares after an edit is a proper forecast score the evaluator could be required to cite. (Comparative inference)

---

## 3. Residual correlation as a model-quality gate Paper A lacks

Paper A’s “Forecast has changed” (MAE > 700) conflates *any* large move with a *well-specified* move. Paper B treats strong residual correlations as evidence that the model still misses structure—even when MSE looks acceptable.

> **Quote (Mehdi et al.):** *"These correlations are additional indicators of the model quality; the weaker the correlations the better the model. Stronger correlations imply that further modeling is necessary to better fit the time series."*

> **Quote (Mehdi et al.):** *"The correlations at lag 0 between the residuals of the first two dimensions computed by DPSM and GDPSM are \(-0.4529\) and \(-0.0092\), respectively. This shows that our model explains the time series better than DPSM."*

> **Quote (Gindullina et al.):** *"The forecast for infected cases is considered to have changed significantly if the calculated MAE exceeds this value… LLMs can only slightly change the loss function or simply add some constants, which will not change our forecast."*

Transfer: after a comment-driven retrain, report residual correlations among \(\{S,I,R,D\}\) (or among transformed shares). A run that clears MAE-700 but spikes cross-compartment residual correlation is a bad edit, not a success. (Comparative inference)

---

## 4. MAE 700/1100 are empirical magnitude gates, not proportion scores

Paper A chooses 700 and 1100 empirically on incidence scale. Paper B scores on transformed proportion space (symmetric log-ratio / DirBeta coordinates), so errors are comparable across dimensions that sum to one.

> **Quote (Gindullina et al.):** *"A value of 1100 was empirically chosen as the threshold… MAE… A value greater than this threshold indicates a catastrophic loss of model adequacy during modification."*

> **Quote (Gindullina et al.):** *"The lower threshold of significance was determined empirically using test data - MAE greater than 700."*

> **Quote (Mehdi et al.):** *"for \(\gamma=0.001\)… Dimension 1 DPSM… 0.166… GDPSM… 0.067"*

Raw case-count MAE cannot tell whether an edit preserved compositional coherence; proportion MSE can. Keep 700/1100 as secondary magnitude filters; make share-MSE primary for “matching training data” on compartments. (Comparative inference)

---

## 5. Partitioned Beta/Dirichlet problems vs monolithic loss rewrite

Paper B’s methodological claim is that splitting a \((d+1)\)-composition into \(d\) smaller exponential-family problems improves forecasts. Paper A rewrites the *entire* loss in one LLM shot under coarse Table A.2 prohibitions.

> **Quote (Mehdi et al.):** *"We demonstrate that dividing the modeling problem into multiple smaller problems leads to more accurate predictions."*

> **Quote (Mehdi et al.):** *"This approach partitions the modeling and forecasting of \((d + 1)\)-dimensional time series into \(d\) smaller problems with fewer parameters to learn."*

> **Quote (Gindullina et al.):** *"The current system of rules for modifying loss functions lacks sufficient detail to provide meaningful control over the generation process."*

Class/subclass templates that edit *one compartment share’s penalty* (term2 only) while scoring all shares jointly is closer to GDPSM’s partition than to free whole-loss rewrite. (Comparative inference)

---

## 6. Epidemic logic checks vs positivity/unit-sum modeling

Paper A’s criterion 3 verifies non-negativity and cumulative monotonicity after the fact. Paper B builds positivity and unit-sum into the observation model from the start.

> **Quote (Gindullina et al.):** *"Compliance with the epidemic logic… Non-negativity of all model compartments (SIRD model). Monotonicity of cumulative values."*

> **Quote (Mehdi et al.):** *"Let \(X = (X_1,\ldots,X_{d+1})\) denote a vector of proportions that follows a \(d\)-dimensional GD distribution… for \(\sum_{l=1}^d X_l < 1\) and \(0 < X_l < 1\)."*

Post-hoc logic filters catch some disasters; they do not score forecast skill on the simplex. A compositional scoring layer would fail closed on Fig. 4c plateaus that “satisfy” logic but destroy share dynamics. (Comparative inference)

---

## 7. \(\gamma\)-sweep and temperature: sensitivity Paper A under-reports

Paper A explores LLM temperature 1.0 for diversity but does not sweep a continuous forgetting/dispersion parameter on the forecast score itself. Paper B’s \(\gamma\in(0,1)\) explicitly trades prediction sharpness; \(\gamma=0.999\) degrades both models.

> **Quote (Mehdi et al.):** *"we compare GDPSM and DPSM with the data obtained from Simulation 1 for 5 different values of \(\gamma = \{0.001, 0.250, 0.500, 0.750, 0.999\}\), averaged over 10 runs"*

> **Quote (Mehdi et al.):** *"other values of \(\gamma\) give equivalent results with the exception of \(\gamma = 0.999\) that leads to significantly degraded results."*

> **Quote (Gindullina et al.):** *"All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment."*

A fair Expert-Guided PINN ablation would sweep scoring hyperparameters (share-MSE windows, residual lag) the way Paper B sweeps \(\gamma\)—not only LLM scale. (Comparative inference)

---

## 8. LLM-expert-evaluator needs proper scores as features

Paper A’s Future work proposes an evaluator LLM to “quantify forecast compliance” without specifying numeric features. Paper B already lists the features that make compositional forecast quality auditable.

> **Quote (Gindullina et al.):** *"An LLM-expert-evaluator could quantify forecast compliance with the original comment; low confidence scores could trigger automatic loss regeneration or comment refinement."*

> **Quote (Mehdi et al.):** *"We show the merits of our model via standardized residuals and mean squared error (MSE) of the predictions."*

> **Quote (Mehdi et al.):** *"The experimental results show that our model performs better than a single Dirichlet PSM in terms of standardized residuals and goodness-of-fit of the predictions."*

Bind the evaluator: must cite share-MSE and max |residual correlation| before emitting a compliance label. (Speculative extension)

---

## 9. Comparison table

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Object of forecast | Infected incidence curve (+ SIRD PINN) | Quality-class proportion vectors \(\sum=1\) | SIRD shares ≈ compositional series (Comparative inference) |
| Primary success | Subjective comment compliance 25–27% | MSE of predictions on test proportions | Proper score > visual match (Comparative inference) |
| Secondary diagnostics | MAE 700 / 1100; epidemic logic | Standardized residuals; lag-0 residual corr. | Residual corr. catches bad structure (Empirically shown in B) |
| Empirical headline | Proof-of-concept feasibility | GDPSM MSE often 2–3× lower than DPSM | Show numbers, not only % compliance (Author-stated in both) |
| Model structure | One LLM rewrite of full loss | \(d\) partitioned DirBeta PSMs | Prefer compartment-scoped edits + joint score (Comparative inference) |
| Constraints | Post-hoc non-negativity / monotonicity | Built-in simplex / GD support | Encode shares in scoring, not only filters (Comparative inference) |
| Sensitivity protocol | Temperature 1.0; 3 LLM scales | \(\gamma\)-sweep; 10-run averages | Sweep score params, not only models (Comparative inference) |

---

## Direction 1. Compositional scorecard beside Fig. 5

**Pipeline stage:** Evaluation Approach (§2.4) / Future work LLM-expert-evaluator.  
**Mechanism:** After each accepted retrain, convert SIRD trajectories to shares; report (i) MSE vs baseline shares on training window, (ii) standardized residuals, (iii) lag-0 residual correlation matrix. Require the evaluator to cite these before binary “compliant.”  
**Failure modes addressed:** subjective primary metric; MAE-only “changed” gate; silent share incoherence under term2 penalties.  
**Acceptance:** publish residual-corr and share-MSE columns next to compliance %. (Speculative extension)

---

## Direction 2. Template edits scoped like GDPSM partitions

**Pipeline stage:** PINN Customizer / class–subclass templates.  
**Mechanism:** Map Table A.2 “Add penalty to term\(k\)” to a single-share penalty while the score always evaluates the full 4-vector on the simplex—mirroring Paper B’s \(d\) small problems with joint compositional metrics.  
**Failure modes addressed:** whole-loss rewrites that move I while corrupting S/R/D correlations (Fig. 4 ambiguous/unsuccessful).  
**Acceptance:** ablate partitioned vs whole-loss rewrite under identical comments. (Speculative extension)

---

## Direction 3. Keep MAE 700/1100 as secondary magnitude only

**Pipeline stage:** Evaluation criteria redesign.  
**Mechanism:** Demote empirical MAE gates to alerts; promote share-MSE and residual correlation to primary automatic filters before human compliance judgment.  
**Failure modes addressed:** scale-dependent thresholds that do not respect unit-sum geometry. (Speculative extension)

---

---

## Manuscript placement

- **§2.4 Evaluation Approach + Results:** promote share-MSE / residual correlations over MAE 700/1100 and subjective compliance (cluster **4**).
- **§2.3 / templates:** partition edits like GD→d Betas (cluster **9** secondary).
- **Limitations:** unit-sum geometry of SIRD compartments.

## What not to transfer

QoS web-service GDPSM simulations are not epidemic surveillance. No LLM/HITL in Paper B. Transfer **compositional scoring (MSE, residuals, residual corr on shares)**—not power-steady Kalman machinery as a PINN replacement. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Ranking runs by share-MSE + |residual corr| disagrees with author binary compliance and with raw MAE gates.

**Protocol.** For each accepted retrain: \(s=(S,I,R,D)/\mathrm{pop}\) (or renormalize); compute share-MSE vs baseline on train window; lag-0 residual correlation; keep MAE 700/1100 as secondary alerts only.

**Metric.** Spearman ρ(compliance, share-MSE); flip rate of pass/fail when MAE gates replaced by share-MSE quantile. Expect weak ρ and nontrivial flips. (Speculative extension)

## Related essays in this series

- [`16_skvorc_2020_ela_problem_space.md`](16_skvorc_2020_ela_problem_space.md) — scale/normalization hygiene.
- [`04_miller_2020_contrastive_explanation.md`](04_miller_2020_contrastive_explanation.md) — foils on share features.
- [`01_hidalgo_2018_glucose_grammatical_evolution.md`](01_hidalgo_2018_glucose_grammatical_evolution.md) — zone scoring cousin.
- Bridge: Forecast Hub / WIS discussion in `../dinara_comprehensive_review.md` cluster 4.


## Conclusion

Mehdi et al. show how to evaluate forecasts when the object is a vector of proportions: MSE, residuals, and residual correlations—not author visual agreement. Expert-Guided PINN’s SIRD compartments are compositional in exactly that sense, yet Paper A still leads with subjective compliance and empirical MAE thresholds. The sharp transfer is metrological: keep comment-following as a *task*, but score it with GDPSM-style proper metrics on compartment shares. Until share-MSE and residual correlations appear beside the 25–27% bar, “forecast quality after expert edit” remains under-measured.

