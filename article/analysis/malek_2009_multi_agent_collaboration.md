> **Paper B — live link:** (specialization study, Czech Technical University 2009; no DOI available)  
> **Source in `src/`:** [`../src/2009 Global Optimization through Meta-Heuristic Collaboration in a Multi-Agent System.md`](../src/2009%20Global%20Optimization%20through%20Meta-Heuristic%20Collaboration%20in%20a%20Multi-Agent%20System.md)

Gindullina et al. (hereafter **Paper A**) implement a four-component pipeline: Conversational Agent → Hierarchical BERT classifier → PINN Customizer → off-the-shelf LLM (Llama-3.1-8B / Llama-3.3-70B / DeepSeek-V3.1). Compliance rates across the three LLMs are 6% / 25% / 27% — an implicit portfolio in which different LLMs perform differently on the same 20 comments. The paper's Future-work section names an explicit multi-agent extension: «*A promising direction is to evolve the system toward a multi-agent architecture, where specialized LLMs enhance autonomy and objectivity. An LLM-expert-evaluator could quantify forecast compliance ... An LLM-loss-semantic-checker could verify alignment between the generated code and modification rules.*» No architecture, no coordination protocol, no empirical demonstration.

Malek (2009; hereafter **Paper B**) — a Czech Technical University specialization study — presents a working multi-agent architecture for meta-heuristic collaboration on Aglobe: Problem Agent, SolutionPool Agent, Algorithm Agent (one per meta-heuristic, wrapped by an adapter interface), and Adviser Agent (parameter reasoning). Meta-heuristics collaborate through a shared SolutionPool blackboard rather than through direct coupling, and the phenotype/genotype abstraction lets any algorithm consume any other's output. Empirical validation: GA + TS collaboration on 10 TSP benchmark instances beats individual GA or TS on 9/10 (eil51: 428 vs 478/430; berlin52: 7544 vs 8261/8007; ch130: 7303 vs 11300/9315; etc.), under identical 10-minute compute budgets.

Paper B is not about PINN, LLMs, or epidemics; it is a domain-agnostic template for how independent optimization procedures should be composed into a system that collaborates rather than being called in sequence. The transferable thesis is sharp: **Paper A's Future-work multi-agent LLM architecture is a re-instance of Malek's 2009 Aglobe design, but proposed without acknowledging that (i) a shared SolutionPool is the coordination locus, (ii) an Adviser Agent is the parameter-selection layer, (iii) an adapter interface (phenotype/genotype abstraction) is the way heterogeneous LLMs are combined, and (iv) empirical collaboration-over-individual has already been demonstrated in Paper B; naming these elements gives Paper A's multi-agent Future work a concrete design + a decade of empirical precedent.**

---

## 1. Aglobe multi-agent architecture as blueprint

Paper B's core architectural decision is to use a multi-agent platform (Aglobe) with four agent types, each responsible for a distinct concern. Paper A's Future work proposes a multi-agent architecture without naming any of these components or a coordination protocol.

> **Quote (Malek):** *"There are following agent types in our system: a problem agent, a solution pool agent, an algorithm agent and an adviser agent. ... Problem agent is the entry point of our system. ... SolutionPool agent manages the population of candidate solutions ... Algorithm agent which disposes of a particular meta-heuristic algorithm. ... Adviser agent provides parameter settings for the meta-heuristic algorithms and receives reports on algorithm runs."*

> **Quote (Gindullina et al.):** *"A promising direction is to evolve the system toward a multi-agent architecture, where specialized LLMs enhance autonomy and objectivity. An LLM-expert-evaluator could quantify forecast compliance with the original comment; low confidence scores could trigger automatic loss regeneration or comment refinement. An LLM-loss-semantic-checker could verify alignment between the generated code and modification rules, reducing hallucinations."*

Direct mapping: Paper A's implicit Problem Agent = Conversational Agent + classifier; SolutionPool = missing (each LLM call is stateless); Algorithm Agents = wrapped LLMs; Adviser = missing (no parameter reasoning). Paper A's proposed «LLM-expert-evaluator» is an additional Algorithm Agent operating on modification outputs; «LLM-loss-semantic-checker» is another. What Paper A does not name is *what coordinates them* — that is exactly the SolutionPool + Adviser layer in Paper B. (Comparative inference)

