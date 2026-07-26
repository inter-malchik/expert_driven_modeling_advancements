> **Paper B — live link:** [https://doi.org/10.1006/imms.1993.1008](https://doi.org/10.1006/imms.1993.1008)  
> **Source in `src/`:** [`../src/1993 interactive inductive learning.md`](../src/1993%20interactive%20inductive%20learning.md)

Gindullina et al. (hereafter **Paper A**) run an expert-in-the-loop PINN cycle: free-text comment → Conversational Agent → hierarchical class/subclass → PINN Customizer prompt → LLM rewrite of the entire SIRD loss → compile check only → retrain. Best “Compliance with the comment” is only 25–27% (DeepSeek / Llama-70B) vs 6% (Llama-8B) at temperature 1.0 (~20 launches). Documented pathologies include literal insertion of numeric cues from the comment into the loss, unused code, and a boundary-condition weight edit that produced a >700-day outbreak. Future work names class–subclass *modification templates* and an LLM-loss-semantic-checker—still as plans.

Hadjimichael and Wasilewska (1993; hereafter **Paper B**) already ship a closed interactive inductive cycle: user *conditions* (equivalence relations on attribute values) → Conditional Probabilistic Learning Algorithm (CPLA) → rule family → Condition Suggestion Algorithm (CSA) proposes *safer, syntax-derived* generalizations → user selects a subset → re-run. Preliminary results cut rule counts up to 43%; the grades example goes 11→6 rules after accepting CSA. Empirically, coarse user-supplied conditions over-generalize and raise entropy; CSA’s conservative merges do not.

The transferable thesis is sharp: **Paper A’s planned templates and interactive rewrite are not a green field—they are CPLA/CSA for PINN loss ASTs. The Customizer should propose admissible edits; the expert should accept a subset—not paste NL numbers straight into the objective.**

---

## 1. Interactive cycle: user conditions → rules → safer suggestions

Paper A already closes the loop with the expert at both ends (confirm class/subclass; accept/reject forecast). Paper B makes the *middle* of that loop explicit: the system does not only consume user structure—it *suggests* the next structure.

> **Quote (Hadjimichael & Wasilewska):** *"The cycle begins by taking any (possibly empty) set of user-supplied conditions and running CPLA on the examples database with those conditions. CPLA… will then output a family of decision rules which will then be passed to CSA, where suggested conditions will be generated. The user can examine the suggested conditions and select a subset of them to feed back into CPLA for another pass."*

> **Quote (Gindullina et al.):** *"A key contribution of this study is an interactive framework that instantiates an expert-in-the-loop optimization cycle. The process begins with an expert’s qualitative assessment of a forecast, which is translated into a structured specification for loss function modification."*

Paper A’s Customizer still treats the LLM as a one-shot rewriter after class confirmation. CSA’s role—emit candidate safe edits for user subset selection—is exactly what Future work’s templates + semantic-checker should implement. (Comparative inference)

---

## 2. Conditions as DSL; Table A.2 as prose without a suggestion engine

Paper B’s conditions are a typed DSL: equivalence relations on value sets that reshape indiscernibility before learning. Paper A’s Appendix A rules are English permissions (“Add penalty to term2”) that the LLM may still violate while compiling.

> **Quote (Hadjimichael & Wasilewska):** *"conditions specify equivalences on sets of attribute values, such that objects may become indistinguishable."*

> **Quote (Gindullina et al.):** *"For the confirmed class and subclass combination, the corresponding loss function modification rules are extracted from the knowledge base… defining which components of the original loss function can be modified (e.g., by adding a penalty term) and which are prohibited."*

> **Quote (Gindullina et al.):** *"we plan to replace the simple penalty additions by class-subclass-specific modification templates. These templates will explicitly define which loss components and parameters can be altered, which mathematical operators are admissible, and what numerical ranges are permitted."*

Historical precedent: Paper B already treats expert structure as an editable DSL inside the learning loop, not as free NL appended to a prompt. Paper A’s templates are rediscovering that interface for loss operators. (Author-stated) (Comparative inference)

---

## 3. Over-generalization: coarse user conditions vs literal numeric insertion

Paper B’s decisive empirical lesson is that *human* initial conditions can be worse than system-suggested ones: wide grade-band equivalences leave 11 rules, introduce non-deterministic/unknown rules, and raise entropy—whereas CSA’s limited merges yield six deterministic rules.

> **Quote (Hadjimichael & Wasilewska):** *"The number of rules did not decrease at all, because of the wide-ranging effect of the conditions supplied by the user. Also, for this set of rules, the entropy function is non-zero, since there are six non-deterministic rules… From these two facts we can conclude that the CSA-supplied conditions were better than the user-supplied conditions. Whereas the user made a general decision about the data, CSA made a more conservative and limited decision."*

> **Quote (Hadjimichael & Wasilewska):** *"So we see that CSA will always suggest the minimal set of conditions to reduce the size of the rule family, and is not as susceptible to over-generalization, as a human being might be."*

> **Quote (Gindullina et al.):** *"There is a systematic problem with interpreting numerical values in expert comments. In particular, the meta-llama/Llama-3.3-70B-Instruct model exhibits a tendency to literally include these numerical parameters in the loss function without sufficient semantic adaptation."*

Literal “7–10 day” insertion and unconstrained BC-weight edits are the PINN analogue of the user’s over-wide grade equivalences: the *form* of the expert cue is taken too literally, collapsing semantic intent. CSA’s lesson: map cues to *minimal admissible* operators, then let the expert approve—do not trust raw NL magnitude. (Empirically shown in B) (Comparative inference)

---

## 4. Fig. 4b disasters vs CSA’s “suggest, don’t auto-apply”

Paper A trains whatever compiles. Paper B never auto-applies CSA output; the user moderates feedback. That single design choice is the difference between a 700-day outbreak and a rejected suggestion.

> **Quote (Gindullina et al.):** *"As a result, the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days). This example illustrates that, in the absence of clear and interpretable modification rules, an LLM may generate a loss function whose use leads to inadequate forecasts."*

> **Quote (Hadjimichael & Wasilewska):** *"Figure 1 shows how the three elements of the system, CPLA, CSA and the user form a cycle in which the user moderates the feedback from CSA."*

> **Quote (Gindullina et al.):** *"After generating the LLM candidate loss function, its automatic validation is performed… Syntactic analysis – checking the code’s compilability using the Python interpreter."*

Compile-only gates accept over-generalized edits. A CSA-style Customizer would emit candidate template instantiations (peak offset ∈ [7,10], admissible terms) for expert subset selection *before* full retrain. (Comparative inference)

---

## 5. Comparison table: interactive structure and failure modes

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Expert structure object | Free NL + class/subclass + Table A.2 prose | Conditions = equivalence relations on `VAL_a` | Typed DSL > free rewrite (Comparative inference) |
| System suggestion role | Future: templates / semantic-checker | CSA proposes merges of similar rules | Suggest-then-select already worked in 1993 (Author-stated) |
| User moderation | Confirm class; accept/reject forecast | Select subset of suggested conditions | Missing: moderate *edits*, not only class tags (Comparative inference) |
| Over-generalization risk | Literal numeric insertion; BC weight disasters | Coarse user conditions ↑ entropy / unknowns | Conservative system suggestions beat raw user form (Empirically shown) |
| Success evidence | 25–27% best compliance (subjective) | Up to 43% fewer rules; 11→6 in grades example | Compaction + lower entropy as secondary metrics (Author-stated) |
| Auto-accept of machine edit | Yes if compiles | No—user chooses CSA subset | Fail closed before retrain (Comparative inference) |

---

## 6. Similarity merges as a template library sketch

CSA merges rules that share certainty and target concept, proposing the *minimal* conditions that collapse those domains—an early “admissible operator set” derived from syntax, not from free generation.

> **Quote (Hadjimichael & Wasilewska):** *"Two rules which map classes in \(R(A)^*\) to the same class in \(R(E)^*\) with the same certainty are considered similar."*

> **Quote (Hadjimichael & Wasilewska):** *"This algorithm forms of a set of suggested conditions to merge similar rules whose domains are described by the same attributes."*

> **Quote (Gindullina et al.):** *"The current system of rules for modifying loss functions lacks sufficient detail to provide meaningful control over the generation process."*

Transfer: for each subclass, precompute a finite set of *similar* loss edits (penalty on term2; bounded peak offset; time-window weight) and have the LLM *select/instantiate* among them—CSA for PINN—rather than inventing a new AST. (Speculative extension)

---

## 7. Feedback relationship vs static NL→objective claim

Paper A’s Introduction contrasts static expert constraints with adaptive NL interaction. Paper B already defined that distinctiveness against data-in/tree-out learners in 1993.

> **Quote (Hadjimichael & Wasilewska):** *"the model is distinctive in that it defines a feedback relationship between the user and the learning program, unlike other inductive learning systems which simply input data and output a decision tree. This interactiveness allows for rule (tree) compaction and generalization."*

> **Quote (Gindullina et al.):** *"What this paper adds… interactive adaptation of Physics-Informed Neural Network loss function, powered by a Large Language Model, which makes it possible to formalize the expert knowledge into the PINN optimization objective via expert’s interactions with the LLM using natural language"*

Novelty for Q1 framing: LLM-mediated *surface* on a PINN loss is new; the *interactive rewrite cycle with system-suggested safer structure* is not. Cite CPLA/CSA when claiming interaction, and reserve novelty for epidemiology + PINN + LLM. (Comparative inference)

---

## 8. Certainty / entropy as cousins of compliance subjectivity

Paper B surfaces uncertainty in the rule family (certainty \(c\), entropy \(H\), unknown rules). Paper A’s primary success metric remains subjective visual compliance.

> **Quote (Hadjimichael & Wasilewska):** *"the certainty of a rule is defined as: \(c = \max(P(E_j \mid A_i), 1 - P(E_j \mid A_i))\)"*

> **Quote (Gindullina et al.):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the \"Compliance with the comment\" criterion."*

A CSA-like template proposer can refuse merges that would raise a PINN-side “entropy” proxy (e.g., epidemic-logic violations, MAE>1100) and flag them as Paper A’s “ambiguous”—instead of training first and labeling after. (Speculative extension)

---

## 9. Compaction evidence vs 25–27% PoC

Paper B reports measurable structure compaction from the interactive cycle; Paper A reports feasibility under a subjective primary metric. Both are early systems—but only Paper B shows that *system-suggested* structure improves the artifact relative to raw user structure.

> **Quote (Hadjimichael & Wasilewska):** *"Preliminary results have shown decreases in the number of rules ranging up to 43% using real experimental data."*

> **Quote (Gindullina et al.):** *"The key result is confirmation of the fundamental feasibility of integrating expert knowledge through LLM into PINN, with a success rate of 25-27% for the best models (Figure 5)."*

> **Quote (Hadjimichael & Wasilewska):** *"The user plays an integral part in the cycle by supplying conditions, as well as selecting from the suggested conditions, to adjust the data so as to maximize information content of the rules, while minimizing the uncertainty of the system."*

Transfer metric for templates: not only binary compliance, but reduction in unsafe/ambiguous edits and in unused-code rate when CSA-style subset selection is on. (Comparative inference)

---

## Direction 1. PINN Customizer as CSA: propose template instantiations, expert selects subset

**Pipeline stage:** PINN Customizer (replace free one-shot rewrite).  
**Mechanism:** For the confirmed class/subclass, enumerate a finite CSA-style candidate set (admissible ops × bounded numeric maps); LLM ranks/fills slots; expert selects subset before retrain; never auto-apply.  
**Failure modes addressed:** literal numeric insertion; compile-pass / intent-fail (Fig. 4b); unused dead code.  
**Precedent:** user moderates CSA feedback; CSA-conservative > user-coarse (Empirically shown). (Speculative extension)

---

## Direction 2. Over-generalization audit mirroring Example 5.3 vs 5.2

**Pipeline stage:** evaluation / Future work ablation.  
**Mechanism:** Same comments, two arms—(i) free LLM rewrite, (ii) CSA-style minimal templates—report compliance, epidemic-logic, and a diversity/entropy proxy of accepted edits.  
**Failure modes addressed:** claiming “more detailed rules” without testing whether loose user form still over-generalizes through the LLM.  
**Acceptance:** prefer the arm that cuts dangerous over-generalization without collapsing diversity to a single skeletal penalty. (Speculative extension)

---

## Manuscript placement

- **Future work templates + §2.3 Customizer:** CSA propose→select cycle as the interactive pattern for templates (clusters **8**, **9**).
- **Discussion of literal numeric insertion:** map to Paper B’s coarse user conditions vs conservative CSA.
- **Introduction (HITL):** historical precedent that expert-in-the-loop ≠ dumping free form into the objective.

## What not to transfer

Rough-set CPLA math, UCI grade examples, and 1993 UI chrome are not deliverables. No LLM in Paper B. Transfer **suggest-then-select over structural conditions** and the over-generalization caution—not inductive-rule learning as a replacement for PINN. (Comparative inference)

## Concrete next experiment

**Hypothesis.** CSA-style “propose 3 template instantiations → expert selects \(k\in\{1,2,3\}\)” beats auto-apply best LLM sample on unused-term rate and Zone A, at similar compile@1.

**Protocol.** For each comment: enumerate 3 admissible (op, term, range) fills; LLM ranks; expert selects subset; retrain only selected. Control: current one-shot auto-apply.

**Metric.** Unused-term %; literal-number insertion %; Zone A∪B; expert time. Expect select-subset lower unsafe edits. (Speculative extension)

## Related essays in this series

- [`03_tonda_2013_bnsl_interaction.md`](03_tonda_2013_bnsl_interaction.md) — Forced/Forbidden selection UX.
- [`01_hidalgo_2018_glucose_grammatical_evolution.md`](01_hidalgo_2018_glucose_grammatical_evolution.md) — grammar candidates.
- [`05_merhej_2015_asp_rules_of_thumb.md`](05_merhej_2015_asp_rules_of_thumb.md) — soft properties as CSA suggestions.
- Bridge: [`../dinara_analysis/15_ouyang_2022_instructgpt.md`](../dinara_analysis/15_ouyang_2022_instructgpt.md) — selected vs rejected as preference pairs.

## Conclusion

Paper B is a 1993 blueprint for what Paper A still lists as Future work: an interactive cycle where the *system suggests safer structural edits* and the *user selects*, rather than swallowing free-form expert magnitude into the objective. CPLA/CSA show that over-generalization is a human–system failure mode older than LLMs—and that conservative, syntax-derived suggestions beat coarse user conditions. Expert-Guided PINN should therefore implement modification templates as a CSA for loss ASTs: propose minimal admissible rewrites, require subset acceptance, and treat literal numeric insertion as the grades-example failure, not as an unavoidable LLM quirk.
