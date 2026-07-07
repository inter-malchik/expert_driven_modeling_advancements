> **How to read this comparison**
>
> - **Paper A** denotes Gindullina et al. (Expert-Guided PINN); **Paper B** denotes the cited source paper.
> - Quoted passages are taken from the papers named in the comparison.
> - Interpretive links between papers are argued explicitly; they are not claims made by either author team.
> - Sections titled **Proposed direction** suggest possible follow-up work. They are engineering ideas, not reported results.


Paper A (Gindullina et al., "Expert-guided forecasting of epidemic ARI incidence based on physics-informed neural networks and large language models") builds an Expert-Guided PINN pipeline: an epidemiologist's comment passes through a dialogue agent and a hierarchical classifier, after which the PINN Customizer assembles a prompt with rules and passes it to an LLM that is expected to generate the entire Python code of the modified loss function in a single step. The authors already introduce an explicit ontology—four classes and subclasses of expert formulations (Appendix A)—and extract textual modification rules from it (Table A.2), but the final transition from those rules to executable code remains stochastic generation without an intermediate canonical representation.

Paper B (Gruber, 1993, "A Translation Approach to Portable Ontology Specifications") solves a structurally related problem thirty years earlier: how to translate an expressive declarative domain specification (an ontology in KIF) into restricted but executable target representations (Loom, Epikit, KEE, and others), preserving content while acknowledging the incompleteness of translation. The central mechanism is not "ask an agent to rewrite code," but a two-level translation architecture: idiom recognition → canonical form via the Frame Ontology → deterministic back-end translators. This makes Paper B almost a ready blueprint for what Paper A itself proposes in Future work but has not yet implemented: *class-subclass-specific modification templates* with explicit admissible operators and parameter ranges.

Below we show that Gindullina and co-authors built a **content ontology** layer (a hierarchy of comment classes) but skipped the **representation ontology** layer (a formal vocabulary of portable loss-modification idioms) and the compilation pipeline. That gap explains why Table A.2 does not constrain the LLM as intended, and why failures in Fig. 4b–c look like translation errors, not merely "hallucinations."

---

## 1. Two translation tasks: from an expressive source to a restricted target

Both papers formalize the transition from a rich, human-readable knowledge description to a narrow executable language on which the computational system actually runs.

> **Quote (Gindullina et al.):** *«The process begins with an expert's qualitative assessment of a forecast, which is translated into a structured specification for loss function modification. An LLM synthesizes this specification into executable code, which, after passing sanity checks, guides the PINN's training.»*

> **Quote (Gruber):** *«One problem is how to accommodate the stylistic and organizational differences among representations while preserving declarative content. Another is how to translate from a very expressive language into restricted languages, remaining system-independent while preserving the computational efficiency of implemented systems.»*

For Gruber, the source is KIF (full first-order predicate calculus); the target is specialized representation systems with *«restricted syntax and support limited reasoning over a restricted subset of full first order logic»*. For Gindullina, the source is natural language + class/subclass + Appendix A rules; the target is PyTorch code for composite loss $L = L_{data} + L_{IC} + L_{ODE}$. The difference is not in the domain, but in the **translation mechanism**: Gruber—idiom recognition and canonicalization; Gindullina—one-shot LLM with post-hoc compiler checks.

---

## 2. Ontology as a shared vocabulary and ontological commitments

Paper A calls the class hierarchy an "ontology" and uses it to narrow the space of admissible modifications:

> **Quote (Gindullina et al.):** *«Manually defining rules for all possible expert comments is infeasible, so we structure comments using a hierarchical ontology. It is based on four basic classes, identified through an analysis of typical expert statements»*.

Gruber provides the precise theoretical frame: an ontology is *«an explicit specification of a conceptualization»*, and a common ontology defines the vocabulary on which agents agree:

> **Quote (Gruber):** *«A common ontology defines the vocabulary with which queries and assertions are exchanged among agents.»*

> **Quote (Gruber):** *«Thus, a commitment to a common ontology is a guarantee of consistency, but not completeness, with respect to queries and assertions using the vocabulary defined in the ontology.»*

A practical parallel: expert confirmation of class/subclass in Paper A is a ritual of fixing **ontological commitment** before extracting rules from the knowledge base. But unlike Gruber, where class definitions such as `author` contain formal axioms (`value-cardinality`, `value-type`), class definitions 1–4 in Table A.2 remain at the level of natural language ("Add penalty to term2") without machine-readable constraints on operators and ranges—precisely what the authors of Paper A themselves acknowledge as insufficient.

---

## 3. Table A.2 versus Frame Ontology: soft rules and future templates

Paper A's current system is a set of free-form permissions:

| Class | Permitted Modifications (excerpt) | Constraints |
|:--- |:--- |:--- |
| 1 | Add penalty to term2 / term1 / term4 / term3 | Modification of other function components is **prohibited** |
| 4 | Add offset to desired peak day in term2 | Modification of other function components is **prohibited** |

