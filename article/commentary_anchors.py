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
}
