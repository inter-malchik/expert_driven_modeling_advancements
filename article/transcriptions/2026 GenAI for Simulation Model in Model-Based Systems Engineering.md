# GenAI for Simulation Model in Model-Based Systems Engineering

Lin Zhang*, Senior Member, IEEE, Yuteng Zhang, Dusit Niyato, Fellow, IEEE, Lei Ren, Senior Member, IEEE, Pengfei Gu, Zhen Chen, Graduate Student Member, IEEE, Yuanjun Laili, Member, IEEE, Wentong Cai, Senior Member, IEEE, Agostino Bruzzone

## Abstract
Generative AI (GenAI) has demonstrated remarkable capabilities in code generation, and its integration into complex product modeling and simulation code generation can significantly enhance the efficiency of the system design phase in Model-Based Systems Engineering (MBSE). In this study, we introduce a generative system design methodology framework for MBSE, offering a practical approach for the intelligent generation of simulation models for system physical properties. First, we employ inference techniques, generative models, and integrated modeling and simulation languages to construct simulation models for system physical properties based on product design documents. Subsequently, we fine-tune the language model used for simulation model generation on an existing library of simulation models and additional datasets generated through generative modeling. Finally, we introduce evaluation metrics for the generated simulation models for system physical properties. Our proposed approach to simulation model generation presents the innovative concept of scalable templates for simulation models. Using these templates, GenAI generates simulation models for system physical properties through code completion. The experimental results demonstrate that, for mainstream open-source Transformer-based models, the quality of the simulation model is significantly improved using the simulation model generation method proposed in this paper.

**Index Terms**—Generative AI, modeling & simulation, model-based systems engineering

## I. INTRODUCTION
THE increasing demand for research and development of complex products, such as spacecraft and complex mechanical equipment, has placed greater demands on system design and verification. Model-Based Systems Engineering (MBSE) [1] offers effective guidance for managing the complexity of such product development. The core principle of MBSE is to support all phases of a system’s lifecycle—from the initial design stage, through the operation and maintenance stage, to the final disposal stage—by a unified, formalized, and standardized model, thus enabling the transition from a document-based research and development (R&D) approach to a model-driven R&D approach.

The three core elements of MBSE are modeling languages, tools, and methodologies. Graphical system modeling languages, such as the Systems Modeling Language (SysML) [2], are widely used in academia and industry to support system engineering views and define various R&D elements in complex product development. However, mainstream MBSE methods, such as Harmony-SE [3] and Magicgrid [4], face challenges when using various graphical modeling languages, particularly in addressing system architectures and physical properties. The different characterization methods of system architectures and physical properties lead to poor model consistency. Although metamodel transformation [5] and co-simulation [6] provide promising solutions, both approaches require the collaborative use of multiple heterogeneous languages and tools. As a result, the current MBSE-oriented R&D approach increases the learning curve and inefficiency for system engineers. Furthermore, this multi-language and tool-integrated development approach restricts the application of intelligent methods to automate the generation of multi-level models throughout the system development process.

Unifying the modeling and simulation process is a key trend in the evolution of MBSE. A unified model representation can effectively address the challenges of integrating multi-stage and multi-domain models, thereby enhancing the efficiency of complex product research and development. Numerous institutions and scholars have explored integrated modeling and simulation languages, tools, and methodologies. For example, organizations like the International Council on Systems Engineering are advancing the adoption of the semantic modeling language SysML 2.0 [7], which aims to replace the current SysML. This new version enhances model expressiveness and consistency through a unified meta-modeling framework. The KARMA specification, a multi-architecture unified modeling language along with its associated toolchain system, proposed by Lu et al. [8], has been utilized to address the data integration challenges during the development of complex equipment.

In our previous research, we proposed an integrated modeling and simulation language based on discrete event system specification (DEVS) [9] extension development—X language [10], [11]. By extracting the structural representations of mainstream modeling languages, X language identifies the commonalities and interaction mechanisms across multi-domain models, providing a unified characterization approach for system architecture and physical properties. Additionally, X language defines two modeling forms—graphical and textual—consistent with meta-models. The aforementioned features of X language provide a strong foundation for intelligent generative design and modeling.

Generative artificial intelligence (GenAI) has enabled the integration of intelligence into system modeling and simulation within MBSE. GenAI, in its primary form as a large language model (LLM), is grounded in deep learning techniques and can perform various natural language processing tasks. With computing power advances, several ultra-large-scale models have emerged, such as GPT3 [12] and LLama2 [13]. With billions or even hundreds of billions of parameters, these models can handle larger data sizes and more complex tasks, and are widely used and integrated into software systems in several domains. AI models’ maturity and adaptability in coding scenarios have also grown significantly. GPT-4 [14] is an upgraded version of GPT-3. In addition to the basic complementary functions, GPT-4 is able to write code directly and help users debug, and its code has been greatly improved in both quality and length. Open-source code generation models in the same period include Code-Llama [15] by meta, WizardCoder [16] proposed by Microsoft, Code-Qwen [17] model introduced by Alibaba Group and CodeGeeX [18] proposed by Wisdom Spectrum AI, etc. The rapid development of LLM in terms of information extraction and code generation has made possible its application in industry [19], [20] and MBSE. The rich knowledge base and strong innovation capabilities of LLMs enable them to generate system code automatically, relationships between model elements, and related documentation, accelerating the system design and development process and increasing the productivity of engineers. Cámara, J. et al. [21] investigated ChatGPT’s current ability to perform modeling tasks and assist modelers, Tikayat Ray et al. [22] used an LLM to standardize a requirements hierarchy model, and Bader, E. et al. [23] implemented the task of generating UML component diagram elements by fine-tuning a large language model. However, most related GenAI applications focus primarily on the requirement and functional levels of MBSE, with limited research on the generation of simulation models for the system physical properties of products. The simulation model for the system physical properties of products represents one of the key models in MBSE. It is the foundation for achieving critical tasks such as life prediction, fault diagnosis, and performance evaluation.

Based on the previous research, this paper proposes an innovative generative system design methodology framework for MBSE, offering a practical direction for the intelligent generation of simulation models focused on the system physical properties of products. We employ inference techniques, generative models, and integrated modeling and simulation languages to construct simulation models for system physical properties based on product design documents. The scalable templates for simulation models proposed in this paper ensure the accuracy of the generated models. The evaluation framework proposed in this paper provides a practical approach for evaluating the quality of generated models. The main contributions of this paper are as follows:

1. This paper proposes a generative system design method for MBSE. The method utilizes BERT, Transformer-based models, and X language to extract information regarding the model’s composition, architecture, and behavior from product design documents, subsequently constructing simulation models for system physical properties.  
2. A specification and method for constructing scalable simulation model templates are proposed. Using these templates, Transformer-based models generate simulation models for system physical properties through code completion. This approach overcomes LLM’s limitations in processing long text inputs.  
3. A simulation model evaluation method is proposed for simulation models generated by Transformer-based models. The method introduces evaluation metrics beyond code accuracy tailored to the unique characteristics of simulation models and employs the entropy weighting method (EWM) to calculate weights, enhancing the evaluation’s objectivity.

