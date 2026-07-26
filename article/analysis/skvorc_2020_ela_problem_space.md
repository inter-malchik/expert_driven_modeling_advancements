> **Paper B — live link:** [https://doi.org/10.1016/j.asoc.2020.106138](https://doi.org/10.1016/j.asoc.2020.106138)  
> **Source in `src/`:** [`../src/2020 Understanding the problem space.md`](../src/2020%20Understanding%20the%20problem%20space.md)

Gindullina et al. (hereafter **Paper A**) gate forecast success with empirically chosen MAE thresholds—1100 for “matching training data,” 700 for “forecast has changed”—and treat incidence trajectories from a fixed St. Petersburg window as the evaluation substrate. Those thresholds and any future “instance features” of expert scenarios are expressed in absolute incidence units. Nothing in the Evaluation Approach audits whether conclusions survive shift/scale of the incidence axis.

Škvorc, Eftimov & Korošec (2020; hereafter **Paper B**) show that many exploratory landscape analysis (ELA) features are **not invariant** to shift and scale: without filtering, t-SNE separates original vs shifted/scaled copies of the same functions; after Wilcoxon filtering (101→49→23 invariant→16 after correlation), pairing recovers. Thesis: **Paper A’s MAE gates and scenario descriptors are scale-fragile in the same sense; Expert-Guided PINN needs an invariance audit before treating absolute MAE cutoffs or instance features as stable evaluation currency.**

---

## 1. Absolute MAE thresholds are scale-tied by construction

Paper A’s first two criteria are hard cutoffs on MAE in incidence units.

> **Quote (Gindullina et al.):** *"A value of 1100 was empirically chosen as the threshold for successfully meeting this criterion, using the MAE (Mean Absolute Error) metric."*

> **Quote (Gindullina et al.):** *"The lower threshold of significance was determined empirically using test data - MAE greater than 700."*

> **Quote (Škvorc et al.):** *"a large amount of them are not invariant to simple transforms like scaling and shifting, at least when analyzing these two datasets."*

If incidence were rescaled (per 100k vs raw counts; city vs district; under-ascertainment factor), 700/1100 would move relative to the data even when relative forecast shape were unchanged. That is the evaluation analogue of Paper B’s non-invariant features. (Author-stated in both) (Comparative inference)

---

## 2. Without invariance filtering, transforms dominate visualization

Paper B’s control experiment is the cautionary picture for any absolute descriptor.

> **Quote (Škvorc et al.):** *"Fig. 7 shows what happens if we perform PCA on the full feature set, without first excluding non-invariant features. As we can see, the visualization almost cleanly splits the dataset into the two groups: the original problems and the problems that had the scale and shift transformation applied to them."*

> **Quote (Škvorc et al.):** *"Finally, Fig. 8 shows the visualization without the non-invariant landscape features… Here, we can see that the same numbered problems stay relatively close to one another."*

> **Quote (Gindullina et al.):** *"The analysis was conducted on daily and cumulative incidence data for the period from July 5, 2020 to June 28, 2021 (359 days)"*

Paper A reports criteria on one untransformed series. A silent change of units or population base would act like Paper B’s shift/scale: absolute MAE features would cluster by *scale regime*, not by true modification success. (Empirically shown in B; Comparative inference for A)

---

## 3. Wilcoxon filter as a methodological template

Paper B’s procedure is reusable for evaluation metrics, not only ELA.

> **Quote (Škvorc et al.):** *"In order to determine which features are not invariant, we used the following procedure: … Generate two sample sets… one without any preprocessing, and one where a random shift and scale transformation is applied… Use a statistical test to determine which landscape features show statistical differences… Exclude these features from further use."*

> **Quote (Škvorc et al.):** *"we used a paired Wilcoxon signed-rank test with a significance level of 0.05."*

> **Quote (Gindullina et al.):** *"Due to the lack of standardized numerical metrics for assessing the semantic correspondence of a forecast to an expert’s textual commentary, a system of qualitative validation criteria was developed."*

Apply the same paired test to Paper A’s criteria under incidence \(y' = a\cdot y + b\): binary pass/fail for MAE>700 / MAE<1100 will flip systematically unless thresholds are redefined as relative (e.g., MAE / mean incidence, or MAE on z-scored series). (Speculative extension grounded in B’s method)

---

## 4. “Forecast has changed” is not transform-invariant as stated

Criterion 2 uses absolute MAE against the baseline forecast.

> **Quote (Gindullina et al.):** *"2. Forecast has changed… The forecast for infected cases is considered to have changed significantly if the calculated MAE exceeds this value… LLMs can only slightly change the loss function or simply add some constants, which will not change our forecast."*

> **Quote (Škvorc et al.):** *"Since we are interested in finding relations between these base problems and not their transformed versions, landscape features that are not invariant to these transformations are not useful to us."*

A constant additive bump that matters at low incidence may fail MAE>700 after downscaling, or pass after upscaling, without any change in relative dynamics. Relative \(L_1\) or normalized curve distance would be the invariant analogue of Paper B’s retained features. (Comparative inference)

---

## 5. Instance features for expert scenarios inherit the same risk

Paper A’s class/subclass ontology and Future work templates will eventually need scenario descriptors (peak height, wave length, training MAE). Paper B warns that many numeric descriptors of “problem shape” collapse under shift/scale.

> **Quote (Škvorc et al.):** *"Our analysis revealed that 26 out of 49 features were not invariant to these transformations. This leaves us with a total of 23 invariant features."*

> **Quote (Škvorc et al.):** *"In practice, we believe this means that such features should be removed before performing any analysis based on exploratory landscape analysis."*

> **Quote (Gindullina et al.):** *"Developing suitable templates and bounds is problem-dependent and will be refined iteratively through experiments that assess training stability and forecast quality."*

If template bounds or scenario clustering use raw peak incidence or raw MAE, they will mis-group “same epidemic shape, different scale” scenarios—exactly Fig. 7’s split. Prefer scale-free descriptors (peak timing, relative amplitude, compartment ratios). (Comparative inference)

---

## 6. Comparison table: evaluation invariance

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Absolute numeric gates | MAE 700 / 1100 | Many ELA features fail shift/scale | Absolute cutoffs are scale-fragile (Comparative inference) |
| Invariance audit | None reported | Paired Wilcoxon original vs shifted/scaled | Import the audit before claiming stable criteria (Author-stated method in B) |
| Failure without filter | Not tested | t-SNE splits by transform, not identity (Fig. 7) | Risk of scale-regime artifacts in A (Empirically shown in B) |
| After filter | — | Same problems re-pair (Fig. 8); 23→16 features | Relative / invariant metrics recover signal (Empirically shown in B) |
| Data substrate | One city series, fixed units | CEC/BBOB with explicit transforms | Rescale incidence as stress test (Speculative extension) |
| Scenario descriptors | Class/subclass + empirical thresholds | ELA instance features | Use scale-free features for templates (Comparative inference) |

---

## 7. Epidemic-logic criteria are closer to invariant—MAE is not

Paper A’s third criterion (non-negativity, monotonic cumulatives, asymptotics) is largely unit-free; the MAE pair is not.

> **Quote (Gindullina et al.):** *"3. Compliance with the epidemic logic… Non-negativity of all model compartments… Monotonicity of cumulative values… Asymptotic behavior consistent with the underlying epidemiological model."*

> **Quote (Škvorc et al.):** *"selecting proper features is very important. First, because some landscape features might not be appropriate for a given task. For example, we have shown that a large number of features are not invariant to shifting and scaling of problems."*

Promote logic checks and relative shape metrics to primary automated gates; demote absolute MAE to secondary, scale-declared diagnostics (always report the incidence unit and population base). (Comparative inference)

---

## 8. Subjective compliance does not cancel scale fragility

Even if primary success stays human “compliance,” Paper A still uses MAE to filter catastrophic / trivial runs before that judgment.

> **Quote (Gindullina et al.):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the \"Compliance with the comment\" criterion."*

> **Quote (Gindullina et al.):** *"A value greater than this threshold indicates a catastrophic loss of model adequacy during modification."*

> **Quote (Škvorc et al.):** *"if these features are not excluded, then such transformations can significantly negatively influence the visualization. This means that this step is necessary to prevent us from reaching incorrect conclusions."*

Scale-fragile MAE filters change which runs reach the human judge—biasing the 25–27% compliance denominator. Invariance audit is prerequisite even for subjective primary metrics. (Comparative inference)

---

## 9. Same name, different scale: CEC vs BBOB as a warning

Paper B further shows that identically named functions can still separate when sampling regimes differ—another absolute-metric trap.

> **Quote (Škvorc et al.):** *"despite being named similarly, problems from different benchmarks still appear differently when sampled and plotted, and as such also appear far apart on the landscape feature based visualization."*

> **Quote (Škvorc et al.):** *"One other major factor that our analysis cannot account for is the difference in the area that the problem that is being sampled from."*

> **Quote (Gindullina et al.):** *"Matching training data… catastrophic loss of model adequacy"* / *"Forecast has changed… non-trivial nature of the changes"*

Transfer: comparing Expert-Guided PINN runs across pathogens, seasons, or reporting systems under fixed 700/1100 is like comparing CEC and BBOB “Schwefel” under raw ELA—labels look shared; absolute numbers are not. Declare scale, normalize, then compare. (Empirically shown in B; Comparative inference)

---

## Direction 1. Incidence rescaling stress test for Evaluation Approach

**Pipeline stage:** Evaluation Approach (§2.4) / reproducibility appendix.  
**Mechanism:** Re-run Fig. 5 criteria under \(y'=a\cdot y\) (and mild shift) for a grid of \(a\); report which binary gates flip; replace 700/1100 with scale-normalized thresholds (MAE / mean(\(y_{\mathrm{train}}\)), or MAE on min–max normalized curves) that keep pass/fail stable across \(a\).  
**Failure modes addressed:** scale-fragile MAE gates; silent unit dependence; biased compliance denominators.  
**Measurable acceptance:** Kendall τ of run rankings before/after rescale ≥ high threshold for normalized metrics; near 0 for raw 700/1100. (Speculative extension)

---

## Direction 2. Scale-free instance features for expert scenarios and templates

**Pipeline stage:** Future work templates + scenario selection for Institute studies.  
**Mechanism:** Describe comments/scenarios with invariant features (peak day, relative peak height, rise/fall ratios, compartment fractions)—audited à la Paper B’s Wilcoxon filter—before clustering scenarios or setting numeric template bounds.  
**Failure modes addressed:** template bounds tied to raw incidence; scenario clusters that separate only by scale. (Speculative extension)

---

Paper B’s contribution here is methodological hygiene: absolute landscape (or error) numbers that move under shift/scale are not safe building blocks for comparative evaluation. Expert-Guided PINN’s MAE thresholds sit in that unsafe class until audited.

---

## Manuscript placement

- **§2.4 Evaluation Approach / reproducibility:** incidence rescale audit for MAE 700/1100 (cluster **4**).
- **Future work templates / scenario features:** Wilcoxon-style invariance filter (cluster **4**/FLA hygiene).
- **Limitations:** absolute thresholds as researcher degrees of freedom.

## What not to transfer

flacco / t-SNE / CEC–BBOB benchmarking is not the epidemic deliverable. Transfer **invariance audit for absolute numeric gates**—not a full ELA pipeline on PINN weights. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Raw MAE 700/1100 pass/fail rankings are unstable under \(y'=a\cdot y\) for \(a\in\{0.1,1,10\}\); normalized MAE (÷ mean train incidence) preserves rankings.

**Protocol.** Re-score existing Fig. 5 runs under rescaled incidence; compute Kendall τ of rankings; replace gates with normalized thresholds that keep τ high.

**Metric.** τ(raw) vs τ(normalized); flip count of binary gates. Expect raw τ near 0 across \(a\). (Speculative extension)

## Related essays in this series

- [`12_mehdi_2015_compositional_forecasting.md`](12_mehdi_2015_compositional_forecasting.md) — share/normalized metrics.
- [`11_daza_2016_basin_entropy.md`](11_daza_2016_basin_entropy.md) — complementary diagnostics.
- [`01_hidalgo_2018_glucose_grammatical_evolution.md`](01_hidalgo_2018_glucose_grammatical_evolution.md) — clinical zones less scale-tied if relative.
- Bridge: FLA surveys already in `../uncompared.md` / compared Tier 3.


## Conclusion

Škvorc et al. demonstrate that unfiltered numeric descriptors of problem instances split under shift/scale, and that Wilcoxon invariance filtering restores meaningful pairing. Paper A’s MAE thresholds of 700 and 1100—and any raw incidence instance features for expert scenarios—are the same kind of absolute descriptor. Before treating them as stable gates, Expert-Guided PINN should run an incidence-rescaling audit and prefer normalized / scale-free metrics for “changed,” “matched training,” and template bounds. Until then, evaluation setup fragility remains an unmeasured confounder of the reported success rates.

