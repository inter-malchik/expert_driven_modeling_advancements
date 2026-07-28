# Basin entropy: a new tool to analyze uncertainty in dynamical systems

Alvar Daza^1, Alexandre Wagemakers^1, Bertrand Georgeot^2, David Guéry-Odelin^3 & Miguel A. F. Sanjuán^1

Scientific Reports | 6:31416 | DOI: 10.1038/srep31416

Received: 13 June 2016  
Accepted: 18 July 2016  
Published: 12 August 2016

OPEN

^1 Nonlinear Dynamics, Chaos and Complex Systems Group, Departamento de Física, Universidad Rey Juan Carlos, Móstoles, Madrid, Tulipán s/n, 28933, Spain.  
^2 Laboratoire de Physique Théorique, IRSAMC, Université de Toulouse, CNRS, UPS, France.  
^3 Laboratoire Collisions, Agrégats, Réactivité, IRSAMC, Université de Toulouse, CNRS, UPS, France.  

Correspondence and requests for materials should be addressed to A.D. (email: alvar.daza@urjc.es)

## Abstract

In nonlinear dynamics, basins of attraction link a given set of initial conditions to its corresponding final states. This notion appears in a broad range of applications where several outcomes are possible, which is a common situation in neuroscience, economy, astronomy, ecology and many other disciplines. Depending on the nature of the basins, prediction can be difficult even in systems that evolve under deterministic rules. From this respect, a proper classification of this unpredictability is clearly required. To address this issue, we introduce the basin entropy, a measure to quantify this uncertainty. Its application is illustrated with several paradigmatic examples that allow us to identify the ingredients that hinder the prediction of the final state. The basin entropy provides an efficient method to probe the behavior of a system when different parameters are varied. Additionally, we provide a sufficient condition for the existence of fractal basin boundaries: when the basin entropy of the boundaries is larger than $\log 2$, the basin is fractal.

Dynamical systems describe magnitudes evolving in time according to deterministic rules. These magnitudes evolve in time towards some asymptotic behavior depending on the initial conditions and on the specific choice of parameters. If a given dynamical system possesses only one attractor in a certain region of phase space, then for any initial condition its final destination is clearly determined. However, dynamical systems often present several attractors and, in these cases of multistability, elucidating which orbits tend to which attractor becomes a fundamental question.

A basin of attraction^1 is defined as the set of points that, taken as initial conditions, lead the system to a specific attractor. When there are two different attractors in a certain region of phase space, two basins exist which are separated by a basin boundary. This basin boundary can be a smooth curve or can be instead a fractal curve. The study of these basins can provide much information about the system since their topology is deeply related to the dynamical nature of the system. For example, systems with chaotic dynamics usually display basins of attraction with fractal structures^2.

The previous discussion applies typically to dissipative dynamical systems. However, for open Hamiltonian systems, where the concept of attractors or basins of attraction is meaningless, we can still define escape basins in an analogous way to the basins of attraction in a dissipative system. An escape basin, or exit basin, is the set of initial conditions that escapes through a certain exit. The Hénon-Heiles Hamiltonian is a well-known model for an axisymmetrical galaxy and it has been used as a paradigm in Hamiltonian nonlinear dynamics. It is a two-dimensional time-independent dynamical system, where orbits having an energy above the critical one can escape through one of the three different exits. It is widely known that when two or more escapes are possible in Hamiltonian systems, fractal boundaries typically appear^3.

In order to give an intuitive picture of our problem we may look at Fig. 1(a,b). The figures show the escape basins of the Hénon-Heiles Hamiltonian for two different values of the energy $E$ above the critical energy that separates bounded motions from unbounded motions. Most initial conditions leave the region through one of the three different exits to infinity for any $E$ above this critical energy. The colors represent points that taken as initial conditions leave the region through a specific exit. With this in mind, we may intuitively understand that it is harder to predict in advance which will be the final destination of an orbit in Fig. 1(a) than in Fig. 1(b).

**Figure 1. Comparison between basins.** Escape basins for the Hénon-Heiles system but different energies. They represent which exit will take each initial condition. It is clear that determining the final destination of the trajectories in the case (a) is harder than in the case (b).

**Figure 1 description:** The figure contains two square basin plots labeled (a) and (b). Both show escape basins of the Hénon-Heiles Hamiltonian using red, blue, green, and mixed boundary colors. Panel (a) displays a highly interwoven, fine-scale pattern with many small colored filaments and mottled regions, indicating stronger mixing of basins. Panel (b) displays broader, smoother colored regions with less fine-scale interweaving. Both plots have a triangular/three-exit structure, with colored lobes meeting near the center.

The problem is that even though, we can have an intuitive notion that Fig. 1(a) is more uncertain than Fig. 1(b), there is no quantitative measure to affirm this. Moreover, this is not easy to assess when we compare two figures of basins corresponding to close values of the energy.

This is precisely the idea of uncertainty or unpredictability which we are considering here. This remark is important since we are aware that these terms are polysemic and consequently its use in the literature might be confusing. In this paper we refer to unpredictability or uncertainty as the difficulty in the determination of the final state of a system, that is, to which attractor the initial conditions will tend to. Note that we speak about attractors for simplicity, though the discussion is identical for open Hamiltonian systems, where there are no attractors. This notion of unpredictability strongly differs from others used in nonlinear dynamics, like the Kolmogorov-Sinai entropy^4,5, the topological entropy^6, or the expansion entropy^7, which refer to the difficulty of predicting the evolution of the trajectories. All these quantities are related to the topology of the trajectories, whereas our aim here is to develop an entropy depending on the topology of the basins.

