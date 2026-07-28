# Glucose Prognosis by Grammatical Evolution

J. Ignacio Hidalgo<sup>1(B)</sup>, J. Manuel Colmenar<sup>2</sup>, G. Kronberger<sup>3</sup>, and S. M. Winkler<sup>3</sup>

<sup>1</sup> Adaptive and Bioinspired Systems Group, Universidad Complutense de Madrid, 28040 Madrid, Spain  
hidalgo@dacya.ucm.es

<sup>2</sup> Rey Juan Carlos University, Tulipán s/n, 28933 Móstoles (Madrid), Spain

<sup>3</sup> Heuristic and Evolutionary Algorithms Laboratory, University of Applied Sciences Upper Austria, Softwarepark 11, 4232 Hagenberg, Austria

## Abstract

Patients suffering from Diabetes Mellitus illness need to control their levels of sugar by a restricted diet, a healthy life and in the cases of those patients that do not produce insulin (or with a severe defect on the action of the insulin they produce), by injecting synthetic insulin before and after the meals. The amount of insulin, namely bolus, to be injected is usually estimated based on the experience of the doctor and of the own patient. During the last years, several computational tools have been designed to suggest the boluses for each patient. Some of the successful approaches to solve this problem are based on obtaining a model of the glucose levels which is then applied to estimate the most appropriate dose of insulin. In this paper we describe some advances in the application of evolutionary computation to obtain those models. In particular, we extend some previous works with Grammatical Evolution, a branch of Genetic Programming. We present results for ten real patients on the prediction on several time horizons. We obtain reliable and individualized predictive models of the glucose regulatory system, eliminating restrictions such as linearity or limitation on the input parameters.

© Springer International Publishing AG 2018  
R. Moreno-Díaz et al. (Eds.): EUROCAST 2017, Part I, LNCS 10671, pp. 455–463, 2018.  
https://doi.org/10.1007/978-3-319-74718-7_55

## 1 Introduction

Diabetes Mellitus is a chronic disease characterized by an elevated blood glucose level due to a problem in the production or in the effect of insulin which, only in Spain, affects to more than five million people, which represents around 10% of the population in 2017. There are two main types of diabetes; Type 1 (DM1) and Type 2 (DM2). Patients with DM1 need to measure their glucose level many times a day, as well as injecting insulin subcutaneously. Patients with DM2 have to take measures of their glucose mainly in the meal times and, eventually, they have to inject themselves insulin. In clinical practice, blood sugar can be measured by continuous glucose monitors (CGM) and insulin is injected either manually or by continuous subcutaneous infusers or insulin pumps. The ideal solution for the patient is the development of an artificial pancreas (AP) [1].

AP is a solution, partially developed, where the glycemic control is completely autonomous. It requires a predictive model to estimate the future progress of blood glucose. With the information of the glucose level, a control algorithm would determine the dose of insulin to be delivered by the insulin pump, taking into account the variables and parameters included in the model. Current predictive models only consider measurements under controlled conditions of patients, which in most cases do not reflect the real-life or the patient. Glucose value prediction as a function of the insulin and food intakes is a difficult task that diabetics need to do everyday, since the AP is not accessible nowadays.

Taking glycemia, food intakes, levels of fatigue, stress, etc... as inputs, we can generate reliable predictive models of the levels of blood glucose, and implement bolus calculators for the daily management of the disease. Evolutionary Computation (EC) and Machine Learning (ML) had shown promising results in previous works [2]. In this work Grammatical Evolution techniques are applied for the prediction of glucose using the values measured by Continuous Glucose Monitoring (CGM) systems. We obtain more reliable and individualized predictive models of the glucose regulatory system, eliminating restrictions such as linearity or limitation on the input parameters. Our goal is to identify models (predictors) for the future glucose values after 30, 60, 90 and 120 min. The predictors were trained and tested using real data of 10 patients from a public hospital of Spain.

The rest of the paper is organized as follows. Section 2 describes the extraction of glucose models through Grammatical Evolution. Section 3 shows the experimental experience we have conducted and, finally, Sect. 4 draws the conclusions and the future work.

## 2 Glucose Prognosis of Diabetic Patients with Grammatical Evolution

Grammatical Evolution (GE) [3,4] is a form of Genetic Programming which represents the individuals using chromosomes instead of trees. The chromosomes are decoded through a grammar which produces the representation (phenotype) of a given individual. The use of chromosomes in GE allows the researcher the application of any of the available genetic operators that can be applied in Genetic Algorithms (GA) [5]. Moreover, given that the grammar is involved in the decodification, it is possible to introduce some information of the problem into the grammar to guide the optimization process to the best solutions.

