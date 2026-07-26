> **Paper B — live link:** [https://doi.org/10.1038/srep31416](https://doi.org/10.1038/srep31416)  
> **Source in `src/`:** [`../src/2016 Basin entropy a new tool to analyze uncertainty in dynamical systems.md`](../src/2016%20Basin%20entropy%20a%20new%20tool%20to%20analyze%20uncertainty%20in%20dynamical%20systems.md)

Gindullina et al. (hereafter **Paper A**) retrain a SIRD PINN after an LLM rewrites the loss from free-text expert comments. Best “Compliance with the comment” is only 25–27%; 15–28% of runs leave the forecast essentially unchanged; catastrophic edits produce 700+-day outbreaks that still pass compile. Authors attribute physically wrong forecasts partly to “fundamental limitations of PINN,” but diagnose almost exclusively with MAE gates (700 / 1100), epidemic-logic checks, and subjective plot reading—never with a measure of *which attractors* the edited loss can still reach.

Daza, Wagemakers, Georgeot, Guéry-Odelin, and Sanjuán (2016; hereafter **Paper B**) introduce **basin entropy** \(S_b\) and **boundary basin entropy** \(S_{bb}\) to quantify final-state unpredictability in multistable dynamical systems: discretize phase space into \(\varepsilon\)-boxes, treat attractors as colors, apply Gibbs entropy per box. Same basin stability can hide radically different mixing; \(S_{bb}>\log 2\) is a sufficient fractal-boundary test. Escape basins in Hénon–Heiles and multistable Duffing show that “harder to predict which exit” is a topological fact, not an annotation error.

The transferable thesis is sharp: **treat some Expert-Guided PINN failures as attractor-structure problems in the SIRD / loss landscape, diagnose them with \(S_b\)/\(S_{bb}\), and stop blaming every unchanged or catastrophic forecast on the LLM alone.**

---

## 1. Unchanged forecasts vs multistable basins

Paper A flags a non-trivial fraction of runs where loss edits do not move the infected curve past the MAE-700 gate. Paper B’s opening intuition is exactly that: two phase portraits can look “deterministic” while one is far harder to assign to a final state.

> **Quote (Gindullina et al.):** *"our analysis identified a subset of instances (15–28%) (Figure 5 ) where adapting the loss function did not yield a meaningful divergence from the original forecast."*

> **Quote (Daza et al.):** *"With this in mind, we may intuitively understand that it is harder to predict in advance which will be the final destination of an orbit in Fig. 1(a) than in Fig. 1(b)."*

> **Quote (Daza et al.):** *"The problem is that even though, we can have an intuitive notion that Fig. 1(a) is more uncertain than Fig. 1(b), there is no quantitative measure to affirm this."*

If the base PINN sits deep in a large basin of a multistable loss landscape, a soft “Add penalty to term2” may leave the trajectory in the same attractor—MAE unchanged—without the LLM “doing nothing.” (Comparative inference)

---

## 2. Catastrophic edits as basin switching, not only wrong weights

Fig. 4b’s 700-day outbreak follows a boundary-condition weight change after a “shift peak 7–10 days” comment. Paper A narrates this as rule under-specification. Paper B supplies a complementary geometry: tiny parameter moves can land initial conditions across fractal or Wada-like boundaries into a different attractor family.

> **Quote (Gindullina et al.):** *"As a result, the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days)."*

> **Quote (Daza et al.):** *"This notion of unpredictability strongly differs from others used in nonlinear dynamics, like the Kolmogorov-Sinai entropy… which refer to the difficulty of predicting the evolution of the trajectories… our aim here is to develop an entropy depending on the topology of the basins."*

Compile-pass + “plausible shape” is compatible with having jumped basins. \(S_b\) on a grid over \((\beta,\gamma)\) / loss-weight parameters would flag high final-state uncertainty *before* another 5000-epoch retrain. (Comparative inference) (Speculative extension)

---

## 3. Basin stability ≠ uncertainty; MAE ≠ mixing

Paper A’s secondary gates ask whether training MAE stayed below 1100 and whether the forecast “changed.” Paper B shows four basins with identical basin stability \(1/2\) that uncertainty exponent and volume metrics cannot rank—while \(S_b\) orders them by mixing.

> **Quote (Daza et al.):** *"The basin stability would be the same in both cases but obviously fractal boundaries have a more complex structure. A clear example is shown in Fig. 2, where all the basins have the same basin stability. The uncertainty exponent also fails to capture the uncertainty associated to these basins. However, the basin entropy clearly distinguishes the four of them."*

> **Quote (Gindullina et al.):** *"A value of 1100 was empirically chosen as the threshold for successfully meeting this criterion, using the MAE… A value greater than this threshold indicates a catastrophic loss of model adequacy during modification."*

MAE magnitude does not encode how finely SIRD outcomes interleave under small loss edits. Two edits can both clear MAE-700 while one sits on a smooth basin and the other on a riddled boundary. (Comparative inference)

---

## 4. \(S_b\) definition as a diagnostic for PINN/SIRD grids

Paper B’s constructive definition maps cleanly onto a post-edit diagnostic grid over compartment states or loss hyperparameters.

> **Quote (Daza et al.):** *"We discretize \(\Omega\) via a finite number of boxes covering it… Each box contains… trajectories, each one leading to a color… \(S_i = \sum_{j=1}^{m_i} p_{i,j}\log(1/p_{i,j})\)… \(S_b = S/N\)."*

> **Quote (Daza et al.):** *"An interpretation of this quantity is associated to the degree of uncertainty of the basin, ranging from 0 (a sole attractor) to \(\log N_A\) (completely randomized basins with \(N_A\) equiprobable attractors)."*

For Expert-Guided PINN: color = asymptotic SIRD regime (e.g., short wave / long endemic / extinguished), \(\Omega\) = sampled IC or loss-weight neighborhood after LLM edit. High \(S_b\) ⇒ “forecast may look stable but final compartment fate is unresolved.” (Speculative extension)

---

## 5. Boundary entropy \(S_{bb}\) and the \(\log 2\) fractal test

Paper A already checks non-negativity and cumulative monotonicity (criterion 3) but has no boundary-structure test when comments push the peak or BC weights.

> **Quote (Daza et al.):** *"\(S_{bb} = S/N_b\)… if the boundary basin entropy is larger than \(\log 2\), then the boundary is fractal… \(S_{bb} > \log 2 \Rightarrow \alpha < 1\)."*

> **Quote (Gindullina et al.):** *"Compliance with the epidemic logic… Non-negativity of all model compartments (SIRD model). Monotonicity of cumulative values. Asymptotic behavior consistent with the underlying epidemiological model."*

Logic checks are necessary but local. \(S_{bb}>\log 2\) on a peak-offset / BC-weight plane would flag fractal sensitivity—exactly the regime where “shift peak slightly” becomes Fig. 4b. (Comparative inference)

---

## 6. PINN systemic limits vs basin entropy parameter sets

Paper A hypothesizes that infinite-growth and training-data mismatch may be PINN pathologies, not only LLM bugs—yet offers no parameter map of that uncertainty.

> **Quote (Gindullina et al.):** *"The observed cases of physically incorrect forecasts… may be attributed to fundamental limitations of PINN noted in the literature… We hypothesize that discrepancies between the forecast and training data… may be a consequence of these architectural features of PINNs, and not solely errors in the operation of the LLMs."*

> **Quote (Daza et al.):** *"We call the plot of the basin entropy in a two-dimensional parameter space basin entropy parameter set… Combined with Monte Carlo sampling… speed up the computation by a factor 20… For the 94% of the parameters evaluated the relative error… was less than 5%."*

A \((F,\omega)\)-style \(S_b\) map over loss-edit hyperparameters (penalty weights, BC multipliers) would separate “PINN multistability hotspots” from “LLM nonsense edits”—the ablation Paper A’s hypothesis still lacks. (Speculative extension)

---

## 7. Number of attractors and ambiguous plateaus

Paper A’s Fig. 4c “ambiguous” plateau—growth requested, flat high endemic delivered—reads as a third asymptotic regime beside short wave and long outbreak. Paper B shows \(S_b\) rises when \(N_A\) increases even if boundaries are not more fractal.

> **Quote (Daza et al.):** *"The last factor that contributes to the basin entropy, according to Eq. 6, is the number of attractors \(N_A\). In general, as the number of attractors increases, the uncertainty increases too, and so does the basin entropy."*

> **Quote (Gindullina et al.):** *"Ambiguous result. The expert’s requirements are formally satisfied, but the result is questionable (for example, the curve looks unrealistic)."*

> **Quote (Gindullina et al.):** *"the new forecast shows a stabilization in the number of cases (although growth was requested), and the resulting curve is unusually flat compared to typical incidence trajectories."*

Coloring “short decline / plateau endemic / runaway growth” as distinct attractors would raise \(S_b\) precisely where Paper A now bins outcomes as ambiguous by eye. (Comparative inference)

---

## 8. Subjective compliance cannot see basin mixing

Paper A’s primary 25–27% bar collapses topology into binary author judgment. Paper B’s Discussion positions \(S_b\) as the missing quantitative language for claims that were previously only intuitive.

> **Quote (Gindullina et al.):** *"The key result is confirmation of the fundamental feasibility of integrating expert knowledge through LLM into PINN, with a success rate of 25-27% for the best models (Figure 5)."*

> **Quote (Daza et al.):** *"Many authors describe fractal basin boundaries and when discussing its associated unpredictability, some vague affirmations are found due to a lack of an appropriated measure."*

> **Quote (Daza et al.):** *"The basin entropy quantifies the final state unpredictability of dynamical systems. It constitutes a new tool for the exploration of the uncertainty in nonlinear dynamics."*

Reporting \(S_b\) next to compliance would let authors partition failures: low \(S_b\) + non-compliant ⇒ LLM intent miss; high \(S_b\) + any plot ⇒ structure-limited predictability. (Comparative inference)

---

## 9. Comparison table

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Failure narrative | LLM code errors + PINN systemic limits (Author-stated) | Final-state unpredictability from basin topology (Author-stated) | Topology can explain “unchanged”/catastrophe without LLM blame (Comparative inference) |
| Change detection | MAE > 700 vs baseline forecast | \(S_b\) sensitive to boundary size, \(\alpha\), \(N_A\) | Magnitude ≠ mixing (Empirically shown in B) |
| Catastrophic gate | MAE > 1100 on training fit | High \(S_b\) / \(S_{bb}>\log 2\) near boundaries | Fractal BC edits need entropy gates (Comparative inference) |
| Compartments | SIRD terms term1–term4 in Table A.2 | Colors = attractors / exits | Map SIRD regimes to colors (Speculative extension) |
| Parameter exploration | Temperature 1.0, ~20 launches per LLM | Basin entropy parameter set + MC 2000 boxes | Cheap \(S_b\) maps before full retrain (Empirically shown in B) |
| Subjective primary metric | “Compliance with the comment” 25–27% | Quantitative \(S_b \in [0,\log N_A]\) | Entropy complements visual compliance (Comparative inference) |
| Ambiguous outcomes | Author ternary: success / fail / ambiguous | Entropy rises with \(N_A\) and mixing | Plateau regimes as extra colors (Comparative inference) |

---

## Direction 1. Post-edit \(S_b\) screen on SIRD regime colors

**Pipeline stage:** PINN Customizer → evaluation (before expert visual judgment).  
**Mechanism:** After compile-pass retrain (or a cheap surrogate), sample a grid of nearby ICs / loss weights; color by asymptotic infected regime (short wave / plateau / runaway / extinguished); report \(S_b\). Reject or regenerate if \(S_b\) spikes vs baseline.  
**Failure modes addressed:** 15–28% “unchanged” misattributed solely to unused constants; silent basin jumps that still look “plausible.”  
**Acceptance:** report \(\Delta S_b\) alongside MAE 700/1100. (Speculative extension)

---

## Direction 2. Basin-entropy parameter set over Table A.2 penalties

**Pipeline stage:** Limitations / Future work templates.  
**Mechanism:** For class-4 peak-shift and BC-weight edits, build an \(S_b\) map over admissible weight ranges (Monte Carlo boxes as in Paper B) *before* free LLM rewrite; forbid templates that land in hot \(S_b\) cells. Use \(S_{bb}>\log 2\) as a fast fractal screen on the same grid.  
**Failure modes addressed:** Fig. 4b 700-day outbreaks; “PINN systemic limitations” claimed without a map.  
**Acceptance:** publish a parameter-set figure analogue of Paper B Fig. 4 for penalty weights. (Speculative extension)

---

## Direction 3. Stratify Fig. 5 failures by \(S_b\)

**Pipeline stage:** Results reporting / ablation.  
**Mechanism:** Re-bin the 20 launches per LLM into high vs low baseline \(S_b\) neighborhoods; report compliance conditional on entropy stratum.  
**Failure modes addressed:** pooling structure-limited runs with pure LLM misses into one 25–27% number. (Speculative extension)

---

## Manuscript placement

- **§3.4 / Limitations (PINN systemic limits):** cite \(S_b\)/\(S_{bb}\) as measurable partition of LLM vs landscape failure (clusters **5**, **6**).
- **§2.4 Evaluation:** report \(\Delta S_b\) beside MAE 700/1100.
- **Future work templates:** forbid high-\(S_b\) weight cells before free rewrite.

## What not to transfer

Do not require Duffing oscillators, Wada-basin theory, or SciRep Monte Carlo grids as epidemic products. Transfer **basin-entropy diagnostic after warm-start retrain**—not a claim that SIRD already exhibits fractal boundaries. (Comparative inference)

## Concrete next experiment

**Hypothesis.** A non-trivial fraction of “forecast unchanged” (15–28%) and Fig. 4b disasters have elevated \(\Delta S_b\) vs baseline even under *identical* loss (seed-only warm-start), separating basin stickiness from LLM semantic error.

**Protocol.** (i) Continue-train with *unchanged* loss, multiple seeds → baseline \(S_b\). (ii) Apply LLM edit → retrain → \(S_b'\). Color asymptotic regimes (short wave / plateau / runaway / extinguished) on a coarse IC/weight grid (Paper B Monte Carlo spirit).

**Metric.** \(\Delta S_b\); fraction of “unchanged” in high-\(S_b\) cells; compliance stratified by entropy. Expect some unchanged cases are basin, not unused constants. (Speculative extension)

## Related essays in this series

- [`16_skvorc_2020_ela_problem_space.md`](16_skvorc_2020_ela_problem_space.md) — scale hygiene for MAE.
- [`12_mehdi_2015_compositional_forecasting.md`](12_mehdi_2015_compositional_forecasting.md) — share metrics vs absolute MAE.
- [`01_hidalgo_2018_glucose_grammatical_evolution.md`](01_hidalgo_2018_glucose_grammatical_evolution.md) — zones for regime colors.
- Bridge: [`../dinara_analysis/39_malan_gradient_walk_nn_landscapes.md`](../dinara_analysis/39_malan_gradient_walk_nn_landscapes.md) — NN landscape probes.

## Conclusion

Daza et al. quantify a kind of uncertainty Expert-Guided PINN currently only narrates: which final epidemiological state a trajectory reaches when attractors mix. Paper A’s 15–28% unchanged forecasts and catastrophic long outbreaks sit at the intersection of LLM mis-edits *and* multistable PINN/SIRD structure. Basin entropy \(S_b\) and boundary entropy \(S_{bb}\) give objective diagnostics that MAE thresholds and subjective compliance cannot. Until Expert-Guided PINN reports basin entropy beside Fig. 5, “PINN limitations versus LLM error” remains an untested hypothesis rather than a measured partition.