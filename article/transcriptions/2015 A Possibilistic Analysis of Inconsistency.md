# A Possibilistic Analysis of Inconsistency

Didier Dubois and Henri Prade (B)  
IRIT–CNRS, 118, Route de Narbonne, Toulouse, France  
{dubois,prade}@irit.fr

## Abstract

Central in standard possibilistic logic (where propositional logic formulas are associated with lower bounds of their necessity measures), is the notion of inconsistency level of a possibilistic logic base. Formulas whose level is strictly above this inconsistency level constitute a sub-base free of any inconsistency. Some extensions, based on the notions of paraconsistent completion of a possibilistic logic base, and of safely supported formulas, have been proposed for handling formulas below the level of inconsistency. In this paper we further explore these ideas, and show the interest of considering the minimal inconsistent subsets in this setting. Lines for further research are also outlined.

## 1 Introduction

Reasoning under inconsistency [6,13], or evaluating the inconsistency of a knowledge base [10,11] have raised a lot of interest in artificial intelligence for a long time. However, the different approaches which have been proposed do not usually take into account the fact that all the formulas in a knowledge base are not necessarily equally certain. Possibilistic logic [8] provides a simple way for a partial handling of inconsistency by taking advantage of a stratification of the knowledge base according to the certainty level associated to the logical formulas. Then we can compute an inconsistency level for a propositional knowledge base, and all the formulas whose certainty is strictly above this inconsistency level form a consistent sub-base. The formulas whose certainty is equal to or smaller than the inconsistency level remain drown in inconsistency, including formulas that are not involved in any minimal inconsistent subsets. This state of fact can be somewhat remedied by defining a paraconsistent completion of the knowledge base, and by using a so-called safely supported entailment relation [3,5]. Strangely enough, this entailment is more productive than the possibilistic logic entailment, but it nevertheless preserves the consistency of the set of consequences. Yet it has remained largely ignored. This short paper revisits the approach and shows its relation with minimal inconsistent subsets.

The paper is structured as follows. Section 2 deals with the flat case [4] where formulas are not associated with certainty levels. We present the idea of paraconsistent completion as a basis for analyzing the conflicts, and then identify the safely supported consequences. In Sect. 3, we deal with possibilistic logic formulas, and extend the previous definitions. Then a new characterization of safely supported entailment is proposed. Lines for further research are also discussed.

© Springer International Publishing Switzerland 2015  
C. Beierle and A. Dekhtyar (Eds.): SUM 2015, LNAI 9310, pp. 347–353, 2015.  
DOI: 10.1007/978-3-319-23540-0_23

## 2 Flat Propositional Knowledge Bases

Let $\Sigma = \{p_i \mid i = 1, \ldots, n\}$ denote a propositional logic knowledge base. $\Sigma$ may be inconsistent. Let us first recall two basic notions, needed in the forthcoming discussion: the notions of support for a proposition and of minimal inconsistent subset. A $\Sigma$-based support (or reason, or argument) for a proposition $p$ is a subset $S_p$ of propositions in $\Sigma$ such that (i) $S_p$ is consistent; (ii) $S_p \vdash p$ (where $\vdash$ is the classical logic consequence relation); (iii) $\nexists S' \subset S_p$ such that $S' \vdash p$. In other words, $S_p$ is a minimal consistent subset of propositions in $\Sigma$ that together entail $p$. Likewise, a minimal inconsistent subset of $\Sigma$ is a minimal subset of propositions that entail $\bot$: a non empty subset $S_{\bot}$ of $\Sigma$ such that (i) $S_{\bot}$ is inconsistent ($S_{\bot} \vdash \bot$); (ii) $\nexists S' \subset S_{\bot}$ such that $S' \vdash \bot$.

For a complete analysis of the inconsistency situation of formulas in $\Sigma$, we need to define the “paraconsistent completion” $\Sigma_{\mathrm{comp}}$ of $\Sigma$.