---

## 2. SolutionPool as shared blackboard for iterative refinement

Paper B's central insight is that heterogeneous meta-heuristics share candidate solutions through a global pool, not through direct calls. Paper A's LLM iterations are stateless — each retry starts from the current PINN loss with no memory of prior attempts within the same comment.

> **Quote (Malek):** *"In our concept, the results of work of particular meta-heuristics are shared through a global population of candidate solutions. We denote the place, where the population is located, as a solution pool. ... Each meta-heuristic takes one or more solutions from and after it finishes, puts them back into solution pool. Simply, candidate solutions are improved by many different meta-heuristics and population of candidate solutions is being evolved."*

> **Quote (Gindullina et al.):** *"Iterative correction – if compilation errors are detected, the system automatically generates a clarifying request to LLM describing the error so that a corrected version can be regenerated."*

Paper A retries the LLM only on compile failure and gives it no context beyond the error message. A SolutionPool would store: (i) all k candidate modifications the LLM has previously emitted for this comment; (ii) their compile results, MAE scores, and (once evaluators exist) TRM-style rewards; (iii) which modifications passed / failed which criteria. On the next LLM call, this history is part of the prompt. The mechanism converts stateless single-shot rewriting into pool-mediated iterative refinement — exactly the structure Paper B validated on TSP. (Comparative inference)

---

## 3. Adviser Agent = missing parameter/LLM-selection layer

Paper B's Adviser Agent chooses parameters for each Algorithm Agent based on reports of past algorithm behavior. Paper A uses fixed hyperparameters across all launches (temperature=1.0, one prompt template, one LLM per experiment); no per-comment adaptation, no learning from failures.

> **Quote (Malek):** *"Adviser agent provides parameter settings for the meta-heuristic algorithms and receives reports on algorithm runs. This agent is an object of interest for future work (reasoning). ... During the algorithm runtime a lot of information may be tracked. For example: the number of solution improvements, the number of iterations without change, the change of average solution quality, etc. All the information may indicate if the algorithm parameters were set properly."*

> **Quote (Gindullina et al.):** *"All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment."*

The Adviser Agent's role in Paper A would be: given comment class, class-history statistics, and past LLM outputs, choose (i) which LLM to route the comment to (comment-class-aware portfolio selection — see essay 25 on Kerschke), (ii) at what temperature, (iii) with what prompt template. The role is empirical, not conceptual — it uses runtime information to steer the next call. Paper A's 25-27% headline is measured under the ablated regime «no Adviser». (Comparative inference)

---

## 4. Adapter pattern: heterogeneous LLMs behind unified interface

Paper B insists that heterogeneous algorithms are wrapped by adapters, exposing a unified interface to the coordinator. Paper A evaluates three LLMs separately (three columns in Fig. 5), never composing them.

> **Quote (Malek):** *"The inner representation of the candidate solution is the first thing we have to deal with during the algorithm unifying process. Such a representation is algorithm-specific. Dealing with various meta-heuristics, their different solution representations have to be mutually transformed. ... according to our abstraction, an algorithm takes the candidate solutions in phenotype representation on its input. It converts the solution into its inner representation–genotype. After processing, the solution is converted back to the phenotype representation and put on the output. This evolves chaining of any algorithms that can do the phenotype/genotype mapping."*

> **Quote (Gindullina et al.):** *"three models with different parameter sizes were selected: meta-llama/Llama-3.1-8B-Instruct ... meta-llama/Llama-3.3-70B-Instruct ... deepseek-ai/DeepSeek-V3.1"*

In Paper A's terms: phenotype = loss AST (algorithm-independent, PyTorch-compilable); genotype = the LLM's internal prompt+response space. Wrapping each LLM as an Adapter with `input(prompt, current_AST) → output(modified_AST)` allows chaining: DeepSeek proposes an edit, Llama-70B verifies it, an LLM-Semantic-Checker inspects it. Paper A has this structure implicit in its Customizer but does not expose it as an adapter interface, and does not compose multiple LLMs in a single chain. (Comparative inference)