In the case of modeling the glycemia of diabetic patients with GE, the phenotype of an individual is the model expression for prognosis. Hence, we need to create a grammar to guide the optimization process towards a model expression for prediction. Therefore, the grammar should consider that the prediction for a given time $t$ may depend on the previous values of glucose, carbohydrates ingestion and insulin injection, as we previously stated in [6]. Taking into account this principle, several approximations can be made for the design of the grammar. In this paper we have tested two different kinds of grammars: a directed grammar, (Fig. 1) and a symbolic regression grammar (Fig. 2). The figures show excerpts of the rules that have been defined in the grammars. Next, we give the most important details related to them.

The directed grammar, also used in [7] for a different approach based on models for each meal of the day, presents an initial symbol, `<func>`, which defines an expression based on glucose (`<exprgluc>`), plus some expression regarding carbohydrates (`<exprch>`), minus an expression of insulin (`<exprins>`). In other words, this expression fixes a pattern that will be followed in all the individuals. Hence, the search process is directed in that way. The expression of glucose denoted by `<exprgluc>` is defined by a recursive rule that may produce a complex formula using arithmetic operators (`<op>`), functions (`<preop>`) and constant values (`<cte>`) which, in our case, are generated through a base and an exponent built with integer values.

We have implemented the GE process in Java using the ABSys JECO library [8] and compilable phenotypes to speed up the evaluation of individuals [9]. This is the reason because elements like the `<preop>` operands appear under the Java syntax. The glucose expression works with a prediction window of up to 2 h. Therefore, the terminal values can be either the predicted value within the window, or the real data before this window. This behavior is obtained with the functions `predictedData` and `realData`, and the indexes that are defined for them: `<idxCurr2h>`, which corresponds to the time within current two hours, and `<idx2hOrMore>`, which corresponds to the time before the last two hours. Notice that the dataset provides data in a 5 min’ basis, therefore, $t - 24$ means 2 h ago.

As in the case of glucose, the expression for the carbohydrates may be recursively constructed, and takes into account the first previous intake since time $t$ of the first input variable, which is the carbohydrates, as stated by the terminal function `getPrevCarbo(t)`. This value is modified by a constant, and is translated into a curve, following a similar approach to the “Batemanization” explained in [7].

The expression for the insulin is analogous in the sense that it is built using similar rules. However, instead of taking the previous insulin value, the terminal symbol is `getVariable(2,t-<idx>)`, which returns the value of the second input variable, the insulin, in time `t-<idx>`. This behavior is defined in this way because the amount of insulin values could by high due to the basal insulin, which is usually injected though a pump on a 5 min basis. The rest of the rules of the grammar correspond to terminal and non-terminal symbols related to operators and auxiliary indexes such as `<op>`, `<preop>`, etc. We refer to this grammar as $GE_{dir}$ in the experimental results.

**Fig. 1. Excerpt of production rules for the directed grammar developed for the extraction of glycemic models.**

```text
# Model expression
<func > ::= <exprgluc > + <exprch > - <exprins >

# Glucose
<exprgluc > ::= (<exprgluc > <op > <exprgluc >) | <preop > (<exprgluc >)
| (<cte > <op> <exprgluc >) | predictedData(t-<idx >)
| realData(t-<idx2hOrMore >)

# CH
<exprch > ::= (<exprch > <op > <exprch >) | <preop > (<exprch >)
| (<cte > <op> <exprch >) | (getPrevCarbo(t) * <cte > * <curvedCH >)

# Insulin
<exprins > ::= (<exprins > <op> <exprins >)
| <preop > (<exprins >)
| (<cte > <op> <exprins >)
| getVariable(2,t-<idx >)

<op> ::= +| -|*|/
<preop > ::= Math.exp|Math.sin|Math.cos|Math.log
<cte > ::= <base >*Math.pow(10,< sign ><exponent >)
<base > ::= <dgtNoZero ><dgtNoZero >
<exponent > ::= 1|2|3|4|5|6|8|9
<sign > ::= +|-
<idx > ::= <dgtNoZero >|<dgtNoZero ><dgt >|<dgtNoZero ><dgt ><dgt >
<dgtNoZero > ::= 1|2|3|4|5|6|7|8|9
<dgt > ::= 0|1|2|3|4|5|6|7|8|9
```

**Fig. 2. Excerpt of production rules for the symbolic regression grammar developed for the extraction of glycemic models.**

