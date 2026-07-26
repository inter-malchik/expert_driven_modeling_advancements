> **Paper B — live link:** [https://doi.org/10.1007/978-3-319-23540-0_25](https://doi.org/10.1007/978-3-319-23540-0_25)  
> **Source in `src/`:** [`../src/2015 Using Rules of Thumb for Repairing Inconsistent Answer Set Programs.md`](../src/2015%20Using%20Rules%20of%20Thumb%20for%20Repairing%20Inconsistent%20Answer%20Set%20Programs.md)

Gindullina et al.'s work (hereafter **Paper A**) constrains LLM edits to a PINN loss with a coarse class/subclass rule table (Appendix A / Table A.2: mostly “add penalty to term\(k\); other components prohibited”), then accepts any compilable rewrite that authors visually judge compliant (25–27% best / 6% for 8B). Future work promises class-subclass **modification templates** with admissible operators and numeric ranges, but offers no calibration design for those ranges.

Merhej, Schockaert & De Cock's *"Using Rules of Thumb for Repairing Inconsistent Answer Set Programs"* (hereafter **Paper B**) studies the dual problem—repair a scientific model that conflicts with observations—on gene regulatory networks encoded in ASP. The baseline minimizes edit cost; the proposed method adds **expert soft rules of thumb** (seven literature properties) as penalties. Empirically, rules-of-thumb repairs beat minimal repairs on F1 and Jaccard across five networks × seven corruption setups × ten runs; correct repairs are *rarely* minimal; rule *ranges* are learned leave-one-network-out while weights stay hand-uniform. Thesis: Paper A’s compile-passing, minimally guided penalty edits are the ASP “minimal repair” baseline Merhej shows is inferior; leave-one-out range calibration of soft expert rules is the missing blueprint for the modification templates Paper A already names (Comparative inference).

---

## 1. Minimal repair is a reasonable default — and often wrong

Paper B states the methodological trap Paper A still lives in:

> **Quote (Merhej et al.):** *"Although several approaches to this end have already been proposed, most of them merely find a repair which is in some sense minimal. In many applications, however, expert knowledge is available which could allow us to identify better repairs."*

> **Quote (Merhej et al.):** *"First, there is no reason why the correct repair has to be minimal; as we will see in Sect. 5, in the case of GRNs the correct repair is actually rarely minimal."*

Paper A’s pipeline optimizes for *syntactic* minimality of disruption only indirectly (TSED similarity, compile success) and for *instruction-looking* plots, not for epidemiologically plausible structure of the edit:

> **Quote (Gindullina et al.):** *"After generating the LLM candidate loss function, its automatic validation is performed... Syntactic analysis – checking the code's compilability using the Python interpreter."*

> **Quote (Gindullina et al.):** *"The key result is confirmation of the fundamental feasibility of integrating expert knowledge through LLM into PINN, with a success rate of 25-27% for the best models... highlighting the need to develop more stringent generation rules and control mechanisms."*

A compilable, small TSED edit that yields a 700-day outbreak is precisely a “minimal” change that is not a *plausible* repair (Empirically shown in A Fig. 4b; Empirically shown anti-minimal thesis in B) (Comparative inference).

---

## 2. Expert soft constraints beat the minimal baseline

Paper B’s headline experimental claim:

> **Quote (Merhej et al.):** *"We notice a consistent improvement in both metrics with the addition of rules of thumb. Instead of only minimizing the number of applied repair operations, the addition of rules of thumb also focuses on preserving the biggest number of properties that were found in similar GRNs."*

> **Quote (Merhej et al.):** *"Our experiments have shown that our method of repairing by using rules of thumb leads to a better performance in terms of F1 score and Jaccard measure. This leads to more plausible repairs than when simply selecting the minimal one, with only very limited access to training data."*

Paper A has no analogue of F1/Jaccard against a held-out “correct” loss structure—only subjective compliance. The comparative implication is directional: adding soft expert structure should raise plausible-edit rates above the current 25–27% ceiling if templates encode properties, not only “add penalty” permissions (Empirically shown in B; Comparative inference for A).

---

## 3. Hand-weighted rules parallel Table A.2

Paper B is candid that weights were not learned:

> **Quote (Merhej et al.):** *"Note that we cannot realistically expect any training data to be available to learn weights (e.g. reflecting the importance of each principle), making our approach quite different from e.g. approaches for repairing using soft constraints in Markov logic... Therefore, we instead set the weights in a uniform manner, i.e. they are chosen such that each principle roughly has the same impact on the choice of repair. In other words, our approach is only based on a direct encoding of available expert knowledge."*

Paper A’s Table A.2 is the same epistemic object—hand-authored, coarse, equally “strict” prohibitions—without even soft penalties for violating epidemiological side properties:

> **Quote (Gindullina et al.):** *"The current system of rules for modifying loss functions lacks sufficient detail to provide meaningful control over the generation process."*

> **Quote (Gindullina et al.):** *"A significant limitation is the lack of mechanisms to control the interpretability of the generated loss functions. The current rule system (Appendix A), based on specifying the target components of the loss function for modification, is insufficient to ensure semantic transparency and explainability of the changes made."*

Both papers encode expert knowledge as hand-set soft/hard preferences; only Paper B then *measures* whether that encoding improves repair quality against ground truth (Comparative inference).

---

## 4. Leave-one-out calibration of ranges: blueprint for templates

The transferable methodology is not the biology—it is how ranges are set:

> **Quote (Merhej et al.):** *"Every time we select a network to corrupt and repair, we learn the relevant parameters of the rules of thumb from the other four, uncorrupted networks. For Property 2, we learn the degrees \(k_{min}\) and \(k_{max}\) from the other four networks... The range \([\mathrm{diameter}_{min}, \mathrm{diameter}_{max}]\) in Property 5 is learned similarly..."*

Paper A’s Future work asks for exactly such numeric bounds, without a protocol:

> **Quote (Gindullina et al.):** *"We plan to replace the simple penalty additions by class-subclass-specific modification templates. These templates will explicitly define which loss components and parameters can be altered, which mathematical operators are admissible, and what numerical ranges are permitted... Developing suitable templates and bounds is problem-dependent and will be refined iteratively through experiments that assess training stability and forecast quality."*

Leave-one-outbreak-out (or leave-one-season-out) calibration of admissible weight ranges, peak-offset windows, and penalty magnitudes is Paper B’s design pattern applied to SIRD-PINN templates (Author-stated need in A; Empirically shown LOO design in B) (Speculative extension).

---

## 5. Dead code and literal parameters as failed soft constraints

Paper A’s systematic generation errors:

> **Quote (Gindullina et al.):** *"We determined systematic errors in the generated code: Adding unused variables and constant terms; Erroneous assumptions about the presence of nonexistent patterns in the data; Incorrect interpretation and use of numerical parameters mentioned in comments."*

In Paper B’s terms, these are repairs that satisfy hard consistency (compilability / “has an answer set”) while violating soft expert properties (no dead terms; numeric cues map to bounded updates). Property-style soft constraints—“penalty coefficients must lie in \([w_{\min},w_{\max}]\) learned from prior successful edits”; “forbid unused bindings”—are the natural ASP-to-PINN transfer (Empirically shown failure modes in A; Speculative extension).

---

## 6. Seven properties vs. four comment classes

Paper B’s expert knowledge is a *checklist of network properties* (fixed point, degree bounds, edge count, likely activator/inhibitor roles, diameter, motifs, basin size), each contributing a capped penalty:

> **Quote (Merhej et al.):** *"In this section, we will consider the seven principles about GRNs that we found in the literature (see Sect. 3). We will briefly explain how each of these principles can be encoded as some kind of soft constraint in ASP. These soft constraints will introduce penalty weights if they are not satisfied by correct repairs."*

Paper A’s knowledge is a *taxonomy of comment speech acts* (curve shape, measures, numeric dynamics, peak position):

> **Quote (Gindullina et al.):** *"It is based on four basic classes, identified through an analysis of typical expert statements: 1. Behavior of the epidemiological curve (visual characteristics). 2. Taking into account measures to counter the spread of the epidemic. 3. Parameters or temporal dynamics of the epidemiological process (numerical characteristics). 4. Position of the epidemic peak on the time axis (in terms of incidence and mortality)."*

The mismatch matters: speech-act classes tell the LLM *where* to edit; property rules tell the solver *which repairs remain plausible*. Modification templates should bind each subclass to both a permitted operator set **and** a property-penalty set (Comparative inference).

---

## 7. Inconsistency as the trigger shared by both pipelines

Paper B repairs when graph dynamics disagree with a time-series table; Paper A “repairs” when the expert disagrees with a PINN forecast. Both are belief-revision loops under imperfect models:

> **Quote (Merhej et al.):** *"In applications where ASP programs simulate a system, inconsistencies could mean that the rules describing the system being simulated are not in agreement with available observations. We may want to find a way to adapt the description of the system, which amounts to a form of belief revision for answer set programs."*

> **Quote (Gindullina et al.):** *"Experience with operational forecasting indicates the need for periodic calibration and adjustment of model behavior, which in turn requires the continuous involvement of highly qualified specialists..."*

The shared structure justifies importing Paper B’s soft-repair evaluation discipline into Paper A’s expert-calibration loop (Comparative inference).

---

## 8. Comparative summary

| Criterion | Paper A (Gindullina et al.) | Paper B (Merhej et al.) | Takeaway |
| :--- | :--- | :--- | :--- |
| Repair objective | Match NL comment (subjective) | Restore consistency + soft properties | A lacks property-level soft cost (Comparative inference) |
| Baseline | Compile-ok LLM edit | Minimal edge add/remove | Minimal ≠ correct (Empirically shown in B) |
| Expert knowledge form | Table A.2 hard permissions | 7 soft rules of thumb | Soft penalties beat hard-only gates (Empirically shown in B) |
| Weight / range setting | Hand rules; templates promised | Hand-uniform weights; LOO ranges | Steal LOO for template bounds (Author-stated / Empirically shown) |
| Metrics | Compliance 25–27%; MAE gates | F1, Jaccard vs. original network | Need structure-level scores for loss edits (Comparative inference) |
| Training data for rules | Synthetic comments for BERT | Leave-one-network-out from 4 peers | Calibrate on held-out outbreaks (Empirically shown in B) |

---

## Direction 1. Soft property layer beside Table A.2

**Pipeline stage:** PINN Customizer validation (post-codegen, pre- or post-retrain).

**Mechanism:** Score candidate losses with soft penalties (population conservation residual, monotone \(D\), bounded peak shift, no unused terms); reject minimal compile-ok edits with high property cost—mirroring RoTh vs. minimal repair.

**Failure mode:** 700-day outbreak; dead-code “successes” (Empirically shown in A).

(Speculative extension — soft-vs-minimal Empirically shown in B.)

---

## Direction 2. Leave-one-season-out bounds for modification templates

**Pipeline stage:** Future-work template design.

**Mechanism:** From prior seasons/cities, learn admissible ranges for penalty weights and peak offsets; deploy on the held-out season exactly as Paper B learns \(k_{\min}/k_{\max}\) and diameter ranges from the other four GRNs.

**Failure mode:** Literal insertion of comment numbers without semantic adaptation (Author-stated in A).

(Speculative extension — LOO Empirically shown in B.)

---

## Direction 3. Report F1-style structure metrics on loss ASTs

**Pipeline stage:** Evaluation.

**Mechanism:** Against a curated gold set of acceptable loss patches per subclass, report precision/recall of edited terms (analogue of edge-set F1), not only visual compliance %.

**Failure mode:** 25–27% primary metric that cannot separate lucky plots from structured repairs (Empirically shown weakness in A).

(Speculative extension)

---

## Direction 4. Uniform-impact weighting until institute labels exist

**Pipeline stage:** Template rollout.

**Mechanism:** Follow Paper B: keep principle weights roughly equal until Smorodintsev experts can rank property importance; do not pretend gradient-learned weights without data.

**Failure mode:** Overfitting soft costs to author intuitions (Author-stated caution in B).

(Speculative extension)

---

## Manuscript placement

- **Future work (class–subclass templates):** cite leave-one-out *range* calibration of soft expert properties as the missing recipe beside Table A.2 (clusters **9**, **7** elicitation secondary).
- **§3.4 / Discussion:** “minimal compile-passing edit” is the baseline Paper B beats—reframe unsuccessful Fig. 4 cases accordingly.
- **Evaluation:** add structure-level F1 on loss AST vs gold patches (cluster **4**).

## What not to transfer

ASP gene-regulatory networks, clasp/`#minimize`, and biology motif libraries are not epidemic deliverables. Paper B has no LLM. Transfer **soft expert properties + LOO range calibration + soft cost beating minimal repair**—not Answer Set encodings. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Soft epi-PINN rules-of-thumb with LOO-calibrated ranges beat Table A.2-only minimal edits on structure F1 and Zone A rate.

**Draft soft properties (uniform weight until Institute ranks them):**
1. Peak-time shift magnitude ∈ subclass range.
2. Post-peak I-slope sign matches comment.
3. No BC/IC weight change unless subclass authorizes.
4. No unused penalty terms (dead code cost).
5. Non-negativity / cumulative monotonicity hard (IC).
6. Duration not > N days unless requested.
7. Literal comment numbers map to *scaled* parameters, not raw loss constants.

**Protocol.** Leave-one-season/wave-out to set numeric ranges; same comments as Paper A; compare minimal Table A.2 vs soft-augmented templates.

**Metric.** Loss-AST F1/Jaccard vs curated gold; Zone A∪B; unused-term rate. Expect soft layer > minimal on F1 even if compile@1 similar. (Speculative extension)

## Related essays in this series

- [`01_hidalgo_2018_glucose_grammatical_evolution.md`](01_hidalgo_2018_glucose_grammatical_evolution.md) — grammar vs over-hard skeleton.
- [`13_potyka_2015_priority_probabilistic_kb.md`](13_potyka_2015_priority_probabilistic_kb.md) — priority layers for soft vs IC.
- [`15_dubois_2015_possibilistic_inconsistency.md`](15_dubois_2015_possibilistic_inconsistency.md) — conflicting properties salvage.
- Bridge: [`../dinara_analysis/03_yu_2025_spec2rtl_agent.md`](../dinara_analysis/03_yu_2025_spec2rtl_agent.md) — verify structured intermediate before execute.

## Conclusion

Merhej et al. demonstrate that when a formal model conflicts with data, **expert soft rules of thumb systematically beat minimal repairs**, even with hand-uniform weights, provided property *ranges* are calibrated leave-one-out. Gindullina et al. currently ship the minimal-repair analogue—coarse Table A.2 plus compile checks—and defer templates without a calibration recipe. The strongest cross-paper reading is operational: treat modification templates as rules of thumb with LOO-bounded numeric ranges and a soft property cost, then measure repair quality with structure-level F1/Jaccard analogues rather than subjective compliance alone.
