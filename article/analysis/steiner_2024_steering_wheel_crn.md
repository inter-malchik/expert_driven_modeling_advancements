> **Paper B — live link:** [https://doi.org/10.1038/s41467-024-47997-9](https://doi.org/10.1038/s41467-024-47997-9)  
> **Source in `src/`:** [`../src/2024 A human-machine interface for automatic exploration of chemical reaction networks.md`](../src/2024%20A%20human-machine%20interface%20for%20automatic%20exploration%20of%20chemical%20reaction%20networks.md)

Gindullina et al. (hereafter **Paper A**) open an epidemiologist’s free-text comment into a largely unstructured conversational loop, then collapse it—via classifier and Table A.2 rules—into a single LLM rewrite of the entire SIRD PINN loss. Compile check is the only automatic gate; the expert’s success/failure/ambiguous verdict never re-enters the model. Primary “Compliance with the comment” remains 25%/27%/6% (70B / DeepSeek / 8B). The Conversational Agent itself is not quantitatively evaluated; Future work names templates and multi-agent checkers but not a reproducible *protocol language* for steering search.

Steiner and Reiher (2024; hereafter **Paper B**) face an analogous combinatorial explosion—chemical reaction networks too large for brute force, yet too uncertain for freezing all intermediates a priori. Their answer is the **STEERING WHEEL**: alternating Network Expansion and Selection steps, assembled as an on-the-fly keyword protocol (Association, Dissociation, Rearrangement, motif/energy filters), executed only after each step completes so the campaign remains reproducible and publishable (Zenodo protocols + container; ~76k reaction trials → ~78k structures). Across Wilkinson, Ziegler–Natta, Monsanto, and Ga/silica cases, experts steered without listing every intermediate, and still recovered known cycles plus new paths.

Paper B therefore contributes what Paper A’s open NL→loss loop lacks: an auditable HITL protocol in which human guidance is typed, sequential, and replayable—mapping naturally onto replacing ad hoc loss rewrites with named expansion/selection operations over loss-edit space. The transferable thesis: **Expert-Guided PINN should become a STEERING WHEEL over loss edits, not a chat that occasionally emits a compilable objective.**

---

## 1. Open conversation vs linear steering protocol

Paper A’s interaction is free text plus class confirmation; the path from comment to loss edit is not a publishable step list. Paper B treats operator input as protocol construction.

> **Quote (Gindullina et al.):** *"The expert starts the forecasting procedure and evaluates the model’s forecast by inspecting the plots. If the forecast is unsatisfactory, the expert enters a textual comment in the \"Instructions for the model\" field."*

> **Quote (Steiner & Reiher):** *"The steering protocol therefore consists of two alternating exploration steps: Network Expansion Step and Selection Step."*

The structural claim: Expert-Guided PINN needs an explicit Expansion/Selection vocabulary for *loss-edit campaigns*, not only a chatbot that validates concreteness. Without that vocabulary, every “successful” run remains a non-replayable anecdote. (Comparative inference)

---

## 2. Steer without freezing all intermediates

Paper A’s Table A.2 and planned templates risk over-specifying *which* loss components move. Paper B’s design principle is the opposite of full predefinition: guide without listing every node.

> **Quote (Steiner & Reiher):** *"one does not want to limit mechanistic studies by preselecting all reaction intermediates, which brings inherent biases and constraints."*

> **Quote (Gindullina et al.):** *"These templates will explicitly define which loss components and parameters can be altered, which mathematical operators are admissible, and what numerical ranges are permitted."*

Templates remain necessary for Paper A’s LLM safety, but STEERING WHEEL shows a middle path: restrict *operations and foci* (Selection), allow discovery of unexpected phenotypes (Expansion)—as when Monsanto path B (second methanol association) appeared without being encoded upfront. Paper A currently gets “unexpected” edits mostly as failures (literal numbers, dead code, 700-day BC), not as guided discoveries. (Comparative inference)

---

## 3. Keywords as a DSL for expert control

Paper B’s protocol is built from chemically meaningful keywords the operator can compose; Paper A’s “rules” remain prose attached to a free rewrite.

> **Quote (Steiner & Reiher):** *"This steering protocol is assembled in terms of keywords – such as \"Dissociation\" to initiate the search for specific dissociation reactions – by a human operator on the fly."*

> **Quote (Steiner & Reiher):** *"This protocol therefore supports easy processing and may easily be generated from written form into spoken language."*

> **Quote (Gindullina et al.):** *"The module receives structured information as input: a comment created by an expert, its corresponding class and subclass, associated modification rules, and the source code of the PINN loss function."*

If class/subclass selected “Peak late” and the next Expansion were a typed operator (`ShiftPeakOffset`, `ReweightBC`, `AddTerm2Penalty`) under Selection filters (allowed terms, numeric bounds), the Conversational Agent could emit protocol steps instead of unconstrained NL for the Customizer. (Comparative inference)

---

## 4. Reproducibility: complete each step before the next

Paper A runs temperature 1.0 “to achieve maximum variation,” then plans lower temperature for production. Paper B forbids advancing while prior calculations are incomplete—because partial completion makes campaigns non-reproducible. That is a stronger discipline than “set T=0 later”: it is a *workflow invariant*.

> **Quote (Steiner & Reiher):** *"While such intuitive interactions with a running exploration allow for flexible workflows, they harbor the danger of producing non-reproducible mechanism exploration campaigns."*

> **Quote (Steiner & Reiher):** *"we designed our framework in such a way that it ensures reproducibility by requiring every step of the created exploration protocol to be completed, i.e., every calculation set up must be finished, before any further manipulations of the network are permitted."*

> **Quote (Gindullina et al.):** *"All LLMs were set to a temperature of 1.0 to achieve maximum variation in results even when entering the same comment."*

Paper A’s compliance numbers are therefore hard to audit as a *campaign*. A STEERING-WHEEL discipline—log protocol steps, freeze seeds, finish retrain+checks before the next Expansion—would make Expert-Guided PINN runs citeable the way Zenodo protocols are. (Comparative inference)

---

## 5. Compile-only vs preview-before-commit

Paper A trains once code compiles; Fig. 4b’s 700-day epidemic is a post-hoc discovery. Paper B’s HERON interface *previews* how many calculations an Expansion would launch and which reactive sites are involved before the operator commits. Preview is the missing pre-train semantic gate.

> **Quote (Steiner & Reiher):** *"The graphical user interface displays how a potential next Network Expansion Step would affect the exploration by presenting the number of calculations set up for the expansion, alongside with the constructed reactive complexes and their reactive sites."*

> **Quote (Steiner & Reiher):** *"Together with the existing average runtime information available in HERON, the computing time for the step can be estimated."*

> **Quote (Gindullina et al.):** *"the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days). This example illustrates that, in the absence of clear and interpretable modification rules, an LLM may generate a loss function whose use leads to inadequate forecasts."*

A Customizer “preview” of proposed AST edits (which weights change, which BCs weaken) before retrain is the direct transfer of Expansion preview—exactly where Paper A’s LLM-loss-semantic-checker should sit. (Comparative inference)

---

## 6. Later Expansion can revisit early choices

Paper A’s one-shot rewrite has no typed “reopen BC weight” step after an ambiguous result; the expert can only comment again in free text. Paper B stresses that early Expansions do not permanently freeze the network.

> **Quote (Steiner & Reiher):** *"any Expansion Step can be applied on the whole CRN at any point in the protocol, meaning that any part of an explored mechanism can be studied in more detail later on with additional calculations."*

> **Quote (Gindullina et al.):** *"Ambiguous result. The expert’s requirements are formally satisfied, but the result is questionable (for example, the curve looks unrealistic)."*

Ambiguous Fig. 4c outcomes need a protocol verb (“undo BC×4; try Term2 growth penalty”) rather than another opaque full rewrite. (Comparative inference)

---

## 7. Exhaustive option remains available

Paper B’s steering does not permanently amputate search power: any step can later go toward exhaustive reactive-site pairing. Paper A’s compile-only loop has no analogous “widen Selection” control—only another free comment.

> **Quote (Steiner & Reiher):** *"While the framework allows for efficient explorations based on human input, each exploration step and therefore the complete network can be pushed towards exhaustive exploration (i.e., considering any pair of atoms of any nodes of the reaction network as reactive) at any point in the workflow."*

> **Quote (Gindullina et al.):** *"A promising direction is to evolve the system toward a multi-agent architecture, where specialized LLMs enhance autonomy and objectivity. An LLM-expert-evaluator could quantify forecast compliance with the original comment… An LLM-loss-semantic-checker could verify alignment between the generated code and modification rules, reducing hallucinations."*

Checkers without a widen/narrow Selection vocabulary still operate inside one opaque rewrite; STEERING WHEEL shows how human autonomy and machine autonomy share a common step API. (Comparative inference)

---

## 8. Pipeline mapping

| Criterion | Paper A | Paper B | Takeaway |
| :--- | :--- | :--- | :--- |
| Human control medium | Free-text comment + class confirm | Keyword Expansion/Selection protocol | Protocol > open chat for audit (Comparative inference) |
| Search restriction | Table A.2 / planned templates | Selection steps + filters without listing all intermediates | Steer foci, don’t freeze all nodes (Author-stated) |
| Reproducibility | T=1.0 exploratory runs; verdict not fed back | Step must finish; protocols + container on Zenodo | Publishable campaigns (Empirically shown) |
| Pre-commit visibility | Compile check only | Expansion preview (counts, sites, cost) | Preview AST edits before retrain (Comparative inference) |
| Failure mode | Literal numbers; unused code; 700-day BC edit | Wrong ESM / missing solvent can miss paths—protocol re-run with DFT | Named re-Expansion after diagnosed miss (Author-stated) |
| Conversational layer | Agent validates comment quality; not scored | GUI + linear protocol; operator decisions logged | Score Agent by protocol fidelity, not chat fluency (Comparative inference) |
| Discovery under guidance | Single rewrite; unexpected BC edits often *bad* | Guided search still found new Monsanto / Ga paths | Good steering preserves serendipity (Empirically shown) |

---

## 9. Publishing the campaign, not only the forecast plot

Paper B deposits protocols and containers so others can replay steered explorations. Paper A shares architecture and aggregate percentages, but a given comment→loss path is not a citeable artifact.

> **Quote (Steiner & Reiher):** *"Therefore, all explorations presented in this study are easily reproducible with the provided container and protocols deposited on Zenodo, where also the resulting calculations (in total 76,000 reaction trials yielding 78,000 chemical structures) are stored in a MongoDB framework."*

> **Quote (Gindullina et al.):** *"Fig. 3. (a) Comparative Performance of LLMs in loss function generation tasks (temperature=1.0, 20 launches)"*

Twenty launches at T=1.0 measure stochasticity; they do not yield a protocol another institute can re-run after changing one Selection filter. Expert-Guided PINN’s Smorodintsev validation would benefit from STEERING-WHEEL-style protocol deposits per expert session. Crucially, Paper B’s steered Monsanto/Ga runs still found *new* paths under keyword guidance, whereas Paper A’s “novel” loss edits are often uninterpretable relative to the comment (BC×4 for “grow two more weeks”). Steering should raise interpretable novelty, not random novelty that happens to compile. (Comparative inference)

> **Quote (Steiner & Reiher):** *"The two findings, the catalyst degrading mechanism and the alternative paths in the catalytic cycle, highlight how an automated and systematic, yet guidable, algorithm allows one to study complex reaction mechanisms in great detail."*

> **Quote (Gindullina et al.):** *"This example highlights a limitation of using LLMs without additional control mechanisms: modifications to the loss function may be effectively random rather than logically justified by epidemiological reasoning."*

---

## Direction 1. Replace ad hoc NL→loss with Expansion/Selection protocol steps

**Pipeline stage:** Conversational Agent + PINN Customizer (and evaluation logging).  
**Mechanism:** Map class/subclass to a menu of typed Expansion operators (e.g. `AddCompartmentPenalty`, `ShiftPeakOffset`, `ReweightTerminalBC`) and Selection filters (admissible terms, numeric ranges, epidemic-logic invariants). The Agent outputs a *protocol draft*; Customizer executes one Expansion at a time with AST preview and semantic checker; only after compile+logic+preview gates does retrain run; the next step waits for completion (STEERING WHEEL reproducibility rule).  
**Failure modes addressed:** unreviewed Conversational Agent; compile-pass semantic disasters (700-day outbreak); unreproducible T=1.0 campaigns; inability to surgically undo bad BC edits without another free-text rewrite.  
**Artifact:** deposit each session’s protocol list alongside the final forecast plot. (Speculative extension)

---

## Direction 2. Evaluation: score the Conversational Agent by protocol fidelity

**Pipeline stage:** Conversational Agent (currently unscored) + logging.  
**Mechanism:** Treat Agent success as (i) producing a well-formed Expansion/Selection draft, (ii) matching expert-confirmed class/subclass to allowed operator menus, (iii) refusing comments that cannot map to any operator—rather than only “concreteness/certainty/objectivity” of free text.  
**Failure modes addressed:** unevaluated Agent component; comments that compile into semantically random loss edits; missing audit trail for ambiguous Fig. 4c outcomes.  
**Metric sketch:** protocol-valid drafts / total comments; mean steps-to-accepted-forecast. (Speculative extension)

---

Among HITL orphans, STEERING WHEEL is the strongest reproducibility blueprint: keyword protocols, completion barriers, and deposited campaigns—exactly the audit surface Expert-Guided PINN’s conversational loop currently lacks.

---

## Manuscript placement

- **Introduction (HITL framing) + Future work:** reposition Expert-Guided PINN as a *steered* loss-space explorer (cluster **8** interactive ML), not only “LLM writes loss.”
- **§2.1 Conversational Agent + §2.3 Customizer:** cite Expansion/Selection + completion barrier as the missing evaluation surface for the unevaluated Agent (cluster **2** agent patterns secondary).
- **Limitations / reproducibility:** protocol deposits vs “data on request” + T=1.0 scatter (cluster **10** governance transparency).

## What not to transfer

Do not import Chemoton chemistry operators, GFN2-xTB/DFT refinement stacks, or MongoDB CRN stores as epidemiological requirements. Paper B has no LLM and no PINN. Transfer **protocol shape** (typed Expansion/Selection, finish-before-next, depositable session log)—not reaction-network search heuristics. (Comparative inference)

## Concrete next experiment

**Hypothesis.** Replacing free-text→single loss rewrite with a fixed 5-step SIRD steering protocol raises protocol-valid sessions and cuts Fig. 4b-style BC disasters at equal LLM.

**Example protocol (one comment: “sharper post-peak decline”):**
1. **Select** subclass Peak/Decline; lock admissible terms `{L_ODE.I, L_data.I}`.
2. **Expand** `AddPenalty(postpeak_slope_I, range)`.
3. **Preview** AST diff + expected qualitative effect (no retrain).
4. **Gate** compile + non-negativity/monotonicity check.
5. **Execute** continue-train; only then allow next Expansion.

**Metric.** *Protocol fidelity* = fraction of sessions whose Agent output maps 1:1 onto menu operators; *unsafe edit rate* = BC/IC weight flips absent from protocol; secondary = Compliance / Zone A. Expect fidelity ≫ baseline Agent (today unscored) and lower 700-day pathologies. (Speculative extension)

## Related essays in this series

- [`03_tonda_2013_bnsl_interaction.md`](03_tonda_2013_bnsl_interaction.md) — Forced/Forbidden + latency.
- [`01_hidalgo_2018_glucose_grammatical_evolution.md`](01_hidalgo_2018_glucose_grammatical_evolution.md) — typed operators as grammar.
- [`06_hayes_2017_policy_explanation.md`](06_hayes_2017_policy_explanation.md) — post-edit “What will you do” before step 5.
- Bridge: [`../dinara_analysis/04_moeltner_lab_in_the_loop.md`](../dinara_analysis/04_moeltner_lab_in_the_loop.md) — trajectory validation beyond compile.

## Conclusion

STEERING WHEEL is the HITL blueprint Paper A’s conversational loop is missing: expert control expressed as alternating expansion and selection keywords, completeable and replayable, without requiring a full a priori inventory of intermediates. Transplanted to Expert-Guided PINN, that means treating loss modification as a steered exploration over edit space—auditable protocol steps with previews—rather than a single opaque NL→code leap. Templates and LLM checkers remain necessary; without a protocol discipline like Steiner and Reiher’s, they still float inside an unreproducible chat. The Q1 framing follows: Expert-Guided PINN is a domain-specific steering wheel over loss space, not “the first NL→objective system.”
