# Risk-Aware Optimization and Residual Quantiles

> **Source links:** [Akazan et al. (2025)](https://arxiv.org/abs/2511.18515) · [Han et al. (2022)](https://arxiv.org/abs/2209.05315)

Analysis based on:
- **Akazan et al. (2025)**: "RRaPINNs: Residual Risk-Aware Physics Informed Neural Networks"
- **Han et al. (2022)**: "Residual-Quantile Adjustment for Adaptive Training of Physics-informed Neural Network"

## Context and Problem
Epidemiological data often contains outliers or periods of high volatility (e.g., the start of a new variant). In Paper A, the MAE thresholding approach treats all points with equal weight in the loss function, which can lead to the model "ignoring" critical shifts if they represent a minority of the time points. This is particularly dangerous for the 7–10 day peak shifts requested by experts, where a small localized error in the loss function can lead to a large global trajectory failure.

## Methodological Solution: Risk-Aware Residuals

### 1. Residual Risk-Aware Loss (RRaPINN)
Akazan et al. introduce the use of **Conditional Value-at-Risk (CVaR)** at the loss level. Instead of minimizing the mean residual, the model explicitly targets the "tail" of the residual distribution.
- **Mechanism**: Use a hinge or mean-excess surrogate penalty to control the largest residuals.
- **Benefit**: This explicitly enforces chance constraints and enables transparent control of tail error, ensuring that the model doesn't sacrifice the peak's accuracy to lower the bulk error during other periods of the epidemic.

### 2. Residual-Quantile Adjustment (RQA)
Han et al. (2022) suggest per-sample weights proportional to the residual, trimmed above a quantile threshold to the sample median.
- **Outcome**: This forces the PINN to focus on "hard" points (outliers or regions of sharp change) while preventing loss of attention to the majority of the domain.

## Application to Expert-Guided Modeling
Integrating RRaPINN and RQA into the Customizer's loss generation logic provides a methodological fix for "unphysical" outcomes:
1. **Focus on Expert's Delta**: If the expert requests a change at day $T$, the RQA can dynamically increase the weights for $t \in [T-k, T+k]$, forcing the model to prioritize the expert's specific intervention.
2. **Robustness to Noise**: CVaR prevents the model from converging to a solution that looks good on average but fails catastrophically on the specific physical constraint the expert is worried about.

This transition from "mean-square error" to "risk-aware optimization" is a major step toward building robust, expert-led public health systems.