The structure of this paper is organized as follows: Section II describes the construction specifications for X-language-based scalable templates and the method for constructing scalable templates at different model levels. Section III details three key methods: 1) the method using BERT, Transformer-based models, and scalable templates to generate simulation models for system physical properties based on the product design documents, and 2) the evaluation method for the generated simulation model. Section IV outlines the complete process of generating and evaluating the aircraft electrical system simulation model using the aforementioned simulation model generation methods.

The definitions of key terms involved in this paper are summarized in Table I to avoid ambiguity.

---

## II. X LANGUAGE SIMULATION MODEL TEMPLATE CONSTRUCTION

This section introduces the fundamental concepts of DEVS and presents X language, a formal modeling and simulation language based on DEVS. X language model will serve as the primary object generated by the method proposed in this paper. At the end of this section, we describe a scalable template of X language based on its syntax, which serves as a foundational prerequisite for the proposed method.

### A. Basic Concepts of DEVS
DEVS represents a formal modeling specification used to describe discrete event systems. DEVS models typically comprise the following core components:

**Atomic Model** defines the fundamental constituent units of a system, capturing its behavior and state. The atomic model in DEVS is defined by a seven-tuple constructor:

\[
AtomicDEVS = < S, ta, \delta_{int}, X, \delta_{ext}, Y, \lambda >
\tag{1}
\]

The elements of (1) are defined as follows:

1. **State set (S):** Describe all possible states of the model.  
2. **Input Event Set (X):** Define the types of external events the model can receive.  
3. **Output Event Set (Y):** Define the types of external events the model can generate.  
4. **Internal Transition Function (\(\delta_{int}\)):** Define the rules governing the transition of a model from one state to another, independent of external events.  
5. **External Transition Function (\(\delta_{ext}\)):** Defines the procedure for updating the model’s state upon receiving an external event.  
6. **Output Function (\(\lambda\)):** Defines the output behavior triggered by the model in a particular state.  
7. **Time Advance Function (\(ta\)):** Defines the duration for which the model stays in its current state before a state transition occurs.

**Coupled Model** integrates multiple atomic models or other coupled models to create more complex system structures. The coupled model in DEVS is defined by a four-tuple constructor:

\[
CoupledDEVS = < D, EIC, EOC, IC >
\tag{2}
\]

The elements of (2) are defined as follows:

1. **Set of Components (D):** Include multiple atomic models or other coupled models.  
2. **External Input Coupling (EIC):** Defines how external input events are passed to the submodel.  
3. **External Output Coupling (EOC):** Define how the output events of the submodel are passed to the outside of the system.  
4. **Internal Coupling (IC):** Define event transfer relationships between sub-models or between sub-models and external components.

The operational mechanism of the DEVS model is based on the event-driven principle and progresses in discrete time steps. Although the core design of the DEVS architecture primarily focuses on modeling discrete events, extensions of DEVS and some of its derivative frameworks support continuous-discrete hybrid systems by introducing mechanisms for “continuous state change” or by combining continuous state variables with discrete event processing [24]. Hybrid DEVS and similar extensions provide modeling capabilities for continuous-discrete hybrid systems, but current DEVS tools (e.g., CD++ and DEVSJAVA) offer limited support for hybrid modeling. Most of these tools remain focused on traditional discrete-event systems, and the hybrid modeling functionality is neither fully optimized nor standardized [25]. Some tools may necessitate users to develop additional modules for hybrid modeling or perform extensive custom configurations, thereby increasing development costs.

### B. Basic Concepts of X Language
The structure of the X language is illustrated in Fig. 1.

X language is a modeling and simulation language developed based on DEVS. It complements the description of continuous port connectivity and integrates both continuous and discrete event port connectivity to model and simulate the interaction between continuous and discrete behavior-dominated hybrid models. X language supports the integrated modeling of system architecture and physical characteristics, thereby enabling comprehensive modeling and simulation analysis in system designs [26], [27]. Additionally, X language supports dual-mode modeling (graphical and textual), with graphical representation enhancing interactivity, whereas textualization enables the integration of GenAI within X language.

The core classes of X language are presented in Table II. This section provides a detailed description of the functions of these classes.

**Couple class:** Couple class is a crucial component in X language, facilitating the integration of simulation analysis modeling and system architecture modeling. It corresponds to the coupled model in the DEVS architecture. The keyword **Part** in the attribute component and the keyword **Connection** in the connection component are specific to the couple class and used to describe the model’s composition and the connection relationship, respectively, and together constitute the architecture of the couple class model.

**Discrete class:** Discrete classes facilitate the modeling of discrete-event systems. The discrete class is indivisible, serving as the fundamental simulation unit within a discrete model. The keywords **State** and **Transform** in the state component are specific to the discrete class and used to represent transfer scenarios and conditions between different states in discrete events.

**Continuous class:** Continuous class is established to accomplish the modeling of continuous systems. The continuous class facilitates the construction of non-causal models, primarily based on equation solving. The keyword **Equation** in the equation component is specific to the continuous class and used to describe the behavior of the continuous class.

The continuous and discrete classes are atomic models in X language, corresponding to the atomic models in DEVS. The mapping between X language couple class, discrete class, and continuous class models and the corresponding elements in DEVS is illustrated in Fig. 2. X language couple class and atomic class models encompass all elements of the coupled and atomic models in DEVS, with some extensions beyond these elements.

### Table I. Term and Definition Table

| Term | Definition |
|---|---|
| simulation model | simulation model for system physical properties of products |
| header/attribute/connection | components of the couple class model |
| header/definition/state/equation | components of the atomic class model |
| Name/Import/Port/Part/Connection | keywords of X language couple class and the code governed by the keywords in X language couple class model |
| Name/Import/Port/Value/Parameter/State/Transform/Equation | keywords of X language atomic class and the code governed by the keywords in X language atomic class model |
| correctness similarity | a metric for evaluating the degree of deviation of an incorrect simulation model from an ideally correct model |
| simulation correctness | the degree of correctness of the simulation model, calculated by correctness similarity |
| degree of error | a metric to quantify the actual impact of errors on the simulation model code |
| model consistency | a metric to evaluate the consistency of the same elements across upper and lower models |
| scalable template | simulation model templates characterized by a flexible design pattern, allowing their length and content to be dynamically adjusted based on the number or attributes of the included elements |
| product design document | the natural language documentation that engineers use as a reference when designing and modeling a system |
| simulation model corpus | a corpus comprising content related to the design of simulation models |
| component-level model corpus | a corpus comprising content related to the design of component-level simulation models |

### Table II. Components of X Language Class

| Class | Component | keyword | definition |
|---|---|---|---|
| couple | header | the Name | name of the couple class model |
| couple | header | Import | the import of subsystem models (couple class or atomic class) |
| couple | attribute | Part | the submodule contained in the couple, i.e., instantiation of the subsystem models |
| couple | attribute | Port | the port of the couple class for connecting to external systems |
| couple | connection | Connection | the signal or data connection relationship between subsystems |
| discrete | header | Name | the name of the discrete class model |
| discrete | header | Import | the import of functions used in the model |
| discrete | definition | Port | the port of the discrete class for connecting to external systems |
| discrete | definition | Value | the model’s variables during the simulation process |
| discrete | definition | Parameter | the intrinsic property of the discrete class where its internal elements are constants |
| discrete | state | State | the transfer situation and transfer conditions between different states in a discrete event |
| discrete | state | Transform | the transformation conditions and transformation processes of discrete states |
| continuous | header | Name | the name of the continuous class model |
| continuous | header | Import | the import of functions used in the model |
| continuous | definition | Port | the port of the continuous class for connecting to external systems |
| continuous | definition | Value | the model’s variables during the simulation process |
| continuous | definition | Parameter | the intrinsic property of the continuous class where its internal elements are constants |
| continuous | equation | Equation | the dynamic behavior of the continuous class |