The concept of basin of attraction is broadly used in all branches of science. The flow of water close to an obstacle can be described by means of basins of attraction, and their complicated structure explains the heterogeneity of phytoplankton and the information integration of the early macromolecules evolution^8. Ideas traveling in a neuronal network can be expressed in terms of orbits moving among different basins of attraction^9. The decisions of agents subjected to changes in the market information exhibit complex dynamics, and this is reflected in their intricate basins of attraction^10. The prediction of the evolution of interacting populations can be difficult when fractal boundaries separate the possible outcomes^11. These examples illustrate that we can gain much insight by measuring and understanding the uncertainty associated to the basins.

Many authors describe fractal basin boundaries and when discussing its associated unpredictability, some vague affirmations are found due to a lack of an appropriated measure. In particular, this has been the case with the Wada basins which have received much attention in the past few years because they are said to be even more unpredictable than fractal basins^3,11–14. This affirmation appears repeatedly in the literature, and though it can be intuitively accepted, there is actually no quantitative basis for that.

Our paper constitutes an attempt to give a quantitative answer to the question of the uncertainty of the basins and this is precisely the problem that we discuss here. We propose a natural way to characterize the uncertainty of the basins by defining a quantitative measure that we call basin entropy. The main idea is to build a grid in a given region of phase space, so that through this discretization a partition of the phase space is obtained where each element can be considered as a random variable with the attractors as possible outcomes. Applying the Gibbs entropy definition to that set results in a quantitative measure of the unpredictability associated to the basins. The discretization that we are considering arises naturally both in experiments and in numerical simulations. First, the experimental determination of initial conditions in phase space is physically impossible due to the intrinsic errors of the measurements. In the case of numerical experiments, the limitations of the computing resources constrain the resolution of the phase space under analysis. This unavoidable scaling error can induce wrong predictions even in deterministic models. Then, a natural question arises: how does the uncertainty in the initial condition affect the final state prediction?

A first approach to study the final state uncertainty has been investigated by Grebogi et al.^15. Given two attractors, they studied how the predictability of the system depends on the topology of their basins of attraction. They found a quantity $\alpha$ called uncertainty exponent, which is the dimension of the phase space $D$ minus the capacity dimension $d$ of the boundary that separates both basins

$$
\alpha = D - d.
\tag{1}
$$

The uncertainty exponent takes the value $\alpha = 1$ for basins with smooth boundaries, and $\alpha < 1$ for basins with fractal boundaries. The closer $\alpha$ gets to zero the more difficult it becomes to predict the system. If smooth and fractal basins are mixed, the uncertainty exponent can still be calculated for each boundary, although the procedure is cumbersome^16. As we will discuss later on, while the concept of uncertainty exponent is truly useful its application has several limitations.

Another approach to measure the unpredictability consists of evaluating the volume of each basin of attraction in a certain region of phase space. The ratio of the volume occupied by a single basin to the total volume defines the basin stability^17. It aims at classifying the different basins according to their relative sizes: larger basins are considered more stable. This notion has proved to be useful for the study of the stability of large networks of coupled oscillators, nevertheless it does not take into account how the basins are mixed. For different sets of parameters, a basin with two attractors can show smooth or fractal boundaries while the volume of each basin remains constant. The basin stability would be the same in both cases but obviously fractal boundaries have a more complex structure. A clear example is shown in Fig. 2, where all the basins have the same basin stability. The uncertainty exponent also fails to capture the uncertainty associated to these basins. However, the basin entropy clearly distinguishes the four of them. In the following we provide the mathematical and computational foundation of the basin entropy and a method for its computation.

**Figure 2. Comparison of the different techniques.** The figure shows different basins obtained from well-known dynamical systems with two attractors. In panels (a and b), the uncertainty exponent is $\alpha = 1$ since both boundaries are smooth, while in (c,d) $\alpha = 0$ since both of them are riddled basins. The basin stability is equal to $1/2$ for the four basins. However, the basin entropy is able to distinguish the four cases and provides a method to measure quantitatively the unpredictability in increasing order from (a–d).

**Figure 2 description:** The figure contains four square basin images labeled (a), (b), (c), and (d), each in grayscale/black-white. Panel (a) shows a simple smooth diagonal division into two large regions. Panel (b) shows more complex but still smooth nested bands and curved stripes. Panel (c) shows a riddled-looking basin with many fine vertical gray-scale variations and speckled mixing. Panel (d) shows a highly speckled, apparently random black-gray pattern over the entire square. The visual complexity increases from (a) to (d).

## Concept and definition of basin entropy

Suppose we have a dynamical system with $N_A$ attractors for a choice of parameters in a certain region $\Omega$ of the phase space. We discretize $\Omega$ via a finite number of boxes covering it. Here we study two-dimensional phase spaces, so that we cover $\Omega$ with a grid of boxes of linear size $\varepsilon$. Now we build an application $C:\Omega \to \mathbb{N}$ that relates each initial condition to its attractor, so that we will refer to that application as the color. Each box contains in principle infinitely many trajectories, each one leading to a color labeled from $1$ to $N_A$. In practice we can use only a finite number of trajectories per box. Indeed, it would correspond to the number of times an experiment is repeated, or the number of trajectories computed in a numerical simulation. In this work, we use square boxes with twenty-five trajectories per box (if not otherwise stated) in our numerical simulations. We have seen that twenty-five trajectories per box allows fast computation and provides accurate values of the basin entropy in all the cases studied here (see Fig. S1 in the Supplementary Information).

