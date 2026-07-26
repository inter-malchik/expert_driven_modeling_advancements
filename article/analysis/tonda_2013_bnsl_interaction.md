> **Paper B — live link:** [https://doi.org/10.1007/978-3-319-11683-9_17](https://doi.org/10.1007/978-3-319-11683-9_17)  
> **Source in `src/`:** [`../src/2013 Balancing User Interaction and Control in BNSL.md`](../src/2013%20Balancing%20User%20Interaction%20and%20Control%20in%20BNSL.md)

Gindullina et al.'s work (hereafter **Paper A**) builds Expert-Guided PINN so that an epidemiologist can reshape a SIRD forecast with natural-language comments: Conversational Agent → BERT class/subclass (~81%) → one-shot LLM loss rewrite → compile check → retrain. Compliance with the comment reaches only 25–27% for the best models and 6% for Llama-3.1-8B; evaluation remains author-judged plots, with no published study on institute epidemiologists.

Tonda, Spritzer & Lutton's *"Balancing User Interaction and Control in BNSL"* (hereafter **Paper B**) attacks the same HITL trade-off one decade earlier, for Bayesian network structure learning: experts mark edges **Forced / Forbidden / Normal**, then alternate visualization with automatic search (GTT, Bayesian Search, μGP). Preliminary tests used **two real agri-food experts**. The decisive result is not that memetic search scores higher, but that experts preferred **fast GTT iterations with persistent typed constraints** over slower “better” evolution—exactly the interaction discipline Paper A still lacks when it plans Smorodintsev validation and class-subclass templates (Comparative inference).

Thesis: free NL is not the scarce resource; **typed, cumulative constraints plus latency-aware iteration** are. Paper B already ran that protocol with n=2 domain experts; Paper A’s missing real-expert evaluation and Future-work templates should import Forced/Forbidden-style controls before adding more conversational freedom.

---

## 1. Same open problem: how often to ask the expert

Paper B frames the interaction–automation dilemma explicitly:

> **Quote (Tonda et al.):** *"How to best access an expert's knowledge, however, is still an open issue: asking a human user for input at a high frequency may lead to the well-known problem of user fatigue; not asking frequently enough might result in too little feedback."*

> **Quote (Tonda et al.):** *"full human interaction can lead to the well-known problem of user-fatigue, while a completely automated evolutionary process can miss important contributions by the expert."*

Paper A closes every successful run by returning a plot to a human, but never measures fatigue, wait time, or how many re-modification cycles experts will tolerate after a full PINN retrain (Author-stated loop in A; Empirically shown fatigue concern in B) (Comparative inference).

---

## 2. Real experts (n=2) versus author-as-expert and synthetic comments

Paper B’s evaluation is small but *real*:

> **Quote (Tonda et al.):** *"In order to validate the proposed approach, test runs were performed in cooperation with two experts on food processing and agriculture."*

> **Quote (Tonda et al.):** *"A test run with a modelling expert showed that the tool is able to assist the user in expressing knowledge that would be difficult to encode in a classical fitness function, returning more satisfying models than a completely automatic approach."*

Paper A’s classifier is trained on synthetic DeepSeek-generated comments, and “Compliance with the comment” is judged by the authors against plots:

> **Quote (Gindullina et al.):** *"The hierarchical classifier was trained and evaluated on synthetic data, which may not capture the full linguistic variability of real expert feedback. Large-scale validation on authentic expert comments is planned for future work at the Smorodintsev Research Institute for Influenza."*

> **Quote (Gindullina et al.):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the "Compliance with the comment" criterion."*

Paper B therefore supplies the missing *protocol shape*—domain specialists in the loop, qualitative satisfaction vs. fully automatic baselines—not merely another ML score (Comparative inference).

---

## 3. Forced / Forbidden / Normal as typed constraints on the search space

Paper B does not ask experts to rewrite fitness code. It asks them to **type** edges:

> **Quote (Tonda et al.):** *"Edge properties show the id and name of an edge's origin and target nodes and helps users prepare the network for evolution of the network by setting the edge as forced or forbidden, or leaving it as a normal edge. Forced edges will appear in green in the workspace, while forbidden edges will appear in red."*

Paper A already has a hierarchical ontology and Table A.2 “add penalty / PROHIBITED” rules, but the expert still speaks free NL that the LLM may literalize:

> **Quote (Gindullina et al.):** *"These rules, provided in Appendix A, represent strict guidelines for LLM, defining which components of the original loss function can be modified (e.g., by adding a penalty term) and which are prohibited."*

> **Quote (Gindullina et al.):** *"There is a systematic problem with interpreting numerical values in expert comments. In particular, the meta-llama/Llama-3.3-70B-Instruct model exhibits a tendency to literally include these numerical parameters in the loss function without sufficient semantic adaptation."*

Forced/Forbidden is the UX pattern Paper A’s planned modification templates should expose *to the epidemiologist*, not only bury inside LLM prompts (Speculative extension grounded in B’s GUI; Author-stated templates in A).

---

## 4. Preference for fast iteration over “better” automation

The empirical punchline of Paper B:

> **Quote (Tonda et al.):** *"Despite results of slightly higher quality provided by the memetic approach, both users felt that the improvement in quality did not justify the extra time needed to obtain the solution (this approach can take up to several minutes, while the others finish running after a few seconds). For this reason, the experts favoured a more interactive approach, running the deterministic heuristic (GTT), changing the forced and forbidden arcs in its results, and repeating the process until a satisfactory solution was found."*

Paper A’s loop always pays LLM generation **plus** full PINN retraining before any expert judgment; secondary criteria already show 15–28% of runs change the loss without meaningful forecast change (Empirically shown in A §3.4). Under Paper B’s preference ordering, that latency is a first-class failure mode for institute deployment, not a secondary engineering detail (Comparative inference).

---

## 5. Persistent constraints and side-by-side compare

Experts in Paper B asked for cumulative constraints and paired comparison:

> **Quote (Tonda et al.):** *"Since the process of structure learning is interactive, the users also noted how the possibility of cumulating constraints would be beneficial. In the current framework, the forced and forbidden arcs are clearly visible in each network, but they have to be set again every time a learning method is run."*

> **Quote (Tonda et al.):** *"They felt, however, that comparing candidates would have been more immediate and effective if the interface would allow such candidates to be shown side-by-side, two at a time."*

Paper A’s navigation pathway already shows initial vs. modified curves (Fig. A.7), but constraints are not a first-class, editable object across turns—each comment restarts the NL→class→LLM chain. Cumulating Forced/Forbidden analogues (e.g., “keep post-peak decay penalty; forbid weakening \(I(T_{\max})\to 0\)”) would have blocked the >700-day outbreak case where the LLM weakened the terminal boundary condition (Empirically shown in A Fig. 4b; Speculative extension).

---

## 6. Knowledge that will not fit a classical fitness / loss

Paper B’s scientific motivation matches Paper A’s Introduction:

> **Quote (Tonda et al.):** *"Even though several classes of complex problems can be effectively tackled with Evolutionary Computation, most possess qualities that are difficult to directly encode in the fitness function or in the individual's genotype description."*

> **Quote (Gindullina et al.):** *"Our solution eliminates the need for rigorous a priori mathematical formalization and static architecture, offering epidemiologists an adaptive tool for calibrating forecasts without requiring a deep understanding of the model's internal parameterization."*

Both papers reject “encode everything a priori.” Paper B shows experts can still contribute via **structured marks**; Paper A jumps to free text and then struggles at 25–27% compliance (Empirically shown in A). The comparative lesson is sequencing: typed interaction first, NL as a fallback channel (Comparative inference).

---

## 7. Comparative summary

| Criterion | Paper A (Gindullina et al.) | Paper B (Tonda et al.) | Takeaway |
| :--- | :--- | :--- | :--- |
| Expert study | Planned at Smorodintsev; current eval author/synthetic | n=2 agri-food experts | B already ran the study shape A needs (Comparative inference) |
| Expert input form | Free NL (+ class confirm) | Forced / Forbidden / Normal edges | Typed constraints reduce literalization risk (Comparative inference) |
| Automation trade-off | One-shot LLM + full PINN retrain | Experts chose fast GTT over slow memetic | Latency dominates quality for HITL users (Empirically shown in B) |
| Constraint persistence | Rules in prompt / Table A.2 | Experts demanded cumulative constraints | Persist edits across iterations (Author-stated need in B) |
| Primary success | Subjective “Compliance with the comment” 25–27% | Qualitative “more satisfying” than fully automatic | A lacks B’s human-preference protocol (Comparative inference) |
| User fatigue | Unmeasured | Explicit design risk | Measure cycles-to-accept in institute study (Author-stated in B) |

---

## Direction 1. Forced / Forbidden / Normal for loss edits

**Pipeline stage:** Conversational Agent → PINN Customizer (replace free-form only).

**Mechanism:** After class/subclass confirmation, let the expert mark loss terms or epidemiological fluents as Forced (must strengthen), Forbidden (must not weaken), or Normal—mirroring Paper B’s edge properties—before the LLM runs.

**Failure mode:** Literal numeric insertion; 700-day outbreak from weakened boundary weight (Empirically shown in A).

(Speculative extension — UX Empirically shown in B.)

---

## Direction 2. Smorodintsev protocol after Paper B’s preference test

**Pipeline stage:** Evaluation / Future work user study.

**Mechanism:** With institute epidemiologists, compare (i) free-NL Expert-Guided PINN, (ii) typed-constraint + short retrain proxy, (iii) fully automatic baseline; record time-to-satisfactory forecast and fatigue, not only compliance %.

**Failure mode:** Designing for peak MAE quality while experts abandon slow loops (Empirically shown preference in B).

(Speculative extension)

---

## Direction 3. Cumulative constraint store across re-modification

**Pipeline stage:** PINN Customizer state.

**Mechanism:** Keep accepted Forced/Forbidden marks when the expert rejects a forecast and comments again—addressing Paper B’s “set again every time” complaint.

**Failure mode:** Ambiguous/unsuccessful Fig. 4 cases repeating the same unsafe edit class (Empirically shown in A).

(Speculative extension)

---

## Direction 4. Latency budget as a first-class metric

**Pipeline stage:** System calibration + reporting.

**Mechanism:** Report wall-clock per iteration (LLM + PINN) beside compliance; prefer templates/heuristics that finish in seconds when experts face multi-turn calibration, per GTT-over-memetic preference.

**Failure mode:** 15–28% “changed loss, unchanged forecast” wasting full retrains (Empirically shown in A).

(Speculative extension — preference Empirically shown in B.)

---

## Direction 5. Split large comment spaces like Paper B’s sub-networks

**Pipeline stage:** Expert UI / ontology navigation.

**Mechanism:** Paper B’s expert repeatedly partitioned the 27-variable cheese network into smaller sub-graphs to mark Forced/Forbidden with confidence; offer epidemiologists subclass-scoped edits (e.g., peak-only vs. full SIRD) instead of one global NL comment per turn.

**Failure mode:** Ambiguous whole-curve comments routed to the wrong loss term (Empirically shown in A Fig. 4).

(Speculative extension — partitioning Empirically shown in B §5.)

---

## Manuscript placement

- **Limitations (synthetic comments / no real experts) + Future work at Smorodintsev:** Paper B is the closest orphan precedent for *n≥2 domain experts* on an interactive model loop (cluster **8**).
- **§2.2–2.3 ontology/rules:** Forced/Forbidden/Normal as the UX for planned templates (cluster **9**).
- **Evaluation Approach:** add wall-clock per round as a first-class metric beside compliance (cluster **4** secondary).

## What not to transfer

Bayesian-network structure learning ≠ SIRD PINN loss editing. Do not require Qt GUIs, OGDF layouts, or GTT/μGP solvers. Transfer **interaction economics** (typed cumulative constraints, expert preference for fast loops, persistent Forced/Forbidden)—not BN scoring metrics. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Experts prefer Forced/Forbidden loss-AST tags + ≤60s preview over free NL→full retrain when both are offered, and typed tags raise joint (compile ∧ changed ∧ logic ∧ intent) success vs free NL.

**Protocol (Smorodintsev, n≥4 epidemiologists).** Within-subject: (A) current NL pipeline; (B) Forced/Forbidden/Normal on `{term, op, range}` with side-by-side plots. Cap each turn’s LLM+PINN budget; log latency and abandon rate.

**Metric.** Preference (forced choice); SUS; joint success rate; median seconds/turn. Expect B preferred on latency/satisfaction even if single-metric compliance is similar—mirroring GTT-over-memetic. (Speculative extension)

## Related essays in this series

- [`02_steiner_2024_steering_wheel_crn.md`](02_steiner_2024_steering_wheel_crn.md) — protocolized steering.
- [`09_hadjimichael_1993_interactive_inductive.md`](09_hadjimichael_1993_interactive_inductive.md) — suggest-then-select.
- [`14_bisquert_2015_dual_process_argument.md`](14_bisquert_2015_dual_process_argument.md) — engagement strata for the same study.
- Bridge: [`../dinara_analysis/15_ouyang_2022_instructgpt.md`](../dinara_analysis/15_ouyang_2022_instructgpt.md) — log success/fail as preference data, don’t discard.

## Conclusion

Tonda et al. show that domain experts will guide a hard model-learning loop when constraints are **typed**, **visible**, and **cheap to iterate**—and that they will reject higher-quality automation that makes them wait. Gindullina et al. already know free NL→loss is fragile (25–27% / 6%, subjective compliance, synthetic classifier data) and name templates plus institute validation. Read together, Paper B is not a Bayesian-networks footnote: it is the interaction blueprint Paper A’s Future work still needs before more conversational agents are stacked on an untyped, high-latency retrain cycle.
