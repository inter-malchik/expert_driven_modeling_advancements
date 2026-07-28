### Cards Handover (Sources & Evidence)

This handoff gives everything a developer needs to continue adding and maintaining the “Sources & Evidence” sections for expert commentary cards. It aligns with the project’s methodology focus: every card’s title and body must be traceable to verbatim, verifiable sources (preferably local transcriptions in `article/transcriptions`).

---

#### 1) Purpose and scope
- Raise methodological rigor of cards by: (a) stating claims precisely, (b) linking each to verbatim English quotes, (c) pointing to exact Section/Figure/Equation markers.
- Do NOT add external links unless explicitly approved. Priority source is local transcriptions under `article/transcriptions`.
- Keep all formatting and file layout consistent with the existing repository patterns.

Definition of Done (DoD) for a card:
- The card file in `article/commentaries_data/**/nXX.md` contains a “Sources & Evidence” section.
- For each claim in the card’s title/body, there is:
  - a short one-line claim;
  - an “Evidence:” line naming the source and locator (Section/Figure/Equation/lines);
  - 1–3 verbatim English quotes (copy-paste from the local transcription) that directly justify the claim.
- No speculative or unreferenced assertions remain in the title/body. If something is a comparative inference, label it accordingly in the card’s metadata/body.

---

#### 2) Where everything lives
- Cards (markdown):
  - `article/commentaries_data/1_introduction/nX.md`
  - `article/commentaries_data/2_1_conversational_agent/nX.md`
  - `article/commentaries_data/2_2_hierarchical_text_classifier/nX.md`
  - `article/commentaries_data/2_3_pinn_customizer/nX.md`
  - `article/commentaries_data/2_4_evaluation_approach/nX.md`
  - `article/commentaries_data/2_methodology/nX.md`
  - `article/commentaries_data/3_2_code_correctness/nX.md`
  - `article/commentaries_data/3_3_working_with_the_framework/nX.md`
  - `article/commentaries_data/3_4_framework_performance/nX.md`
  - `article/commentaries_data/4_limitations_and_future_work/nX.md`
  - `article/commentaries_data/5_conclusion/nX.md`

- Sources (transcriptions, primary evidence):
  - `article/transcriptions/*.md` (use only local files unless the owner explicitly approves external documents).

- Analyses (context, not mandatory for S&E):
  - `article/analysis/*.md` (e.g., `rathore_2024_loss_landscape.md`, `yu_2025_spec2rtl_agent.md`, etc.).

---

#### 3) Required structure inside a card
Append or update a section like this (verbatim quotes must be in English):

```
## Sources & Evidence

This section maps the card’s claims to verbatim citations (English) from local transcriptions.

1) Claim: "<precise, minimal claim>"
   - Evidence: <Author, Year>, <Section / Figure / Equation / lines in the local transcription file>
   - Quotes (verbatim):
     > "… exact copied sentence 1 …"
     > "… exact copied sentence 2 …"  (optional)

2) Claim: "<another precise claim>"
   - Evidence: <Author, Year>, <locator>
   - Quotes (verbatim):
     > "…"
```

Notes:
- Do not paraphrase inside the quote block. Keep quotes short (1–3 lines).
- If a claim is an inference drawn from multiple sources, split it into atomic claims and attach quotes to each atomic part.
- If something remains a hypothesis, label it “Speculative extension” or “Comparative inference” in the body.

---

#### 4) Allowed sources and locators
- Primary: `article/transcriptions/*.md` (OCR/hand transcriptions of papers). Use Section/Subsection titles, Figure/Table numbers, or Equation numbers; if not available, mention “lines ~XX–YY”.
- Secondary (only if present locally): `article/analysis/*.md` for contextual alignment, but still prefer direct quotes from the transcription.

Forbidden without prior approval:
- Pulling quotes from the open web.
- Adding external URLs that are not already in the repo.

---

#### 5) Editing workflow (step-by-step)
1) Open the target card file `article/commentaries_data/**/nXX.md`.
2) Read the existing title/body. Extract 2–6 discrete claims actually asserted.
3) Search `article/transcriptions` for the relevant paper(s) backing each claim.
4) For each claim, locate exact supporting sentences. Copy them verbatim (English) and add them under “Quotes (verbatim)”. Add “Evidence:” with Section/Figure/Equation/lines.
5) If the body uses language that goes beyond what is quoted, either:
   - add the additional supporting quotes; or
   - reword the body to strictly match the evidence; or
   - label clearly as “Comparative inference” or “Speculative extension”.
