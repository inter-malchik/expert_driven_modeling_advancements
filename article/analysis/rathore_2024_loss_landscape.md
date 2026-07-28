# PINN Loss Landscape and Optimization Hygiene

> **Source links:** [Rathore et al. (2024)](https://arxiv.org/abs/2402.01868) · [Dashtbayaz et al. (2024)](https://www.ijcai.org/proceedings/2024/647)

Analysis based on:
- **Rathore et al. (2024)**: "Challenges in Training PINNs: A Loss Landscape Perspective"
- **Dashtbayaz et al. (2024)**: "Physics-Informed Neural Networks: Minimizing Residual Loss with Wide Networks and Effective Activations"

## Context and Problem
Текущая реализация Expert‑Guided PINN (Paper A) использует Adam на всём цикле дообучения. Согласно Rathore et al. (ICML 2024), ландшафт лосса PINN обладает выраженной жёсткостью (stiffness) и плохой обусловленностью из‑за наличия дифференциальных операторов в физическом слагаемом. Это приводит к тому, что первая‑порядковая оптимизация часто застревает на высоких плато/седлах, и провал сходимости принимается за «неверную гипотезу эксперта», хотя является именно «ошибкой оптимизации».

## Key Findings

### 1. Landscape Stiffness and Conditioning
Rathore et al. показывают, что применение дифференциального оператора к нейросети радикально искажает геометрию лосса: растёт кривизна и ухудшается обусловленность Гессиана. Для корректного решения требуется очень малая величина лосса (на слайдах ICML указывается порядок 1e−4 и ниже для низкой L2‑relative error). 
- **Выбор активаций**: Dashtbayaz et al. (2024) теоретически обосновывают, что для существования глобального минимума по residual‑лоссу третья производная активации должна быть локально биективной. Практически это поддерживает выбор **Sine** (для задач 2‑го порядка) и **Softplus** (для 1‑го порядка, как SIRD) вместо Tanh/ReLU.

### 2. The Adam + L-BFGS Hybrid
Ключевая рекомендация для робастности — гибридная оптимизация: переход от методов первого порядка (Adam) к методам квазиньютоновского типа (L‑BFGS).
- **Adam** эффективен как «грубый глобальный поиск», но стагнирует у минимума из‑за стохастичности и нечувствительности к кривизне.
- **L‑BFGS** лучше справляется с жёсткостью residual‑поверхности и даёт высокую точность (до $10^{-8}$ по лоссу), что необходимо для достоверного соответствия траектории экспертной инструкции.
- В работе также упоминается более продвинутый второй‑порядковый метод **NysNewton‑CG (NNCG)**, показывающий дальнейшее улучшение; его можно рассматривать как перспективную замену этапу L‑BFGS при наличии реализации.

## Methodological Proposed Update: Optimizer Hygiene
Чтобы правки эксперта корректно отображались в поведении PINN, вводим обязательный двухфазный цикл оптимизации для каждой правки:
1. **Фаза 1 (глобальная):** Adam 1–2 тыс. итераций, шаг подбора — до входа в «правильный бассейн притяжения» после изменения лосса.
2. **Фаза 2 (уточнение):** L‑BFGS до сходимости или достижения порога точности. Рекомендуемые критерии завершения:
   - `loss_phys + loss_data < 1e-4` или
   - `||∇L||_∞ < 1e-6` и относительное улучшение < 1e‑5 за 50 итераций.

При наличии реализации второго порядка можно протестировать **NysNewton‑CG** как альтернативу L‑BFGS.

Этот слой «Optimizer Hygiene» критичен для перехода от исследовательского прототипа к робастному методологическому стандарту.

---

## Evidence Map (Sources & Evidence for Card n51)

This section mirrors the card’s claims and anchors them to primary sources with verbatim English quotes.

1) Claim: "PINN loss landscape is ill‑conditioned due to differential operators in the residual term."
   - Source: Rathore et al. (2024), Abstract; Contributions; §5, §5.2.
   - Quotes (verbatim):
     > "We demonstrate that the loss landscape of PINNs is ill-conditioned due to differential operators in the residual term and show that quasi-Newton methods improve the conditioning by 1000× or more (Section 5)."

     > "We see residual loss, which contains the differential operator D, is the most ill-conditioned among all components. Our theory (Section 8) shows this ill-conditioning is likely due to the ill-conditioning of D."

2) Claim: "First‑order methods alone struggle on ill‑conditioned losses; convergence is slow."
   - Source: Rathore et al. (2024), §5.1.
   - Quote (verbatim):
     > "A large condition number implies the loss is very steep in some directions and flat in others, making it difficult for first-order methods to make sufficient progress toward the minimum. When H_L(w) has a large condition number (particularly, for w near the optimum), the loss L is called ill-conditioned."

3) Claim: "Adam+L‑BFGS outperforms Adam or L‑BFGS alone across problems and widths."
   - Source: Rathore et al. (2024), §6, Table 1.
   - Quotes (verbatim):
     > "We show that Adam+L‑BFGS is superior across a variety of network sizes (Section 6)."

     > "Across each network width, the lowest loss and L2RE is always delivered by Adam+L‑BFGS." (see Table 1)

4) Claim: "Useful PINN solutions require training to near‑zero loss; lowering loss by orders of magnitude yields much lower L2RE."
   - Source: Rathore et al. (2024), §4; Figure 2.
   - Quotes (verbatim):
     > "PINNs must be trained to near-zero loss to obtain a reasonably low L2RE."

     > "On the convection PDE, a loss of 10^{-3} yields an L2RE around 10^{-1}, but decreasing the loss by a factor of 100 to 10^{-5} yields an L2RE around 10^{-2}, a 10× improvement." (Fig. 2)

5) Claim: "Activation choice (Sine/Softplus) justified so residual loss admits global minima."
   - Source: Dashtbayaz et al. (2024), Abstract; §1; §4; Figure 1.
   - Quotes (verbatim):
     > "To solve a k‑th order PDE, the k‑th derivative of the activation function should be bijective." (Abstract)

     > "This presence of σ' in PINNs highlights the importance of an activation function with well‑behaved derivatives ... as it involves higher‑order derivatives of σ." (§1)

     > "Figure 1: ... only Softplus has a bijective first derivative." (Fig. 1 caption)
