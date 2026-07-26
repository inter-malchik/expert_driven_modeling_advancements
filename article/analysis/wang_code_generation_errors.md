> **How to read this comparison**
>
> - **Paper A** denotes Gindullina et al. (Expert-Guided PINN); **Paper B** denotes the cited source paper.
> - Quoted passages are taken from the papers named in the comparison.
> - Interpretive links between papers are argued explicitly; they are not claims made by either author team.
> - Sections titled **Proposed direction** suggest possible follow-up work. They are engineering ideas, not reported results.


Paper A (Gindullina et al., 2026) uses instruct LLMs to rewrite SIRD PINN loss functions from epidemiologist comments, validating outputs mainly through Python compilation and qualitative forecast review. Paper B (Wang et al., 2025, *Towards Understanding the Characteristics of Code Generation Errors Made by Large Language Models*) decomposes LLM codegen failures on HumanEval into thirteen semantic and fourteen syntactic characteristics, proving that most incorrect solutions compile and require multi-hunk repair.

The pairing is structurally tight: Paper A's PINN Customizer is a domain-specific instance of Paper B's problem — NL task description → executable code — with epidemiological stakes when silent semantic errors pass the Code Tester. Paper B supplies the taxonomy and repair methodology Paper A's *LLM-loss-semantic-checker* names but does not implement.

---

## 1. Same codegen problem, different application shell

Wang et al. study general Python functions from HumanEval; Gindullina et al. study one critical function family — composite epidemic loss code. Both depend on LLMs interpreting natural language precisely:

> **Quote (Wang et al.):** *"Semantic characteristics can help identify the high-level root causes of these code generation errors... Syntactic characteristics can help localize where the error occurs in an incorrect code solution."*

> **Quote (Gindullina):** *"a detailed prompt for the LLM is generated, containing (Figure 2): The context of the forecast modification problem. Rules limiting the space of possible changes. The original loss function. Output data format requirements."*

Paper A adds domain rules (Table A.2) Wang's benchmark lacks; Paper B shows rules alone do not prevent semantic failure at scale.

---

## 2. Compiler check is necessary but insufficient

Paper A's Code Tester:

> **Quote (Gindullina):** *"Syntactic analysis – checking the code's compilability using the Python interpreter. Iterative correction – if compilation errors are detected, the system automatically generates a clarifying request to LLM describing the error so that a corrected version can be regenerated."*

Wang et al.'s central empirical finding:

> **Quote (Wang et al.):** *"Interestingly, most of the incorrect code solutions are compilable and runnable without any compilation errors. Thus, we cannot easily capture these errors via compiler check."*

Paper A's *Compliance with the comment* at 6–27% despite high compile rates after correction is exactly this gap: syntax satisfied, epidemiological semantics not.

---

## 3. Garbage Code and unused loss terms

Paper A lists a systematic symptom:

> **Quote (Gindullina):** *"Adding unused variables and constant terms."*

Wang et al. formalize it:

> **Quote (Wang et al.):** *"Garbage Code is defined as unnecessary or irrelevant code that does not contribute to the intended functionality."*

Smaller models produce more *meaningless code snippets*; larger models shift toward subtler errors. Paper A's Llama-8B vs 70B split — 50% first-try compile failure vs stronger semantics but still 25–27% compliance — fits B's size–error-profile pattern.

---

## 4. Constant Value Error and literal expert numerics

Paper A on numeric comments:

> **Quote (Gindullina):** *"There is a systematic problem with interpreting numerical values in expert comments. In particular, the meta-llama/Llama-3.3-70B-Instruct model exhibits a tendency to literally include these numerical parameters in the loss function without sufficient semantic adaptation."*

Wang et al.:

> **Quote (Wang et al.):** *"Constant Value Error is an error that occurs when an incorrect constant value is set, which can occur in function arguments, assignments, or other parts of the code."*

B notes larger models make more constant-value mistakes while avoiding garbage snippets — mirroring Llama-70B's literal "10" insertion behavior in Paper A. Valid syntax hides wrong epidemiological binding.

---

## 5. Multi-hunk errors vs. interpreter-log repair loop

Wang et al. on repair effort:

> **Quote (Wang et al.):** *"84.21% of the incorrectly generated code has Levenshtein distance scores above 50 edits, with 52.63% of them requiring more than 200 edits."*

> **Quote (Wang et al.):** *"Overall, the majority of errors are single-hunk or multi-hunk errors, which require substantial effort to repair compared with single-line errors."*

Paper A returns raw interpreter errors to the LLM. Wang shows such coarse feedback is mismatched to error scale — especially for *wrong (logical) direction* mapped to whole *incorrect code blocks*. PINN loss edits that reshape epidemic dynamics are multi-hunk by nature.

---

## 6. Partial vs. complete failure — dual repair strategy

