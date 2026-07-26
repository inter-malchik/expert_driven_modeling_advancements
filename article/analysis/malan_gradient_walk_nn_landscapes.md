Work A (Gindullina et al., «Expert-guided forecasting of epidemic ARI incidence based on physics-informed neural networks and large language models») translates expert commentary into modifications of the PINN **composite loss** ($L = L_{data} + L_{IC} + L_{ODE}$) and retrains the network with fixed Adam hyperparameters. The failures in Fig. 4b,c—weakening or fourfold strengthening of the zero boundary condition in response to requests about peak shift and continued growth—the authors explain by the lack of LLM control and «architectural features of PINN», but **do not analyze the geometry of the error landscape** after the edit.

Work B (Bosman, Engelbrecht and Helbig, 2018, «Progressive Gradient Walk for Neural Network Fitness Landscape Analysis») shows on an XOR network: random and progressive random walks almost never reach low-error regions (mean MSE ~0.45), whereas **progressive gradient walk**—direction from the gradient, stochastic step size—captures optimal and near-optimal points (mean MSE down to 0.092 micro). The neural network landscape has a structure of «star-shaped» ravines leading toward the boundaries of weight space.

Connection to Work A: the LLM changes BC/ODE/data penalty weights—this is a **shift of the starting point and slope** in the same high-dimensional landscape along which Adam performs gradient descent. Without FLA sampling (as in Bosman et al.), one cannot predict whether an edit will lead into a «ravine» with prolonged epidemic (4b) or into a plateau with a distorted balance of loss terms (4c). Distinction from essay #40 (Scott & De Jong): there **noise in cheap metrics**; here—**geometry of sampling** the error landscape.

---

## 1. PINN as continuous optimization on an error landscape

> **Quote (Gindullina et al.):** *«The defining characteristic of the PINN methodology is the optimization of a composite loss function that includes both the data-fitting error and the residual of the equations describing the modeled process.»*

> **Quote (Gindullina et al.):** *«In the context of epidemiological forecasting, the PINN loss function typically includes components corresponding to the observed data, the differential equations of the SIR model and its extensions (e.g., SEIR, SIRD), and the initial/boundary conditions.»*

> **Quote (Bosman et al.):** *«NN training is a continuous optimisation problem, which can be studied using FLA. The search space of a NN is made up of all possible real-valued weight combinations, where each weight combination corresponds to a certain measure of error.»*

Expert-Guided PINN does not change the network architecture between iterations—it changes the **objective function** (weights and forms of penalties in $L_{IC}$, $L_{ODE}$, $L_{data}$). This is equivalent to swapping the fitness landscape while keeping weight dimensionality θ fixed. Bosman et al. precisely study how the **sampling method** affects the visible properties of such a landscape.

---

## 2. Random sampling is blind to «good» regions

> **Quote (Bosman et al.):** *«If the random samples do not include areas of good fitness, then the presence of local optima and/or saddle points cannot be quantified.»*

> **Quote (Bosman et al.):** *«Smith et al. [26] has shown that, given a difficult optimisation problem with a limited number of good fitness areas, random sampling may fail to capture the unique features of the landscape.»*

> **Quote (Bosman et al.):** *«For both random sampling techniques, the average MSE was around 0.45... The lowest error sampled by the random walks hovered around 0.2. Thus, the random walks have sampled mostly average (random guess) fitness areas, and the areas of optimal fitness (near zero) were almost not sampled at all.»*

Analog in Work A: the pipeline **does not probe** the landscape before full retraining. The LLM proposes an edit → one Adam run → the expert sees the forecast. This is closer to **a single trajectory** (or to a random choice of modification at T=1.0) than to representative sampling. Conclusions about modification «success» (MAE > 700, compliance) refer to **the single point found**, not to the structure of the basin around it—as with random walks that describe only «bad» zones.

---

## 3. Progressive gradient walk: gradient + stochasticity

> **Quote (Bosman et al.):** *«This study proposes to combine the gradient information available in case of NNs with the stochasticity of the progressive random walk.»*

> **Quote (Bosman et al.):** *«Gradient vector $\vec{g}_i$ is calculated for point $\vec{x}_i$... Progressive random walk algorithm is used to generate $\vec{x}_{i+1}$.»*

