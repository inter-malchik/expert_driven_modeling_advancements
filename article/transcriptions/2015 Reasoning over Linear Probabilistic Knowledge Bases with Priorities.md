```
# Reasoning over Linear Probabilistic Knowledge Bases with Priorities

Nico Potyka(B)  
Department of Computer Science, Fern Universität in Hagen,  
Hagen, Germany  
nico.potyka@fernuni-hagen.de

*© Springer International Publishing Switzerland 2015*  
*C. Beierle and A. Dekhtyar (Eds.): SUM 2015, LNAI 9310, pp. 121–136, 2015.*  
*DOI: 10.1007/978-3-319-23540-0_9*

## Abstract

We consider the problem of reasoning over probabilistic knowledge bases with different priority levels. While we assume that the knowledge is consistent on each level, there can be inconsistencies between different levels. Examples arise naturally in hierarchical domains when general knowledge is overwritten with more specific information. We extend recent results on inconsistency-tolerant probabilistic reasoning to propose a solution for this problem.

# 1 Introduction

Often our evaluation of the likelihood of an event depends on the level of abstraction that we employ. For instance, you might agree that it is likely that a bird flies. However, a penguin is also a bird, but usually does not fly. It is intuitively clear that our beliefs about penguins are more specific and therefore should overwrite our beliefs about birds; but it can be difficult to automatically resolve conflicts betweens rules, in particular, if there are transitive dependencies.

**Example 1.** Let us consider a probabilistic version of an access control policy scenario from [4]. Suppose we have different files and different users and want to automatically deduce the probability that a user has access to a file. If the probability is 1, we might grant access immediately, otherwise we might send a confirmation request to the system administrator. If the probability is very low, say smaller than 0.1, we might want to send a warning in addition.

If no knowledge about the user and the file is available, the access probability should be 0. However, we want to have specialized rules for particular types of users and files. For instance, if we know that a user is an employee, we want to be less restrictive and increase the probability to 0.5. Of course there can be exceptions, for instance, if the file is confidential. On the other hand, this exception should not apply to executive managers. Finally, we never want to grant access if a user is blacklisted for some reason.

Obviously, we can make this example arbitrarily complex. The key problem is that if we ask for the probability that a user has access to a file, different rules may apply. How can our system decide, as autonomously as possible, which rules apply and which rules have to be excluded to avoid inconsistencies?

This question is closely related to problems considered in belief merging [15] and non-monotonic reasoning [4,6,16] and several proposals have been made to deal with priorities in non-probabilistic logics [2,3,5,25]. There also exist several belief merging approaches for probabilistic logics when no priorities exist [1,7,13,26]. Whereas the goal in [13] is to consolidate the knowledge bases, the goal in [1,26] is to find a probability function that best captures all knowledge bases. In [7], a set of probability functions is considered, which is close to satisfying the inconsistent pieces of information (this will be made more precise at the end of the paper).

Our approach builds up on work in [22–24] and is related to ideas considered in [7] as will be discussed at the end of the paper. We suppose that our knowledge base consists of subsets of increasing priority and a set of integrity constraints that have to be maintained. Since we cannot assume that subsets of different priority are pairwise consistent, the overall knowledge base might be (and probably will be) inconsistent. That is, the knowledge base has no classical probabilistic models, i.e., there are no probability functions that satisfy all constraints in the knowledge base. We define two notions of priority models. Strict priority models are constructed by starting with the models of the integrity constraints. Then this set is successively decreased by selecting the best models with respect to a subset of our priority knowledge base starting with the subset of highest priority. This approach provides some nice guarantees for subsets with high priority, but subsets of low priority can be completely ignored. To overcome this problem, weighted priority models take all knowledge bases into account but weigh them with respect to their priority. We prove some interesting properties and illustrate both approaches by means of our access control policy example. We consider a general probabilistic framework, but illustrate the ideas by means of a relational probabilistic logic similar to those considered in [10,17].

The remainder of this paper is organized as follows: In Sect. 2, we explain our formal framework and discuss some basics from [22–24]. We then introduce and investigate priority knowledge bases, strict and weighted priority models in Sect. 3. In Sect. 4, we discuss related work and conclude in Sect. 5.

# 2 Linear Probabilistic Knowledge Bases and Generalized Models

To begin with, we describe a general framework to define our probabilistic knowledge bases. Let us assume that our knowledge can be represented by means of a set of random variables $X = \{X_1, \ldots, X_n\}$. Each $X \in X$ has a finite domain $\operatorname{dom}(X)$. If $\operatorname{dom}(X) = \{0,1\}$, we call $X$ a Boolean random variable. An assignment $(X_1=x_1, \ldots, X_n=x_n)$ to $X$ is sometimes abbreviated by $(x_1, \ldots, x_n)$ or just by $x$ if the order of the variables in $X$ is clear from the context or not important. If $Y \subseteq X$ and $x$ is an assignment to $X$, $x|_Y$ denotes the assignment $y$ to $Y$ that is obtained from $x$ by restricting to the variables in $Y$. The set of all assignments to $X$ is denoted by $\Omega_X$ and is called the set of possible worlds.

**Example 2.** To model our access control policy, we consider a relational probabilistic language similar to [10,17]. We build up formulas over a finite set of typed predicate symbols, a finite set of typed individuals and an infinite set of (typed) variables. We allow the usual logical connectives, but do not allow quantifiers. Let us consider the types `User` and `File` and the predicates `grantAccess(User, File)`, `employee(User)`, `exec(User)`, `blacklisted(User)`, `confidential(File)`, where `exec` abbreviates executive manager. Let `alice` and `bob` be individuals of type `User` and let `file1`, `file2` be individuals of type `File`. We regard the 12 ground atoms `grantAccess(alice, file1)`, ..., `confidential(file2)` as Boolean random variables and our possible worlds correspond to truth assignments to the ground atoms.

Given a set of random variables $X$, we denote by $P_X$ the set of all joint probability distributions over $X$. If $P \in P_X$, $Y \subseteq X$, $Z = X \setminus Y$, then the joint probability distribution $P_Y$ over $Y$ obtained from $P$ by marginalizing out $Z$ is

$$
P_Y(y) = \sum_z P(y,z),
$$

where the sum ranges over the variable assignments to $Z$.

Given a subset $Y \subseteq X$, a linear probabilistic constraint function $l$ over $P_X$ with scope $\operatorname{scope}(l)=Y$ is a function $l:P_X \to \mathbb{R}$ that has the form

$$
l(P) = \sum_y P_Y(y) f_l(y),
$$

where $f:\Omega_Y \to \mathbb{R}$ is called the feature function of $l$. Roughly speaking, in probabilistic logics, constraint functions correspond to rules and feature functions indicate whether a world verifies or falsifies a rule, see, e.g., [10] for a detailed example. We say that $P \in P_X$ satisfies $l$ iff $l(P)=0$ and $l(P)=0$ is called the linear probabilistic constraint corresponding to $l$. A linear probabilistic knowledge base over $P_X$ is a set $KB$ consisting of linear probabilistic constraint functions over $P_X$. The scope of $KB$ is the union of the scopes of the constraints in $KB$, i.e.,

$$
\operatorname{scope}(KB) = \bigcup_{c \in KB} \operatorname{scope}(c).
$$

We say that $P \in P_X$ satisfies $KB$ iff $P$ satisfies all $l \in KB$. The set

$$
\operatorname{Mod}(KB) = \{P \in P_X \mid l(P)=0 \text{ for all } l \in KB\}
$$

of all probability distributions satisfying $KB$ is called the set of models of $KB$. $KB$ is called consistent if $\operatorname{Mod}(KB) \neq \emptyset$. Otherwise, $KB$ is called inconsistent.

**Remark 1.** Note that each constraint function can as well be written as a sum over $\Omega_X$:

$$
l(P) = \sum_y P_Y(y) f_l(y)
     = \sum_y \sum_z P(y,z) f_l(y)
     = \sum_{x \in \Omega_X} P(x) f_l(x|_Y).
$$

The second equation is obtained by putting in the definition of the marginal $P_Y$, the third equation by using the fact that each two assignments $y,z$ to $Y,Z$ correspond to an assignment $x$ to $X=Y \cup Z$.

**Example 3.** In our running example, we represent rules by probabilistic conditionals $(\phi \mid \psi)[\rho]$, where the conclusion $\phi$ and the premise $\psi$ are formulas in our language and $\rho \in [0,1]$ is a probability, c.f. [10,17]. For instance, the probabilistic conditional $(grantAccess(U,F)\mid confidential(F))[0]$ expresses intuitively that users usually do not have access to confidential files. If the premise $\psi$ is tautological, we just omit it. For instance, $(blacklisted(U))[0.05]$ expresses that users are usually not blacklisted. We define the probability of a ground formula $\phi$ with respect to a joint probability distribution $P$ to be

$$
P(\phi) = \sum_{x \in \Omega} P(x)\, \mathbf{1}_{\{\phi\}}(x),
$$

where the indicator function $\mathbf{1}_{\{\phi\}}$ yields 1 iff $\phi$ evaluates to true under $x$ in the usual sense (and 0 otherwise). $P$ satisfies a ground conditional $(\phi \mid \psi)[\rho]$ iff

$$
P(\phi \land \psi) = P(\psi)\cdot \rho.
$$

Note that this definition coincides with conditional probability whenever $P(\psi)>0$. $P$ satisfies a general conditional $(\phi \mid \psi)[\rho]$ iff $P$ satisfies each ground instance of $(\phi \mid \psi)[\rho]$. For instance, $P$ satisfies $(blacklisted(U))[0.05]$, iff $P$ satisfies its ground instances $(blacklisted(alice))[0.05]$ and $(blacklisted(bob))[0.05]$. To see that our conditionals indeed induce linear constraint functions, recall that $P$ satisfies a ground conditional $(\phi \mid \psi)[\rho]$ iff

$$
\begin{aligned}
0 &= P(\phi \land \psi) - P(\psi)\cdot \rho \\
  &= P(\phi \land \psi) - (P(\phi \land \psi) + P(\neg \phi \land \psi))\cdot \rho \\
  &= P(\phi \land \psi)\cdot (1-\rho) - P(\neg \phi \land \psi)\cdot \rho \\
  &= \sum_{x \in \Omega} P(x)\, \mathbf{1}_{\{\phi \land \psi\}}(x)\cdot (1-\rho)
     - \sum_{x \in \Omega} P(x)\, \mathbf{1}_{\{\neg \phi \land \psi\}}(x)\cdot \rho \\
  &= \sum_{x \in \Omega} P(x)\cdot
     \left(\mathbf{1}_{\{\phi \land \psi\}}(x)\cdot (1-\rho)
     - \mathbf{1}_{\{\neg \phi \land \psi\}}(x)\cdot \rho\right)
     \qquad := f(Y).
\end{aligned}
$$

From Remark 1, we see that this is a linear probabilistic constraint. The scope $Y$ of the feature function $f$ is the set of ground atoms appearing in $(\phi \mid \psi)[\rho]$ and the feature function is defined by

$$
f(Y)=\mathbf{1}_{\{\phi \land \psi\}}(x|_Y)\cdot (1-\rho) - \mathbf{1}_{\{\neg \phi \land \psi\}}(x|_Y)\cdot \rho.
$$

Note that the feature function yields $1-\rho$ if the conditional is verified and $-\rho$ if the conditional is falsified. Correspondingly, each general conditional induces a set of constraints (one for each ground instance). For instance, $(blacklisted(U))[0.05]$ induces two constraints, one for $(blacklisted(alice))[0.05]$ and one for $(blacklisted(bob))[0.05]$. The scope of the first one is `blacklisted(alice)`, the scope of the second one is `blacklisted(bob)`. However, for the sake of clarity, we will usually just write the general conditional, but keep in mind that it represents several constraints.

To reason with probabilistic knowledge bases, we can use the probability distributions in $\operatorname{Mod}(KB)$ to compute (conditional) probabilities for arbitrary formulas. For instance, given a formula $\phi$, the probabilistic entailment problem is to derive upper and lower bounds on $P(\phi)$ for $P \in \operatorname{Mod}(KB)$ [11,17,20]. Formally, we want to solve

$$
\operatorname{opt}_{P \in \operatorname{Mod}(KB)} P(\phi),
$$

where $\operatorname{opt} \in \{\min,\max\}$. The lower bound $l$ and the upper bound $u$ on the probability of $\phi$, is the result of the minimization and maximization problem, respectively.

Another way to reason with $\operatorname{Mod}(KB)$ is to find a unique probability function $P^\ast \in \operatorname{Mod}(KB)$ that optimizes some quality criterion like the entropy. Then one can use $P^\ast$ directly to compute probabilities for formulas [10,12,21]. However, if $KB$ is inconsistent, no such probability distribution exists and there is no way to infer reasonable information with these approaches.

To reason with inconsistent knowledge bases, we can replace $\operatorname{Mod}(KB)$ with a set of probability distributions which satisfy the knowledge base as best as possible [7,22]. The idea in [22] is to use those probability functions that minimally violate the knowledge base. To make this idea more precise, it is useful to represent linear constraint functions by matrices. To avoid ambiguity in this representation, we have to impose an ordering on the possible worlds and on the constraints. Let $N = |\Omega_X|$ and consider an arbitrary but fixed order $x_1, \ldots, x_N$ of the worlds in $\Omega_X$. Let $l$ be a linear constraint over $P_X$. The constraint matrix corresponding to $l$ is the $(1 \times N)$-matrix $A_l$ which has the entry $f_l(x_j|_{Y_l})$ at the $j$-th position for $1 \leq j \leq N$. Let $KB$ be a linear probabilistic knowledge base over $P_X$, let $M=|KB|$ and consider an arbitrary but fixed order $l_1, \ldots, l_M$ of the constraints in $KB$. Then the constraint matrix corresponding to $KB$ is the $(M \times N)$-matrix

$$
A_{KB} =
\begin{pmatrix}
A_{l_1} \\
\vdots \\
A_{l_M}
\end{pmatrix}.
$$

To keep our notation simple, we identify probability functions $P$ over $\Omega_X$ with column vectors, whose $i$-th entry is the probability of the $i$-th world. Then $P$ satisfies $KB$ iff

$$
A_{KB}P =
\begin{pmatrix}
A_{l_1}P \\
\vdots \\
A_{l_M}P
\end{pmatrix}
=
\begin{pmatrix}
\sum_{x \in \Omega_X} P(x) f_{l_1}(x|_{Y_1}) \\
\vdots \\
\sum_{x \in \Omega_X} P(x) f_{l_M}(x|_{Y_M})
\end{pmatrix}
=
\begin{pmatrix}
0 \\
\vdots \\
0
\end{pmatrix}.
$$

Now given a knowledge base $KB$ and some continuous vector norm $\|\cdot\|$, we consider the following minimization problem:

$$
\min_{P \in P_X} \|A_{KB}P\| \tag{1}
$$

The minimum exists; it is 0 if and only if $KB$ is consistent [22]. In particular, in the latter case, the minimal solutions are just the models of $KB$. Conversely, if $KB$ is inconsistent, the minimal solutions minimally violate $KB$ with respect to $\|\cdot\|$. Therefore, the optimal solutions of (1) are called generalized models of $KB$, see [22,23] for more details. Consistent probabilistic reasoning approaches can be generalized to inconsistency-tolerant probabilistic reasoning approaches by just replacing the models with the generalized models [23,24].

# 3 Linear Priority Knowledge Bases and Priority Models

Now let us get back to our initial problem. We have a knowledge base that contains rules with different levels of priority. Whereas we can assume that the knowledge base is consistent on each particular level, there can be conflicts between different levels. We could apply generalized reasoning approaches to the whole (inconsistent) knowledge base to deduce new information. However, the results will not necessarily reflect what we want. The reason is that we cannot define that some rules are more important than others. That is, instead of overwriting knowledge of low priority with knowledge of higher priority, we would merge the knowledge independently of the priority.

To overcome this problem, we will partition our knowledge base in subsets with different priority levels. In order to account for knowledge that has to be respected independently of the priority, we will also allow a set of integrity constraints that is guaranteed to be satisfied if it is consistent. We will call a Priority Knowledge Base valid iff the knowledge on each level is consistent with the integrity constraints.

**Definition 1 (Linear Priority Knowledge Base, Validity).** Let $X$ be a set of random variables. A linear priority knowledge base over $X$ is a tuple $(KB_1, \ldots, KB_k, IC)$, where $KB_1, \ldots, KB_k, IC$ are linear probabilistic knowledge bases over $X$. For $1 \leq i \leq k$, $KB_i$ is called the subset with priority $i$. The elements in $IC$ are called integrity constraints. $k$ is called the number of priority levels. $(KB_1, \ldots, KB_k, IC)$ is called valid iff $KB_i \cup IC$ is consistent for $1 \leq i \leq k$.

**Remark 2.** Note that validity implies that $IC$ is consistent for otherwise $KB_i \cup IC$ is inconsistent for $1 \leq i \leq k$.

**Example 4.** Let us continue our running example and consider the priority knowledge base $KB = (KB_1, KB_2, KB_3, KB_4, KB_5, IC)$, where

$$
KB_1 = \{(grantAccess(U,F))[0], (blacklisted(U))[0.05]\}
$$

$$
KB_2 = \{(grantAccess(U,F)\mid employee(U))[0.5],\;
(blacklisted(U)\mid employee(U))[0.01]\}
$$

$$
KB_3 = \{(grantAccess(U,F)\mid confidential(F))[0]\}
$$

$$
KB_4 = \{(grantAccess(U,F)\mid exec(U))[0.7],\;
(blacklisted(U)\mid exec(U))[0.001]\}
$$

$$
KB_5 = \{(exec(alice))[1], (employee(bob))[1], (confidential(file1))[1]\}
$$

$$
IC = \{(employee(U)\mid exec(U))[1],\;
(grantAccess(U,F)\mid blacklisted(U))[0]\}
$$

On the first level, we define generic knowledge. If no knowledge is available, we do not want to grant access. Also, we make the assumption that it is rather unlikely that a user is blacklisted. On the second level, we increase the access probability and decrease the blacklist probability for employees. On level 3, we make an exception for confidential files. Afterwards, we further increase access probability and decrease blacklist probability for executive managers on level 4.

The last level contains domain knowledge. We know that `alice` is an executive manager, `bob` is an employee and `file1` is confidential. Our integrity constraints state that executive managers are employees and that we do not grant access to blacklisted users.

## 3.1 Strict Priority Models

Our first approach is motivated by the desire to guarantee that all rules in the subset with the highest priority hold. After this goal is achieved, we look at the next subset successively. That is, we start with the models of our integrity constraints. Then we successively decrease this set by selecting the best models with respect to a subset of our priority knowledge base starting with the subset of highest priority. The following definition describes this approach precisely.

**Definition 2 (Strict Priority Models).** Let $KB = (KB_1, \ldots, KB_k, IC)$ be a linear priority knowledge base over $X$ and let $\|\cdot\|$ be some continuous vector norm. We let

$$
SPMod^{k+1}_{\|\cdot\|}(KB) = \operatorname{Mod}(IC)
$$

and

$$
SPMod^{i}_{\|\cdot\|}(KB)
=
\arg\min_{P \in SPMod^{i+1}_{\|\cdot\|}(KB)} \|A_{KB_i}P\|
\quad \text{for } i=k,\ldots,1.
$$

Let

$$
SPMod_{\|\cdot\|}(KB) = SPMod^{1}_{\|\cdot\|}(KB).
$$

The elements in $SPMod_{\|\cdot\|}(KB)$ are called the strict priority models of $KB$.

**Remark 3.**
1. To enhance readability, we usually omit the subscript $\|\cdot\|$, but keep in mind that $SPMod(KB)$ depends on the selected norm.
2. Strict priority models are defined recursively. We let $SPMod^{k+1}(KB)$ be the set of models of our integrity constraints $IC$. Then we go backwards for $i=k,\ldots,1$ and let $SPMod^i(KB)$ be the set of probability distributions in $SPMod^{i+1}(KB)$ that minimally violate the constraints in $KB_i$.

Before looking at an example, we state some basic results of technical interest.

**Lemma 1.** Let $KB = (KB_1, \ldots, KB_k, IC)$ be a linear priority knowledge base over $X$ and let $\|\cdot\|$ be some continuous vector norm. If $KB$ is valid, then

1. $SPMod^i(KB)$ is non-empty, compact and convex for $1 \leq i \leq k+1$.
2. $\emptyset \neq SPMod(KB)=SPMod^1(KB) \subseteq \cdots \subseteq SPMod^k(KB)$.

**Proof.**
1. First note that validity of $KB$ implies that $\operatorname{Mod}(IC) \neq \emptyset$. In particular, $\operatorname{Mod}(IC)$ is a subset of $P_X$ that is defined by linear equality constraints. Therefore, $SPMod^{k+1}(KB)=\operatorname{Mod}(IC)$ is also compact and convex. Now we proceed by induction and show that if $SPMod^{i+1}(KB)$ is non-empty, compact and convex, so is $SPMod^i(KB)$. Continuity of $\|\cdot\|$ and compactness of $SPMod^{i+1}(KB)$ imply that a minimum of $\arg\min_{P \in SPMod^{i+1}(KB)} \|A_{KB_i}P\|$ exists and that the set of minima (that is, $SPMod^i(KB)$) is closed. As a subset of $SPMod^{i+1}(KB)$, $SPMod^i(KB)$ is also bounded and therefore compact. In particular, the objective function $f(x)=\|A_{KB_i}x\|$ is convex since $\|\cdot\|$ is convex (this follows from homogeneity and the triangular inequality for norms) and the composition of convex and linear functions is convex. This implies that $SPMod^i(KB)$ is also convex.
2. Non-emptiness follows from (1), the subset relationships follow from the definition. $\square$

The practical importance of Lemma 1.1 is that it guarantees the existence of a minimum if we minimize some continuous function over $SPMod(KB)$ and that the minimum is unique if the function is also strictly convex. Lemma 1.2 is immediate, but is mentioned for emphasis. Given the strict priority models, Lemma 1.1 allows us to apply the usual reasoning approaches. For instance, we can compute upper and lower bounds on the probability of formulas [11,17,20] or select a best strict priority model to compute probability of formulas [10,12,21].

**Example 5.** Let us compute upper and lower bounds on some formulas for the knowledge base in Example 4. To keep things simple, we will only ask for the probability of ground formulas. More strictly speaking, given a ground formula $\phi$, we want to solve

$$
\operatorname{opt}_{P \in SPMod(KB)} P(\phi),
$$

where $\operatorname{opt} \in \{\min,\max\}$. Like for the Probabilistic Entailment Problem, the lower bound $l$ and the upper bound $u$ on the probability of $\phi$, is the result of the minimization and maximization problem, respectively. We write $\phi[l,u]$ to denote the result. If $l \approx u$, we sometimes just write $\phi[l]$ to enhance readability. For instance, we have the following rounded results when using the Euclidean norm to determine our strict priority models:

- $grantAccess(alice, file1)[0.7]$
- $grantAccess(bob, file1)[0]$
- $grantAccess(alice, file2)[0.7]$
- $grantAccess(bob, file2)[0.5]$
- $blacklisted(alice)[0.0001]$
- $blacklisted(bob)[0.01]$

Recall that `alice` is an executive manager and that `file1` is confidential. Note that the first query shows that the knowledge about executive managers in $KB_4$ suppresses the knowledge about confidential files in $KB_3$ as desired.

What can we say about strict priority models in general? The following proposition states that valid linear priority knowledge bases always have strict priority models and that these always satisfy our integrity constraints and the subset with highest priority.

**Proposition 1 (Upmost Consistency).** Let $KB = (KB_1, \ldots, KB_k, IC)$ be a linear priority knowledge base over $X$ and let $\|\cdot\|$ be some continuous vector norm. If $KB$ is valid, then

$$
\emptyset \neq SPMod(KB) \subseteq \operatorname{Mod}(KB_k \cup IC). \tag{2}
$$

**Proof.** Since $SPMod(KB)=SPMod^1(KB)$, it follows that $\emptyset \neq SPMod(KB) \subseteq SPMod^k(KB)$ from Lemma 1.2. Therefore, it suffices to show that $SPMod^k(KB)=\operatorname{Mod}(KB_k \cup IC)$ to prove the claim. By validity, $KB_k \cup IC$ is consistent. Therefore, we have $\min_{P \in SPMod^{k+1}(KB)} \|A_{KB_k}P\|=0$ and the minimal elements are models of $KB_k$. In particular, they are also models of $IC$ because we optimize over $SPMod^{k+1}(KB)$. Hence, $SPMod^k(KB) \subseteq \operatorname{Mod}(KB_k \cup IC)$. Conversely, if $P \in \operatorname{Mod}(KB_k \cup IC)$, then $A_{KB_k}P=0$ and therefore $P \in SPMod^k(KB)$. Hence, $SPMod^k(KB)=\operatorname{Mod}(KB_k \cup IC)$, which completes the proof. $\square$

So strict priority models always satisfy the integrity constraints and the rules of highest priority. In fact, a slightly stronger property holds. If all knowledge bases from level $l$ up to $k$ are consistent, then the strict priority models are models of $KB_l, \ldots, KB_k$ and of $IC$.

**Proposition 2 (Upward Consistency).** Let $KB = (KB_1, \ldots, KB_k, IC)$ be a linear priority knowledge base over $X$ and let $\|\cdot\|$ be some continuous vector norm. If $KB$ is valid and $\bigcup_{i=l}^k KB_i$ is consistent, then

$$
SPMod(KB) \subseteq \operatorname{Mod}\left(\bigcup_{i=l}^k KB_i \cup IC\right). \tag{3}
$$

**Proof.** Like in the proof of Proposition 1, it suffices to show that $SPMod^l(KB)=\operatorname{Mod}(\bigcup_{i=l}^k KB_i \cup IC)$. We prove the claim by induction on the difference $d=k-l$. For $d=0$, i.e., $l=k$, we proved the claim in Proposition 1. Now suppose that the claim holds for all natural numbers lower than $d$ and consider $\bigcup_{i=k-d-1}^k KB_i$. Since $\bigcup_{i=k-d-1}^k KB_i$ is consistent by assumption, so is $\bigcup_{i=k-d}^k KB_i$ and therefore

$$
SPMod^{k-d}(KB)=\operatorname{Mod}\left(\bigcup_{i=k-d}^k KB_i \cup IC\right)
$$

by our induction hypothesis. Now,

$$
SPMod^{k-d-1}(KB)
=
\arg\min_{P \in SPMod^{k-d}(KB)} \|A_{KB_{k-d-1}}P\|
=
\arg\min_{P \in \operatorname{Mod}(\bigcup_{i=k-d}^k KB_i \cup IC)} \|A_{KB_{k-d-1}}P\|.
$$

Since $\bigcup_{i=k-d-1}^k KB_i$ is consistent by assumption, we can proceed like in the proof of Proposition 1 to show that

$$
\min_{P \in \operatorname{Mod}(\bigcup_{i=k-d}^k KB_i \cup IC)} \|A_{KB_{k-d-1}}P\| = 0
$$

and to conclude from this that

$$
SPMod^{k-d-1}(KB)=\operatorname{Mod}\left(\bigcup_{i=k-d-1}^k KB_i \cup IC\right).
$$

$\square$

The assumption of Proposition 2 will usually be only satisfied for subsets with high priority. What can we say about subsets with low priority? Intuitively, there should be at least some guarantees for constraints that are independent of higher priority levels. Indeed, the following proposition states that if there is a subset of constraints $C \subseteq KB_l$ on level $l$ whose scope is disjunct from the scope of all knowledge bases with level greater than $l$, then $C$ is still satisfiable on level $l+1$.

**Proposition 3 (Upward Independence).** Let $KB = (KB_1, \ldots, KB_k, IC)$ be a valid linear priority knowledge base over $X$ and let $\|\cdot\|$ be some continuous vector norm. Let $C \subseteq KB_l$ for some $l<k$ such that

$$
\operatorname{scope}(C) \cap \operatorname{scope}\left(\bigcup_{p=l+1}^k KB_p\right)=\emptyset.
$$

Then

$$
\operatorname{Mod}(C) \cap SPMod^{l+1}(KB) \neq \emptyset. \tag{4}
$$

**Proof.** First note that by validity, $\operatorname{Mod}(C)\neq \emptyset$ (for otherwise $KB_l$ and hence $KB_l \cup IC$ were inconsistent) and $SPMod^{l+1}(KB)\neq \emptyset$. Let $Y=\operatorname{scope}(C)$ and let $Z=X \setminus Y$. Let $P^{(1)} \in \operatorname{Mod}(C)$ and let $P_Y^{(1)}$ denote the probability distribution obtained from $P^{(1)}$ by marginalizing out $Z$. Let $P^{(2)} \in SPMod^{l+1}(KB)$ and let $P_Z^{(2)}$ denote the probability distribution obtained from $P^{(2)}$ by marginalizing out $Y$. Then

$$
P(y,z)=P_Y^{(1)}(y)P_Z^{(2)}(z)
$$

is a probability distribution over $X$ since for all assignments $x$ to $X$, we have $P(x)=P_Y^{(1)}(y)P_Z^{(2)}(z)\geq 0$ and

$$
\sum_x P(x)
=
\sum_y \sum_z P(y,z)
=
\left(\sum_y P_Y^{(1)}(y)\right)\left(\sum_z P_Z^{(2)}(z)\right)
=1.
$$

Furthermore, for all $c^{(1)} \in C$ with scope $\operatorname{scope}(c^{(1)})=Y^{(1)}$, we have

$$
\begin{aligned}
c^{(1)}(P)
&=
\sum_y \sum_z P_Y^{(1)}(y)P_Z^{(2)}(z) f_{c^{(1)}}(y|_{Y^{(1)}}) \\
&=
\left(\sum_z P_Z^{(2)}(z)\right)
\left(\sum_y P_Y^{(1)}(y) f_{c^{(1)}}(y|_{Y^{(1)}})\right)
= 0,
\end{aligned}
$$

since $P^{(1)} \in \operatorname{Mod}(c^{(1)})$. Hence, $P \in \operatorname{Mod}(C)$. Analogously, it follows that for all constraints relevant to $SPMod^{l+1}(KB)$, we have that they attain the same value for $P$ as for $P^{(2)}$. But this implies that also $P \in SPMod^{l+1}(KB)$ (for $P^{(2)}$ and $P$ yield the same objective value for all optimization problems) and therefore $\operatorname{Mod}(C) \cap SPMod^{l+1}(KB) \neq \emptyset$. $\square$

So if $C$ is independent of subsets of higher priority, we know that there is at least one model of $C$ in $SPMod^{l+1}(KB)$. However, this does not mean that a model of $C$ will be in $SPMod^l(KB)$ because the probability distributions in $\operatorname{Mod}(C)\cap SPMod^{l+1}(KB)$ might strongly violate the remaining constraints in $KB_l \setminus C$. This case, however, is only possible if there are dependencies between $C$ and $KB_l \setminus C$ as explained in the following proposition. In fact, if there are no such dependencies, then even $SPMod^l(KB) \subseteq \operatorname{Mod}(C)$ holds, i.e., all $P \in SPMod^l(KB)$ are models of $C$.

**Proposition 4 (Level Independence).** Let $KB = (KB_1, \ldots, KB_k, IC)$ be a valid linear priority knowledge base over $X$ and let $\|\cdot\|$ be some continuous vector norm. Let $C \subseteq KB_l$ for some $l<k$ such that $\operatorname{Mod}(C)\cap SPMod^{l+1}(KB)\neq \emptyset$. If

$$
\operatorname{scope}(C) \cap \operatorname{scope}(KB_l \setminus C) = \emptyset,
$$

then

$$
SPMod^l(KB) \subseteq \operatorname{Mod}(C). \tag{5}
$$

**Proof.** For the sake of contradiction, assume that $P^{(l)} \in SPMod^l(KB)$ and that $P^{(l)} \notin \operatorname{Mod}(C)$. Let $Y=\operatorname{scope}(C)$ and let $Z=X \setminus Y$. Then $\operatorname{scope}(KB_l \setminus C) \subseteq Z$ by assumption. Let $P^C \in (\operatorname{Mod}(C)\cap SPMod^{l+1}(KB))$ and let $P_Y^C$ denote the probability distribution obtained from $P^C$ by marginalizing out $Z$. Let $P_Z^{(l)}$ denote the probability distribution obtained from $P^{(l)}$ by marginalizing out $Y$. Just like in the proof of Proposition 3, we can check that

$$
P(y,z)=P_Y^C(y)P_Z^{(l)}(z)
$$

is a probability distribution over $X$ that coincides with $P^C$ for the constraints in $C$ and that coincides with $P^{(l)}$ for the constraints in $KB_l \setminus C$. That is,

$$
c(P)=c(P^{(l)}) \text{ for all } c \in KB_l \setminus C
$$

and

$$
c(P)=0 \text{ for all } c \in C
$$

since $P^C \in \operatorname{Mod}(C)$. This implies in particular that $P \in SPMod^{l+1}(KB)$. But since $P^{(l)} \notin \operatorname{Mod}(C)$, there is a $c \in C$ such that $c(P^{(l)}) \neq 0$. But this means that

$$
\|A_{KB_l}P\| < \|A_{KB_l}P^{(l)}\|
$$

contradicting $P^{(l)} \in SPMod^l(KB)$ (for then $\|A_{KB_l}P^{(l)}\|=\min_{P' \in SPMod^{i+1}(KB)} \|A_{KB_i}P'\|$). Hence, if $P^{(l)} \in SPMod^l(KB)$, then $P^{(l)} \in \operatorname{Mod}(C)$ must also hold. $\square$

**Remark 4.** Note that by the subset relationships from Lemma 1.2, $SPMod^l(KB) \subseteq \operatorname{Mod}(C)$ implies that $SPMod(KB) \subseteq \operatorname{Mod}(C)$. That is, if the assumptions of Upward and Level Independence are satisfied for $C$, then each strict priority model of $KB$ will also be a model of $C$.

## 3.2 Weighted Priority Models

Even though strict priority models have some nice properties, they cannot guarantee that subsets of low priority have any influence on the final outcome of $SPMod(KB)$ unless they are consistent with or independent of the upper levels. In fact, in some extreme cases, $SPMod^l(KB)$ might contain only a single distribution for some $l>1$. Then $SPMod^{l'}(KB)=SPMod^l(KB)$ whenever $1 \leq l' < l$.

In order to allow that each subset of our priority knowledge base has some influence on the final outcome, let us consider another approach to define models of prioritized knowledge bases. Instead of considering the subsets successively based on their priorities, we consider them simultaneously but weigh them with respect to their priority.

**Definition 3 (Weighted Priority Models).** Let $KB = (KB_1, \ldots, KB_k, IC)$ be a linear priority knowledge base over $X$, let $\|\cdot\|$ be some continuous vector norm and let $w:\{1,2,\ldots,k\}\to \mathbb{R}_{>0}$ be some monotonically increasing weight function. We let

$$
WPMod^w_{\|\cdot\|}(KB)
=
\arg\min_{P \in \operatorname{Mod}(IC)}
\left\|
\begin{pmatrix}
w(1)\cdot A_{KB_1} \\
\vdots \\
w(k)\cdot A_{KB_k}
\end{pmatrix}
P
\right\|
$$

and call $WPMod^w_{\|\cdot\|}(KB)$ the set of weighted priority models of $KB$.

**Remark 5.**
1. Again, we omit the superscript $w$ and the subscript $\|\cdot\|$ to enhance readability, but keep in mind that $SPMod(KB)$ depends on both.
2. The symbol $\cdot$ denotes scalar multiplication. Hence, each row in $A_{KB_i}$ is multiplied by $w(i)$.

$WPMod(KB)$ has the same nice properties like $SPMod(KB)$. The claim follows from similar arguments like Lemma 1.1, so that we omit the proof.

**Lemma 2.** Let $KB = (KB_1, \ldots, KB_k, IC)$ be a linear priority knowledge base over $X$ and let $\|\cdot\|$ be some continuous vector norm. If $KB$ is valid, then $WPMod(KB)$ is non-empty, compact and convex.

Hence, in particular, $WPMod(KB)$ is always non-empty and by definition a subset of $\operatorname{Mod}(IC)$. We emphasize this as a counterpart to Propositions 1 and 2. Note that we can guarantee only that the integrity constraints are satisfied.

**Proposition 5 (Integrity).** Let $KB = (KB_1, \ldots, KB_k, IC)$ be a linear priority knowledge base over $X$ and let $\|\cdot\|$ be some continuous vector norm. If $KB$ is valid, then

$$
\emptyset \neq WPMod(KB) \subseteq \operatorname{Mod}(IC).
$$

**Example 6.** Let us compute probability bounds like in Example 4, but this time using weighted priority models. We use again the Euclidean norm and the weight function $w(p)=2\cdot p$ (in theory, we might have used the identity function as well, but it caused numerical problems). This yields the following rounded results:

- $grantAccess(alice, file1)[0.44]$
- $grantAccess(bob, file1)[0.14]$
- $grantAccess(alice, file2)[0.63]$
- $grantAccess(bob, file2)[0.4]$
- $blacklisted(alice)[0.005]$
- $blacklisted(bob)[0.018]$

The fact that the access probability for `file2` is significantly lower for `alice` than for `bob` indicates that all levels have been taken into account. However, given the access probability of `alice` for `file1`, one might argue that the lower levels have too much influence (`alice` being an executive manager should weigh stronger than `file1` being confidential). To increase the weight of the upper priority levels, let us consider a non-linear weight function. We let $w(p)=10^{p-1}$ for $1 \leq p \leq 5$. This yields the following rounded results:

- $grantAccess(alice, file1)[0.693]$
- $grantAccess(bob, file1)[0.005]$
- $grantAccess(alice, file2)[0.7]$
- $grantAccess(bob, file2)[0.5]$
- $blacklisted(alice)[0.001]$
- $blacklisted(bob)[0.01]$

There is still a minor decrease in the access probability of `alice` for `file1`, but overall the results are very close to what one might expect when looking at the priority knowledge base from Example 4.

There is probably no immediate counterpart to the independence properties of strict priority models if we do not make any restrictions on the weight function. In fact, the whole point of weighted priority models is to allow that each subset of the knowledge base influences the outcome, so that we should not expect strong independence properties between priority levels. We might prove some weaker independence properties which do not make use of the priorities, but we leave this for future work.

## 3.3 Implementations

Probabilistic Entailment with strict and with weighted priority models has been implemented in the Java library Log4KR[^1]. The optimization problems are solved by OjAlgo[^2]. You can find the source code and some source examples in the subdirectory

`edu.cs.ai.log4KR.structuredLogics.priorityReasoning`

of the corresponding directories. Note that numerical problems might cause odd results.

# 4 Related Work

If we consider a trivial priority knowledge base consisting only of a single subset with priority 1 and do not demand that this subset is consistent, both the strict and the weighted priority models correspond to the generalized models from [22–24]. In this sense, prioritized reasoning generalizes generalized reasoning approaches from [23,24]. Generalized reasoning, in turn, generalizes common probabilistic reasoning [10–12,17,20,21] in the sense that the generalized models are the usual probabilistic models if the knowledge base is consistent.

Daniel generalized probabilistic models in a similar way and called his generalization the best candidates [7]. To define best candidates, he identified linear constraint functions with the hyperplanes corresponding to their solution sets. Given a probability function $P$ and a linear constraint $c$, he defined the gap between $P$ and $c$ as the Euclidean distance between $P$ and the hyperplane corresponding to $c$. The best candidates can then be defined as the solution set

$$
\arg\min_{P \in P_X} \prod_{c \in R} h([illegible]\operatorname{gap}(P,c)),
$$

where $h$ is some strictly decreasing, (strictly) positive and continuous log-concave function such that $h(0)=1$, see [7], Definition 13. The best candidates satisfy similar nice properties like the generalized models, namely they form a compact and convex set, which corresponds to the usual models if $R$ is consistent. Daniel considered only reasoning with the best candidate having maximum entropy, but, in principle, the best candidates can also be applied to other probabilistic reasoning approaches.

Figure 1 illustrates the relationships between the different notions of models.

**Figure 1. Generalizations of Probabilistic Models: Generalized Models and Best Candidates generalize Probabilistic Models. Strict and Weighted Priority Models generalize Generalized Models (see Sect. 4 for details).**

**Figure description:** The figure is a conceptual hierarchy diagram. It depicts “Probabilistic Models” as the base notion. “Generalized Models” and “Best Candidates” are shown as generalizations of Probabilistic Models. From “Generalized Models,” two further notions branch out: “Strict Priority Models” and “Weighted Priority Models,” indicating that both are extensions of the generalized-model approach rather than direct extensions of classical probabilistic models.

# 5 Conclusions

We proposed two methods to reason with linear probabilistic knowledge bases with priorities. Strict priority models provide some nice guarantees. The rules with highest priority are guaranteed to be satisfied; the same is true for rules with lower priority if they are consistent with or independent of higher priority levels. However, high priority rules can be so restrictive that low priority rules become meaningless. In such cases, weighted priority models can be more appropriate. If we make no restrictions on the weight function, they can only guarantee that the integrity constraints are satisfied. However, sometimes this is just what we want to guarantee that even low priority rules are taken into account.

Our results hold for linear probabilistic knowledge bases in general. These arise naturally from different probabilistic logics, see, e.g., [9,10,14,20] for some examples beyond our simple relational language. In fact, the results can be generalized to inequality constraints by just introducing slack variables as done in [8] for generalized models. Inequality constraints are, indeed, desirable to allow imprecise probabilities like in [9,17–19]. However, since the notation becomes more cumbersome, we did not consider inequality constraints here.

We also did not discuss computational aspects. However, note that we can apply similar ideas like in [23,24] to show that several interesting reasoning problems for priority knowledge bases can be solved by convex programming techniques. For instance, computing upper and lower bounds on the probability of formulas corresponds to a convex program. If we restrict to $p$-Norms, the problem remains convex if we allow conditional probabilities and becomes quadratic for $p=2$ and linear for $p=1,\infty$.

# References

1. Adamcík, M.: *Collective Reasoning under Uncertainty and Inconsistency*. Ph.D. thesis, University of Manchester (2014)

2. Amgoud, L., Kaci, S.: An argumentation framework for merging conflicting knowledge bases. *Int. J. Approximate Reasoning* **45**(2), 321–340 (2007)

3. Benferhat, S., Dubois, D., Kaci, S., Prade, H.: Possibilistic merging and distance-based fusion of propositional information. *Ann. Math. Artif. Intell.* **34**(1–3), 217–252 (2002)

4. Bonatti, P.A., Faella, M., Sauro, L.: Adding default attributes to EL++. In: *Proceedings of the Twenty-Fifth AAAI Conference on Artificial Intelligence, AAAI 2011* (2011)

5. Brewka, G.: Reasoning about priorities in default logic. In: *AAAI 1994*, pp. 940–945 (1994)

6. Britz, K., Heidema, J., Meyer, T.A.: Semantic preferential subsumption. In: *KR 2008*, pp. 476–484 (2008)

7. Daniel, L.: *Paraconsistent Probabilistic Reasoning*. Ph.D. thesis, L’Ecole Nationale [illegible] Supérieure des Mines de Paris (2009)

8. De Bona, G., Finger, M.: Measuring inconsistency in probabilistic logic: rationality postulates and dutch book interpretation. *Artificial Intelligence* (2015, to appear)

9. De Bona, G., Cozman, F.G., Finger, M.: Towards classifying propositional probabilistic logics. *J. Appl. Logic* **12**(3), 349–368 (2014)

10. Fisseler, J.: First-order probabilistic conditional logic and maximum entropy. *Logic J. IGPL* **20**(5), 796–830 (2012)

11. Jaumard, B., Hansen, P., Poggi, M.: Column generation methods for probabilistic logic. *ORSA - J. Comput.* **3**(2), 135–148 (1991)

12. Kern-Isberner, G.: *Conditionals in Nonmonotonic Reasoning and Belief Revision*. LNCS (LNAI), vol. 2087. Springer, Heidelberg (2001)

13. Kern-Isberner, G., Rödder, W.: Belief revision and information fusion in a probabilistic environment. In: *Proceedings 16th International FLAIRS Conference, FLAIRS 2003*, pp. 506–510. AAAI Press, Menlo Park (2003)

14. Kern-Isberner, G., Thimm, M.: Novel semantical approaches to relational probabilistic conditionals. In: Lin, F., Sattler, U., Truszczynski, M. (eds.) *Proceedings Twelfth International Conference on the Principles of Knowledge Representation and Reasoning, KR 2010*, pp. 382–391. AAAI Press (2010)

15. Konieczny, S., Pérez, R.P.: Logic based merging. *J. Philos. Logic* **40**(2), 239–270 (2011)

16. Kraus, S., Lehmann, D., Magidor, M.: Nonmonotonic reasoning, preferential models and cumulative logics. *Artif. Intell.* **44**(1), 167–207 (1990)

17. Lukasiewicz, T.: Probabilistic deduction with conditional constraints over basic events. *J. Artif. Intell. Res.* **10**, 380–391 (1999)

18. Lukasiewicz, T.: Expressive probabilistic description logics. *Artif. Intell.* **172**(6), 852–883 (2008)

19. Lutz, C., Schröder, L.: Probabilistic description logics for subjective uncertainty. In: *Proceedings of KR 2010*. AAAI Press (2010)

20. Nilsson, N.J.: Probabilistic logic. *Artif. Intell.* **28**, 71–88 (1986)

21. Paris, J.B., Vencovská, A.: On the applicability of maximum entropy to inexact reasoning. *Int. J. Approximate Reasoning* **3**(1), 1–34 (1989)

22. Potyka, N.: Linear programs for measuring inconsistency in probabilistic logics. In: *Proceedings KR 2014*. AAAI Press (2014)

23. Potyka, N., Thimm, M.: Consolidation of probabilistic knowledge bases by inconsistency minimization. In: *Proceedings ECAI 2014*, pp. 729–734. IOS Press (2014)

24. Potyka, N., Thimm, M.: Probabilistic reasoning with inconsistent beliefs using inconsistency measures. In: *International Joint Conference on Artificial Intelligence 2015 (IJCAI 2015)* (2015, to appear)

25. Qi, G., Liu, W., Bell, D.A.: Merging stratified knowledge bases under constraints. In: *The Twenty-First National Conference on Artificial Intelligence and the Eighteenth Innovative Applications of Artificial Intelligence Conference, July 16–20, 2006, Boston, Massachusetts, USA*, vol. 21, p. 281. AAAI Press, Menlo Park; MIT Press, Cambridge 1999 (2006)

26. Wilmers, G.: A foundational approach to generalising the maximum entropy inference process to the multi-agent context. *Entropy* **17**(2), 594–645 (2015)

[^1]: https://www.fernuni-hagen.de/wbs/research/log4kr/index.html
[^2]: http://ojalgo.org/

```

