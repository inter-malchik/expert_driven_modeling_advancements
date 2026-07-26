> **How to read this comparison**
>
> - **Paper A** denotes Gindullina et al. (Expert-Guided PINN); **Paper B** denotes the cited source paper.
> - Quoted passages are taken from the papers named in the comparison.
> - Interpretive links between papers are argued explicitly; they are not claims made by either author team.
> - Sections titled **Proposed direction** suggest possible follow-up work. They are engineering ideas, not reported results.


Dina Gindullina and co-authors' work (hereafter **Paper A**) introduces Expert-Guided PINN, a pipeline where an epidemiologist's comment passes through a conversational agent and a hierarchical classifier, after which a single LLM call generates an entirely new Python loss function for the PINN in one step. Zhongzhi Yu and co-authors' work, "Spec2RTL-Agent: Automated Hardware Code Generation from Complex Specifications Using LLM Agent Systems" (hereafter **Paper B**), solves the structurally identical task of translating unstructured natural language specifications into executable code—but is one technological step ahead. Instead of generating target code in a single pass, Spec2RTL-Agent processes implementations through three sequential representations (pseudocode → Python → C++) with verification at each stage, plus a dedicated adaptive reflection module that identifies the root cause of errors, rather than simply restarting generation when a compiler fails.

This makes Paper B a nearly direct solution to the main gap in Paper A. Gindullina et al. note that their LLM succeeds at syntactic tasks (code compilability reaches 80–100% after iterative correction) but fails at semantic ones: "Compliance with the comment"—the alignment of the generated modification with the expert's actual intent—hits only 25–27% for top-performing models and just 6% for Llama-3.1-8B. The "Future work" section of Paper A explicitly names the missing mechanisms: "class-subclass-specific modification templates" and an "LLM-loss-semantic-checker," but does not propose a concrete architecture to implement them. Paper B demonstrates a working prototype of exactly this architecture: intermediate, human-readable, verifiable code representations before final compilation, plus a module that tracks errors not as "the compiler crashed" but as "at which step, and why, the logic diverged from the specification."

Below, we break down exactly where the two systems share structural similarities, where Paper B is technically more mature at this same critical bottleneck, and what elements of the Spec2RTL-Agent architecture can be transferred to Gindullina's PINN Customizer without modifying its original domain.

---

## 1. Two "specification → executable code" systems: a structural parallel