6) Save the card. If the card cites analysis pages, ensure `filenote` paths (if present in Python indexes) are correct.
7) Optional: build the article view to spot rendering issues (see Build & Verify below).

Style rules:
- Keep quotes in English, even if the card body is Russian.
- Limit each quote block to 1–3 short quotes per claim.
- Prefer precise locators (Section/Figure/Equation). Pages/lines are acceptable for transcriptions lacking formal markers.

---

#### 6) Build & verify locally (optional but recommended)
- Quick render check (if used in your workflow):
  - `scripts/build_body_html.py` and `article/analysis_view.py` are already wired for the project. If you run them, ensure your environment matches `requirements.txt`.
- Visual inspection:
  - Open the Streamlit app (`streamlit_app.py`) if you rely on it during review; confirm the card shows “Sources & Evidence” properly and internal anchors render.
- Sanity checklist per card:
  - [ ] “Sources & Evidence” section exists.
  - [ ] Every primary claim has at least one verbatim quote and a locator.
  - [ ] No unreferenced factual assertions remain.
  - [ ] If inference/speculation is present, it is labeled.
  - [ ] All file paths/anchors render without errors.

---

#### 7) Naming and IDs
- Do not rename `nXX.md` IDs. Keep them stable.
- Keep directory names as they are (e.g., `2_3_pinn_customizer`).
- Do not add IDE-specific folders/configs; follow JetBrains/PyCharm standards already in use.

---

#### 8) Prioritized backlog (cards likely still missing “Sources & Evidence”)

Use this as a working queue. Always verify before editing, as some cards may have been completed recently.

- n4, n19, n22, n23, n28, n29, n33, n35, n38, n40, n42, n43, n46, n48, n49, n24

Recommendation:
1) Start with evaluation/limitations (2_4_evaluation_approach, 4_limitations_and_future_work) because they are methodology-critical.
2) Then cover remaining methodology/customizer items.
3) Finish with framework/workflow/performance.

When picking each card:
- Skim the body → list claims → attach quotes from `article/transcriptions`.
- Keep edits minimal and strictly evidence-backed.

---

#### 9) Examples to emulate
See these already-updated cards for good structure and tone:
- `article/commentaries_data/4_limitations_and_future_work/n51.md` (optimizer hygiene; Rathore 2024; quotes mapped to claims)
- `article/commentaries_data/2_3_pinn_customizer/n21.md` (big‑valley funnels; Ochoa & Veerapen 2016; LON definitions)
- `article/commentaries_data/2_3_pinn_customizer/n16.md` (noise sensitivity; Scott & De Jong 2016)
- `article/commentaries_data/2_2_hierarchical_text_classifier/n17.md` (undercutting; Amgoud & Nouioua 2015)

---

#### 10) Common pitfalls and how to avoid them
- Pitfall: Paraphrasing instead of quoting.
  - Fix: Always include at least one verbatim sentence per claim.
- Pitfall: Quoting unrelated sections.
  - Fix: Ensure the quoted text semantically entails the claim. If it doesn’t, reframe the claim or find a better source.
- Pitfall: Overclaiming beyond the source.
  - Fix: Split into atomic claims and back each separately; or downgrade to “Comparative inference”.
- Pitfall: External links creep in.
  - Fix: Stay within `article/transcriptions`; escalate if a truly missing source is required.

---

#### 11) Hand-off checklist for the next developer
- [ ] Read this handoff file end-to-end once.
- [ ] Pick 3–5 cards from the backlog and complete their “Sources & Evidence” sections.
- [ ] Keep a short commit message per batch (e.g., `cards: add S&E for n29,n33,n35 (local transcriptions only)`).
- [ ] If you must refactor card bodies to align with sources, keep changes minimal and evidence-driven.
- [ ] Do not modify Python indices unless you add or move `filenote` files; if you do, mirror the existing patterns.

---

#### 12) Contact/notes
- This project is methodologically driven. When in doubt, bias toward formal rigor: fewer, stronger claims with precise citations.
- If a necessary transcription is missing, pause and request it rather than citing the web.

---

### Mini-templates (ready to paste) + Action log

Below are ready-to-paste “Sources & Evidence” blocks for two backlog cards (n4, n19) and a short action log showing how to proceed.