---

## 5. Empirical validation: collaboration > individual

Paper B is empirical, not just architectural. On 10 TSP instances (eil51 to u574), GA + TS collaboration achieves better minimum values than either alone on 9/10 instances at identical compute budget.

> **Quote (Malek):** *"eil51: 426 (optimal), 478 (min GA), 430 (min TS), **428** (min GA+TS). berlin52: 7542 (optimal), 8261 (min GA), 8007 (min TS), **7544** (min GA+TS). ... We have got the best results by algorithm collaboration in most cases and we found the results promising for future work."*

> **Quote (Gindullina et al.):** *"The study revealed a strong correlation between framework effectiveness and language model scale. ... DeepSeek scores highest at 27%, Llama-3.3-70B is close at 25%, while Llama-3.1-8B drops significantly to 6%."*

Paper A's evaluation asks: which LLM is best? Paper B's evaluation asks: does collaboration beat any single algorithm? The two questions have different answers. Paper A implicitly assumes single-LLM selection is optimal (pick the best of three); Paper B's TSP evidence suggests that a two-LLM chain (e.g., Llama-70B proposes, DeepSeek verifies) might produce compliance rates above 27% *without* requiring a new base model — the same LLMs, different composition. (Comparative inference)

---

## 6. No Free Lunch: comment-class × LLM interaction is unexplored

Paper B motivates its collaboration approach via NFL: no single algorithm is best across all problem classes. Paper A does not run per-comment-class LLM comparison.

> **Quote (Malek):** *"According to the No Free Lunch Theorem the average solution quality provided by any meta-heuristic algorithm running on the set of all combinatorial optimization problems is statistically identical. In other words, for any algorithm, any elevated performance over one class of problems is exactly paid for in performance over another class. Simple implication can be done. To be able to achieve better results in more classes of problems, we should dispose of more algorithms."*

> **Quote (Gindullina et al.):** *"To empirically evaluate the impact of model scale on the quality of expert comment interpretation and the generation of correct loss functions, three models with different parameter sizes were selected"*

Paper A's «which LLM is best across all comments» is exactly the anti-NFL question. Reframing per NFL: for each comment class × subclass, which LLM (or LLM combination) is best? Paper A's Fig. 5 aggregates over comment classes; per-class breakdown would likely show that Llama-8B beats larger models on some subclasses (particularly simpler compile-only tasks) even though it loses in aggregate. This is directly related to essay 25 (Kerschke portfolio selection). (Comparative inference)

---

## 7. Meta-heuristic competition and diversity

Paper B's Future-work section introduces meta-heuristic competition and population diversity as coordination levers. Paper A has neither: no way for LLMs to «compete» on a comment, no way to ensure candidate modifications are diverse.

> **Quote (Malek):** *"Because of limited resources and possibly unlimited number of algorithm agents, we have to select which combination of meta-heuristics and in how many instances (algorithm agents) is employed for solving a given optimization problem. In this context a competition of algorithm agents is intended. ... The solution pool agent is responsible for providing candidate solutions to particular algorithm agent. It could maintain the population diverse enough by selecting candidate solution from the pool."*

> **Quote (Gindullina et al.):** *"a subset of instances (15–28%) where adapting the loss function did not yield a meaningful divergence from the original forecast"*

Paper A observes 15–28% «forecast unchanged» — a diversity failure in the LLM output distribution. Under Paper B's design, the SolutionPool would ensure that each new LLM call is prompted with previously-seen (comment, modification) pairs as *negative examples*, forcing diversity in the emitted modifications. This does not require new LLM capability; it requires shared state across LLM calls. (Speculative extension)

---

