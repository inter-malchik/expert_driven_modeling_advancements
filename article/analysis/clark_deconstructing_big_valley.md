Paper A (Gindullina et al., Expert-Guided PINN) closes each expert-in-the-loop iteration by **further training** a SIRD-PINN from the current weight state under an LLM-modified composite loss, then showing the expert a new forecast. The authors report that 15–28% of runs produce no meaningful forecast change despite a new loss, and that interactive sessions are sequential—each round starts from the model produced by the previous one. Paper B (Ochoa and Veerapen, 2016, *Deconstructing the Big Valley Search Space Hypothesis*) uses local optima networks (LON) on TSP to show that the classic “big valley”—local optima clustered around one global optimum—**decomposes into disconnected funnels** (connected components). Once iterated local search is trapped in a sub-optimal funnel, standard escape moves (double-bridge kicks in Chained Lin–Kernighan) cannot reach other components; random restarts become necessary.

The comparative payoff is structural, not domain-identical: Paper A’s retraining loop is an iterated local search over PINN weights under a changing objective, warm-started from the prior solution. Paper B supplies a named landscape mechanism—**funnel entrapment**—that can explain part of the 15–28% “unchanged forecast” subset and the **order dependence** of a multi-comment session without attributing every failure to the LLM (Comparative inference). This complements essay #41 (gradient ravines in continuous error landscapes): here the emphasis is **disconnected basins** and insufficient escape operators, not sampling geometry alone.

---

## 1. The big-valley picture versus multi-funnel reality

The big valley hypothesis posits that good local optima cluster around the global optimum, making search tractable.

> **Quote (Ochoa and Veerapen):** *«The big valley hypothesis suggests that, in combinatorial optimisation, local optima of good quality are clustered and surround the global optimum.»*

> **Quote (Ochoa and Veerapen):** *«We argue that this view of combinatorial search spaces is not complete. We challenge the existence of a single valley, and present compelling and visual evidence of examples where the big valley de-constructs into several valleys, also called 'funnels' in the study of energy surfaces in theoretical chemistry.»*

Paper A does not analyse the PINN weight landscape, but its training stage assumes that a small loss edit plus continued Adam optimisation can reach forecasts aligned with expert intent. The “globally convex” intuition is implicit in treating each comment as a local corrective step. Paper B shows that assumption fails on hard TSP instances even under state-of-the-art heuristics (Empirically shown).

---

## 2. Funnel entrapment and the need for restarts

Paper B links funnel structure directly to search stagnation:

> **Quote (Ochoa and Veerapen):** *«When trapped in a sub-optimal funnel, a local search heuristic will not be able to escape even with relatively large random perturbations.»*

> **Quote (Ochoa and Veerapen):** *«Once the search process is trapped in a sub-optimal funnel, it simply cannot escape from it using the underlying escaping mechanism (double-bridge moves in our study). Increasing the number of iterations will not improve the performance, the search will stall, as transitions to other funnels are not possible.»*

Paper A’s retraining uses fixed hyperparameters and no documented random re-initialisation when a modification fails to move the forecast:

> **Quote (Gindullina et al.):** *«After successfully generating a syntactically correct loss function, the module initiates the process of further training of PINN»* with Adam at learning rate 0.0001, decaying every 5000 epochs (§2.3).

> **Quote (Gindullina et al.):** *«our analysis identified a subset of instances (15–28%) (Figure 5) where adapting the loss function did not yield a meaningful divergence from the original forecast.»*

If weights remain in the basin of the pre-modification solution, the forecast can stay unchanged even when the loss code differs—a pattern consistent with funnel trapping under warm start, not only LLM no-ops (Comparative inference). Paper A does not run same-loss multi-seed controls to separate optimisation variance from modification effect (Author-stated gap in dinara_comprehensive_review.md critique).

---

## 3. Local optima networks as a diagnostic metaphor

Paper B compresses landscapes into graphs whose **connected components** are funnels:

> **Quote (Ochoa and Veerapen):** *«Local optima networks compress the whole search space into a graph, where nodes are local optima and edges are transitions among them with a given search operator.»*

> **Quote (Ochoa and Veerapen):** *«funnels correspond to connected components. Once trapped in a connected component, it is not easy for the search process to hop to another component. There are no connections among components with the underlying escaping mechanism.»*

Paper A’s pipeline has no analogue: after LLM edits the loss, the Code Tester checks compilability only, then training proceeds. There is no graph-level check of whether the new objective connects the current weights to regions that satisfy the expert comment. Fig. 4 plots show “PINN initial model” (grey) versus “Modified PINN model” (green)—a single hop per iteration, not exploration of alternative basins (Author-stated).