```text
<func > ::= <gl> <op> <ch > <op> <ins > <op> <cte >
<gl> ::= <preop > (<gl >) | <gl> <op> <gl> | <vargl >
<ch> ::= <preop > (<ch >) | <ch> <op> <ch> | <cte > <op > (<ch >) | <varch >
<ins > ::= <preop > (<ins >) | <ins > <op> <ins > | <varins >
<op> ::= +| -|/|*
<vargl > ::= getVariable(2,k)|getVariable(3,k)|getVariable(4,k)|getVariable(5,
k)|getVariable(6,k)|getVariable(7,k)|getVariable(8,k)
<varch > ::= getVariable(9,k)|getVariable(10,k)|getVariable(11,k)|getVariable
(12,k)|getVariable(13,k)|getVariable(14,k)|getVariable(15,k)|getVariable
(16,k)|getVariable(17,k)|getVariable(18,k)|getVariable(19,k)|getVariable
(20,k)|getVariable(21,k)|getVariable(22,k)|getVariable(23,k)
<varins > ::= getVariable(24,k)|getVariable(25,k)|getVariable(26,k)|
getVariable(27,k)|getVariable(28,k)|getVariable(29,k)|getVariable(30,k)|
getVariable(31,k)|getVariable(32,k)|getVariable(33,k)|getVariable(34,k)|
getVariable(35,k)|getVariable(36,k)|getVariable(37,k)|getVariable(38,k)
<preop >::= Math.exp|Math.log
<cte >::= <c><c>.<c><c>
<c> ::= 0|1|2|3|4|5|6|7|8|9
```

In the case of the symbolic regression grammar displayed in Fig. 2 the approach is different. The `<func>` symbol does not direct the final expression for the phenotype. On the contrary, the `<op>` symbol provides different arithmetic operations, and the recursive definitions of `<gl>`, `<ch>` and `<ins>` allow the construction of complex expressions for each element. Moreover, the symbols `<vargl>`, `<varch>` and `<varins>` lead to different terminal elements for glucose, carbohydrates and insulin input variables.

In the experiments conducted with this grammar we have extended the dataset for each patient generating a total number of 38 input variables whose aim is to preprocess the input data. As seen in the grammar, input variables from 2 to 8 correspond to values calculated from the glucose; input variables from 9 to 23 correspond to values related to carbohydrates and input variables from 24 to 38 correspond to insulin values. Therefore, this grammar should behave in a more general way regarding the search process. We refer to this grammar as $GE_{SR}$ in the experimental results.

## 3 Experimental Results

We made a retrospective study on ten DM1 patients ($n = 10$) who were selected because they presented a good glucose control. Data from patients were acquired over multiple days using Medtronic insulin pump records. Log entries were stored in five-minute intervals containing the date and time, and depending on the event the blood glucose value, the amount of insulin (injected via pump), and/or the amount of carbohydrate intakes as estimated by the patients. The characterization of the patient is female (80%), with an average age 42.3 (±11.07), years of progress of disease 27.2 (±10.32), years with pump therapy 10 (±4.98), weight 64.78 (±13.31) kg, HbA1c average of 7.27% (±0.5%). The average number of days with data is 44.80 (±30.73).

In the experimentation we have compared our GE approach, using the two grammars described in the previous section ($GE_{SR}$ and $GE_{Dir}$) with two baseline predictors approaches. The first baseline, called Avg, considers the average glucose of the previous values in the past two hours. The second baseline, called Last, considers as prediction the last known value of the glucose. For each patient we have obtained four different models for the prediction of blood glucose concentration in 30, 60, 90 and 120 min using each one of the proposals. In order to perform a cross validation process, we have divided the data into 10 folds. Finally, we have run the algorithms 5 times on each fold to avoid the random bias.

As stated before, the GE algorithm use standard genetic operators. In particular, we apply the classical genetic algorithm with a population size of 200 individuals, which runs during 250 generations. We use single-point crossover with 0.75 probability and uniform mutation with a probability of 0.15. Regarding the parameters that are particular for GE we use 300 codons with 5 as maximum number of wrappings, and RMSE of the differences between the predicted and the expected glucose values as fitness function.

Table 1 shows the experimental results. Each row presents the averaged results for the 10 patients in terms of Clarke Error Grid Analysis (CEGA), a metric commonly used in Endocrinology to test the clinical significance of differences between predictions and real values of blood glucose [10]. CEGA uses a Cartesian diagram divided into five zones (A to E). Zone A and B are predictions with no danger for the patient, while zones C to E are potentially dangerous. Higher values of results in zones A and B are better, while lower numbers in zones C, D and E are preferred. Results in Table 1 are divided into four blocks, one for each time horizon.