```
OCR quality was generally good because parsed text was provided page by page, but several issues remain.

1. Page 1:
- "Fern Universit¨at" was normalized to "Fern Universität" as an obvious OCR diacritic issue.
- "di!erent" corrected to "different".
- "inconsisten￾cies" corrected to "inconsistencies".
- "infor￾mation" corrected to "information".
- "betweens rules" likely should be "between rules" in the source, but I preserved the parsed text except for obvious OCR; this phrase may deserve verification against the PDF.

2. Pages 3–5, formulas:
- Several logical symbols were degraded in OCR. I reconstructed formulas where the intended notation was clear from context.
- In Example 3, the OCR dropped negation marks / disambiguation in the derivation. I reconstructed the standard form:
  - $P(\phi \land \psi) + P(\neg \phi \land \psi)$
  - $\mathbf{1}_{\{\neg \phi \land \psi\}}$
  This is strongly supported by the surrounding prose (“verified” vs “falsified”), but should still be checked against the original PDF.
- The notation around feature functions had OCR corruption such as " :=f(Y)" and unclear scope markers. These were normalized.

3. Page 5:
- The parsed text says the constraint matrix corresponding to KB is a "(1 × N)-matrix" even though the displayed object is clearly an $M \times N$ matrix. I corrected this to "$(M \times N)$-matrix" as an obvious typo/OCR inconsistency.

4. Page 6:
- In integrity constraints, OCR produced `(grantAccess(U, F)| blacklisted(U)(F))[0]`, which is malformed. I reconstructed it as `(grantAccess(U,F) | blacklisted(U))[0]`, which matches the explanatory text “we do not grant access to blacklisted users.” This should be verified against the original PDF.

5. Pages 7–11, propositions and proofs:
- Some OCR artifacts affected indices/superscripts, e.g. `SPModl # (KB)` and malformed minimization notation. I normalized these where the intended mathematics was inferable.
- In Proposition 3 proof, the parsed text incorrectly referred to `c(1) ∈ SPModl+1(KB)` where it should refer to constraints in `C` / relevant higher-level constraints. I transcribed conservatively while keeping the proof readable; the PDF should be checked if exact formal symbols matter.
- In Proposition 4 proof, the minimization index `SPMod^{i+1}(KB)` appears in the OCR though the local level is `l`; this may be an OCR or source typo. I preserved the mathematical intent while noting uncertainty.