### C. X Language Class Template Construction
Complex product simulation models are characterized by high complexity and multi-scale. For such model code generation scenarios, generating accurate and consistent simulation code directly through GenAI is challenging. In this paper, the simulation model is constructed using scalable templates based on X language to address the issues above. X language scalable template deconstructs the syntax while preserving key elements and the overall model structure, thereby allowing model length and content to be dynamically adjusted based on the number and attributes of the included elements.

The core idea behind employing scalable templates for constructing simulation models is to modify the approach to code generation tasks. This study generates the simulation model through a modular code completion task. Compared to generating a complete simulation model, modular code completion can effectively address issues such as performance degradation, context loss, and output truncation caused by excessively long input contexts [29]. However, modular code completion can reduce consistency from module to module and system to subsystem. Therefore, when generating simulation models using scalable templates, additional algorithms are required to enhance the consistency of the models, which will be explained in detail in Section III.

There are several rules to follow when building a scalable template:

1. The top-down design principle should be followed when constructing the template. Specifically, model templates at the system level should be constructed prior to model templates at the component level.  
2. When constructing the template, the most effective description of the system-level structure of the simulation model and its contained elements should be extracted to minimize the amount of text generated by the LLM and improve accuracy.  
3. The coupling relationships between modules must be clarified when constructing the template. The coupling relationship of modules should be considered when using GenAI to generate simulation models.

Based on the characteristics of X language and the modeling specifications of the scalable templates discussed above, this paper develops scalable templates for X language couple class model, discrete class model, and continuous class model, as follows. A detailed description of the usage of these templates will be provided in Section III.

```text
couple <CoupleName>
import <AtomicName1>;
import <AtomicName2>;
...
part:
    <AtomicName1> <PartName1>;
    <AtomicName2> <PartName2>;
    ...
parameter:
    <DataType> <ParameterName1> = <Value1>;
    ...
port:
    <PortType> <CouplePortName1> = <InitialValue1>;
    ...
value:
    <DataType> <VariableName1> = <Value1>;
    ...
connection:
    connect(<PartName1>.<PortName1>, <PartName2>.<PortName2>);
end;

discrete <DiscreteName>
import <FunctionName1>;
...
parameter:
    <DataType> <ParameterName1>=<Value1>;
    ...
value:
    <DataType> <VariableName1>=<Value1>;
    ...
port:
    <PortType> <DiscretePortName1>=<InitialValue1>;
    ...
state:
initial state <InitialStateName>
    when entry() then
        statehold(<StateholdTime>);
    end;
    <StateAction>
end;

state <StateName1>
    when entry() then
        statehold(<StateholdTime>);
    end;
    <StateAction>
end;
...
end;

continuous <ContinuousName>
import <FunctionName>
...
parameter:
    <DataType> <ParameterName1>=<Value1>;
    ...
value:
    <DataType> <VariableName1>=<Value1>;
    ...
port:
    <PortType> <DiscretePortName1>=<InitialValue1>;
    ...
equation:
    <Equation>;
    ...
end;
```

---

## III. SIMULATION MODEL GENERATION METHOD BASED ON SCALABLE TEMPLATES AND TRANSFORMER-BASED MODELS

This section focuses on integrating BERT, Transformer-based models, and scalable templates to generate corresponding simulation models from product design documents. The overall technical implementation framework for the proposed method is illustrated in Fig. 3. Specifically, Section III-A provides a detailed introduction to the overall technical framework and specific steps of the simulation model generation process. Section III-B and Section III-C elaborate on the data processing and training methods of various language models employed in this workflow. Finally, Section III-D proposes a set of evaluation metrics to evaluate the performance of different language models in generating simulation code.

### A. Overall Technical Implementation Framework
This section elaborates on the three steps of the Simulation Model Generation Method Based on Scalable Templates and Transformer-based Models.

**Step 1: Identify the relevant corpus for target simulation models.** Product design document refers to the natural language documentation that engineers use as a reference when designing and modeling a system. However, such documents may contain irrelevant information, such as background knowledge or excessive details, which are unnecessary for constructing a simulation model. Therefore, extracting the relevant information from these documents for model construction is essential. We use BERT fine-tuned for Named Entity Recognition (NER) and single-sentence classification tasks to process the documents. If a sentence is not labeled in either task, it is considered redundant and excluded from the corpus. The remaining sentences are then added to the simulation model corpus. Subsequently, the product design documents are manually reviewed, and the corpus is adjusted as necessary.

**Step 2: Couple class model generation.** The couple class model must be constructed before the atomic class model in accordance with the principle of forward design through top-down model generation. Fine-tuned BERT for NER tags tokens, allowing us to identify system relationships within the simulation model corpus. This process ultimately enables the construction of the complete system composition by aggregating system relationships. The fine-tuned BERT model for single-sentence classification is capable of categorizing individual sentences. In Step 2, we employ it to determine whether the sentences in the model corpus describe the system’s connectivity relationships and add them to the connection corpus. Then, Transformer-based model inference is applied based on the connection corpus and the system composition to derive the connection relationships between subsystems. After defining the system composition and system connectivity relationships, the couple class model is constructed by populating the system composition into the keyword **import** of the couple class template and the system connection relations into the keyword **connection**.

**Step 3: Atomic class model generation.** The name of the atomic class model corresponds to the name of the subsystem, and the keyword **Port** of the atomic class model is derived by analyzing the keyword **Connection** of the couple class model. Additionally, the valuetype of the port is reasoned through the port names and the model description document. Due to the complexity and variable format of the keyword **State** of the discrete class model, the keywords **Value** and **State** are coupled and generated by the fine-tuned Transformer-based model. The fine-tuning method for this model is described in detail in Section III-C. The generation of the keyword **State** of the discrete class model should employ the Few-shot [30] method to construct the prompts, as illustrated in Table III. Similar to the discrete class, the value and equation parts of the continuous class, which are coupled, are generated uniformly by Transformer-based models. After completing the construction of the state and equation parts, it is necessary to verify these components for any undefined functions. If there is an undefined function, the function class model of X language needs to be generated according to the function name and the code of the atomic class model. The function class supports the procedural programming paradigm so that the function class simulation code can be generated using GenAI for code scenarios.

### Algorithm 1. Extract subsystem ports
**Input:** keyword “Connection”, subsystem name “PartName”  
**Output:** list of subsystem ports “PortList”  
**Note:** format of connect: `connect(part1.port1, part2.port2).`

```text
PortList ← ∅
for connect in Connection do
    if part1 == PartName then
        PortType ← ReasonPortType(part1, port1)
        PortList.Add("input" + PortType + port1)
    end if
    if part2 == PartName then
        PortType ← ReasonPortType(part2, port2)
        PortList.Add("output" + PortType + port2)
    end if
end for
```

