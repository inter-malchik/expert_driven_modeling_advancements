> **Paper B — live link:** [https://doi.org/10.1007/978-3-319-23540-0_23](https://doi.org/10.1007/978-3-319-23540-0_23)  
> **Source in `src/`:** [`../src/2015 A Possibilistic Analysis of Inconsistency.md`](../src/2015%20A%20Possibilistic%20Analysis%20of%20Inconsistency.md)

Gindullina et al. (hereafter **Paper A**) encode expert guidance as a stratified class/subclass rule table (Appendix A / Table A.2): permitted “add penalty…” edits with hard prohibitions on other loss components. When comments or rules conflict—or when successive edits pull the loss in incompatible directions—the pipeline has only crude options: accept the LLM rewrite if it compiles, or reject and retry. There is no principled salvage of the non-conflicting fragment of the rule KB.

Dubois & Prade (2015; hereafter **Paper B**) revisit possibilistic inconsistency: beyond discarding everything at or below global \(\mathrm{inc}(\Sigma)\), they use paraconsistent completion and **safely supported entailment**—keep a reason \(S\) only when \(\mathrm{Def}(S)>\mathrm{Uns}(S)\), equivalently delete, inside each minimal inconsistent subset, formulas whose weight equals that subset’s \(\mathrm{inc}(S)\). Thesis: **Paper A’s Appendix A rule KB and multi-comment sessions need Def>Uns salvage, not accept-all / discard-all, when expert rules or comments conflict.**

---

## 1. Global discard vs local salvage

Standard possibilistic practice throws away all formulas ≤ global inconsistency level—including innocents not in any conflict. Paper B’s point is that this is too destructive.

> **Quote (Dubois & Prade):** *"Then we can compute an inconsistency level for a propositional knowledge base, and all the formulas whose certainty is strictly above this inconsistency level form a consistent sub-base. The formulas whose certainty is equal to or smaller than the inconsistency level remain drown in inconsistency, including formulas that are not involved in any minimal inconsistent subsets."*

> **Quote (Dubois & Prade):** *"this entailment is more productive than the possibilistic logic entailment, but it nevertheless preserves the consistency of the set of consequences."*

> **Quote (Gindullina et al.):** *"The current system of rules for modifying loss functions lacks sufficient detail to provide meaningful control over the generation process."*

If two subclass rules or two successive expert comments conflict, treating the whole Table A.2 row-set as “inconsistent → ignore constraints” (LLM free rewrite) or “inconsistent → abort” mirrors global discard. Safely supported salvage keeps the free fragment. (Author-stated in B; Comparative inference for A)

---

## 2. Minimal inconsistent subsets as the conflict unit

Paper B ties attacks to local conflicts, not to a single scalar.

> **Quote (Dubois & Prade):** *"a minimal inconsistent subset of \(\Sigma\) is a minimal subset of propositions that entail \(\bot\)"*

> **Quote (Dubois & Prade):** *"the safely supported entailment from \(\Sigma\) coincides with the possibilistic entailment from the consistent possibilistic logic base \(\Sigma_{\mathrm{cons}}\) obtained from \(\Sigma\) by deleting, in all minimal inconsistent subsets \(S\) of \(\Sigma\), the formulas with a certainty level equal to \(\mathrm{inc}(S)\)."*

> **Quote (Gindullina et al.):** *"For the confirmed class and subclass combination, the corresponding loss function modification rules are extracted from the knowledge base. These rules, provided in Appendix A, represent strict guidelines for LLM"*

Map each Table A.2 constraint (and each accepted comment-as-rule) to a weighted formula. When class-4 “offset peak” conflicts with class-1 “add penalty to term2” under a shared integrity constraint (e.g., terminal BC must stay), identify MIS and drop only the weakest conflicting items—not every rule in Appendix A. (Comparative inference)

---

## 3. Def > Uns: free reasons, not adventurous ones

Paper B’s free-reason test is the operational criterion.

> **Quote (Dubois & Prade):** *"A reason is free iff \(\mathrm{Def}(S) > \mathrm{Uns}(S)\), i.e. iff its certainty is above the strength of the strongest attack."*

> **Quote (Dubois & Prade):** *"Then a proposition \(p\) is safely supported if it exists a reason \(S\) that is free for it. It can be shown that the set of safely supported consequences of a base \(\Sigma\) is always consistent."*

> **Quote (Gindullina et al.):** *"Modification of other function components is **prohibited**."* (Table A.2, repeated per class)

Prohibitions in Table A.2 are currently absolute. Under Def>Uns, a soft prohibition attacked by a stronger integrity constraint (non-negativity, monotonic cumulative, asymptotic BC) can be locally demoted without discarding the entire subclass permission set. (Author-stated in B; Comparative inference)

---

## 4. Accept-all vs discard-all vs \(\Sigma_{\mathrm{cons}}\)

Paper A’s runtime behavior under conflict is effectively binary: compile-and-show, or iterative fix on syntax only—no semantic conflict resolution among rules.

> **Quote (Gindullina et al.):** *"After generating the LLM candidate loss function, its automatic validation is performed… 1. Syntactic analysis – checking the code’s compilability"*

> **Quote (Gindullina et al.):** *"As a result, the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days). This example illustrates that, in the absence of clear and interpretable modification rules, an LLM may generate a loss function whose use leads to inadequate forecasts."*

> **Quote (Dubois & Prade):** *"Considering minimal inconsistent subsets provides a local view of where the conflicts take place, and then the deletion of the less certain formulas inside these subsets enables us to restore consistency while keeping more information than with the standard possibilistic logic view."*

Fig. 4b is accept-all on a compilable but semantically conflicting edit (peak-shift intent vs weakened terminal BC). \(\Sigma_{\mathrm{cons}}\)-style filtering would drop the weaker conflicting modification before retrain. (Empirically shown in A; Author-stated remedy in B) (Comparative inference)

---

## 5. Argumentative inference is too adventurous for PINN gates

Paper B contrasts safely supported inference with argumentative inference, which can yield jointly inconsistent conclusions.

> **Quote (Dubois & Prade):** *"This departs from the so-called argumentative inference… which is more adventurous than the safely supported inference, since it may lead to an inconsistent set of conclusions"*

> **Quote (Dubois & Prade):** *"For instance, consider the base \(\Sigma=\{r,\neg r\vee p,\neg r,r\vee q\}\). Then, we can infer both \(p\) and \(q\) argumentatively… from which one can infer neither that \(p\) nor \(q\) is safely supported."*

> **Quote (Gindullina et al.):** *"3. Compliance with the epidemic logic… Non-negativity… Monotonicity of cumulative values… Asymptotic behavior"*

Paper A’s epidemic-logic criterion is a hard integrity layer—closer to safe support than to adventurous “there exists a reason.” Multi-agent Future work must not let an LLM-evaluator assert both “peak shifted” and “terminal BC weakened to free growth” as jointly OK. (Comparative inference)

---

## 6. Comparison table: conflict handling for Appendix A

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Expert KB form | Table A.2 NL permissions/prohibitions | Weighted possibilistic formulas \((p_i,a_i)\) | Stratify A.2 rows with certainty weights (Comparative inference) |
| Conflict unit | Implicit (compile fail / bad plot) | Minimal inconsistent subsets | Localize which rules fight (Author-stated in B) |
| Default salvage | Accept compilable rewrite or abort/retry | \(\Sigma_{\mathrm{cons}}\): drop weight \(=\mathrm{inc}(S)\) in each MIS | Keep Def>Uns fragment (Author-stated in B) |
| Consistency of consequences | Epidemic-logic check post hoc | Safely supported set always consistent | Prefer safe support over adventurous multi-comment accept (Author-stated in B) |
| Multi-comment sessions | Sequential overwrite of loss | Paraconsistent completion + free reasons | Salvage non-attacked prior rules (Comparative inference) |
| Fig. 4b pathology | Peak-shift → weaken BC → 700-day outbreak | Accept-all across conflicting intents | Would fail Def>Uns vs asymptotic integrity (Comparative inference) |

---

## 7. Weighting Table A.2 and integrity constraints

Paper B assumes a linear certainty scale; Paper A’s constraints are unweighted prose.

> **Quote (Dubois & Prade):** *"Let \(\Sigma=\{(p_i,a_i)\mid i=1,\cdots,m\}\), where \(a_i\) is the strength with which \(p_i\) is believed to be true in \(\Sigma\). The higher \(a_i\), the higher the strength."*

> **Quote (Gindullina et al.):** *"we plan to replace the simple penalty additions by class-subclass-specific modification templates. These templates will explicitly define which loss components and parameters can be altered, which mathematical operators are admissible, and what numerical ranges are permitted."*

Assign templates/integrity constraints graded weights: epidemic-logic invariants > subclass permissions > soft shape preferences. Then \(\mathrm{inc}(S)\) deletion preferentially drops soft preferences, not non-negativity. (Speculative extension)

---

## 8. Paraconsistent completion as a conflict dashboard

Paper B’s \(\Sigma_{\mathrm{para}}\) makes attacks visible as \((p_i,\pi_i,\gamma_i)\).

> **Quote (Dubois & Prade):** *"\(\Sigma_{\mathrm{para}}=\{(p_i,\pi_i,\gamma_i)\mid (p_i,a_i)\in\Sigma,\;\pi_i\) is the greatest weight of a reason for \(p_i\)… \(\gamma_i\) is the greatest weight of a reason for \(\neg p_i\)…"*

> **Quote (Gindullina et al.):** *"A promising direction is to evolve the system toward a multi-agent architecture… An LLM-loss-semantic-checker could verify alignment between the generated code and modification rules"*

A semantic-checker should emit \(\Sigma_{\mathrm{para}}\)-style triples for active rules vs generated edits: high \(\gamma\) on “terminal BC strength” after a peak-shift comment is an explicit attack signal—before retrain, not after a 700-day plot. (Speculative extension)

---

## 9. Multi-comment sessions as incremental \(\Sigma\) growth

Paper A’s navigation pathway allows repeated comment → retrain cycles; each accepted edit adds constraints to the active loss without a conflict ledger.

> **Quote (Gindullina et al.):** *"The loop is closed by presenting the refined forecast to the expert, enabling continuous model alignment with domain knowledge."*

> **Quote (Gindullina et al.):** *"Receive and assess the updated forecast."* (Fig. A.7 pathway)

> **Quote (Dubois & Prade):** *"This short paper is intended to show that the benefit of taking into account the certainty levels of formulas when reasoning under inconsistency may be still much higher than the one already obtained by applying standard possibilistic logic where only formulas strictly above the inconsistency level of the knowledge base are salvaged."*

After comment \(n\), treat prior accepted warrants as weighted formulas still in \(\Sigma\). A new comment that attacks an earlier free rule should trigger local MIS repair—not silent overwrite of the whole loss and not a full reset of Appendix A. That is the incremental reading of safely supported salvage. (Comparative inference)

---

## Direction 1. Appendix A as a weighted possibilistic KB with \(\Sigma_{\mathrm{cons}}\) filtering

**Pipeline stage:** PINN Customizer rule loading (pre-LLM and post-LLM).  
**Mechanism:** Encode Table A.2 permissions, prohibitions, and epidemic-logic invariants as \((p,a)\); on multi-rule / multi-comment conflict, compute MIS, form \(\Sigma_{\mathrm{cons}}\) by deleting weight \(=\mathrm{inc}(S)\) items, prompt the LLM only with the safely supported fragment.  
**Failure modes addressed:** accept-all conflicting edits (Fig. 4b); discard-all that throws away free subclass rules; silent rule contradiction across sequential comments.  
**Measurable acceptance:** fraction of free rules retained; zero safely supported \(\bot\); fewer logic-violating retrains. (Speculative extension)

---

## Direction 2. Def>Uns gate inside the LLM-loss-semantic-checker

**Pipeline stage:** Future work semantic-checker.  
**Mechanism:** For each candidate loss edit, treat “edit implements subclass warrant” and “edit preserves integrity constraints” as competing reasons; accept only if Def>Uns for the warrant reason against integrity attacks—or demote the warrant and request regeneration.  
**Failure modes addressed:** adventurous joint acceptance of incompatible intents; compile-pass / intent-fail disasters. (Speculative extension)

---

Paper B is narrow but surgically relevant: when Expert-Guided PINN’s rule KB becomes inconsistent, the rational move is neither to trust every compilable rewrite nor to flush Appendix A—it is to keep the safely supported fragment.

---

## Manuscript placement

- **Appendix A rule KB + multi-comment UI:** \(\Sigma_{\mathrm{cons}}\) salvage (clusters **9**, **7**).
- **Future work semantic-checker:** Def>Uns gate before retrain.
- **Discussion:** accept-all vs discard-all as false dichotomy.

## What not to transfer

Possibilistic logic calculus need not be user-facing. Transfer **local MIS repair / keep free formulas**—not a full SUM-style reasoner in production. (Comparative inference)

## Concrete next experiment

**Hypothesis.** When two sequential comments conflict, \(\Sigma_{\mathrm{cons}}\) prompting retains more free subclass rules and fewer logic violations than accept-all concatenation or full reset.

**Salvage sketch:** weight Table A.2 + accepted warrants; on conflict compute MIS; delete weight \(=\mathrm{inc}(S)\) items; prompt LLM with remaining fragment only.

**Metric.** Free-rule retention; Criterion-3 fails; unused-term rate vs accept-all / discard-all arms. (Speculative extension)

## Related essays in this series

- [`13_potyka_2015_priority_probabilistic_kb.md`](13_potyka_2015_priority_probabilistic_kb.md) — priorities vs salvage.
- [`05_merhej_2015_asp_rules_of_thumb.md`](05_merhej_2015_asp_rules_of_thumb.md) — soft properties under conflict.
- [`08_arioua_2015_explanatory_dialogues.md`](08_arioua_2015_explanatory_dialogues.md) — \(CS_E\) commitments.
- Bridge: [`../dinara_analysis/11_gruber_ontolingua_portable_ontology.md`](../dinara_analysis/11_gruber_ontolingua_portable_ontology.md) — shared ontology for weighted rules.


## Conclusion

Dubois & Prade show that inconsistency under weighted formulas should be repaired locally: delete only the weakest members of each minimal inconsistent subset, and entail via Def>Uns free reasons. Expert-Guided PINN’s Appendix A and multi-comment loops currently behave like accept-all (if it compiles) or discard-all (abort/retry), which either produces Fig. 4b-type disasters or throws away still-free constraints. Weight Table A.2, compute \(\Sigma_{\mathrm{cons}}\), and let the semantic-checker enforce safely supported entailment before retrain.

