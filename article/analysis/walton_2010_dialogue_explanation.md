> **Paper B — live link:** [https://doi.org/10.1007/s11229-010-9745-z](https://doi.org/10.1007/s11229-010-9745-z)  
> **Source in `src/`:** [`../src/2010 A dialogue system specification for explanation.md`](../src/2010%20A%20dialogue%20system%20specification%20for%20explanation.md)

Gindullina et al. (hereafter **Paper A**) ship a Conversational Agent that validates expert comments for concreteness, certainty, and objectivity, then closes the loop when the expert visually judges “Compliance with the comment” (primary success 25%/27%/6%). Component 1 of four is never evaluated as a dialogue; success of the whole pipeline collapses into a feels-right plot check that Limitations themselves call subjective.

Walton (2010/2011; hereafter **Paper B**) specifies **Explan**: opening / explanation / closing stages, speech acts with pre- and post-conditions, and a success criterion that is *not* “I understand.” Transfer of understanding is tested by a dialectical shift to examination dialogue (Scriven’s test: capacity to answer *new* questions). The transferable thesis is sharp: **Paper A’s Conversational Agent and post-edit acceptance currently implement CE’s rejected “feels-right” closure; Explan supplies the missing success test and repair-loop semantics for evaluating that unevaluated agent.**

---

## 1. Success is transfer of understanding, not assent

Paper B’s central definition of explanatory success directly contradicts Paper A’s primary criterion as operationalized.

> **Quote (Walton):** *"A successful explanation has been achieved when there has been a transfer of understanding from the party giving the explanation to the party asking for it."*

> **Quote (Gindullina et al.):** *"Compliance with the comment. This is the primary criterion for assessing the technical success of the modification system. A comparative analysis is performed between the expert’s text commentary and the visualization of the modified forecast. If the forecast has changed in accordance with the commentary, the result is considered successful."*

Matching a plot to a comment is closer to assent than to demonstrated understanding of *why* the loss changed. (Author-stated in both) (Comparative inference)

---

## 2. “I understand” is an insufficient closing rule

Paper B explicitly rejects the CE closure Paper A’s UI still approximates—expert says the curve looks right, loop ends.

> **Quote (Walton):** *"The problem with this criterion is that the explainee could be faking, or could simply be mistaken. Even though he says he now understands what he formerly did not, this may simply not be true."*

> **Quote (Walton):** *"The “feels-right” explanation is often associated with bias."*

> **Quote (Gindullina et al.):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the \"Compliance with the comment\" criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results."*

Paper A already *admits* the bias; Paper B names the philosophical diagnosis and the fix. (Author-stated alignment) (Comparative inference)

---

## 3. Scriven’s test → examination shift as evaluation protocol

Paper B’s operationalization of success is an embedded examination dialogue—exactly usable as an Agent ablation protocol.

> **Quote (Walton):** *"Based on this remark, we now formulate Scriven’s Test: the success of an explanation is judged by the explainee’s capacity to answer new questions, shown in an extension of the dialogue sequence where probing questions are put to the explainee."*

> **Quote (Walton):** *"The proposal made here is to use something called an examination dialogue. The examination dialogue is embedded into the original explanation type of dialogue to provide a continuation of it in which the explanation offered and accepted in the explanation is tested."*

> **Quote (Gindullina et al.):** *"1. Conversational Agent, which helps the user formulate a comment suitable for forecast modification."*

Evaluating component 1 should mean: after a “successful” rewrite, can the expert (or a held-out examiner LLM) answer *new* questions about which loss term changed and why—not merely restate the original comment. (Comparative inference)

---

## 4. Anomaly-driven opening vs. free-text comment intake

Explan opens when an anomaly is detected in a shared account; Paper A opens when an expert dislikes a forecast. The structures rhyme.

> **Quote (Walton):** *"The fourth requirement for the opening stage of an explanation dialogue is that the explainee has to detect an anomaly in the account, something that doesn’t fit in with the account."*

> **Quote (Gindullina et al.):** *"If the forecast is unsatisfactory, the expert enters a textual comment in the “Instructions for the model” field."*

> **Quote (Gindullina et al.):** *"The conversational agent’s functionality includes validating expert comments for compliance with the following criteria: concreteness (a single specific point), certainty (lack of vagueness), and objectivity (lack of emotional overtones)."*

Form filters (concreteness…) are not anomaly formalization. Explan’s opening stage would require the Agent to extract an explicit anomaly relative to the shared SIRD account (e.g., “peak too early relative to measures”) before classification. (Comparative inference)

---

## 5. Failure cycle and repair without conflating forecast skill

Paper B’s failure cycle {ask → attempt → exam fail → re-ask} is the right semantics for LLM rewrite failure—separate from whether the expert’s epidemiological advice was wise.

> **Quote (Walton):** *"This explanation improvement cycle shown in Fig. 1, {3, 4, 5, 10, 11, 3}, can go around several times, as the two parties move collaboratively to better and better explanations until enough success has been achieved so that transfer of understanding has taken place."*

> **Quote (Gindullina et al.):** *"It is crucial to note that the successful model modification via external input does not mean the quality or correctness of the expert’s suggestion itself, which may be suboptimal… This study, therefore, assesses the capability for instruction-following, not the impact of the comment on forecast accuracy."*

Paper A already separates instruction-following from advice quality; Explan separates *understanding transfer* from both. A failed examination after Fig. 4b should reopen explanation (regenerate loss / clarify anomaly), not inflate “unsuccessful result” as if it were only a PINN pathology. (Author-stated separation in A; Author-stated cycle in B) (Comparative inference)

---

## 6. Speech acts vs. today’s Agent moves

Paper B enumerates locutions Paper A’s Agent only partially implements.

> **Quote (Walton):** *"Explanation Request: The speech act ‘ExplanAnom$x$’ makes a request to the explainer to provide understanding concerning some anomaly $x$."*

> **Quote (Walton):** *"Explanation Attempt: a response to a previous explanation request made by the explainee that purports to convey understanding to the explainee."*

> **Quote (Gindullina et al.):** *"Based on the LLM response, the agent either approves the comment for further processing or initiates an iterative refinement process, providing the expert with appropriate instructions."*

Paper A has refinement of the *comment*, and an LLM *attempt* at a loss—but no symmetric examination moves where the system probes whether the expert understood the *modification*. Future multi-agent evaluator work should add those speech acts explicitly. (Comparative inference)

---

## 7. Comparison table: dialogue success criteria

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Dialogue goal | Comment → compilable loss → compliant plot | Transfer of understanding | Plot assent ≠ understanding (Comparative inference) |
| Closing test | Expert visual judgment | Examination / Scriven new questions | Peirastic exam > “I understand” (Author-stated in B) |
| Agent evaluation | None reported for component 1 | Spec + 14 substages to closure | Use Explan substages as Agent protocol (Comparative inference) |
| Opening trigger | Unsatisfactory forecast + form-valid NL | Anomaly in shared account | Formalize anomaly before classify (Comparative inference) |
| Failure handling | Successful / unsuccessful / ambiguous plots | Exam-fail → re-ask improvement cycle | Repair loop separate from forecast skill (Author-stated in both) |
| Subjectivity diagnosis | Limitations: compliance subjective | “Feels-right” bias (Trout) | Same disease; B names the cure (Comparative inference) |

---

## 8. Closure rules as acceptance criteria for Agent ablations

Paper B’s six closure rules give measurable stopping conditions Paper A can adopt when ablating the Conversational Agent.

> **Quote (Walton):** *"Closure Rule 3: If the explainer is not satisfied, there should be a shift to an examination dialogue in which the explainee’s understanding of the explanation is tested."*

> **Quote (Walton):** *"Closure Rule 6: The explanation dialogue terminates when either (a) there has been a transfer of understanding of the kind required or (b) it must be closed off for practical reasons."*

> **Quote (Gindullina et al.):** *"A promising direction is to evolve the system toward a multi-agent architecture, where specialized LLMs enhance autonomy and objectivity. An LLM-expert-evaluator could quantify forecast compliance with the original comment…"*

The LLM-expert-evaluator should not only score plot–comment match; it should run Closure Rule 3—probe understanding of the loss edit—before declaring success. Practical timeouts (Rule 6b) map cleanly onto Paper A’s compute-heavy retrain budget. (Speculative extension grounded in Author-stated Future work)

---

## 9. Peirastic vs. exetastic exams for institute deployment

Paper B distinguishes probing comprehension from critically attacking truth—useful when Smorodintsev experts later replace synthetic comments.

> **Quote (Walton):** *"Guthrie described the distinction between these two types of examination as a component of the Aristotelian method of dialectical discussion used for testing and investigating… In the peirastic type, the aim is merely get an account representing what the respondent is supposedly claiming… The exetastic type is more argumentative."*

> **Quote (Gindullina et al.):** *"Large-scale validation on authentic expert comments is planned for future work at the Smorodintsev Research Institute for Influenza."*

For Agent evaluation, peirastic exams ask whether the expert can reconstruct the loss edit; exetastic exams ask whether that edit is epidemiologically warranted. Paper A’s instruction-following study needs the former first; institute studies can add the latter without conflating them into one compliance bit. (Comparative inference)

---

## Direction 1. Evaluate the Conversational Agent with Scriven exams

**Pipeline stage:** Conversational Agent (component 1) + evaluation.  
**Mechanism:** After each “compliant” run, administer a short examination dialogue (new questions on which term changed, which operators were forbidden, what foil trajectory was avoided). Score Agent+pipeline by exam pass rate, not only author binary compliance.  
**Failure modes addressed:** unevaluated Agent; subjective primary metric; conflation of assent with understanding. (Speculative extension)

---

## Direction 2. Formalize comment intake as ExplanAnom

**Pipeline stage:** Conversational Agent opening.  
**Mechanism:** Require an explicit anomaly relative to the baseline PINN account before BERT classification; map subclasses to anomaly types (peak timing, post-peak slope, measures mismatch).  
**Failure modes addressed:** vague comments that pass form gates but under-specify foil; ambiguous Fig. 4c outcomes. (Speculative extension)

---

## Direction 3. Multi-agent evaluator as examination dialogue, not vibe judge

**Pipeline stage:** Future-work LLM-expert-evaluator.  
**Mechanism:** Implement Closure Rules 3–6: evaluator asks new questions about the modification; low exam scores trigger regeneration; practical timeouts map to retrain budget.  
**Failure modes addressed:** subjective primary metric; evaluator without a success test beyond plot similarity. (Speculative extension)

---

## Manuscript placement

- **§2.1 Conversational Agent (currently unevaluated):** Scriven exam as first Agent KPI (cluster **8**).
- **§2.4 + Future work LLM-evaluator:** examination dialogue, not plot vibe (cluster **3**).
- **Limitations:** separate instruction-following from understanding transfer.

## What not to transfer

Paper B is a dialogue-logic specification with no code, no PINNs, no epidemics. Do not require the full Explan speech-act inventory or Yale anomaly corpus as a blocker. Transfer **success = exam-tested understanding** and the peirastic/exetastic split—not philosophical machinery wholesale. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Agent+pipeline “success” under Scriven exams is substantially lower than author binary compliance on the same runs.

**Five probes (after a “compliant” forecast):**
1. Which loss term changed?
2. Which operators were forbidden by rules?
3. What foil trajectory was avoided?
4. Would weakening \(L_{IC}\) satisfy the comment? (expect No)
5. State one numeric range that was *not* taken literally from the comment.

**Protocol.** Blind rater scores pass/fail per probe; optional LLM-evaluator must answer before labeling success.

**Metric.** Exam pass rate vs binary compliance; κ. Expect exam ≪ 25–27%. (Speculative extension)

## Related essays in this series

- [`08_arioua_2015_explanatory_dialogues.md`](08_arioua_2015_explanatory_dialogues.md) — stores for logging exams.
- [`04_miller_2020_contrastive_explanation.md`](04_miller_2020_contrastive_explanation.md) — foil in probe 3.
- [`06_hayes_2017_policy_explanation.md`](06_hayes_2017_policy_explanation.md) — predicate answers.
- Bridge: [`../dinara_analysis/15_ouyang_2022_instructgpt.md`](../dinara_analysis/15_ouyang_2022_instructgpt.md) — preference labels from exam fail/pass.

## Conclusion

Walton’s Explan reframes Paper A’s unevaluated Conversational Agent from a comment-quality filter into a dialogue whose success is *demonstrated* transfer of understanding. The subjective “Compliance with the comment” criterion is the textbook “feels-right” closing rule Explan rejects; Scriven’s examination shift is the blueprint Future work’s LLM-expert-evaluator still lacks. Until Expert-Guided PINN can fail an examination after a pretty plot, component 1 remains a proof-of-concept gesture rather than a measured dialogue system.