Although $\varepsilon$ is our limiting resolution, the information provided by the trajectories inside a box can be used to make hypotheses on the uncertainty associated to the box. We consider the colors into the box distributed at random according to some proportions. We can associate a probability to each color $j$ inside a box $i$ as $p_{i,j}$ which will be evaluated by computing statistics over the trajectories inside the box.

Taking into account that the trajectories inside a box are independent in a statistical sense, the Gibbs entropy of every box $i$ is given by

$$
S_i = \sum_{j=1}^{m_i} p_{i,j}\log\left(\frac{1}{p_{i,j}}\right),
\tag{2}
$$

where $m_i \in [1,N_A]$ is the number of colors inside the box $i$, and the probability $p_{i,j}$ of each color $j$ is determined simply by the number of trajectories leading to that color divided by the total number of trajectories in the box.

We choose non-overlapping boxes covering $\Omega$, so that the entropy of the whole grid is computed by the addition of the entropy associated to each one of the $N$ boxes of the grid

$$
S = \sum_{i=1}^{N} S_i
= \sum_{i=1}^{N}\sum_{j=1}^{m_i} p_{i,j}\log\left(\frac{1}{p_{i,j}}\right).
\tag{3}
$$

We note here that the growth of the number of boxes $N$ with the reduction of $\varepsilon$ provokes a counterintuitive effect: as we reduce the scaling box size $\varepsilon$ the entropy $S$ grows. In order to avoid this effect, we consider the entropy $S$ relative to the total number of boxes $N$ and define the following variable

$$
S_b = \frac{S}{N},
\tag{4}
$$

which we call basin entropy. An interpretation of this quantity is associated to the degree of uncertainty of the basin, ranging from $0$ (a sole attractor) to $\log N_A$ (completely randomized basins with $N_A$ equiprobable attractors). This latter upper value is in practice seldom realized even for extremely chaotic systems. The basin entropy in general decreases with the scaling box size $\varepsilon$, as explained hereafter. We now have a tool to quantitatively compare different basins of attraction.

Despite the fact that the basin entropy depends on the scaling box size $\varepsilon$, given a fixed $\varepsilon$ the value of the basin entropy converges as the number of trajectories inside a box increases.

At this point, we can delve deeper into the consequences of this definition by considering a simple hypothesis, which is to assume that the colors inside a box are equiprobable, thus $p_{i,j} = 1/m_i$, $\forall j$. If we add the entropy of all the trajectories in a box, then we recover the Boltzmann expression for the entropy $S_i = \log(m_i)$, where $m_i$ are the different colors inside a box (the accessible microstates of the Boltzmann entropy). Then the equiprobable total entropy becomes $S = \sum_{i=1}^{N} S_i = \sum_{i=1}^{N}\log(m_i)$. Furthermore, if we have a grid on a given region of phase space, many boxes will have an equal number of colors. That is, many boxes will be in the interior or lie near the boundary between two or more basins. Then we can say that there are $N_k$ equal boxes (in the sense that they have the same number of colors), where $k \in [1,k_{\max}]$ is the label for the different boundaries. Boxes lying outside the basin boundaries do not contribute to the entropy as they only have one color. In other words, what matters is what happens at the basin boundaries. Then, the basin entropy reads

$$
S_b = \sum_{k=1}^{k_{\max}} \frac{N_k}{N}\log(m_k).
\tag{5}
$$

By following the method of the box-counting dimension $D_k$^18, by which we compute fractal dimensions of basin boundaries, the number of boxes that contains a boundary grows like $N_k = n_k\varepsilon^{-D_k}$ where $n_k$ is a positive constant. In the case of smooth boundaries, the equation $D_k = D - 1$ holds, $D$ being the dimension of the phase space. For fractal boundaries $D_k$ can be larger, but obviously we always have $D_k \leq D$. On the other hand, the number of boxes in the whole region of phase space, grows as $N = \tilde{n}\varepsilon^{-D}$, where $\tilde{n}$ is a positive constant. Substituting these expressions for $N_k$ and $N$ in Eq. 5, and recalling that $\alpha_k = D - D_k$ is the uncertainty exponent^15 for each boundary, we get

$$
S_b = \sum_{k=1}^{k_{\max}} \frac{n_k}{\tilde{n}} \varepsilon^{\alpha_k}\log(m_k).
\tag{6}
$$

This last expression reveals important information. The basin entropy has three components: the term $n_k/\tilde{n}$ is a normalization constant that accounts for the boundary size which is independent of $\varepsilon$; the term of the uncertainty exponent $\alpha_k$, is related with the fractality of the boundaries and contains the variation of the basin entropy with the box size; finally there is a term that depends on the number of different colors $m_k$. All these terms depend on the dynamics of the system, while the scaling box size $\varepsilon$ depends only on the geometry of the grid.

Equation 6 sheds light into some interesting questions. First, we can compare smooth boundaries ($\alpha_k = 1$) and fractal boundaries ($\alpha_k < 1$). For both of them, smooth and fractal basins, we get $S_b \to 0$ when $\varepsilon \to 0$, but it converges faster in the smooth case. That is, it is more difficult for the basin entropy to decrease its value in a system with fractal boundaries. Despite other important factors, fractal boundaries introduce a larger uncertainty than the smooth ones. Furthermore, if $\alpha_k = 0$ then $S_b > 0$ no matter the scaling box size (this might happen in riddled basins^19–21).

