Paper A (Gindullina et al., «Expert-guided forecasting of epidemic ARI incidence based on physics-informed neural networks and large language models») evaluates success of loss modifications against four qualitative criteria with MAE thresholds of 700 and 1100, chosen empirically, and against subjective compliance with the comment at n=20 and temperature=1.0. Each iteration includes expensive PINN retraining, and the authors do not separate retraining noise from the effect of the LLM edit.

Paper B (Scott and De Jong, 2016, «Landscape Features for Computationally Expensive Evaluation Functions: Revisiting the Problem of Noise») shows on BBOB: cheap landscape features on a hill-climber break down at p around 10⁻³, explicit averaging at N=15 does not help, population-based search gives implicit averaging but changes what is being measured.

Distinction from essay #41 (Malan, gradient walk): there the geometry of neural-network error-landscape sampling; here noise in cheap metrics under a limited evaluation budget. Both are cluster 5, but the angle differs: sampling bias vs measurement fragility.

## 1. Expensive evaluation and cheap diagnostics

Retraining the PINN after each loss edit is a computationally costly black-box call, comparable to expensive simulations in metaheuristics.

> **Quote (Scott and De Jong):** *«These applications tend to involve fitness functions that are very expensive to compute—each evaluation taking on the order of seconds, minutes, or even hours to complete.»*

> **Quote (Gindullina et al.):** *«After successfully generating a syntactically correct loss function, the module initiates the process of further training of PINN»* with Adam, decay every 5000 epochs.

Scott and De Jong seek landscape features estimable in hundreds–thousands of queries. Gindullina uses cheap proxies: MAE on training data, binary thresholds, visual compliance—without budget to separate noise from signal.

---

## 2. Two goals in tension: cheap and noise-robust

> **Quote (Scott and De Jong):** *«There is a practical need, then, for landscape features that are both (A) inexpensive to estimate, and (B) accurate in the presence of small to moderate amounts of noise.»*

> **Quote (Scott and De Jong):** *«We show via a small set of relatively inexpensive landscape features based on hill-climbing methods that these two goals are in tension with each other: cheap features are sometimes extremely sensitive to even very small amounts of noise.»*

## 3. Microscopic noise breaks cheap features

On BBOB, features 1–4 (distances between local optima of the hill-climber) become inaccurate already at p around 1e-3.

> **Quote (Scott and De Jong):** *«In general we find that features 1–4 are extremely sensitive to noise: the estimate becomes inaccurate as soon as p reaches a value of about 10^{-3}.»*

> **Quote (Scott and De Jong):** *«Even very, very small quantities of noise are sufficient to entirely frustrate efforts to accurately measure features of a fitness landscape with these methods.»*

Parallel: MAE thresholds 700/1100 and the gap between 700 and 1100—a narrow window on a noisy scale. A forecast shift of 650 MAE may be retraining noise, not LLM weakness.

> **Quote (Gindullina et al.):** *«A value of 1100 was empirically chosen as the threshold for successfully meeting this criterion»* and *«MAE greater than 700»* for forecast has changed—both *«empirically chosen»* / *«determined empirically using test data»*.

This is garden-of-forking-paths: features calibrated on the same dataset used for evaluation, without sensitivity analysis—the opposite of Scott and De Jong’s FLA approach.

---

## 4. Explicit averaging does not help

> **Quote (Scott and De Jong):** *«We find that using explicit averaging of fitness has very little discernible impact on the accuracy of fitness measurements. Even at N = 15, a great deal of error remains.»*

> **Quote (Scott and De Jong):** *«Our answer to RQ2 is thus negative: it seems that explicit averaging is not an effective means of correcting for noise.»*

Gindullina does not average PINN retraining across seeds for a fixed loss. The 15–28% subset where the forecast *«did not yield a meaningful divergence»* is consistent with the cheap metric forecast has changed catching optimization noise, not absence of LLM effect.

> **Quote (Gindullina et al.):** *«Our analysis identified a subset of instances (15–28%) where adapting the loss function did not yield a meaningful divergence from the original forecast.»*

## 5. Population-based search: implicit averaging and a change of quantity

> **Quote (Scott and De Jong):** *«Population-based search methods are more robust to noise than hill-climbing methods.»*

> **Quote (Scott and De Jong):** *«Population-based search methods are not measuring the same thing as hill-climbing methods.»*

> **Quote (Scott and De Jong):** *«Our answer to RQ3 is thus mixed: population-based search methods are more robust to noise, but they are not measuring the same thing as hill-climbing methods.»*

Analogy: a single PINN run is a hill-climber; an ensemble or multi-seed run is a population. Expert-Guided PINN does no implicit averaging—one retrain per edit. If forecasts were averaged across seeds for a fixed loss, forecast has changed might become more stable—but the meaning would change (mean forecast vs one draw).

---

## 6. Expensive features 5–7 and computational budget

