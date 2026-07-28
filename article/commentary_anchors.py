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
        'After successfully generating a syntactically correct loss function, the module initiates the process of further training of PINN'
    ),
    "n17": (
        'For the confirmed class and subclass combination, the corresponding loss function modification rules are extracted from the knowledge base. These rules, provided in Appendix A, represent strict guidelines for LLM, defining which components of the original loss function can be modified (e.g., by adding a penalty term) and which are prohibited.'
    ),
    "n18": (
        'An LLM-loss-semantic-checker could verify alignment between the generated code and modification rules, reducing hallucinations.'
    ),
    "n19": (
        'It is crucial to note that the successful model modification via external input does not mean the quality or correctness of the expert’s suggestion itself'
    ),
    "n20": (
        'The conversational agent’s functionality includes validating expert comments for compliance with the following criteria: concreteness (a single specific point), certainty (lack of vagueness), and objectivity (lack of emotional overtones).'
    ),
    "n21": (
        'After successfully generating a syntactically correct loss function, the module initiates the process of further training of PINN'
    ),
    "n22": (
        'our analysis identified a subset of instances (15–28%) (Figure 5 ) where adapting the loss function did not yield a meaningful divergence from the original forecast.'
    ),
    "n23": (
        'The current system of rules for modifying loss functions lacks sufficient detail to provide meaningful control over the generation process.'
    ),
    "n24": (
        'We conducted a Nemenyi post-hoc test, which revealed that Meta-Llama-3.1-8B-Instruct, unlike Llama-3.3-70B-Instruct, generates functions that deviate more significantly from the original. This correlates with the empirical observation that 50% of its output fails compilation (Figure 3), suggesting that the increased syntactic incorrectness is due to more aggressive source code modification. Differences between all other pairs of models were statistically insignificant.'
    ),
    "n25": (
        'Simplifying the interaction between the operator and the mathematical model could substantially broaden the use of forecasting in epidemiological practice'
    ),
    "n26": (
        'A key contribution of this study is an interactive framework that instantiates an expert-in-the-loop optimization cycle. The process begins with an expert’s qualitative assessment of a forecast, which is translated into a structured specification for loss function modification.'
    ),
    "n27": (
        "A key contribution of this study is an interactive framework that instantiates an expert-in-the-loop optimization cycle. The process begins with an expert's qualitative assessment of a forecast, which is translated into a structured specification for loss function modification."
    ),
    "n28": (
        'A significant limitation is the lack of mechanisms to control the interpretability of the generated loss functions. The current rule system (Appendix A), based on specifying the target components of the loss function for modification, is insufficient to ensure semantic transparency and explainability of the changes made.'
    ),
    "n29": (
        'we plan to replace the simple penalty additions by class-subclass-specific modification templates. These templates will explicitly define which loss components and parameters can be altered, which mathematical operators are admissible, and what numerical ranges are permitted.'
    ),
    "n30": (
        'The Meta-Llama-3.1-8B-Instruct model demonstrated lower compliance with comments (Figure 5).'
    ),
    "n31": (
        'The defining characteristic of the PINN methodology is the optimization of a composite loss function that includes both the data-fitting error and the residual of the equations describing the modeled process. In the context of epidemiological forecasting, the PINN loss function typically includes components corresponding to the observed data, the differential equations of the SIR model and its extensions (e.g., SEIR, SIRD), and the initial/boundary conditions.'
    ),
    "n32": (
        'The defining characteristic of the PINN methodology is the optimization of a composite loss function that includes both the data-fitting error and the residual of the equations describing the modeled process.'
    ),
    "n33": (
        'A promising direction is to evolve the system toward a multi-agent architecture, where specialized LLMs enhance autonomy and objectivity. An LLM-expert-evaluator could quantify forecast compliance with the original comment; low confidence scores could trigger automatic loss regeneration or comment refinement. An LLM-loss-semantic-checker could verify alignment between the generated code and modification rules, reducing hallucinations.'
    ),
    "n34": (
        'we used a PINN’s architecture based on the SIRD model equations from Abramova and Leonenko (2024)'
    ),
    "n35": (
        'The current system of rules for modifying loss functions lacks sufficient detail to provide meaningful control over the generation process.'
    ),
    "n36": (
        'The proposed approach to evaluating results has a significant subjective component, particularly in the "Compliance with the comment" criterion. The lack of formalized metrics for measuring the semantic correspondence between the comment and the forecast limits the objectivity of the results.'
    ),
    "n37": (
        'The model, based on "bert-base-cased", was fine-tuned on a synthetic dataset of 2000 expert-like commentaries. This dataset was generated by DeepSeek-V3.1 using real expert comments to ensure representativeness'
    ),
    "n38": (
        'Due to the lack of standardized numerical metrics for assessing the semantic correspondence of a forecast to an expert’s textual commentary, a system of qualitative validation criteria was developed.'
    ),
    "n39": (
        'After automatic classification, the expert confirms the correctness of the assigned class and subclass.'
    ),
    "n40": (
        'A value of 1100 was empirically chosen as the threshold for successfully meeting this criterion, using the MAE (Mean Absolute Error) metric.'
    ),
    "n41": (
        'These templates will explicitly define which loss components and parameters can be altered, which mathematical operators are admissible, and what numerical ranges are permitted.'
    ),
    "n42": (
        'The current rule system (Appendix A), based on specifying the target components of the loss function for modification, is insufficient to ensure semantic transparency and explainability of the changes made.'
    ),
    "n43": (
        'The hierarchical classifier was trained and evaluated on synthetic data, which may not capture the full linguistic variability of real expert feedback. Large-scale validation on authentic expert comments is planned for future work at the Smorodintsev Research Institute for Influenza.'
    ),
    "n44": (
        'The loop is closed by presenting the refined forecast to the expert, enabling continuous model alignment with domain knowledge.'
    ),
    "n45": (
        'If the forecast is unsatisfactory, the expert enters a textual comment in the “Instructions for the model” field.'
    ),
    "n46": (
        'The defining characteristic of the PINN methodology is the optimization of a composite loss function that includes both the data-fitting error and the residual of the equations describing the modeled process.'
    ),
    "n47": (
        'the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days).'
    ),
    "n48": (
        'An LLM-expert-evaluator could quantify forecast compliance with the original comment; low confidence scores could trigger automatic loss regeneration or comment refinement.'
    ),
    "n49": (
        'A promising direction is to evolve the system toward a multi-agent architecture, where specialized LLMs enhance autonomy and objectivity. An LLM-expert-evaluator could quantify forecast compliance with the original comment; low confidence scores could trigger automatic loss regeneration or comment refinement. An LLM-loss-semantic-checker could verify alignment between the generated code and modification rules, reducing hallucinations.'
    ),
    "n50": (
        'After successfully generating a syntactically correct loss function, the module initiates the process of further training of PINN'
    ),
    "n51": (
        'The defining characteristic of the PINN methodology is the optimization of a composite loss function that includes both the data-fitting error and the residual of the equations describing the modeled process.'
    ),
    "n52": (
        'A value of 1100 was empirically chosen as the threshold for successfully meeting this criterion, using the MAE (Mean Absolute Error) metric.'
    ),
}
