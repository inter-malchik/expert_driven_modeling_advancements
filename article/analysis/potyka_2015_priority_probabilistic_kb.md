> **Paper B — live link:** [https://doi.org/10.1007/978-3-319-23540-0_9](https://doi.org/10.1007/978-3-319-23540-0_9)  
> **Source in `src/`:** [`../src/2015 Reasoning over Linear Probabilistic Knowledge Bases with Priorities.md`](../src/2015%20Reasoning%20over%20Linear%20Probabilistic%20Knowledge%20Bases%20with%20Priorities.md)

Gindullina et al. (hereafter **Paper A**) encode expert intent as flat English rules—“Add penalty to term2… Modification of other function components is **prohibited**”—then let an LLM rewrite the whole PINN loss. Hard epidemiological requirements (non-negativity, cumulative monotonicity, asymptotic SIRD behavior) sit in a separate post-hoc filter (criterion 3), while curve-shape wishes compete as soft penalties with no priority semantics. Competing comments across classes have no ordered resolution; Integrity of epi logic is checked *after* training, not enforced as a model class.

Potyka (2015; hereafter **Paper B**) defines **linear priority knowledge bases** \((KB_1,\ldots,KB_k,IC)\): each level consistent with integrity constraints \(IC\), but levels may conflict. **Strict priority models** successively \(\arg\min\) violation from highest priority down; **weighted priority models** minimize a stacked, monotonically weighted residual under \(P\in\operatorname{Mod}(IC)\). Euclidean examples with \(w(p)=10^{p-1}\) recover near-strict access-control probabilities (e.g., `grantAccess(alice,file1)` ≈ 0.693 vs strict 0.7).

The transferable thesis is sharp: **model hard epidemic logic as \(IC\), rank competing expert comments as priority layers \(KB_i\), and stop treating “add soft penalty” as if it had the same force as integrity—Paper A’s flat Table A.2 is the no-priority merge Paper B warns against.**

---

## 1. Flat soft norms vs priority layers

Paper A’s Appendix A gives one permitted modification per subclass, all as soft penalty additions. Paper B’s motivating claim is that merging without priorities fails when specific rules must overwrite general ones.

> **Quote (Potyka):** *"Instead of overwriting knowledge of low priority with knowledge of higher priority, we would merge the knowledge independently of the priority."*

> **Quote (Gindullina et al.):** *"For the confirmed class and subclass combination, the corresponding loss function modification rules are extracted from the knowledge base… defining which components of the original loss function can be modified (e.g., by adding a penalty term) and which are prohibited."*

> **Quote (Potyka):** *"A linear priority knowledge base over \(X\) is a tuple \((KB_1, \ldots, KB_k, IC)\), where \(KB_1, \ldots, KB_k, IC\) are linear probabilistic knowledge bases over \(X\)."*

Two expert comments—“sharper decline” and “shift peak 7–10 days”—currently both become undifferentiated penalties. Priority layers would order them. (Comparative inference)

---

## 2. Integrity constraints vs post-hoc epidemic logic

Paper A’s criterion 3 verifies SIRD logic after retrain. Paper B’s \(IC\) are *never* sacrificed: both strict and weighted models optimize only inside \(\operatorname{Mod}(IC)\).

> **Quote (Gindullina et al.):** *"Compliance with the epidemic logic. The criterion verifies whether the modified forecast satisfies the fundamental requirements of the subject area… Non-negativity of all model compartments… Monotonicity of cumulative values… Asymptotic behavior consistent with the underlying epidemiological model."*

> **Quote (Potyka):** *"In order to account for knowledge that has to be respected independently of the priority, we will also allow a set of integrity constraints that is guaranteed to be satisfied if it is consistent."*

> **Quote (Potyka):** *"\(\emptyset \neq WPMod(KB) \subseteq \operatorname{Mod}(IC)\)."* (Proposition 5)

Fig. 4b’s 700-day outbreak is exactly what hard \(IC\) on terminal infected≈0 / finite duration should have forbidden *inside* the feasible set—not merely marked unsuccessful after the fact. (Comparative inference)

---

## 3. Strict priority: highest comment wins

When an epidemiologist’s peak-shift comment (class 4) conflicts with a generic curve-shape penalty (class 1), Paper A has no overwrite semantics. Paper B’s strict models guarantee the top layer.

> **Quote (Potyka):** *"If \(KB\) is valid, then \(\emptyset \neq SPMod(KB) \subseteq \operatorname{Mod}(KB_k \cup IC)\)."* (Proposition 1, Upmost Consistency)

> **Quote (Potyka):** *"Note that the first query shows that the knowledge about executive managers in \(KB_4\) suppresses the knowledge about confidential files in \(KB_3\) as desired."*

> **Quote (Gindullina et al.):** *"the LLM… responded to this comment by reducing the influence of the zero boundary condition in the loss function… This example illustrates that, in the absence of clear and interpretable modification rules, an LLM may generate a loss function whose use leads to inadequate forecasts."*

Map: \(IC\) = epidemic logic; \(KB_k\) = confirmed expert comment for this turn; lower \(KB_i\) = default PINN data/ODE terms. Strict semantics would not let a BC-weight hack “satisfy” a peak-shift request by violating terminal logic. (Comparative inference)

---

## 4. Weighted priority: soft curve shape without killing low layers

Paper A’s Future work still plans “simple penalty additions” replaced by templates—but without saying how multiple soft wishes trade off. Paper B’s weighted models keep every layer alive under monotone weights.

> **Quote (Potyka):** *"Instead of considering the subsets successively based on their priorities, we consider them simultaneously but weigh them with respect to their priority."*

> **Quote (Potyka):** *"We let \(w(p)=10^{p-1}\) for \(1 \leq p \leq 5\). This yields… \(grantAccess(alice, file1)[0.693]\)… overall the results are very close to what one might expect…"*

> **Quote (Gindullina et al.):** *"we plan to replace the simple penalty additions by class-subclass-specific modification templates. These templates will explicitly define which loss components and parameters can be altered… and what numerical ranges are permitted."*

Templates specify *admissible* edits; weighted priority specifies *how hard* they pull relative to data-fit and ODE residuals. Without \(w(p)\), Table A.2 penalties remain unranked soft norms. (Comparative inference)

---

## 5. Validity per level vs synthetic classifier + confirm

Paper B requires each \(KB_i\cup IC\) consistent (**validity**). Paper A trains a hierarchical classifier on synthetic comments and asks the expert to confirm class/subclass—but never checks that the induced penalty set is consistent with epidemic \(IC\).

> **Quote (Potyka):** *"\((KB_1, \ldots, KB_k, IC)\) is called valid iff \(KB_i \cup IC\) is consistent for \(1 \leq i \leq k\)."*

> **Quote (Gindullina et al.):** *"After automatic classification, the expert confirms the correctness of the assigned class and subclass."*

> **Quote (Gindullina et al.):** *"The hierarchical classifier was trained and evaluated on synthetic data, which may not capture the full linguistic variability of real expert feedback."*

Confirming the label ≠ proving the penalty template is jointly satisfiable with non-negativity / BC integrity. A validity check before LLM codegen would catch Fig. 4b-type rule sets. (Comparative inference)

---

## 6. Generalized minimal violation vs compile-only gates

When levels conflict, Paper B still returns nonempty compact convex **generalized** models via \(\min\|A_{KB}P\|\). Paper A’s automatic loop stops at Python compilability.

> **Quote (Potyka):** *"\(\min_{P \in P_X} \|A_{KB}P\|\)… if \(KB\) is inconsistent, the minimal solutions minimally violate \(KB\)… called generalized models."*

> **Quote (Gindullina et al.):** *"After generating the LLM candidate loss function, its automatic validation is performed… 1. Syntactic analysis – checking the code’s compilability using the Python interpreter."*

Syntax-minimal is not constraint-minimal. A Potyka-style residual on epi \(IC\) + comment constraints would reject compilable losses that maximally violate integrity. (Comparative inference)

---

## 7. Low-priority defaults can vanish under strict semantics

Paper B warns that strict models may ignore lower layers entirely when the top optimum is a singleton—exactly the risk if Paper A elevates every confirmed comment to absolute overwrite of data/ODE terms.

> **Quote (Potyka):** *"Even though strict priority models have some nice properties, they cannot guarantee that subsets of low priority have any influence on the final outcome of \(SPMod(KB)\) unless they are consistent with or independent of the upper levels. In fact, in some extreme cases, \(SPMod^l(KB)\) might contain only a single distribution for some \(l>1\)."*

> **Quote (Potyka):** *"In such cases, weighted priority models can be more appropriate."*

> **Quote (Gindullina et al.):** *"Matching training data… A value greater than this threshold indicates a catastrophic loss of model adequacy during modification."*

Design choice for Expert-Guided PINN: use **strict** for \(IC\) + current comment vs soft shape wishes; use **weighted** when data-fit (\(KB_1\)) must retain pull under a strong peak-shift comment. (Comparative inference)

---

## 8. Multiple simultaneous comments need merging semantics

Paper A’s loop assumes one comment per turn. Institute practice will produce concurrent wishes (peak timing + sharper decline + measure effect). Paper B’s whole point is autonomous resolution when several rules apply.

> **Quote (Potyka):** *"The key problem is that if we ask for the probability that a user has access to a file, different rules may apply. How can our system decide, as autonomously as possible, which rules apply and which rules have to be excluded to avoid inconsistencies?"*

> **Quote (Gindullina et al.):** *"It is based on four basic classes, identified through an analysis of typical expert statements"*

Stacking class-1 and class-4 penalties without \(KB_i\) order recreates the “merge independently of priority” failure. (Comparative inference)

---

## 9. Comparison table

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Expert structure | Flat Table A.2 “add penalty / prohibited” | Ordered \((KB_1,\ldots,KB_k,IC)\) | Priorities > flat merge (Author-stated in B) |
| Hard requirements | Post-hoc criterion 3 (logic) | \(IC\) inside \(\operatorname{Mod}(IC)\) always | Lift epi logic into \(IC\) (Comparative inference) |
| Conflict resolution | None (LLM invents weights) | Strict overwrite or weighted stack | Comment layers need semantics (Comparative inference) |
| Soft curve wishes | Undifferentiated penalty terms | Lower \(KB_i\) or small \(w(i)\) | Soft ≠ integrity (Comparative inference) |
| Consistency notion | Compile + expert label confirm | Validity: each \(KB_i\cup IC\) consistent | Label OK ≠ constraint OK (Comparative inference) |
| Empirical illustration | 25–27% compliance; Fig. 4 failures | Access-control bounds; \(w=10^{p-1}\approx\) strict | Weights can approximate strict (Empirically shown in B) |
| Risk of ignore-defaults | Catastrophic MAE after strong edit | Strict may freeze lower layers | Prefer weighted when data-fit must survive (Comparative inference) |

---

## Direction 1. Split loss into \(IC\) + priority comment layers

**Pipeline stage:** PINN Customizer / Appendix A redesign.  
**Mechanism:** Encode non-negativity, cumulative monotonicity, and terminal BC as hard \(IC\) (feasible set or infinite penalty). Place the confirmed expert subclass in \(KB_k\); keep data/ODE residuals as lower \(KB_i\). Optimize strict or weighted (Euclidean) residuals instead of free LLM weight invention.  
**Failure modes addressed:** Fig. 4b BC sabotage; Fig. 4c uninterpretable 4× BC boost; flat soft-norm collisions.  
**Acceptance:** every accepted run logs which layer was active and \(\|A_{KB_i}P\|\). (Speculative extension)

---

## Direction 2. Validity gate before codegen

**Pipeline stage:** after class/subclass confirm, before LLM prompt.  
**Mechanism:** Prove or numerically test that the subclass template ∪ \(IC\) is valid in Potyka’s sense; if not, refuse or escalate to conversational repair—do not train.  
**Failure modes addressed:** synthetic-classifier overconfidence; compile-pass / logic-fail disasters. (Speculative extension)

---

## Direction 3. Default to \(w(p)=10^{p-1}\) for multi-comment turns

**Pipeline stage:** Conversational Agent / multi-comment UI.  
**Mechanism:** When the expert enters two comments in one session, assign confirmed subclasses to stacked \(KB_i\) with exponential weights (Paper B’s practical choice) rather than concatenating English rules into one prompt.  
**Failure modes addressed:** autonomous rule clash without priority (Author-stated problem in B). (Speculative extension)

---

---

## Manuscript placement

- **Appendix A / Future work templates:** add priority layers \(IC\) vs \(KB_i\) (clusters **9**, **7**).
- **§2.3 Customizer:** validity gate before codegen.
- **Discussion Fig. 4b/c:** unranked soft-norm collisions.

## What not to transfer

Access-control conditionals and Log4KR are not epidemic software. Transfer **integrity constraints outside soft bargain + ranked \(KB_i\)**—not probabilistic KB solvers as a drop-in for LLM. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Encoding epidemic-logic as hard \(IC\) and subclass comment as \(KB_k\) (data/ODE lower) reduces logic-violating compile-pass disasters vs flat Table A.2 soft English.

**Layer sketch:** \(IC\) = non-negativity, cumulative monotonicity; \(KB_1\) = class rules; \(KB_2\) = subclass ranges; soft Euclidean pull with \(w(p)=10^{p-1}\) for multi-comment turns.

**Protocol.** Same comments; refuse invalid \(KB\cup IC\); compare logic-fail rate and Zone A to baseline.

**Metric.** Criterion-3 fails; unauthorized BC/IC flips; compliance. Expect fewer logic fails. (Speculative extension)

## Related essays in this series

- [`05_merhej_2015_asp_rules_of_thumb.md`](05_merhej_2015_asp_rules_of_thumb.md) — soft properties under \(IC\).
- [`15_dubois_2015_possibilistic_inconsistency.md`](15_dubois_2015_possibilistic_inconsistency.md) — conflict salvage.
- [`01_hidalgo_2018_glucose_grammatical_evolution.md`](01_hidalgo_2018_glucose_grammatical_evolution.md) — grammar as feasible set.
- Bridge: [`../dinara_analysis/12_lin_frequentist_or_bayesian.md`](../dinara_analysis/12_lin_frequentist_or_bayesian.md) — priors vs penalties framing.


## Conclusion

Potyka shows that competing probabilistic rules need either strict overwrite or explicitly weighted pull—and that integrity constraints must sit outside the soft bargain. Expert-Guided PINN currently flattens every comment into soft penalty English and checks epidemic logic only after the fact. The sharp transfer is architectural: \(IC\) for hard epi laws, \(KB_i\) for ranked expert comments, generalized/priority models instead of compile-only LLM rewrites. Until Table A.2 grows priority semantics, “add penalty to term2” will keep losing to unranked soft conflict—and Fig. 4b-type catastrophes will keep compiling.