## 8. Comparison table

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Multi-agent architecture | Proposed as Future work, no design | 4-agent Aglobe (Problem/SolutionPool/Algorithm/Adviser) | Direct blueprint available (Comparative inference) |
| Coordination locus | Sequential LLM call, no shared state | SolutionPool as blackboard | State-sharing is the missing coordination (Comparative inference) |
| Parameter selection | Fixed T=1.0, single prompt | Adviser Agent based on runtime reports | Per-comment-class routing feasible (Comparative inference) |
| Composition of algorithms | Three LLMs evaluated separately | Adapter pattern → any-to-any chaining | Chain LLMs, don't pick best (Comparative inference) |
| Empirical collaboration | Not tested | 9/10 TSP wins over individual | Direct empirical precedent (Empirically shown for B) |
| Diversity mechanism | Temperature=1.0 (entropy) | Diversity-managed SolutionPool | Structured diversity, not stochastic (Comparative inference) |
| NFL framing | Aggregate «best LLM» question | Per-instance portfolio | Per-comment-class routing likely wins (Speculative extension) |

---

## Direction 1. Aglobe-style multi-agent LLM architecture for Expert-Guided PINN

**Pipeline stage.** §2.3 PINN Customizer + Future work multi-agent.  
**Mechanism.** Build the multi-agent Future-work extension with named components:
- **Problem Agent:** the Conversational Agent + classifier (existing).
- **SolutionPool Agent:** stores per-comment history — all LLM-emitted candidate modifications, their compile results, MAE scores, TRM/MQM rewards.
- **Algorithm Agents:** one wrapper per LLM (Llama-8B, Llama-70B, DeepSeek), plus a Semantic-Checker Agent (essay 21 AC1–AC3 tester), plus an Evaluator Agent (essay 20 TRM-style Bradley-Terry ranker).
- **Adviser Agent:** given comment class, past LLM performance on that class, and pool state, choose which LLM to route to and at what temperature; update from reports.
- **Coordination protocol:** per-comment cycle — Problem Agent → Adviser routes to k=4 LLMs → each emits modification → SolutionPool aggregates → Semantic-Checker and Evaluator score → Adviser learns → best modification retrained on PINN.

**Failure modes addressed.** Unspecified Future-work architecture; stateless LLM calls; 15–28% «forecast unchanged» diversity failures; single-LLM assumption; no learning from failures. (Speculative extension)

---

## Direction 2. Empirical validation: LLM collaboration > individual (Malek TSP analogue)

**Pipeline stage.** Evaluation — replicate Paper B's collaboration-vs-individual comparison for LLMs on Paper A's benchmark.  
**Mechanism.** Fix the 20 comments. For each: (i) individual runs — record each LLM's best-of-3 compliance rate; (ii) collaboration run — Llama-70B proposes k=4 modifications, DeepSeek-V3.1 verifies each (AC1–AC3 approximation), 8B tries the most disagreed-with candidate as a diversity injection; select best under Evaluator. Fix total LLM budget (e.g., 12 total calls per comment) so collaboration doesn't get a compute advantage.  
**Failure modes addressed.** Never-tested collaboration hypothesis; ambiguous framing of «which LLM is best» — reframed as «is collaboration better than any single LLM?»  
**Expected signal.** Direct analogue of Paper B's TSP result: collaboration ≥ individual on some plausible fraction of the 20 comments (Paper B saw 9/10 TSP; Paper A might see 12/20 or better). If < 10/20, that itself is publishable — «LLMs do not compose the way meta-heuristics do». (Speculative extension)

---

## Manuscript placement

- **§4 Future work — multi-agent architecture:** cite Malek 2009 (and MAGMA — Roli & Milano) as the design precedent; name the 4 agent types; specify SolutionPool + Adviser as the coordination layer.
- **§3.4 Discussion of Fig. 5:** reframe 6%/25%/27% not as a single best-LLM ranking but as evidence of per-instance LLM strength differences — motivate portfolio selection (cluster **1** LLM-as-optimizer of `dinara_comprehensive_review.md`; overlaps with essay 25 Kerschke).
- **§2.3 PINN Customizer:** describe the Adapter pattern implicit in the current design and make it explicit for future LLM swap.

## What not to transfer