Wang distinguish tasks failing some tests vs. all tests. Paper A's Fig. 4 spectrum — successful reshape, catastrophic 700-day outbreak, ambiguous flat curve — parallels partial vs. complete semantic failure on the **epidemiological test** (forecast plausibility) rather than HumanEval unit tests.

> **Quote (Wang et al.):** *"These subtle error characteristics in partially failed tasks, likely due to missed conditions, may be fixable with traditional automated program repair techniques."*

A loss that trains but violates boundary intent (700-day case) may need local condition repair; NaN or flatline collapses may need full regeneration — Wang's Finding 5/6 pattern applied to PINN outcomes.

---

## 7. Taxonomy-labeled repair prompts improve GPT-4 fixes

Wang et al. propose taxonomy-guided agents:

> **Quote (Wang et al.):** *"one can first train a machine learning model to predict the types of errors. Then, the predicted errors can then be encoded in the prompt to guide the repair agent. For instance, instead of prompting the repair agent with "fix the bug at Line 6," one can prompt the agent with "fix the incorrect function arguments at Line 6," which may lead to a more accurate patch."*

On BigCodeBench-Hard, labeled prompts raised GPT-4 repairs from 3 to 12 of 84 incorrect solutions vs. unlabeled baselines. Paper A's proposed semantic checker is the epidemiology-specific version of this classifier→prompt pipeline.

---

## 8. Task complexity gating before generation

Wang link error rates to prompt length and solution complexity. Paper A does not score comment difficulty before invoking the LLM. A Conversational Agent extension could decompose complex expert requests — matching Paper A's own observation that multi-part comments stress models — before PINN Customizer invocation.

| Criterion | Paper A (Gindullina et al.) | Paper B (Wang et al.) | Takeaway |
|:--- |:--- |:--- |:--- |
| Validation | Python compiler + plot review | Semantic + syntactic taxonomy | A catches minority of errors |
| Silent failures | 700-day / ambiguous curves | ≥82% wrong code compiles | Same structural blind spot |
| Numeric bugs | Literal parameter insertion | Constant Value Error class | Shared large-model pathology |
| Repair loop | Interpreter message → LLM | Taxonomy-labeled repair prompts | B shows 4× gain on hard set |
| Metrics | MAE gates, TSED on code | Levenshtein, CodeBERTScore | Text distance ≠ epidemic semantics |

---

## 9. Semantic–syntactic mapping for PINN Customizer

Wang's Sankey mappings pair root causes to locations — e.g., *wrong (logical) direction* with *incorrect code block*. Paper A's modification rules specify **which term*** may change but not diagnostic mapping when compliance fails. Encoding Wang's matrix for loss-function edits would let iterative correction target "incorrect condition on term2 boundary weight" instead of generic compile logs.

---

## Proposed direction 1. Semantic error classifier before PINN retraining

**Pipeline stage:** Code Tester (extend beyond syntax).

**Mechanism:** Classify generated loss against Wang taxonomy + epidemic rule table; block retrain on Garbage Code / Wrong logical direction.

**Failure mode:** Compilable loss producing unphysical forecasts.

---

## Proposed direction 2. Taxonomy-guided iterative correction

**Pipeline stage:** PINN Customizer repair loop.

**Mechanism:** Map failure to semantic+syntactic label; prompt LLM with "fix Constant Value Error in term3 weight at line N."

**Failure mode:** Raw interpreter logs failing on multi-hunk loss edits.

---

## Proposed direction 3. Dual-mode repair (local vs. full regeneration)

**Pipeline stage:** PINN Customizer after short PINN probe train.

**Mechanism:** Partial epidemic-logic failure → localized APR-style patch; complete collapse → regenerate at lower temperature.

**Failure mode:** 700-day partial semantic failure vs. total breakdown.

---

## Proposed direction 4. Comment complexity gate in Conversational Agent

**Pipeline stage:** Conversational Agent / classifier entry.

**Mechanism:** Estimate AST-edit complexity of proposed modification; split overloaded comments.

**Failure mode:** Multi-clause expert requests correlating with Garbage Code.

---

## Proposed direction 5. TSED + Wang metrics for evaluation reporting

**Pipeline stage:** Evaluation / benchmarking.

**Mechanism:** Report CodeBERTScore and hunk-type distributions alongside compliance and MAE.

**Failure mode:** Subjective compliance without codegen-quality traceability.

---

## Conclusion

Wang et al. explain **why** Paper A's compiler-centric pipeline under-reports LLM failure: semantic epidemiological violations present as compilable, often multi-hunk *Constant Value*, *Garbage Code*, and *wrong logical direction* errors. Their taxonomy and labeled-repair evidence are a direct blueprint for Paper A's *LLM-loss-semantic-checker* — moving Expert-Guided PINN from blind prompt iteration to directed automated repair on differential-equation code.