### Table III. Method of Constructing the Prompts for Generating the Value and State Parts

| From | Classification | Specific meaning |
|---|---|---|
| user | BNF | Backus-Naur Form (BNF) of X language |
| user | state | Describe the parts that “state” contains and the text specification of “state”, then give a few examples of “state” |
| system | state response | The Transformer-based model’s understanding of the “state” specification |
| user | introduction | “Drawing on the textual descriptions of both the system model and the subsystem model, please develop the code for the keyword State of the discrete class subsystem model in accordance with the modeling specifications for the keyword State and the preceding code parts of the discrete class model. Note that only the code of the keyword State should be included in your output.” |
| user | couple text | Textual description of the couple class model to which the atomic class model to be generated belongs |
| user | discrete text | Textual description of the atomic class model to be generated |
| user | generated code | Generated code parts of the discrete class model, for example, keyword Name, keyword Parameter, keyword Port, etc. |
| user | note | Prompts added based on generic errors in Transformer-based model output results |

### B. NER-BERT Model Training
This section details the training method for the NER task fine-tuned BERT model used in Step 2 of Section III-A. The application of BERT [31] is a pre-trained deep learning model that uses a bidirectional Transformer encoder to understand words in context and generate word vector representations with rich semantic information. One of the notable advantages of the BERT model lies in its high flexibility, allowing it to effectively adapt to various downstream tasks through a range of fine-tuning strategies [32]. NER-BERT presented in this section is employed to analyze the simulation model corpus in the early stages of model construction, identifying module containment relationships, extracting relevant information, and omitting irrelevant content. The extracted containment relationship data informs the construction of both the system model and its corresponding subsystems.

The training method of NER-BERT is illustrated in Fig. 4. When providing BERT with an input dataset, the constructed data source must meet the following conditions:

1. It is the whole or part of the actual industrial model construction documentation;  
2. It contains a sufficient number of parent and subsystem containment relationships;  
3. It has substantial data without inclusion relationships as the data in question.

Upon completing the dataset preparation, fine-tuning training of the model can commence, enabling the BERT to perform the NER tasks outlined above. The input to BERT consists of the original word vectors for each word in the text, whereas the output comprises the vectors for each word or phrase after integrating the full semantic information of the text. As shown in the NER-BERT training section of Fig. 4, the fine-tuning process for the NER task connects a fully connected layer and a softmax layer to the original BERT output section. This addition enables the model to predict the tokens’ tags based on these vectors.

After training BERT for single-sentence classification scenarios in a similar manner, the system’s composition and connection relations can be extracted using both NER-BERT and the fine-tuned BERT for single-sentence classification. These relations can then be used to construct X language couple class model.

### C. Transformer-based Models Training
After constructing the couple class model, the next step is to generate the atomic class model, utilizing both the couple class model and the component-level model corpus. This section describes the training method for Transformer-based models, which is employed in Step 3 of Section III-A for the code generation of the behavioral component of the atomic class model. The models trained in this section are primarily employed to generate the behavioral simulation codes within the atomic class models of X language, specifically the keyword **State** in discrete class models and the keyword **Equation** in continuous class models.

#### 1) Data Set Preparation
The dataset used to fine-tune Transformer-based was derived from X language model repository. However, this library faces two primary challenges: the limited number of models available for training large models and the significant homogenization of models. This homogenization arises because models with different structures and expressions have distinct application ranges. The scarcity of instances for some less frequently used models diminishes the quality of training. To address these issues, this paper employs generative modeling to create additional datasets, supplementing X language model library and providing a solution for the challenge of training corpus scarcity in practical applications.

In this paper, we utilize GPT-3.5 for X language model generation. The prompts used to generate X language models consist of three components: **Introduction**, **Input**, and **Task**. The Introduction component encompasses prior knowledge of X language, including its modeling specifications and BNF, with several simulation models extracted from X language model library to facilitate Few-shot learning. The Input component represents the model description, which can be either a simple name or an extensive description, including, but not limited to, the model’s function, parameters, and domain constraints. The Task component serves as the task description, i.e., “Generate a couple/continuous/discrete simulation model of X language based on the model described in the aforementioned Input component.” Fig. 5 illustrates an example of generating an X language simulation model based on the prompts. The newly generated X language models, along with those in the original X language model library, constitute the training corpus. Subsequently, the contents of the corpus are converted into a dataset format suitable for training. The dataset format must include three components: **Instruction**, **Input** and **Output**.

Taking the discrete class model as an example, the mask training method can be employed to achieve code completion for the keyword **State** of the discrete class model; that is, the other components of the discrete model are utilized to predict its state and value parts. Specifically, the Instruction, Input and Output components are presented in Table IV. In addition to the Instruction texts listed in Table IV, the Instruction for different samples adopts diverse and near-synonymous expressions to enhance the richness of the data and assist the training model in better understanding and generalizing the semantics of this specific instruction. The Output is extracted from the model using a regular expression method.

### Table IV. Components of the Dataset

| Component | Content |
|---|---|
| Instruction | “This is a partially masked code for X language discrete class models. The parts represented by [MASK] may include value, state, and other keywords of discrete class models that have been concealed. Based on the available code, please speculate on the exact content in [MASK].” |
| Input | The value and state keywords of the discrete model are masked, with the masked parts replaced by “[MASK]”. |
| Output | The code for the value and state parts of the discrete class model. |

#### 2) Transformer-based Model Training
After the dataset’s preparation, the model’s training can commence. Specifically, let \(D\) represent the input simulation task description, \(C\) denotes the desired code result. Specifically, \(D\) represents the input in the dataset constructed above, whereas \(C\) represents the output in the same dataset. \(f(\cdot)\) signifies Transformer-based models. The output of Transformer-based models is:

\[
C' = f(D).
\tag{3}
\]

