```
# Modeling and Forecasting Time Series of Compositional Data: A Generalized Dirichlet Power Steady Model

Mohamad Mehdi\(^{1}\) (B), Elise Epaillard\(^{3}\), Nizar Bouguila\(^{2}\), and Jamal Bentahar\(^{2}\)

\(^{1}\) Engineering and Computer Science, Concordia University, Montreal, Canada  
mo mehdi@encs.concordia.ca

\(^{2}\) Concordia Institute for Information Systems Engineering, Concordia University, Montreal, Canada  
\{bouguila,bentahar\}@ciise.concordia.ca

\(^{3}\) ELectrical and Computer Engineering, Concordia University, Montreal, Canada  
e epail@encs.concordia.ca

© Springer International Publishing Switzerland 2015  
C. Beierle and A. Dekhtyar (Eds.): SUM 2015, LNAI 9310, pp. 170–185, 2015.  
DOI: 10.1007/978-3-319-23540-0_12

## Abstract

This paper presents GDPSM a power steady model (PSM) based on generalized Dirichlet observations for modeling and predicting compositional time series. The model’s unobserved states evolve according to the generalized Dirichlet conjugate prior distributions. The observations’ distribution is transformed into a set of Beta distributions each of which is re-parametrized as a unidimensional Dirichlet in its exponential form. We demonstrate that dividing the modeling problem into multiple smaller problems leads to more accurate predictions. We evaluate this model with the web service selection application. Specifically, we analyze the proportions of the quality classes that are assigned to the web services interactions. Our model is compared with another PSM that assumes Dirichlet observations. The experiments show promising results in terms of precision errors and standardized residuals.

**Keywords:** Time series · State space models · Generalized Dirichlet

## 1 Introduction

Time series of continuous proportions or compositional data, have been analyzed and modeled using various approaches [1,5]. This kind of series presents itself in domains varying from economics (e.g., yearly gross domestic product), to chemistry (e.g., chemical compositions), to political sciences (e.g., vote and seat shares). Generally, time series of compositional data are multivariate and denoted by time-dependent vectors of proportions that sum to one. To model such data, one might resort to standard techniques such as the multivariate autoregressive integrated moving average (ARIMA) [17] and Kalman filters [9]. However, due to the positive nature of the components of compositional data and their sum to one constraint, these techniques are not applicable [1].

Various approaches have been proposed to deal with the positivity and dependence of the compositional data’s components. For instance, Aitchison proposed the mapping of the data from the positive simplex $S^d = \{(s_1,\ldots,s_d), \text{ s.t. } \sum_{i=1}^d s_i < 1\}$, to the $d$-dimensional real space $\mathbb{R}^d$ [1]. Specifically, he suggested the additive and multiplicative logistic transforms. Inspired by Aitchison’s proposals, the authors in [5] employed the multivariate ARIMA to model compositional time series transformed using the above additive logistic transform. The practicality of this transform has been shown via a public opinion polls application. However, one limitation of such approach is dealing with zero values of $s_i$ which yield $y_i = \pm \infty$. In the same line of research, [12] used the same transform with multivariate dynamic linear models. To circumvent the zero-infinity issue, looking for a replacement for the additive transformation might be the answer. For instance, [19] proposed an alternative approach that employs a hyperspherical transform. This was intended to overcome the positivity and unit-sum constraints of compositional data. It also promised to solve the problems that arise with cases that have zero-valued components. This approach is based on modeling each component of the time series by the available data instances. The time series are first mapped through a non-linear dimensionality reduction approach onto a hypersphere. As such, the dimension $d$ of a time series is reduced to $d-1$. Furthermore, [2] suggested the Box-Cox transformation which is a general form of the additive logistic transformation. Afterwards, the authors proposed a regression model, framed in a dynamic Bayesian structure, to model compositional time series.

Additionally, forecasting is another major part of the body of time series literature. [7] provides a review for time series forecasting models including exponential smoothing methods, ARIMA, state space and structural models, Kalman filters, and autoregressive conditional heterscedastic models. A stochastic extension to traditional autoregressive moving average (ARMA) time series models was proposed in [16]. State space models consist of observation and state processes that may be non-linear and non-Gaussian. The main usage of such models is to deduce the properties of the states given the knowledge from the observations. It is noteworthy to mention that all ARMA and ARIMA may be written as state space models. In the case of linear processes, Kalman filters are used to solve the corresponding state space models. The authors in [8] developed a Dirichlet state space model to forecast compositional time series. They also propose an estimation approach of the trends, covariates, and interventions in time series. A motor vehicle production data set that consists of the number of vehicle production in Japan, the United States, and the rest of the world during the years 1947 to 1987.

**Motivation:** As mentioned earlier, a wide range of real applications in varied domains involve compositional time series. The majority of these applications handle series that consist of yearly, quarterly, or monthly proportions. However, with the plethora of online data, some compositional time series may arise on a daily or even hourly basis. For example, the geographic distribution of the users of social media websites may be measured on an hourly basis for various business related functions. Therefore, given the large amount of available data, the need to understand this data, and the benefits in turning it into actionable insights, building a modeling and forecasting model for compositional time series becomes of unprecedented significance.

**Contributions:** In this paper, we build upon and extend the literature of compositional time series forecasting by the following contributions. (1) We propose to model and forecast compositional time series based on a novel PSM in which the observations are assumed to follow a generalized Dirichlet (GD) distribution. (2) We transform the GD distribution of $d$ dimensions to $d$ Beta distributions which, in turn, are transformed to $d$ unidimensional Dirichlet distributions in their exponential form. This approach partitions the modeling and forecasting of $(d + 1)$-dimensional time series into $d$ smaller problems with fewer parameters to learn. (3) We evaluate our model with a new application, web service selection, in comparison to outdated ones used in the literature. (4) We compare our model’s forecasting performance to that of the Dirichlet-based power steady model (DPSM) proposed in [8]. We show the merits of our model via standardized residuals and mean squared error (MSE) of the predictions.

The rest of the paper is organized as follows. Section 2 describes the GD distribution and the transformations that it undergoes to be represented by multiple Dirichlet distributions. Section 3 highlights the characteristics of state space models and the details of the proposed time series model based on the GDPSM are described in Sect. 4. The experimental evaluation of the proposed model using various simulated data are presented and discussed in Sect. 5. Section 6 concludes the paper by summarizing its main contributions and suggesting directions for future work.

## 2 Generalized Dirichlet Formulation

Let $X = (X_1,\ldots,X_{d+1})$ denote a vector of proportions that follows a $d$-dimensional GD distribution with the parameters vector $\alpha = (\alpha_1,\beta_1,\ldots,\alpha_d,\beta_d)$. The probability distribution function of $X$ is given by:

$$
p(X_1,\ldots,X_d)
=
\prod_{l=1}^{d}
\frac{\Gamma(\alpha_l + \beta_l)}{\Gamma(\alpha_l)\Gamma(\beta_l)}
X_l^{\alpha_l-1}
\left(1-\sum_{j=1}^{l} X_j\right)^{\gamma_l},
\tag{1}
$$

for $\sum_{l=1}^d X_l < 1$ and $0 < X_l < 1$, for $l = 1,\ldots,d$, where $\alpha_l > 0$, $\beta_l > 0$, $\gamma_l = \beta_l - \alpha_{l+1} - \beta_{l+1}$, for $l = 1,\ldots,d - 1$, and $\gamma_d = \beta_d - 1$. Also, note that:

$$
\Gamma(x) = \int_0^\infty t^{x-1} e^{-t} \, dt.
$$

Since $X$ follows a generalized Dirichlet and is completely neutral, it can be transformed to $d$ independent Beta distributions [3,20]. Let $Y = (Y_1,\ldots,Y_d)$ be the result of the following transformation:

$$
Y_j =
\begin{cases}
X_j, & \text{if } j = 1,\\[4pt]
\dfrac{X_j}{1-X_1-\cdots-X_{j-1}}, & \text{if } 2 \leq j \leq d.
\end{cases}
\tag{2}
$$

The parameters vector $\alpha$ can be estimated by considering that each of the $Y_j$ has a Beta distribution with parameters $\alpha_j$ and $\beta_j$. Therefore, the joint probability distribution of $Y$ can be written as follows:

$$
p(Y \mid \alpha)
=
\prod_{l=1}^{d}
B(\alpha_l,\beta_l)^{-1} Y_l^{\alpha_l-1}(1-Y_l)^{\beta_l-1},
\tag{3}
$$

where $B(\alpha_l,\beta_l) = \dfrac{\Gamma(\alpha_l)\Gamma(\beta_l)}{\Gamma(\alpha_l+\beta_l)}$. The Beta distribution belongs to the exponential family in which each density is given by the following:

$$
p(Y \mid \theta)
=
H(Y)\exp\left(\sum_{s=1}^{S} \eta_s(\theta) T_s(Y) + \Phi(\theta)\right),
\tag{4}
$$

where $\eta_s(\theta)$ are called the natural parameters, $T_s(Y)$ are the sufficient statistics, $H(Y)$ is a base measure, and $\Phi(\theta)$ is referred to as the log-partition function.

Equation (3) can thus be written as an exponential density:

$$
p(Y \mid \alpha)
=
\exp\left(
\sum_{l=1}^{d}
\log(B(\alpha_l,\beta_l)^{-1})
+
(\alpha_l-1)\log Y_l
+
(\beta_l-1)\log(1-Y_l)
\right)
$$

$$
=
\prod_{l=1}^{d}\frac{1}{Y_l(1-Y_l)}
\exp\left(
\sum_{l=1}^{d}
\log\left(
\frac{\Gamma(\alpha_l+\beta_l)}{\Gamma(\alpha_l)\Gamma(\beta_l)}
\right)
+
\alpha_l \log Y_l
+
\beta_l \log(1-Y_l)
\right).
\tag{5}
$$

Let $S = 2d$, then we have:

$$
H(Y) = \prod_{l=1}^{d}\frac{1}{Y_l(1-Y_l)},
\tag{6}
$$

$$
T_l(Y) =
\begin{cases}
\log Y_l, & \text{for } l = 1,\ldots,d,\\[4pt]
\log(1-Y_{l-d}), & \text{for } l = d+1,\ldots,2d,
\end{cases}
\tag{7}
$$

$$
\eta_l(\theta) =
\begin{cases}
\alpha_l, & \text{for } l = 1,\ldots,d,\\[4pt]
\beta_{l-d}, & \text{for } l = d+1,\ldots,2d,
\end{cases}
\tag{8}
$$

$$
\Phi(\theta)
=
\sum_{l=1}^{d}
\log\left(
\frac{\Gamma(\alpha_l+\beta_l)}{\Gamma(\alpha_l)\Gamma(\beta_l)}
\right).
\tag{9}
$$

In the case of exponential density functions, a conjugate prior on $\theta$ is of the following form [13]:

$$
\pi(\theta) \propto \exp\left(\sum_{s=1}^{S}\rho_s \eta_s(\theta) + \kappa \Phi(\theta)\right),
\tag{10}
$$

where $(\rho_1,\ldots,\rho_S)$ and $\kappa$ are the prior’s hyperparameters. Therefore, the conjugate prior family to $d$-dimensional GD distributions transformed to $d$ independent Beta written in their exponential form (Eq. (5)) is given by:

$$
\pi(\theta) \propto
\exp\left(
\sum_{l=1}^{d}\rho_l \alpha_l
+
\sum_{l=d+1}^{2d}\rho_l \beta_{l-d}
+
\kappa \sum_{l=1}^{d}
\log\left(
\frac{\Gamma(\alpha_l+\beta_l)}{\Gamma(\alpha_l)\Gamma(\beta_l)}
\right)
\right).
\tag{11}
$$

The $d$ Beta distributions that generate $Y$, are also simplified unidimensional Dirichlet distributions. In $K + 1$ dimensions, the Dirichlet density of a vector of proportions, $Y = (Y_1,\ldots,Y_{K+1})$, is given by:

$$
p(Y \mid \alpha)
=
\frac{\Gamma\left(\sum_{j=1}^{K+1}\alpha_j\right)}
{\prod_{j=1}^{K+1}\Gamma(\alpha_j)}
\prod_{j=1}^{K+1} Y_j^{\alpha_j-1},
\tag{12}
$$

where $\alpha = (\alpha_1,\ldots,\alpha_{K+1})$ is the parameters vector, $\sum_{j=1}^{K+1} Y_j = 1$ and $0 < Y_j < 1$. This distribution can also be depicted by $Y \sim \operatorname{Dir}(\alpha)$. In the exponential form, the density (12) becomes:

$$
p(X \mid \theta)
=
\exp\left(
\log\left(
\Gamma\left(\sum_{l=1}^{K+1}\alpha_l\right)
\right)
-
\sum_{l=1}^{K+1}\log(\Gamma(\alpha_l))
+
\sum_{l=1}^{K+1}\alpha_l \log(X_l)
-
\sum_{l=1}^{K+1}\log(X_l)
\right).
\tag{13}
$$

In [8], Eq. (13) is re-parametrized to separate the effects of its mean,

$$
\theta =
\left(
\frac{\alpha_1}{\sum_{j=1}^{K+1}\alpha_j},
\ldots,
\frac{\alpha_{K+1}}{\sum_{j=1}^{K+1}\alpha_j}
\right),
$$

and spread

$$
\tau = \sum_{j=1}^{K+1}\alpha_j.
$$

As a result, we get:

$$
p(Z \mid \theta,\tau)
=
\exp\left(
\tau Z^T \theta
+
\tau \frac{\sum_{j=1}^{K+1} W_j}{K+1}
-
\log\left(
\frac{\prod_{j=1}^{K+1}\Gamma(\theta_j \tau)}
{\Gamma\left(\sum_{j=1}^{K+1}\theta_j \tau\right)}
\right)
\right),
\tag{14}
$$

where $W = \log(X)$ and $Z = W - \dfrac{\sum_{l=1}^{K+1} W_l}{K+1}$. In case $K = 2$, the Beta distribution of each $Y_j$ can be written in the exponential form of a unidimensional Dirichlet as follows:

$$
p(Y_j \mid \theta)
=
\exp\left(
\log\left(
\frac{\Gamma(\alpha_1 + \alpha_2)}{\Gamma(\alpha_1)\Gamma(\alpha_2)}
\right)
+
\alpha_2 \log(1-Y_j)
+
\alpha_1 \log(Y_j)
-
\log(Y_j)
-
\log(1-Y_j)
\right).
\tag{15}
$$

Following the same re-parametrization, Eq. (15) becomes:

$$
p(Z'_j \mid \theta',\tau')
=
\exp\left(
\tau' \left(Z_j^{\prime T}\theta' + W'_j\right)
-
\log\left(
\frac{\prod_{l=1}^{K}\Gamma(\theta'_l \tau')}
{\Gamma\left(\sum_{l=1}^{K}\theta'_l \tau'\right)}
\right)
\right),
\tag{16}
$$

where

$$
\theta' = \left(\theta'_1 = \frac{\alpha_1}{\tau'}, \theta'_2 = \frac{\alpha_2}{\tau'}\right), \qquad
\tau' = \alpha_1 + \alpha_2,
$$

$$
W'_j = \frac{\log(Y_j) + \log(1-Y_j)}{2},
$$

and

$$
Z'_j =
\left(
\log(Y_j) - W'_j,\,
\log(1-Y_j) - W'_j
\right).
$$

Given these parameters, we represent the distribution of $Y$ by $Y \sim \operatorname{DirBeta}(\tau' \theta')$. A conjugate prior family to the Dirichlet distributions in their exponential form is:

$$
p(\theta' \mid \lambda,\kappa,\tau')
\propto
\exp\left(
\lambda
\left(
\tau' \kappa^T \theta'
-
\log\left(
\frac{\Gamma(\tau' \theta'_1)\Gamma(\tau' \theta'_2)}
{\Gamma(\tau' \theta'_1 + \tau' \theta'_2)}
\right)
\right)
\right).
\tag{17}
$$

## 3 State Space Models

Dynamic linear models (DLM) can be represented in what is called a state space form. This representation consists in identifying the change of an observed variable (aka observation vector) in terms of another unobserved variable (aka state vector). The authors in [10] proposed a steady model for DLM that is only defined for normal distributions and is equivalent to an ARIMA(0,1,1) model. However, [14] generalized this model by redefining it across non-Gaussian distributions. More specifically, it was generalized to cases where the conditional probability of the observations given the states follows an exponential family distribution. The generalized model, also known as the PSM, is defined by:

$$
p(x_t \mid y^t) \sim PR(\omega),
\qquad
p(x_{t+1} \mid y^t) \propto p(x_t \mid y^t)^k,
\tag{18}
$$

where $0 < k < 1$ and $PR(\omega)$ is the conjugate prior for the exponential family distribution of $p(y_t \mid x_t)$. This model was first developed to be applied to univariate observations. However, [15] generalized the PSM of a time series to handle multivariate processes. Specifically, a symmetric multivariate PSM in which the process evolution is defined based on the density of the parameter vector is proposed. This generalization was also introduced as part of a Bayesian forecasting framework. However, this model undergoes some limitations when the observations follow a Dirichlet distribution [8], which are mostly due to the fact that the PSM estimates both the dispersion and location of the distribution at the same time. This problem can be solved by using the re-parametrized form of the Dirichlet distribution (Eq. (13)) which allows the separation of the dispersion $\tau$ and the location $\theta$.

## 4 Generalized Dirichlet Power Steady Model (GDPSM)

Given a time series of proportions denoted by $X : \{X^t = (X_1^t,\ldots,X_{d+1}^t)\}$, where $t = 1,\ldots,T$, we first assume that each vector in this time series follows a GD distribution $X^t \sim GD(\alpha_1^t,\ldots,\alpha_d^t,\beta_1^t,\ldots,\beta_d^t)$. Afterward, we apply the geometric transformation denoted by Eq. (2) on each of these vectors [3,4]. Using this transformation, $X^t$ is transformed to $W_t$ that follows a Beta distribution with parameters $(\alpha_l^t,\beta_l^t)$ which define the GD distribution of $X^t$, where $1 \leq l \leq d$. Since Beta distributions are special cases of Dirichlet distributions, we finally model the time series by $T \times d$ unidimensional Dirichlet distributions, $X_l^t = \operatorname{Dir}(\alpha_{l1}^t,\alpha_{l2}^t)$. Each of the $T \times d$ distributions is then re-parametrized as per Eqs. (15) and (16). Subsequently, we build $T \times d$ state space models, each of which is based on an unobserved state $\theta'_t$, to model each of the observations $(W_{11},\ldots,W_{1d},\ldots,W_{T1},\ldots,W_{Td})$. These observations are denoted by:

$$
(W_{tj} \mid \theta'_t,\tau'_t) \sim \operatorname{DirBeta}(\tau'_t \theta'_t),
\tag{19}
$$

where $1 \leq j \leq d$ and $\theta'_t$ follows the PSM given by Eq. (18). In other words, the conditional probability of $\theta'_{t+1}$ given the observations $W_{1j},\ldots,W_{tj}$, is defined as:

$$
p(\theta'_{t+1} \mid W^t) \propto p(\theta'_t \mid W^t)^\gamma
\qquad \text{where } 0 < \gamma < 1.
\tag{20}
$$

Equation (20) reveals an interesting property of the $(\theta'_{t+1} \mid W^t)$ and $(\theta'_t \mid W^t)$ distributions; their modes are equal, but the dispersion of the former is greater.

### 4.1 Time Series Model

The GD time series model is defined by two steps similar to those of a Gaussian Kalman filter: a prediction and an update step. In the prediction step, $p(\theta'_{t+1}\mid W^t)$ is computed using Eq. (20). Both sides of this equation follow the conjugate prior given by Eq. (17), each with different parameters. Formally, this is given by:

$$
p(\theta'_{t+1} \mid W^t)
\sim
\exp\left(
\lambda_{t+1\mid t}
\left(
\tau'_t \kappa_{t+1\mid t}^T \theta'_{t+1}
-
\log
\left(
\frac{
\Gamma(\tau'_t \theta'_{t+1,1})\Gamma(\tau'_t \theta'_{t+1,2})
}{
\Gamma(\tau'_t \theta'_{t+1,1} + \tau'_t \theta'_{t+1,2})
}
\right)
\right)
\right),
\tag{21}
$$

$$
p(\theta'_t \mid W^t)
\sim
\exp\left(
\lambda_{t\mid t}
\left(
\tau'_t \kappa_{t\mid t}^T \theta'_t
-
\log
\left(
\frac{
\Gamma(\tau'_t \theta'_{t1})\Gamma(\tau'_t \theta'_{t2})
}{
\Gamma(\tau'_t \theta'_{t1} + \tau'_t \theta'_{t2})
}
\right)
\right)
\right).
\tag{22}
$$

The prediction step consists of Eq. (24), which is a known fact and (25), which is derived by taking the log of Eq. (20), and the two equations above:

$$
\lambda_{t+1\mid t}
\left(
\tau'_t \kappa_{t+1\mid t}^T \theta'
-
\log
\left(
\frac{
\Gamma(\tau'_t \theta'_1)\Gamma(\tau'_t \theta'_2)
}{
\Gamma(\tau'_t \theta'_1 + \tau'_t \theta'_2)
}
\right)
\right)
=
\gamma \lambda_{t\mid t}
\left(
\tau'_t \kappa_{t\mid t}^T \theta'
-
\log
\left(
\frac{
\Gamma(\tau'_t \theta'_1)\Gamma(\tau'_t \theta'_2)
}{
\Gamma(\tau'_t \theta'_1 + \tau'_t \theta'_2)
}
\right)
\right).
\tag{23}
$$

knowing that:

$$
\kappa_{t+1\mid t} = \kappa_{t\mid t},
\tag{24}
$$

therefore,

$$
\lambda_{t+1\mid t} = \gamma \lambda_{t\mid t}.
\tag{25}
$$

$\gamma$ is a model parameter, such that $0 < \gamma < 1$. As for the update step, we need to compute $p(\theta'_{t+1}\mid W^{t+1})$ which, according to Bayes’ theorem, can be written as:

$$
p(\theta'_{t+1} \mid W^{t+1}) = p(W_{t+1} \mid \theta'_{t+1}) \times p(\theta'_{t+1}),
\tag{26}
$$

where $p(W_{t+1} \mid \theta'_{t+1})$ is the data likelihood that follows, in this case, the GD reformulated as $\operatorname{DirBeta}(\tau'_t\theta'_t)$ and given by Eq. (16). $p(\theta'_{t+1})$ is the prior and is given by Eq. (17). Therefore, applying the log to both sides of Eq. (26) yields the following:

$$
\lambda_{t+1\mid t+1} = \lambda_{t+1\mid t} + 1,
\tag{27}
$$

$$
\kappa_{t+1\mid t+1}
=
\left(
1 - \frac{1}{\lambda_{t+1\mid t+1}}
\right)\kappa_{t+1\mid t}
+
\frac{1}{\lambda_{t+1\mid t+1}} z_{t+1}.
\tag{28}
$$

### 4.2 Model Evaluation

We evaluate our model by the standardized residuals, the mean squared error (MSE) of the predictions, and the correlations between the residuals at lag 0. We compare our results with those of DPSM. The standardized residuals are computed as follows [8]:

$$
R_t = \frac{Z_t - E[Z_t \mid D_{t-1}]}{\operatorname{var}[Z_t \mid D_{t-1}]},
\tag{29}
$$

where $D_{t-1}$ denotes all the observations available at time $(t-1)$. $E[Z_t \mid D_{t-1}]$ and $\operatorname{var}[Z_t \mid D_{t-1}]$ are the respective posterior mean and variance of the prediction density, formally given by:

$$
p(Z_{t+1} \mid W^t) = \int p(Z_{t+1} \mid \theta_{t+1}) p(\theta_{t+1} \mid W^t)\, d\theta_{t+1}.
\tag{30}
$$

Since there is no direct solution for this density, we use the approximation proposed in [18] and used in [8]. Given the density $p(Z_{t+1}\mid W^t)$, its mean is approximated as follows:

$$
E[Z_{t+1} \mid W^t] = E[Z_{t+1} \mid \Theta],
\tag{31}
$$

where $\Theta = (\lambda,\kappa,\tau')$. According to [6,8], if a variable follows the Dirichlet distribution in Eq. (16) with the conjugate prior given by Eq. (17), then the following equality holds:

$$
E[Z_{t+1} \mid \Theta] = E[Z_{t+1} \mid \lambda,\kappa,\tau'] = \kappa.
\tag{32}
$$

Therefore, the posterior mean of the density in Eq. (30) is equal to $\kappa$. The posterior variance also lacks an exact solution and is solved in [18] by approximating each term of the following:

$$
\operatorname{var}[Z_{t+1} \mid D_{t-1}]
=
E[Z_{t+1}^2 \mid D_{t-1}] - \left(E[Z_{t+1} \mid D_{t-1}]\right)^2.
\tag{33}
$$

Furthermore, we compute the correlations at lag 0 between the residuals of each pair of dimensions in the analyzed time series. These correlations are additional indicators of the model quality; the weaker the correlations the better the model. Stronger correlations imply that further modeling is necessary to better fit the time series [8].

## 5 Experiments

**Application: Web Service Selection.** Business applications are increasingly being deployed as autonomous web applications that are published and used on the web (Web Services). The abundance of web services that provide similar functionalities creates a competitive market while rendering the selection of services that best meet the consumers requirements a challenging task. A common solution to this problem considers the trustworthiness of services as a selection criterion based on the outcomes of various quality of service (QoS) metrics, including response time, throughput, reliability, availability, security, and cost. Therefore, the quality of a web service changes continuously during its lifetime. Therefore, we assume that a component for service performance monitoring already exists [21]. A web service consumer can then evaluate and store, after each interaction with any web service, the values of multiple QoS metrics. Then, each vector of QoS metrics’ values are classified into a priori defined quality classes [11]. Afterwards, we count based on a predefined time interval, the number of interactions with a web service that belong to each of the defined quality classes.

The main objective is then to model the QoS-based behavior of web services and predict their future performance to assist the web service selection process. To evaluate our GD time series model, we run different simulations with synthetic data due to the unavailability of real QoS data sets. We are aware of two real data sets; QWS and WS-Dream. The former includes the averages over time of multiple QoS metrics’ measurements of 2,507 web services monitored over a six-day period. As such, the data set includes one quality for each of the monitored web services. The latter reports the response time, http code, and http message of 100 web services over a large number of invocations from 150 computers distributed in more than 20 countries. However, the time of each invocation is not available which makes it hard to build a realistic time-series model for each of the monitored web services. Therefore, we validate our approach with multiple simulated data that embed time-variant processes.

### 5.1 Simulation 1: Trigonometric Functions

We evaluate our model with the outcomes of a web service’s transactions that are classified into $D$ quality classes such as Very Good, Good, and Average. We make the assumption that the proportions $C = \{C_1;\ldots;C_D\}$ of each class during a specific period of time, follow a latent model that we specify using trigonometric functions. At each time step, the number of transactions are counted and assigned to their corresponding quality class. Their overall evolution is modeled by oscillating functions as a web service performance is not constant. We propose to use trigonometric functions as they are easy to handle and to generate with various settings (mean, amplitude, frequency). These functions can be expressed in the form $C'_i(t) = F_i + \gamma_i \operatorname{trig}_i(f_i t) + \nu_{it}$, $i = 1,\ldots,D$, where $\operatorname{trig}_i(f_i t)$ is either the cosine or sine function of frequency $f_i$ randomly taken in the range $[0.0001, 0.009]$. These values keep the functions variations at a reasonable level, see Fig. 1. $\gamma_i$ is a scaling factor controlling the amplitude of the number of transactions within a given class, $A_i$ is a translation coefficient that controls the average number of transactions of a given class per time step, and $\nu_t$ is a white Gaussian noise. $t$ represents the time steps and $D$ the number or quality classes (equal to 3 or 6 here). As $\nu_{it}$ is unbounded, the functions $C'_i$ can sporadically go below 0. These rare occurrences are individually handled by assigning a low random value to the sample, within the predefined range $[10, 50]$. In our experiments, we fixed $A_i = 1200$ and $\gamma_i = 1000$ for all $i$’s, and the Signal-to-Noise Ratio has been set to 20. These values can be adapted if a more realistic model is needed without impact on the overall performance of the method presented here. All values are rounded in order to get integers which represent the number of transactions over a given period of time for a given quality class.

The proportion vectors are finally obtained by normalizing the $C'_i$ functions,

$$
C_i(t) = \frac{C'_i(t)}{\sum_{d=1}^{D} C'_d(t)},
$$

where the function $C_i$ represents the proportions of requests that have been processed in *Good*, *Average*, *Poor*, ... standing by the web service among the total number of requests sent during a given period of time. The algorithm takes these proportions $C_i(t)$, $t = 1,\ldots,1000$, as input data, of which the first 20 samples are only used for training purpose and the 980 remaining samples are used as testing data. In the first experiment, we compare GDPSM and DPSM with the data obtained from Simulation 1 for 5 different values of $\gamma = \{0.001, 0.250, 0.500, 0.750, 0.999\}$, averaged over 10 runs, for the cases of 3 and 6 quality classes.

#### Figure 1

**Fig. 1. Sample data (left) with zoom (right).**

**Description:** The figure contains two line plots of quality class proportions over time.  
- **Left panel:** x-axis is **Time Step** (approximately 0 to 1000), y-axis is **Quality Class Proportion** (0 to 1). Multiple colored curves oscillate over time, showing periodic changes in class proportions.  
- **Right panel:** a zoomed view over approximately time steps 300 to 400, again with y-axis from 0 to 1. The zoom highlights smoother local oscillatory behavior and phase differences among the classes.

#### Three Quality Classes Results

Figure 1 displays the data simulated in one of the 10 runs. The standardized residuals computed by Eq. (29) for GDPSM and DPSM averaged over each of the $d - 1$ dimensions, are displayed in Table 1 (left). For all values of $\gamma$, our model’s residuals are slightly smaller than the ones given by the DPSM. The correlations at lag 0 between the residuals of the first two dimensions computed by DPSM and GDPSM are $-0.4529$ and $-0.0092$, respectively. This shows that our model explains the time series better than DPSM.

**Table 1. Standardized residuals (left) and MSE (right) for 3-dimensional data**

**Standardized residuals**

| $\gamma$ | Dimension 1 DPSM | Dimension 1 GDPSM | Dimension 2 DPSM | Dimension 2 GDPSM |
|---|---:|---:|---:|---:|
| 0.001 | 0.665 | 0.632 | 0.647 | 0.639 |
| 0.250 | 0.666 | 0.631 | 0.653 | 0.645 |
| 0.500 | 0.673 | 0.637 | 0.663 | 0.658 |
| 0.750 | 0.670 | 0.667 | 0.696 | 0.698 |
| 0.999 | 0.855 | 0.838 | 0.899 | 0.900 |

**MSE**

| $\gamma$ | Dimension 1 DPSM | Dimension 1 GDPSM | Dimension 2 DPSM | Dimension 2 GDPSM |
|---|---:|---:|---:|---:|
| 0.001 | 0.166 | 0.067 | 0.190 | 0.144 |
| 0.250 | 0.134 | 0.054 | 0.154 | 0.117 |
| 0.500 | 0.116 | 0.048 | 0.132 | 0.101 |
| 0.750 | 0.119 | 0.050 | 0.132 | 0.101 |
| 0.999 | 0.558 | 0.276 | 0.587 | 0.445 |

Furthermore, Table 1 (right) shows the MSE of both GDPSM and DPSM which demonstrate that our model yields more accurate predictions than DPSM for both dimensions. To visualize the prediction performance of our model, we display $Z$, the symmetric log ratio of the quality class proportions after being transformed using Eq. (2) (actual data) versus the predicted data $(E[p(Z_{t+1}\mid W_t)])$ in Fig. 2. This figure demonstrates that our model is capable of predicting the time series and providing a smoother distribution than that of the actual ones. The latter is actually due to the fact that we are using a noisy signal. The prediction mostly fits the functional part of the model.

#### Figure 2

**Fig. 2. Actual versus predicted data for the first (left) and second (right) dimensions.**

**Description:** The figure contains two line plots comparing **Actual data** and **Predicted data** over time for transformed series values.  
- Both panels use **Time Step** on the x-axis (roughly 0 to 1000) and **Symmetric log ratio of quality class proportion** on the y-axis (roughly from -3 to 3).  
- The predicted curves track the central trend of the actual curves while appearing visibly smoother and less noisy.  
- Recurrent peaks and troughs occur at similar time locations in both actual and predicted series.

#### Six Quality Classes Results

We rerun the same experiment with another set of 10 different simulated 6-dimensional data, each of which is represented by the trigonometric function defined earlier. This aims to further validate the efficiency of partitioning the time series model into $d$ simpler problems to solve and thus lead to lower prediction errors. The average of the standardized residuals of GDPSM and DPSM over the 10 simulated data are displayed in Table 2. For clarity, we only present the results for $\gamma = 0.001$ which raised the best performance for the 3-dimensional residuals (see Table 1). It is noteworthy to mention that other values of $\gamma$ give equivalent results with the exception of $\gamma = 0.999$ that leads to significantly degraded results. This mostly confirms what has been observed in [8]. The correlations at lag 0 between each pair of dimensions are given in Table 3.

Our model shows better performance due to the overall smaller correlations. Table 4 illustrates the out-performance of GDPSM in comparison to DPSM in terms of goodness-of-fit. The MSE of GDPSM’s predictions for all the dimensions are two to three times smaller than those of DPSM. Figure 3 reports the actual and predicted data.

**Table 2. Standardized residuals for GDPSM and DPSM with 6-dimensional data**

| Model | Dimension 1 | Dimension 2 | Dimension 3 | Dimension 4 | Dimension 5 |
|---|---:|---:|---:|---:|---:|
| DPSM | 0.642 | 0.625 | 0.669 | 0.705 | 0.693 |
| GDPSM | 0.555 | 0.541 | 0.620 | 0.675 | 0.674 |

**Table 3. Residuals correlations at lag 0**

**DPSM**

|  | Dim 1 | Dim 2 | Dim 3 | Dim 4 | Dim 5 |
|---|---:|---:|---:|---:|---:|
| Dim 1 | 1 | -0.242 | -0.197 | -0.144 | -0.195 |
| Dim 2 | -0.242 | 1 | -0.193 | -0.200 | -0.172 |
| Dim 3 | -0.197 | -0.193 | 1 | -0.160 | -0.196 |
| Dim 4 | -0.144 | -0.200 | -0.160 | 1 | -0.182 |
| Dim 5 | -0.195 | -0.172 | -0.196 | -0.182 | 1 |

**GDPSM**

|  | Dim 1 | Dim 2 | Dim 3 | Dim 4 | Dim 5 |
|---|---:|---:|---:|---:|---:|
| Dim 1 | 1 | -0.040 | -0.027 | -0.005 | 0.001 |
| Dim 2 | -0.040 | 1 | -0.032 | -0.014 | 0.001 |
| Dim 3 | -0.027 | -0.032 | 1 | -0.017 | 0.001 |
| Dim 4 | -0.005 | -0.014 | -0.017 | 1 | 0.0003 |
| Dim 5 | 0.001 | 0.001 | 0.001 | 0.0003 | 1 |

**Table 4. MSE for GDPSM and DPSM with 6-dimensional data**

| $\gamma$ | Dim 1 DPSM | Dim 1 GDPSM | Dim 2 DPSM | Dim 2 GDPSM | Dim 3 DPSM | Dim 3 GDPSM | Dim 4 DPSM | Dim 4 GDPSM | Dim 5 DPSM | Dim 5 GDPSM |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.001 | 0.238 | 0.075 | 0.226 | 0.072 | 0.221 | 0.071 | 0.215 | 0.074 | 0.230 | 0.135 |
| 0.250 | 0.194 | 0.061 | 0.185 | 0.059 | 0.179 | 0.057 | 0.174 | 0.060 | 0.186 | 0.110 |
| 0.500 | 0.169 | 0.054 | 0.162 | 0.052 | 0.155 | 0.050 | 0.149 | 0.051 | 0.161 | 0.095 |
| 0.750 | 0.178 | 0.057 | 0.170 | 0.055 | 0.156 | 0.050 | 0.146 | 0.052 | 0.165 | 0.096 |
| 0.999 | 0.730 | 0.241 | 0.714 | 0.246 | 0.735 | 0.254 | 0.719 | 0.281 | 0.677 | 0.427 |

#### Figure 3

**Fig. 3. Actual (left) versus predicted (right) 6-dimensional function-based data.**

**Description:** The figure contains two multi-line plots for six-dimensional transformed compositional data.  
- **Left panel:** actual data across approximately 0 to 1000 time steps, with y-axis labeled **Symmetric log ration of quality class proportion** [sic]. Several colored curves fluctuate strongly, with one series showing larger spikes than the others.  
- **Right panel:** predicted data over the same interval. The predicted curves preserve the periodic structure but are smoother and less noisy than the actual data.

### 5.2 Simulation 2: Random Data

In this simulation, we test our model with randomly generated 3 and 6 dimensional data. The quality class of a web service interactions do vary according to the time they occurred. In Simulation 1, we showed that GDPSM is capable of modeling and forecasting time series generated from noisy time-varying functions. However, it is equally essential for the proposed model to perform well with random data to prove its robustness. Similar to Simulation 1, we compute the standardized residuals, the residuals correlations, and the MSE of the predictions.

#### Three Quality Classes Results

Table 5 displays the DPSM and GDPSM standardized residuals (left) and MSE (right) of predictions. Figure 4 shows the actual and predicted data. The correlations between the residuals of the two dimensions as computed by DPSM and GDPSM are $-0.4862$ and $0.0116$, respectively (Fig. 5).

**Table 5. Standardized residuals (left) and MSE (right) for 3-dimensional random data**

**Standardized residuals**

| $\gamma$ | Dimension 1 DPSM | Dimension 1 GDPSM | Dimension 2 DPSM | Dimension 2 GDPSM |
|---|---:|---:|---:|---:|
| 0.001 | 0.798 | 0.792 | 0.801 | 0.810 |
| 0.250 | 0.799 | 0.792 | 0.800 | 0.810 |
| 0.500 | 0.800 | 0.792 | 0.799 | 0.810 |
| 0.750 | 0.804 | 0.794 | 0.802 | 0.810 |
| 0.999 | 0.808 | 0.798 | 0.804 | 0.804 |

**MSE**

| $\gamma$ | Dimension 1 DPSM | Dimension 1 GDPSM | Dimension 2 DPSM | Dimension 2 GDPSM |
|---|---:|---:|---:|---:|
| 0.001 | 0.126 | 0.071 | 0.126 | 0.097 |
| 0.250 | 0.101 | 0.056 | 0.102 | 0.078 |
| 0.500 | 0.084 | 0.047 | 0.085 | 0.065 |
| 0.750 | 0.072 | 0.040 | 0.073 | 0.055 |
| 0.999 | 0.064 | 0.036 | 0.064 | 0.049 |

#### Figure 4

**Fig. 4. Actual (left) versus Predicted (right) 3-dimensional random data.**

**Description:** The figure contains two line plots comparing actual and predicted transformed values for random 3-dimensional data.  
- x-axis is **Time Step** (shown approximately from 250 to 500 in the displayed range).  
- y-axis is **Symmetric log ration of quality class proportion** [sic].  
- The actual series is noisy with rapid short-term fluctuations. The predicted series follows the central movement while remaining smoother.

#### Figure 5

**Fig. 5. Actual (left) versus Predicted (right) 6-dimensional random data.**

**Description:** The figure contains two multi-line plots for six-dimensional random transformed data over approximately time steps 100 to 200.  
- The left panel shows highly variable actual series with frequent crossings and abrupt changes.  
- The right panel shows predicted series that retain separation among dimensions while smoothing much of the short-term irregularity.

#### Six Quality Classes Results

We repeat the same experiment above with 6-dimensional simulated random data. It is noteworthy to mention that we select 6 as the higher number of dimensions since it would not realistically make sense to classify a web service quality into more than 6 classes (Tables 6, 7 and 8).

**Table 6. Standardized residuals for GDPSM and DPSM with 6-dimensional random data**

| Model | Dimension 1 | Dimension 2 | Dimension 3 | Dimension 4 | Dimension 5 |
|---|---:|---:|---:|---:|---:|
| DPSM | 0.801 | 0.816 | 0.803 | 0.794 | 0.789 |
| GDPSM | 0.802 | 0.810 | 0.811 | 0.795 | 0.799 |

**Table 7. Residuals correlations at lag 0**

**DPSM**

|  | Dim 1 | Dim 2 | Dim 3 | Dim 4 | Dim 5 |
|---|---:|---:|---:|---:|---:|
| Dim 1 | 1 | -0.067 | -0.011 | -0.300 | -0.169 |
| Dim 2 | -0.067 | 1 | -0.070 | -0.278 | -0.201 |
| Dim 3 | -0.011 | -0.070 | 1 | -0.299 | -0.199 |
| Dim 4 | -0.300 | -0.278 | -0.299 | 1 | -0.309 |
| Dim 5 | -0.169 | -0.201 | -0.199 | -0.309 | 1 |

**GDPSM**

|  | Dim 1 | Dim 2 | Dim 3 | Dim 4 | Dim 5 |
|---|---:|---:|---:|---:|---:|
| Dim 1 | 1 | -0.051 | -0.101 | -0.103 | 0.015 |
| Dim 2 | -0.051 | 1 | -0.107 | -0.103 | 0.0174 |
| Dim 3 | -0.101 | -0.107 | 1 | -0.242 | 0.026 |
| Dim 4 | -0.103 | -0.103 | -0.242 | 1 | 0.034 |
| Dim 5 | 0.015 | 0.0174 | 0.026 | 0.034 | 1 |

**Table 8. MSE for GDPSM and DPSM with 6-dimensional random data**

| $\gamma$ | Dim 1 DPSM | Dim 1 GDPSM | Dim 2 DPSM | Dim 2 GDPSM | Dim 3 DPSM | Dim 3 GDPSM | Dim 4 DPSM | Dim 4 GDPSM | Dim 5 DPSM | Dim 5 GDPSM |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.001 | 0.137 | 0.046 | 0.203 | 0.075 | 0.175 | 0.077 | 0.494 | 0.203 | 0.314 | 0.158 |
| 0.250 | 0.111 | 0.037 | 0.162 | 0.060 | 0.140 | 0.062 | 0.394 | 0.162 | 0.252 | 0.127 |
| 0.500 | 0.093 | 0.031 | 0.135 | 0.050 | 0.117 | 0.051 | 0.327 | 0.135 | 0.210 | 0.105 |
| 0.750 | 0.079 | 0.027 | 0.116 | 0.043 | 0.100 | 0.044 | 0.280 | 0.115 | 0.180 | 0.090 |
| 0.999 | 0.069 | 0.023 | 0.102 | 0.038 | 0.088 | 0.038 | 0.245 | 0.101 | 0.158 | 0.080 |

## 6 Conclusion

This paper presents a power steady model that is based on observations that follow a generalized Dirichlet distribution. This model is optimized by dividing the problem of the model parameters estimation into multiple smaller problems. As such, the resulting model consists of multiple power steady models that depend on Dirichlet distributed observations. We evaluate the proposed approach by applying it to the web service selection problem where the time series consist of the proportions of quality classes to which a web service was assigned over a period of time. These time series are simulated using two different mechanisms; either generated from trigonometric functions or from random distributions. The experimental results show that our model performs better than a single Dirichlet PSM in terms of standardized residuals and goodness-of-fit of the predictions. Evaluating this model with real compositional time series is left for a future work after collecting the values of various QoS metrics of multiple web services for a three-month period.

## References

1. Aitchison, J.: The statistical analysis of compositional data. *J. R. Stat. Soc. Ser. B (Methodol.)* **44**(2), 139–177 (1982)

2. Bhaumik, A., Dey, D.K., Ravishanker, N.: Joint statistical meetings - Bayesian statistical science - time series analysis of compositional data using a dynamic linear model approach (1999)

3. Bouguila, N., Ziou, D.: High-dimensional unsupervised selection and estimation of a finite generalized dirichlet mixture model based on minimum message length. *IEEE Trans. Pattern Anal. Mach. Intell.* **29**(10), 1716–1731 (2007)

4. Boutemedjet, S., Bouguila, N., Ziou, D.: A hybrid feature extraction selection approach for high-dimensional non-Gaussian data clustering. *IEEE Trans. Pattern Anal. Mach. Intell.* **31**(8), 1429–1443 (2009)

5. Brunsdon, T.M., Smith, T.: The time series analysis of compositional data. *J. Off. Stat.* **14**(3), 237–253 (1998)

6. Diaconis, P., Ylvisaker, D.: Conjugate priors for exponential families. *Ann. Stat.* **7**(2), 269–281 (1979)

7. Gooijer, J.G.D., Hyndman, R.J.: 25 years of time series forecasting. *Int. J. Forecast.* **22**(3), 443–473 (2006)

8. Grunwald, G.K., Raftery, A.E., Guttorp, P.: Time series of continuous proportions. *J. R. Stat. Soc. Ser. B* **55**, 103–116 (1993)

9. Hamilton, J.D.: *Time Series Analysis*. Princeton University Press, Princeton (1994)

10. Harrison, P.J., Stevens, C.F.: Bayesian forecasting. *J. R. Stat. Soc. Ser. B (Methodol.)* **38**(3), 205–247 (1976)

11. Mehdi, M., Bouguila, N., Bentahar, J.: Probabilistic approach for QoS-aware recommender system for trustworthy web service selection. *Appl. Intell.* **41**(2), 503–524 (2014)

12. Quintana, J.M., West, M.: Time series analysis of compositional data. In: Bernando, J.M., DeGroot, M.H., Lindley, D.V., Smith, A.F.M. (eds.) *Bayesian Statistics 3*, pp. 747–756. Oxford University Press, Oxford (1988)

13. Robert, C.P.: *The Bayesian Choice: From Decision-Theoretic Foundations to Computational Implementation*, 2nd edn. Springer, New York (2007)

14. Smith, J.Q.: A generalization of the Bayesian steady forecasting model. *J. R. Stat. Soc. Ser. B (Methodol.)* **41**(3), 375–387 (1979)

15. Smith, J.Q.: The multiparameter steady model. *J. R. Stat. Soc. Ser. B (Methodol.)* **43**(2), 256–260 (1981)

16. Thiesson, B., Chickering, D.M., Heckerman, D., Meek, C.: Arma time-series modeling with graphical models. In: *Proceedings of the 20th Conference on Uncertainty in Artificial Intelligence*, pp. 552–560. AUAI Press (2004)

17. Tiao, G.C., Box, G.E.P.: Modeling multiple times series with applications. *J. Am. Stat. Assoc.* **76**(376), 802–816 (1981)

18. Tierney, L., Kadane, J.B.: Accurate approximations for posterior moments and marginal densities. *J. Am. Stat. Assoc.* **81**(393), 82–86 (1986)

19. Wang, H., Liu, Q., Mok, H.M.K., Fu, L., Tse, W.M.: A hyperspherical transformation forecasting model for compositional data. *Eur. J. Oper. Res.* **179**(2), 459–468 (2007)

20. Wong, T.T.: Parameter estimation for generalized Dirichlet distributions from the sample estimates of the first and the second moments of random variables. *Comput. Stat. Data Anal.* **54**(7), 1756–1765 (2010)

21. Zeng, L., Lei, H., Chang, H.: Monitoring the QoS for web services. In: Krämer, B.J., Lin, K.-J., Narasimhan, P. (eds.) *ICSOC 2007*. LNCS, vol. 4749, pp. 132–144. Springer, Heidelberg (2007)
```

