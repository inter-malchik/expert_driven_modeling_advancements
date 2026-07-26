> **Paper B — live link:** [https://jasss.soc.surrey.ac.uk/11/4/12.html](https://jasss.soc.surrey.ac.uk/11/4/12.html)  
> **Source in `src/`:** [`../src/2008 Why Model?.md`](../src/2008%20Why%20Model%3F.md)

Gindullina et al. (hereafter **Paper A**) title their contribution *«Expert-guided forecasting of epidemic ARI incidence based on physics-informed neural networks and large language models»*, and open their introduction with «Accurate forecasting in computational and mathematical epidemiology is crucial». Their evaluation, however, treats compliance-with-comment as the primary criterion and explicitly notes that «this study, therefore, assesses the capability for instruction-following, not the impact of the comment on forecast accuracy». The paper reports 25–27% compliance as feasibility proof — a rate the authors themselves call subjective — and never demonstrates that expert-guided modifications produce better out-of-sample forecasts than a data-driven PINN alone.

Joshua Epstein (2008; hereafter **Paper B**) is a two-page keynote-essay that codifies a philosophical position: prediction is one of at least 17 reasons to build a model; the choice is not whether to model but whether to make the model *explicit*; and all scientific knowledge — including models — should be held with «militant ignorance», an iron commitment to «I don't know». The essay is small, argumentative, non-empirical, and touches almost every diagnosis in `dinara_comprehensive_review.md` about how Paper A frames its own contribution.

Paper B is not about PINN or LLMs; it is a normative statement about what modeling *is for*. The transferable thesis is sharp: **Paper A's «feasibility of expert-guided forecasting» framing conflates 3 or 4 of Epstein's 17 modeling purposes (predict, explain, illuminate uncertainties, discipline policy dialogue); disentangling them — using Epstein as the taxonomy — turns 25–27% compliance from an ambiguous headline into a specific claim about instruction-following, and it re-classifies Fig. 4b/c not as method failures but as canonical examples of Epstein's «all models are wrong; some are useful» aphorism, provided the framing makes explicit which of the 16 non-predictive goals the LLM-guided cycle serves.**

---

## 1. «Everyone is a modeler» and Paper A's implicit LLM model

Epstein's opening move is that anyone who imagines an epidemic unfolding is already running a model — an *implicit* one whose assumptions are hidden. Paper A's LLM-generated loss modification is an implicit model in exactly this sense: the LLM's understanding of what «shift the peak by 7–10 days» implies for the SIRD loss function is buried inside its weights.

> **Quote (Epstein):** *"Anyone who ventures a projection, or imagines how a social dynamic—an epidemic, war, or migration—would unfold is running some model. ... But typically, it is an implicit model in which the assumptions are hidden, their internal consistency is untested, their logical consequences are unknown, and their relation to data is unknown."*

> **Quote (Gindullina et al.):** *"After generating the LLM candidate loss function, its automatic validation is performed (Figure 2), which includes: 1. Syntactic analysis – checking the code's compilability using the Python interpreter."*

Under Epstein, compile-check is a symptom, not a solution: it verifies that the *output* of the implicit LLM model is executable, but leaves the LLM's model implicit. What Paper A calls «lack of interpretability of the generated loss functions» is exactly Epstein's «assumptions are hidden». Making the LLM-model explicit — via facet-typed slots (essay 22) or structural-equation representations (essay 21) — is the direct upgrade this essay recommends. (Comparative inference)

---

## 2. Explanation ≠ prediction: Paper A's own admission

Paper A openly separates instruction-following (evaluated) from forecast accuracy (unevaluated). Epstein's second-most-emphatic point is that explanation and prediction are distinct modeling goals — plate tectonics explains but does not predict earthquake timing.

> **Quote (Epstein):** *"One crucial distinction is between explain and predict. Plate tectonics surely explains earthquakes, but does not permit us to predict the time and place of their occurrence. Electrostatics explains lightning, but we cannot predict when or where the next bolt will strike. ... I consider this model to be explanatory, but I would not insist that it is predictive on that account."*

> **Quote (Gindullina et al.):** *"It is crucial to note that the successful model modification via external input does not mean the quality or correctness of the expert's suggestion itself, which may be suboptimal. This study, therefore, assesses the capability for instruction-following, not the impact of the comment on forecast accuracy."*

The two quotes are the same idea. Epstein makes it foundational: explanation is a fully legitimate goal without prediction. Paper A quietly confesses that its measured quantity is not predictive. Under Epstein's framing, Paper A's 25–27% is a compliance-with-expert-intention rate, not a forecasting metric — and *that is fine*, provided the paper says so more emphatically in the title and abstract. (Comparative inference)

---

## 3. Sixteen non-predictive goals: re-classifying Paper A's contribution

Epstein's central table lists 16 modeling goals beyond prediction. At least four of them apply directly to Paper A:

> **Quote (Epstein):** *"1. Explain (very distinct from predict) 2. Guide data collection 3. Illuminate core dynamics 4. Suggest dynamical analogies 5. Discover new questions 6. Promote a scientific habit of mind 7. Bound (bracket) outcomes to plausible ranges 8. Illuminate core uncertainties. 9. Offer crisis options in near-real time 10. Demonstrate tradeoffs / suggest efficiencies 11. Challenge the robustness of prevailing theory through perturbations 12. Expose prevailing wisdom as incompatible with available data 13. Train practitioners 14. Discipline the policy dialogue 15. Educate the general public 16. Reveal the apparently simple (complex) to be complex (simple)"*

> **Quote (Gindullina et al.):** *"Simplifying the interaction between the operator and the mathematical model could substantially broaden the use of forecasting in epidemiological practice"*

Mapping: (a) **Discipline the policy dialogue (#14)** — the HITL cycle forces epidemiologists to state their beliefs about the epidemic *before* seeing the forecast, exposing implicit assumptions; (b) **Train practitioners (#13)** — modifying loss terms teaches epidemiologists what BC weight actually does; (c) **Illuminate core uncertainties (#8)** — Fig. 4b's 700-day outbreak is a diagnostic of PINN sensitivity to BC-weight tuning, not just a method failure; (d) **Reveal the apparently simple to be complex (#16)** — «shift the peak by 7 days» turns out to imply non-obvious interactions across loss components. Paper A implicitly does all four, but never names them. Naming them promotes its 25–27% to a defensible headline. (Comparative inference)

---

## 4. «All models are wrong, but some are useful»: Fig. 4b/c as illuminating errors

Epstein quotes George Box: «all models are wrong, but some are useful». He then argues that the value of a *fruitfully wrong* model is qualitative behavior, not point accuracy. Paper A's Fig. 4b (700-day outbreak) and Fig. 4c (BC ×4 plateau) are treated as failures.

> **Quote (Epstein):** *"Indeed, by such lights, all the best models are wrong. But they are fruitfully wrong. They are illuminating abstractions. ... they capture qualitative behaviors of overarching interest, such as predator-prey cycles, or the nonlinear threshold nature of epidemics and the notion of herd immunity. ... the issue is whether the model offers a fertile idealization."*

> **Quote (Gindullina et al.):** *"the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days). This example illustrates that, in the absence of clear and interpretable modification rules, an LLM may generate a loss function whose use leads to inadequate forecasts."*

Under Epstein, Fig. 4b/c are not *just* failures — they are **illuminating**: they reveal that PINN loss modifications are more sensitive to auxiliary terms (BC weight) than to the ostensible target (peak position). This is exactly what Epstein calls «illuminate core uncertainties» — a documented, reproducible demonstration that the loss surface has non-obvious sensitivities. Reporting them as fruitful failures rather than method failures is a rhetorical upgrade with real epistemic content. (Comparative inference)

---

## 5. Guide data collection: 20 launches vs pre-registered hypotheses

Epstein's third goal is «guide data collection» — theory precedes data, tells you what to measure. Paper A collects data (20 launches per LLM) *after* the ontology and prompts are fixed, and never uses the results to guide further data collection.

> **Quote (Epstein):** *"'Science proceeds from observation, and then models are constructed to "account for" the data.' The social science rendition—with which I am most familiar—would be that one first collects lots of data and then runs regressions on it. This can be very productive, but it is not the rule in science, where theory often precedes data collection. ... Without models, in other words, it is not always clear what data to collect!"*

> **Quote (Gindullina et al.):** *"All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment. This setting was used exclusively during the testing and prototyping phase to explore the system's full behavioral range."*

Paper A treats T=1.0 as a data-collection mechanism (maximize variation, see what comes out). Under Epstein's frame, a model-driven data-collection strategy would specify: for each comment class, *predict* what fraction of LLM-generated modifications will pass which criterion, then collect data to test that prediction. This is the discipline `dinara_comprehensive_review.md` calls «prediction of failure modes», absent in Paper A. (Comparative inference)

---

## 6. Militant ignorance: Paper A's honest reporting is the strongest defense

Epstein's most Feynman-inflected point is that scientific knowledge must be held with «militant ignorance»: a commitment to «I don't know». Paper A does exhibit some of this virtue — it explicitly documents Fig. 4b/c as failures, honestly reports 25–27% compliance, and dedicates a Limitations section.

> **Quote (Epstein):** *"the most important contribution of the modeling enterprise—as distinct from any particular model, or modeling technique—is that it enforces a scientific habit of mind, which I would characterize as one of militant ignorance—an iron commitment to "I don't know". That is, all scientific knowledge is uncertain, contingent, subject to revision, and falsifiable in principle."*

> **Quote (Gindullina et al.):** *"These results should be considered proof-of-concept, demonstrating the potential of the approach but also highlighting the need to develop more stringent generation rules and control mechanisms to ensure the interpretability and reliability of the results."*

Under Epstein, the 25–27% figure is *virtue*, provided it is framed correctly. The failure mode is not the number but the framing: Paper A's abstract still calls the result «feasibility of this approach», which suggests success rather than «we do not yet know how much of this compliance is causal». Rephrasing: «we demonstrate 25–27% instruction-compliance under conditions X, Y, Z; whether this constitutes forecast-improvement in operational use remains an open question we intend to answer via Smorodintsev field study» — that is militant ignorance in operational form, and it is stronger science than the current framing. (Comparative inference)

---

## 7. Discipline the policy dialogue: automation bias vs stated tradeoffs

Epstein's #14 goal («discipline the policy dialogue») argues that explicit models make tradeoffs and uncertainties available to non-specialist decision makers. Paper A's Vaccaro (2024) citation warns that human+AI teams often lose to either alone — the automation-bias concern in `dinara_comprehensive_review.md` §4.

> **Quote (Epstein):** *"in the policy sphere ... models do not obviate the need for judgment. However, by revealing tradeoffs, uncertainties, and sensitivities, models can discipline the dialogue about options and make unavoidable judgments more considered."*

> **Quote (Gindullina et al.):** *"it is worth noting that the use of LLMs in combination with forecasting models, while addressing long-standing challenges, may also introduce new issues related to the interaction between human and artificial intelligence Kovalchuk et al. (2022), Vaccaro et al. (2024)."*

Epstein prescribes what Paper A cites but does not operationalize: revealing tradeoffs, uncertainties, and sensitivities as first-class outputs. Paper A shows a forecast plot; it does not show the LLM-modification's confidence, alternative modifications considered, or sensitivity to random seeds. Under Epstein's frame, the primary output of the Customizer should be a tradeoff card, not a single forecast line. (Speculative extension)

---

## 8. Comparison table

| Criterion | Paper A | Paper B (Epstein) | Takeaway |
| :--- | :--- | :--- | :--- |
| Modeling goal | Implicit conflation: predict + explain + comply | 17 distinct goals (predict + 16 others) | Disentangle to defend 25–27% (Comparative inference) |
| Model status | Implicit LLM; explicit PINN loss | Explicit preferred over implicit | LLM-model needs to be made explicit (Comparative inference) |
| Validation vocabulary | «Compliance with the comment» (subjective) | «Calibrate» not «validate»; Popperian falsifiability | Rename metric to «instruction-compliance under X, Y, Z» (Comparative inference) |
| Failure interpretation | Fig. 4b/c as method failure | «All best models are wrong; some are fruitfully wrong» | Fig. 4b/c illuminate PINN loss sensitivity (Comparative inference) |
| Data collection | Post hoc, T=1.0, 20 launches | Theory precedes data | Pre-register predicted failure modes (Speculative extension) |
| Epistemic virtue | Documented, but under-framed | Militant ignorance | Frame 25–27% as scientific virtue, not weakness (Comparative inference) |
| Policy role | Single forecast output | Tradeoffs, uncertainties, sensitivities | Ship tradeoff card, not forecast line (Speculative extension) |

---

## Direction 1. Re-frame Paper A's contribution against Epstein's 17-goal taxonomy

**Pipeline stage.** Introduction, Conclusion, and title framing (no pipeline changes; framing only).  
**Mechanism.** Explicitly enumerate which of Epstein's 17 goals the Expert-Guided PINN system serves:
- **Primary:** Discipline the policy dialogue (#14) + Train practitioners (#13) + Illuminate core uncertainties (#8) + Suggest tradeoffs (#10).
- **Secondary:** Reveal simple to be complex (#16) — via Fig. 4b/c documentation.
- **Not addressed:** Prediction accuracy (Goal 0, prediction) — call this out as a separate line of future work.

Rewrite the abstract along these lines: *«We introduce an interactive system that (i) disciplines the policy dialogue by translating expert judgment into inspectable code, (ii) trains practitioners in the semantics of PINN loss modification, and (iii) illuminates sensitivity of forecast trajectories to auxiliary loss terms. Instruction-compliance rate under our specific protocol reaches 25–27%; predictive skill improvement is deferred to future work.»*

**Failure modes addressed.** Ambiguity in headline; automation-bias risk from overselling prediction; misalignment between title (forecasting) and evaluation (compliance). (Speculative extension)

---

## Direction 2. Tradeoff-card output as the primary Customizer artifact

**Pipeline stage.** §2.3 PINN Customizer output presentation + Sahatova 2023 GUI baseline.  
**Mechanism.** Replace «show new forecast plot» with a tradeoff card listing per-modification: (i) k=8 candidate modifications the LLM considered, ranked by MQM / TRM-analogue (essay 20); (ii) forecast plot for top-3, not just top-1; (iii) sensitivity plot: how the top-1 forecast varies under retrain-seed permutation; (iv) which loss terms were modified and by how much; (v) which epidemic-logic constraints are preserved; (vi) confidence score derived from surrogate (essay 19).  
**Failure modes addressed.** Automation bias (expert sees alternatives, not a single confident line); over-reliance on single-shot LLM output; opacity of what changed in the loss. Direct implementation of Epstein's «discipline the policy dialogue». (Speculative extension)

---

## Manuscript placement

- **Introduction:** cite Epstein to enumerate the 17 modeling goals and identify which apply to Expert-Guided PINN. Positions the paper's contribution more sharply and creates space for the honest concession that predictive skill is unmeasured (clusters **7** knowledge elicitation, **10** automation bias/governance of `dinara_comprehensive_review.md`).
- **§4 Limitations:** rephrase «significant subjective component» as «instruction-compliance evaluation, per Epstein's #14 «discipline the policy dialogue»; predictive-skill goal (Epstein #0) is a separate contribution deferred to Smorodintsev field study».
- **§5 Conclusion:** end with Epstein's militant-ignorance line — reframing 25–27% as scientific virtue rather than as weakness.

## What not to transfer

Epstein's essay is a keynote lecture, not empirical work. Do not import his agent-based-modeling examples (Anasazi Sugarscape) — Paper A is about PINN, not agent-based simulation. Do not treat the 17-goal list as exhaustive; it is «off the top of my head» per Epstein's own words. Do not confuse Epstein's «militant ignorance» with an excuse to under-evaluate: Epstein's target is over-claiming, not under-claiming. And do not use Epstein to justify not doing the Smorodintsev field study (`dinara_comprehensive_review.md` §2.5); Epstein specifically advocates operational calibration and testing. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Restating Paper A's contribution against Epstein's 17-goal taxonomy — explicitly naming which goals the paper does and does not achieve — will shift reviewer response from «feasibility unclear» to «feasibility demonstrated for specific named goals», without any change to the underlying system, evaluation, or numbers.

**Protocol.**
1. Draft an alternate abstract per Direction 1.
2. Send both abstracts blind to 3–5 epidemiologists (Smorodintsev + external) and 3–5 ML researchers.
3. Ask each: (i) what does this paper achieve; (ii) what is missing; (iii) would you cite this in policy or as a method benchmark?
4. Compare mean responses.

**Expected signal.** Reviewers see clearer scope in the Epstein-framed abstract; policy-relevant citations increase; method-benchmark citations decrease (correctly — Paper A is not yet a forecasting benchmark). This is a rhetorical experiment, not a technical one — cheap and revealing. (Speculative extension)

## Related essays in this series

- [`20_zhang_2026_trm_complex_reasoning.md`](20_zhang_2026_trm_complex_reasoning.md) — decoupling reasoning quality from answer correctness; direct operational form of Epstein's explanation-≠-prediction distinction.
- [`10_studer_1998_knowledge_engineering.md`](10_studer_1998_knowledge_engineering.md) — knowledge-modeling perspective; Epstein's #14 (discipline the dialogue) as KE outcome.
- [`04_miller_2020_contrastive_explanation.md`](04_miller_2020_contrastive_explanation.md) — contrastive framing supports Epstein's #14/#16.
- [`12_mehdi_2015_compositional_forecasting.md`](12_mehdi_2015_compositional_forecasting.md) — proper scoring rules for the (deferred) prediction-goal work.

## Conclusion

Paper B is a two-page keynote-essay; it does not describe any system, dataset, or algorithm. It is nonetheless the most concise philosophical foundation available for a paper in Paper A's exact position: a modeling contribution that oscillates between three under-distinguished goals (predict, explain, comply), whose primary metric is honestly reported at 25–27% but under-framed as feasibility, and whose most-discussed «failures» (Fig. 4b/c) are actually illuminating uncertainties. Epstein's 17-goal taxonomy, his explanation-≠-prediction distinction, and his militant-ignorance principle are all available as rhetorical machinery — no code changes required. The upgrade is entirely in framing, and it makes Paper A a stronger paper about what it actually does, which is not (yet) forecast prediction but rather HITL policy-dialogue-discipline with quantitative instruction-compliance evidence.
