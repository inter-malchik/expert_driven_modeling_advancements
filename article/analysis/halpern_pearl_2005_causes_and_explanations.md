> **Paper B — live link:** [https://arxiv.org/abs/cs/0011012](https://arxiv.org/abs/cs/0011012) (companion papers, revised 2005)  
> **Source in `src/`:** [`../src/2005 Causes and Explanations: A Structural-Model Approach. Part I: Causes.md`](../src/2005%20Causes%20and%20Explanations%3A%20A%20Structural-Model%20Approach.%20Part%20I%3A%20Causes.md) + [`Part II: Explanations.md`](../src/2005%20Causes%20and%20Explanations%3A%20A%20Structural-Model%20Approach.%20Part%20II%3A%20Explanations.md)

Gindullina et al. (hereafter **Paper A**) evaluate LLM-generated PINN loss modifications along four qualitative criteria — matching training data, forecast has changed, epidemic logic, and «Compliance with the comment» — the last of which the authors themselves describe as having «a significant subjective component». Fig. 4b (700-day outbreak from a boundary-condition weight reduction) is characterized as «effectively random rather than logically justified by epidemiological reasoning». Future work names an «LLM-expert-evaluator» that «could quantify forecast compliance with the original comment» — but no formal definition of what «compliance» means, or how to test it, is given.

Halpern & Pearl (2005; hereafter **Paper B**) — Part I *Causes* and Part II *Explanations* — supply exactly that missing formalism. Part I defines *actual causality* over structural equations via three conditions AC1–AC3: the cause must hold (AC1); there must exist a structural contingency (partition of variables into causally-active \(\vec{Z}\) and passive \(\vec{W}\), with alternative setting \(\vec{w}'\)) under which changing the cause changes the effect (AC2a) *and* setting \(\vec{W}\) to \(\vec{w}'\) does not by itself affect the effect (AC2b); and the cause is minimal (AC3). Part II builds on this to define *(causal) explanation* relative to an agent's epistemic state \(K\): an explanation of \(\varphi\) is a fact \(\vec{X}=\vec{x}\) that is not known for certain but which, if found to be true, would constitute an actual cause of \(\varphi\) in every context in \(K\) where it holds (EX1–EX4). Explanatory power and partial-explanation *goodness* are given probabilistic operational definitions.

Paper B is not about PINNs, LLMs, or epidemic forecasting; it is the foundational formalism under Miller 04 (Contrastive Explanation, already Rank 4) — and it directly supplies the missing definitional core for what Paper A's Future-work «LLM-expert-evaluator» must actually compute. The transferable thesis is sharp: **Paper A's «Compliance with the comment» is trying, informally, to test whether the LLM's loss modification constitutes an actual cause of the requested forecast change relative to the epidemiologist's epistemic state; Halpern-Pearl AC1–AC3 + EX1–EX4 give the exact conditions to make that test formal, and diagnose Fig. 4b as a canonical AC2b failure — the LLM's edit changed the effect but did not do so via a legitimate active causal process.**

---

## 1. Structural-equation model of the loss-modification pipeline

Paper A's pipeline is a chain: comment → class/subclass → LLM → modified loss → PINN retrain → forecast → author judgment. Paper B insists that causal claims about *this* chain be evaluated relative to an explicit structural model — which random variables are endogenous, which are exogenous, what functions relate them.

> **Quote (Gindullina et al.):** *"A key contribution of this study is an interactive framework that instantiates an expert-in-the-loop optimization cycle. The process begins with an expert's qualitative assessment of a forecast, which is translated into a structured specification for loss function modification."*

> **Quote (Halpern & Pearl):** *"the truth of every claim must be evaluated relative to a particular model of the world; that is, our definition allows us to claim only that \(C\) causes \(E\) in a (particular context in a) particular structural model. It is possible to construct two closely related structural models such that \(C\) causes \(E\) in one and \(C\) does not cause \(E\) in the other."*

Paper A never writes down the structural model. Endogenous variables are implicit (LLM sample, compile bit, loss AST, retrain seed, forecast trajectory, MAE bucket); exogenous variables (LLM temperature=1.0, PINN random seed, dataset) are also implicit. Under H-P, this omission is not a stylistic choice — it means every «cause» claim in Paper A (e.g. «the LLM's modification caused the 700-day outbreak») is model-underspecified. (Comparative inference)

---

## 2. AC1–AC3 and «Compliance with the comment»

Paper A's primary metric asks the human: does the modified forecast match the expert's textual commentary? Under Paper B's frame, this is a claim of the form «\((\text{LLM edit}) = (\text{specific modification})\) is an actual cause of \((\text{forecast change})\)» — a claim that must be checked against AC1 (both hold), AC2 (there is a contingency under which flipping the edit flips the forecast, and the contingency itself is causally inert), and AC3 (no smaller edit suffices).

> **Quote (Halpern & Pearl):** *"\(\vec{X} = \vec{x}\) is an actual cause of \(\varphi\) in \((M, \vec{u})\) if the following three conditions hold. **AC1.** \((M, \vec{u}) \models (\vec{X} = \vec{x}) \land \varphi\). **AC2.** There exists a partition \((\vec{Z}, \vec{W})\) of \(\mathcal{V}\) ... (a) changing \((\vec{X}, \vec{W})\) from \((\vec{x}, \vec{w})\) to \((\vec{x}', \vec{w}')\) changes \(\varphi\) from true to false. (b) setting any subset of variables in \(\vec{W}\) to their values in \(\vec{w}'\) should have no effect on \(\varphi\), as long as \(\vec{X}\) is kept at its current value \(\vec{x}\). **AC3.** \(\vec{X}\) is minimal."*

> **Quote (Gindullina et al.):** *"Compliance with the comment. This is the primary criterion for assessing the technical success of the modification system. A comparative analysis is performed between the expert's text commentary and the visualization of the modified forecast. If the forecast has changed in accordance with the commentary, the result is considered successful."*

Paper A's Criterion 4 does something like AC1 (both edit and effect hold) but skips AC2 and AC3 entirely. There is no test for whether the edit would still have changed the forecast under a structural contingency (e.g., different retrain seed); there is no test for whether a smaller edit would also suffice. This is exactly why 25–27% compliance is subjective — the criterion is under-specified. (Comparative inference)

---

## 3. Fig. 4b as AC2b failure

Paper A's Fig. 4b: the expert asks for a 7–10-day peak shift; the LLM reduces the boundary-condition weight; the forecast changes (700-day outbreak) but the change is not the requested one. In H-P terms, the LLM's edit *did* change the effect (AC2a holds), but under a structural contingency (BC weight = zero) the effect changes via a *different* active causal process than the one the comment specified. AC2b — «setting \(\vec{W}\) to \(\vec{w}'\) should not affect \(\varphi\)» — fails: the auxiliary manipulation is what actually drives the outcome.

> **Quote (Gindullina et al.):** *"the expert asked to shift the epidemic peak by 7–10 days ... The LLM ... responded to this comment by reducing the influence of the zero boundary condition ... the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days)."*

> **Quote (Halpern & Pearl):** *"AC2(b), which has no obvious analogue in the literature, is an attempt to counteract the "permissiveness" of AC2(a) with regard to structural contingencies. Essentially, it ensures that \(\vec{X}\) alone suffices to bring about the change from \(\varphi\) to \(\neg\varphi\); setting \(\vec{W}\) to \(\vec{w}'\) merely eliminates spurious side effects that tend to mask the action of \(\vec{X}\)."*

Framed as AC2b failure, Fig. 4b is not a mysterious «random» failure — it is a diagnosable event: the LLM emitted a candidate cause whose supposed active causal process (peak-shift request → BC-weight edit → new peak time) is *not* the actual active causal process (BC-weight edit → outbreak lengthening). A correct evaluator would test the modification against AC2b before accepting compliance. (Comparative inference)

---

## 4. Preemption: the doctor forgot to treat the epidemic

Paper B's Suzy-Billy preemption analysis gives the tools to distinguish "the LLM's edit caused the forecast change" from "a co-varying background variable caused the forecast change". Paper A's Fig. 4c (Llama-8B multiplied BC weight ×4, producing an unrealistic plateau) is a preemption analogue: which edit component actually drove the plateau?

> **Quote (Halpern & Pearl):** *"If we want to argue in a case of preemption that \(X = x\) is the cause of \(\varphi\) rather than \(Y = y\), then there must be a random variable ... that takes on different values depending on whether \(X = x\) or \(Y = y\) is the actual cause. If the model does not contain such a variable, then it will not be possible to determine which one is in fact the cause."*

> **Quote (Gindullina et al.):** *"the meta-llama/Meta-Llama-3.1-8B-Instruct model increased the weight of the zero boundary condition ... by a factor of four, which is difficult to interpret in relation to the expert's request. As a result, the new forecast shows a stabilization in the number of cases ... modifications to the loss function may be effectively random rather than logically justified by epidemiological reasoning."*

Paper B insists on a *disambiguating variable* — a proxy variable whose value distinguishes candidate causes. For Paper A, this would be a per-comment «which loss component was expected to drive the change» tag: an evaluator can then check whether the modification's actual effect passed through that component. Without such a variable, «effectively random» is a description of unmeasured preemption, not of true randomness. (Comparative inference)

---

## 5. Explanation relative to \(K\): the epidemiologist's epistemic state

Paper B Part II is emphatic that explanation is agent-relative: what counts as an explanation depends on what the agent already knows.

> **Quote (Halpern & Pearl):** *"Following Gärdenfors, we take the notion of explanation to be relative to an agent's epistemic state. What counts as an explanation for one agent may not count as an explanation for another agent."*

> **Quote (Halpern & Pearl):** *"An individual in a given epistemic state \(K\) asks why \(\varphi\) holds. What constitutes a good answer to his question? A good answer must (a) provide information that goes beyond \(K\) and (b) be such that the individual can see that it would, if true, be (or be very likely to be) a cause of \(\varphi\)."*

Paper A's evaluator (the author playing the epidemiologist) has an implicit epistemic state \(K\), but it is never described. The four criteria act as if there were a universal notion of «adequate response» — but «shift the peak by 7–10 days» means one thing to a specialist who already knows peak-timing coincides with post-peak slope, and another to a non-specialist. The two interpretations exclude different modifications. Formally: `EX2` (the proposed explanation must be a sufficient cause of \(\varphi\) *in every context in \(K\) where the explanation holds*) requires that the evaluator's \(K\) be pinned down before compliance can be checked. (Comparative inference)

> **Quote (Gindullina et al.):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the "Compliance with the comment" criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results."*

The subjectivity Paper A admits is exactly the missing \(K\).

---

## 6. Sufficient cause vs actual cause: compile-check as sufficient only

Paper B distinguishes sufficient cause (AC1 + AC2 without minimality) from actual cause (AC1 + AC2 + AC3). Paper A's automatic gate — «did the code compile?» — tests something even weaker: sufficient causation of «execution proceeds», not sufficient causation of «forecast changes as requested».

> **Quote (Halpern & Pearl):** *"\(\vec{X} = \vec{x}\) is a sufficient cause of \(\varphi\) in \((M, \vec{u})\) if AC1 and AC2 hold, but not necessarily AC3."*

> **Quote (Gindullina et al.):** *"Syntactic analysis – checking the code's compilability using the Python interpreter. Iterative correction – if compilation errors are detected, the system automatically generates a clarifying request."*

Compile-passing is a sufficient cause of «PyTorch executes»; it is not a sufficient cause of anything about compliance. The gap between «code compiles» and «modification is an actual cause of the requested forecast change» is exactly where all Paper A's failure modes live: unused terms, literal number insertion, BC-weight arbitrariness. AC3-minimality also matters: if two unrelated LLM edits happen to co-produce compliance, minimality would reject the redundant one. (Comparative inference)

---

## 7. Explanatory power vs probability: reweighting Paper A's 25–27%

Paper B Part II Section 4 defines partial-explanation *goodness* as the conditional probability that the explanation actually causes the effect, and *explanatory power* as the prior probability that the explanation raises \(\varphi\)'s probability via its own contexts.

> **Quote (Halpern & Pearl):** *"we would argue that a better measure of the explanatory power of \(\vec{X} = \vec{x}\) is \(\Pr^-(K_{\vec{X}=\vec{x},\varphi} \mid \vec{X} = \vec{x})\). ... In particular, they agree that \(O = 1\) [oxygen] has very low explanatory power, while \(ML_1 = 1\) [an arsonist's match] has high explanatory power."*

> **Quote (Gindullina et al.):** *"The key result is confirmation of the fundamental feasibility of integrating expert knowledge through LLM into PINN, with a success rate of 25-27% for the best models."*

Under H-P, 25–27% is a raw hit rate that mixes: (a) partial explanations with high goodness but low probability (a rare LLM edit that would actually cause the requested change); (b) partial explanations with low goodness but high probability (a common LLM edit that happens to co-occur with a compliant forecast for unrelated reasons — the barometer-and-rain problem Paper B explicitly warns against). Decomposing 25–27% into goodness × probability would reveal which term Paper A is optimizing when it changes LLM scale. (Comparative inference)

---

## 8. Comparison table

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Causal model of pipeline | Implicit, unnamed variables | Explicit structural equations \((\mathcal{U}, \mathcal{V}, \mathcal{R}, \mathcal{F})\) | Every «cause» claim in A is model-underspecified (Comparative inference) |
| Primary compliance test | AC1 only (both edit and effect hold) | AC1 + AC2 (contingency) + AC3 (minimality) | 25–27% counts unstructured coincidences (Comparative inference) |
| Test for structural contingency | Absent (each launch independent) | Partition \(\vec{Z} \cup \vec{W}\), test AC2a + AC2b | Fig. 4b is a canonical AC2b failure (Empirically shown for B) |
| Agent's epistemic state | Implicit, un-parameterized | Explicit set \(K\) of contexts | Compliance is \(K\)-relative; no unique answer without \(K\) (Comparative inference) |
| Preemption handling | Ambiguous («effectively random») | Disambiguating variable required | Fig. 4c is unresolved preemption, not randomness (Comparative inference) |
| Explanation quality | Binary success | Partial goodness × probability | Decompose 25–27% by goodness (Speculative extension) |
| Compile-check role | Primary automatic gate | Sufficient cause of execution, not of compliance | Gap between compile and actual cause is unmonitored (Comparative inference) |

---

## Direction 1. Actual-cause test as the LLM-expert-evaluator's primary check

**Pipeline stage.** Evaluation (replace subjective «Compliance with the comment») + Future work «LLM-expert-evaluator».  
**Mechanism.** Implement AC1–AC3 as a testable procedure per (comment, modification, forecast) triple. AC1: verify the modification is applied and forecast changes. AC2a: perturb the modification (revert the single most-salient LLM-edited AST node) and check that the forecast reverts (structural contingency at \(\vec{w}'\)). AC2b: hold the modification fixed and perturb *other* pipeline variables (retrain seed, unrelated hyperparameter) — verify these do not by themselves reproduce the target forecast. AC3: try smaller edits (each AST node individually) and verify none alone suffices.  
**Failure modes addressed.** Fig. 4b AC2b failure (BC-weight edit alone drives outcome, not the peak-shift request); Fig. 4c preemption; unused-code (fails AC3 minimality); literal-number insertion (fails AC1 if the number is not the operative cause). (Speculative extension)

---

## Direction 2. Explanation-with-epistemic-state \((\psi, \vec{X}=\vec{x})\) as the compliance rubric

**Pipeline stage.** Evaluation + Conversational Agent + expert-side interface.  
**Mechanism.** Adopt Paper B's general Definition 5.1 form \((\psi, \vec{X}=\vec{x})\) where \(\psi\) restricts admissible causal models (Paper A's Table A.2 rules and epidemiological invariants) and \(\vec{X}=\vec{x}\) is the modification. Elicit an epidemiologist's epistemic state \(K\) upfront via a short pre-questionnaire (which peak-timing conventions, which SIRD parameterization). Check EX1–EX4 rather than a binary «yes, it complies» vote. Report partial-explanation *goodness* per Paper B Definition 4.3.  
**Failure modes addressed.** Subjective binary primary metric; conflation of «probability that this LLM edit occurs» with «probability that it causally explains the forecast change» — the barometer-and-rain problem. (Speculative extension)

---

## Manuscript placement

- **§2.4 Evaluation Approach + Future work «LLM-expert-evaluator»:** cite Paper B Part I AC1–AC3 as the formal definition of what compliance-testing must compute; cite Part II EX1–EX4 as the definition of what a partial explanation with goodness reports (clusters **3** LLM-as-judge, **4** proper scoring of `dinara_comprehensive_review.md`).
- **§3.4 Discussion of Fig. 4b/c:** relabel «effectively random» as AC2b failure and preemption without disambiguating variable; cite Miller 04 (which Paper B underlies) for the contrastive extension.
- **§4 Limitations:** replace «significant subjective component» with «\(K\) is unparameterized; goodness cannot be computed» — a sharper, remediable limitation.

## What not to transfer

Paper B is a philosophical foundation, not a running system — the AC1–AC3 test is not automated in a mature tool for large models like PINN loss ASTs. Do not import Halpern-Pearl's Suzy-Billy causal networks verbatim (they are illustrative examples over binary variables, not PINN forward passes). Do not treat AC1–AC3 as a decidable procedure without engineering: the partition search is exponential in the number of variables and requires the modeler to identify \(\vec{Z}\) and \(\vec{W}\); in practice, use *candidate* partitions restricted to the AST nodes edited by the LLM plus the PINN random seed. And do not conflate the epistemic-state \(K\) of Part II with the training-time \(K\) of a reward model — Paper B's \(K\) is a set of contexts, not a set of preference pairs à la TRM. (Comparative inference)

## Concrete next experiment

**Hypothesis.** For each of Paper A's 20 comments × 3 LLMs = 60 modifications, computing an operationalized AC1–AC3 test using a small automated perturbation harness (revert one AST edit; permute retrain seed; try each edit-node individually) will reclassify a substantial fraction of the 25–27% «compliant» modifications as AC2b failures — with the reclassification concentrated on cases where the LLM's edit is far from the loss term the comment class actually targets.

**Protocol.**
1. For each (comment class, modification), identify the AST node edited by the LLM.
2. AC2a: revert that node, rerun PINN retrain, check forecast reverts.
3. AC2b: hold the edit, permute retrain seed 5×, check forecast is stable (edit alone drives the change, not the seed).
4. AC3: if the LLM edited multiple nodes, try each individually.
5. Report: (fraction passing AC1 only) vs (fraction passing AC1+AC2a+AC2b+AC3).

**Expected signal.** Fraction passing full AC1–AC3 will be substantially below 25–27% — Paper A's headline number is closer to sufficient-cause than actual-cause rate. The gap size is the actionable metric.

**Ties to existing directions.** Direction 1 of this essay + Direction 1 of `20_zhang_…` (TRM training data): reclassified pairs (AC1-only pass, AC1+AC2+AC3 fail) become the informative training pairs for a Modification Quality Model. (Speculative extension)

## Related essays in this series

- [`04_miller_2020_contrastive_explanation.md`](04_miller_2020_contrastive_explanation.md) — direct extension of Paper B to contrastive foils; Miller cites Halpern-Pearl throughout.
- [`20_zhang_2026_trm_complex_reasoning.md`](20_zhang_2026_trm_complex_reasoning.md) — TRM as the automated evaluator; ME² quadrants map onto EX1–EX4 (macro-effectiveness ≈ AC2a, micro-effectiveness ≈ AC2b).
- [`07_walton_2010_dialogue_explanation.md`](07_walton_2010_dialogue_explanation.md) — dialogue transfer-of-understanding: how the epidemiologist's \(K\) is elicited operationally.
- [`19_wei_2024_dante_active_optimization.md`](19_wei_2024_dante_active_optimization.md) — surrogate that pre-screens candidates; can be gated on approximate AC2b-check before full retrain.

## Conclusion

Paper B is not about PINNs, LLMs, or epidemics; it is about what a causal claim and a causal explanation *mean* in a structural-equation model, and what an agent-relative explanation actually asserts about an agent's epistemic state. Paper A's Future-work «LLM-expert-evaluator» is a proposal to compute something like this — but without the formalism, it inherits the subjectivity Paper A itself flags. AC1–AC3 turn «did the LLM's edit cause the forecast change?» into a testable proposition; EX1–EX4 turn «did the modification satisfy the comment?» into a check against the epidemiologist's \(K\); explanatory power and partial-explanation goodness turn the 25–27% headline into two decomposable factors (goodness and probability). Fig. 4b becomes a diagnosable AC2b failure and Fig. 4c a preemption case missing a disambiguating variable — not «effectively random». Adopting Halpern-Pearl as the definitional core is the cheapest structural upgrade Paper A can make: no new code, only a stricter specification of what «compliance» computes.