```
- Source consisted of OCR-parsed page text plus images for pages 10–14. I reconstructed the article in Markdown and corrected obvious OCR artifacts such as broken ligatures and line-wrap hyphenation.
- Formulas on pages 3–8 were partially corrupted in the OCR stream. I restored them into standard mathematical notation where the intended expression was clear from context, but some symbols may still differ from the publisher PDF typography.
- Equation numbering was preserved, but several equations likely contain uncertainty in indices and variable names due to OCR corruption:
  - Eq. (1): the original OCR showed malformed summation/product layout and an apparent typo `\Gamma(\alpha_l) + \Gamma(\beta_l)`; I restored it to the standard generalized Dirichlet factor `\Gamma(\alpha_l+\beta_l)/(\Gamma(\alpha_l)\Gamma(\beta_l))`.
  - Eqs. (5)–(11): OCR mixed upper/lower indices and duplicated summation bounds; I normalized them to a consistent exponential-family form.
  - Eq. (14): OCR around the denominator and the definition of $Z$ was badly fragmented; the reconstruction follows the most plausible Dirichlet exponential-form parameterization.
  - Eq. (16): OCR had symbols like `W$`, `Z $T`, `K` and indexing corrupted. I reconstructed a consistent form, but the exact typography of the original may differ.
  - Eq. (17): OCR for the hyperparameter preceding the parenthesis was unclear (appearing as `,` or similar). I rendered it as `\lambda`, which is the most plausible notation in context.
  - Eqs. (21)–(28): OCR was severely degraded for Greek letters and conditional-index notation (e.g., `,t+1|t`, `κT`, `θ$`). I rendered these as `\lambda_{t+1\mid t}`, `\kappa_{t+1\mid t}`, etc. The structure should be correct, but exact notation should be verified against the PDF.
  - Eq. (29): the standardized residual formula in OCR lacked a square root in the denominator; I preserved the OCR reading literally as variance in denominator rather than guessing `\sqrt{\mathrm{var}}`, though the latter may be what the original intended.
  - Eqs. (31)–(33): OCR alternated between densities and variables inside expectations/variances; I interpreted these as expectations/variances of $Z_{t+1}$, but this should be checked.
- Table data for Tables 1, 2, 4, 5, 6, and 8 were legible from OCR/images and were transcribed directly.
- Table 3 and Table 7 were displayed in triangular correlation-matrix format in the scanned images. I reconstructed them as full symmetric matrices using the visible lower-triangular values. One value in Table 3 GDPSM (`0.0003`) was tiny and could be slightly off if the image resolution obscured the decimal placement.
- Figure captions were clear. Since the figures are line plots, I provided detailed natural-language descriptions instead of code diagrams.
- A few textual items may reflect OCR ambiguities:
  - Page 1 author marker `(B)` likely denotes corresponding author symbol and was preserved as-is.
  - `ELectrical` in affiliation 3 appears capitalized oddly in OCR; preserved except obvious spacing fixes.
  - Reference 5 journal abbreviation appeared as `J. O!. Stat.` in OCR; normalized to `J. Off. Stat.` as an obvious OCR fix.
  - Reference 9 `Princenton` was normalized to `Princeton` as an obvious OCR fix.
  - References with umlauts/diacritics (e.g., `Krämer`) were restored where clear from context.
- Pages most affected by OCR uncertainty: pages 3–8 (all math-heavy pages), especially formulas and parameter notation in Sections 2–4.
- If exact formula fidelity is critical, the original PDF should be rechecked visually for Eqs. (1), (14), (16), (17), and (21)–(33).
```