The optimization objective during training is to minimize the loss function \(L(C', C)\), or, more precisely, maximize the probability of the conditional language model, as illustrated in (4). The goal is to maximize the log probability of predicting each word \(y_t\) in the target sequence \(y\), given the input sequence \(x\) and the previous words \(y<t\). The optimization is performed by adjusting the model parameters \(\Phi\) to improve the model’s prediction accuracy for the next word in the sequence. This section will focus on the fine-tuning of the model to achieve this objective.

\[
\max_{\Phi} \sum_{(x,y)\in Z} \sum_{t=1}^{|y|} \log \left(P_{\Phi}(y_t \mid x, y<t)\right)
\tag{4}
\]

In this section, we choose CodeQwen1.5-7B [33] as the pre-trained model for fine-tuning. CodeQwen1.5 is a specialized code LLM built on the Qwen1.5 language model, and CodeQwen exhibits superior performance in long-term context understanding and generation compared to other open-source models of similar size. We utilizes the open-source project LLaMA Factory [34] as the fine-tuning tool. LLaMA Factory is an LLM training and fine-tuning platform that offers greater flexibility and ease of use compared to other fine-tuning methods or tools. LLaMA Factory supports multiple model architectures and simplifies the fine-tuning process. We choose the Low-Rank Adaptation (LoRA) [35] method to fine-tune the model. The LoRA method reduces the computational and memory requirements for training by decomposing the parameter matrices in a large model into two or more low-rank matrices and then updating only a portion of them. The principle of LoRA is shown in (5):

\[
h = W_0x + \Delta Wx = W_0x + BAx,
\]
\[
B \in R^{d\times r}, \ A \in R^{r\times d} \ \text{and} \ r \ll \min(d,k).
\tag{5}
\]

### D. Evaluation Method for Simulation Models Generated by Transformer-based Models
Mainstream code evaluation methods typically evaluate code based on metrics such as syntactic and semantic consistency (e.g., CodeBLEU [36]) and functional correctness (e.g., Pass@k [37]). However, simulation modeling of complex products introduces unique requirements and challenges for evaluation. In comparison to other code types, simulation model codes are characterized by their modular, hierarchical, and parametric structure. These characteristics cause the evaluation results of the above methods for evaluating simulation model codes to deviate from their actual quality. In contrast, the manual evaluation of simulation models, although capable of assigning reasonable scores based on the characteristics of the simulation model, ultimately depends on the scorer’s judgment in the absence of precise evaluation criteria. Therefore, this section introduces code evaluation metrics specific to X language simulation models tailored to their unique characteristics. These additions enhance the relevance of X language simulation model evaluations and provide specific metrics that guide manual evaluation. The evaluation metrics in this paper primarily evaluate X language simulation model based on **Degree of Error** and **Model Consistency** [38]. These two metrics are described in detail below.

**Degree of error:** In product design scenarios, Simulation models with a low degree of error tend to require less effort during subsequent modifications. Thus, in addition to evaluating the accuracy of the generated model, the Degree of Error index of any erroneous model also holds a reference value. The Degree of Error differs from the n-gram [39] approach. It evaluates the actual impact of errors on the model and assesses the ease of implementing modifications, and it often requires manual evaluation combined with a code checker and compiler.

**Model consistency:** Model consistency refers to the requirement that the representation of the same element in both the upper and lower models must remain consistent. The primary metrics of model consistency examined in this paper include:
1. Name consistency between the attribute part of the system model and the header part of the subsystem  
2. Port consistency between the connection part of the system model and the definition part of the subsystem  
3. Consistency between the functions invoked in the atomic class model and the definitions provided in the function class model

Based on the above two metrics, the simulation model evaluation method proposed in this paper is outlined as follows:

A complete set of simulation models includes a top-level model and its subsystems, with each subsystem potentially containing additional subsystems. The parent model is always a couple class model, whereas sub-models may be an atomic class model. The score of the parent model is derived from the simulation correctness of itself and its sub-models, specifically:

\[
Score = A_{parent}\cdot \sum_{i=1}^{n} C_{subsystem,i}\cdot A_{subsystem,i}.
\tag{6}
\]

In (6), \(A_{parent}\) signifies the simulation correctness of the parent model (couple class), \(C_{subsystem,i}\) denotes the weight of the \(i\)-th subsystem model (couple class or atomic class), and \(A_{subsystem,i}\) indicates the simulation correctness of the \(i\)-th subsystem model. For a set of simulation models undergoing evaluation, the final score is denoted as \(Score_{top}\), representing the score of the top-level model.

In this paper, the simulation correctness \(A_i\) is calculated as (7). X language simulation model is modular, allowing us to connect the ports of the model being tested to the correctly defined subsystem simulation models for test simulation. If the outputs of the model being tested are correct during the simulation, the model is considered fully correct.

\[
A_i =
\begin{cases}
1, & \text{Fully correct} \\
\epsilon \cdot P_i, & \text{Incorrect model simulation outputs}
\end{cases}
\tag{7}
\]

In (7), \(\epsilon\) represents penalty coefficient, a constant less than 1. \(P_i\) denotes the correctness similarity of the model. \(P_i\) is less than 1, with values closer to 1 indicating greater proximity to the correct model. The correctness similarity \(P_{ci}\) of the couple class model is calculated as (8).

\[
P_{ci} = k_h \cdot P_{header,i} + k_a \cdot P_{attribute,i} + k_c \cdot P_{connection,i}
\tag{8}
\]

\(k_h\), \(k_a\) and \(k_c\) denote the weights assigned to the correctness similarity for the attribute part and the connection part, respectively. \(P_{header,i}\), \(P_{attribute,i}\) and \(P_{connection,i}\) denote the correctness similarity for the header part, the attribute part and connection part, respectively. \(P_{attribute,i}\) and \(P_{connection,i}\) are calculated by comparing the product design document with the attribute part and the connection part of the couple class model:

\[
P_{attribute,i} = F1_{part,i}\cdot P_{port,i},
\tag{9}
\]

\[
P_{connection,i} = F1_{connection,i},
\tag{10}
\]

\(P_{port,i}\) denotes the correctness similarity for the keyword Port in the attribute part. \(F1\) indicates F1 score in machine learning of keywords Part and Connection. The correctness similarity \(P_i\) of the atomic class model is calculated as (11).

\[
P_i = k_h \cdot P_{header,i} + k_d \cdot P_{definition,i}
+ I(d)\cdot k_s \cdot P_{state,i} + I(c)\cdot k_e \cdot P_{equation,i}
\tag{11}
\]

\(k_h\), \(k_d\), \(k_s\), and \(k_e\) denote the weights assigned to the correctness similarity for the header, definition, state (for discrete class) and equation parts (for continuous class), respectively. \(P_{header,i}\), \(P_{definition,i}\), \(P_{state,i}\), and \(P_{equation,i}\) denote the correctness similarity for the header part, definition part, state part (for discrete class), and equation part (for continuous class), respectively. \(I(d)\) and \(I(c)\) represent indicator functions for the conditions “model is a discrete class model” and “model is a continuous class model” respectively, where the value is 1 when the condition is satisfied and 0 when it is not. \(P_{header,i}\), \(P_{port,i}\), \(P_{definition,i}\), \(P_{state,i}\), and \(P_{equation,i}\) are calculated as (12) and (13).

\[
P_{*,i} =
\begin{cases}
1, & \text{consistency} \\
\epsilon_* \cdot \frac{CE_{*,i}}{CE_{*,i}+IE_{*,i}}, & \text{inconsistency}
\end{cases}
,\quad *=header,port,definition
\tag{12}
\]

\[
P_{*,i} = \alpha_i^m \cdot \beta_i^n,\quad *=state,equation
\tag{13}
\]

\(\epsilon_h\) and \(\epsilon_d\) represent penalty coefficient. \(CE\) and \(IE\) denote elements that are consistent and inconsistent with other models, respectively. \(\alpha_i\) and \(\beta_i\) denote the attenuation of “correctness similarity” in the \(i\)-th model due to syntax errors and simulation logic errors, respectively, a constant less than 1. \(m\) and \(n\) denote the numbers of syntax errors and simulation logic errors in the model, respectively. Syntax detectors and compilers can typically detect syntax errors, whereas simulation logic errors must be identified through manual inspection. Consequently, from the perspective of modification effort, simulation logic errors are often more severe, necessitating that \(\beta_i\) be smaller than \(\alpha_i\). Considering that the Degree of Error in the state section is related to its length, the formulas for \(\alpha_i\) and \(\beta_i\) are provided to ensure that \(P_{state,i}\) is not influenced by the length of the keyword State:

\[
\log \alpha_i = \frac{len_c}{len_i}\cdot \log \alpha_c,\quad
\log \beta_i = \frac{len_c}{len_i}\cdot \log \beta_c.
\tag{14}
\]

\(len_c\) and \(len_i\) denote the standard keyword State length and the keyword State length of the \(i\)-th model, respectively. \(\alpha_c\) and \(\beta_c\) represent the standard attenuation coefficients. For the above evaluation metrics, \(P_{attribute,i}\), \(P_{header,i}\), and \(P_{definition,i}\) focus on the consistency of the model, whereas \(P_{state,i}\) and \(P_{equation,i}\) emphasize the Degree of Error in keyword State (for discrete class) and equation part (for continuous class) of the model.

The penalty coefficients in the above equation are determined based on the actual importance of each component of the model. The weights assigned to each model and to each component within the model are calculated using EWM. EWM is a multi-criteria decision-making approach that leverages the concept of information entropy to determine the weight of each criterion in an evaluation. This method assigns weights based on the variability of the data associated with each criterion; criteria with higher variability are assigned greater weights as they contribute more informative value to the evaluation [40].

This set of evaluation metrics considers the modularity of the simulation model and the characteristics of the design and development process. It will be employed in Section IV to evaluate the quality of the generated simulation model.

---

## IV. SIMULATION MODEL GENERATION FOR AIRCRAFT ELECTRICAL SYSTEM

This section generates and evaluates a set of simulation models for the aircraft electrical system based on the simulation model generation method outlined in Section III. Section IV-A details the experimental preparation required for generating the aircraft electrical system. Section IV-B demonstrates the efficacy of the fine-tuned NER-BERT model in extracting relevant information from the aircraft electrical system documentation. Section IV-C generates multiple sets of simulation models using different Transformer-based models. Section IV-D evaluates the results against the model evaluation metrics presented in Section III-D.

### A. Preparation of Experiments
The preparation for the experiment will be presented in terms of case introduction, data preparation, and experimental equipment.

**Case introduction:** The aircraft electrical system examines the variations in electrical current, voltage, and power utilized during the aircraft’s actual flight. The aircraft electrical system comprises six components: power supply, flight scenario control module, control bus, radar, rudder, and thrust module. The relationship between the subsystems is illustrated in Fig. 6. The functions of these six subsystems are presented in Table V.

### Table V. The Functions of Subsystems

| Name | Function |
|---|---|
| power supply | This subsystem provides a stable operating voltage of 28.5V to each module throughout the entire duration of operation. |
| flight scenario control module | This subsystem is responsible for designing flight trajectories that enable the aircraft to adhere to a predefined path. |
| control bus | This subsystem receives commands, parses them, and subsequently transmits the commands to the power equipment to adjust its power consumption. |
| radar | This subsystem detects the position of a target. |
| rudder | This subsystem adjusts power according to received commands. |
| thrust | This subsystem specializes in generating thrust to propel the aircraft forward. |

**Data preparation:** In this paper, we select relevant papers on the aircraft electrical system [41], [42] and the model-building instructions document compiled by our team for constructing the aircraft’s electrical system as the data preparation for this experiment.

**Experimental equipment:** For the hardware configuration, the experimental computing platform includes an A100 80GB GPU, an i9-13900K processor, and 256GB of RAM. The software environment comprises Ubuntu 20.04 LTS as the operating system, PyTorch 2.4 as the deep learning framework, and CUDA 12.4 with cuDNN 9.1 for GPU acceleration.

### B. Couple Class Simulation Model Generation
This section utilizes the NER-BERT model fine-tuned in Section III-B to extract the system composition of the aircraft electrical system. The process is illustrated in Fig. 7.

The tagging results of NER-BERT are compared with manual annotations, and if the tags for each token in a sentence are correct, NER-BERT is deemed to have correctly tagged the entire sentence. Ultimately, the accuracy of NER-BERT is 81.3%. Although this accuracy rate is relatively modest, we observe that the causes of incorrect token tags in NER-BERT can generally be categorized into two main groups:

1. Errors in individual token tags within longer word sequences, i.e., incorrect boundaries of the tags.  
2. Misclassification of irrelevant tokens, which do not belong to any entity, as entity tags.

Specifically, the precision of entity tags for a given token is 95.06%, whereas recall achieves 100%. In addition to the aircraft electrical system, we also performed experiments on the electric vehicle system, railroad crossing system, and aircraft take-off system. The results of NER-BERT’s entity tagging for these product design documents are presented in Table VI. In the experiments, the recall rates for entity tags reached 100%. This indicates that no system composition information is omitted, allowing engineers to adjust only the NER-BERT tagged content to derive the system composition, thus eliminating the need to read the entire product design document.

### Table VI. The Results of NER-BERT’s Entity Tagging

| Model Name | Sent Acc | Token Acc | Ent Prec | Ent Rec |
|---|---:|---:|---:|---:|
| aircraft electrical system | 0.813 | 0.988 | 0.951 | 1 |
| electric vehicle system | 0.882 | 0.992 | 0.960 | 1 |
| railroad crossing system | 0.846 | 0.982 | 0.906 | 1 |
| aircraft take-off system | 0.961 | 0.996 | 0.971 | 1 |

Notes:  
- Sent Acc: Sentence Accuracy  
- Token Acc: Token Accuracy  
- Ent Prec: Precision of Entity Tags  
- Ent Rec: Recall of Entity Tags

### C. Atomic Class Simulation Model Generation
The atomic model generation method is presented in Step 3 of the Simulation Model Generation Method Based on Scalable Templates and Transformer-based Models in Section III-A. Take the subsystem AutoPilot as an example. The AutoPilot subsystem performs the functions of the rudder module. Based on the connection part of the couple class model, AutoPilot can retrieve the relevant port connection relationships and populate the keyword Port of AutoPilot with this information. The prompts are formulated based on the structure outlined in Table III and serve as inputs to the Transformer-based models trained in Section III-C to generate the behavioral code of the atomic class (state for discrete class, equation for continuous class) and its corresponding keyword Value. The comparison of generated model and manual written model is presented in Fig. 8. Although there are differences in expression between the generated and manually written models, the generated model maintains the same semantics and adheres to X language syntax specifications.

After completing the generation of all atomic models, both the generated couple class models and atomic models are imported into X language development tool, XLab. XLab can transform the generated text code into graphical models. In the aircraft electrical system model, each subsystem’s graphical or textual composition, definitions, connectivity relationships, and internal logic are shown in Fig. 9. The mapping relationship between the final model and the various modules of the aircraft electrical system is outlined as follows: power supply - Battery, flight scenario control module - Control, control bus - BallisticSceneControl, radar - Radar, rudder - AutoPilot, thrust - Thrust. So far, we have successfully generated a complete simulation model of the aircraft electrical system using the Simulation Model Generation Method Based on Scalable Templates and Transformer-based Models proposed in this paper.

### D. Simulation Model Code Evaluation
This section evaluates the impact of the aforementioned model generation methods on generating simulation models using various Transformer-based models based on the evaluation metrics outlined in Section III-D.

We selected three open-source models for the code generation scenario (CodeQwen1.5-7b, CodeGemma-7b [43], and DeepSeek-Coder-6.7b [44]) and evaluated the quality of the aircraft electrical system models generated with and without the use of the simulation model generation method proposed in this paper. Additionally, we selected two high-performance proprietary models (Claude-3.5-Sonnet, GPT-4o) and evaluated the aircraft electrical system models they generated directly. For the aircraft electrical system, set the values of \(\epsilon\), \(\epsilon_{header}\), \(\epsilon_{port}\), and \(\epsilon_{definition}\) in the evaluation metrics to 0.8, 0.6, 0.6, and 0.6, respectively. Set the values of \(\alpha_c\), \(\beta_c\), and \(len_c\) to 0.2, 0.1, and 1 state, respectively. We generated 20 sets of aircraft electrical system models using each model, both with and without the proposed method, and then manually evaluated them based on the evaluation metrics described above. We obtained several atomic class models and one couple class model using each method. We calculated the scores of atomic models as 8 and calculated their final scores as (6). We employed EWM to calculate the weights of the models and components, accentuating the gap in the final scores. The average scores of the 20 sets from different models and methods were compared, and the scores of atomic models and the final scores are presented in Table VII. The meanings of Meth.a and Meth.b in Table VII are as follows:

- **Meth.a)** The simulation model generation method proposed in this paper.  
- **Meth.b)** Generate the simulation model directly using Transformer-based models. The prompts include X language BNF, X language model examples, a description of the model to be generated, and a description of the parent system model.

