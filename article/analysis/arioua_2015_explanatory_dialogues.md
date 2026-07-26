> **Paper B — live link:** [https://doi.org/10.1007/978-3-319-23540-0_19](https://doi.org/10.1007/978-3-319-23540-0_19)  
> **Source in `src/`:** [`../src/2015 Formalizing Explanatory Dialogues.md`](../src/2015%20Formalizing%20Explanatory%20Dialogues.md)

Gindullina et al. (hereafter **Paper A**) list four components—Conversational Agent, hierarchical classifier, PINN Customizer, LLM—yet report metrics only for classifier accuracy (0.811) and post-rewrite forecast criteria (compliance 25%/27%/6%). Component 1 has no dialogue metrics; Future work gestures at multi-agent evaluators without store-level success conditions.

Arioua and Croitoru (2015; hereafter **Paper B**) formalize Walton’s CE as **ECE** in Prakken’s framework: liberal protocol R1–R7, commitment store \(CS_E\), non-understanding store \(NUS_X\), success when \(NUS_X=\emptyset\), plus termination \(O(k^{D(\varphi)})\) and store space \(O(|\Sigma|)\). The transferable thesis is sharp: **empty \(NUS_X\) operationalizes Walton’s “transfer of understanding” into an ablation metric Paper A can attach to the Conversational Agent and to nested questions about opaque loss edits—without waiting for another subjective plot vote.**

---

## 1. Empty \(NUS_X\) as measurable dialogue success

Paper B converts the philosophical success criterion into a store invariant.

> **Quote (Arioua & Croitoru):** *"A successful explanatory dialogue is a dialogue where the explainee’s understanding store is empty. Certainly, we cannot be sure whether the understanding has really taken place but it is one way to quantify the success and failure of an explanatory dialogue."*

> **Quote (Gindullina et al.):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the \"Compliance with the comment\" criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results."*

For Expert-Guided PINN, treat each unexplained claim about the *modification* (which term changed, which operator applied, which foil was avoided) as an element of \(NUS_X\); dialogue success = store cleared—not “author liked the green curve.” (Author-stated in both) (Comparative inference)

---

## 2. Effect rules: explain adds, positive removes

Paper B’s effect rules give the update semantics a Conversational Agent ablation needs.

> **Quote (Arioua & Croitoru):** *"If \(\operatorname{sp}(m)=\operatorname{explain}(\varphi)\) then \(NUS_X=NUS_X \cup \{\varphi\}\),"*

> **Quote (Arioua & Croitoru):** *"If \(\operatorname{sp}(m)=\operatorname{positive}(\varphi)\) then \(NUS_X=NUS_X \setminus \{\varphi\}\)."*

> **Quote (Gindullina et al.):** *"1. Conversational Agent, which helps the user formulate a comment suitable for forecast modification."*

Today the Agent adds/removes nothing measurable—it only approves or rewrites comments. Instrumenting it with \(NUS_X\) turns “iterative refinement” into logged store transitions that can be compared across Agent variants. (Comparative inference)

---

## 3. Nested negative feedback vs. one-shot comment

ECE allows the explainee to reject a *part* of an explanans and request a nested explanation—Paper A’s loop is one comment → one loss → one plot judgment.

> **Quote (Arioua & Croitoru):** *"\(\operatorname{negative}(\rho,\varphi)\): \(X\) doesn’t understand \(\rho\) in the explanation of \(\varphi\)"*

> **Quote (Arioua & Croitoru):** *"we allow for nested explanation requests and feedback when the explainee cannot understand something in the explanation."*

> **Quote (Gindullina et al.):** *"Upon completion of the training process, the system visualizes the resulting forecast, calculates metrics, and presents it to an expert for comparative analysis… At this stage, the expert evaluates the relevance of the modified forecast to the original comment and decides whether to retain it or re-modify it."*

Fig. 4b/c failures often need nested “I don’t understand why the *boundary weight* changed given a *peak-shift* comment”—exactly \(\operatorname{negative}(\rho,\varphi)\) over loss fragments, not a full restart. (Empirically motivated by A; Author-stated nesting in B) (Comparative inference)

---

## 4. \(CS_E\) against circular and inconsistent loss stories

Paper B’s commitment store and R7 block circular explanans; Paper A’s LLM freely invents edits that conflict with stated rules.

> **Quote (Arioua & Croitoru):** *"Avoid circular explanations. This means that it is forbidden to explain \(\psi\) by \(\{\varphi\}\) such that \(\varphi\) is asked to be explained…"*

> **Quote (Arioua & Croitoru):** *"R7: If \(\operatorname{sp}(m)=\operatorname{attempt}(\Gamma,\varphi)\) then there is no \(\psi \in \Gamma\) such that \(\psi \in NUS_X\)."*

> **Quote (Gindullina et al.):** *"An LLM-loss-semantic-checker could verify alignment between the generated code and modification rules, reducing hallucinations."*

Implement the semantic-checker as \(CS_E\) + R7 over Appendix A commitments: if the LLM’s attempt cites a component still marked non-understood or prohibited, the move is illegal—before retrain. (Comparative inference)

---

## 5. Termination bounds as Agent stress-test design

Paper B proves finite termination under finite explanatory models—useful when deciding how deep nested loss-explanation can go before timeout.

> **Quote (Arioua & Croitoru):** *"Proposition 1 (Termination). If the conditions in Lemmas 1 and 2 hold for every explanandum \(\varphi\) then any legal explanatory dialogue \(d\) will terminate in finite steps."*

> **Quote (Arioua & Croitoru):** *"Then every legal explanatory dialogue \(d\) with topic \(\varphi\) will terminate at most in \(O(k^{D(\varphi)})\) steps."*

> **Quote (Gindullina et al.):** *"A critical aspect of the developed framework is the implemented mechanism for iteratively correcting the generated code, which allowed us to increase the overall success rate to at least 80% for all tested models. However, it should be noted that this mechanism requires additional queries to the LLMs, which significantly increases computational costs and time…"*

Paper A already feels query-cost pressure on syntax repair; ECE’s depth bound \(D(\varphi)\) is the right knob for capping nested *semantic* explanation before another full PINN retrain. (Empirically shown cost in A; Formally shown bound in B) (Comparative inference)

---

## 6. Comparison table: stores as ablation metrics

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Dialogue success | Subjective compliance 25–27% | \(NUS_X=\emptyset\) | Store emptiness > plot assent (Comparative inference) |
| Agent metrics | None for component 1 | Store size, steps to empty, negatives count | Ablation-ready KPIs (Comparative inference) |
| Feedback grain | Accept / reject whole forecast | Nested \(\operatorname{negative}(\rho,\varphi)\) | Partial loss-fragment probes (Author-stated in B) |
| Consistency guard | Compile check; planned semantic-checker | \(CS_E\) + R7 no circular attempts | Checker = commitment legality (Comparative inference) |
| Complexity | Extra LLM calls for syntax fix | Worst-case \(O(k^{D(\varphi)})\) steps; \(O(|\Sigma|)\) space | Bound nested explanation depth (Formally shown in B) |
| Walton link | Unevaluated Agent; Future multi-agent | Operationalizes CE with stores + shifts | ECE is the metric layer on Explan (Author-stated in B) |

---

## 7. ARG shift: challenge explanans before trusting the plot

Paper B’s ECE→ARG shift lets the explainee argue over a piece of the explanation—analogous to challenging an LLM’s claimed loss rationale before accepting compliance.

> **Quote (Arioua & Croitoru):** *"as an example we describe a shift to argumentative dialogue with the goal of giving the explainee the possibility to challenge explainer’s explanations."*

> **Quote (Arioua & Croitoru):** *"If the explainer wins then we update \(NUS_X\) according to Definition 5, else \(NUS_X\) persists as it was."*

> **Quote (Gindullina et al.):** *"An LLM-expert-evaluator could quantify forecast compliance with the original comment; low confidence scores could trigger automatic loss regeneration or comment refinement."*

Low-confidence compliance should shift to ARG over the disputed explanans (e.g., “BC weight ×4 explains continued growth”), updating \(NUS_X\) only if the explainer side wins—not if the curve merely moved. (Comparative inference)

---

## 8. Protocol liberalism vs. Paper A’s linear navigation

Paper A’s Fig. A.7 pathway is strictly linear (review → confirm class → assess forecast). ECE’s liberal protocol permits backtracking—necessary when experts discover mid-dialogue that the wrong subclass was confirmed.

> **Quote (Arioua & Croitoru):** *"we generalize the sequential protocol of [19,20] and introduce a more flexible protocol (liberal protocol) where the explainee and the explainer can backtrack to early stages in the dialogue."*

> **Quote (Gindullina et al.):** *"After automatic classification, the expert confirms the correctness of the assigned class and subclass. This validation step is critical to minimizing errors due to natural language ambiguity."*

A single early mis-confirm currently poisons the entire LLM prompt. Liberal backtrack to re-open classification after a nested \(\operatorname{negative}\) is an Agent feature ECE already justifies. (Comparative inference)

---

## 9. Abstract explanatory model as template for loss-edit explanations

Paper B keeps the explanatory relation abstract (\(E_i\)) so domain knowledge can plug in—exactly how Paper A should treat class/subclass modification templates as the explainer’s \(E_E\).

> **Quote (Arioua & Croitoru):** *"Due to the controversy around explanatory models, in this formalization we just consider an abstract setting where the model \(E_i\) can provide an explanation for an arbitrary explanandum."*

> **Quote (Gindullina et al.):** *"we plan to replace the simple penalty additions by class-subclass-specific modification templates. These templates will explicitly define which loss components and parameters can be altered, which mathematical operators are admissible, and what numerical ranges are permitted."*

Once templates exist, each admissible rewrite is an \(\operatorname{attempt}(\Gamma,\varphi)\); nested questions about \(\rho \in \Gamma\) are ECE moves, not ad hoc chat. That ties Future-work templates to Agent evaluation instead of treating them as unrelated upgrades. (Comparative inference)

---

## Direction 1. Instrument the Conversational Agent with \(NUS_X\) / \(CS_E\)

**Pipeline stage:** Conversational Agent + evaluation (component 1 ablation).  
**Mechanism:** Log every explain/positive/negative move; primary Agent KPIs = steps-to-empty-\(NUS_X\), number of nested negatives, final \(|NUS_X|\), illegal R7 attempts blocked. Compare Agent variants on these, independent of forecast MAE.  
**Failure modes addressed:** unevaluated Agent; subjective compliance as sole success. (Speculative extension)

---

## Direction 2. Semantic-checker as R7 over Appendix A commitments

**Pipeline stage:** LLM-loss-semantic-checker (Future work).  
**Mechanism:** Maintain \(CS_E\) from Table A.2 permissions; reject attempts that explain using still-nonunderstood or prohibited components; on ARG-win over a disputed fragment, remove it from \(NUS_X\) and allow retrain.  
**Failure modes addressed:** hallucinations; circular rationales; compile-pass / intent-fail. (Speculative extension)

---

## Direction 3. Cap nested explanation depth before retrain

**Pipeline stage:** PINN Customizer loop.  
**Mechanism:** Set max explanatory depth \(D\) from Proposition 2’s spirit; if \(NUS_X\) nonempty at cap, regenerate loss or escalate to human—avoid unbounded LLM Q&A before another 5000-epoch train.  
**Failure modes addressed:** query-cost blowup already seen in syntax repair. (Speculative extension)

---

## Manuscript placement

- **§2.1 Agent evaluation:** instrument \(NUS_X\)/\(CS_E\) logs as Agent KPIs (cluster **8**).
- **Future work multi-agent + semantic-checker:** R7 over Appendix A commitments (clusters **2**, **3**).
- **§2.3 Customizer:** depth cap before another long retrain.

## What not to transfer

ECE coal/black examples and Prakken framework formalism need not ship in production epidemiology code. Transfer **empty-\(NUS_X\) success**, **commitment store**, and **nested negative** as *logging contracts*—not a full dialectical agent rewrite. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Agent variants ranked by steps-to-empty-\(NUS_X\) diverge from rankings by author compliance.

**Instrumentation.** On each turn log: explain/positive/negative moves; \(NUS_X\) claims about loss fragments; \(CS_E\) Appendix A permissions; nested depth; R7 blocks.

**Depth cap.** If \(NUS_X\) nonempty after \(D=3\) nested explains, regenerate loss or escalate—no retrain.

**Metric.** Mean steps-to-empty-\(NUS_X\); % sessions empty at end; correlation with binary compliance (expect weak). (Speculative extension)

## Related essays in this series

- [`07_walton_2010_dialogue_explanation.md`](07_walton_2010_dialogue_explanation.md) — Scriven ideal ECE measures.
- [`06_hayes_2017_policy_explanation.md`](06_hayes_2017_policy_explanation.md) — predicate content of \(NUS_X\).
- [`15_dubois_2015_possibilistic_inconsistency.md`](15_dubois_2015_possibilistic_inconsistency.md) — conflicting commitments.
- Bridge: [`../dinara_analysis/03_yu_2025_spec2rtl_agent.md`](../dinara_analysis/03_yu_2025_spec2rtl_agent.md) — reflection branches when \(NUS_X\) stuck.

## Conclusion

Arioua and Croitoru turn Walton’s transfer-of-understanding ideal into stores and protocol rules a software team can log. For Expert-Guided PINN, that is the missing instrumentation of the Conversational Agent: success when \(NUS_X\) empties over claims about the *loss edit*, consistency via \(CS_E\)/R7, and nested negatives when only a fragment of the LLM’s rationale fails. Until those metrics exist, “multi-agent evaluator” Future work remains unmeasurable prose beside a 25–27% subjective bar.