Paper B is a 2009 specialization study on TSP with GA + TS meta-heuristics; do not import Aglobe-specific message-passing details (`init`, `getSolutions`, `putBestSolution`), TSP-specific benchmark instance names, or the memetic-algorithm literature. Do not treat LLMs as meta-heuristics — they operate on natural-language input, not on numeric feature vectors, and the phenotype/genotype abstraction requires adaptation. Do not claim NFL as a rigorous no-single-LLM-dominates theorem — NFL applies to search algorithms over problem-instance distributions, not to LLMs over natural-language distributions. And do not import the Adviser Agent as unconditionally superior: Paper B itself flags the Adviser as future work. (Comparative inference)

## Concrete next experiment

**Hypothesis.** On Paper A's 20 comments, a two-LLM collaboration (Llama-70B proposes k=4 modifications; DeepSeek-V3.1 evaluates + Semantic-Checker Agent rejects; final selection via Best-of-4 with Evaluator) will produce compliance rates above the best single LLM (27%) at fixed total-call budget.

**Protocol.**
1. Implement SolutionPool as an in-memory dictionary keyed by comment_id, storing per-comment history.
2. Implement Adviser as a simple portfolio-selection rule: on first call to a comment class, use Llama-70B; on retry, use DeepSeek-V3.1.
3. Implement Semantic-Checker Agent as essay 21 AC2a-approximation: revert the LLM's most-salient AST edit and check that forecast reverts.
4. Compare: individual Llama-70B (27%), individual DeepSeek (27%), collaboration (unknown).
5. Also record: (i) diversity of modifications per comment (Malek's fear); (ii) SolutionPool utilization (does history influence next call?); (iii) per-comment-class breakdown.

**Expected signal.** Collaboration compliance ≥ 32% (matching Paper B's TSP relative improvement); per-comment-class breakdown reveals LLM strengths (Llama-70B on Class 2, DeepSeek on Class 4, etc.).

**Ties to other directions.** Directly enables Direction 1 of essay 20 (Modification Quality Model as Evaluator Agent), Direction 1 of essay 21 (AC1–AC3 in Semantic-Checker Agent), Direction 1 of essay 25 (Kerschke per-instance LLM portfolio selection in Adviser Agent). (Speculative extension)

## Related essays in this series

- [`03_tonda_2013_bnsl_interaction.md`](03_tonda_2013_bnsl_interaction.md) — real-expert interactive loop; complementary human-in-the-loop coordination.
- [`19_wei_2024_dante_active_optimization.md`](19_wei_2024_dante_active_optimization.md) — DUCB acquisition — could be the Adviser Agent's scoring rule.
- [`20_zhang_2026_trm_complex_reasoning.md`](20_zhang_2026_trm_complex_reasoning.md) — TRM instantiates the Evaluator Agent.
- [`21_halpern_pearl_2005_causes_and_explanations.md`](21_halpern_pearl_2005_causes_and_explanations.md) — Semantic-Checker Agent could implement AC1–AC3 test.
- [`22_noy_2001_ontology_development_101.md`](22_noy_2001_ontology_development_101.md) — slot-and-facet ontology as the phenotype representation shared through SolutionPool.

## Conclusion

Paper B is a 2009 CTU specialization study on TSP with meta-heuristics; it predates Paper A's LLM concerns by 15 years. But its architectural template — Problem/SolutionPool/Algorithm/Adviser on Aglobe, phenotype/genotype adapter pattern, shared-blackboard collaboration, and NFL-motivated portfolio thinking — is precisely the design Paper A's Future-work section proposes without naming. Paper B's empirical result (collaboration wins 9/10 TSP instances) is the direct testable prediction for Paper A's LLM collaboration: two-LLM composition should beat any single LLM at fixed budget. The upgrade for Paper A is architectural clarity, not new algorithms. Naming the four agent types, exposing the adapter interface, adding a SolutionPool for state-sharing, and running the collaboration-vs-individual experiment turns Future work from proposal to first draft, using patterns that have a decade of empirical precedent in a directly analogous problem.