### Table VII. Evaluation Results of Simulation Models Generated Using Different Methods

| Model name | CodeGemma Meth.a | CodeGemma Meth.b | CodeQwen Meth.a | CodeQwen Meth.b | DeepSeek-Coder Meth.a | DeepSeek-Coder Meth.b | Claude-3.5-Sonnic | GPT-4o |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AutoPilot | 1 | 0.234 | 1 | 0.265 | 1 | 0.297 | 0.402 | 0.379 |
| BallisticSceneControl | 0.689 | 0 | 0.779 | 0.024 | 1 | 0.016 | 0.135 | 0.168 |
| Battery | 1 | 0.474 | 1 | 0.435 | 1 | 0.457 | 0.485 | 0.51 |
| ControlBusModule | 0.667 | 0 | 0.679 | 0 | 0.697 | 0 | 0 | 0.044 |
| Thrust | 1 | 0.125 | 1 | 0.109 | 1 | 0.116 | 0.316 | 0.241 |
| Oper | 0.823 | 0.263 | 0.828 | 0.255 | 0.881 | 0.260 | 0.257 | 0.266 |
| Radar | 0.494 | 0.038 | 0.494 | 0.008 | 0.518 | 0.023 | 0.194 | 0.158 |
| **Final score** | **0.810** | 0.161 | **0.825** | 0.156 | **0.870** | 0.165 | 0.241 | 0.242 |