### 2.1 Paraconsistent Completion

For analyzing the potential conflicts in $\Sigma$, it is convenient to proceed with the following construction. The paraconsistent completion $\Sigma_{\mathrm{comp}}$ of $\Sigma$ is obtained by applying the following procedure: to each formula $p_i$ in $\Sigma$, one associates i) the set of reasons for $p_i$, and ii) the set of reasons for $\neg p_i$. More formally,

$$
\Sigma_{\mathrm{comp}} =
\{(p_i, \{P_1, \cdots, P_r\}, \{C_1, \cdots, C_s\}) \mid p_i \in \Sigma,\; P_i \text{ is a reason for } p_i,\; C_j \text{ is a reason for } \neg p_i\}.
$$

Clearly, if $p_i \in \Sigma$, then $(p_i, \{P_1, \cdots, P_r\}, \{C_1, \cdots, C_s\}) \in \Sigma_{\mathrm{comp}}$, and if $\exists j$ s.t. $p_j \equiv \neg p_i$ then $(\neg p_i, \{P'_1, \cdots, P'_s\}, \{C'_1, \cdots, C'_r\}) \in \Sigma_{\mathrm{comp}}$ with $\forall i\; P'_i = C_i$, $\forall j\; C'_j = P_j$. Note that as soon as $p_i \in \Sigma$, the set of reasons for $p_i$ is not empty: it contains at least $\{p_i\}$.

The reasons for and against $p_i$ can be summarized by triples of the form $(p_i, \pi_i, \gamma_i)$ for $i = 1, \ldots, n$ where $\pi_i \in \{0, 1\}$, $\gamma_i \in \{0, 1\}$, and: (i) $p_i \in \Sigma$; (ii) $\pi_i = 1$ for acknowledging the fact that $\exists P_k$, a reason for $p_i$; (iii) $\gamma_i = 1$ if $\exists C_l$ that is a reason for $\neg p_i$, and $\gamma_i = 0$ if $\nexists C_l$ (no reason for $\neg p_i$). Let

$$
\Sigma_{\mathrm{para}} = \{(p_i, \pi_i, \gamma_i) : i = 1, \ldots, n\}.
$$

Note that $\pi_i \neq 0$ (hence $= 1$), since each $p_i \in \Sigma$ supports itself.

If $\min(\pi_i, \gamma_i) = 1$, then $p_i$ is said to be paraconsistent (in the sense of “conflicting”). Thus in $\Sigma$, there are two kinds of propositions, the formulas $p_i$ such as $\gamma_i = 0$ which should be considered as true, and the formulas that are paraconsistent. Note that strictly speaking there is no formula of the form $(p_j, 0, 1)$ in $\Sigma_{\mathrm{para}}$ since the information that $p_j$ is false appears there only under the form $(\neg p_j, 1, 0)$, i.e. $\neg p_j$ is true. However, note also that one may have $(p_i, \{\{p_j\}\}, \{C_1, \cdots, C_s\}) \in \Sigma_{\mathrm{comp}}$, where no $C_k$ contains $\neg p_j$, which might be understood as suggesting that $p_j$, being only supported by itself, is questionable. Besides, there is no formula of the form $(p_k, 0, 0)$ in $\Sigma_{\mathrm{para}}$ (it would express that there is no reason for $p_k$, nor for $\neg p_k$).

### 2.2 Safely Supported Propositions

Once $\Sigma_{\mathrm{comp}}$ and $\Sigma_{\mathrm{para}}$ are built from $\Sigma$, one can evaluate reasons $S$ in favor of a proposition $p$ by means of the two evaluations, $\mathrm{Def}(S)$ and $\mathrm{Uns}(S)$, respectively revealing the potential weakness of its support and its lack of safety:

- $\mathrm{Def}(S) = \min_i\{\pi_i \mid (p_i,\pi_i,\gamma_i) \in \Sigma_{\mathrm{para}} \text{ and } p_i \in S\}$.

  In fact, one always has $\mathrm{Def}(S) = 1$ since $\forall i$, $p_i \in S$, we have $\pi_i = 1$, and the case $\mathrm{Def}(S) = 0$ is impossible here since $p_i$ is in $\Sigma$ ($p_i \in \Sigma$ is understood as $(p_i, 1)$). We shall see that when propositional formulas become weighted, we still always have $\mathrm{Def}(S) > 0$, but $\mathrm{Def}(S)$ may be “close to $0$”.

- $\mathrm{Uns}(S) = \max_i\{\gamma_i \mid (p_i,\pi_i,\gamma_i) \in \Sigma_{\mathrm{para}} \text{ and } p_i \in S\}$.

Clearly, $\mathrm{Uns}(S) = 0$ if $\forall i \mid p_i \in S$, $\gamma_i = 0$, i.e. if $S$ does not contain any paraconsistent formula, while $\mathrm{Uns}(S) = 1$ if $\exists i \mid p_i \in S$, $\gamma_i = 1$, i.e. there is at least one paraconsistent formula in $S$. Thus, $\mathrm{Uns}(S)$ reflects if there are a reason pro and a reason against an element of $S$ that can be both built from formulas in $\Sigma$.

A reason $S$ in favor of proposition $p$ is free iff $\mathrm{Def}(S) > \mathrm{Uns}(S)$, i.e. iff all the formulas in $S$ are believed to be true and none is inconsistent with other formulas in $\Sigma$. By extension, in this case, we shall say all the formulas in $S$ are free as well. Moreover, any formula in a minimal inconsistent subset $S_{\bot} = \{r_1, r_2, \cdots, r_k\}$ of $\Sigma$ is not free, since $S_{\bot} \setminus \{r_j\}$ is consistent and $\forall j$, $S_{\bot} \setminus \{r_j\} \vdash \neg r_j$. Thus, if $\exists S_{\bot}$, $r_j \in S_{\bot} \subseteq \Sigma$ then $(r_j, 1, 1) \in \Sigma_{\mathrm{para}}$, i.e., $r_j$ is a paraconsistent formula in $\Sigma$. If a formula is involved in several minimal inconsistent subsets, one might think that this formula could be considered as more “paraconsistent” since there exists several distinct reasons against it. However, this looks debatable since a “basic” piece of information often used in inferences may have some chance to be, on the contrary, strongly established.

In the classical case, $\mathrm{Def}(S) > \mathrm{Uns}(S) \Leftrightarrow \mathrm{Uns}(S) = 0$, since then $\mathrm{Def}(S) = 1$. Thus, a proposition $p$ is safely supported if it exists a reason $S$ for it which is free. The safely supported propositions are just the consequences of the set of free ones. It follows that the set of safely supported formulas in $\Sigma$ is always consistent. So in particular, $p$ and $\neg p$ cannot be both safely supported.

This departs from the so-called argumentative inference [2], which is more adventurous than the safely supported inference, since it may lead to an inconsistent set of conclusions, but not to direct contradictions such as $p$ and $\neg p$. The argumentative inference amounts to conclude $p$ if there is a reason for $p$ and no reason for $\neg p$ in $\Sigma$.

For instance, consider the base $\Sigma = \{r, \neg r \vee p, \neg r, r \vee q\}$. Then, we can infer both $p$ and $q$ argumentatively from $\Sigma$. In contrast, the reader can check that

$$
\Sigma_{\mathrm{para}} = \{(r,1,1),(\neg r,1,1),(\neg r \vee p,1,0),(r \vee q,1,0)\},
$$

from which one can infer neither that $p$ nor $q$ is safely supported.

Still, as recalled in the discussion section, one can also infer $(p,1,1)$ and $(q,1,1)$ from $\Sigma_{\mathrm{para}}$, thus acknowledging that $p$ and $q$ are indeed paraconsistent conclusions.