#### Mini-template for n4
Target file: `article/commentaries_data/.../n4.md` (verify the exact section folder; typical location: `article/commentaries_data/2_methodology/n4.md`).

```
## Sources & Evidence

This section maps the card’s claims to verbatim citations (English) from local transcriptions.

1) Claim: "<precise claim #1 for n4>"
   - Evidence: <Author, Year>, <Section / Figure / Equation / lines in the local transcription file>
   - Quotes (verbatim):
     > "<copy exact sentence>"

2) Claim: "<precise claim #2 for n4>"
   - Evidence: <Author, Year>, <locator>
   - Quotes (verbatim):
     > "<copy exact sentence>"

3) Claim: "<optional claim #3>"
   - Evidence: <Author, Year>, <locator>
   - Quotes (verbatim):
     > "<copy exact sentence>"
```

Suggested local sources to check in `article/transcriptions` (adjust to the actual theme of n4):
- Rathore 2024; Dashtbayaz 2024; Scott & De Jong 2016; Ochoa & Veerapen 2016; Oreskes 1994; Noy & McGuinness 2001 (choose the one(s) that directly justify the card’s concrete claims).

---

#### Mini-template for n19
Target file: `article/commentaries_data/2_4_evaluation_approach/n19.md` (verify path exists).

```
## Sources & Evidence

This section maps the card’s claims to verbatim citations (English) from local transcriptions.

1) Claim: "<precise claim #1 for n19>"
   - Evidence: <Author, Year>, <Section / Figure / Equation / lines>
   - Quotes (verbatim):
     > "<copy exact sentence>"

2) Claim: "<precise claim #2 for n19>"
   - Evidence: <Author, Year>, <locator>
   - Quotes (verbatim):
     > "<copy exact sentence>"

3) Claim: "<optional claim #3>"
   - Evidence: <Author, Year>, <locator>
   - Quotes (verbatim):
     > "<copy exact sentence>"
```

Suggested local sources to check in `article/transcriptions` for evaluation/metrics themes:
- Oreskes et al. 1994 (verification/validation/confirmation), InstructGPT 2022 (pairwise RM & datasets), Hallucination surveys 2024/2025, Möltner 2026 (self‑validation), Spec2RTL‑Agent 2025 (multi‑agent verification loop).

---

#### Action log (example)

- [Step 1] Identify target files for n4 and n19 via project tree (or list):
  - n4 → expected at `article/commentaries_data/2_methodology/n4.md`.
  - n19 → expected at `article/commentaries_data/2_4_evaluation_approach/n19.md`.

- [Step 2] Extract concrete claims from each card’s title/body (2–6 max). If any claim is too broad, split into atomic claims.

- [Step 3] Open `article/transcriptions/` and locate matching sources. Prefer sections with explicit Section/Figure/Equation (or use lines ~XX–YY if needed).

- [Step 4] Paste the corresponding mini-template into each card file under a new `## Sources & Evidence` section and fill in:
  - Evidence: <Author, Year>, <locator> for each claim.
  - 1–3 verbatim English quotes per claim.

- [Step 5] If body wording exceeds what is supported by quotes, either:
  - add additional quotes for full support; or
  - reword the body to strictly match evidence; or
  - label residual parts as “Comparative inference” / “Speculative extension”.

- [Step 6] Sanity checklist per card: section present, all claims mapped, no unreferenced assertions, render OK.

---

### Run log (concrete actions)

Timestamp (local): 2026-07-28 11:47

1) Prepared mini-template for n4
   - Target path (expected): `article/commentaries_data/2_methodology/n4.md`
   - Action: Added ready-to-paste “Sources & Evidence” block in this handoff (see section “Mini-template for n4”).
   - Next step for dev: Open n4.md → extract 2–4 atomic claims from body → fill Evidence locators and paste 1–3 verbatim quotes per claim from `article/transcriptions`.
   - Suggested local sources to check: Rathore 2024; Dashtbayaz 2024; Scott & De Jong 2016; Ochoa & Veerapen 2016; Oreskes 1994; Noy & McGuinness 2001 (pick those that directly entail the claims).

2) Prepared mini-template for n19
   - Target path (expected): `article/commentaries_data/2_4_evaluation_approach/n19.md`
   - Action: Added ready-to-paste “Sources & Evidence” block in this handoff (see section “Mini-template for n19”).
   - Next step for dev: Open n19.md → extract concrete claims (evaluation/metrics context) → fill Evidence locators and paste 1–3 verbatim quotes per claim from `article/transcriptions`.
   - Suggested local sources to check: Oreskes 1994; InstructGPT 2022; Hallucination surveys 2024/2025; Möltner 2026; Spec2RTL‑Agent 2025.