As shown in Table VII, the simulation model generation method proposed in this paper improves the quality of the simulation models generated by mainstream Transformer-based models, such as CodeGemma, CodeQwen, and DeepSeek Coder. The quality of the generated simulation model surpasses that of directly using Claude 3.5, Sonnic, and GPT-4. This suggests a practical direction for generating simulation models focused on the physical properties of systems.

Additionally, we observed a phenomenon during our experiments: Transformer-based models perform poorly on the simple model Radar, which we believe is due to its a priori knowledge of radar. Instead of assisting in generating the simulation model, this prior knowledge hinders the process, which contradicts our expectations. This is most likely since the a priori knowledge related to radar in the Transformer-based models differs from the description of radar in the model design document. The Transformer-based models utilize their a priori knowledge when generating the simulation model, leading to a deviation between the final simulation model and the model design document. After renaming the Radar module, the quality of the simulation code for this module improved. This suggests that Transformer-based models’ generalization ability may hinder the generation of high-quality simulation models when the simulation model is well documented. Determining how to help Transformer-based models better balance the application of prior knowledge with task requirements when generating content based on existing knowledge will be one of the future research directions for the application of GenAI in MBSE.

---

## V. CONCLUSION
This paper proposes a method for generating simulation models using scalable templates and Transformer-based models, offering a practical approach for the intelligent generation of simulation models of system physical properties in product systems. The main conclusions of this study are as follows:

1. The token recognition in product design document sentences by the NER-BERT model trained in this study effectively filters redundant information and provides a reliable reference for designing the system composition.  
2. The simulation model evaluation method proposed in this study integrates the unique characteristics of simulation models and introduces evaluation metrics beyond code accuracy. This approach enables a quantitative evaluation of simulation codes.  
3. The method for generating simulation models using scalable templates and Transformer-based models generates simulation models for system physical properties through modular code completion, overcoming the limitations of LLM in handling long text inputs. The quality of simulation models generated with this method is improved compared to using Transformer-based models directly.

Although the Transformer-based models and scalable template-based simulation model generation methods proposed in this paper significantly enhance the simulation model generation code, there remains room for further improvement. In the future, more efforts will focus on expanding the size and diversity of the Transformer-based models training dataset and exploring the application of GenAI across other stages of the MBSE lifecycle.

---

## REFERENCES

[1] S. Friedenthal, R. Griego, and M. Sampson, “Incose model based systems engineering (mbse) initiative,” in *INCOSE 2007 symposium*, vol. 11. sn, 2007.  

[2] S. Friedenthal, A. Moore, and R. Steiner, “Omg systems modeling language (omg sysml) tutorial,” in *INCOSE Intl. Symp*, vol. 9. Citeseer, 2006, pp. 65–67.  

[3] B. Douglass, “The Harmony Process. I-Logix white paper, I-Logix,” Inc.: Burlington, MA, USA, 2005.  

[4] J. A. Estefan et al., “Survey of model-based systems engineering (mbse) methodologies,” *Incose MBSE Focus Group*, vol. 25, no. 8, pp. 1–12, 2007.  

[5] X. Li and J. Liu, “A method of sys ml-based visual transformation of system design-simulation models,” *Journal of Computer-Aided Design & Computer Graphics*, vol. 28, no. 11, pp. 1973–1981, 2016.  

[6] L. Zhao, J. Ye, H. Qi, G. Wei, and Z. Yong, “Simulation of civil aircraft takeoff scenario based on mbse,” *Journal of System Simulation*, vol. 33, no. 10, pp. 2499–2510, 2021.  

[7] J. Gray and B. Rumpe, “Reflections on the standardization of sysml 2,” pp. 287–289, 2021.  

[8] J. Lu, G. Wang, J. Ma, D. Kiritsis, H. Zhang, and M. Törngren, “General modeling language to support model-based systems engineering formalisms (part 1),” in *INCOSE international symposium*, vol. 30, no. 1. Wiley Online Library, 2020, pp. 323–338.  

[9] B. P. Zeigler, H. Praehofer, and T. G. Kim, *Theory of modeling and simulation*. San Diego: Academic press, 2000.  

[10] L. Zhang, F. Ye, Y. Laili, K. Xie, P. Gu, X. Wang, C. Zhao, X. Zhang, and M. Chen, “X language: an integrated intelligent modeling and simulation language for complex products,” in *2021 Annual Modeling and Simulation Conference (ANNSIM)*. IEEE, 2021, pp. 1–11.  

[11] L. Zhang, F. Ye, K. Xie, P. Gu, X. Wang, Y. Laili, C. Zhao, X. Zhang, M. Chen, T. Lin et al., “An integrated intelligent modeling and simulation language for model-based systems engineering,” *Journal of Industrial Information Integration*, vol. 28, p. 100347, 2022.  

