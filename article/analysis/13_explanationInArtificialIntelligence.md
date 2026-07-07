> **How to read this comparison**
>
> - **Paper A** denotes Gindullina et al. (Expert-Guided PINN); **Paper B** denotes the cited source paper.
> - Quoted passages are taken from the papers named in the comparison.
> - Interpretive links between papers are argued explicitly; they are not claims made by either author team.
> - Sections titled **Proposed direction** suggest possible follow-up work. They are engineering ideas, not reported results.


Paper A (Gindullina et al., 2026) builds Expert-Guided PINN: a dialogue in which an epidemiologist comments on a forecast, an LLM rewrites PINN loss code, and the expert judges the result. Paper B (Tim Miller, 2019, *Explanation in Artificial Intelligence: Insights from the Social Sciences*) surveys philosophy and psychology to argue that explainable AI must match **how people actually explain** — contrastively, socially, pragmatically — not engineer intuitions of “good explanations.”

Paper A is a strong **inverse XAI** case: the human explains to the machine. It aligns with Miller's contrastive and dialogical claims more closely than most post-hoc SHAP systems — but it under-implements Miller's foil elicitation, bidirectional intelligibility, and the social negotiation of what counts as fixed background.

---

## 1. Explanation as dialogue, not weight dumps

Miller's scope claim:

> **Quote (Miller):** *"Ultimately, it is a human–agent interaction problem. Human-agent interaction can be defined as the intersection of artificial intelligence, social science, and human–computer interaction (HCI)."*

Paper A's architecture is explicitly conversational:

> **Quote (Gindullina):** *"The conversational agent's functionality includes validating expert comments for compliance with the following criteria: concreteness (a single specific point), certainty (lack of vagueness), and objectivity (lack of emotional overtones)."*

The PINN Customizer then closes the loop with a new plot. This is Miller's “explanation as social transfer of knowledge” with roles flipped: explainee = PINN pipeline, explainer = epidemiologist. Miller warns experts should not run the asylum; Paper A keeps the epidemiologist as domain authority while the LLM handles code.

| Criterion | Paper A | Paper B (Miller) | Takeaway |
|:--- |:--- |:--- |:--- |
| Interaction mode | Chat + plot feedback | Dialogue, Gricean maxims | A implements social XAI inverted |
| Contrast structure | Expert vs. current forecast | Fact vs. foil (P vs. Q) | A's comments are implicit foils |
| Model transparency | Loss code hidden from expert | Avoid dumping full causal chains | A shields user from math |
| Evaluation | Pragmatic comment compliance | Probability ≠ explanatory quality | A de-emphasizes pure MAE |

---

## 2. Contrastive explanation: fact and foil on the epidemic plot

Miller's central claim:

> **Quote (Miller):** *"people do not ask why event P happened, but rather why event P happened instead of some event Q."*

> **Quote (Miller):** *"Lipton refers to the two cases, P and Q, as the fact and the foil respectively; the fact being the event that did occur, and the foil being the event that did not."*

Paper A's successful example is explicitly contrastive:

> **Quote (Gindullina):** *"the expert first obtained a forecast corresponding to the black dashed line and then entered the comment 'After the peak there should be a sharper decline in the number of cases.'... The plot shows that the number of cases after the peak indeed decreases faster than in the initial forecast."*

**P** = baseline forecast; **Q** = sharper post-peak decline. Table A.2 rules target the difference (penalties on `term2`), not full model rewrite — matching Miller's point that contrastive answers cite **differences**, not complete causal histories. Gap: Miller notes foils are often implicit and hard to infer; Paper A does not structuredly elicit Q (e.g., “decline over how many days?”) before codegen.

---

## 3. Gricean quantity, relation, manner in the Conversational Agent

Miller ties explanation to cooperative conversation (Section 5; citing Hilton, Grice).

Paper A operationalizes this in validation rules — concreteness (quantity/relation), certainty and objectivity (manner). The hierarchical classifier further restricts which loss components may change, enforcing **relation** between comment class and editable `term*`. When Llama-8B violates manner (vague mapping of “two more weeks growth” to boundary weights), the result is an ambiguous plateau — a pragmatic failure, not merely syntax.

---

## 4. Mechanistic versus statistical explanation

Miller (via Lombrozo and others): people prefer mechanisms over bare covariation.

Paper A anchors on SIRD ODE residuals in $L_{ODE}$:

> **Quote (Gindullina):** *"The defining characteristic of the PINN methodology is the optimization of a composite loss function that includes both the data-fitting error and the residual of the equations describing the modeled process."*