---

## 4. Global optima outside the largest funnel

A central empirical finding in Paper B is that the global optimum may lie in a **small** funnel:

> **Quote (Ochoa and Veerapen):** *«The global optimum might be located in a small valley, which offers a clear and visual explanation of the increased search difficulty in these cases.»*

On instance rat575 (hardest in their table), global optima appear in the 8th connected component, containing only 2.67% of sampled local optima—while Chained-LK success rate is 0.01 (Empirically shown).

Paper A’s hardest metric is semantic compliance at 25–27% for the best LLMs (Empirically shown):

> **Quote (Gindullina et al.):** *«the best-performing models achieve a 25–27% success rate in generating predictions that semantically align with expert intent.»*

The parallel is methodological: both systems can appear “almost working” on marginal criteria while the primary target remains in a **small, hard-to-reach** region of the search space—TSP global tours versus comment-aligned epidemic curves (Comparative inference). Paper A’s 81–85% “forecast has changed” (Fig. 5) can mask that the changed forecast still misses expert intent, similar to finding many local optima without reaching the funnel that contains the desired behaviour.

---

## 5. Warm-start retraining as iterated local search

Paper B’s sampling uses Chained Lin–Kernighan: kick (double-bridge), then local search (LK)—iterated local search (ILS):

> **Quote (Ochoa and Veerapen):** *«If a better tour is produced, we discard the old LK tour and keep the new one. Otherwise, we continue with the old tour and kick it again.»*

Paper A’s loop is cognate: keep trained weights, change loss, continue optimisation:

> **Quote (Gindullina et al.):** *«The PINN was retrained with this loss, yielding a new forecast shown by the green dashed line.»*

Fig. 4 captions distinguish the grey “PINN initial model” from the green modified model—sequential dependence on the previous solution (Author-stated). Paper B implies that without **tunnelling** between funnels, ILS stalls; Paper A provides no escape operator (random re-init, ensemble, or loss-space tunneling) when a comment requires a qualitatively different basin—e.g. shifting peak timing without weakening the zero boundary condition (Fig. 4b failure) (Comparative inference).

---

## 6. Order of expert comments and non-commutative modifications

Paper B’s funnel insight explains why **restart ensembles** matter in combinatorial search; Paper A’s interactive pathway (Appendix A.7) is strictly sequential with no ablation on comment order.

> **Quote (Gindullina et al.):** *«A key contribution of this study is an interactive framework that instantiates an expert-in-the-loop optimization cycle.»*

If each modification warm-starts from the prior PINN state, the reachable forecasts form a **path-dependent** set: comment B after comment A may not reach the same region as B alone from the base model—analogous to entering different TSP funnels depending on kick history (Comparative inference). Paper A never tests permutation of comments or reset-to-base between rounds (Author-stated limitation). Essay #39 (linear vs hierarchical modification templates) addressed representation; Paper B addresses **dynamical entrapment** in the weight landscape.

---

## 7. Documented failures reinterpreted through funnel structure

Fig. 4b: peak-shift request leads to weakening the zero boundary condition and a >700-day epidemic:

> **Quote (Gindullina et al.):** *«reducing the influence of the zero boundary condition in the loss function... the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days).»*

Within one funnel, local improvements in shape can coexist with catastrophic constraint violation—Paper B’s fitness-distance plots show distinct components with near-optimal tour cost on rat575 (§5.2). Fig. 4c: fourfold BC weight increase yields plateau instead of continued growth; authors hypothesise BC dominance reduced ODE penalty effectiveness (Author-stated). That is a **reweighted funnel**: optimisation settles in a basin where BC terms dominate, not where the expert’s growth instruction is encoded (Comparative inference). Paper B does not study PINNs; the link is explanatory, not a claimed replication (Speculative extension boundary noted).

---

## 8. Sampling bias and attributed causes of failure

Paper B is explicit that LON data are sampled, not exhaustive:

> **Quote (Ochoa and Veerapen):** *«the sampling mechanism, including the parameter values for the number of kicks and runs, introduces a bias generating an approximation of the search space and not the complete picture.»*

Paper A likewise attributes some bad forecasts to PINN optimisation limits rather than LLM error alone:

> **Quote (Gindullina et al.):** *«The use of physics-informed neural networks inherits their systemic limitations... including the complexity of optimization, sensitivity to hyperparameters, and the lack of guarantees that physical constraints will be satisfied in the final solution.»*

> **Quote (Gindullina et al.):** *«We hypothesize that discrepancies between the forecast and training data (Figure 5), as well as violations of epidemiological logic in some cases, may be a consequence of these architectural features of PINNs, and not solely errors in the operation of the LLMs.»*