> **Quote (Bosman et al.):** *«A progressive gradient walk, on the other hand, has successfully captured error values around zero (optimal fitness).»*

A PINN by definition provides gradients of the composite loss with respect to network weights. Bosman et al. use the sign of the gradient as a **direction mask**, while randomizing step magnitude—to avoid sticking to a single trajectory of pure gradient descent and to explore neighborhoods of «interesting» regions. For Expert-Guided PINN this hints at a **cheap predictor** before expensive retrain: a short gradient walk from current weights under the **candidate** loss from the LLM assesses whether the modification pulls toward a low-error zone or into a ravine.

---

## 4. «Starfish», ravines, and space boundaries

> **Quote (Bosman et al.):** *«Previous theoretical studies have indicated that the NN error landscapes are comprised of plateaus and narrow ravines.»*

> **Quote (Bosman et al.):** *«The gradient walk leaned strongly towards the borders of the search space... This observation is in line with the previous studies, proposing that the NN error landscapes have a "starfish" or "sombrero" structure, with ravines of lower error leading outwards.»*

> **Quote (Bosman et al.):** *«Unbounded gradient walks exhibited less clustering than bounded walks... Spikes associated with particular ranges may be explained by the presence of local minima or saddle points that could have trapped the gradient walk.»*

Case Fig. 4b aligns with this picture: weakening zero BC reduces the penalty for the epidemic «tail» → the optimizer can **slide along a ravine** with acceptable curve shape but **anomalous duration** (>700 days). Gindullina describe exactly this:

> **Quote (Gindullina et al.):** *«The LLM responded to this comment by reducing the influence of the zero boundary condition in the loss function... Training with this modified loss produced a new forecast that effectively ignores this boundary condition. As a result, the epidemic curve retains a plausible shape but exhibits an unrealistically long outbreak duration (more than 700 days).»*

The shape is «plausible», the duration is a pathology of **balance among composite loss terms** in a landscape with outward ravines—not merely «LLM error» in a narrow sense.

---

## 5. Fig. 4c: weight skew and plateau

> **Quote (Gindullina et al.):** *«The model increased the weight of the zero boundary condition... by a factor of four, which is difficult to interpret in relation to the expert's request.»*

> **Quote (Gindullina et al.):** *«A plausible explanation is that the strong emphasis on the boundary condition caused the PINN to penalize violations of the SIRD equations less strongly.»*

> **Quote (Bosman et al.):** *«Interestingly, both the micro and the macro gradient walks exhibited peaks around specific error values. This can be an indication of the presence of local minima or saddle points at those fitness values.»*

Fourfold BC strengthening is a sharp shift into **another ravine** of the fitness landscape: penalty for epidemic end dominates, ODE residual recedes to second place → plateau and «stabilization» instead of the requested growth. Bosman et al. show that **peaks in the fitness histogram** of a gradient walk signal modality and saddle structures—a metric Gindullina lack when evaluating an «ambiguous» outcome.

---

## 6. Gradient descent as algorithm-specific sampling (and fixed Adam)

> **Quote (Bosman et al.):** *«Analysing the trajectory of gradient descent is algorithm-specific... Steep gradients combined with the learning rate parameter may induce large steps through the search space, while weak gradients may produce small steps.»*

> **Quote (Gindullina et al.):** *«Fixed training hyperparameters (determined during the system calibration stage) were used: the model is trained with the Adam optimizer at an initial learning rate of 0.0001, scheduled to decay by a factor of 10 every 5000 epochs.»*

> **Quote (Gindullina et al.):** *«including the complexity of optimization, sensitivity to hyperparameters, and the lack of guarantees that physical constraints will be satisfied in the final solution.»*

Work A fixes lr and decay—one **trajectory** on the landscape. Bosman et al. criticize pure GD as a non-representative sampler; progressive gradient walk is a compromise. After an LLM edit the same Adam may land in a different basin, but without a walk **alternative local structures remain invisible**. Gindullina's hypothesis about «PINN, not LLM» is partly correct, but without FLA one cannot separate: bad loss from the LLM vs bad **reachability** of a good minimum at the given lr.

---

## 7. FLA metrics change with sampling method

> **Quote (Bosman et al.):** *«Since progressive gradient walks capture a different distribution of fitness values compared to the random walks, the FLA metrics are expected to yield different results when calculated over the gradient walks.»*