These ideas can be successfully applied for Wada basins. Basins exhibiting the Wada property have only one boundary that separates all the basins^12,22. We can argue that increasing the number of colors in the boundary boxes increases the basin entropy and therefore its uncertainty. In particular, having all possible colors in every boundary box is a unique situation found only in Wada basins. Nevertheless, Eq. 6 also reveals that some non-Wada basins can show larger basin entropy than others exhibiting the Wada property. This can be the case when a system has the Wada property but there is one basin which occupies most of the phase space. Other factors like the number of attractors and the boundary size also play a role in the uncertainty according to the basin entropy formulation. Therefore the Wada property increases the uncertainty under the basin entropy perspective, but each case must be carefully studied.

The basin entropy idea can also be used to develop new tools. In some cases, we may be interested only in the uncertainty of the boundaries. In particular, we often want to know if a boundary is fractal. For that purpose we can restrict the calculation of the basin entropy to the boxes falling in the boundaries, that is, we can compute the entropy only for those boxes $N_b$ which contain more than one color,

$$
S_{bb} = \frac{S}{N_b},
\tag{7}
$$

where $S$ is calculated in the same way described before (see Eq. 3). We refer to this number $S_{bb}$ as boundary basin entropy, because it quantifies the uncertainty referring only to the boundaries.

The nature of this quantity $S_{bb}$ is different from the basin entropy $S_b$ defined in Eq. 4. The $S_b$ is sensitive to the size of the basins, so it can distinguish between different basins with smooth boundaries, whilst the $S_{bb}$ cannot. However, it is worthwhile to introduce this new concept since it provides a sufficient condition to assess easily that some boundaries are fractal. Here is the reasoning. Suppose that we have several basins in a 2D phase space separated by smooth boundaries. Then, every box in the boundary will have only two colors, except a few countable number of boxes that may contain three colors or more. If we take a sufficient number of boxes in the boundaries, the effect of those boxes containing more than two colors will be negligible for the computation of the basin entropy in the boundaries $S_{bb}$. Then, the maximum possible value of $S_{bb}$ that a smooth boundary can show is $\log 2$, which would imply a pathological case where every box in the boundary contains equal proportions of two basins $p_i = 1/2$, $\forall i \in \mathbb{N}$. Therefore, considering a sufficient number of boxes in the boundaries, we can affirm that if the boundary basin entropy is larger than $\log 2$, then the boundary is fractal, which can be expressed as

$$
S_{bb} > \log 2 \Rightarrow \alpha < 1.
\tag{8}
$$

This is a sufficient but not necessary condition: as we shall discuss in Section 4.1, there may be fractal boundaries with $S_{bb} < \log 2$. Nevertheless, this threshold can be very useful to assess quickly the fractality of some boundaries, avoiding to compute the boundaries for different scales (which is not always possible). In Section 4.1, we will show on an example that the criterion (8) enables reliably to find parameter regions exhibiting fractal boundaries. A detailed proof of the $\log 2$ criterion can be found in the Supplementary Information.

## What does the basin entropy measure?

Here we illustrate the main features of basin entropy with several examples of dynamical systems, showing how its dependence on the boundary size $n_k/\tilde{n}$, the uncertainty exponent $\alpha_k$ and the number of attractors $N_A$.

The term $n_k/\tilde{n}$ corresponds to an estimate of the size of the boundary, since it normalizes the number of boxes containing the boundaries divided by the total number of boxes covering $\Omega$:

$$
\frac{N_k}{N} = \frac{n_k}{\tilde{n}}\varepsilon^{\alpha_k}.
\tag{9}
$$

To study the contribution of this term, we consider the damped Duffing oscillator given by

$$
\ddot{x} + \delta\dot{x} - x + x^3 = 0.
\tag{10}
$$

This equation describes the motion of a unit mass particle in a double well potential with dissipation. This system presents two attractive fixed points in $(\pm 1,0)$ of the $(x,\dot{x})$ phase space. The higher the damping coefficient $\delta$ the faster the orbits tend to the fixed points and, as a consequence, the basin of attraction appears more deformed for smaller values of $\delta$ (Fig. 3(a–c)). The damped Duffing oscillator is bistable, $N_A = 2$, and has a smooth boundary with uncertainty exponent $\alpha = 1$.

Observing the basins of attraction corresponding to the three different values of $\delta$, it is noticeable that the basin of Fig. 3(c) has a much simpler structure than the basin in Fig. 3(a). The outcome of an initial condition within an $\varepsilon$-box would be more difficult to predict in the second case. Nevertheless, both basins have the same uncertainty exponent $\alpha = 1$ since in both cases the boundary is smooth. The differences in the values of the basin entropy originates from the differences in the region of discretized phase space occupied by the boundary, that is, the boundary size, which is reflected by the term $n/\tilde{n}$ (indices have been dropped since now there is only one boundary).

To highlight this effect, we have computed the basin entropy $S_b$ versus the scaling box size $\varepsilon$ for three different values of the damping coefficient $\delta$. The results are shown in the log-log plot of Fig. 3(d), where each fit corresponds to a different value of $\delta$. We must note that we have normalized the region of the phase space, so that the values of the scaling box size $\varepsilon$ in all the plots of the paper are the inverse of the number of pixels used as a grid. By taking logarithms on both sides of Eq. 6, we have

$$
\log(S_b) = \log\left(\frac{n}{\tilde{n}}\right) + \log(\log(N_A)) + \alpha\log(\varepsilon).
\tag{11}
$$