Both papers admit **unobserved landscape structure**—incomplete LON samples versus unmeasured PINN basins—but only Paper B supplies a concrete structural vocabulary (funnels) for stagnation. Paper A lists optimisation sensitivity without diagnosing entrapment (Comparative inference). A funnel-aware evaluation would make the PINN hypothesis testable: unchanged forecasts at fixed loss across seeds versus across basins reached only after restarts.

---

## 9. Comparison table

| Criterion | Paper A (Expert-Guided PINN) | Paper B (Ochoa & Veerapen) | Takeaway |
| :--- | :--- | :--- | :--- |
| Search space | PINN weights under composite loss | TSP tours under LK local search | Both are local-search landscapes |
| Iteration pattern | Further training from current weights | Chained LK with double-bridge kicks | Both are ILS-style |
| Landscape model | None | LON; funnels = connected components | Paper A lacks funnel diagnostics |
| Escape when stuck | More Adam epochs; new LLM loss | Fails within funnel; needs restarts/tunnelling | Paper A may stall like trapped ILS |
| “No change” outcomes | 15–28% unchanged forecast | ILS stalls inside component | Warm-start trapping is a candidate cause |
| Hard cases | 25–27% comment compliance | rat575: GO in 2.67% component; 1% CLK success | Primary success may live in small funnel |
| Order effects | Sequential expert loop, not tested | Kick history determines component | Comment order may matter (untested in A) |

---

## Direction 1. Multi-start retraining after each loss modification

**Stage:** PINN Customizer retraining loop. **Mechanism:** After LLM produces a candidate loss, run K trainings from diverse weight initialisations (or K noise perturbations of current weights), not only warm start. **Failure mode addressed:** 15–28% unchanged forecasts and funnel entrapment under continue-training (Speculative extension; motivated by Paper B’s restart requirement).

## Direction 2. Funnel probe before accepting a modification

**Stage:** Between Code Tester and full retrain. **Mechanism:** Short optimisation bursts or progressive gradient walks (cf. essay #41) from current weights under candidate loss; estimate whether loss decreases along directions that move the forecast metric (peak day, post-peak slope). Reject modifications that only descend within the current basin. **Failure mode:** Fig. 4b-style plausible curves with violated semantics (Speculative extension).

## Direction 3. Reset-to-base policy for cross-class comments

**Stage:** PINN Customizer policy layer. **Mechanism:** When the classifier assigns a new class/subclass (e.g. peak position vs curve shape), retrain from the **calibrated base PINN** rather than the last interactive state—analogous to ILS random restart when kicks fail to improve. **Failure mode:** Path-dependent hysteresis across sequential comments (Comparative inference → Speculative extension).

## Direction 4. Tunneling operators between loss basins

**Stage:** LLM modification templates (Future work). **Mechanism:** Instead of arbitrary weight edits in code, allow large structured jumps—e.g. swap adaptive weighting scheme (NTK / ReLoBRaLo) or temporarily zero one loss term then ramp it—mirroring Paper B’s call for *«escaping and tunnelling mechanisms that allow the search process to navigate among funnels.»* **Failure mode:** BC/ODE imbalance in Fig. 4b,c (Speculative extension; Paper B Author-stated future work).

## Direction 5. Report joint success and basin diagnostics

**Stage:** Evaluation (§2.4). **Mechanism:** Publish conjunction of all four criteria (joint success rate per dinara_comprehensive_review.md) plus variance over seeds at **fixed** loss. Optionally log TSED + forecast MAE variance as a crude “component size” proxy. **Failure mode:** Marginal Fig. 5 bars overstating practical utility; confounding LLM error with optimisation trap (Speculative extension).

---

## Conclusion

Ochoa and Veerapen empirically deconstruct the TSP big valley into multiple disconnected funnels, demonstrating that iterated local search with standard escapes cannot move between them and that global optima may sit in small, hard-to-find components. Gindullina et al. implement an expert-in-the-loop cycle that warm-starts PINN retraining after each LLM loss edit, reports substantial “unchanged forecast” rates, and does not test order effects or multi-start escape. Mapping Paper B’s funnel entrapment onto Paper A’s continue-training loop offers a landscape-theoretic account of optimisation stagnation that complements LLM-centric explanations and gradient-pathology analyses elsewhere in the `dinara_analysis` series (Cluster 5). The actionable lesson is not to copy TSP heuristics into PINNs, but to treat each expert comment as potentially requiring **basin escape**—restarts, tunneling moves, or funnel diagnostics—not merely more epochs in the same warm-started basin.