---

### Backlog directory map (nXX → path)

For the current backlog, these are the expected locations of the card files (verify existence before editing):

- n4  → `article/commentaries_data/2_methodology/n4.md`
- n19 → `article/commentaries_data/2_4_evaluation_approach/n19.md`
- n22 → `article/commentaries_data/3_4_framework_performance/n22.md`
- n23 → `article/commentaries_data/4_limitations_and_future_work/n23.md`
- n24 → `article/commentaries_data/3_2_code_correctness/n24.md`
- n28 → `article/commentaries_data/4_limitations_and_future_work/n28.md`
- n29 → `article/commentaries_data/4_limitations_and_future_work/n29.md`
- n33 → `article/commentaries_data/4_limitations_and_future_work/n33.md`
- n35 → `article/commentaries_data/4_limitations_and_future_work/n35.md`
- n38 → `article/commentaries_data/2_4_evaluation_approach/n38.md`
- n40 → `article/commentaries_data/2_4_evaluation_approach/n40.md`
- n42 → `article/commentaries_data/4_limitations_and_future_work/n42.md`
- n43 → `article/commentaries_data/4_limitations_and_future_work/n43.md`
- n46 → `article/commentaries_data/2_methodology/n46.md`
- n48 → `article/commentaries_data/4_limitations_and_future_work/n48.md`
- n49 → `article/commentaries_data/2_4_evaluation_approach/n49.md`

Use this as a quick router when opening files for S&E updates.

---

### Gold example (full S&E block)

This is an example of a finished “Sources & Evidence” section, adapted from an already completed card. It shows the expected density and style.

```
## Sources & Evidence

This section maps the card’s claims to verbatim citations (English) from local transcriptions.

1) Claim: "The PINN loss is ill‑conditioned mainly due to the residual term with differential operators; quasi‑Newton methods improve conditioning."
   - Evidence: Rathore et al. (2024), Sections 5–6; Figures 3 & 7; Table 1
   - Quotes (verbatim):
     > "We show empirically that the ill‑conditioning of the PINN loss is mainly due to the residual loss, which contains the differential operator D."  (Sec. 5.2)
     > "For all three problems, the magnitude of eigenvalues and the condition number has been reduced by at least 10^3 [with L‑BFGS preconditioning]."  (Sec. 5.3)

2) Claim: "Adam+L‑BFGS outperforms Adam or L‑BFGS alone across widths and PDEs."
   - Evidence: Rathore et al. (2024), Section 6; Table 1
   - Quotes (verbatim):
     > "Across each network width, the lowest loss and L2RE is always delivered by Adam+L‑BFGS."  (Sec. 6.1)
```

Notes:
- Keep 1–3 quotes per claim, short and directly entailing the claim; add Figure/Table/Equation markers where applicable.

---

### Quick reference of common transcriptions (where to look)

Use these pointers to quickly locate justifying quotes. Paths are under `article/transcriptions/`.

- Lin 2024 — "To Be a Frequentist or Bayesian? Five Positions in a Spectrum"
  - Look at: Bayes’ Rule (likelihood as frequentist prob.), Centrism: Frequentist Bayes, The Epistemological Question (frequentist standards; empirical Bayes)

- Oreskes 1994 — "Verification, Validation, and Confirmation of Numerical Models in the Earth Sciences"
  - Look at: definitions/limits of V&V; partial confirmation; why a faulty model may appear correct; calibration vs verification

- Rathore 2024 — "Challenges in Training PINNs: A Loss Landscape Perspective"
  - Look at: Sec. 4 (near‑zero loss ↔ L2RE), Sec. 5 (ill‑conditioning; residual term), Sec. 5.3 (L‑BFGS preconditioning), Sec. 6 (Adam+L‑BFGS), Sec. 7 (NNCG)

- Scott & De Jong 2016 — "Landscape Features... Noise"
  - Look at: Abstract/§1 (cheap features vs noise), §3.1 (p≈1e‑3 sensitivity), §3.2 (explicit averaging weak), Eq. (1),(2)

