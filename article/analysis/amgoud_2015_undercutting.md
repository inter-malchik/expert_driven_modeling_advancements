> **Paper B — live link:** [https://doi.org/10.1007/978-3-319-23540-0_18](https://doi.org/10.1007/978-3-319-23540-0_18)  
> **Source in `src/`:** [`../src/2015 Undercutting in Argumentation Systems.md`](../src/2015%20Undercutting%20in%20Argumentation%20Systems.md)

Gindullina et al. (hereafter **Paper A**) ship Appendix A / Table A.2 as soft English “add penalty…” guidelines that the LLM may ignore while still compiling. Documented failure modes include unused constants, literal numeric insertion, and a Fig. 4b case where a peak-shift comment weakened a terminal boundary condition and produced a 700+ day outbreak. When a new expert comment conflicts with an earlier rule or with epidemic-logic integrity constraints, the pipeline has no named operation for *blocking a defeasible modification rule*—only accept-if-compiles, retry, or subjective “Compliance with the comment” (25%/27%/6%).

Amgoud and Nouioua (2015; hereafter **Paper B**) show that **undercutting alone**—blocking the application of a named defeasible rule when an exception or a conflicting conclusion follows—can capture every conflict that other systems split across undercut + rebuttal, while still satisfying rationality postulates under naive, stable, and preferred semantics. The transferable thesis is sharp: **treat Table A.2 subclass edits as named defeasible rules \(r_i\), and treat conflicting comments / integrity facts as undercuts that mark \(r_i\) blocked—not as silent unused terms or full KB discard.**

---

## 1. Named defeasible rules vs anonymous prompt text

Paper B’s language forces every defeasible rule to have a name in \(L^\#\), and allows strict rules whose heads *are* those names—explicitly encoding “this rule is inapplicable.”

> **Quote (Amgoud & Nouioua):** *"By default, any defeasible rule can be applied, unless explicitly mentioned in the language by strict rules \(x_1, \ldots, x_n \to x\) with \(x \in L^\#\). Such a rule is read as follows: If \(x_1, \ldots, x_n\) hold, then the defeasible rule \(x\) is always not applicable."*

> **Quote (Gindullina et al.):** *"For the confirmed class and subclass combination, the corresponding loss function modification rules are extracted from the knowledge base. These rules, provided in Appendix A, represent strict guidelines for LLM, defining which components of the original loss function can be modified (e.g., by adding a penalty term) and which are prohibited."*

Paper A’s “prohibited” lines are still prose inside a prompt. Paper B’s point is operational: a blocked rule is a first-class object that cannot fire in any accepted derivation. Mapping each Table A.2 row to a named \(r_{\mathrm{subclass}}\) is the missing precondition for undercut-as-gate. (Comparative inference)

---

## 2. Undercut as the single conflict relation

Paper B’s Definition 8 is deliberately minimal: argument \(a\) undercuts \(b\) iff the conclusion of \(a\) is the *name* of a defeasible rule used in \(b\).

> **Quote (Amgoud & Nouioua):** *"\((d, x)\) undercuts \((d^\#, x^\#)\), denoted by \((d, x)\, R_u\, (d^\#, x^\#)\), iff \(x \in Def(d^\#)\)."*

> **Quote (Amgoud & Nouioua):** *"any defeasible rule \(x \Rightarrow y\) should be blocked when \(\neg y\) follows from the theory."*

> **Quote (Gindullina et al.):** *"Adding unused variables and constant terms."* (listed among observed LLM failure modes)

Expert-Guided PINN’s “unused penalty” pathology is undercut failure made invisible: the LLM may emit a term that corresponds to a blocked or superseded rule while still compiling. An undercut gate would require that if Criterion-3 epidemic logic (or a later comment) entails \(\neg Head(r_i)\), then \(r_i\) is marked blocked in the Customizer prompt and any emitted AST node keyed to \(r_i\) fails the semantic check. (Comparative inference)

---

## 3. Pollock’s red-light example ↔ Fig. 4b exception

Paper B’s running illustration is exactly the exception pattern Paper A needs for “do not touch terminal BC when the comment is about peak timing.”

> **Quote (Amgoud & Nouioua):** *"The object is red \((or)\) because it looks red \((lr\))."* … *"The rule \(lr \Rightarrow or\) is inapplicable since the object is illuminated by a red light."* … *"The argument \(b\) undercuts \(a\) and the conclusion \((or)\) of \(a\) is not drawn from the theory."*

> **Quote (Gindullina et al.):** *"the expert asked to shift the epidemic peak by 7–10 days… The LLM… responded… by reducing the influence of the zero boundary condition… outbreak duration (more than 700 days)."*

Fig. 4b is a red-light case: the subclass rule “add peak-offset / penalty on peak features” is defeasible; the integrity fact “terminal BC weight must stay” should undercut any derivation that names a BC-edit rule. Today that undercut is missing, so the LLM invents a different (illegal) rule and compiles. (Comparative inference)

---

## 4. Characterized outputs vs opaque compliance

Paper B’s second contribution is that extensions and plausible conclusions are *characterized*—not only postulate-checked.

> **Quote (Amgoud & Nouioua):** *"we present the first argumentation system that uses only undercutting and fully characterize both its extensions and its plausible conclusions under various acceptability semantics."*

> **Quote (Gindullina et al.):** *"Compliance with the comment… A comparative analysis is performed between the expert’s text commentary and the visualization of the modified forecast."* … *"the proposed approach to evaluating results has a significant subjective component."*

For Paper A, the analogue of \(Output(H)\) is the set of loss edits that survive undercut filtering under all preferred options of the current rule KB—not a visual glance. That does not replace Zone/MAE scoring, but it separates “rule blocked” from “forecast looked wrong.” (Comparative inference)

---

## Directions for Expert-Guided PINN

**Direction 1. Name every Table A.2 row.** Assign \(r_{c,s}\) identifiers; Customizer may only emit AST edits tagged with allowed names. (Speculative extension)

**Direction 2. Undercut-as-gate before retrain.** When a new comment or Criterion-3 check entails \(\neg Head(r)\), mark \(r\) blocked; refuse compile-pass AST nodes that still use \(r\). (Speculative extension)

**Direction 3. Log blocked rules in the Conversational Agent.** Surface “rule \(r_{\mathrm{peak}}\) blocked by terminal-BC integrity” instead of another concreteness lecture. (Speculative extension)

**Failure modes addressed:** unused/dead terms; silent BC edits under peak comments; accept-all concatenation of conflicting subclass rules. (Speculative extension)

---

## Manuscript placement

- **Appendix A / Future work templates:** name defeasible modification rules and undercut closures \(\neg Head(r)\to r\) (clusters **9**, **7**).
- **§2.3 Customizer + planned LLM-loss-semantic-checker:** undercut gate before retrain.
- **Discussion Fig. 4b:** frame as missing undercut on BC-edit rules, not only “insufficient rules.”

## What not to transfer

Do not ship ASPIC-style full argument graphs, preferred-extension solvers, or SUM proof appendices as epidemic products. Paper B has no LLM, no PINN, no forecast skill metric. Transfer **named defeasible edits + undercut-as-block**—not a claim that Expert-Guided PINN already has characterized \(Output(H)\). (Comparative inference)

## Concrete next experiment

**Hypothesis.** Undercut-as-gate on named Table A.2 rules reduces unused-term rate and Criterion-3 logic fails versus accept-all prompting, without lowering compile@1 below the paper’s post-repair ≥80% band.

**Protocol.** (i) Tag each Appendix A row as \(r_i\). (ii) On each comment, compute blocked set: integrity IC undercuts unauthorized BC/IC edits; a second comment that contradicts \(Head(r_i)\) undercuts \(r_i\). (iii) Prompt LLM only with unblocked rules; semantic-check rejects AST nodes keyed to blocked names. Arms: accept-all baseline vs undercut gate.

**Metric.** Unused-term rate; Criterion-3 fail rate; Zone-style / compliance rate vs Paper A’s 25–27% headline; count of explicit “blocked \(r_i\)” events. Expect unused-term and logic-fail ↓; compliance not worse. (Speculative extension)

## Related essays in this series

- [`15_dubois_2015_possibilistic_inconsistency.md`](15_dubois_2015_possibilistic_inconsistency.md) — salvage free fragment vs undercut block.
- [`05_merhej_2015_asp_rules_of_thumb.md`](05_merhej_2015_asp_rules_of_thumb.md) — soft properties under hard IC.
- [`13_potyka_2015_priority_probabilistic_kb.md`](13_potyka_2015_priority_probabilistic_kb.md) — priority layers vs single undercut relation.
- Bridge: [`../dinara_analysis/03_yu_2025_spec2rtl_agent.md`](../dinara_analysis/03_yu_2025_spec2rtl_agent.md) — structured intermediate before execute.

## Conclusion

Amgoud and Nouioua show that blocking named defeasible rules—undercutting—is powerful enough to handle both exceptions and inconsistency without a second attack relation, and that the resulting plausible conclusions can be characterized. Expert-Guided PINN still treats Appendix A rules as anonymous prompt text and treats conflicts as compile-or-reject drama plus subjective compliance. Until modification templates are *named* and conflicting comments/integrity facts can undercut them, unused terms and Fig. 4b-style illegal edits remain expected modes rather than prevented ones.