Both papers address the same type of problem: converting an informal, lengthy, and partially unstructured input (an expert's comment / a NIST specification document) into formally correct executable code that controls a physical or computational process.

> **Quote (Gindullina et al.):** *«1. Conversational Agent, which helps the user formulate a comment suitable for forecast modification. 2. Hierarchical text classifier, which defines the class and subclass of an expert comment. 3. PINN Customizer, which is responsible for the core logic of the framework... 4. LLM that translates a comment into executable code for a loss function satisfying given constraints.»*

> **Quote (Yu et al.):** *«Spec2RTL-Agent operates in three critical stages: (1) Understanding, analyzing the specification to extract constraints and structure implementation plans... (2) Coding, progressively refining the implementation by first generating structured high-level code before transforming it into synthesizable C++ for High-Level Synthesis (HLS), and (3) Reflection, iteratively verifying, debugging, and refining intermediate outputs through an adaptive refinement mechanism to enhance robustness.»*

The parallel is almost verbatim: classifier + rules ≈ Understanding, PINN Customizer + LLM ≈ Coding, iterative correction ≈ (a stripped-down) Reflection. Yet Paper A condenses three stages of human engineering into a single code generation step, while Paper B explicitly models all three as separate, verifiable agent stages with their own inputs and outputs. This is not a terminological difference, but an architectural one—and it is this gap that drives the difference in the reliability of their results.

---

## 2. PINN Customizer as the "Single-Shot" approach: the very strategy Paper B deliberately rejects

A key observation: what Gindullina implemented as her core production pipeline, Yu et al. tested in their work as the *weakest baseline*—and demonstrated its clear inadequacy.

> **Quote (Gindullina et al.):** *«The module receives structured information as input: a comment created by an expert, its corresponding class and subclass, associated modification rules, and the source code of the PINN loss function. Based on this data, a detailed prompt for the LLM is generated, containing (Figure 2): The context of the forecast modification problem. Rules limiting the space of possible changes. The original loss function. Output data format requirements.»*

In other words: one prompt, all constraints included, and the LLM must produce a complete, final codebase in a single pass. This matches exactly the definition of the "Single-Shot" baseline from Paper B:

> **Quote (Yu et al.):** *«Single-Shot: The entire specification document is input into an LLM, which is tasked with generating the target RTL in a single attempt.»*

And the results of this baseline in Paper B's controlled experiment are unambiguous:

> **Quote (Yu et al.):** *«The Single-Shot approach, which directly prompts LLMs to generate implementations, failed in all three test cases, underscoring the complexity of the task.»*

Formally, the tasks are different (a 200+ line RTL module versus modifying a loss function of just a few lines), so the 0/3 failure rate for RTL does not translate directly to the 25–27% rate for PINN loss—but the qualitative conclusion holds: wherever "one-touch" generation has been tested in controlled comparisons with alternatives, it performs poorly. Paper A does not conduct such internal comparisons (it tests different LLMs with the same single-step architecture, never testing any other architecture), so it lacks its own data to distinguish how much of the missing 73–75% success rate stems from model weaknesses, and how much from the single-shot generation architecture itself.

---

## 3. Progressive coding: the missing link between rules and PyTorch code

The central technical contribution of Spec2RTL-Agent is not that generation is split into subfunctions (though that is also important), but that *every* subfunction is not implemented directly in the target language, but moves sequentially through layers of abstraction.

> **Quote (Yu et al.):** *«Inspired by the varying proficiency levels of LLMs in handling different programming languages, from high-level to low-level code, we leverage higher-level code as a reference to guide the generation of corresponding lower-level implementations. The process involves sequentially generating pseudocode, Python, and C++ code. For each sub-function, a Coder first drafts the code and a Verifier then assesses its accuracy, suggesting necessary revisions or a complete regeneration when needed.»*

In Gindullina's work, this layer is entirely absent: expert comment → class/subclass → rules from Table A.2 → directly to PyTorch code. There is no intermediate step where a human (or a second LLM) could read "what the system plans to do" before it becomes executable math. This is the very gap that her own error analysis highlights:

> **Quote (Gindullina et al.):** *«Incorrect interpretation and use of numerical parameters mentioned in comments.»*

And a specific documented case where the lack of a verifiable intermediate step led to a silent failure even after successful compilation:

> **Quote (Gindullina et al.):** *«the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days). This example illustrates that, in the absence of clear and interpretable modification rules, an LLM may generate a loss function whose use leads to inadequate forecasts.»*

If a step like "pseudocode: increase the penalty for violating $I(t)\to 0$ as $t\to T_{max}$ by a factor of X" existed between the "rules" and PyTorch code, the weakening of exactly that penalty (which caused the 700-day outbreak) would have been visible and verifiable *before* PINN training—just as in Paper B, the Verifier checks pseudocode and Python versions before errors can reach the C++ code that goes into HLS synthesis.

---

## 4. From compiler-triggered error handling to adaptive reflection: a fundamentally different model of failure

The error-handling mechanism in Paper A boils down to one rule: if the code fails to compile → send the interpreter's error message to the LLM → ask for corrections.

> **Quote (Gindullina et al.):** *«After generating the LLM candidate loss function, its automatic validation is performed... which includes: 1. Syntactic analysis – checking the code's compilability using the Python interpreter. 2. Iterative correction – if compilation errors are detected, the system automatically generates a clarifying request to LLM describing the error so that a corrected version can be regenerated.»*