Features 5–7 (gradient walk, big valley) require 10^5–10^6 queries—more robust to noise, but costlier.

> **Quote (Scott and De Jong):** *«Features 5–7 are much more robust to noise than features 1–4, but they are also much more expensive to compute.»*

Gindullina has no analogue of an «expensive» feature: hold-out WIS or multi-seed stability are absent. All four criteria in Fig. 5 are cheap; none tests robustness to retraining noise.

> **Quote (Gindullina et al.):** *«The main limitations of PINNs include their sensitivity to hyperparameters, the need for careful tuning, and challenges in achieving stable convergence.»*

Sensitivity to hyperparameters is a source of noise in the PINN fitness landscape; without FLA-like diagnostics, thresholds 700/1100 may be artifacts of a single draw.

---

## 7. Sources of noise in Expert-Guided PINN

1. **PINN retrain:** stochastic Adam, decay schedule—different MAE for the same loss.
2. **LLM:** temperature=1.0, n=20—variability of edits and compliance.
3. **Thresholds:** empirical 700/1100 on train—not cross-validated.
4. **Mixed errors:** authors do not separate LLM syntax vs PINN convergence vs threshold noise.

> **Quote (Gindullina et al.):** *«The LLM was configured with a temperature of 1.0»*—maximum stochasticity with subjective compliance scoring.

Scott and De Jong explicitly pose three RQs: (1) sensitivity of cheap features to noise—yes; (2) effectiveness of explicit averaging—no; (3) population-based alternative—partial. Gindullina does not pose analogous questions: no RQ on MAE variance for a fixed loss, no threshold-robustness test, no comparison of single retrain vs ensemble.

## 8. Comparative table

| Aspect | Scott and De Jong (2016) | Gindullina et al. (Expert-Guided PINN) |
|--------|--------------------------|------------------------------------------|
| Expensive evaluation | Simulations, seconds–hours | PINN retraining on each iteration |
| Cheap metric | Features 1–4 (hill-climber) | MAE, thresholds 700/1100, compliance |
| Noise | Explicit Gaussian, p up to 1e-1 | Not modeled; T=1.0, single retrain |
| Robustness of cheap metrics | Break at p ~ 1e-3 | Not tested |
| Explicit averaging | N=15 insufficient (RQ2 −) | No multi-seed for fixed loss |
| Implicit averaging | Population search (RQ3 ±) | Single optimization run |
| Expensive metrics | Features 5–7, 10^5+ evals | Hold-out / stability—absent |
| Conclusion | Cheap vs robust in tension | Ad hoc thresholds on noisy fitness |

---

## 9. Literature-review clusters

**Cluster 5** (expensive black-box optimization, landscape analysis): Scott and De Jong—FLA methodology under noise; Gindullina—expensive black box without landscape diagnostics.

**Cluster 4** (validation, researcher degrees of freedom): Dinara’s empirical thresholds and 15–28% unchanged without seed control—garden of forking paths; Scott and De Jong—controlled noise and explicit RQs.

---

## Direction 1. Multi-seed control for a fixed loss

Before evaluating the LLM: K PINN retrainings with the same loss, different seeds. Score forecast has changed by confidence interval of MAE shift, not by one draw relative to 700.

## Direction 2. Sensitivity of thresholds 700/1100

Threshold sweep on hold-out or bootstrap; report fraction of «successes» that changes when shifting ±50 MAE—analogous to testing features at different p.

## Direction 3. Separating LLM and PINN noise

Fix loss (human-written), vary only PINN seed → estimate optimization noise. Fix seed, vary only LLM → generation noise. Both are currently mixed in the four criteria.

## Direction 4. Implicit averaging instead of one retrain

Ensemble of M PINN forecasts after one edit; forecast criterion—median shift vs baseline CI. Costlier, but aligned with Scott and De Jong’s conclusion on population methods.

## Direction 5. Proper scoring instead of binary thresholds

A continuous score (CRPS, log score on hold-out WIS) is more robust to microscopic noise than binary «MAE > 700»—parallel to moving from features 1–4 to costlier but robust metrics.

---

## Summary

Scott and De Jong formalize the tension between cheap landscape diagnostics and noise robustness: hill-climber features collapse at tiny p, explicit averaging does not help, population search is more robust but measures something else. Expert-Guided PINN builds evaluation on cheap empirical MAE thresholds and subjective compliance under expensive retraining and a stochastic LLM—without measuring variance. The 15–28% subset with unchanged forecast may reflect PINN noise, not failure of the expert edit. Integration: multi-seed baseline, threshold sensitivity, separation of noise sources, ensemble retrain if needed—transferring FLA-under-noise lessons to validation of LLM-guided PINN.

---

## Self-report

| Parameter | Value |
|----------|----------|
| Lines (approx.) | ~152 |
| Quotes Paper A | 8 |
| Quotes Paper B | 10 |
| Directions | 5 |
| Clusters | 5, 4 |
| Language | English |