Expert comments adjust mechanistic penalties, not arbitrary weights on a black-box MLP. Miller would classify this as efficient/mechanistic explanation at the population level — but Paper A does not **explain back** which mechanism changed in expert-facing prose, only that the curve moved. Limitation aligns with Miller's “model of self” problem: the PINN's inner state remains opaque behind LLM code.

---

## 5. Pragmatic evaluation: epidemic logic and comment compliance

Miller: people judge explanations by pragmatic fit, not probability alone (Section 4.5.2 in Miller).

Paper A's four criteria include:

> **Quote (Gindullina):** *"Compliance with the epidemic logic"* and *"Compliance with the comment (main success criterion)"*

High epidemic-logic scores (90–100%) with low comment compliance (6–27%) mirror Miller's separation of **coherence with background beliefs** vs. **answering the actual contrastive question**. A forecast can respect ODE non-negativity yet fail the expert's foil — exactly when pragmatic explanation succeeds statistically but not socially.

---

## 6. Correctability without full explainability: asymmetry vs. Kulesza/Miller

Miller cites explanatory debugging tradition: explanations should enable correction.

Paper A implements **human → model** correction via loss edits but not **model → human** explanations of why a particular penalty was chosen. Miller would flag this as one-way intelligibility: the expert cannot see the “difference vector” between fact and foil in equation space. Future multi-agent evaluator could verbalize the contrastive mapping Miller demands.

---

## 7. Abnormality, controllability, temporality in the ontology

Miller (Section 4.4.2): explainers focus on abnormal, controllable, temporal factors.

Paper A's four comment classes map closely: curve behavior (abnormality), anti-epidemic measures (controllability), dynamics/numbers (temporality), peak position (temporal landmark). BERT+ML at ~81% accuracy subsumes free text into these explanation types before LLM action — a computational foil for “what kind of contrast is being requested?”.

---

## 7. Social expectations and the “inmates running the asylum” problem

Miller's warning:

> **Quote (Miller):** *"The very experts who understand decision-making models the best are not in the right position to judge the usefulness of explanations to lay users — a phenomenon that Miller et al. refer to (paraphrasing Cooper [31]) as 'the inmates running the asylum'."*

Paper A inverts the asylum: **domain experts** (epidemiologists) judge forecasts; **ML experts** built the LLM+PINN stack. The epidemiologist never sees loss code — avoiding engineer-designed explanations that violate Gricean quantity. Risk: without reverse explanation, ML-side errors (wrong `term` edited) are invisible to the very users Miller says must evaluate pragmatic fit. Split-responsibility classification confirmation is a partial social checkpoint — the expert validates **category**, not **mechanism**.

Miller also notes people anthropomorphize agents and expect human-like explanatory norms. Paper A's Conversational Agent mimics clinical interview style (concreteness, objectivity) — aligning social expectations before the PINN acts.

---

## Proposed direction 1. Explicit foil elicitation in Conversational Agent

**Pipeline stage:** Conversational Agent.

**Mechanism:** After expert comment, agent asks contrastive follow-up (“compared to current forecast, should peak day move earlier or later, by about how much?”) per Miller's foil requirement.

**Failure mode addressed:** Implicit foil misread (Fig. 4b/c).

---

## Proposed direction 2. Contrastive loss templates keyed to (P, Q) pairs (PINN Customizer)

**Pipeline stage:** PINN Customizer.

**Mechanism:** Generate penalties only on features that differ between baseline forecast and stated foil trajectory, not full term rewrites.

**Failure mode addressed:** Over-editing AST (TSED failures on small models).

---

## Proposed direction 3. Reverse explanation: natural-language summary of loss delta (evaluation display)

**Pipeline stage:** Post-codegen, pre-retrain.

**Mechanism:** LLM summarizes “I increased post-peak penalty on infected compartment” for expert approval — Miller's actionable intelligibility.

**Failure mode addressed:** Semantic opacity of generated loss.

---

## Proposed direction 4. Pragmatic success metric with inter-rater agreement (evaluation)

**Pipeline stage:** Evaluation protocol.

**Mechanism:** Multiple epidemiologists score comment compliance; report agreement — treating explanation quality as social, not private.

**Failure mode addressed:** Subjective compliance criterion.

---

## Conclusion

Paper A is among the few applied systems that treat **expert contrastive judgment** as the primary control signal for a physical model, which Miller's survey prescribes at the HCI layer. It does not yet complete the social contract Miller outlines: mutual intelligibility, explicit foils, and pragmatic explanation of the model's counter-move. Closing that gap — especially foil elicitation and reverse contrastive summaries — is the direct design agenda the two papers jointly imply.
