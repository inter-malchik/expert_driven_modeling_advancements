# Residual Construction and Advanced Architectures in PINNs

> **Source links:** [Eshkofti et al. (2025)](https://arxiv.org/abs/2503.14222) · [Chiu et al. (2026)](https://arxiv.org/abs/2602.19475)

Analysis based on:
- **Eshkofti et al. (2025)**: "Vanishing Stacked-Residual PINN for State Reconstruction of Hyperbolic Systems"
- **Chiu et al. (2026)**: "Scale-PINN: Learning Efficient Physics-Informed Neural Networks Through Sequential Correction"

## Context and Problem
In the Expert-Guided PINN framework (Paper A), every expert intervention triggers a retraining cycle. A major limitation observed is the stochasticity of the result: given the same expert instruction and valid code generation, the PINN might converge to different trajectories, or fail to converge to a physical solution altogether (e.g., the 700-day outbreak). This is often due to the "stiffness" of the loss landscape and the inability of vanilla PINN losses to handle sharp transitions or noise in the expert-guided loss terms.

## Methodological Solution: Stacked and Sequential Residuals

### 1. Stacked-Residual PINN (Eshkofti et al., 2025)
Eshkofti proposes a hierarchical composition of the neural approximation:
$$u_i(x,t) = u_{i-1}(x,t) + |\alpha_i| \mathcal{N}_i([t, x, u_{i-1}(t, x)]; \theta_i)$$

Key principles:
- **Vanishing Viscosity**: The training starts with a smooth, viscous version of the problem ($\gamma > 0$) and progresses towards the target hyperbolic system ($\gamma = 0$).
- **Hierarchical Correction**: Each block operates at a reduced viscosity, refining the previous approximation.
- **Outcome**: Reduces error variance by an order of magnitude compared to vanilla PINNs, ensuring that expert-guided corrections are stable across different random seeds.

### 2. Sequential Correction / Scale-PINN (Chiu et al., 2026)
Chiu introduces a smoothing correction using a **Helmholtz filter** to mitigate oscillations in the loss landscape.
- **Mechanism**: $u_\theta(x,t)_{next} = \text{Filter}(u_\theta(x,t)_{prev})$.
- **Benefit**: Induces stability similar to implicit Richardson iteration, significantly accelerating training (10-100x) and matching specialist CFD solvers on benchmarks.

## Application to Expert-Guided Modeling
Implementing these architectures in the PINN Customizer would transform the "retraining" step from a blind search into a disciplined, multi-stage refinement:
1. **Stage 1 (Viscous)**: Apply the expert's loss edit with high viscosity/smoothing to capture the macroscopic intent.
2. **Stage 2 (Refinement)**: Stack a residual block to sharpen the forecast (e.g., the peak shift requested by the expert).
3. **Stage 3 (Scale-PINN)**: Use the Helmholtz filter to ensure the final trajectory is physically consistent and free of high-frequency noise induced by the LLM-generated loss terms.

This methodological bridge directly addresses the "instruction collapse" and "stochastic variance" identified as core limitations in the original paper.

## Loss Formulation (per stage k)
- Stacked approximation:
  - `u_k(t, x) = u_{k-1}(t, x) + |α_k| · N_k([t, x, u_{k-1}(t, x)]; θ_k)`
- Physics residual with vanishing viscosity (hyperbolic PDE setting):
  - `R_γk(u_k) = u_t + f(u)_x − γ_k · u_xx`
- Total loss at stage k (example):
  - `L_k = λ_data · L_data(u_k) + λ_phys · ||R_γk(u_k)||^2 + λ_bc · L_bc(u_k)`
- Time‑series/ODE adaptation: viscosity can be implemented as temporal Tikhonov/Helmholtz smoothing penalty on `u` or its derivatives.

## Training Schedule and Criteria
- Viscosity schedule: `γ_k = γ_0 · ρ^k`, with defaults `γ_0 ∈ [1e−1, 1]`, `ρ ∈ (0, 1)`; final stages target `γ_k → 0`.
- Stage gating:
  - Plateau detection: `ΔL < ε` over `N` steps (e.g., ε=1e−4 relative, N=500–1000 iters).
  - Physical Consistency Score (PCS): require `PCS ≥ τ` (e.g., τ=0.95) before advancing; if not reached, extend stage or slightly increase `γ_k`.
- Optimizers per stage: Adam for basin entry, then L‑BFGS for precision (see n51, Rathore 2024).
- Optional sequential correction: apply Helmholtz filter (Scale‑PINN) after each stage.

### Pseudocode (high‑level)
```
u = u0
for k in 1..L:
    γk = γ0 * ρ**k
    freeze(u)
    define uk = u + |αk| * Nk([t, x, u]; θk)
    minimize Lk(uk; γk) with Adam -> L-BFGS
    if PCS(uk) >= τ and plateau: u = uk else adjust γk / steps
    optional: u = HelmholtzFilter(u)
return u
```

## Implementation Notes for PINN Customizer
- Configuration: `{L, γ0, ρ, stage_iters, plateau_eps, plateau_window, PCS_threshold, use_helmholtz}`.
- Logging: per stage record `{MAE, PCS, seed_std, γk, optimizer_switch_step}`; compare to single‑stage baseline.
- Reproducibility: evaluate across ≥3 seeds; report mean±std for MAE/PCS.
- Interfaces: reuse existing training loop; add hooks for stage transitions, viscosity update, and optional filter.

## Metrics & Ablations
- Variance reduction: std of MAE/PCS across seeds (expect ↓ up to 10× vs. baseline per Eshkofti).
- Effect of L (number of stacks), `γ0`, `ρ`, and Helmholtz filter on convergence speed and PCS.
- Compliance accuracy on targeted expert instruction (e.g., peak timing/height) vs. global MAE.

## Failure Modes and Mitigations
- Over‑smoothing (loss of sharp features): lower `γ0`/increase ρ; switch to next stage earlier; use CVaR (see n52) to protect peaks.
- Boundary/IC sensitivity: strengthen `λ_bc`; warm‑start with better `u0`.
- Ill‑conditioning at low viscosity: rely on Adam→L‑BFGS switch (n51), gradient clipping/normalization.

## Cross‑References
- n51 Optimizer Hygiene (Rathore 2024): Adam→L‑BFGS inside each stage.
- n3 PCS: gate stage transitions by PCS.
- n13 Model Arena: evaluate multiple schedules `{L, γ0, ρ}` and select best‑of‑N by MAE+PCS.