- Ochoa & Veerapen 2016 — "Deconstructing the Big Valley..."
  - Look at: Abstract/§1 (multiple funnels), §3 (LON definitions), remarks on restarts and large perturbations

- Noy & McGuinness 2001 — "Ontology Development 101"
  - Look at: competency questions; slots & facets (value type / allowed values / cardinality); domain & range

- Kreikemeyer 2025 — "Using (Not‑so) Large LLMs... Formal DSL"
  - Look at: grammar‑constrained decoding (EBNF), LoRA/PEFT settings, reported accuracy (~84.5%), synthetic+few‑shot

- InstructGPT 2022 — "Training LMs to follow instructions with human feedback"
  - Look at: Step 2 (RM as pairwise), Eq. for RM loss, multi‑candidate ranking datasets

- Möltner 2026 — "Creation, Evaluation and Self‑Validation of Simulation Models with LLMs"
  - Look at: self‑validation loop; list of validation methods (Table); performance metrics (e.g., F1/FPR/TPR)

---

### Front‑matter [[sources]] vs. “Sources & Evidence” policy

- Front‑matter `[[sources]]` (at the top of `nXX.md`) is a light bibliography pointer for rendering and navigation.
- The “Sources & Evidence” section is the single source of truth for verification: it must contain claim‑level, verbatim quotes with precise locators.
- When to edit front‑matter `[[sources]]`:
  - Add or remove an entry only if the set of cited papers in the card’s body materially changes.
  - Do not duplicate every micro‑source; keep `[[sources]]` concise (primary papers only).
- When updating “Sources & Evidence”:
  - Always ensure each factual assertion in title/body has at least one supporting quote.
  - If an assertion is an inference not directly quoted, mark it as “Comparative inference” or “Speculative extension”.
  - Prefer local transcriptions; avoid external URLs unless explicitly approved.

---

### Run log — appended entries (2026‑07‑28)

- [Step] Added S&E skeleton to n35
  - Path: `article/commentaries_data/4_limitations_and_future_work/n35.md`
  - Action: Appended `## Sources & Evidence` block with 3 claim slots and placeholders for Evidence/Quotes.
  - Next: Fill verbatim quotes from the paper referenced in front‑matter (Merhej, Schockaert, De Cock 2015) or other locally cited sources in the card body.

- [Step] Added S&E skeleton to n38
  - Path: `article/commentaries_data/2_4_evaluation_approach/n38.md`
  - Action: Appended `## Sources & Evidence` block with 3 claim slots and placeholders for Evidence/Quotes.
  - Next: Use local transcription for ICON Challenge (algorithm selection) to quote normalised score, shared infrastructure (ASlib), and cross‑scenario eval.

- [Step] Added S&E skeleton to n40
  - Path: `article/commentaries_data/2_4_evaluation_approach/n40.md`
  - Action: Appended `## Sources & Evidence` block with 3 claim slots and placeholders for Evidence/Quotes.
  - Next: Use Skvorc, Eftimov, Korosec (2020) local transcription to quote about instance‑space analysis/normalisation/feature scaling where relevant to audit shift/scale sensitivity of evaluation.

- [Step] Filled S&E for n35 with verbatim quotes
  - Path: `article/commentaries_data/4_limitations_and_future_work/n35.md`
  - Sources used: Merhej, Schockaert, De Cock (2015) — lines 21, 29, 33–34, 67–68, 35
  - Claims covered: (1) plausible vs minimal repairs with expert knowledge; (2) GRN diameter property enabling non‑minimal but plausible repairs; (3) rules of thumb formalized in ASP.

- [Step] Filled S&E for n38 with verbatim quotes
  - Path: `article/commentaries_data/2_4_evaluation_approach/n38.md`
  - Sources used: Kotthoff, Hurley, O’Sullivan (2017) — lines 50–52, 56–60, 81–82
  - Claims covered: (1) pre‑ICON incomparability; (2) ASlib + code + bootstrap protocol; (3) normalized score 0=oracle, 1=single‑best.

- [Step] Filled S&E for n40 with verbatim quotes
  - Path: `article/commentaries_data/2_4_evaluation_approach/n40.md`
  - Sources used: Škvorc, Eftimov, Korošec (2020) — lines 30–31, 44–47, 38, 66–67, 32–37
  - Claims covered: (1) benchmark design & representativeness; (2) non‑invariance to scaling/shifting; (3) ELA/t‑SNE instance‑space visualization for auditing problem sets.