Since in this case, we have $\alpha = 1$ and $N_A = 2$ for all our simulations, it is clear that the variation of the basin entropy with $\delta$ is entirely due to the term $n/\tilde{n}$. Most importantly, we have obtained values of the slope $\alpha = 1$ within the statistical error for all the fits. Therefore, although all these basins have the same uncertainty exponent, they have a different basin entropy for a given value of $\varepsilon$. The basin entropy is sensitive to their different structure and is able to quantify their associated unpredictability.

The fractal dimension of the boundaries also plays a crucial role in the formulation of the basin entropy. This is reflected in the uncertainty exponent $\alpha_k$^15 of Eq. 6. In order to highlight the effects of the variations in the uncertainty exponent, we have chosen a model that can display the Wada property^3. This means that there is only one fractal boundary separating all the basins. The model is the Hénon-Heiles Hamiltonian^23,

$$
H = \frac{1}{2}(\dot{x}^2+\dot{y}^2) + \frac{1}{2}(x^2+y^2) + x^2y - \frac{1}{3}y^3,
\tag{12}
$$

which describes the motion of a particle in an axisymmetrical potential well that for energy values above a critical one, the trajectories may escape from the bounded region inside the well and go on to infinity through three different exits. If we vary the energy from $E = 0.2$ to $E = 0.22$, the fractal dimension of the boundaries is modified with $E$, though the Wada property is preserved^24 (see Fig. 3(e–g)). The proportion of red, blue and green remains as a constant for these three basins, leading to constant values of the basin stability. However, the basin entropy accounts for their different structures.

As we compute the basin entropy for different scaling box sizes, we observe that the main effect of varying the parameter $E$ is a change of the slope in the log-log plot of Fig. 3(h). Equation 11 relates these changes in the slope to the uncertainty exponent $\alpha$ of the boundary. Smaller energies lead to smaller uncertainty exponents, since the boundaries have a more complex structure and consequently the slopes in the log-log plot decrease too. Obviously the offset also varies for the different values of the energy. This is related to changes in the boundary size $n/\tilde{n}$ which in this case cannot be completely separated from the changes in $\alpha$. This example shows that the scaling of the basin entropy with box size directly reflects the fractal dimension of the basin boundaries. For small box sizes this effect dominates and the largest fractal dimensions of the basins gives the largest basin entropies even though the offsets are different (see Fig. 3(h)).

The last factor that contributes to the basin entropy, according to Eq. 6, is the number of attractors $N_A$. In general, as the number of attractors increases, the uncertainty increases too, and so does the basin entropy. Furthermore, it is impossible to isolate the effect of the number of attractors from the contribution of the boundary size, since they are not independent: if a new attractor emerges while tuning a parameter, a new boundary is also created. We illustrate these effects using a simple map where the number of attractors can be tuned. This map comes from the Newton method to find the complex roots of unity $z^r = 1$^25, and can be written as

$$
z_{n+1} = z_n - \frac{z_n^r - 1}{rz_n^{r-1}},
\tag{13}
$$

where $z \in \mathbb{C}$ and $r,n \in \mathbb{N}$. The attractors of this map are the solutions of $z^r = 1$, so the parameter $r$ determines the number of attractors, $r = N_A$ (see Fig. 3(i–k) for $r = 4,5,6$). The basins of attraction of this system have disconnected Wada boundaries, that is, all the basins share the same boundaries and are disconnected^22.

From Eq. 11 we can predict that increasing the number of attractors increases the offset in the log-log plot of the basin entropy versus the box size. This can be observed in Fig. 3(l), where an increasing number of attractors leads to an increasing value of the basin entropy for all the $\varepsilon$ considered.

**Figure 3. Basin entropy ingredients.** (a–c) Basins of attraction of $\ddot{x}+\delta\dot{x}-x+x^3=0$. (d) Log-log plot of the basin entropy for different values of the scaling box size $\varepsilon$. The three basins have two attractors and $\alpha = 1$ (same slope in the log-log plot), but the boundary size $n_k/\tilde{n}$ is different and the basin entropy reflects it for each case. (e–g) Escape basins of the Hénon-Heiles Hamiltonian $H=\frac{1}{2}(\dot{x}^2+\dot{y}^2)+\frac{1}{2}(x^2+y^2)+x^2y-\frac{1}{3}y^3$. (h) The log-log plot of the basin entropy shows different slopes for each case, since the uncertainty exponent $\alpha$ varies. (i–k) The basins of attraction indicate the initial conditions that lead to the complex roots of unity using the Newton method described by $z_{n+1}=z_n-\frac{z_n^r-1}{rz_n^{r-1}}$. (l) The log-log plot shows that the basin entropy increases when the number of attractors increases, leading to larger values in the intercepts of the fits as predicted.

**Figure 3 description:** The figure is a multi-panel composite. Panels (a–c) show black-and-white basins of attraction of the damped Duffing oscillator in the $(x,\dot{x})$ phase space for $\delta=0.1$, $\delta=0.2$, and $\delta=0.3$, respectively. The horizontal axis is $x$ and the vertical axis is $\dot{x}$. Panel (a) has the most distorted smooth boundary bands; panels (b) and (c) become progressively simpler. Panel (d) is a log-log plot with horizontal axis $\log\varepsilon$ and vertical axis $\log S_b$, showing three approximately parallel increasing straight-line fits corresponding to the three $\delta$ values. Panels (e–g) show colored escape basins of the Hénon-Heiles Hamiltonian for $E=0.20$, $E=0.21$, and $E=0.22$, with axes $x$ and $y$; the basin patterns are three-colored and fractal-like inside a bounded region. Panel (h) is a log-log plot of $\log S_b$ versus $\log\varepsilon$ with three lines of different slopes for the three energy values. Panels (i–k) show colored basins of attraction for Newton’s method in the complex plane for $r=4$, $r=5$, and $r=6$, with axes $\Re(z)$ and $\Im(z)$; the number of colored sectors increases with $r$. Panel (l) is a log-log plot of basin entropy showing higher offsets as $r$ increases.