[12] T. B. Brown, “Language models are few-shot learners,” *arXiv preprint arXiv:2005.14165*, 2020.  

[13] H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale et al., “Llama 2: Open foundation and fine-tuned chat models,” *arXiv preprint arXiv:2307.09288*, 2023.  

[14] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat et al., “Gpt-4 technical report,” *arXiv preprint arXiv:2303.08774*, 2023.  

[15] B. Roziere, J. Gehring, F. Gloeckle, S. Sootla, I. Gat, X. E. Tan, Y. Adi, J. Liu, R. Sauvestre, T. Remez et al., “Code llama: Open foundation models for code,” *arXiv preprint arXiv:2308.12950*, 2023.  

[16] Z. Luo, C. Xu, P. Zhao, Q. Sun, X. Geng, W. Hu, C. Tao, J. Ma, Q. Lin, and D. Jiang, “Wizardcoder: Empowering code large language models with evol-instruct,” *arXiv preprint arXiv:2306.08568*, 2023.  

[17] J. Bai, S. Bai, Y. Chu, Z. Cui, K. Dang, X. Deng, Y. Fan, W. Ge, Y. Han, F. Huang et al., “Qwen technical report,” *arXiv preprint arXiv:2309.16609*, 2023.  

[18] Q. Zheng, X. Xia, X. Zou, Y. Dong, S. Wang, Y. Xue, Z. Wang, L. Shen, A. Wang, Y. Li et al., “Codegeex: A pre-trained model for code generation with multilingual evaluations on humaneval-x,” *arXiv preprint arXiv:2303.17568*, 2023.  

[19] L. Ren, H. Wang, Y. Tang, and C. Yang, “Aigc for industrial time series: From deep generative models to large generative models,” *arXiv preprint arXiv:2407.11480*, 2024.  

[20] R. Zhang, H. Du, D. Niyato, J. Kang, Z. Xiong, A. Jamalipour, P. Zhang, and D. I. Kim, “Generative ai for space-air-ground integrated networks,” *IEEE Wireless Communications*, 2024.  

[21] J. Cámara, J. Troya, L. Burgueño, and A. Vallecillo, “On the assessment of generative ai in modeling tasks: an experience report with chatgpt and uml,” *Software and Systems Modeling*, vol. 22, no. 3, pp. 781–793, 2023.  

[22] A. Tikayat Ray, B. F. Cole, O. J. Pinon Fischer, A. P. Bhat, R. T. White, and D. N. Mavris, “Agile methodology for the standardization of engineering requirements using large language models,” *Systems*, vol. 11, no. 7, p. 352, 2023.  

[23] E. Bader, D. Vereno, and C. Neureiter, “Facilitating user-centric model-based systems engineering using generative ai.” in *MODELSWARD*, 2024, pp. 371–377.  

[24] T.-G. Kim and S. Y. Lim, “Hybrid modeling and simulation methodology based on devs formalism,” in *SCSC’2001*. ACM, 2001.  

[25] G. Wainer, “Cd++: a toolkit to develop devs models,” *Software: Practice and Experience*, vol. 32, no. 13, pp. 1261–1306, 2002.  

[26] Y. Zhang, P. Gu, Z. Chen, and L. Zhang, “A method and implementation of automatic requirement tracking and verification for complex products based on x language,” in *China Intelligent Networked Things Conference*. Springer, 2022, pp. 443–455.  

[27] P. Gu, L. Zhang, Z. Chen, and J. Ye, “Collaborative design and simulation integrated method of civil aircraft take-off scenarios based on x language,” *Journal of System Simulation*, vol. 34, no. 5, pp. 929–943, 2022.  

[28] K. Xie, L. Zhang, Y. Laili, and X. Wang, “Xdevs: A hybrid system modeling framework,” *International Journal of Modeling, Simulation, and Scientific Computing*, vol. 13, no. 02, p. 2243001, 2022.  

[29] A. Vaswani, “Attention is all you need,” *Advances in Neural Information Processing Systems*, 2017.  

[30] O. Vinyals, C. Blundell, T. Lillicrap, D. Wierstra et al., “Matching networks for one shot learning,” *Advances in neural information processing systems*, vol. 29, 2016.  

[31] J. Lee and K. Toutanova, “Pre-training of deep bidirectional transformers for language understanding,” *arXiv preprint arXiv:1810.04805*, vol. 3, no. 8, 2018.  

[32] Y. Liu, “Fine-tune bert for extractive summarization,” *arXiv preprint arXiv:1903.10318*, 2019.  

[33] Q. Team, “Code with codeqwen1.5,” April 2024. [Online]. Available: https://qwenlm.github.io/blog/codeqwen1.5/  

[34] Y. Zheng, R. Zhang, J. Zhang, Y. Ye, and Z. Luo, “Llamafactory: Unified efficient fine-tuning of 100+ language models,” *arXiv preprint arXiv:2403.13372*, 2024.  

[35] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen, “Lora: Low-rank adaptation of large language models,” *arXiv preprint arXiv:2106.09685*, 2021.  

[36] S. Ren, D. Guo, S. Lu, L. Zhou, S. Liu, D. Tang, N. Sundaresan, M. Zhou, A. Blanco, and S. Ma, “Codebleu: a method for automatic evaluation of code synthesis,” *arXiv preprint arXiv:2009.10297*, 2020.  

[37] C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, and P. J. Liu, “Exploring the limits of transfer learning with a unified text-to-text transformer,” *Journal of machine learning research*, vol. 21, no. 140, pp. 1–67, 2020.  

[38] O. Iordache, *Modeling multi-level systems*. Springer Science & Business Media, 2011.  

[39] M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. D. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman et al., “Evaluating large language models trained on code,” *arXiv preprint arXiv:2107.03374*, 2021.  

[40] Y. Zhu, D. Tian, and F. Yan, “Effectiveness of entropy weight method in decision-making,” *Mathematical Problems in Engineering*, vol. 2020, no. 1, p. 3564835, 2020.  

[41] P. Gu, Y. Zhang, Z. Chen, C. Zhao, K. Xie, Z. Wu, and L. Zhang, “X-rmtv: An integrated approach for requirement modeling, traceability management, and verification in mbse,” *Systems*, vol. 12, no. 10, p. 443, 2024.  

[42] P. Gu, Y. Li, Z. Wu, Z. Chen, K. Xie, and L. Zhang, “Research on integrated modeling and simulation method of missile electrical system based on x language,” in *China Intelligent Networked Things Conference*. Springer, 2024, pp. 219–230.  

[43] C. Team, H. Zhao, J. Hui, J. Howland, N. Nguyen, S. Zuo, A. Hu, C. A. Choquette-Choo, J. Shen, J. Kelley et al., “Codegemma: Open code models based on gemma,” *arXiv preprint arXiv:2406.11409*, 2024.  

[44] D. Guo, Q. Zhu, D. Yang, Z. Xie, K. Dong, W. Zhang, G. Chen, X. Bi, Y. Wu, Y. Li et al., “Deepseek-coder: When the large language model meets programming–the rise of code intelligence,” *arXiv preprint arXiv:2401.14196*, 2024.  