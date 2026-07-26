> **Paper B — live link:** [https://doi.org/10.1007/978-3-319-74718-7_55](https://doi.org/10.1007/978-3-319-74718-7_55)  
> **Source in `src/`:** [`../src/2018 Glucose Prognosis by Grammatical Evolution.md`](../src/2018%20Glucose%20Prognosis%20by%20Grammatical%20Evolution.md)

Gindullina et al. (hereafter **Paper A**) translate an epidemiologist’s free-text comment into a full rewrite of a SIRD PINN loss via Conversational Agent → hierarchical classifier (BERT+ML, accuracy 0.811) → PINN Customizer prompt → off-the-shelf LLM → compile check only → retrain. Primary success—“Compliance with the comment”—is only 25%/27%/6% (Llama-70B / DeepSeek / Llama-8B) at temperature 1.0 (~20 launches). Documented failures include literal numeric insertion, unused code, and a boundary-condition weight change that produced a 700+ day epidemic. Future work explicitly calls for class–subclass *modification templates* and an LLM-expert-evaluator / LLM-loss-semantic-checker, while admitting that compliance scoring is subjective and MAE gates (700 / 1100) are empirical.

Hidalgo, Colmenar, Kronberger, and Winkler (2018; hereafter **Paper B**) already operate a working structural DSL for expert domain knowledge: Grammatical Evolution (GE) grammars that constrain which glucose predictors may be expressed, evaluated with Clarke Error Grid Analysis (CEGA)—a clinical zone metric—rather than visual “does it look right?” judgment. Their directed grammar \(GE_{Dir}\) hard-codes “glucose + carbs − insulin”; the freer symbolic-regression grammar \(GE_{SR}\) does not. Empirically, premature domain knowledge in \(GE_{Dir}\) *reduced phenotypic diversity* and did not reliably reduce clinically dangerous zones relative to \(GE_{SR}\). On ten real DM1 patients and horizons 30–120 min, GE beat Last/Avg baselines; the authors’ own conclusion privileges grammar structure over “more domain knowledge is always better.”

Paper B therefore supplies what Paper A only plans: executable templates for expert structure, plus a domain-grounded scoring logic that can replace subjective compliance—and a cautionary ablation against over-constraining Table A.2–style rules when those rules become the sole skeleton of search. The transferable thesis is sharp: **treat planned modification templates as GE grammars, score with CEGA-like zones, and do not ship \(GE_{Dir}\)-style premature skeletons.**

---

## 1. Modification templates as grammars, not NL appendices

Paper A’s Appendix A rules are soft English instructions (“Add penalty to term2”) that the LLM may ignore while still compiling. Future work wants templates that hard-limit operators and numeric ranges. Paper B already implements that idea as production rules: the phenotype *must* be derived from the grammar.

> **Quote (Gindullina et al.):** *"we plan to replace the simple penalty additions by class-subclass-specific modification templates. These templates will explicitly define which loss components and parameters can be altered, which mathematical operators are admissible, and what numerical ranges are permitted."*

> **Quote (Hidalgo et al.):** *"given that the grammar is involved in the decodification, it is possible to introduce some information of the problem into the grammar to guide the optimization process to the best solutions."*

The comparative payoff is architectural: Paper A’s templates are still planned as prompt text; Paper B shows templates as a generative filter that forbids illegal phenotypes before evaluation. That is the difference between “tell the LLM what not to do” and “make illegal programs un-decodable.” (Comparative inference)

---

## 2. \(GE_{Dir}\) vs Table A.2: premature structure can hurt

Paper A’s Table A.2 already narrows edits (“Modification of other function components is **prohibited**”). Paper B’s directed grammar is the stronger analogue—and its authors report that hard-wiring domain knowledge was *not* always beneficial for avoiding dangerous predictions.

> **Quote (Hidalgo et al.):** *"This is an interesting result, since the inclusion of knowledge in the grammar, as \(GE_{Dir}\) does, is not beneficial for the quality of the prediction in this case. The reason is that, due to the structure of the grammar, the diversity of the solutions is lower with \(GE_{Dir}\) than with \(GE_{SR}\)."*

> **Quote (Gindullina et al.):** *"The current system of rules for modifying loss functions lacks sufficient detail to provide meaningful control over the generation process."*

Paper A’s failure modes (unused terms; BC weight edits that ignore intent) sit in the gap between “rules too loose for the LLM” and “rules too rigid for search.” \(GE_{Dir}\) warns that closing that gap by freezing the skeletal form can collapse the search space before a good phenotype appears. Shipping Table A.2 as a hard phenotype skeleton without a freer \(GE_{SR}\) control arm would ignore that warning. (Comparative inference)

---

## 3. Directed skeleton as the fixed starting point

Paper B makes the mechanism of diversity loss explicit: every individual begins from the same functional pattern.

> **Quote (Hidalgo et al.):** *"<func > ::= <exprgluc > + <exprch > - <exprins >"*

> **Quote (Hidalgo et al.):** *"the probability of having solutions with different phenotypes, i.e. different models, is lower with \(GE_{Dir}\) since the starting point is always the same."*

> **Quote (Gindullina et al.):** *"The current rule system (Appendix A), based on specifying the target components of the loss function for modification, is insufficient to ensure semantic transparency and explainability of the changes made."*

If Paper A’s planned templates harden into a single “always add penalty to term2” phenotype family per subclass, they recreate \(GE_{Dir}\)’s fixed start—exactly when Fig. 4b needed a different operator class (peak shift ≠ weaken terminal BC). (Comparative inference)

---

## 4. CEGA vs “Compliance with the comment”

Paper A’s primary criterion is a human visual match between comment and plot. Paper B scores forecasts with CEGA zones A–E: A+B clinically safe; C–E potentially dangerous—independent of author satisfaction. That difference matters because Paper A’s Future work still proposes an “LLM-expert-evaluator” without specifying *what objective signal* the evaluator should maximize.

> **Quote (Gindullina et al.):** *"The proposed approach to evaluating results has a significant subjective component, particularly in the \"Compliance with the comment\" criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results."*

> **Quote (Hidalgo et al.):** *"CEGA uses a Cartesian diagram divided into five zones (A to E). Zone A and B are predictions with no danger for the patient, while zones C to E are potentially dangerous."*

> **Quote (Hidalgo et al.):** *"Higher values of results in zones A and B are better, while lower numbers in zones C, D and E are preferred."*

CEGA does not solve “did we follow the comment?”, but it shows how a clinical domain can replace binary author judgment with zone-based risk—exactly the objectivity Paper A’s future LLM-expert-evaluator still lacks a design for. (Comparative inference)

---

## 5. Compile-only gates vs fitness that sees clinical harm

Paper A’s automatic loop stops at syntax; a 700-day outbreak still trains. Paper B’s fitness is RMSE, but *reporting* privileges CEGA dangerous zones—so a model that “works” numerically can still be rejected clinically. The contrast is the gap between “runs” and “safe to use.”

> **Quote (Gindullina et al.):** *"After generating the LLM candidate loss function, its automatic validation is performed (Figure 2), which includes: 1. Syntactic analysis – checking the code’s compilability using the Python interpreter."*

> **Quote (Gindullina et al.):** *"As a result, the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days)."*

> **Quote (Hidalgo et al.):** *"we can conclude that \(GE_{SR}\) reduces the number of predictions in dangerous zones."*

Empirically, at \(t{+}30\), zone D is 1.44 for \(GE_{SR}\) vs 2.27 for \(GE_{Dir}\) (Table 1). Transfer: Paper A’s MAE thresholds (700 / 1100) are magnitude gates, not harm zones. An epidemic Clarke-style grid (timing error × amplitude error × compartment logic) could fail closed on Fig. 4b-type disasters that currently pass compile. (Empirically shown) (Speculative extension)

---

## 6. Comparison table: structure, metrics, failure risk

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Expert structure encoding | Table A.2 NL rules + LLM rewrite of entire loss | BNF production rules decoding chromosomes to phenotypes | Templates as grammar > templates as prose (Comparative inference) |
| Constraint tightness | “Add penalty…” with prohibited components | \(GE_{Dir}\): fixed gluc+CH−ins skeleton; \(GE_{SR}\): freer ops + 38 engineered inputs | Hard skeleton can cut diversity (Empirically shown) |
| Primary success metric | Subjective “Compliance with the comment” 25–27% best | CEGA % in zones A–E on held-out folds | Clinical zones beat visual compliance (Comparative inference) |
| Automated stop condition | Compile / iterative fix on syntax errors | RMSE fitness + CEGA reporting | Syntax ≠ semantic / clinical validity (Author-stated) |
| Documented over-constraint risk | Rules “lack sufficient detail”; templates planned | Premature knowledge in \(GE_{Dir}\) not always beneficial | Over-tight Table A.2 clones risk \(GE_{Dir}\) failure (Comparative inference) |
| Numeric handling | Literal insertion of comment numbers into loss (esp. 70B) | Constants only via grammar-admissible `<cte>` forms | Map numbers to bounded operators, don’t paste (Comparative inference) |

---

## 7. Numeric cues: literals in loss vs constants in grammar

Paper A’s Llama-70B “literally include[s] these numerical parameters in the loss function without sufficient semantic adaptation.” Paper B also emits numeric constants, but only through grammar-admissible productions—not by pasting “7–10 days” into an arbitrary BC weight.

> **Quote (Gindullina et al.):** *"the meta-llama/Llama-3.3-70B-Instruct model exhibits a tendency to literally include these numerical parameters in the loss function without sufficient semantic adaptation."*

> **Quote (Hidalgo et al.):** *"<cte > ::= <base >*Math.pow(10,< sign ><exponent >)"*

A class–subclass template that *maps* “shift peak 7–10 days” to a bounded offset operator—rather than letting the LLM invent which weight to edit—is closer to GE’s constant productions than to free rewrite. (Comparative inference)

---

## 8. Diversity collapse and unused-code failures

Paper A records unused variables among systematic code errors. Paper B’s decoding analysis ties low diversity under \(GE_{Dir}\) to a fixed starting symbol.

> **Quote (Gindullina et al.):** *"We determined systematic errors in the generated code: • Adding unused variables and constant terms. • Erroneous assumptions about the presence of nonexistent patterns in the data. • Incorrect interpretation and use of numerical parameters mentioned in comments."*

> **Quote (Hidalgo et al.):** *"Those results indicate that a further exploration of the grammars is needed, in combination with a pre-processing of the data."*

If Paper A’s templates freeze one skeletal penalty pattern per subclass, the LLM may pad dead code inside the allowed region—\(GE_{Dir}\)’s diversity collapse in another medium. Templates need *admissible variety*, not a single canonical rewrite. (Comparative inference)

---

## 9. Ablation logic Paper A still lacks

Paper A varies LLM scale under one Customizer architecture and reports 25–27% best-case compliance. Paper B fixes the evolutionary engine and varies *grammar structure* on the same ten patients, four horizons, and CEGA reporting—so constraint design is attributable.

> **Quote (Hidalgo et al.):** *"In this paper we have tested two different kinds of grammars: a directed grammar… and a symbolic regression grammar."*

> **Quote (Gindullina et al.):** *"The key result is confirmation of the fundamental feasibility of integrating expert knowledge through LLM into PINN, with a success rate of 25-27% for the best models (Figure 5). These results should be considered proof-of-concept… highlighting the need to develop more stringent generation rules and control mechanisms."*

Before shipping class–subclass templates, Expert-Guided PINN needs a \(GE_{Dir}\) vs \(GE_{SR}\) analogue: same LLM, two template tightness levels, same comments—otherwise “more stringent rules” may silently recreate the directed-grammar failure. Paper B already evaluates via compilable phenotypes—illegal programs never reach fitness—whereas Paper A’s iterative fix only recovers syntax (≥80%) after free generation, leaving compliance at 25–27%. (Comparative inference)

> **Quote (Hidalgo et al.):** *"We have implemented the GE process in Java using the ABSys JECO library and compilable phenotypes to speed up the evaluation of individuals."*

> **Quote (Gindullina et al.):** *"A critical aspect of the developed framework is the implemented mechanism for iteratively correcting the generated code, which allowed us to increase the overall success rate to at least 80% for all tested models."*

---

## Direction 1. PINN Customizer: GE-style modification grammars with CEGA-like gates

**Pipeline stage:** PINN Customizer (replace free rewrite) + evaluation (replace subjective compliance).  
**Mechanism:** Encode each class/subclass as a BNF (or constrained-decoding) grammar over loss ASTs—admissible ops, terms, and numeric ranges—then sample/optimize phenotypes; score candidates with an epidemic Clarke-style grid plus compile+semantic checks before full retrain.  
**Failure modes addressed:** literal numeric insertion; unused dead code; compile-pass / intent-fail cases (700-day outbreak); subjectivity of “Compliance with the comment.”  
**Design caution from Paper B:** Prefer \(GE_{SR}\)-like templates that preserve phenotypic diversity over \(GE_{Dir}\)-like skeletons that bake in “glucose+carbs−insulin” equivalents of Table A.2. Run a same-LLM tightness ablation before productionizing. (Speculative extension)

---

## Direction 2. Evaluation: zone metrics feeding the LLM-expert-evaluator

**Pipeline stage:** evaluation loop (and Future work’s LLM-expert-evaluator).  
**Mechanism:** Replace binary author “compliance” with a fixed epidemic error-grid (zones for timing miss, amplitude miss, and logic violation), optionally as features an evaluator LLM must cite; keep MAE 700/1100 only as secondary magnitude filters.  
**Failure modes addressed:** subjective primary metric; ambiguous vs unsuccessful conflation; silent acceptance of plausible-looking but unsafe curves (Fig. 4b/c).  
**Measurable acceptance:** report % in safe vs dangerous zones per comment class, not only author binary success. (Speculative extension)

---

This pairing is highest-priority among the 2026-07 orphan set precisely because Paper B already *implemented* the two artifacts Paper A only names: structural templates and clinically grounded forecast scoring.

---

## Manuscript placement

- **Future work / §2.3 PINN Customizer:** cite as empirical precedent that *modification templates* should be generative grammars (cluster **9** DSL/constrained decoding), not longer English rows in Table A.2.
- **§2.4 Evaluation + Results:** cite CEGA as a zone-based alternative to subjective “Compliance with the comment” and arbitrary MAE 700/1100 (cluster **4** proper scoring).
- **Discussion of Fig. 4b/c:** use \(GE_{Dir}\) diversity collapse as caution when tightening rules (clusters **5**/pathology framing secondary).

## What not to transfer

Do not claim GE *is* a PINN+LLM system, or that glucose CGM protocols map 1:1 onto SIRD incidence. Paper B has no conversational agent, no hierarchical classifier, and no compilable PyTorch loss rewrite. Transfer the **grammar-as-DSL** and **clinical zone scoring** patterns only—not JECO chromosomes, Bateman carbs curves, or DM1 pump therapy details. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Same LLM (e.g. Llama-3.3-70B), same 20 comments: \(GE_{SR}\)-like freer modification grammar yields higher *safe-zone* rate than \(GE_{Dir}\)-like skeleton that freezes “add penalty to termK,” without lowering compile rate.

**BNF sketch (loss-edit phenotype):**
```text
<edit> ::= <op> <term> <weight>
<op>   ::= AddPenalty | Reweight | ShiftPeakBias
<term> ::= L_data | L_IC | L_ODE.S | L_ODE.I | L_ODE.R | L_ODE.D
<weight> ::= <float_in_range_for_subclass>
```
**Epidemic Clarke-style zones (example):** Zone A = peak time within ±3 days and post-peak slope sign matches comment; B = magnitude-only match; C–E = logic/non-negativity or >700-day pathology.

**Protocol.** Generate *k* grammar-legal phenotypes per comment → compile → short PINN continue-train → zone score; compare to single-shot Table A.2 baseline.

**Metric / expected signal.** Primary = % Zone A∪B (not author binary); secondary = compile@1, TSED, unused-term rate. Expect freer grammar ≥ directed skeleton on Zone A∪B; if directed wins only on compile, publish that tradeoff before claiming “more stringent rules.” (Speculative extension)

## Related essays in this series

- [`05_merhej_2015_asp_rules_of_thumb.md`](05_merhej_2015_asp_rules_of_thumb.md) — soft calibrated rules vs hard skeletons.
- [`02_steiner_2024_steering_wheel_crn.md`](02_steiner_2024_steering_wheel_crn.md) — protocolized HITL around typed operators.
- [`04_miller_2020_contrastive_explanation.md`](04_miller_2020_contrastive_explanation.md) — foil ⟨P,Q⟩ to fill zone labels.
- Bridge: [`../dinara_analysis/03_yu_2025_spec2rtl_agent.md`](../dinara_analysis/03_yu_2025_spec2rtl_agent.md) — progressive verify before target code (grammar as intermediate).

## Conclusion

Paper B is not about PINNs or LLMs; it is about *how* expert structure should enter a search over models. Grammatical Evolution already treats domain knowledge as a grammar—Paper A’s planned modification templates—and already evaluates forecasts with clinical zones rather than author impression. The \(GE_{Dir}\) result is the sharpest transferable lesson: premature hard constraints can reduce diversity and worsen dangerous outcomes. Expert-Guided PINN should therefore implement templates as searchable grammars with diversity-preserving freedom and CEGA-like harm metrics—not as tighter English rows in Table A.2 fed to a single-shot LLM rewrite. Until that grammar-vs-skeleton ablation exists, “more detailed rules” remain an untested bet.