We can observe that GE produced better prediction in all cases and we can conclude that $GE_{SR}$ reduces the number of predictions in dangerous zones. This is an interesting result, since the inclusion of knowledge in the grammar, as $GE_{Dir}$ does, is not beneficial for the quality of the prediction in this case. The reason is that, due to the structure of the grammar, the diversity of the solutions is lower with $GE_{Dir}$ than with $GE_{SR}$. We have noticed that in the decoding process the probability of having solutions with different phenotypes, i.e. different models, is lower with $GE_{Dir}$ since the starting point is always the same. Those results indicate that a further exploration of the grammars is needed, in combination with a pre-processing of the data.

**Table 1. Average of predictions (in percent) on independent test data. For each patients and prediction horizon, the best modeling results are highlighted. Added percentages could be higher than 100, since we are averaging values of 10 patients.**

| Horizon | $t + 30$ A+B | $t + 30$ C | $t + 30$ D | $t + 30$ E | $t + 60$ A+B | $t + 60$ C | $t + 60$ D | $t + 60$ E |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Alg |  |  |  |  |  |  |  |  |
| Last | 71.83 + 25.25 | 0.22 | 2.68 | 0.02 | 53.84 + 39.82 | 1.20 | 4.78 | 0.36 |
| Avg | 39.98 + 45.85 | 0.00 | 14.17 | 0.00 | 39.98 + 45.91 | 0.00 | 14.12 | 0.00 |
| $GE_{Dir}$ | **85.36 + 22.07** | 0.29 | 2.27 | 0.01 | **63.01 + 40.69** | 1.23 | 4.81 | 0.25 |
| $GE_{SR}$ | 80.66 + 17.53 | **0.37** | **1.44** | **0.01** | 58.64 + 35.81 | **1.27** | **4.06** | **0.21** |

| Horizon | $t + 90$ A+B | $t + 90$ C | $t + 90$ D | $t + 90$ E | $t + 120$ A+B | $t + 120$ C | $t + 120$ D | $t + 120$ E |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Alg |  |  |  |  |  |  |  |  |
| Last | 44.40 + 45.57 | 2.83 | 6.16 | 1.05 | 39.13 + 47.96 | 4.14 | 6.88 | 1.88 |
| Avg | 40.00 + 45.90 | 0.00 | 14.11 | 0.00 | 40.05 + 45.87 | 0.00 | 14.08 | 0.00 |
| $GE_{Dir}$ | **51.91 + 47.98** | **2.08** | **7.48** | **0.55** | **46.72 + 48.77** | 2.42 | 11.88 | 0.21 |
| $GE_{SR}$ | 47.59 + 43.37 | 2.27 | 6.15 | 0.62 | 41.74 + 47.01 | **2.17** | **8.19** | **0.89** |

Figure 3 shows the CEGA results for one of the patients with the best model on one of the cross validation folds with $GE_{SR}$. As we can observe, there is a small number of predictions in the dangerous zones. Similar results are obtained for all the patients and all the folds. Figure 4 presents a comparison of the predicted glucose values and real values for $GE_{SR}$. Four figures are presented, best patient and worst patient in the best and worst days.

**Fig. 3. Clarke error grid analysis results for 30 (up-left), 60 (up-right), 90 (down-left), and 120 (down-right) minutes for patient 1**

Detailed description: The figure contains four Clarke Error Grid scatter plots arranged in a 2×2 layout. Each subplot is titled “Clarke Error Grid”. The plots correspond to prediction horizons of 30 minutes (upper-left), 60 minutes (upper-right), 90 minutes (lower-left), and 120 minutes (lower-right). The horizontal axis and vertical axis range approximately from 0 to 400. The background is divided into colored Clarke error zones labeled A, B, C, D, and E, with green, yellow, orange, and red/pink regions marking the clinical zones. Red/orange scatter points labeled “Data” show pairs of predicted and reference glucose values. In the 30-minute plot, most points form a dense diagonal cloud through zone A and neighboring safe regions. In the 60-, 90-, and 120-minute plots, the point cloud becomes wider and more dispersed, with more points spreading into zones B, C, and D, while only a small number appear in the most dangerous zones.

**Fig. 4. A comparison of the predicted glucose values and real values for $GE_{SR}$. Four figures are presented, best patient best day (up-left), best patient worst day (up-right), and worst patient in the best day (down-left), and worst day (down-right).**

