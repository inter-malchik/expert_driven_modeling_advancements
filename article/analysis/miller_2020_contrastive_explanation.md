> **Paper B — live link:** [https://arxiv.org/abs/1811.03163](https://arxiv.org/abs/1811.03163)  
> **Source in `src/`:** [`../src/2020 Contrastive Explanation A Structural-Model Approach.md`](../src/2020%20Contrastive%20Explanation%20A%20Structural-Model%20Approach.md)

Gindullina et al.'s work (hereafter **Paper A**) treats “Compliance with the comment” as the primary success metric for Expert-Guided PINN: after an LLM rewrites the SIRD-PINN loss, authors visually decide whether the new incidence curve matches the expert’s text. Best models reach only 25–27% (6% for Llama-3.1-8B). Limitations frankly call this criterion subjective and Future work proposes an “LLM-expert-evaluator” without specifying what proposition that evaluator should check.

Miller's *"Contrastive Explanation: A Structural-Model Approach"* (hereafter **Paper B**) supplies that missing semantics. Building on Halpern–Pearl structural causal models and Lipton’s Difference Condition, it defines answers to **“Why P rather than Q?”** (counterfactual foil) and **“Why P but Q?”** (bi-factual surrogate) via contrastive causes and CE1–4 / BE1–4 relative to an epistemic state \(K\). Thesis: Paper A’s primary metric is an underspecified *Why P?* judgment; Paper B shows that instruction-following for forecast edits is inherently **contrastive**, and that an objective evaluator must verify a Difference Condition between the requested fact \(P\) and an explicit foil \(Q\)—not a binary “looks compliant” score (Comparative inference).

---

## 1. People do not ask Why P — and neither should PINN evaluation

Paper B’s central empirical claim from social science, which it then formalizes:

> **Quote (Miller):** *"That is, people do not ask "Why P?"; they ask "Why P rather than Q?", although often Q is implicit from the context. Following Lipton [1990], we will refer to P as the fact and Q as the contrast case."*

Paper A’s primary criterion is exactly the non-contrastive form:

> **Quote (Gindullina et al.):** *"Compliance with the comment. This is the primary criterion for assessing the technical success of the modification system. A comparative analysis is performed between the expert's text commentary and the visualization of the modified forecast. If the forecast has changed in accordance with the commentary, the result is considered successful."*

> **Quote (Gindullina et al.):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the "Compliance with the comment" criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results."*

Without an explicit \(Q\) (slower decline vs. sharper; peak+7 days vs. peak+0; continued growth vs. plateau), raters cannot agree on what “in accordance” means (Author-stated gap in A; Author-stated contrastive thesis in B) (Comparative inference).

---

## 2. Difference Condition as the content of “compliance”

Lipton’s Difference Condition, which Paper B adopts as the selection principle for contrastive answers:

> **Quote (Miller):** *"To explain why P rather than Q, we must cite a causal difference between P and not-Q, consisting of a cause of P and the absence of a corresponding event in the history of not-Q. — Lipton [1990, p. 256]."*

> **Quote (Miller):** *"To define contrastive cause, we adopt and formalise Lipton's Difference Condition [Lipton, 1990], which states that we should find causes that are different in the 'history' of the two events."*

Mapped to Paper A: success is not “any edit that moves the curve,” but that the post-edit trajectory realizes \(P\) for reasons that differentiate it from foil \(Q\)—e.g., stronger post-peak penalty on \(I(t)\) rather than weakened \(I(T_{\max})\to 0\). The 700-day outbreak after a peak-shift comment fails the Difference Condition: the causal difference cited by the LLM (boundary weight) is not the difference that separates “peak later” from “peak now” (Empirically shown failure in A Fig. 4b; Comparative inference).

---

## 3. Counterfactual vs. bi-factual: two evaluation questions Paper A conflates

Paper B distinguishes two explananda Paper A’s single plot-check mixes:

> **Quote (Miller):** *"An counterfactual question is of the form "Why P rather than Q?", and asks why some fact P occurred instead of some hypothetical foil Q. A bi-factual question is of the form "Why P but Q?", and asks why some fact P occurred in the current situation while some surrogate Q occurred in some other factual situation."*

For Expert-Guided PINN:

- **Counterfactual compliance:** Why does the *modified* forecast show sharper post-peak decline (\(P\)) rather than the *initial* PINN trajectory (\(Q\))?
- **Bi-factual compliance:** Why does run \(i\) satisfy the comment while run \(j\) (same comment, temperature=1.0) does not?

Paper A reports 20 launches at \(T=1.0\) and aggregates bars in Fig. 5, but never scores pairs of trajectories under an explicit \(\langle P, Q \rangle\) (Empirically shown setup in A; Author-stated typology in B) (Comparative inference).

---

## 4. CE1–4 as a blueprint for the LLM-expert-evaluator

Paper A’s Future work:

> **Quote (Gindullina et al.):** *"An LLM-expert-evaluator could quantify forecast compliance with the original comment; low confidence scores could trigger automatic loss regeneration or comment refinement."*

Paper B’s Definition 4 states what a contrastive counterfactual explanation *is*, relative to epistemic state \(K\):

> **Quote (Miller):** *"CE1 \((M, \vec{u}) \models \varphi \wedge \neg \psi\) for each \(\vec{u} \in K\) — that is, the agent accepts that \(\varphi\) and that \(\neg\psi\)."*

> **Quote (Miller):** *"CE2 \(\langle \vec{X} = \vec{x}, \vec{X} = \vec{y} \rangle\) is a sufficient counterfactual cause for \(\langle \varphi, \psi \rangle\), for each \(\vec{u} \in K\) such that \((M, \vec{u}) \models \vec{X} = \vec{x}\)."*

> **Quote (Miller):** *"CE3 \(\vec{X}\) is minimal — no subset of \(\vec{X}\) satisfies CE2."*

> **Quote (Miller):** *"CE4 ... that is, agent is initially uncertain whether the explanation is true or not, meaning the explanation provides meaningful information."*

Operational transplant: the evaluator must (i) extract \(\varphi=P\) and foil \(\psi=Q\) from the comment + initial forecast, (ii) check that the modified curve satisfies \(P \wedge \neg Q\), (iii) cite a minimal contrastive cause in loss-space (which template/term changed), and (iv) abstain when \(K\) already entails the difference—CE4’s “no new information” case, which Paper A currently cannot express (Author-stated Future work in A; Author-stated CE1–4 in B) (Speculative extension).

---

## 5. Secondary MAE gates are not contrastive causes

Paper A’s gates (MAE>700 “forecast changed”; MAE<1100 “still fits data”; epidemic-logic checks) are useful filters but do not encode \(\langle P, Q \rangle\):

> **Quote (Gindullina et al.):** *"Due to the lack of standardized numerical metrics for assessing the semantic correspondence of a forecast to an expert's textual commentary, a system of qualitative validation criteria was developed."*

A forecast can change a lot (pass gate 2), stay non-negative (pass gate 3), and still answer the wrong contrast—as in Fig. 4c, where continued growth was requested but a flat plateau appeared after quadrupling the terminal boundary weight (Empirically shown in A). Paper B’s lesson: quantity of change ≠ difference relative to the foil (Comparative inference).

---

## 6. Why-not systems that ignore the Difference Condition

Paper B warns that much of XAI answers why-not without contrast:

> **Quote (Miller):** *"First, while there many of papers what answer why-not questions, most of these are counterfactual solutions, not contrastive, meaning that they to not make explicit use of the difference between the fact and the foil, with some exceptions..."*

Paper A’s LLM-as-codegen path is in that trap: it produces *some* counterfactual loss world, then asks humans whether the plot “matches.” Without forcing the Difference Condition into the evaluator prompt or metric, the multi-agent Future work risks another non-contrastive judge (Comparative inference).

---

## 7. Comparative summary

| Criterion | Paper A (Gindullina et al.) | Paper B (Miller) | Takeaway |
| :--- | :--- | :--- | :--- |
| Primary question | “Does the plot match the comment?” | “Why \(P\) rather than \(Q\)?” | A needs explicit foils (Comparative inference) |
| Selection principle | Author visual judgment | Difference Condition (Lipton via Miller) | Cite causal difference, not any cause (Author-stated in B) |
| Evaluator agent | Named in Future work | CE1–4 / BE1–4 relative to \(K\) | Formal job description for LLM-expert-evaluator (Comparative inference) |
| Abstention | No “no explanation” outcome | CE4 when \(K\) already determines the cause | Allow evaluator to refuse scoring (Author-stated in B) |
| Headline score | Compliance 25–27% / 6% | Theoretical (illustrative examples) | Replace subjective % with contrastive adequacy rate (Speculative extension) |
| Failure example | Peak-shift → 700-day outbreak | Bee vs Fly: shared features are non-contrastive | Shared SIRD terms ≠ answer to the comment (Comparative inference) |

---

## Direction 1. Comment → \(\langle P, Q \rangle\) at Conversational Agent

**Pipeline stage:** Conversational Agent (before classifier).

**Mechanism:** Require every approved comment to state fact and foil (“sharper post-peak decline rather than the current slow decline”); store \(Q\) as the initial forecast features when implicit.

**Failure mode:** Subjective compliance without inter-rater foil agreement (Author-stated limitation in A).

(Speculative extension — question form Author-stated in B.)

---

## Direction 2. Contrastive adequacy as primary metric

**Pipeline stage:** Evaluation (replace primary criterion 4).

**Mechanism:** Score 1 iff modified trajectory satisfies \(P \wedge \neg Q\) on predefined observables (peak day, post-peak slope, two-week growth), else 0; report separately from MAE gates.

**Failure mode:** 25–27% visual compliance that cannot be audited (Empirically shown in A).

(Speculative extension)

---

## Direction 3. LLM-expert-evaluator implements CE1–4

**Pipeline stage:** Future-work multi-agent layer.

**Mechanism:** Evaluator outputs a contrastive pair \(\langle \vec{X}=\vec{x}, \vec{X}=\vec{y} \rangle\) in template/loss vocabulary; regenerate if CE2 fails; return “no explanation” when CE4 fails (already known).

**Failure mode:** Judge that scores plot similarity without Difference Condition (Comparative inference from B’s XAI critique).

(Speculative extension — CE formalization Author-stated in B; role Author-stated in A.)

---

## Direction 4. Bi-factual audit across temperature=1.0 replicates

**Pipeline stage:** Evaluation protocol.

**Mechanism:** For each comment, treat successful vs. unsuccessful runs as bi-factual \(\langle P, Q \rangle\) and demand that the evaluator cite loss-edit differences (BE-style), not only aggregate Fig. 5 bars.

**Failure mode:** Hidden instability under \(T=1.0\) masked by mean compliance (Empirically shown setup in A).

(Speculative extension)

---

## Manuscript placement

- **§2.4 Evaluation Approach + Limitations (subjective compliance):** redefine primary success as contrastive adequacy (cluster **3** LLM-as-judge + **4** scoring).
- **Future work (LLM-expert-evaluator):** implement CE1–4 as the judge’s contract, with meta-validation vs humans (cluster **3**).
- **Results Fig. 4:** re-annotate success/fail/ambiguous as ⟨P,Q⟩ foils.

## What not to transfer

Paper B is a formal XAI/philosophy paper with arthropod/planning illustrations—no epidemiology, no PINNs, no LLMs. Do not require full Halpern–Pearl SCMs of the city epidemic before shipping a judge. Transfer the **contrastive question form** and **Difference Condition**—not the entire causal-model ontology. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Scoring the same 20 runs with CE1–4 (explicit foil) yields lower inter-rater disagreement and a different model ranking than author binary “Compliance with the comment.”

**Fig. 4-style foil example.** Comment: “outbreak lasts two more weeks.”  
- \(P\): peak delayed ≈14 days, duration extended.  
- \(Q_{\text{fail}}\): BC weight ×4 → 700+ day epidemic (wrong difference).  
Difference Condition must cite *duration/peak timing*, not arbitrary \(L_{IC}\) weight.

**CE1–4 rubric (evaluator checklist):** CE1 factivity of \(P\); CE2 contrastive cause present in loss edit; CE3 minimality; CE4 “no explanation” if expert already knows the cause. Blind 2 raters + optional LLM-judge; report κ and joint success.

**Metric.** κ(binary) vs κ(contrastive); correlation of judge with human CE pass. Expect binary inflated vs CE. (Speculative extension)

## Related essays in this series

- [`01_hidalgo_2018_glucose_grammatical_evolution.md`](01_hidalgo_2018_glucose_grammatical_evolution.md) — zones as coarse foils.
- [`07_walton_2010_dialogue_explanation.md`](07_walton_2010_dialogue_explanation.md) — exam after contrastive claim.
- [`12_mehdi_2015_compositional_forecasting.md`](12_mehdi_2015_compositional_forecasting.md) — quantitative foil features.
- Bridge: [`../dinara_analysis/13_explanationInArtificialIntelligence.md`](../dinara_analysis/13_explanationInArtificialIntelligence.md) — social-science explanation roots.

## Conclusion

Miller’s contrastive structural-model account turns Paper A’s acknowledged weakness—the subjective primary metric—into a design specification: compliance is contrastive adequacy under an explicit foil, selected by the Difference Condition, and checkable with CE1–4. Expert-Guided PINN already generates the two worlds (initial vs. modified forecast) that bi-factual and counterfactual questions need; it does not yet *score* their difference. The LLM-expert-evaluator named in Future work should not be another vibe-check on plots—it should be a contrastive judge.
