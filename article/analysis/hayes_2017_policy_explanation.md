> **Paper B — live link:** [https://doi.org/10.1145/2909824.3020223](https://doi.org/10.1145/2909824.3020223)  
> **Source in `src/`:** [`../src/2017 Improving Robot Controller Transparency Through Autonomous Policy Explanation.md`](../src/2017%20Improving%20Robot%20Controller%20Transparency%20Through%20Autonomous%20Policy%20Explanation.md)

Gindullina et al. (hereafter **Paper A**) close the Expert-Guided PINN loop with a plot and a subjective “Compliance with the comment” judgment (25%/27%/6% for Llama-70B / DeepSeek / Llama-8B). After the LLM rewrites the SIRD loss, the expert sees a curve—not a reason. Limitations admit that Appendix A’s coarse “Add penalty to term2” rules fail to ensure “semantic transparency and explainability of the changes made,” and Future work still names templates and checkers without an interaction language for *why* an edit fired.

Hayes and Shah (2017; hereafter **Paper B**) already solve a structurally analogous opacity problem for robot controllers (hard-coded conditionals, tabular RL, DQN): communicable predicates + Quine–McCluskey Boolean cover yield NL answers to “When do you…?”, “Why didn’t you…?”, and “What will you do when…?” without requiring the collaborator to read the policy code. The transferable thesis is sharp: **treat post-edit loss behavior as a queryable policy, and give Paper A’s Conversational Agent (and the planned LLM-loss-semantic-checker) Hayes-style predicate queries as the missing interpretability layer—not another plot glance.**

---

## 1. Opacity of learned/generated control is Paper A’s interpretability gap

Paper B frames the capability–transparency trade-off for controllers humans cannot inspect; Paper A inherits the same gap once the LLM emits a new loss.

> **Quote (Hayes & Shah):** *"As a robot’s roles and responsibilities grow increasingly complex, its controller can quickly become incomprehensible through the necessary use of these methods, highlighting an implicit trade-off between capability and transparency."*

> **Quote (Gindullina et al.):** *"A significant limitation is the lack of mechanisms to control the interpretability of the generated loss functions. The current rule system (Appendix A), based on specifying the target components of the loss function for modification, is insufficient to ensure semantic transparency and explainability of the changes made."*

Paper A’s Fig. 4b failure (peak-shift comment → weakened terminal BC → 700+ day outbreak) is exactly the kind of “why didn’t you do the intended behavior?” case Paper B designs Algorithm 3 to answer. (Author-stated gap in A; Author-stated framing in B) (Comparative inference)

---

## 2. Communicable predicates as the DSL between NL comment and loss AST

Paper B does not explain raw feature vectors; it projects states onto Boolean predicates with NL templates. That is the missing middle layer between Paper A’s free-text comment and the LLM’s free rewrite.

> **Quote (Hayes & Shah):** *"To make this natural language generation and interpretation tractable, we employ communicable predicates: Boolean classifiers similar to traditional STRIPS-style planning predicates with associated natural language descriptions."*

> **Quote (Gindullina et al.):** *"we plan to replace the simple penalty additions by class-subclass-specific modification templates. These templates will explicitly define which loss components and parameters can be altered, which mathematical operators are admissible, and what numerical ranges are permitted."*

A predicate library for Expert-Guided PINN—e.g., `peak_after(t*)`, `post_peak_decline_steep`, `I_end_near_zero`—would let templates *name* admissible effects, and let a post-retrain explainer *ground* whether those effects hold, instead of hoping the LLM’s penalty term is self-explanatory. (Comparative inference)

---

## 3. Three query templates map onto Paper A’s interaction loop

Paper B’s query set is not decorative HRI fluff; it matches the moments Paper A’s expert already faces—before comment, after failed edit, and when probing safety of a proposed change.

> **Quote (Hayes & Shah):** *"allowing for indication of environmental conditions under which certain robot behaviors will occur (“When do you do __?”), identification of which robot behaviors will occur under a specified set of environmental conditions (“What do you do when __?”), or an explanation for why a particular behavior did not occur (“Why didn’t you do __?”)."*

> **Quote (Gindullina et al.):** *"The conversational agent’s functionality includes validating expert comments for compliance with the following criteria: concreteness (a single specific point), certainty (lack of vagueness), and objectivity (lack of emotional overtones)."*

Today the Conversational Agent only gates comment *form*. Hayes-style queries would upgrade it to a *behavior* interface: after Fig. 4b, “Why didn’t you shift the peak?” should return a predicate difference (e.g., boundary weight changed; peak-day offset absent)—not another concreteness lecture. (Comparative inference)

---

## 4. “Why didn’t you” isolates the Fig. 4b pathology

Paper B’s conveyor-belt fault probe shows the payoff of contrastive debugging without reading code.

> **Quote (Hayes & Shah):** *"Using Algorithm 3, the model was able to identify the issue, responding with the following: “I did not inspect the part because I cannot reach the part. I inspect the part when the stock feed is on and I have detected a part and I can reach the part.”"*

> **Quote (Gindullina et al.):** *"The LLM `meta-llama/Llama-3.3-70B-Instruct` responded to this comment by reducing the influence of the zero boundary condition in the loss function… As a result, the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days)."*

Mapped: the intended “behavior” is peak shift; the realized dominant edit is BC attenuation. A predicate-cover answer—“I didn’t shift the peak because `I_end_near_zero` was relaxed; I shift peaks when `peak_day_offset ∈ [7,10]` is active”—would surface the semantic failure that compile-check and MAE≥700 currently miss. (Empirically shown failure in A; Empirically shown probe in B) (Comparative inference)

---

## 5. Minimal Boolean cover vs. opaque full loss dumps

Paper B measures explanation quality by accuracy, succinctness, and legibility—and minimizes DNF covers with Quine–McCluskey. Paper A currently offers either raw generated code or a plot.

> **Quote (Hayes & Shah):** *"As ideal model summaries are precise, concise, and interpretable, the quality of a system response is measured by its accuracy (faithfulness to the underlying model), succinctness (minimization of information transferred), and legibility (ability to be interpreted by a human)."*

> **Quote (Gindullina et al.):** *"After generating the LLM candidate loss function, its automatic validation is performed (Figure 2), which includes: 1. Syntactic analysis – checking the code’s compilability using the Python interpreter."*

Syntax gates faithfulness to Python, not faithfulness to intent. A minimized predicate cover of “states where the modified loss dominates the baseline trajectory” would be the interpretability artifact Future work’s LLM-loss-semantic-checker should verify against class/subclass rules. (Comparative inference)

---

## 6. Comparison table: interpretability after the edit

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Opaque artifact | LLM-rewritten PINN loss | RL / conditional robot policy | Same need: explain without reading code (Comparative inference) |
| Grounding layer | Planned modification templates; Appendix A NL rules | Communicable predicates + string templates | Predicates = executable middle DSL (Comparative inference) |
| Query language | Comment concreteness / certainty / objectivity | When / Why didn’t / What will you do | Behavior queries > form gates (Comparative inference) |
| Failure diagnosis | Author inspects Fig. 4 plots | Algorithm 3 predicate differences | Isolate BC vs. peak-offset edits (Empirically shown in B) |
| Success of explanation | Subjective comment–plot match 25–27% | Cover fidelity + FP/FN over/understatement | Succinct faithful cover ≠ visual vibe (Author-stated in B) |
| Conversational Agent role | Pre-filter comment quality | Interactive expectation calibration | Upgrade Agent to post-edit Q&A (Comparative inference) |

---

## 7. FP/FN cover bounds as honesty about approximate explanations

Paper B quantifies linguistic over- and understatement when predicates only approximate the true state region—critical for PINNs, where trajectories are continuous and predicates will be coarse.

> **Quote (Hayes & Shah):** *"Our formulation also affords the ability to quantify linguistic overstatement and understatement, mapping to false positive and false negative rates, respectively."*

> **Quote (Gindullina et al.):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the \"Compliance with the comment\" criterion."*

An Expert-Guided PINN explainer that reports “approximately: post-peak decline steep (FP 0.12)” is already more objective than a binary author compliance bit—and supplies features an LLM-expert-evaluator can cite. (Comparative inference)

---

## 8. Conversational Agent as the front-end for policy queries

Paper A’s Agent is unevaluated as a dialogue system; Paper B shows what a useful post-decision dialogue *asks*.

> **Quote (Gindullina et al.):** *"1. Conversational Agent, which helps the user formulate a comment suitable for forecast modification."*

> **Quote (Hayes & Shah):** *"This interactive, targeted expectation calibration is an important initial step toward understanding and debugging robot behaviors, as it facilitates the precise identification of the ways in which expected and realized actions do not align."*

Ablating component 1 should therefore measure not only “comment approved,” but whether experts can recover, via When/Why-didn’t/What-will queries, the dominant loss-edit predicates after retrain. That is an evaluation protocol Paper A currently lacks. (Author-stated unevaluated component in A; Author-stated interaction goal in B) (Comparative inference)

---

## 9. Domain coverage: discrete, continuous, and hand-coded controllers

Paper B validates across GridWorld Q-learning, CartPole DQN, and hand-coded inspection—showing the method is representation-agnostic. That matters because Paper A’s opaque artifact is neither an MDP nor a robot, but a regenerated Python loss: the same “policy” abstraction still applies if states are trajectory snapshots and “actions” are dominant loss-edit operators.

> **Quote (Hayes & Shah):** *"We demonstrate applicability to a variety of robot controller types including those that utilize conditional logic, tabular reinforcement learning, and deep reinforcement learning…"*

> **Quote (Gindullina et al.):** *"We introduce Expert-Guided PINN, a novel software framework for the interactive adaptation of Physics-Informed Neural Network (PINN) loss functions, powered by a Large Language Model (LLM)."*

Transfer does not require claiming that PINNs are MDPs; it requires treating the *post-edit behavioral model* (how forecasts change under comments) as something collaborators can query in predicate language. (Comparative inference)

---

## Direction 1. Predicate library over SIRD trajectories + loss terms

**Pipeline stage:** post-retrain UI + Future-work templates / LLM-loss-semantic-checker.  
**Mechanism:** Define communicable predicates on compartments and on loss components (`penalty_on_term2`, `bc_weight_scaled`, `peak_offset_active`); after each LLM edit, build a cover of trajectory differences and answer Hayes queries in the Conversational Agent.  
**Failure modes addressed:** opaque Fig. 4b/c edits; interpretability gap; Agent limited to form-checking.  
**Measurable acceptance:** expert can isolate intended vs. realized predicates without reading loss code. (Speculative extension)

---

## Direction 2. “Why didn’t you comply?” as semantic-checker input

**Pipeline stage:** LLM-loss-semantic-checker (Future work).  
**Mechanism:** On compliance failure, auto-issue Algorithm-3-style queries against intended subclass effects vs. observed dominant edit; feed the predicate diff back into regeneration prompts.  
**Failure modes addressed:** compile-pass / intent-fail; unused terms; literal numeric insertion without named operators. (Speculative extension)

---

## Direction 3. Pre-flight “What will you do when…” before full retrain

**Pipeline stage:** PINN Customizer, after compile check, before expensive retrain.  
**Mechanism:** Approximate the intended subclass effect as a predicate region; ask “What will you do when peak should shift 7–10 days?” against the candidate loss’s predicted effect signature; abort retrain if the cover cites BC attenuation instead of peak offset.  
**Failure modes addressed:** 700-day outbreaks that currently waste a full training run after a silent semantic mismatch. (Speculative extension)

---

## Manuscript placement

- **Limitations (interpretability of generated loss) + Future work semantic-checker:** predicates + When/Why-didn’t/What-will as the missing layer (clusters **9**, **8**).
- **§2.1 Conversational Agent:** upgrade from concreteness filter to query front-end over loss edits.
- **§2.3 after compile, before retrain:** “What will you do when…” preflight.

## What not to transfer

Do not require robot MDP logging, Quine–McCluskey covers, or GridWorld/CartPole demos as epidemic deliverables. Paper B has no epidemiology. Transfer **communicable predicates + three query templates**—not HRI team-fluency metrics as primary endpoints. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Preflight “What will you do when [subclass effect]?” aborts ≥50% of Fig. 4b-style BC disasters before retrain, without lowering compile@1.

**SIRD predicate library (minimal):** `peak_time_I`, `postpeak_slope_I`, `duration_outbreak`, `nonneg_all`, `bc_weight_I0`, `unused_penalty_present`.

**Protocol.** After LLM loss compile: verbalize top-k predicate effects; ask Why-didn’t / What-will against subclass foil; abort if cover cites forbidden predicates; else retrain. Compare abort-and-regen vs baseline single-shot.

**Metric.** Unsafe-edit rate (BC/IC flips without authorization); retrain waste (GPU-hours on rejected runs); Zone A among completed. (Speculative extension)

## Related essays in this series

- [`02_steiner_2024_steering_wheel_crn.md`](02_steiner_2024_steering_wheel_crn.md) — protocol step before execute.
- [`04_miller_2020_contrastive_explanation.md`](04_miller_2020_contrastive_explanation.md) — foil for Why-didn’t.
- [`07_walton_2010_dialogue_explanation.md`](07_walton_2010_dialogue_explanation.md) — exam after verbalization.
- Bridge: [`../dinara_analysis/03_yu_2025_spec2rtl_agent.md`](../dinara_analysis/03_yu_2025_spec2rtl_agent.md) — verify intermediate before target.

## Conclusion

Hayes and Shah supply the interpretability *interface* Paper A’s Limitations describe but do not design: predicates that ground opaque control in NL, plus When / Why-didn’t / What-will queries that turn expectation mismatch into a diagnosable difference. Expert-Guided PINN already has a Conversational Agent and a post-edit forecast; what it lacks is a policy-explanation layer between them. Until loss edits are queryable in predicate language, “semantic transparency” remains an aspiration and the Agent remains a concreteness filter rather than a transparency tool.
