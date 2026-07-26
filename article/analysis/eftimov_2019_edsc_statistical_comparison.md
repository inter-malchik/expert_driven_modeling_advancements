> **Paper B — live link:** [https://doi.org/10.1016/j.ins.2019.03.049](https://doi.org/10.1016/j.ins.2019.03.049)  
> **Source in `src/`:** [`../src/2019 A novel statistical approach for comparing meta-heuristic stochastic optimization algorithms according to the distribution of solutions.md`](../src/2019%20A%20novel%20statistical%20approach%20for%20comparing%20meta-heuristic%20stochastic%20optimization%20algorithms%20according%20to%20the%20distribution%20of%20solutions.md)

Gindullina et al. (hereafter **Paper A**) report compliance rates of 6% / 25% / 27% across Llama-8B / Llama-70B / DeepSeek-V3.1 on 20 comments, and interpret this as evidence that «DeepSeek scores highest». They apply a Nemenyi post-hoc test but only on TSED (tree similarity of edit distance between generated code and baseline), not on compliance rates. No confidence intervals, no omnibus test on compliance, no Bonferroni correction, no distributional analysis of the LLM outputs — just three point estimates and a qualitative comparison. `dinara_comprehensive_review.md` §2.2 already noted the elementary problem: at n=20 and p=0.25, the 95% CI on compliance is roughly ±19 percentage points, so 25% vs 27% is well within noise.

Eftimov & Korošec (2019; hereafter **Paper B**) introduce *extended Deep Statistical Comparison* (eDSC), a two-part framework for comparing meta-heuristic stochastic optimization algorithms: (i) compare distributions of *solution values* via two-sample Anderson-Darling ranking (DSC), then Friedman omnibus + Bonferroni; (ii) compare distributions of *solutions in the search space* via multivariate E-test on hypervolume (√det(Σ)) of the covariance matrix. The framework identifies four diagnostic scenarios based on whether value-significance and distribution-significance hold jointly. Empirical validation on BBOB 2009: of 100 randomly-selected 3-algorithm comparisons at d=2, 41 show no significance in either dimension, 59 show value-significance but no distributional significance.

Paper B is not about PINN, LLMs, or epidemics; it is a methodological upgrade for comparing stochastic algorithms whose outputs are (i) numerical scores and (ii) points in a search space. The transferable thesis is sharp: **Paper A's 6/25/27 comparison is a statistical primitive — three unadjusted point estimates without an omnibus test, without confidence intervals, and without a distributional comparison of the 60 LLM-generated modifications; applying eDSC to Paper A's existing data (compliance-values via Anderson-Darling, modification-distributions via multivariate E-test on TSED / AST-edit vectors) is a near-zero-cost upgrade that would replace «DeepSeek is best» with «under the current sample size, LLMs are indistinguishable on compliance value but likely distinguishable on modification-diversity» — a strictly more informative claim.**

---

## 1. Paper A's Nemenyi-on-TSED does not test the primary metric

Paper A applies a statistical test — Nemenyi post-hoc — but only on TSED, a *secondary* measure of code similarity. Compliance rate — the *primary* metric — receives no statistical test.

> **Quote (Gindullina et al.):** *"We conducted a Nemenyi post-hoc test, which revealed that Meta-Llama-3.1-8B-Instruct, unlike Llama-3.3-70B-Instruct, generates functions that deviate more significantly from the original. This correlates with the empirical observation that 50% of its output fails compilation (Figure 3), suggesting that the increased syntactic incorrectness is due to more aggressive source code modification. Differences between all other pairs of models were statistically insignificant."*

> **Quote (Eftimov & Korošec):** *"Existing approaches for making a statistical comparison of meta-heuristic stochastic optimization algorithms only focus on performance analysis with respect to the obtained solutions values (i.e., fitness function values), without considering where these values are in the search space. ... Statistical analyses are crucial and must be made carefully, since they provide the data on which the conclusions are based."*

Paper A's Nemenyi test on TSED tells us that Llama-8B's generated code is different from Llama-70B's. It does *not* tell us that 27% (DeepSeek) is significantly different from 25% (Llama-70B) on compliance. Under Paper B's frame, this is the single most important omission: the primary success metric has no accompanying inferential statistic. (Comparative inference)

---

## 2. Anderson-Darling as an upgrade over median-based ranking

Paper B specifies Anderson-Darling as the ranking primitive because it uses the *entire distribution* rather than a single summary statistic (median or average).

> **Quote (Eftimov & Korošec):** *"Using the approach of Garcia et al., one needs to be aware that averages are sensitive to outliers. A common approach is to use medians because they are less sensitive to outliers. However, in both cases the results can still be affected by the ranking scheme. This happens when differences between the averages or medians are in some ε-neighborhood (e.g., 10⁻⁹, 10⁻¹⁰, etc.), and means that the algorithms obtain different rankings because there are no ties present. ... The main contribution of the DSC approach is its ranking scheme, which is based on the whole distribution, instead of using only one statistic to describe the distribution."*

> **Quote (Gindullina et al.):** *"Each row of Figure 5 [Compliance rate: Llama-70B: 25%, DeepSeek: 27%, Llama-8B: 6%] represents the fraction of successful outcomes across 20 launches."*

Paper A's 25/27% is a single-statistic summary of 20 Bernoulli outcomes per LLM. Paper B recommends comparing the *distribution* of outcomes — but Paper A's outcome is binary, so Anderson-Darling as-is doesn't apply directly. What does apply: the underlying continuous quantities Paper A collects (MAE for Criterion 1, MAE for Criterion 2, TSED for code similarity) — these are all continuous distributions where Anderson-Darling replaces Wilcoxon/Nemenyi for a stricter test. For Criterion 4 (compliance) specifically, a chi-square or Fisher exact test on the 3×2 contingency table (LLM × compliant/not) is the direct upgrade. (Comparative inference)

---

## 3. Bonferroni correction: not applied to the LLM comparison

Paper B is emphatic about Bonferroni correction for multiple pairwise comparisons.

> **Quote (Eftimov & Korošec):** *"Because multiple pairwise comparisons are made, these p-values are corrected using the Bonferroni correction in order to control the family-wise error, FWER. The FWER is the probability of making one or more false discoveries (type I errors) among all the hypotheses when performing multiple pairwise hypotheses tests."*

> **Quote (Gindullina et al.):** *"Differences between all other pairs of models were statistically insignificant."*

Paper A does say «insignificant» for pairs other than 8B-vs-70B, but does not report the p-values or the correction. Under Bonferroni for m=3 comparing 3 LLMs (\(\binom{3}{2} = 3\) pairwise tests), α should be corrected to α/3 = 0.0167 at the standard 5% level. Without correction, any of the three p-values could crossing 0.05 by chance at rate 3×5% = 15% under the null. This is the standard multiple-comparison problem, and Paper A does not address it. (Comparative inference)

---

## 4. Two-dimensional comparison: values × distributions

Paper B's most consequential contribution is the two-dimensional framework: comparing algorithms simultaneously on *value* and on *distribution-in-search-space*. This maps directly onto Paper A.

> **Quote (Eftimov & Korošec):** *"There is no statistical significance between the performances of the compared algorithms with regard to the obtained solutions values, but there is a statistical significance with respect to the distribution of the obtained solutions in the search space. In this scenario the decision about algorithm preference is determined according to user needs (sparse or clustered solutions). ... it is assumed that the algorithm with the sparser distribution of obtained solutions has better exploration power."*

> **Quote (Gindullina et al.):** *"To quantify the degree of correspondence between the original loss function and its modified versions generated by language models, the TSED (Tree Similarity of Edit Distance) metric was applied (Figure 3)."*

Paper A has (i) compliance rates (values); (ii) TSED distributions (a proxy for distribution-in-search-space over loss-AST-edits). Paper B's four-scenario framework maps as:
- **Scenario A** (same values, same distribution): LLMs interchangeable — Llama-70B vs DeepSeek likely at n=20.
- **Scenario B** (same values, different distribution): same compliance rate but different *diversity* of modifications — e.g., DeepSeek generates more clustered edits (exploitation) while Llama-70B generates more spread edits (exploration).
- **Scenario C** (different values, same distribution): different compliance but similar edit distributions — the losing LLM has worse exploitation of its explored region.
- **Scenario D** (both different): fundamentally different behavior — Llama-8B vs the others.
Applying this partition to Paper A's data would replace one number (27%) with a diagnostic assignment per LLM pair, per comment class. (Comparative inference)

---

## 5. Hypervolume as the search-space diversity measure

Paper B's operationalization of «distribution-in-search-space» is hypervolume = √det(covariance matrix) — a shape-and-size measure. For Paper A, the analogue is diversity of the LLM-emitted modification vectors.

> **Quote (Eftimov & Korošec):** *"To estimate the distribution of the obtained solutions in the search space, the measure of multivariate spread needs to be defined. For this purpose, by using the random matrix theory, the square root of the determinant of the covariance matrix is used. This gives us the hypervolume, incorporating both shape (correlation) and size (standard deviation) information."*

> **Quote (Gindullina et al.):** *"a subset of instances (15–28%) where adapting the loss function did not yield a meaningful divergence from the original forecast."*

If Paper A encodes each modification as a feature vector (per essay 19 Direction 1 and essay 22 slot-and-facet), the hypervolume of these vectors per LLM measures diversity. Empirically, «15–28% forecast unchanged» is a diversity failure — the LLM keeps emitting near-identical modifications for the same comment. Paper B's hypervolume metric would quantify this directly, per LLM and per comment class. Diversity of an LLM's modifications is directly relevant to Paper A's automation-bias concerns (essay 23 Epstein) — a high-diversity LLM presents the epidemiologist with alternatives, low-diversity does not. (Speculative extension)

---

## 6. Empirical BBOB result: 41/100 no-difference is the null Paper A ignores

Paper B's headline empirical result — 41/100 comparisons showed no significance in either value or distribution — is a warning against publishing tiny differences as findings.

> **Quote (Eftimov & Korošec):** *"there are 41 out of 100 combinations that belong to the first scenario, while in the second case there are 59. ... The first one is that there is no statistical significance between the performance of the algorithms over multiple problems according to the obtained solutions values and their distributions in the search space."*

> **Quote (Gindullina et al.):** *"The key result is confirmation of the fundamental feasibility of integrating expert knowledge through LLM into PINN, with a success rate of 25-27% for the best models."*

Under Paper B's empirical baseline, ~41% of algorithm pairs show no difference — noise dominates. Paper A's 25% vs 27% is exactly in the noise range predicted by n=20 sampling. Reporting «25-27% for the best models» as if these were meaningfully different LLMs is exactly the mistake Paper B empirically documents on a well-established benchmark. Under Paper B's protocol, the honest statement is «Llama-70B and DeepSeek-V3.1 are statistically indistinguishable on compliance at n=20; Llama-8B is different from both». (Comparative inference)

---

## 7. Power analysis: the minimum n Paper A needs

Paper B §6 discusses power analysis — how large n must be to detect a specified effect size. Paper A never asks this question.

> **Quote (Eftimov & Korošec):** *"Section 6 presents a discussion of the power analysis and the conclusions are presented in Section 7."*

> **Quote (Gindullina et al.):** *"For each model, we ran the framework 20 times on the same comment set to accumulate statistics."*

To detect a 25% vs 30% difference (5 percentage points, a plausible effect size for meaningful LLM differences on compliance) at 80% power with two-tailed α=0.05, the required n per group is approximately 500 — not 20. Paper A's n=20 has less than 15% power to detect a 5-percentage-point difference. This is a fundamental methodological point: at n=20, only very large effect sizes (>25 percentage points) are statistically detectable. Llama-8B's 6% vs the others' 25/27% is one such large effect — hence Paper A's Nemenyi test detected 8B as different. The finer distinctions among the larger models are simply below detection threshold at this sample size. (Comparative inference)

---

## 8. Comparison table

| Criterion | Paper A | Paper B (eDSC) | Takeaway |
| :--- | :--- | :--- | :--- |
| Statistical test on primary metric | None (Nemenyi on TSED only) | Anderson-Darling + Friedman + Bonferroni | Primary compliance rate not tested (Comparative inference) |
| Ranking primitive | Point estimate (25%, 27%) | Whole-distribution ranking | 27% vs 25% is single-point comparison (Comparative inference) |
| Multiple-comparison correction | Not applied | Bonferroni for FWER | m=3 needs α/3 (Comparative inference) |
| Two-dimensional comparison | Only value dimension | (value × distribution) framework | 4 diagnostic scenarios available (Comparative inference) |
| Distribution-in-search-space | Not measured | Hypervolume √det(Σ) | Modification diversity per LLM measurable (Speculative extension) |
| Sample size | n=20 (0.15 power for 5pp) | Empirical: 41/100 no-difference on BBOB | n=20 detects only huge effects (Empirically shown for B) |
| Framing of «best LLM» | «DeepSeek scores highest at 27%» | Distinguishability under given n | «Indistinguishable at current n» is honest (Comparative inference) |

---

## Direction 1. Apply eDSC to Paper A's existing 60-launch dataset

**Pipeline stage.** §3 Results and Discussion (statistical analysis of existing data — no new experiments).  
**Mechanism.** For the existing 20 comments × 3 LLMs = 60 launches:
1. **DSC (values):** for each pair of LLMs, run Fisher exact test on 20×2 contingency table for each Paper A criterion. Apply Bonferroni for \(\binom{3}{2} \times 4\) = 12 tests (α_corr = 0.00417). Report which pairs are significantly different on which criteria.
2. **eDSC (distributions):** encode each modification as a feature vector `(class, subclass, target_term, operator, numeric_bucket)` per essay 22. Compute the multivariate E-test on the 20-modification distributions per LLM. Compute hypervolume per LLM per class.
3. **Four-scenario partition:** for each (LLM_A, LLM_B, criterion) triple, classify as scenario A/B/C/D. Report the counts.
4. **Power analysis:** compute the minimum n needed to detect a 5-percentage-point compliance difference; report as a limitation.

**Failure modes addressed.** Unsupported «DeepSeek is best» framing; automation-bias risk from a single confident-sounding number; missed diversity-vs-quality trade-offs. (Speculative extension)

**Cost.** Under 1 day of statistical work on already-collected data.

---

## Direction 2. Design-of-experiments: minimum-n calculation before scaling

**Pipeline stage.** §2.4 Evaluation Approach — pre-registered analysis plan.  
**Mechanism.** Before running the next batch of experiments (e.g., Smorodintsev field study), specify:
1. Target effect size (e.g., we want to detect a 5-percentage-point compliance improvement over baseline 27%).
2. Test procedure (per Direction 1 — eDSC).
3. Required sample size (from power analysis).
4. Pre-registered hypothesis and analysis plan.

Publish this as an appendix. When results arrive, run the pre-specified analysis — no p-hacking. This is exactly the militant-ignorance principle (essay 23 Epstein) in operational form.

**Failure modes addressed.** Researcher-degrees-of-freedom in MAE thresholds (700 / 1100) — pre-registration bounds them; underpowered experiments that produce inconclusive results and are interpreted as feasibility. (Speculative extension)

---

## Manuscript placement

- **§3.3 Working with the framework:** add a subsection «Statistical significance of pairwise LLM differences» reporting the eDSC analysis from Direction 1. Position 25% vs 27% as within-noise and 8B as clearly different (clusters **4** proper scoring and **10** automation-bias mitigation of `dinara_comprehensive_review.md`; overlaps with essay 25 Kerschke).
- **§4 Limitations:** replace «significant subjective component» with the concrete «n=20 has 0.15 power to detect 5pp compliance difference; therefore 25% vs 27% is not distinguishable given this sample size».
- **§4 Future work:** append a design-of-experiments plan for the Smorodintsev study (Direction 2), pre-registering the effect size and required n.

## What not to transfer

Paper B is a benchmarking methodology for stochastic optimization on BBOB with continuous search spaces; do not import BBOB-specific test functions, the 17-algorithm competitor set, or the R-package chain (kSamples, energy, scmamp, Matrix, nearPD) verbatim. Paper A's Criterion 4 (compliance) is binary, so the DSC-on-values step must be adapted to categorical comparison (Fisher exact / logistic regression), not Anderson-Darling. The eDSC hypervolume works for continuous vectors — Paper A's modification vectors are mixed (categorical class × integer subclass × float coefficient), requiring a hybrid distance or a discretized covariance approximation. And do not treat 41/100 no-difference as a universal law — the fraction depends on benchmark, algorithm set, and dimension; the point is that "no difference" is a legitimate empirical finding, not a failure mode. (Comparative inference)

## Concrete next experiment

**Hypothesis.** On Paper A's existing 60-launch dataset, applying Fisher exact + Bonferroni correction to pairwise LLM compliance comparisons will show: (i) Llama-8B vs the others is significant at any reasonable correction; (ii) Llama-70B vs DeepSeek is not significant; (iii) LLM × comment-class interaction is significant for at least one comment class, motivating per-instance LLM selection (essay 25).

**Protocol.**
1. Recover per-launch compliance outcomes (binary) from Paper A's data or replication code (`github.com/vnleonenko/Epi_PINN_LLM`).
2. Build the 20×3 outcome table + comment-class labels.
3. Run Fisher exact test on 3 pairwise comparisons. Apply Bonferroni α/3 = 0.0167.
4. Run logistic regression: `compliance ~ LLM + class + LLM:class`. Report significant terms.
5. If LLM×class interaction is significant, report which class × LLM combinations are best.
6. Recompute effective compliance rate under a Kerschke-style per-instance selector using the observed LLM×class interactions.

**Expected signal.** (i) Llama-8B significantly worse (large effect, p<10⁻⁵). (ii) 70B vs DeepSeek indistinguishable (p > 0.5, effectively). (iii) At least one comment class shows LLM×class interaction (p<0.05 uncorrected; p<0.017 with Bonferroni). (iv) Per-instance selector effective rate ≥ 32%, closing 30–70% of the VBS-SBS gap. (Speculative extension)

## Related essays in this series

- [`19_wei_2024_dante_active_optimization.md`](19_wei_2024_dante_active_optimization.md) — data efficiency framing; sample-count-to-optimum as a reportable metric.
- [`20_zhang_2026_trm_complex_reasoning.md`](20_zhang_2026_trm_complex_reasoning.md) — TRM's theorem 5.2 (reward-variance argument) — direct link to distributional-significance testing in eDSC.
- [`23_epstein_2008_why_model.md`](23_epstein_2008_why_model.md) — militant-ignorance framing; pre-registration and honest sample-size reporting.
- [`25_kerschke_2019_algorithm_selection_survey.md`](25_kerschke_2019_algorithm_selection_survey.md) — per-instance selection benefits from proper significance testing.

## Conclusion

Paper B is a 2019 methodology paper for comparing stochastic optimization algorithms — it does not touch PINN, LLMs, or epidemics. But its methodological gap analysis maps almost perfectly onto Paper A: single-point comparisons without omnibus tests or multiple-comparison correction; primary metric untested; value dimension examined but search-space distribution ignored; sample size chosen without power analysis. Applying eDSC — Anderson-Darling / Fisher exact on values, multivariate E-test on modification distributions, Bonferroni on multiple pairs, hypervolume on diversity — turns Paper A's «DeepSeek best at 27%» into a statistically defensible statement about which LLMs are and are not distinguishable at n=20, with which criteria, and on which comment classes. It is the cheapest way to make Paper A's core empirical claim survive peer review, and it operates entirely on the data Paper A already has.