This is a purely syntactic trigger: it does not activate if the code compiles but produces a physically nonsensical forecast (the 700-day epidemic compiled and trained without a single error). Paper B's Adaptive Reflection Module works entirely differently—it does not wait for a crash, but actively analyzes *where in the chain of reasoning* the problem arose, and selects one of four remediation strategies:

> **Quote (Yu et al.):** *«If the error originates from incorrect instructions, the agent redirects the issue to the iterative understanding and reasoning module to revise the instructions for the affected sub-function. If the error stems from previous sub-functions, the Reflection Agent returns to the identified sub-functions to make necessary revisions... If the error is confined to the current sub-function and unrelated to previous outputs, the Reflection Agent restarts the generation of this sub-function... If the error source remains unclear, the agent escalates the issue for human intervention.»*

The difference is fundamental: Gindullina's system only implements the last of these four branches in a truncated form ("regenerate the current step"), and even that only works when a clear crash occurs. Paper B includes a dedicated branch for the case "the error is not in the current code, but in the original instructions"—which is exactly what happened in the case of the incorrect peak shift: the LLM interpreted the rule "modify term2" in a way that was formally permitted by Table A.2, but semantically inconsistent with the expert's intent. Paper B's Reflection module would have reopened the question of the underlying instructions in this scenario, not just the code.

---

## 5. Ablation studies versus model comparisons: the measurement Paper A lacks

Gindullina compares three *different LLMs* with the same pipeline architecture (Llama-3.1-8B / Llama-3.3-70B / DeepSeek-V3.1), which allows assessment of model scale, but not of architecture. In contrast, Paper B fixes the model (GPT-4o for all agents) and varies *pipeline components*, which directly attributes the contribution of each module:

> **Quote (Yu et al.):** *«W/o Understand: This variation of our pipeline omits the iterative understanding and reasoning module... Naive Coding: This configuration removes the progressive coding and prompt optimization module... W/o Reflection: This configuration bypasses the adaptive reflection module.»*

> **Quote (Yu et al.):** *«removing the iterative understanding and reasoning module (W/o Understanding) led to a more than fourfold increase in human interventions, underscoring its importance in planning. Compared to W/o Reflection and Naive Coding, our full Spec2RTL-Agent reduced human interventions by 51.9% and 31.6%, and coding iterations by 47.8% and 31.0%, respectively.»*