We now examine how the notions of reason, of paraconsistent completion, and of safely supported proposition can become graded.

## 3 Possibilistic Logic Bases

We now assume that the propositions that are elements of a reason supporting a proposition may be pervaded with uncertainty. More precisely, the propositions $p_i$ are now replaced by possibilistic logic formulas [8] of the form $(p_i, a_i)$, i.e., $p_i$ is believed with certainty at least $a_i$, $a_i$’s belonging to a linearly ordered, bounded scale $S = \{s_1 = 1 > s_2 > \cdots > s_{n+1} = 0\}$, with top and bottom elements denoted by $1$ and $0$ respectively.

Let $\Sigma = \{(p_i, a_i) \mid i = 1, \cdots, m\}$, where $a_i$ is the strength with which $p_i$ is believed to be true in $\Sigma$. The higher $a_i$, the higher the strength. Thus, $(p,a)$ is subsumed by $(p,b)$ as soon as $b > a$. So, it is assumed that $\Sigma$ does not contain both $(p_i, a_i)$ and $(p_j, a_j)$ with $p_i \equiv p_j$ and $a_i \neq a_j$. Let $\Sigma^* = \{p_i \mid (p_i, a_i) \in \Sigma\}$. Similarly, if $S \subseteq \Sigma$, $S^*$ denotes the set of propositions appearing in the possibilistic formulas in $S$ without their weight. The set of propositions $\Sigma^*$ is not assumed to be consistent. In possibilistic logic, this amounts to say that the inconsistency level of $\Sigma$ is strictly positive [8].

A subset $S$ of $\Sigma$ is said to be a reason for $p$ iff (i) $S^*$ is consistent; (ii) $\exists a > 0$, $S \vdash_{\pi} (p, a)$ where $\vdash_{\pi}$ is the possibilistic logic entailment[^1]; (iii) $\nexists S' \subset S$ such that $S' \vdash_{\pi} (p, b)$ with $b > 0$.

[^1]: Possibilistic inference is governed by the resolution rule $(\neg p \vee q, a), (p \vee r, b) \vdash_{\pi} (q \vee r, \min(a,b))$ [8].

In other words, $S$ is such that $S^*$ is a minimal consistent subset of propositions that entail $p$ and $a$ is the minimum of the weights of the formulas in $S$. $a$ is the weight of the reason. Clearly there may exist distinct reasons $S$ and $S'$ (with $S^* \neq S'^*$) for $p$ in $\Sigma$. Thus the pair $(S, (p, a))$ is a (possibilistic) argument for $p$ with strength $a$, with $a = \min\{a_i \mid (p_i, a_i) \in S\}$.

### 3.1 Graded Paraconsistent Completions

On this basis, one can extend the completions $\Sigma_{\mathrm{comp}}$ and $\Sigma_{\mathrm{para}}$ to a possibilistic logic base $\Sigma$. Namely to each formula $p_i$ in $\Sigma^*$, one may associate i) the set of reasons for $p_i$, and the set of reasons for $\neg p_i$, or ii) or only the weights of the best reason for $p_i$ and of the best reason for $\neg p_i$.

More formally, the first one is defined by

$$
\Sigma_{\mathrm{comp}} =
\{(p_i, \{P_1, \cdots, P_r\}, \{C_1, \cdots, C_s\}) \mid (p_i, a_i) \in \Sigma,\; P_i \text{ is a (graded) reason for } p_i,\; C_j \text{ is a (graded) reason for } \neg p_i\}.
$$

The second completion is defined by

$$
\Sigma_{\mathrm{para}} =
\{(p_i, \pi_i, \gamma_i) \mid (p_i, a_i) \in \Sigma,\; \pi_i \text{ is the greatest weight of a reason for } p_i \text{ in } \Sigma,\; \gamma_i \text{ is the greatest weight of a reason for } \neg p_i \text{ in } \Sigma\}.
$$