## Characterizing chaotic systems

### Basin Entropy Parameter Set

One of the most interesting applications of the basin entropy is to use it as a quantitative measure to compare different basins of attraction. We propose an analogy with the concept of chaotic parameter set^26, which is a plot that visually illustrates in a parameter plane when a dynamical system is chaotic or periodic by simply plotting the Lyapunov exponents for different pairs of parameters. Here, first we choose a given scaling box size $\varepsilon$, and then we evaluate the basin entropy associated to the corresponding basins of attraction for different parameter settings. We call the plot of the basin entropy in a two-dimensional parameter space basin entropy parameter set. To illustrate the possibilities of this technique, we study the periodically driven Duffing oscillator $\ddot{x}+\delta\dot{x}-x+x^3=F\sin\omega t$, whose dynamics can be very different depending on the parameters. We vary the forcing amplitude $F$ and the frequency $\omega$ of the driving, and for each basin we compute its corresponding basin entropy. We have used a resolution of $200 \times 200$ boxes ($\varepsilon = 0.005$) with 25 trajectories per box (a million trajectories per basin) to compute the basins of attraction and the same region of the phase space $\Omega = [-2.5,2.5]\times[-2.5,2.5]$ for all the pairs $(F,\omega)$.

The result is presented in Fig. 4(a), which is a color-code representation of the basin entropy in the parameter plane $(F,\omega)$ for different values of the forcing amplitude and frequency. The hot colors indicate higher values of the basin entropy, while the white pixels are for zero basin entropy. The set of parameters with zero basin entropy indicates that the basin of attraction has only one attractor. Although there is no uncertainty about the final attractor of any initial condition, trajectories may still be very complicated if the attractor is chaotic. This is actually the case for Fig. 4(b), where there is only one chaotic attractor.

The hottest point of the basin entropy parameter set corresponds to the basin of attraction shown in Fig. 4(c) with eight different attractors whose basins are highly mixed. The reason for having this high value of the basin entropy lies at a combination of a high number of attractors and the uncertainty exponent associated to the boundaries that makes basins of attraction more unpredictable. In Fig. 4(d), we can see a basin of attraction with extremely mixed basins, but it has only three attractors so its basin entropy is lower than for Fig. 4(c). The converse situation arises in Fig. 4(e), where there are sixteen different attractors but the boundaries are not very intricate.

Remarkably, it is also possible to explore the parameter space using only a few boxes instead of computing the high resolution basin for each parameter set. To infer a good approximation of the basin entropy, we applied a Monte Carlo sampling method. We have used 2000 boxes for each point in the parameter set, i.e., 50000 trajectories for each value of $(F,\omega)$, instead of the million trajectories needed for the usual procedure (we mean by usual procedure computing the whole basin of attraction and then calculate the basin entropy). Thus, we speed up the computation by a factor 20.

To evaluate the discrepancies between the usual procedure and the random sampling we have calculated the relative error $\varepsilon_{\mathrm{rel}} = 100 \times (S_b - S_b^{RS})/S_b$. For the 94% of the parameters evaluated the relative error in the basin entropy computation was less than 5% (see Fig. S2 in the Supplementary Information). If higher precision is desired one can always increase the number of boxes $N$, since the error decreases as $1/\sqrt{N}$ in the Monte Carlo method. Therefore, one can calculate the basin entropy using a small number of boxes and afterwards, one can compute with a finer grid the most interesting basins. The random sampling procedure is especially useful to compute the basin entropy for high dimensional systems or parameter sets.

**Figure 4. Basin entropy parameter set.** (a) Basin entropy parameter set for the periodically driven Duffing oscillator given by $\ddot{x}+\delta\dot{x}-x+x^3=F\sin\omega t$. It is a color-code map of the basin entropy for different values $(F,\omega)$ of the forcing amplitude and frequency, where we have fixed the scaling box size $\varepsilon=0.005$ and the damping coefficient $\delta=0.15$. We have used a color code where the hot colors represent larger values of the basin entropy. (b) Example of a basin of attraction with zero basin entropy because there is only one attractor, actually a chaotic attractor (whose Poincaré section is plotted in black), for the parameters $F=0.2575$ and $\omega=1.075$. (c) Basins of attraction corresponding to the highest value of the basin entropy in this parameter plane, for $F=0.2495$ and $\omega=1.2687$. (d) Basins of attraction with three attractors and a very low uncertainty exponent happening for $F=0.2455$ and $\omega=1.1758$. (e) Basins of attraction with sixteen different attractors for the parameters $F=0.3384$ and $\omega=0.2929$.

**Figure 4 description:** The main panel (a) is a color-coded parameter map with horizontal axis $F$ and vertical axis $\omega$, showing basin entropy values from low/white to hot colors. It includes white regions indicating zero basin entropy and colored bands/arcs indicating higher entropy. Black connector lines point from selected regions of panel (a) to four surrounding basin examples. Panel (b), upper left, is a plot in the $(x,\dot{x})$ plane with a black Poincaré section, representing one chaotic attractor. Panel (c), upper right, is a highly mixed multicolored basin plot with many fine red, blue, green, and other colored regions. Panel (d), lower right, shows a densely mixed three-color basin with speckled structure. Panel (e), lower left, shows a multicolored basin with large coherent colored domains and smooth-looking boundaries. The central color scale in panel (a) ranges approximately from 0 to 1.4.