The words *prohibited* and *Add penalty* enter the LLM prompt as text; they do not form a formal grammar of admissible AST changes. The authors state this directly:

> **Quote (Gindullina et al.):** *«The current system of rules for modifying loss functions lacks sufficient detail to provide meaningful control over the generation process.»*

> **Quote (Gindullina et al.):** *«The current rule system (Appendix A), based on specifying the target components of the loss function for modification, is insufficient to ensure semantic transparency and explainability of the changes made.»*

In Future work they propose replacing ad hoc penalties with **modification templates**:

> **Quote (Gindullina et al.):** *«We plan to replace the simple penalty additions by class-subclass-specific modification templates. These templates will explicitly define which loss components and parameters can be altered, which mathematical operators are admissible, and what numerical ranges are permitted.»*

Gruber's analogue was implemented thirty years ago as the **Frame Ontology**—an ontology of representational idioms that *«specifies, in a declarative form, the representation primitives»* and defines *«what can be translated»*:

> **Quote (Gruber):** *«The set of idioms that Ontolingua can recognize and translate is defined in an ontology, called the Frame Ontology.»*

> **Quote (Gruber):** *«Together, they constitute a purely declarative representational framework for describing hierarchies of classes with slots.»*

In other words: the *modification templates* from §4 of Paper A are a proposal for a dedicated Frame Ontology for PINN loss, but without an intermediate KIF-like layer and without a back-end translator to PyTorch; instead, the template is again left to free LLM generation.

---

## 4. The Ontolingua compilation pipeline versus the PINN Customizer

Gruber's architecture is explicitly modeled on a compiler:

> **Quote (Gruber):** *«Recognizing idioms and transforming them into canonical form are two of the front-end processes that Ontolingua performs when translating.»*

> **Quote (Gruber):** *«This architecture is analogous to a conventional programming language compiler, which parses source into an intermediate form that is then given to specialized code generation modules.»*

The front end normalizes many equivalent notations into a predictable canonical form; back-end translators expect a finite set of patterns—*«translators look for patterns of the form (range symbol) instead of all of the variants listed above»*.

The PINN Customizer in Paper A follows a different sequence (Fig. 1–2): *«loading a prompt template, loading rules for the expert comment class/subclass, sending a request to the LLM, getting the generated loss function, checking the compilability of the loss function»*. Generation **replaces** translation; the only automatic validator is Python syntax:

> **Quote (Gindullina et al.):** *«1. Syntactic analysis – checking the code's compilability using the Python interpreter. 2. Iterative correction – if compilation errors are detected, the system automatically generates a clarifying request to LLM describing the error so that a corrected version can be regenerated.»*

There is no stage of "recognize modification idiom → canonical template → deterministically generate code." Hence the gap between 80–100% compilability and 25–27% *«Compliance with the comment»*: a Gruber-style front end is missing, and the semantic back end (the proposed *«LLM-loss-semantic-checker»*) has not been built.

---

## 5. Honest incompleteness of translation

Gruber does not hide that translation into restricted languages is **inevitably incomplete**:

> **Quote (Gruber):** *«Because it translates into restricted languages, Ontolingua is inherently incomplete with respect to the KIF language.»*

> **Quote (Gruber):** *«When Ontolingua cannot translate a sentence into a target implementation, it issues an informative message. The practical consequence of not translating a sentence could be that the target system may be unable to enforce a constraint, or it may have to fall back on inefficient theorem proving.»*

> **Quote (Gruber):** *«The good news is that target systems can be customized or replaced without changing the ontology.»*

Paper A, by contrast, reports compilation success but not the semantic portability of the constraint. When the LLM *«reducing the influence of the zero boundary condition»* in response to a request to shift the peak (Fig. 4b), that is precisely the case where the target system (PINN) **failed to honor** the expert's intent despite formally valid code—an analogue of *«unable to enforce a constraint»*, but without an informative message at the translation stage. The authors themselves describe the failure:

> **Quote (Gindullina et al.):** *«This example illustrates that, in the absence of clear and interpretable modification rules, an LLM may generate a loss function whose use leads to inadequate forecasts.»*

In the ambiguous case (Fig. 4c), the modification *«may be effectively random rather than logically justified by epidemiological reasoning»*—a symptom of the absence of a canonical form between the comment and the loss weights.

---

## 6. One idiom, several targets: the lesson of the `author` definition

Gruber illustrates how **one** declarative specification yields **different** but consistent implementations. The class definition `author` with `value-cardinality` and `value-type` constraints translates into Epikit as a set of implications, into Loom as `:define-concept` with `:at-least` and `:same-as`, and into KEE as a frame with `Min.Cardinality` / `Max.Cardinality`. The key point: translation is **deterministic** via the idiom template, not reinvented by the model.

> **Quote (Gruber):** *«The Loom translation looks similar to the Ontolingua form, except that there are no free variables. The second-order relations such as value-type and value-cardinality were fashioned after the analogous operators in Loom derivatives such as:all and:at-least.»*