Note that $\pi_i \geq a_i$.

**Example.** $\Sigma = \{(p, s_1),(\neg p \vee q, s_2),(\neg p, s_3),(\neg r, s_4),(r, s_5),(\neg r \vee q, s_6)\}$ (with $s_6 > 0$).

Then

$$
\Sigma_{\mathrm{para}} =
\{(p,s_1,s_3),(\neg p \vee q,s_2,0),(\neg p,s_3,s_1),(\neg r,s_4,s_5),(r,s_5,s_4),(\neg r \vee q,s_2,0)\}.
$$

$$
\begin{aligned}
\Sigma_{\mathrm{comp}} = \{&
(p,\{\{(p,s_1)\}\},\{\{(\neg p,s_3)\}\}),\\
&(\neg p \vee q,\{\{(\neg p \vee q,s_2)\}\},\emptyset),\\
&(\neg p,\{\{(\neg p,s_3)\}\},\{\{(p,s_1)\}\}),\\
&(\neg r,\{\{(\neg r,s_4)\}\},\{\{(r,s_5)\}\}),\\
&(r,\{\{(r,s_5)\}\},\{\{(\neg r,s_4)\}\}),\\
&(\neg r \vee q,\{\{(p,s_1),(\neg p \vee q,s_2)\},\{(\neg r,s_4)\}\},\emptyset)\}.
\end{aligned}
$$

### 3.2 Graded Safely Supported Propositions

The notion of safely supported proposition then extends to possibilistic propositional formulas with weights. Once $\Sigma_{\mathrm{para}}$ is built from $\Sigma$, one can evaluate reasons $S$ in favor of $p_i$ in the following way, by means of the two measures [3,5]:

- $\mathrm{Def}(S) = \min\{\pi_i \mid ((p_i,\pi_i,\gamma_i) \in \Sigma_{\mathrm{para}} \text{ and } p_i \in S^*\}$.
- $\mathrm{Uns}(S) = \max\{\gamma_i \mid ((p_i,\pi_i,\gamma_i) \in \Sigma_{\mathrm{para}} \text{ and } p_i \in S^*\}$.

$\mathrm{Def}(S)$ reflects the less certain belief in $S$, $\mathrm{Uns}(S)$ the most strongly attacked belief in $S$. Note that we always have $\mathrm{Def}(S) > 0$, but $\mathrm{Def}(S)$ may be equal to $s_n$, and thus now “close to $0$”.

A reason is free iff $\mathrm{Def}(S) > \mathrm{Uns}(S)$, i.e. iff its certainty is above the strength of the strongest attack. Then a proposition $p$ is safely supported if it exists a reason $S$ that is free for it. It can be shown [5] that the set of safely supported consequences of a base $\Sigma$ is always consistent. So in particular, $p$ and $\neg p$ cannot be both safely supported.

It clearly generalizes the case of a binary scale, i.e. a scale $S$ with only two levels $1$ and $0$, (where the condition $\mathrm{Def}(S) > \mathrm{Uns}(S)$ can only hold under the form $\mathrm{Uns}(S) = 0$), which means that all the formulas in $S$ are fully believed and none is attacked. In the graded case, the formulas involved in $S$ are only more believed than they are attacked.

Let us come back to minimal inconsistent subsets. Let $S$ be a minimal inconsistent subset in $\Sigma^*$, and let

$$
\mathrm{inc}(S) = \min\{a_j \mid (p_j,a_j) \in \Sigma,\; p_j \in S\}
$$

be the level of inconsistency of $S$. Then,

$$
\mathrm{inc}(\Sigma) =
\max\{\mathrm{inc}(S) : S \text{ minimal inconsistent subset of } \Sigma\},
$$

where

$$
\mathrm{inc}(\Sigma) = \max\{a \mid \Sigma \vdash_{\pi} (\bot,a)\}
$$

and $\vdash_{\pi}$ is the standard possibilistic entailment defined by possibilistic resolution [8]. Moreover, it appears that if $(p_i, \pi_i, \gamma_i) \in \Sigma_{\mathrm{para}}$, we have

$$
\gamma_i =
\max\{\mathrm{inc}(C_k) : (p_i,a_i) \in \Sigma,\; p_i \in C_k,\; C_k \text{ minimal inconsistent subset of } \Sigma\}
$$

with

$$
\mathrm{inc}(C_k) = \min\{a_j \mid (p_j,a_j) \in \Sigma,\; p_j \in C_k\}.
$$

In fact we have the following result: the safely supported entailment from $\Sigma$ coincides with the possibilistic entailment from the consistent possibilistic logic base $\Sigma_{\mathrm{cons}}$ obtained from $\Sigma$ by deleting, in all minimal inconsistent subsets $S$ of $\Sigma$, the formulas with a certainty level equal to $\mathrm{inc}(S)$. Namely

$$
\Sigma_{\mathrm{cons}} =
\Sigma \setminus
\{(p_i,a_i) \mid (p_i,a_i) \in S,\; S \text{ minimal inconsistent subset of } \Sigma,\; a_i = \mathrm{inc}(S)\}.
$$

### 3.3 Lines for Further Research

The construction of $\Sigma_{\mathrm{comp}}$ and of $\Sigma_{\mathrm{para}}$ is reminiscent of the motivations of Belnap for introducing his well-known four-valued logic [1]. Belnap was considering several sources of information for which an atomic formula $p$ may be known to be true, known to be false, or unknown. This may be naturally encoded by one of the four triples $(p,1,0)$ ($p$ is held for true according to sources), $(p,0,1)$ ($p$ is held for false according to sources), $(p,1,1)$ (this is the paraconsistent case $p$ is true according to some sources and false according to others), and $(p,0,0)$ stands for the case where the truth status of $p$ is unknown for sources. In Belnap’s calculus $(p,1,1)$ and $(q,0,0)$ yields $(p \wedge q,0,1)$, which may appear strange at first glance. As pointed out in [7], this may be understood in the following way. On the one hand, we have both an argument in favor of $p$ true and an argument in favor of $p$ false. On the other hand we have no argument either in favor of $q$ true or in favor of $q$ false. This is enough to build an argument in favor of $p \wedge q$ false (from the argument in favor of $p$ false) and we cannot build any argument in favor of $p \wedge q$ true (since one has no argument in favor of $q$ true).

Yet, there already exists an extension of possibilistic logic inference that can be defined from $\Sigma_{\mathrm{para}}$ (and then extended to $\Sigma_{\mathrm{comp}}$). It is based on the following generalized resolution rule [9] where the paraconsistency of formulas can be propagated:

$$
(\neg p \vee q,\pi_1,\gamma_1),(p \vee r,\pi_2,\gamma_2)
\vdash
(q \vee r,\min(\pi_1,\pi_2),\max(\gamma_1,\gamma_2)).
$$

There is also another inference rule that holds in the logic of supporters [12], a logic closely related to possibilistic logic, which corresponds to the case where there are no reasons against in $\Sigma_{\mathrm{comp}}$, and where the scale $S$ is binary:

$$
(\neg p \vee q, P_1),(p \vee r, P_2)
\vdash
(q \vee r, P_1 \cup P_2).
$$

This rule was proposed moreover in an ATMS-like perspective, where two kinds of literals are distinguished, as in the following example:

**Example.** Given $\mathrm{Assumptions} = \{A, B, C\}$, and the knowledge base $\Sigma = \{(p,A), (q,B),(\neg q \vee p,C)\}$, $p$ in $\Sigma_{\mathrm{comp}}$ is then supported by two reasons, i.e., we have $(p,\{\{A\},\{B,C\}\},\emptyset)$.

Such inference rules may provide the starting point for reasoning directly in terms of arguments, and not only about arguments.

## 4 Concluding Remarks

This short paper is intended to show that the benefit of taking into account the certainty levels of formulas when reasoning under inconsistency may be still much higher than the one already obtained by applying standard possibilistic logic where only formulas strictly above the inconsistency level of the knowledge base are salvaged. Indeed when inconsistency takes place, it is often due to the presence of formulas in which we are not fully confident. Considering minimal inconsistent subsets provides a local view of where the conflicts take place, and then the deletion of the less certain formulas inside these subsets enables us to restore consistency while keeping more information than with the standard possibilistic logic view.

## References

1. Belnap, N.D.: A useful four-valued logic. In: Dunn, J.M., Epstein, G. (eds.) Modern Uses of Multiple-Valued Logic, pp. 7–37. D. Reidel, Dordrecht (1977)

2. Benferhat, S., Dubois, D., Prade, H.: Argumentative inference in uncertain and inconsistent knowledge base. In: Proceeding of the 9th Conference on Uncertainty in Artificial Intelligence, Washington, DC, 9–11 July, pp. 411–419. Morgan Kaufmann, San Mateo (1993)

3. Benferhat, S., Dubois, D., Prade, H.: Reasoning in inconsistent stratified knowledge bases. In: Proceeding of the 26 IEEE International Symposium on Multiple-Valued Logic (ISMVL 1996), Santiago de Compostela, Spain, pp. 184–189, 29–31 May 1996

4. Benferhat, S., Dubois, D., Prade, H.: Some syntactic approaches to the handling of inconsistent knowledge bases: a comparative study. Flat Case. Stud. Logica 58, 17–45 (1997)

5. Benferhat, S., Dubois, D., Prade, H.: An overview of inconsistency-tolerant inferences in prioritized knowledge bases. In: Dubois, D., Prade, H., Klement, E.P. (eds.) Fuzzy Sets, Logic and Reasoning about Knowledge, pp. 395–417. Kluwer Academic Publisher, Dordrecht (1999)

6. Besnard, P., Hunter, A. (eds.): Reasoning with Actual and Potential Contradictions: Handbook of Defeasible Reasoning and Uncertainty Management Systems, vol. 2. Kluwer, Dordrecht (1998)

7. Dubois, D.: On ignorance and contradiction considered as truth-values. Logic J. IGPL 16(2), 195–216 (2008)

8. Dubois, D., Lang, J., Prade, H.: Possibilistic logic. In: Gabbay, D.M., Hogger, C.J., Robinson, J.A., Nute, D. (eds.) Handbook of Logic in Artificial Intelligence and Logic Programming, vol. 3, pp. 439–513. Oxford Sci. Publ, Oxford Univ. Press, New York (1994)

9. Dubois, D., Lang, J., Prade, H.: Handling uncertainty, context, vague predicates, and partial inconsistency in possibilistic logic. In: Driankov, D., Ralescu, A.L., Eklund, P. (eds.) IJCAI-WS 1991. LNCS, vol. 833, pp. 45–55. Springer, Heidelberg (1994)

10. Hunter, A., Konieczny, S.: On the measure of conflicts: Shapley inconsistency values. Artif. Intell. 174(14), 1007–1026 (2010)

11. Jabbour, S., Ma, Y., Raddaoui, B., Sais, L.: Prime implicates based inconsistency characterization. In: Proceeding of the 21st European Conference on Artificial Intelligence (ECAI 2014), pp. 1037–1038. IOS Press, Prague (2014)

12. Lafage, C., Lang, J., Sabbadin, R.: A logic of supporters. In: Bouchon-Meunier, B., Yager, R.R., Zadeh, L.A. (eds.) Information, Uncertainty and Fusion, pp. 381–392. Kluwer, Dordrecht (1999)

13. Rescher, N., Manor, R.: On inference from inconsistent premises. Theor. Decis. 1, 179–219 (1970)