### Log2 criterion

Using the same data, we can also study the boundary basin entropy $S_{bb}$ in the parameter plane. This quantity reflects the uncertainty associated to the boundaries, and we have seen in Section 2 that if $S_{bb} > \log 2$ then the boundary is fractal. For a given scaling box size $\varepsilon$, this process cannot distinguish a true fractal boundary from a smooth boundary which at this scale separates more than two basins inside one box. The results for the periodically driven Duffing oscillator are depicted in the colormap of Fig. 5(a), where white color is assigned to the pairs $(F,\omega)$ displaying only one attractor. By means of this plot we can detect parameter regimes where boundaries are fractal, depicted with hot colors. Figure 5(b) shows the values of the uncertainty exponent, using hot colors for the parameters with fractal boundaries. Comparing Fig. 5(a,b), we can confirm that the $\log 2$ criterion is a sufficient but not necessary condition for fractal boundaries. Indeed, the $\log 2$ criterion works only for cases with three or more basins (see Fig. S3 in the Supplementary Information). Nevertheless the $\log 2$ criterion can be used to ascertain the fractality for basins of comparable size, and is much faster to compute than the direct determination of fractal dimension since it does not require the use of different scales. This makes it especially appealing for experimental settings where the resolution cannot be tuned at will.

**Figure 5. Log2 criterion comparison.** (a) A color map of the boundary basin entropy $S_{bb}$ for different parameters $(F,\omega)$ for the periodically driven Duffing oscillator $\ddot{x}+\delta\dot{x}-x+x^3=F\sin\omega t$ for $\delta=0.15$ and $\varepsilon=0.005$. Hot colors are for basins with $S_{bb}>\log 2$ (b) Uncertainty exponent in the parameter plane. Hot colors indicate fractal boundaries. These figures confirm that the $\log 2$ criterion is a sufficient but not necessary condition for fractal boundaries.

**Figure 5 description:** The figure contains two color maps labeled (a) and (b), both with horizontal axis $F$ and vertical axis $\omega$, covering approximately $F=0.1$ to $0.5$ and $\omega=0$ to $2.5$. Panel (a) shows the boundary basin entropy $S_{bb}$, with a color bar ranging approximately from 0 to 1; red/yellow regions indicate larger boundary basin entropy and white regions indicate one-attractor regimes. Panel (b) shows the uncertainty exponent in the same parameter plane, with a color scale marked by $\log[2]$ and hot colors indicating fractal boundaries. The two panels have similar large-scale structures but differ in which parameter regions are highlighted as fractal or high-entropy.

## Discussion

The basin entropy quantifies the final state unpredictability of dynamical systems. It constitutes a new tool for the exploration of the uncertainty in nonlinear dynamics. This should become a very useful tool with a wide range of applications, as exemplified by the different systems that we have used to illustrate this concept. For instance, escape basins are widely used in astronomy, as shown in recent studies on the Pluto-Charon system^27. In these investigations it is commonly argued that basins close to the escape energy present a higher degree of fractalization^28,29. Here we have shown an example of an open Hamiltonian system used in galactic dynamics, namely the Hénon-Heiles potential, and we have been able to quantify its uncertainty for different values of the energy.

Another kind of problems where basins of attraction are very common is in iterative algorithms. Such algorithms abound in all sort of research fields, where basins of attraction are used to visualize the sensitivity of different methods^30,31. In this work we have applied the basin entropy idea to a prototypical iterative algorithm: the Newton method to find complex roots. We have quantified the uncertainty associated to this algorithm for different numbers of roots. The basin entropy technique can be used to compare the performances of different algorithms or to see how modifications in some parameters like the damping may alter the uncertainty of the iterative processes.

The concept of basin entropy also contributes to quantify the uncertainty of the Wada property, a recurring issue in the literature^3,11–14. Moreover, using the idea of boundary basin entropy, we provide a sufficient condition to test the fractality of the boundaries. In contrast with other methods like the box-counting dimension that require computation at different resolutions, the $\log 2$ criterion can be used with a fixed resolution. We believe that this opens a new window for experimental demonstrations of fractal boundaries.

We have also proposed a new technique called basin entropy parameter set, that can flesh out the information given by bifurcation diagrams and chaotic parameter sets. Combined with Monte Carlo sampling, the basin entropy parameter set can also be used as a quick guide to find sets of parameters leading to simple or more complicated basins of attraction.

We believe that the concept of basin entropy will become an important tool in complex systems studies with applications in multiple scientific fields especially those with multistability and other scientific areas as well.

## References

1. Nusse, H. E. & Yorke, J. A. Basins of attraction. *Science* **271**, 1376–1380 (1996).

2. Aguirre, J., Viana, R. L. & Sanjuán, M. A. F. Fractal structures in nonlinear dynamics. *Rev. Mod. Phys.* **81**, 333–386 (2009).

3. Aguirre, J., Vallejo, J. C. & Sanjuán, M. A. F. Wada basins and chaotic invariant sets in the Hénon-Heiles system. *Phys. Rev. E* **64**, 66208 (2001).

4. Kolmogorov, A. N. New metric invariant of transitive dynamical systems and endomorphisms of Lebesgue spaces. *Doklady of Russian Academy of Sciences* **119**, 861–864 (1959).

5. Sinai, Y. G. On the notion of entropy of a dynamical system. *Doklady of Russian Academy of Sciences* **124**, 768–771 (1959).

