"""Quoted passages in the paper that each commentary annotates."""

from __future__ import annotations

# Exact substrings from article/body_html.py, in reading order.
ANCHOR_TEXTS: dict[str, str] = {
    "n1": (
        "direct use of LLM is associated with the risk of hallucinations Cossio (2025) "
        "– the generation of incorrect or physically unjustified code, which requires "
        "the development of strict control mechanisms."
    ),
    "n2": (
        "A promising direction is to combine the advantages of both approaches within "
        "the framework of Physics-Informed Neural Networks (PINN)"
    ),
    "n3": (
        "A key contribution of this study is an interactive framework that instantiates "
        "an expert-in-the-loop optimization cycle."
    ),
    "n4": (
        "the optimization of a composite loss function that includes both the "
        "data-fitting error and the residual of the equations describing the modeled process"
    ),
    "n5": (
        "translates a comment into executable code for a loss function satisfying given constraints"
    ),
    "n6": (
        "This approach implements a split-responsibility model, where the model performs "
        "the initial segmentation of the input data, and the final decision is made by an expert."
    ),
    "n7": (
        "These rules, provided in Appendix A, represent strict guidelines for LLM, defining "
        "which components of the original loss function can be modified (e.g., by adding a "
        "penalty term) and which are prohibited."
    ),
    "n8": (
        "Syntactic analysis – checking the code's compilability using the Python interpreter."
    ),
    "n9": (
        "Due to the lack of standardized numerical metrics for assessing the semantic "
        "correspondence of a forecast to an expert's textual commentary, a system of "
        "qualitative validation criteria was developed."
    ),
    "n10": (
        "<strong>Compliance with the comment.</strong> This is the primary criterion for "
        "assessing the technical success of the modification system."
    ),
    "n11": (
        "To empirically evaluate the impact of model scale on the quality of expert comment "
        "interpretation and the generation of correct loss functions, three models with "
        "different parameter sizes were selected:"
    ),
    "n12": (
        "All LLMs were set to a temperature of 1.0 to achieve maximum variation in results "
        "even when entering the same comment."
    ),
    "n13": (
        "<strong>Successful result.</strong> The curve is reshaped in accordance with the "
        "expert's request, and its form does not contradict the laws of epidemic dynamics."
        "</li><li><strong>Unsuccessful result.</strong> The curve is reshaped incorrectly."
        "</li><li><strong>Ambiguous result.</strong> The expert's requirements are formally "
        "satisfied, but the result is questionable"
    ),
    "n14": (
        "The current system of rules for modifying loss functions lacks sufficient detail "
        "to provide meaningful control over the generation process."
    ),
    "n15": (
        'The proposed approach to evaluating results has a significant subjective component, '
        'particularly in the "Compliance with the comment" criterion.'
    ),
    "n16": (
        "Wei et al. (2024/25). DANTE: Deep active optimization for complex systems."
    ),
    "n17": (
        "Bradley-Terry Thinking Reward Model, которая разделяет «следование инструкции» и «точность прогноза»."
    ),
    "n18": (
        "Согласно Zhang et al. (2026, TRM), эта проблема решается через Bradley-Terry Thinking Reward Model"
    ),
    "n19": (
        "Согласно Eftimov & Korošec (2019, eDSC), для таких распределений необходимы непараметрические тесты"
    ),
    "n20": (
        "теория Malan (2021) и Daza (2016) показывает, что это классические «патологии сопряженных ландшафтов»."
    ),
    "n21": (
        "отсутствие формальной онтологии (competency questions) делает базу правил (Appendix A) хрупкой и труднорасширяемой."
    ),
    "n22": (
        "Ma et al. (2023). Eureka. Генерация reward-функций как кода (базис метода)."
    ),
    "n23": (
        "Miller (2020). Contrastive Explanation. Оценка успеха через контраст"
    ),
    "n24": (
        "Hidalgo et al. (2018). Glucose Prognosis by Grammatical Evolution. Использование грамматик (DSL) для ограничения LLM."
    ),
    "n25": (
        "Noy & McGuinness (2001). Ontology Development 101. Методология построения иерархии классов"
    ),
    "n26": (
        "Malek (2009). Meta-Heuristic Collaboration in a MAS. Архитектура для Future Work"
    ),
    "n27": (
        "Halpern & Pearl (2005). Causes and Explanations. Формальная база для проверки того, является ли правка LLM"
    ),
    "n28": (
        "The current study is limited by the lack of mechanisms to control the interpretability of the generated loss functions."
    ),
    "n29": (
        "Longo, How the Future Depends on the Past and Rare Events in Systems of Life"
    ),
    "n30": (
        "Broekens et al., Do You Get It? User-Evaluated Explainable BDI Agents"
    ),
    "n31": (
        "Miller et al., Beware of Inmates Running the Asylum"
    ),
    "n32": (
        "Pillay (2010), An Empirical Study into the Structure of Heuristic Combinations"
    ),
    "n33": (
        "Huang et al. (2024), A Survey on Hallucination in Large Language Models"
    ),
    "n34": (
        "Kreikemeyer et al. (2025), Using (Not-So) Large Language Models to Generate Simulation Models"
    ),
    "n35": (
        "Wang et al. (2025), Towards Understanding the Characteristics of Code Generation Errors"
    ),
    "n36": (
        "Gruber (1993), A Translation Approach to Portable Ontology Specifications"
    ),
    "n37": (
        "Yu et al. (2025), Spec2RTL-Agent: Automated Hardware Code Generation"
    ),
    "n38": (
        "Lin (2024), To Be a Frequentist or Bayesian?"
    ),
    "n39": (
        "Möltner et al. (2026), Creation, Evaluation and Self-Validation of Simulation Models with LLMs"
    ),
    "n40": (
        "Khalili & Wimmer (2024), Towards Improved XAI-Based Epidemiological Research"
    ),
    "n41": (
        "The interaction with the framework proceeds through the following steps:"
    ),
    "n42": (
        "The analysis was conducted on daily and cumulative incidence data"
    ),
    "n43": (
        "We hypothesize that discrepancies between the forecast and training data (Figure 5)"
    ),
    "n44": (
        "A promising direction is to evolve the system toward a multi-agent architecture"
    ),
    "n45": (
        "Experience with operational forecasting indicates the need for periodic calibration"
    ),
    "n46": (
        "The impact of operator competence and their understanding of how large language models function"
    ),
    "n47": (
        "This study presents an initial step in this direction in the form of the experimental Expert-Guided PINN framework"
    ),
    "n48": (
        "The define characteristic of the PINN methodology is the optimization of a composite loss function"
    ),
}