Numerically (from the source's Table 1): human interventions fell from ~18.67 (W/o Understanding) to 9.00 (Naive Coding) → 6.33 (W/o Reflection) → 4.33 (full system), while correctness remained 3/3 for the final three configurations. This is exactly the type of controlled experiment missing from Paper A: it has no data to answer the question "how much does a modification template itself add to the success rate, independent of switching models?" The authors' own conclusion highlights this incompleteness:

> **Quote (Gindullina et al.):** *«These results should be considered proof-of-concept, demonstrating the potential of the approach but also highlighting the need to develop more stringent generation rules and control mechanisms to ensure the interpretability and reliability of the results.»*

These "more stringent... mechanisms" are named, but not measured in isolation—and this separate measurement is the key methodological contribution of Paper B's ablation section.

---

## 6. Semantic noise injection: a controlled version of manual "Compliance with the comment" evaluation

The "Compliance with the comment" criterion in Paper A is a qualitative, human-led visual assessment:

> **Quote (Gindullina et al.):** *«This is the primary criterion for assessing the technical success of the modification system. A comparative analysis is performed between the expert's text commentary and the visualization of the modified forecast.»*

This approach has no built-in stress test: it is unknown how resilient the pipeline is to subtle, non-breaking semantic errors that appear anywhere along the pipeline (like the 700-day outbreak case). Paper B conducts exactly this controlled experiment, intentionally introducing subtle semantic flaws at different pipeline stages:

> **Quote (Yu et al.):** *«Revise the generated implementation while introducing a subtle but impactful mistake. The mistake should not be a syntax error but rather a semantic flaw that could lead to functional misbehavior. Ensure that the revised implementation remains coherent and well-structured.»*

> **Quote (Yu et al.):** *«Spec2RTL-Agent demonstrates strong resilience, consistently generating correct implementations while maintaining stable efficiency in # Intervention and # Coding metrics. These results highlight the system's ability to recover from local inconsistencies and maintain high-quality output despite intentional perturbations.»*

Per the source's Table 3, correctness remained 3/3 when noise was injected at any of the four stages (Understanding, Pseudocode, Python, C++), and the number of human interventions only increased moderately (from 4.33 to 6.00 when noise was added at the Understanding stage). Paper A has no equivalent experiment: it is unknown how often Gindullina's pipeline would catch an intentionally hidden, "plausible" error—and this very class of bugs (compiles, looks plausible, but is physically incorrect) is its documented core weakness.

---

## 7. Pipeline stage comparison

| Pipeline Stage | Paper A (Gindullina et al.) | Paper B (Yu et al., Spec2RTL-Agent) |
|:--- |:--- |:--- |
| Input specification parsing | A conversational agent checks the comment for "concreteness, certainty, objectivity"; a hierarchical (BERT+ML) classifier assigns a class/subclass | Iterative Understanding and Reasoning Module: Summarization → Decomposition → Information Augmentation (Description Agent + Verifier) |
| Task decomposition | None: Table A.2 rules define which terms can be modified, but do not split the task into sub-steps | A Decomposer Agent breaks the target function into a sequence of implementable sub-functions |
| Code generation | A single LLM call: rules + original loss code + comment → full PyTorch code in one pass | Progressive Coding: pseudocode → Python → C++ for each sub-function, with a Coder + Verifier at each level |
| Prompt optimization | Fixed prompt template, does not change during operation | A Prompt Optimizer Agent revises prompts based on logs of failed attempts for the current sub-function |
| Error detection | Only code compilability (`Syntactic analysis`) | An Analysis Agent parses the full generation trace and identifies the likely source of the error |
| Error response | Iterative correction: compiler error text → regenerate the full function | Reflection Agent selects from 4 strategies: revise instructions / fix past sub-functions / regenerate current step / escalate to a human |
| Final conversion | Not required — PyTorch code is the final artifact | A Code Optimizer Agent adapts C++ to meet HLS tool requirements (Stratus HLS) → RTL |
| Result evaluation | Manual expert visual assessment ("Compliance with the comment"), no stress testing | Automated `Correct` metric + `# Intervention` + `# Coding`, including ablations and noise injection |
| Component attribution | None: whole LLMs are compared, not architectural variants | Full set of ablations (`W/o Understand`, `Naive Coding`, `W/o Reflection`) with separate performance metrics |

---

## 8. Comparative summary

| Criterion | Paper A (Gindullina et al.) | Paper B (Yu et al.) | Takeaway |
|:--- |:--- |:--- |:--- |
| Core codegen strategy | Single-shot prompt → full PyTorch loss | Progressive pseudocode → Python → C++ per sub-function | A implements B's failed baseline as production architecture |
| Intermediate verification | None before PINN retrain | Coder + Verifier at each abstraction level | Silent semantic failures (700-day outbreak) are structurally predictable |
| Error handling | Compiler traceback → regenerate | Four-branch Reflection Agent + human escalation | A lacks "reopen instructions" path when Table A.2 permits but semantics fail |
| Evaluation design | Three LLMs, same pipeline | Fixed GPT-4o; ablate Understanding / Coding / Reflection | A cannot attribute 73–75% failure to architecture vs. model |
| Stress testing | None on plausible wrong code | Injected semantic noise at four stages | B proves recovery from non-syntax flaws; A's primary weakness is untested |
| Named future work in A | "Modification templates", "LLM-loss-semantic-checker" | Working multi-agent prototype | B is an evaluated blueprint for A's §4 Future work |

Paper B's authors explicitly position progressive coding as a response to varying LLM proficiency across language levels. Paper A's PINN Customizer skips that ladder entirely and pays for it in compliance, not compilability.

---

## Proposed direction 1. Mandatory penalty-modification pseudocode before PyTorch

**Pipeline stage:** PINN Customizer (between classifier output and code generation).

**Mechanism:** Require a structured intermediate artifact—e.g., `TARGET_TERM: term2; OPERATION: increase post-peak $I(t)$ penalty; BOUNDARY_IMPACT: unchanged`—before any PyTorch is emitted, mirroring Paper B's pseudocode stage where higher-level code guides lower-level synthesis.

**Failure mode:** Weakened $I(T_{max})\to 0$ weight producing a >700-day outbreak while code still compiles.

---

## Proposed direction 2. Subclass Verifier agent before retraining

**Pipeline stage:** PINN Customizer (post-pseudocode, pre-PINN retrain).

**Mechanism:** Instantiate Paper B's Verifier pattern: a second LLM pass checks the planned modification against Table A.2, the expert comment, and epidemiological side-effects (e.g., "does weakening $L_{IC}$ conflict with requested post-peak decline?"); block retrain on failed verification.

**Failure mode:** Literal insertion of numeric parameters without semantic adaptation; unused penalty terms.

---

## Proposed direction 3. Adaptive Reflection mapped to Paper A's semantic-checker

**Pipeline stage:** PINN Customizer error loop (extend beyond syntax).

**Mechanism:** After forecast preview or rule mismatch, an Analysis Agent classifies error source as (i) misclassified comment, (ii) wrong Table A.2 rule application, (iii) local code bug, or (iv) escalate to expert—directly porting Yu et al.'s four Reflection branches to Gindullina's proposed "LLM-loss-semantic-checker."

**Failure mode:** Peak-shift comment interpreted as boundary-condition edit (Fig. 4 unsuccessful case).

---

## Proposed direction 4. Architecture ablations on a fixed LLM

**Pipeline stage:** Evaluation protocol (entire pipeline).

**Mechanism:** Fix one model (e.g., DeepSeek-V3.1) and run `W/o pseudocode`, `Naive single-shot`, `W/o Reflection` analogs, measuring Compliance with the comment and expert interventions—replicating Paper B's Table 1 design instead of only swapping model scale.

**Failure mode:** Inability to separate "bigger model" from "better pipeline" when reporting 25–27% headline success.

---

## Proposed direction 5. Semantic-noise injection in the evaluation suite

**Pipeline stage:** Evaluation / retraining loop (offline benchmark).

**Mechanism:** Deliberately corrupt intermediate outputs (mislabeled subclass, inverted penalty direction, subtle boundary tweak) and measure whether the full agent stack recovers—using Paper B's perturbation prompt as a template for stress-testing plausible-but-wrong loss edits before Smorodintsev-scale deployment.

**Failure mode:** Compilable, visually plausible forecasts that violate expert intent.

---

## Conclusion

Yu et al. do not merely share Paper A's problem domain (natural language → executable code); they run the controlled experiment Paper A omits. Spec2RTL-Agent treats single-shot generation as a baseline that fails, then shows—via ablations and semantic-noise injection—that progressive representations, per-stage verification, and adaptive reflection recover from errors that never trigger a compiler. Gindullina et al. already document those errors (700-day outbreaks, literal numerics, 25–27% compliance) and name the missing pieces (modification templates, semantic checker, multi-agent evaluators), but leave them unimplemented. The comparative thesis is therefore sharp: Paper A's PINN Customizer is architecturally equivalent to Paper B's weakest configuration, while Paper B supplies an evaluated migration path that preserves Paper A's epidemiological domain if transplanted stage by stage into the existing Conversational Agent → classifier → Customizer → retrain loop.