> **Quote (Bosman et al.):** *«the FLA metrics obtained from the gradient walks seemed to capture the specific known characteristics of NN error landscapes with better precision.»*

Bosman et al. Table 2: FEM (ruggedness) for gradient walk differs strongly micro vs macro—**step scale** changes visible smoothness. Parallel: fine penalty edit (micro) vs coarse 4× BC weight reassignment (macro) in Work A yields different «success metrics» for the same expert—Fig. 4a vs 4c. Without multi-scale FLA, MAE thresholds 700/1100 are not tied to landscape geometry.

---

## 8. Comparative table

| Aspect | Bosman et al. (2018) | Gindullina et al. (Expert-Guided PINN) |
|--------|----------------------|------------------------------------------|
| Object | NN weight error landscape (XOR, 9D) | Composite loss epidemiological PINN (SIRD) |
| Sampling | Random / progressive / **gradient walk** | One Adam retrain per LLM edit |
| Gradient | Sign → direction mask; step stochastic | Only inside training; not for diagnostics |
| Structure | Ravines, starfish, saddles | Not measured; described post hoc (4b,c) |
| Good regions | Gradient walk: MSE → 0 | Compliance 25–27%; 10% «infinite growth» |
| Failure 4b | Explained by ravine without BC | BC weakening; >700 days |
| Failure 4c | Fitness peaks → modality | 4× BC; plateau instead of growth |
| Conclusion | Sampling method determines FLA | No FLA before/after loss modification |

---

## 9. Literature review cluster

**Cluster 5** (fitness landscape analysis, error landscapes in ML): Bosman et al.—tooling for **neural network** landscapes; Gindullina—applies PINN without landscape analysis after composite loss edits. Complements #40 (noise in cheap features) with the angle of **gradient-biased sampling**.

---

## Direction 1. Gradient-walk sanity check before full retrain

After LLM generates the loss: 50–200 steps of progressive gradient walk from current PINN weights (forward/backward only, no full epochs). If the fitness distribution shifts toward «tails» (high MSE on hold-out points, rising BC violation)—block retrain and request another edit. Closes Fig. 4b risk before showing the expert.

## Direction 2. Multi-scale walk (micro/macro) for edit classes

Per Bosman et al., micro vs macro walk assess ruggedness differently. For Table A.2 subclasses (fine penalty vs BC weight change) set different $s$ (step size) for the walk and acceptable FEM thresholds—align with modification templates.

## Direction 3. Modality diagnostics after BC/ODE edits

Build a fitness histogram along the gradient walk under the candidate loss; **peaks** (as Bosman Fig. 4)—flag ambiguous outcome before expert evaluation. Especially for edits touching $L_{IC}$ vs $L_{ODE}$ (case 4c).

## Direction 4. Unbounded walk for «starfish» ravines

Test unbounded gradient walk when weakening BC: if the trajectory consistently moves toward large |θ| and low BC penalty with poor ODE residual—automatically reject the modification as risk of long epidemic tail.

## Direction 5. Link with LLM-loss-semantic-checker

Semantic checker validates not only Table A.2 but **expected gradient effect**: request «peak shift» must not decrease zero BC weight (Fig. 4b); request «continue growth» must not let BC dominate ODE (Fig. 4c). Rules derived from FLA literature on ravines, not only from comment ontology.

---

## Summary

Bosman et al. show that for NN error landscapes **random sampling is systematically blind** to low-error regions, while progressive gradient walk—gradient direction plus stochastic step—captures the optimum and ravine structures («starfish»). Expert-Guided PINN changes the composite loss and trusts a single Adam run without FLA: failures in Fig. 4b (BC weakening → >700 days) and 4c (4× BC → plateau) fit **gradient pathologies** of skew among $L_{data}+L_{IC}+L_{ODE}$ terms that Bosman et al. would make visible before full retraining. Integration: short gradient walk as predictor, multi-scale FEM, blocking «ravine» edits—transfer FLA from XOR to PINN Customizer.

---

## Self-report

| Parameter | Value |
|----------|----------|
| Lines (approx.) | ~155 |
| Quotes Work A | 12 |
| Quotes Work B | 14 |
| Directions | 5 |
| Clusters | 5 |
| Language | English |