Detailed description: The figure contains four time-series line plots arranged in a 2×2 layout. Each subplot compares two curves, one for real glucose values and one for predicted glucose values, for $GE_{SR}$. The subplots represent the best patient best day (upper-left), best patient worst day (upper-right), worst patient best day (lower-left), and worst patient worst day (lower-right). The horizontal axes represent time samples during the day, and the vertical axes represent glucose level values. The blue and orange lines generally follow similar temporal patterns, with the predicted series tracking rises and drops in the real glucose series. The best-day plots show closer correspondence between the two lines, while the worst-day plots contain larger deviations, sharper peaks, and periods where the prediction does not fully follow the amplitude of the real glucose changes.

## 4 Conclusions and Future Work

In this paper we study the extraction of custom glucose models for diabetic patients by means of Grammatical Evolution (GE). The main contribution of this paper is the application of GE in the model extraction for long datasets from real patients. To this aim, we propose two different kinds of grammars: a directed grammar, which guides the optimization search using information from the problem (carbohydrates raise the glucose level and insulin drops it); and a general grammar similar to the ones used for symbolic regression. The comparison of those different grammars applied to ten real patients indicates that the premature inclusion of knowledge in the grammar is not always beneficial in terms of avoiding dangerous predictions. Therefore, we can conclude that, as expected, the structure of the grammar determines the diversity of the solutions and the probability of having solutions with different phenotypes. As future work, we will extend the experimentation considering a higher number of input variables like the exercise, the stress and some other physiological variables. Moreover, we will work on a different approach considering several objectives which will correspond to different quality measures for the models.

## References

1. El-Khatib, F.H., Russell, S.J., Nathan, D.M., Sutherlin, R.G., Damiano, E.R.: A bihormonal closed-loop artificial pancreas for type 1 diabetes. Sci Transl Med 2(27), 27ra27–27ra27 (2010)

2. Colmenar, J.M., Winkler, S.M., Kronberger, G., Maqueda, E., Botella, M., Hidalgo, J.I.: Predicting glycemia in diabetic patients by evolutionary computation and continuous glucose monitoring. In: Proceedings of the 2016 on Genetic and Evolutionary Computation Conference Companion, pp. 1393–1400. ACM (2016)

3. O’Neill, M., Ryan, C.: Grammatical evolution. IEEE Trans. Evol. Comput. 5(4), 349–358 (2001)

4. O’Neill, M., Ryan, C.: Grammatical Evolution: Evolutionary Automatic Programming in an Arbitrary Language. Kluwer Academic Publishers, Dordrecht (2003)

5. Eiben, A.E., Smith, J.E.: Introduction to Evolutionary Computing. Springer, Heidelberg (2003)

6. Hidalgo, J.I., Colmenar, J.M., Risco-Martin, J.L., Cuesta-Infante, A., Maqueda, E., Botella, M., Rubio, J.A.: Modeling glycemia in humans by means of grammatical evolution. Appl. Soft Comput. 20, 40–53 (2014). Hybrid intelligent methods for health technologies

7. Colmenar, J.M., Winkler, S.M., Kronberger, G., Maqueda, E., Botella, M., Hidalgo, J.I.: Predicting glycemia in diabetic patients by evolutionary computation and continuous glucose monitoring. In: Proceedings of the 2016 on Genetic and Evolutionary Computation Conference Companion, GECCO 2016 Companion, pp. 1393–1400. ACM, New York (2016)

8. Adaptive and Bioinspired Systems Group. ABSys JECO (Java Evolutionary COmputation) library (2015). https://github.com/ABSysGroup/jeco

9. Colmenar, J.M., Hidalgo, J.I., Lanchares, J., Garnica, O., Risco, J.-L., Contreras, I., Sánchez, A., Velasco, J.M.: Compilable phenotypes: speeding-up the evaluation of glucose models in grammatical evolution. In: Squillero, G., Burelli, P. (eds.) EvoApplications 2016. LNCS, vol. 9598, pp. 118–133. Springer, Cham (2016). https://doi.org/10.1007/978-3-319-31153-1_9

10. Clarke, W., Cox, D., Gonder-Frederick, L., Carter, W., Pohl, S.: Evaluating clinical accuracy of systems for self-monitoring of blood glucose. Diab. Care 10(5), 622–628 (1987)

```
The supplied parsed text was generally complete. Figure 3 and Figure 4 details were transcribed as natural-language descriptions because the plots are image-based and axis labels/legends are not fully legible at the provided resolution. Table 1 was reproduced from the parsed text/image; however, the table structure is visually ambiguous because the A+B columns contain values formatted as sums (e.g., “71.83 + 25.25”), while C, D, and E are separate zone columns. Bolded best values were preserved according to the visible table image/parsed text, though the clinical meaning of bolding for lower-is-better columns may appear inconsistent. Minor OCR artifacts such as broken hyphenation and accented characters were corrected where obvious.
```
