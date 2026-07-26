> **Paper B — live link:** [https://doi.org/10.1038/s43588-025-00858-x](https://doi.org/10.1038/s43588-025-00858-x)  
> **Source in `src/`:** [`../src/2024 Deep active optimization for complex systems.md`](../src/2024%20Deep%20active%20optimization%20for%20complex%20systems.md)

Gindullina et al. (hereafter **Paper A**) build an interactive framework in which an epidemiologist's free-text comment is routed through a Conversational Agent, a hierarchical BERT+ML classifier (~81% accuracy), and a PINN Customizer that constructs a single prompt for an off-the-shelf LLM (Llama-3.1-8B / Llama-3.3-70B / DeepSeek-V3.1, temperature=1.0). The LLM rewrites the SIRD PINN loss in one shot; the system checks only compilability and iteratively re-asks on syntax errors, then retrains the PINN and shows the new forecast. The best "Compliance with the comment" rate is 25–27% over 20 launches; Fig. 4b documents a boundary-condition weight edit that produced a 700+ day outbreak, and Fig. 4c documents a ×4 BC reweight that was "effectively random rather than logically justified." Future work names class/subclass modification templates and an "LLM-expert-evaluator" as the two most urgent extensions.

Wei, Peng, Xie et al. (2024/2025; hereafter **Paper B**) present DANTE — deep active optimization with neural-surrogate-guided tree exploration (NTE). A DNN surrogate is trained on ~200 initial points; a tree search over the feature vector expands leaves stochastically, ranks them with a data-driven UCB (DUCB) that adds DNN-predicted node value to the visit-count exploration term, and uses two custom mechanisms — conditional selection and local backpropagation — to prevent value deterioration and escape local optima. Real-world validators (FE, DFT, AlphaFold2) are called only on top candidates; DANTE reaches global optima in 20-to-2,000-dimensional synthetic benchmarks with as few as 500 samples and beats 11 SOTA baselines. Ablation shows that removing conditional selection or local backprop drops convergence to 0%.

Paper B is not about PINNs, LLMs, or epidemics; it is a working active-optimization loop that Paper A is a degenerate case of. Paper A retries the LLM only on compile failure — a strictly weaker acquisition rule than DUCB — and has no mechanism to reject value-deteriorating or locally trapped modifications before a full PINN retrain. The transferable thesis is sharp: **Paper A's expert-in-the-loop cycle is an under-specified deep AO instance whose documented catastrophes (Fig. 4b/c, 15–28% "forecast unchanged") are the exact failure modes DANTE names, ablates, and cures; DANTE also demonstrates that a deep surrogate can pre-score candidate modifications before the expensive validator (full PINN retrain), turning Paper A's single-shot rewrite into a principled sample-efficient search.**

---

## 1. Paper A as an under-specified deep AO instance

Paper A frames itself as an "expert-in-the-loop optimization cycle" but never states an objective function over the space of loss modifications; each round is a one-shot LLM rewrite scored post hoc by author judgment. Paper B is explicit that closed-loop search over expensive labels is exactly the active-optimization frame:

> **Quote (Gindullina et al.):** *"A key contribution of this study is an interactive framework that instantiates an expert-in-the-loop optimization cycle... The loop is closed by presenting the refined forecast to the expert, enabling continuous model alignment with domain knowledge."*

> **Quote (Wei et al.):** *"these data-driven AI algorithms operate in a closed loop to guide experiments or simulations, iteratively identifying and labeling the most informative data points to discover the next best candidates while minimizing data labeling efforts. This approach is known as active learning."*

Under this reading, Paper A's "expert" occupies DANTE's "validation source" slot (FE / DFT / AlphaFold), the LLM occupies the surrogate/search slot, and the PINN retrain occupies the expensive labeling step. What is missing is precisely the acquisition function: Paper A has no formal signal that selects among candidate loss rewrites — it accepts the first compilable one. (Comparative inference)

---

## 2. Compile-only retry vs DUCB as acquisition

Paper A's iterative correction is triggered exclusively by the Python interpreter, never by forecast quality. DANTE's DUCB is the opposite — a scalar acquisition score that combines a learned value estimate with a visit-count exploration term, so nodes are compared on predicted usefulness before any expensive evaluation.

> **Quote (Gindullina et al.):** *"Syntactic analysis – checking the code's compilability using the Python interpreter. Iterative correction – if compilation errors are detected, the system automatically generates a clarifying request to LLM describing the error so that a corrected version can be regenerated."*

> **Quote (Wei et al.):** *"DUCB modifies the original UCB formula by incorporating DNN predictions for node value estimation and adding 1 to the denominator, effectively treating all nodes as if they have been visited at least once. This adjustment ensures that DUCB consistently yields finite values for every node, eliminating the need for exhaustive stochastic rollouts at each leaf."*

Compile-passing code that produces a 700-day outbreak still passes Paper A's gate. A DUCB-shaped gate would demand a *predicted forecast value* before commit; the retry mechanism reduces to a special case where the learned value is $-\infty$ on syntax failure and undefined otherwise. (Comparative inference)

---

## 3. Fig. 4b as canonical value deterioration

Paper A describes Fig. 4b as "in the absence of clear and interpretable modification rules, an LLM may generate a loss function whose use leads to inadequate forecasts." Paper B has a name for this failure and an evaluated mechanism against it.

> **Quote (Gindullina et al.):** *"the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days)."*

> **Quote (Wei et al.):** *"A search tree without conditional selection often results in lower-value leaf nodes being selected during expansion, leading to a rapid decline in value and ultimately hindering the discovery of superior nodes. In NTE, if the DUCB of the root node exceeds that of all leaf nodes, the search continues with the same root node in the next round."*

Framed in DANTE's terms, Fig. 4b is a value-deterioration event: the LLM emitted a leaf (BC-weight reduction) whose predicted forecast quality was lower than the root (unmodified loss), yet Paper A's gate accepted it because it compiled. Conditional selection would have kept the root. Empirically (Fig. 3b in Paper B), removing conditional selection collapses convergence to 0%. (Comparative inference)

---

## 4. Fig. 4c as local-optimum trapping

Paper A's ambiguous case is a modification that formally satisfies rules but produces an unrealistic plateau; the authors attribute this to loss modifications that are "effectively random." Paper B explicitly describes the same failure and its escape mechanism.

> **Quote (Gindullina et al.):** *"modifications to the loss function may be effectively random rather than logically justified by epidemiological reasoning."*

> **Quote (Wei et al.):** *"When DANTE is trapped in a local optimum, repeated visits to the same node trigger updates in the DUCB values of the root and neighboring nodes, generating a local DUCB gradient that helps guide the algorithm away from the local optimum."*

The mechanism is available because DANTE tracks per-leaf visit counts and updates them locally; Paper A has no visit counter — each launch is independent, temperature 1.0 provides free variance but no gradient. Ablating local backprop in Paper B drops convergence to 0%; Paper A operates permanently in that ablated regime. (Comparative inference)

---

## 5. Expensive validator: full PINN retrain as the costly label

Paper A's validator is a full PINN retrain with LR decay every 5,000 epochs — the epidemiological analogue of Paper B's alloy synthesis or AlphaFold call. Paper B's whole design is built to *minimize* the number of times that validator runs.

> **Quote (Gindullina et al.):** *"the model is trained with the Adam optimizer at an initial learning rate of 0.0001, scheduled to decay by a factor of 10 every 5000 epochs."*

> **Quote (Wei et al.):** *"conducting experiments or simulations can be extremely costly, with processes such as synthesizing and characterizing advanced alloys or drug-relevant molecules often costing millions of dollars and taking months or even years of intense labor."*

Every LLM proposal in Paper A pays the full retrain cost regardless of the odds it produces a useful forecast; DANTE would train a cheap surrogate `f: (comment, current loss AST, candidate edit) → predicted forecast skill` and only pass the top-k candidates through the full retrain. This is the concrete Direction 1 below. (Comparative inference)

---

## 6. Ablation logic Paper A does not run

Paper A ships a 4-component architecture (Conversational Agent, classifier, PINN Customizer, LLM) with no per-component ablation. Paper B ablates every DANTE mechanism on Rosenbrock-100d and shows which are load-bearing.

> **Quote (Wei et al.):** *"Without conditional selection, the tree search suffers from the value deterioration problem and has a 0% convergence ratio... Without local backpropagation, DANTE becomes a greedy stochastic tree search, leading to poor performance and similarly a 0% convergence ratio."*

> **Quote (Gindullina et al.):** *"The architecture of the proposed solution includes four main components (Figure 1): Conversational Agent... Hierarchical text classifier... PINN Customizer... LLM"*

Which of the four components in Paper A actually raises compliance above baseline is empirically unknown; the Conversational Agent alone is never evaluated. DANTE's ablation template — remove one mechanism, hold everything else, report convergence ratio and sample count — transfers directly. (Speculative extension)

---

## 7. Discrete feature-vector representation for loss edits

DANTE handles both continuous and discrete search spaces by treating each candidate as a feature vector (e.g., 20-integer amino-acid sequences for peptides, 27-element atomic-percentage vectors for alloys). Paper A's Table A.2 already imposes a discrete class/subclass ontology over admissible edits — exactly the encoding NTE expects.

> **Quote (Wei et al.):** *"We represent the cyclic peptide as a sequence of integers that range from 0 to 19, with each number corresponding to a distinct type of canonical amino acid. The leaf node within the DANTE framework is obtained through stochastic expansion. In this process, two complementary strategies are used: one that introduces random mutations in existing sequences and another that generates entirely new sequences."*

> **Quote (Gindullina et al.):** *"Rules for modifying the loss function based on the class and subclass of the expert comment. Each term represents a specific compartment: term1 (susceptible), term2 (infectious), term3 (dead), term4 (recovered)."*

Encoding a loss edit as `(class, subclass, target_term, operator, numeric_range)` gives a 5-integer feature vector. Stochastic expansion (one-step move, single mutation, scaled mutation) maps onto Table A.2 in the obvious way — flipping one field, changing operator, or resampling a bounded numeric — and yields a tree of *typed* modifications that a DUCB-shaped acquisition can rank. (Comparative inference)

---

## 8. Data efficiency: n=20 free-variance runs vs principled acquisition

Paper A produces variance across launches by setting the LLM temperature to 1.0 and running 20 times. This is not exploration — it is entropy without an acquisition rule. Paper B contrasts principled exploration with random search across every synthetic benchmark; random reaches no global optimum, DANTE reaches all.

> **Quote (Gindullina et al.):** *"All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment. This setting was used exclusively during the testing and prototyping phase to explore the system's full behavioral range."*

> **Quote (Wei et al.):** *"DANTE consistently attains the global optimum with the fewest data points in most tasks, whereas most competing methods fail to achieve the global optimum altogether."*

Paper A's headline 25–27% is measured under the exploration-free "just crank T=1.0" protocol; with n≈20 and p≈0.25 the 95% CI on compliance is roughly ±19 percentage points. Replacing free variance with a DUCB-directed sampler is expected to raise the compliance rate at fixed sample count, and — more importantly — make sample count itself the reportable metric. (Comparative inference)

---

## 9. Comparison table

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Acquisition rule | Compile-check + retry | DUCB = DNN value + visit-count exploration | Compile-only is a strictly weaker gate (Comparative inference) |
| Anti-stagnation mechanism | None (temperature=1.0 free variance) | Conditional selection + local backprop | Fig. 4b/c are named DANTE failure modes (Empirically shown for B) |
| Validator per proposal | Full PINN retrain (LR decay 5,000 epochs) | Surrogate first, expensive validator on top-k | Surrogate pre-screen bypasses most retrains (Comparative inference) |
| Search space encoding | Table A.2 English rules inside a prompt | Integer feature vectors with stochastic expansion modes | Table A.2 is one integer vector away from an NTE-ready space (Speculative extension) |
| Sample efficiency claim | 25–27% success at n=20, T=1.0 | Global optimum at 500 pts in 100d, 3,000 pts in 1,000d | n=20 is far below the smallest DANTE regime (Author-stated for B) |
| Ablation of pipeline | None (4 components, no isolation) | Every mechanism ablated, 0% without CS or LB | Paper A lacks the evidence to attribute its 25% to any single component (Comparative inference) |
| Data regime | Single dataset, single wave, T=1.0 | 6 synthetic + 4 real-world, up to 2,000d | Paper A's regime resembles Paper B's *baseline*, not its results (Comparative inference) |

---

## Direction 1. Pre-retrain surrogate over loss modifications (DANTE-style)

**Pipeline stage.** PINN Customizer + evaluation loop (replace single-shot rewrite + full retrain).  
**Mechanism.** Encode a candidate loss modification as a discrete feature vector `(class, subclass, term_id, operator, numeric_bucket)` derived from Table A.2 plus the planned modification templates. Train a lightweight DNN surrogate `f_θ` mapping `(base loss AST, comment embedding, candidate edit vector)` to predicted post-retrain forecast skill (out-of-sample WIS or MAE). Run NTE with DUCB over this space at each expert comment; retrain the PINN only on top-k candidates ranked by DUCB. Update `f_θ` with each new (edit, actual retrain outcome) pair.  
**Failure modes addressed.** Fig. 4b 700-day outbreak (value deterioration — root retained by conditional selection); Fig. 4c ambiguous stalling (local-optimum escape via local backprop); 15–28% "forecast unchanged" (unused-term edits get low predicted skill and are filtered before retrain); literal numeric insertion (numeric_bucket coordinate is bounded, not free text).  
**Expected signal.** Under a fixed compute budget, principled acquisition should improve compliance-at-fixed-k and lower expected retrain calls per successful modification. (Speculative extension)

---

## Direction 2. Real ground-truth validator: out-of-sample forecast skill

**Pipeline stage.** Evaluation (replace subjective "Compliance with the comment").  
**Mechanism.** Adopt Paper B's "validation source" role for out-of-sample forecast skill: hold future incidence points, retrain with the modified loss on past data only, score the modification via WIS/PIT/MAE against the actually observed future. Score becomes the DANTE label — objective, external, and computable at fixed cost.  
**Failure modes addressed.** Subjective author judgment on primary metric; conflation of "instruction-following" and "forecast improvement"; researcher-degrees-of-freedom in MAE thresholds 700/1,100.  
**Design caution.** Unlike AlphaFold, the epidemic ground truth appears only post-hoc; the surrogate loop must be trainable on retrospective data before deployment on live forecasts. (Speculative extension)

---

## Manuscript placement

- **§2.3 PINN Customizer + Future work:** cite DANTE as the empirical precedent that expert-guided loss modification is best treated as a search over a typed feature vector under a principled acquisition rule, not a single-shot LLM rewrite (clusters **1**/**2**/**9** of `dinara_comprehensive_review.md`).
- **§3.4 Discussion of Fig. 4b/c:** frame the two failures as value-deterioration and local-optimum trapping respectively, with DANTE's conditional selection + local backprop as the named cures (cluster **5** secondary, pathology framing).
- **§4 Limitations:** replace "modifications may be effectively random" with the sharper claim that Paper A currently operates in the *ablated* regime DANTE tests against (0% convergence baseline).
- **Introduction:** position novelty relative to LLM-as-optimizer literature (Eureka, OPRO, Text2Reward — cluster **1**) and scientific-discovery search (LLM-SR, FunSearch — cluster **11**), of which DANTE is the sample-efficient DNN-surrogate variant.

## What not to transfer

DANTE's DNN surrogate is trained over materials descriptors or protein sequences with real physical validators (FE, DFT, AlphaFold2); the analogue in Paper A must operate over `(loss AST, comment, edit)` triples with retrospective forecast-skill labels, and cannot leverage AlphaFold-style universal validators. Do not import the Kubo–Bastin conductivity or Rosetta interface analyzer machinery. The 2,000-dimensional convergence claim does not license extrapolation to Paper A's tiny 4-class × few-subclass ontology; DANTE's most transferable regime is *low-dimensional, low-data* — precisely where Paper A already lives. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Under matched compute budget (equal number of PINN retrains), a DUCB-directed sampler over `(class, subclass, term_id, operator, numeric_bucket)` yields higher compliance-at-fixed-k and higher out-of-sample forecast skill than Paper A's single-shot Table A.2 rewrite.

**Feature vector.**
```text
edit = (class ∈ {1..4},
        subclass ∈ subclass_pool[class],
        term_id ∈ {L_data, L_IC, L_ODE.S, L_ODE.I, L_ODE.R, L_ODE.D},
        operator ∈ {AddPenalty, Reweight, ShiftPeak},
        numeric_bucket ∈ subclass_admissible_range)
```

**Protocol.** Fix Llama-3.3-70B. For each of the 20 existing comments, expand k=8 leaves via stochastic expansion (one-step, single mutation, scaled mutation with p=1/3 each); rank by DUCB using a small surrogate trained on retrospective (edit, retrain-outcome) pairs from Paper A's public runs; retrain top-1. Compare to Paper A's single-shot baseline on: compile@1, out-of-sample WIS, unused-term rate, per-comment retrain count.

**Expected signal.** ≥10 p.p. improvement in out-of-sample WIS at equal retrain budget; ≥50% reduction in unused-term edits; sample-count-to-successful-modification becomes the primary reportable metric. (Speculative extension)

## Related essays in this series

- [`01_hidalgo_2018_glucose_grammatical_evolution.md`](01_hidalgo_2018_glucose_grammatical_evolution.md) — grammar as search-space encoding; complements NTE's feature vectors.
- [`05_merhej_2015_asp_rules_of_thumb.md`](05_merhej_2015_asp_rules_of_thumb.md) — soft-repair beats minimal edit; parallel to DANTE's principled acquisition beating random.
- [`11_daza_2016_basin_entropy.md`](11_daza_2016_basin_entropy.md) — basin entropy diagnoses uncertainty in dynamical systems; useful diagnostic for the surrogate.
- [`16_skvorc_2020_ela_problem_space.md`](16_skvorc_2020_ela_problem_space.md) — exploratory landscape analysis, relevant when the surrogate operates on a features-of-loss space.

## Conclusion

Paper B is not about PINNs, LLMs, or epidemics; it is about how to close an active-optimization loop when labels are expensive and the search space is high-dimensional. Read through that lens, Paper A is a working closed loop with the loop's *acquisition rule* replaced by a syntax check and the loop's *anti-stagnation mechanisms* replaced by temperature=1.0 free variance. Paper B names the failure modes that follow (value deterioration, local-optimum trapping, unused-visit padding) and ablates them empirically — turning Fig. 4b/c from unexplained catastrophes into predicted outcomes of running a specific ablated variant. Expert-Guided PINN can adopt DANTE's structural pattern — typed feature vectors, DUCB acquisition, surrogate pre-scoring before the expensive PINN retrain — without importing any of DANTE's domain machinery, and turn its 25–27% headline into a reportable sample-efficiency curve.