6. Adler, R. L., Konheim, A. G. & McAndrew, M. H. Topological entropy. *Trans. Amer. Math. Soc.* **114**, 309–319 (1965).

7. Hunt, B. R. & Ott, E. Defining chaos. *Chaos* **25**, 97618 (2015).

8. Károlyi, G., Péntek, A., Scheuring, I., Tél, T. & Toroczkai, Z. Chaotic flow: The physics of species coexistence. *PNAS* **97**, 13661–13665 (2000).

9. Rabinovich, M., Huerta, R. & Laurent, G. Transient dynamics for neural processing. *Science* **321**, 48–50 (2008).

10. Brock, W. & Hommes, C. A rational route to randomness. *Econometrica* **65**, 1059–1096 (1997).

11. Vandermeer, J. Wada basins and qualitative unpredictability in ecological models: a graphical interpretation. *Ecol. Model.* **176**, 65–74 (2004).

12. Kennedy, J. & Yorke, J. A. Basins of Wada. *Physica D* **51**, 213–225 (1991).

13. Nusse, H. E. & Yorke, J. A. Characterizing the basins with the most entangled boundaries. *Ergod. Theor. Dyn. Syst.* **23**, 895–906 (2003).

14. Aguirre, J. & Sanjuán, M. A. F. Unpredictable behavior in the Duffing oscillator: Wada basins. *Physica D* **171**, 41–51 (2002).

15. Grebogi, C., McDonald, S. W., Ott, E. & Yorke, J. A. Final state sensitivity: An obstruction to predictability. *Phys. Lett. A* **99**, 415–418 (1983).

16. Grebogi, C., Kostelich, E., Ott, E. & Yorke, J. A. Multi-dimensioned intertwined basin boundaries and the kicked double rotor. *Phys. Lett. A* **118**, 448–452 (1986).

17. Menck, P. J., Heitzig, J., Marwan, N. & Kurths, J. How basin stability complements the linear-stability paradigm. *Nat. Phys.* **9**, 89–92 (2013).

18. Alligood, K. T., Sauer, T. D. & Yorke, J. A. *Chaos: An Introduction to Dynamical Systems.* (Springer, 1996).

19. Alexander, J. C., Yorke, J. A., You, Z. & Kan, I. Riddled basins. *Int. J. Bifurcat. Chaos* **2**, 795–813 (1992).

20. Ott, E., Sommerer, J. C., Alexander, J. C., Kan, I. & Yorke, J. A. Scaling behavior of chaotic systems with riddled basins. *Phys. Rev. Lett.* **71**, 4134–4137 (1993).

21. Lai, Y.-C. & Winslow, R. L. Geometric properties of the chaotic saddle responsible for supertransients in spatiotemporal chaotic systems. *Phys. Rev. Lett.* **74**, 5208–5211 (1995).

22. Daza, A., Wagemakers, A., Sanjuán, M. A. F. & Yorke, J. A. Testing for basins of Wada. *Sci. Rep.* **5**, 16579 (2015).

23. Hénon, M. & Heiles, C. The applicability of the third integral of motion: Some numerical experiments. *Astron. J* **69**, 73 (1964).

24. Blesa, F., Seoane, J. M., Barrio, R. & Sanjuán, M. A. F. To escape or not to escape, that is the question - perturbing the Hénon-Heiles Hamiltonian. *Int. J. Bifurcat. Chaos* **22**, 1230010 (2012).

25. Epureanu, B. & Greenside, H. Fractal basins of attraction associated with a damped Newton’s method. *SIAM Rev.* **40**, 102–109 (1998).

26. Sanjuán, M. A. F. Using nonharmonic forcing to switch the periodicity in nonlinear systems. *Phys. Rev. E* **58**, 4377–4382 (1998).

27. Zotos, E. E. Orbit classification in the planar circular Pluto-Charon system. *Astrophys. Space Sci.* **360**, 1–14 (2015).

28. Zotos, E. E. Escape dynamics and fractal basin boundaries in Seyfert galaxies. *Nonlinear Dyn.* **80**, 1109–1131 (2015).

29. Ernst, A. & Peters, T. Fractal basins of escape and the formation of spiral arms in a galactic potential with a bar. *Mon. Not. R. Astron. Soc.* **443**, 2579–2589 (2014).

30. Asenjo, D., Stevenson, J. D., Wales, D. J. & Frenkel, D. Visualizing basins of attraction for different minimization algorithms. *J. Phys. Chem. B* **117**, 12717–12723 (2013).

31. van Turnhout, M. & Bociort, F. Instabilities and fractal basins of attraction in optical system optimization. *Opt. Express* **17**, 314 (2009).

## Acknowledgements

This work was supported by Spanish Ministry of Economy and Competitiveness under Project No. FIS2013-40653-P. Financial support from the Programme Investissements d’Avenir under the program ANR-11-IDEX-0002-02, reference ANR-10-LABX-0037-NEXT is also acknowledged.

## Author Contributions

A.D., A.W., B.G., D.G.-O. and M.A.F.S. devised the research. A.D. performed the numerical simulations. A.D., A.W., B.G., D.G.-O. and M.A.F.S. analyzed the results and wrote the paper.

## Additional Information

Supplementary information accompanies this paper at http://www.nature.com/srep

Competing financial interests: The authors declare no competing financial interests.

How to cite this article: Daza, A. et al. Basin entropy: a new tool to analyze uncertainty in dynamical systems. *Sci. Rep.* **6**, 31416; doi: 10.1038/srep31416 (2016).

This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/

© The Author(s) 2016