6. Page 11–12:
- In Remark 5, item 1 says `SPMod(KB)` depends on both, but in context it should likely be `WPMod(KB)` depends on both the norm and the weight function. I preserved the text as given in the transcription body only where the sentence appeared, but this is likely a source typo or OCR confusion.

7. Page 13, Related Work formula:
- The formula defining best candidates is incomplete/corrupted in OCR. The term before `gap(P,c)` appears as `[illegible]`; likely something like $\sqrt{2^n}$ or a similar scaling factor, but I did not guess. This is the main unresolved formula-level uncertainty.
- URLs in footnotes were readable and transcribed.

8. Figure 1 (page 14):
- The actual visual layout of the figure was not provided in the parsed text, only the caption. I included a detailed natural-language description rather than a diagram recreation.

9. Reference section:
- Most references were readable.
- Reference 7 contains OCR corruption in the institution name: `L’Ecole Nationale [illegible] Supérieure des Mines de Paris`. The accenting and one word were not fully recoverable from the parsed text.
- A few diacritics were normalized where obvious: `Rödder`, `Pérez`, `Schröder`, `Vencovská`.

10. General:
- Running headers/page numbers were omitted from the markdown body except bibliographic front matter.
- I corrected obvious OCR ligature and hyphenation issues, but did not attempt speculative semantic editing beyond places where the formula/text was clearly reconstructable from context.
```