> **Quote (Gruber):** *«The existence of embedded procedural code in object-oriented systems such as KEE is one reason for maintaining ontologies in a more expressive, declarative language, and translating into the restricted languages.»*

A direct transfer to Paper A: subclass 4.1 ("Early/Late Peak") with permission *«Add offset to desired peak day in term2»* should yield **one** canonical template (term, shift type, admissible day range) from which the back end generates PyTorch—not allow the LLM to choose between "reduce the boundary condition" (Fig. 4b) and "increase BC weight by 4×" (Fig. 4c). Today both outcomes compile because there is no idiom layer between Table A.2 and the code.

The authors of Paper A themselves sketch this transition from procedural code to structure:

> **Quote (Gindullina et al.):** *«An LLM-loss-semantic-checker could verify alignment between the generated code and modification rules, reducing hallucinations.»*

In Gruber's terminology, a semantic checker is not "yet another LLM," but a **back end** that verifies generated code against the canonical idiom specification, as a compiler checks types against declarations.

---

## 7. Distinction from Kreikemeyer (essay 32): translation ontology, not grammar alone

Essay 01 (Kreikemeyer et al.) showed the power of **grammar-constrained decoding** for a formal DSL. Gruber adds a different layer: even without constrained decoding at the token level, one can first fix knowledge in a **system-independent** ontology, then translate to any back end (Loom today, another PINN framework tomorrow). For Expert-Guided PINN this means: modification templates should live **above** the choice of LLM (8B vs 70B vs DeepSeek), as KIF definitions in Ontolingua survive the switch from Loom to Epikit. GCD without an idiom ontology (as in Kreikemeyer) solves the syntax of the target language; the Ontolingua approach solves **semantic alignment** with the expert comment—precisely the failure of Paper A's primary metric.

---

## 8. Comparative table

| Criterion | Paper A (Expert-Guided PINN) | Paper B (Ontolingua) |
|:--- |:--- |:--- |
| Knowledge source | NL comment + class/subclass | KIF ontology definitions |
| Structuring layer | 4-class hierarchy (content ontology) | Frame Ontology (representation ontology) |
| Intermediate representation | None—straight to LLM prompt | Canonical form (ground axioms) |
| Transition to target | Stochastic one-shot LLM generation | Front-end idioms + back-end translators |
| Verification | Python compilability; iterative fix on compiler errors | Message for untranslatable sentences; partial knowledge acceptable |
| Back-end swap | Change LLM (8B / 70B / DeepSeek) without changing class ontology | *«target systems can be customized or replaced without changing the ontology»* |
| Status of "templates" | Proposed in Future work, not implemented | Implemented as Frame Ontology + translators (1993) |

---

## 9. Directions for the Gindullina team

**Direction 1. Introduce a Loss Modification Ontology modeled on the Frame Ontology.** For each class/subclass pair (Fig. A.6), specify not Table A.2 strings but declarative idioms: admissible term ($term2$), operator type (additive penalty / multiplicative weight / temporal offset), parameter range, prohibition on changing $L_{ODE}$. This directly implements their own Future work on *«which mathematical operators are admissible, and what numerical ranges are permitted»* and closes the failure mode of literal insertion of numbers from the comment.

**Direction 2. Split the PINN Customizer into front end and back end per Gruber's Fig. 2.** Front end: LLM or rule maps NL comment to a **canonical modification specification** (JSON/KIF-like record), not PyTorch code. Back end: deterministic code generator from canonical form (like Epikit/Loom translators). This reduces dependence on one-shot generation and differs from grammar-constrained decoding in Kreikemeyer (essay 32): here the source of truth is the idiom ontology, not the EBNF of the entire DSL.

**Direction 3. Semantic checker as a back-end validator of incompleteness.** Implement the proposed *«LLM-loss-semantic-checker»* not as a second free-form judge, but as a check: "canonical specification ⊨ class constraints" before retraining the PINN—by analogy with *«sentences in a tell-and-ask exchange can be checked for logical consistency with the definitions in ontologies»*.

**Direction 4. Preserve the content ontology when swapping LLMs.** Keep the four-class hierarchy and expert confirmation unchanged when replacing Llama/DeepSeek; change only the generation back end—following Gruber's principle that the ontology survives a change of target implementation.

---

## Summary

Paper A built a necessary but insufficient first layer—a **hierarchical ontology of expert comments** and a split-responsibility protocol. Paper B shows what is missing for portable, controlled translation of knowledge into code: a **representation ontology** (Frame Ontology → modification templates), a **canonical intermediate form**, and a **compiler architecture** with explicitly acknowledged incompleteness. As long as the PINN Customizer substitutes a generative model for a translator, Table A.2 remains documentation, not an executable contract—which shows up in 25–27% compliance and the catastrophic cases of Fig. 4b–c. Gruber (1993) is not historical curiosa, but a proven blueprint for the Future work that Gindullina et al. have already formulated but not yet implemented.

---
