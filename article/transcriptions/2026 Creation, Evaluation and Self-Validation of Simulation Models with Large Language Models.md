```markdown
# Creation, Evaluation and Self-Validation of Simulation Models with Large Language Models

**Tobias Möltner, Peter Manzl, Michael Pieber, Johannes Gerstmayr**  
Department of Mechatronics, University of Innsbruck, Technikerstraße 13, Innsbruck, 6020, Austria.  

*Corresponding author(s). E-mail(s): johannes.gerstmayr@uibk.ac.at;  
Contributing authors: tobias.moeltner@uibk.ac.at; peter.manzl@uibk.ac.at; michael.pieber@uibk.ac.at;

---

### Abstract
Engineering tasks are significantly underrepresented in current large language model (LLM) datasets and research, despite their complexity and practical importance. These tasks often demand a deep mathematical understanding and involve a combination of textual descriptions, visual representations, and numerical data. Moreover, engineering frequently relies on accepted approximations and models rather than exact values. Therefore, the present paper advances the integration of LLMs into mechanical engineering by introducing a comprehensive framework for automated simulation model generation and validation. The framework is designed as a benchmark and focuses on mechanical engineering problems in dynamics in particular on multibody dynamics simulation models in Python. It allows for the creation of a large number of test cases due to its use of parametrized models with ground truth solutions, allowing evaluation for executability and correctness. Lastly, LLM-agents are employed to generate simulation models and perform self-evaluation through a predefined set of validation methods, assessing models for parametrization errors. Evaluation results using classical F-score metrics demonstrate that most tested LLMs identify a majority of incorrect models, while the best-performing model achieves high accuracy in differing between correct and wrong simulation models.

**Keywords:** multibody dynamics, mechanical system simulation, large language models, model validation, AI agents

---

## 1 Introduction

The advent of Large Language Models (LLMs) rapidly transformed a wide range of domains, from education and writing to scientific discovery and software development. As their capabilities continue to expand, there is growing interest in applying LLMs to engineering tasks, which often present unique challenges such as limited access to proprietary or standardized technical data, complex reasoning over physical laws and symbolic representations, and the absence of benchmarks that evaluate functional correctness beyond surface-level code generation.

### 1.1 Motivation
Ever since the breakthrough of machine learning for image classification tasks, several engineering applications benefited from the disruptive advances of neural network-based methods, such as in image classification in robotics [40], signal processing [35] or fault diagnosis [27]. The application of LLMs for engineering tasks is still in its infancy as compared to the broad application of LLMs for writing, education or coding [9, 16, 32]. A main problem here is the large amount of technical data, which is predominantly only available in closed sources, be it in databases of international standards (e.g., ASME and DIN) or in internal and therefore secret company databases [6]. Even if data would be available, secondary problems are related to missing evaluation methods for LLMs specialized in engineering.

Existing approaches to LLM benchmarking in engineering primarily assess correctness by comparing generated code using a LLM rubric-based comparison with expert-written reference code or based on API documentation. However, these methods remain tied to surface-level code analysis and do not necessarily reflect true functional performance. In contrast, we assess model correctness through an evaluation of physics-based results independent of how the code is structured or written.

### 1.2 State of the art
The field of Natural Language Processing (NLP) is concerned with how machines understand, interpret, generate and interact with natural languages – i.e. languages as spoken and written by humans such as English – are processed. Since State-Of-The-Art (SOTA) LLMs are trained on massive amounts of text, they are not only able to handle a variety of different natural languages, but also programming languages like C++ or Python.

The flagship models, which typically consist of several hundreds to thousands of billions of parameters, can usually not be run locally, but are only available via an online interface or API like OpenAI’s GPT models [29], Google Gemini [15] (previously known as Google Bard), as well as the Claude 3 model family [3]. In opposition, many of the open-source models like Mistral [22] and its coding-generating variant Codestral, are relatively small models which can be run locally on consumer GPUs. The model family Phi [1] by Microsoft is developed with the goal of providing small language models to be run locally, including smartphones. The open-weight Llama models, developed by Meta, cover a large range of pre-trained sizes, from 8B to 405B (B = billion parameters). The Llama 3 [12] weights of the models are available to run locally, but details on training algorithm and data are not fully disclosed. For research, being able to access the model’s weights and settings is an advantage over closed models due to reproducibility, transparency and size optimizations using quantization techniques. As running LLMs is not only compute-intensive but also requires large GPU memory, quantization techniques are commonly applied to language models after training [10], where parameters of reduced precision are applied rather than 32-bit full precision (floating-point) values. It was found that even 4-bit quantized models are performing well [8], thus enabling bigger LLMs to fit into the same memory using lower-bit quantization can be advantageous.

Assessing the performance of models is a challenging task, as natural languages are ambiguous and vague [39]: two sentences can differ on a word level but still be semantically similar. Originally proposed by Alan Turing in 1950 to distinguish humans from machines, the Turing test – recently reported as passed by modern LLMs with up to 73% human deception rate [21] – involves subjective human judgment, motivating the development of diverse datasets and quantitative evaluation methods for NLP. Early methods like BLEU [34], used for evaluation of machine-translation, and ROUGE [24], applied to automatic summarization, used word overlap and thus do not capture semantic understanding. To test syntax, semantic similarity and reasoning, modern benchmarks like General Language Understanding Evaluation (GLUE) [46], SWAG: a dataset for grounded commonsense inference [51], and the Massive Multitask Language Understanding (MMLU) dataset [18] were developed as well as datasets for specific fields or tasks like MATH [20] and IFEval [54]. The difficulty of these evaluation methods has substantially increased due to the development of more advanced LLMs and their applicability to new problems, thus many datasets were updated [44, 45, 53]. For coding specific benchmarks are developed where code is generated from specifications given in natural language [19, 26], where correctness is checked by test cases.

To test the LLM knowledge and reasoning capabilities, the Google-Proof Q&A GPQA [38] and most recently superGPQA [7] are designed to evaluate graduate-level knowledge and reasoning capabilities across many disciplines, with the superGPQA reporting an accuracy of 61% for the DeepSeek-R1 [17] reasoning model. Although benchmarks include mechanical engineering questions, they are usually underrepresented, e.g., with only 4% in Humanity’s Last Exam (HLE) [31]. Moreover, despite reports of strong performance on multiple choice mechanical engineering exam questions [11], this study only finds a low correlation between common benchmarks and correct simulation code for the presented mechanical engineering problems.

Although LLMs are not inherently well-suited for solving computational problems – a well-known example is that many LLMs fail to correctly count the number of occurrences of "r" in "strawberry" – they handle many programming languages [23], tools and APIs [4, 43] surprisingly well, and they can even act as dynamic agents [37]. To provide LLMs with up-to-date knowledge and improve domain knowledge, Retrieval Augmented Generation (RAG) can be used [36], potentially also for unknown, closed source code [5]. Alternatively, pre-trained models like Llama can be fine-tuned for specific domains and simulation tools, as previously done for Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) [41], but a (high-quality) dataset and large amount of computing power is required. Commonly a ground truth is provided for evaluating performance [25]. Alternatives are one or more LLMs working together [28], where roles such as worker and evaluator or judge might be assigned both for general answers [52] and engineering specific [41, 47]. As for many applications not only plain programming languages are relevant, more recently specific benchmarks for agents to test function calling [49] and tool usage for real-world domains [50] were developed. Traditional supervised pre-training does typically not account for the multi-step dynamic environments the agents are interacting with. To address this, [33] performs iterative fine-tuning with an LLM as a judge.

### 1.3 Objectives and novelty
As shown in the state of the art, the following open problems are identified regarding LLMs for engineering tasks. The first objective and novelty of this paper concerns a fully automated simulation-based evaluation method, in particular to assess the ability of LLMs to create simulation models using a set of mechanical model problems. Because the list of model problems is limited and results cannot be generalized to other problems or domains, the second objective of the paper tackles the question of self-validation ability of LLMs. Can we use LLMs as autonomous agents which perform simulation tasks and evaluate the correctness of the numerical models? While the latter question may sound unfeasible – LLMs checking output of other LLMs –, self-evaluation is enabled by using numerical (in-silico) experiments, thus grounding the LLMs even in the case that they are biased.

In order to achieve the objectives, LLM agents (AI agents) are used to generate simulation models from parametrized textual descriptions. Having ground truth simulation models created by experts, this allows an automated way of evaluation LLMs regarding their ability to correctly model mechanical systems and to create simulation models, thus having a basic – but automated – way of evaluation.

While the primary focus lies within the domain of Multibody Dynamics (MBD), the methodology is designed with extensibility in mind, allowing it to be adapted and transferred to other simulation-driven fields. In doing so, the framework not only supports the assessment of the performance of such large-scale language models in engineering simulation contexts, but also lays the groundwork for broader applicability in domains where physical correctness and semantic alignment are critical.

### 1.4 Structure of the paper
In Section 2, we outline the first part of our methodology, which focuses on evaluating LLM generated simulation code in regards to its syntactic and semantic validity and the functional correctness for a set of canonical mechanical models. This part also highlights the importance of conscientious formulation of LLM input prompts. Building on these insights, Section 3 introduces a novel framework designed to enable self-evaluation through automated in-silico experiments, thereby reducing dependency on manually curated ground truth mechanical models. Finally, Section 4 and the conclusions hereafter summarize results obtained from both evaluation phases, highlighting key takeaways, limitations, and implications for the broader use of LLMs in simulation-driven domains.

---

## 2 Mechanical modeling and simulation code generation

In this section, we present the evaluation of LLMs for mechanical (simulation) model generation, focusing on multibody system dynamics. In particular, we define the mechanical problems, code generation pipeline, and the code evaluation metrics.

### 2.1 Mechanical problem definition
Systematic tests within the present paper are based on a set of mechanical problems. To keep the present approach more general, these problems are denoted as mechanical problems. Within this approach, $P$ represents the set of $n_P$ abstract mechanical problems or scenarios, as

$$P = \{p_k \mid k \in \{1, 2, \dots, n_P\}\} . \tag{1}$$

Each $p_k$ denotes a distinct mechanical scenario (e.g. flying mass point or slider-crank mechanism), independent of any specific modeling formalism or parameters. To translate each mechanical scenario into a form suitable for numerical simulation, we derive one or more mechanical models that capture the essential structure and behavior of the underlying system.

$M(p_k)$ represents the set of $n_{\text{var}}$ mechanical models that are created to represent the mechanical problem $p_k$ with

$$M(p_k) = \{m_{k,i} \mid i \in \{1, 2, \dots, n_{\text{var}}\}\} . \tag{2}$$

where each $m_{k,i}$ is a unique mechanical model (e.g. mass with initial position and velocity) representing the same mechanical problem $p_k$ through different parameters, modeling choices, or levels of abstraction indicated by subscript $i$. This results in a total $n_{\text{total}} = n_P \cdot n_{\text{var}}$ models considered.

For each parametrized model $m_{k,i}$ we assign a textual description: $\text{desc}_{k,i} = D_{\text{text}}(m_{k,i})$. The textual description may also include specific modeling hints, which is important to enable direct comparison of numerical results of simulation models generated by LLMs or experts, e.g., avoiding the choice between rigid body (6 DOF) and point mass (3 DOF) for the flying mass point.

To generate diverse textual descriptions for each model $m_{k,i}$, we define a template with parameter placeholders. This template-based approach enables the systematic creation of multiple semantically consistent variations by substituting parameters (in curly brackets) with different values. The textual descriptions in the present paper are created by multibody experts, however, they could also be created by LLMs using Wikipedia categories “machines” or “mechanisms” as starting point.

The following examples illustrate a template-based textual description of the model “flying mass point”, as well as one concrete instantiation using specific parameter values:

**Template for description:**  
*Projectile motion of a point mass with the following properties: mass $m$ = {mass} kg, gravity $g$ = {gravity} m/s$^2$, initial velocity in x/y/z-direction: $v_x$ = {vx} m/s, $v_y$ = {vy} m/s, $v_z$ = 0 m/s. The initial position is given as $x$ = 0 and $y$ = 0. Gravity acts along the negative y-axis, and there is no other external propulsion or resistance.*

**Parametrized description:**  
*Projectile motion of a point mass with the following properties: mass $m$ = 15 kg, gravity $g$ = 5.0 m/s$^2$, initial velocity in x/y/z-direction: $v_x$ = 0.5 m/s, $v_y$ = 3 m/s, $v_z$ = 0 m/s. The initial position is given as $x$ = 0 and $y$ = 0. Gravity acts along the negative y-axis, and there is no other external propulsion or resistance.*

Each parameter in the template can be instantiated from a predefined range of values, enabling the systematic generation of a large number of consistent textual variants for the same model $m_{k,i}$. The randomization of values is realized in two ways. Potential values may be provided as a list, e.g. ["x", "y"] in case of directions or varied instructions, or a list of specific values, in order to avoid unrealistic values. For more general values like stiffness or mass, we split numbers into base and exponent and choose random numbers from a predefined list of convenient numbers: $[1, 1.2, 1.25, 1.5, 2, 2.5, 3, 4, 5, 6, 7.5, 8]$. These values are chosen from within a specified numerical range for each parameter, such as $[5, 15]$, leading to the list $[5, 6, 7.5, 8, 10, 12, 12.5, 15]$. This randomization process avoids 16-digits numbers and produces values that are convenient for analytical computations and ensures parameters differing at least by 4%. For the template shown above this leads to 3 different values for $g \in [3.73, 9.81, 11.15]$, 8 values $m \in [5, 15]$, 41 values for velocity $v_x \in [0, 20]$ (smallest value after 0 is 0.01), and 6 values for velocity $v_y \in [10, 25]$. This yields a total of 5 904 distinct textual descriptions all corresponding to the same underlying mechanical model. In all cases, random values are chosen using a uniform distribution. The full list of available textual and parametrized descriptions is given in Table 1. With the present approach, each model typically includes thousands up to millions of variations, totaling to more than six billion models with different parameters. It is thus ensured, that the completion of the proposed benchmark cannot be accomplished through memorization.

### 2.1 Mechanical problem definition (Table 1)

#### Table 1: Overview on used mechanical models, including types of bodies, springs and joints; the model is defined to be a multibody system in case that the number of mass points and rigid bodies is larger than 1.

| $k$ | modelname | multibody system | point mass | rigid body | spring damper | distance constraint | spherical joint | prismatic joint | revolute joint | rolling disc | torsional spr.-damp. | Cartesian spr.-damp. |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | flying mass point | – | ✓ | – | – | – | – | – | – | – | – | – |
| 2 | free fall mass point | – | ✓ | – | – | – | – | – | – | – | – | – |
| 3 | single mass oscillator | – | ✓ | – | ✓ | – | – | – | – | – | – | – |
| 4 | single mass oscillator with gravity | – | ✓ | – | ✓ | – | – | – | – | – | – | – |
| 5 | slider crank / point masses | ✓ | ✓ | – | – | ✓ | ✓ | – | – | – | – | – |
| 6 | pendulum with elastic string | – | ✓ | – | ✓ | – | – | – | – | – | – | – |
| 7 | mass oscillator with user function | – | ✓ | – | ✓ | – | – | – | – | – | – | – |
| 8 | spinning disc | – | – | ✓ | – | – | – | – | ✓ | – | – | – |
| 9 | double mass oscillator | ✓ | ✓ | – | ✓ | – | – | – | – | – | – | – |
| 10 | n-mass oscillator | ✓ | ✓ | – | ✓ | – | – | – | – | – | – | – |
| 11 | single pendulum | – | ✓ | – | – | ✓ | – | – | – | – | – | – |
| 12 | double pendulum | ✓ | ✓ | – | – | ✓ | – | – | – | – | – | – |
| 13 | n-pendulum | ✓ | ✓ | – | – | ✓ | – | – | – | – | – | – |
| 14 | four-bar mechanism / point masses | ✓ | ✓ | – | – | ✓ | – | – | – | – | – | – |
| 15 | spring coupled flying rigid bodies | ✓ | – | ✓ | – | – | – | – | – | – | – | ✓ |
| 16 | torsional oscillator | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – |
| 17 | inverted single pendulum | ✓ | ✓ | – | – | ✓ | ✓ | – | – | – | – | – |
| 18 | disc rolling on ground | – | – | ✓ | – | – | – | – | – | ✓ | – | – |
| 19 | double pendulum elastic spring | ✓ | ✓ | – | ✓ | – | – | – | – | – | – | – |
| 20 | n-pendulum elastic spring | ✓ | ✓ | – | ✓ | – | – | – | – | – | – | – |
| 21 | elastic chain | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | – | – |
| 22 | single pendulum / rigid body | – | – | ✓ | – | – | – | – | ✓ | – | – | – |
| 23 | mass point on rigid string | – | ✓ | – | – | ✓ | – | – | – | – | – | – |
| 24 | mass point on elastic string | – | ✓ | – | ✓ | – | – | – | – | – | – | – |
| 25 | link on two prismatic joints | ✓ | ✓ | – | ✓ | ✓ | ✓ | – | – | – | – | – |
| 26 | flying rigid body | – | – | ✓ | – | – | – | – | – | – | – | – |
| 27 | suspended rigid body | – | – | ✓ | – | – | – | – | – | – | – | ✓ |
| 28 | gyroscope on spherical joint | – | – | ✓ | – | – | ✓ | – | – | – | – | – |
| 29 | prismatic joint system | – | – | ✓ | – | – | – | ✓ | – | – | – | – |
| 30 | two mass points with springs | ✓ | ✓ | – | ✓ | – | – | – | – | – | – | – |
| 31 | two mass points with distances | ✓ | ✓ | – | – | ✓ | – | – | – | – | – | – |
| 32 | rigid rotor simply supported | – | – | ✓ | – | – | – | – | – | – | – | ✓ |
| 33 | rigid rotor unbalanced | – | – | ✓ | – | – | – | – | – | – | – | ✓ |
| 34 | double pendulum / rigid bodies | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – |
| 35 | slider crank / rigid bodies | ✓ | – | ✓ | – | – | – | ✓ | ✓ | – | – | – |

---

### 2.2 Large language models for code generation
LLMs are increasingly integrated into Python-based frameworks to enable inference, reasoning, and task automation. However, LLMs are purely generative – they produce text but cannot act. To bridge this gap, agentic frameworks like LangChain[^1] and AutoGPT[^2] use LLMs as reasoning engines, allowing agents to autonomously select and execute actions based on context and predefined goals.

In our framework, LLM agents are employed for the automated generation and evaluation of simulation code. Specifically, agents are used to select relevant simulation elements and evaluation methods, creating the corresponding simulation code, and analyzing simulation results as described in Sections 2.4 and 3.1 in more detail. Whenever possible, we chose deterministic behavior within LLM-APIs, which we could confirm in repeated tests. We embed the agents within a controlled and fault-tolerant environment through systematic exception handling and error checking. To address the inherent ambiguity of LLM outputs, we incorporate XML-tags, which serve as identifiers for relevant information within the language model’s response. During post-processing, these tags are used to systematically extract only the information relevant to the agent’s task, discarding irrelevant content.

[^1]: https://www.langchain.com/
[^2]: https://agpt.co/

To support inference across diverse environments, we use both Hugging Face’s `transformers` pipeline [42] for general-purpose LLMs (e.g., LLaMA, Calme) and GPT4All [2], which is optimized for models in the GGUF format. GGUF enables efficient local inference via `llama.cpp`[^3], allowing direct use of pre-quantized models that run on consumer hardware with minimal setup. While Hugging Face also supports quantized inference through the `bitsandbytes` library, it generally incurs a higher resource overhead as quantization is performed at runtime.

To ensure representative evaluation across deployment scenarios, we selected LLMs from Hugging Face’s Open LLM Leaderboard[^4] based on available hardware, using quantized models where necessary to meet resource constraints. Specifically, we used two NVIDIA H100 GPUs for high-end inference with Hugging Face’s backend (HF) and a consumer-grade RTX 4090 for local execution via GPT4All.

[^3]: https://github.com/ggml-org/llama.cpp
[^4]: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/

Although reasoning models like Deepseek R1 [17] and OpenAI O1 [30] – which are models that go through several steps of a *chain of thought* before answering the question – are currently among the best-ranking LLMs in common benchmarks, they are not employed in the current work due to their larger model sizes, low throughput, and a lack of noticeable improvements in output quality based on initial experiments.

### 2.3 Code generation pipeline
The present section describes how textual descriptions are converted into simulation code using the Python package Exudyn [13]. Note that Exudyn is a simulation engine made for engineers, purely based on physical principles and used in the multibody system scientific community. In a previous work the authors could show that LLMs can convert a textual description directly into a simulation code [14], using closed source, large-context capable and commercial LLMs like ChatGPT. However, it was shown that the reliability of this approach could be drastically improved in case of proper context, providing information on relevant code elements (such as creation of rigid bodies or joints). In the present paper, we use a similar but refined approach, suitable also for much smaller open-source LLMs with smaller context size. Additionally, the present approach is fully automated using LLM-agents running in a loop, creating hundred simulation codes within 10 to 30 minutes on consumer-grade GPUs. We like to note that occasional tests without proper context always failed (with many errors), as our tested LLMs are only partially aware of Exudyn syntax.

Given a textual description $\text{desc}_{k,i}$ an LLM-agent is asked to identify and select the set of simulation code elements that are required for an accurate representation of the described mechanical model. For this selection process, the query includes a predefined set of 22 available modeling elements – such as ground objects, rigid bodies, mass points, constraints, joints, or applied forces – which serve as building blocks for the simulation code. The agent analyzes the list of elements together with the textual model description $\text{desc}_{k,i}$ and maps it to a subset of elements necessary for representing the mechanical model.

After proper processing the subset of elements, we construct a tailored In-Context Learning (ICL)-prompt containing examples and explanations for each of the subset of simulation code elements the LLM-agent previously deemed relevant. These texts contain modeling components such as `GroundObject`, `MassPoint`, and `Force`, along with typical parametrization (but not fitted to the given task) and also include typical library imports and solver calls. The following listing shows an excerpt of such a context, corresponding to the elements `ground` and `mass point`, as needed for the flying mass point example (for full sources, see the GitHub link in the Section “Declarations”):

```python
1  #Create a ground object as an inertial reference frame for the multibody
2  #      system.
3  oGround = mbs.CreateGround(referencePosition=[0,0,0])
4  
5  #Create a point mass object with specified mass at reference position with
6  #      optional initial conditions
7  #physicsMass: the mass in kg
8  #referencePosition: initial/reference position at which mechanism is
9  #      defined;
10 #initialDisplacement: additional initial deviations from referencePosition;
11 #      usually this is [0,0,0]
12 #initialVelocity: initial velocities of mass point
13 #all vectors always have 3 components, no matter if 2D or 3D problem
14 oMass = mbs.CreateMassPoint(physicsMass=5, referencePosition=[1,0,0],
                               initialDisplacement=[0,0,0], #optional,
                               #relative to reference position
                               initialVelocity=[0,0.5,0],   #optional
                               gravity=[0,-9.81,0])         #optional
```

Within the context of the selected modeling elements, we sparsely provide software-specific instructions that define the required command structure, execution order, and necessary auxiliary operations. Having this context and the description for model $m_{k,i}$, the following code generation template is used for our Python-based multibody simulation framework Exudyn, easily transferable to other software packages:

***

The following Python example shows how to generate a multibody model in Exudyn, including most relevant features:
```python
"""
{contextOfTheSelectedModelingElements}
"""
```
Using this example, please build a Python model following exactly the following description of a multibody model:
`{modelDescription}`

Follow exactly the function names and argument names as given in the example and create the Exudyn model. Provide only the Python code without any additional descriptions; you don't need to add comments, except for special cases.
It is very important that you start the code with required imports and that you mark the end of code with the line `"#end-of-code"`.

***

We like to note that this prompt – similar to others in the present paper – is optimized in order to meet restrictions of our tested LLMs as well as to maximize performance, just mentioning a few:

*   The `"#end-of-code"` tag is needed, because often LLMs write text after the final line of code, which cannot be processed automatically.
*   `"do not add comments..."` is required to minimize the number of output tokens.
*   `"Follow exactly the function names and argument names..."` reminds the LLM not to invent or guess any new arguments or function names, usually leading to semantic errors.

By performing inference on each distinct parametrized model description $\text{desc}_{k,i}$ with an input prompt in the form described above, we obtain a corresponding set of LLM-generated simulation codes for each model $m_{k,i}$ as

$$\text{code}_{k,i} = C_{\text{LLM}}(m_{k,i}) . \tag{3}$$

In case of our self-validation approach in Section 3, the template is slightly extended regarding information for the evaluation method. For another case of an elastic chain with mass points (in this case with 15 masses), the LLM QwenCoder-32B-Q4 generated the following simulation code (showing only main part of the code here):

```python
1   ...
2   #Create a ground object as an inertial reference frame for the multibody
3   #      system.
4   oGround = mbs.CreateGround(referencePosition=[0,0,0])
5   
6   #Parameters
7   m = 1  # mass in kg
8   l_single = 1.5  # length of each chain element in m
9   k = 7500  # stiffness in N/m
10  d = 500  # damping in Ns/m
11  g = 3.73  # gravity in m/s^2
12  
13  #Create 15 mass points
14  mass_points = []
15  for i in range(15):
16      oMass = mbs.CreateMassPoint(physicsMass=m, referencePosition=[i*
                                  l_single,0,0],
17                                  initialDisplacement=[0,0,0],
18                                  initialVelocity=[0,0,0],
19                                  gravity=[0,-g,0])
20      mass_points.append(oMass)
21  
22  #Create spring–dampers between mass points
23  for i in range(14):
24      oSpringDamper = mbs.CreateSpringDamper(bodyNumbers=[mass_points[i],
                                                mass_points[i+1]],
25                                             localPosition0=[0,0,0],
26                                             localPosition1=[0,0,0],
27                                             referenceLength=None,
28                                             stiffness=k, damping=d)
29  
30  #Fix the left–most and right–most mass points to ground using spherical
31  #      joints
32  mbs.CreateSphericalJoint(bodyNumbers=[oGround, mass_points[0]],
33                           position=[0,0,0],
34                           constrainedAxes=[1,1,1])
35  
36  mbs.CreateSphericalJoint(bodyNumbers=[oGround, mass_points[14]],
37                           position=[14*l_single,0,0],
38                           constrainedAxes=[1,1,1])
39  
40  #Assemble has to be called just before solving or system analysis (after
41  #      AddSensor!).
42  mbs.Assemble()
43  ...
```

This example already shows the difficulties the LLM has to tackle, in particular related to the for-loop and the correct positioning of mass points as well as of joints.

After code generation, the raw LLM-output is post-processed, mainly to extract Python code and to remove any undesired (e.g., “Here is the requested code:”) or vulnerable content. This step is necessary due to the variability in output formatting and occasional deviation from prompt constraints, as outlined in Section 2.6. While some LLMs only produce plain codes, some others generate Python code in markdown format, which is why we remove text after the `#end-of-code` tag and prior to import routines. Additionally, we add simulation timeout, we redirect simulation-code output to a specified file, and set the destination of simulation results, and we remove all visualization and plotting commands. The latter steps are done with simple line-by-line text-replace commands. Fig. 1 exemplarily shows screenshots for the slider-crank mechanism, which the best performing LLMs are able to correctly create. The graphics shown there is not created by the LLMs (as it was not requested) but taken from the provided sample files.

***

### Figure 1 Description (Snapshots of Slider-Crank Mechanism)
Figure 1 contains four sequential snapshots of a 3D multibody slider-crank simulation generated within Exudyn, demonstrating the successful construction of the complex mechanism containing a blue rotating disc, blue crank pin, dark blue connecting link, and an orange slider block moving horizontally. The solver-finished status is printed at time steps $t = 0$, $t = 0.4$, $t = 0.8$, and $t = 1.2$ seconds respectively.

**Fig. 1:** Snapshots of the slider-crank mechanism with rigid bodies and joints, one of the more complicated tasks in our mechanical models set.

***

### 2.4 Basic code evaluation
Given the large volume of simulation code generated by the LLM, a central challenge arises: how to systematically assess the quality of individual outputs? In other words, we require a method to distinguish between high-quality, correct code, and outputs that are incomplete, erroneous or producing wrong results. This reflects a broader and well-known problem in the domain of LLMs – namely, how to evaluate whether a given output meets the intended task requirements.

Numerous benchmark methodologies have been proposed in this context, each aiming to provide objective or task-specific criteria for determining the performance of LLM-generated content. However, as discussed in Section 1.2 and visualized in Fig. 3, existing SOTA evaluation methods fall short in capturing the correctness of simulation codes within the specific context of MBD. To address this gap, we introduce a basic code evaluation approach that utilizes ground truth implementations for selected mechanical models as a basis for comparison.

Generated simulation code for a parametrized model $m_{k,i}$, as defined in equation Eq. (3), is thus compared against a predefined ground truth, as $\text{code}_{k,i}^{\text{GT}} = C_{\text{GT}}(m_{k,i})$, to assess its correctness. Each ground truth code is carefully prepared and tested by domain experts, and is not provided to the LLMs. Both the expert- and LLM-generated codes are evaluated using identical model parameters to ensure comparability. To further alleviate automatic evaluation of the modeling part, the solver configuration from the ground truth implementation is reused in the corresponding LLM-generated code for comparison. This allows to perform an exact comparison of numerical results of system coordinates, independently of time integration accuracy and time-wise interpolation of results, thus focusing the evaluation to the physical and semantic correctness of the mechanical model.

Before executing any LLM-generated simulation code, we establish a controlled execution environment in which the code is preprocessed and sanitized prior to simulation. In case of errors, exceptions are catched, analyzed and documented.

The results are obtained by executing each simulation code of the model $m_{k,i}$ denoted as

$$(\rho_{k,i}, r_{k,i}) = \text{exec}(\text{code}_{k,i}), \quad \text{and} \quad (\rho_{k,i}^{\text{GT}}, r_{k,i}^{\text{GT}}) = \text{exec}(\text{code}_{k,i}^{\text{GT}}) . \tag{4}$$

Both the results of the LLM-generated code and the ground truth code include two elements: $\rho$, which indicates whether the code terminates with an error ($\rho = 0$) or without one ($\rho = 1$), and $r_{k,i}$, which represents the corresponding numerical simulation result. Note that `exec()` refers to Python’s built-in `exec()` function, which is used to obtain these outputs. Based on this information, we systematically assess the validity of the simulation code by employing two evaluation criteria:

*   **a)** First we investigate if the code is executable, which is based on the ability of a generated simulation code $\text{code}_{k,i}$ to execute without raising syntax or runtime exceptions. This syntactic correctness includes both Python and simulation software (Exudyn) syntax. Formally, we define that a code $\text{code}_{k,i}$ is executable if $\rho_{k,i} = 1$.
*   **b)** Secondly, we analyze if the generated code is correct by comparing it with an expert-created ground truth simulation code. More specifically we analyze the numerical difference of $r_{k,i}$ and $r_{k,i}^{\text{GT}}$, which are both time-dependent solution files with the stored simulated system states (e.g., generalized coordinates) at discrete time steps.

Let $r_{k,i} \in \mathbb{R}^{n_t \times d}$ and $r_{k,i}^{\text{GT}} \in \mathbb{R}^{n_t \times d}$ denote the numerical results obtained from $\text{exec}(\text{code}_{k,i})$ and $\text{exec}(\text{code}_{k,i}^{\text{GT}})$, respectively, where $n_t$ is the number of time steps and $d$ the number of compared coordinates. For comparison, we use coordinates at position, velocity and acceleration level, but no constraint forces, as they may differ just due to joint order while solutions are still correct (this may also happen for bodies, but less likely in our problems). Functional equivalence is assessed by computing a norm-based difference between these solutions as

$$\Delta(r_{k,i}, r_{k,i}^{\text{GT}}) = \min \left( \|r_{k,i} - r_{k,i}^{\text{GT}}\|, \|(r_{k,i} + x_{\text{R}}) - (r_{\text{ref}} + x_{\text{R}})\| \right) . \tag{5}$$

Here, $x_{\text{R}}$ represents the reference configuration extracted from the system description and is included to account for relative representations of the model state. If the resulting difference $\Delta(r_{k,i}, r_{k,i}^{\text{GT}})$ lies below a predefined threshold $\varepsilon$, the simulation results are considered functionally equivalent if

$$\text{code}_{k,i} \equiv \text{code}_{k,i}^{\text{GT}} \iff \Delta(r_{k,i}, r_{k,i}^{\text{GT}}) \le \varepsilon . \tag{6}$$

Preliminary experiments indicated that a threshold of $\varepsilon = 10^{-5}$ provides a robust criterion for distinguishing functionally equivalent simulations from diverging ones. This value effectively accounts for minor numerical round-off errors. It is larger than expected for comparison of mechanical models due to the fact that a single round-off error due to different order of evaluations (e.g., two force elements) may lead to round-off errors due to implicit time integration up to $10^{-6}$ for the present case of example problems.

Thus, we define the executability score $\eta$ and correctness score $\kappa$ as

$$\eta = \frac{\sum_{k,i} \rho_{k,i}}{n_{\text{total}}}, \quad \text{and} \quad \kappa = \frac{\left| \left\{ r_{k,i} \ \middle|\ \Delta(r_{k,i}, r_{k,i}^{\text{GT}}) \le \varepsilon \right\}_{k=1,i=1}^{n_P, n_{\text{var}}} \right|}{n_{\text{total}}} . \tag{7}$$

A schematic overview of the entire pipeline, from physical problem definition, model parametrization, and prompt-based code generation to post-processing and basic code evaluation, which has been prescribed in of Section 2.3 and 2.4, is provided in Fig. 2.

***

### Figure 2 Description (Pipeline Overview)
Figure 2 presents a flowchart summarizing the basic code evaluation pipeline. It shows a physical problem $p_{k=0}$ and parameters generating a textual description $\text{desc}_{k,i}$. This description is fed into an LLM Agent for model selection (elements context) and code generation. The resulting code, including solver settings, undergoes execution via `exec()`, producing the LLM-based solution $r_{k,i}$. Concurrently, domain experts formulate a ground truth model $\text{code}^{\text{GT}}_{k,i}$ and run it to produce a numerical ground truth $r^{\text{GT}}_{k,i}$. Finally, both the executability and correctness of the LLM outputs are determined in the basic code evaluation block.

**Fig. 2:** Schematic overview of the pipeline for simulation code generation and basic evaluation using domain-expert based ground truth implementations.

***

### 2.5 Basic evaluation results
To assess the performance of the proposed code generation and evaluation pipeline, we conducted a series of tests using a selection of SOTA LLMs provided by organizations such as Meta, Calme, Mistral, and Qwen. Each LLM was tasked with generating simulation code for a predefined set of physical problems, formally represented by a curated collection of 35 textual model descriptions. An overview of these mechanical models, showing the main modeling elements, is provided in Table 1. Table 2 shows the performance of 14 different LLMs within our basic evaluation using 10 randomized parametrizations of each mechanical model, totaling to 350 simulation model generations. The tested language models include both Hugging Face (HF) GGUF-formatted models, the latter enabling a wide variety of quantized versions down to 1 bit. Across models, instruction- or chat-tuned versions were selected due to their significantly better performance in code generation tasks. Note that the table uses simplified names for the models; actual identifier strings differ in the respective backends. Notably, 4-bit quantized models, such as Llama3.1-8B-Q4, achieve comparable accuracy and executability to their higher-precision counterparts like Llama3.1-8B-HF, while requiring 53% less runtime and substantially less VRAM. This makes them particularly attractive for resource-constrained environments. For example, QwenCoder-32B-Q4 delivers SOTA results while operating under 18 GB VRAM, outperforming even much larger models like Llama3.3-70B-HF, which needs 141 GB. QwenCoder generated only two non-executable codes, and just 8.3% were incorrect, highlighting its strength in coding-specific tasks.

To contextualize our domain-specific evaluation, we compare our correctness and executability scores with general-purpose benchmark scores from Hugging Face’s Open LLM Leaderboard, as introduced in Section 1. For comparison, we compute the Spearman rank correlation between our scores and those reported on the leaderboard. Note that most metrics are documented only for the 16-bit quantized versions. However, initial tests indicate that the specific quantization used has minimal impact on performance, validating this approach. As shown in Fig. 3, most general-purpose scores show pure correlation with correctness and executability from the simulation model generation approach. As a slight exception, we emphasize and discuss the correlation with IFEval (instruction-following evaluation). As our approach provides detailed information and instructions for model generation, a good performance on instruction-following is required to achieve a high score. However, as the IFEval metric does not measure physics or mechanical knowledge, we find that IFEval itself is not sufficient for our task, as this benchmark does not capture the physical reasoning required for simulation-based modeling – highlighting the limitations of existing evaluation methodologies. This is also underlined by the fact that QwenCoder has a 10% lower IFEval score than Llama3.1-70B, which is just the opposite to our score results (correctness).

#### Table 2: Overview of the tested LLMs, their specifications, and their correctness ($\kappa$) and executability score ($\eta$).

| model name | #parameters (B) | quantization | runtime (min) | tokens per second | VRAM (GB) | backend | correctness (%) | executability (%) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Codestral-22B-Q6 | 22 | 6 | 73 | 32 | 17.5 | gguf | 68.0 | 90.9 |
| DeepSeekCoder-16B-Q6 | 16 | 6 | 57 | 47 | 13.7 | gguf | 26.3 | 55.4 |
| DeepSeekCoder-33B-Q4 | 33 | 4 | 164 | 32 | 18.2 | gguf | 28.6 | 76.0 |
| FluentlyLM-Q4 | 32 | 4 | 111 | 29 | 18.9 | gguf | 39.1 | 72.6 |
| Llama3-8B-Q4 | 8 | 4 | 41 | 86 | 4.6 | gguf | 19.7 | 76.3 |
| Llama3.1-70B-HF | 70 | 16 | 258 | 10 | 141 | HF | 80.9 | 95.1 |
| Llama3.1-8B-Q4 | 8 | 4 | 41 | 86 | 4.6 | gguf | 30.3 | 77.1 |
| Llama3.3-70B-HF | 70 | 16 | 257 | 10 | 141 | HF | 78.9 | 94.0 |
| Phi4-Q4 | 15 | 4 | 33 | 57 | 8.2 | gguf | 74.9 | 93.1 |
| Qwen2.5-32B-Q4 | 32 | 5 | 138 | 29 | 19.9 | gguf | 18.0 | 35.7 |
| Qwen2.5-72B-HF | 72 | 8 | 144 | 11 | 178 | HF | 85.4 | 98.3 |
| QwenCoder-32B-Q4 | 32 | 4 | 89 | 30 | 17.8 | gguf | 91.7 | 99.4 |
| ViperCoder-Q8 | 15 | 8 | 120 | 37 | 14.5 | gguf | 64.6 | 90.3 |

---

### 2.6 Perturbation analysis and prompting
To investigate the sensitivity of LLMs to variations in prompt formulation, we conduct a perturbation analysis. Specifically, we apply controlled structural perturbations to the textual description of mechanical models by introducing random formatting changes. These changes include inserting additional spaces between words, and replacing standard sentence delimiters (represented by the string `". "` ) with a period followed by a line break (`".\n"`). Each perturbed version is identified by a unique variation-identifier `variation ID`, where the IDs are increasing with the degree of variation.

To quantify syntactic differences between generated simulation codes, we compute a pairwise Levenshtein distance matrix [48], for which the minimum number of single-character edits (insertions, deletions, or substitutions) required to transform one string into another is calculated. The distance values are computed for all pairwise combinations and normalized by text length to ensure comparability. Secondly, we analyze the simulations using the correctness evaluation described in Section 2.4. Similar to the aforementioned, simulation results of both the LLM- and expert-generated code are numerically compared and the code generated by the LLM evaluated as being correct or incorrect.

***

### Figure 3 Description (Correlation Matrix)
Figure 3 presents a color-coded Spearman rank correlation matrix comparing performance metrics on several standard LLM benchmarks (MATH, IFEval, MMLU-Pro, GPQA) against the Correctness ($\kappa$) and Executability ($\eta$) scores defined in this study. Key correlations include:
- MATH with MMLU-Pro: 0.89
- IFEval with Correctness: 0.65
- IFEval with Executability: 0.52
- Correctness with Executability: 0.94
The remaining correlation values between traditional academic benchmarks and physics correctness/executability are notably low (ranging from -0.08 to 0.26), indicating a general disconnect.

**Fig. 3:** Correlation matrix for existing benchmark evaluation metrics and the proposed metrics of this work: correctness ($\kappa$) and executability ($\eta$).

***

Our findings reveal that even superficial changes to the textual description of mechanical models can induce significant differences in LLM generated code, both in terms of structure (see Table 3) and correctness. Furthermore, the analysis shows that the sensitivity varies across the utilized backends (e.g., Hugging Face API versus GPT4all), as illustrated in Fig. 4. Therefore, it requires to perform variations in the tests in order to obtain representative results. However, we also observe in Table 3 that many tasks are either simple and thus always successful or hard and therefore wrong in all ten cases. Even though that all tests for a model may be correct, the codes may still be different.

---

## 3 Self-validation of simulation models with LLM agents

In this section, we explore the concept of self-supervised validation of simulation models using LLM agents. Unlike traditional uses of LLMs purely for generation or evaluation, our approach incorporates ground-truth data directly from simulation environments. This integration helps to mitigate the potential biases of LLMs and enriches the evaluation process with reliable reference information.

As a motivation, two key application scenarios are mentioned where such self-validation capabilities are highly beneficial:

*   **Case 1: Large-scale generation and evaluation of physical simulation models.** Here, LLMs are used to generate simulation models based on open sources such as engineering textbooks or engineering-related Wikipedia articles. This setup enables the creation of a large collection of documented simulations, potentially forming the basis of an engineering knowledge database. The ability to perform self-evaluation with high accuracy using simulation ground truth would significantly enhance the quality and trustworthiness of the resulting dataset. Furthermore, such validated data could serve as a valuable resource for further training and refinement of LLMs.
*   **Case 2: LLM-assisted model generation for engineering applications.** In this context, engineers collaborate with LLMs to develop simulation models. If these models can be automatically validated against simulation-based ground truth, their reliability and practical usability could be greatly improved.

***

### Table 3 & Figure 4 Description

#### Table 3: Correctness of the simulation code for mechanical models with varying textual descriptions (variation ID) using Phi-4 (GGUF) in 4-bit quantization.
Table 3 is represented as a horizontal grid plot across models $k \in [1, 35]$ (x-axis) and variation IDs $1$ to $10$ (y-axis). Green regions represent "Correct simulation code", while Red regions show "Diverging/Erroneous simulation code". 
- Selected models like $k=1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 18, 20, 21, 22, 23, 27, 28, 29, 30, 31, 34, 35$ are perfectly green (correct) across all 10 variations.
- Models $k=5, 13, 15, 17, 19, 24, 25, 26, 32, 33$ are dominated by red blocks, indicating consistent failure under parameter/structural changes.
- Intermittent failures appear under $k=10$ (var. ID 3, 6, 9), $k=12$ (var. ID 3), $k=21$ (var. ID 4, 10), and $k=33$ (var. ID 3).

#### Fig. 4: Levenshtein distance heatmaps of generated simulation code for free-falling masspoint using LLama 3.1-8B (GGUF and HF).
Two triangular distance heatmaps show the normalized Levenshtein distance between generated codes for the free-falling masspoint (model 2) under variations 1–10. Heatmap (a) corresponds to GGUF, showing higher structural code variation (distances up to 14). Heatmap (b) corresponds to HuggingFace, showing more syntactic consistency (distances mostly up to 10).

***

### 3.1 Model validation framework with AI agents
With the experimental proof that LLMs are able to generate simulation models from textual descriptions, see Section 2.5, we apply this capability to self-validate simulation models. The validation is then compared to the ground truth in order to determine the performance of this approach. The same approach is applied to intentionally incorrect models in order to check whether model errors are determined.

Within the model validation framework, performed as in-silico experiments with AI agents, there are two nested loops. The outer loop runs over all available models $m_{k,i}$, which are listed in Section 2.3, while the inner loop performs a validation for a single model. For every model with a certain parametrization, a set of evaluation methods is created first, chosen from a list of 18 available methods given shown in Table 4. Before the LLM creates the simulation model $m_{k,i}$, it is asked to choose a set with $n_e = 8$ different evaluation methods,

$$E(m_{k,i}) = \{e_{k,i,j} \mid j \in \{1, 2, \dots, n_e\}\} . \tag{8}$$

Note that an LLM may sometimes not return $n_e = 8$, however, we use $n_e$ in further considerations for simplicity.

#### Table 4: Evaluation methods and IDs, used by LLMs to select a subset of methods.

| v-ID | Evaluation method | v-ID | Evaluation method |
| :---: | :--- | :---: | :--- |
| 1 | Perform a rough calculation | 10 | Check if spherical motion |
| 2 | Evaluate analytical formulas | 11 | Check if circular motion |
| 3 | Evaluate position trajectory | 12 | Check if parabolic motion |
| 4 | Evaluate initial position | 13 | Evaluate motion space |
| 5 | Evaluate static equilibrium for damped systems | 14 | Evaluate velocity space |
| 6 | Evaluate eigenfrequencies of undamped system | 15 | Evaluate angular momentum conservation |
| 7 | Evaluate complex eigenvalues | 16 | Evaluate linear momentum conservation |
| 8 | Check if straight-line motion | 17 | Evaluate damping effects |
| 9 | Check if planar motion | 18 | Evaluate symmetry |

To define intentionally incorrect models, we note that creating them directly is difficult and would require complex prompting or training of LLMs to deliberately introduce realistic but subtle errors. Instead, our approach to generating intentionally incorrect models is as follows: Within the valid parameter space of a given model $m_{k,i}$, we generate a new, randomized parametrization such that each parameter differs from the original. This strategy avoids the issue that modifying only a single parameter might still lead to a valid simulation result (e.g., when a changed parameter does not affect the model outcome, such as gravity being irrelevant for a frictionless horizontal motion). Importantly, while the simulation results are still taken from the correct, expert-created model, the model description itself is altered. This decouples the model from the results, simulating an invalid case without re-generating the simulation model, allowing a consistent comparison between correct and incorrect models while significantly reducing computational costs.

***

### Figure 5 Description (Lab-in-the-Loop Framework)
Figure 5 presents a block diagram for the self-supervised loop. The model description $m_{k,i}$ is sent both to the "Numerical ground truth" branch (creating a baseline "Code evaluation") and to the "LLM agent" which processes model descriptions alongside chosen evaluation methods $e_{k,i,j}$. The LLM agent sets up the "Sensor context $s_{k,i,j}$" and generates "$\text{code}_{k,i,j}$ + solver settings" via its code generation pipeline. This is compiled and executed via `exec()`, producing the physical response "LLM-based solution $r_{k,i,j}$". This response, paired with sensor data, returns to "Model validation" inside the LLM agent, which computes the final numeric score $v_{k,i,j}$.

**Fig. 5:** Schematic overview of the lab-in-the-loop framework.

***

### 3.2 Single model validation
The single model validation is performed by processing $n_e$ evaluation methods, as sketched in Fig. 5, showing the main part of the framework. Starting with a model $m_{k,i}$ and an evaluation method $e_{k,i,j}$, the task is to generate a conjecture (= hypothesis) $H_{\text{text}}(m_{k,i}, e_{k,i,j})$. For instance, in case of “Evaluate complex eigenvalues” the LLM shall generate a conjecture for the eigenvalues of the system. If a method like “Evaluate motion space” requires a sensor, the prompt also includes the request to provide information on the selected sensor, in particular to which body and at which position it is applied, given as $s_{k,i,j} = S_{\text{text}}(m_{k,i}, e_{k,i,j})$.

LLMs usually write a lot of additional, possibly helpful information next to the requested texts. For this reason, we require common XML-tags to mark the relevant output, such as to put the conjecture inside tags `<conjecture>...</conjecture>` as well as the information on the required sensors, using `<sensor>...</sensor>`. As LLMs are accustomed to such constructs, this approach rarely failed in our experiments. Having the parametrized model $m_{k,i}$, the evaluation method $e_{k,i,j}$ and the sensor information $s_{k,i,j}$ – but not the conjecture – the LLM is asked to generate a simulation $\text{code}_{k,i,j}$ based on this information. Here, we have to state that there are two potential sources of errors. Most likely errors involve the simulation model creation itself, while less likely, the application of the sensor itself could be wrong. While we are finally validating the model for correctness of the system coordinates within each step of the simulation, we cannot evaluate the correct application and usage of the sensor. Checking the results and outputs, we only found an insignificant amount of errors due to sensor application.

The code generation is done very similar to Section 2.3, only with the additional evaluation method and sensor to be added. In particular, we require to assign the result of the evaluation method into the variable “output”, which is automatically evaluated by our code, depending on the given evaluation method. Due to cases where the evaluation method is applied incorrectly, in particular when results are not written into the correct variable, the performance of executable codes drops slightly below the performance in Section 2.5.

### 3.3 Extraction of single simulation results
The retrieval of simulation results is a critical task, as it shall be the same for all given mechanical model types. In all cases of analysis, we define simulation textual analysis outputs, given as map from model description $m_{k,i}$, evaluation method $e_{k,i,j}$, and sensor information $s_{k,i,j}$,

$$o_{k,i,j} = O(m_{k,i}, e_{k,i,j}, s_{k,i,j}) \tag{9}$$

Note that outputs $o_{k,i,j}$ represents the results for single sensors or an analysis method (e.g., eigenvalues) and are therefore conceptually different from Eq. (4).

A template is again used to translate simulation results into text. Herein, information on the measured data (eigenvalues, position sensor, etc.) is provided. In case of system analysis methods, such as eigenvalues, the retrieved information provides only the first 12 eigenvalues of the system (omitting the eigenvectors). In case of sensors, which often could include thousands of time steps, output is first resampled into 11 steps. For a simulation time of 1 second, this gives steps of 100 ms, including initial and final values. A larger number of values would be sometimes helpful, in cases like oscillatory motion, but as LLMs often validate every time step, we stick to this value. In all cases of numerical data, the number of provided digits for $o_{k,i,j}$ is limited. For this reason, we do not use conventional round methods, but use dynamical rounding to four effective digits, independent of the exponential part of floating point numbers. Most used LLMs could handle four-digits numbers in basic algebraic operations with sufficient precision (as we only require 2% accuracy for a model to be considered as correct).

### 3.4 Evaluation of single simulation results
For the evaluation of single simulation results two approaches have been tested:

*   **Conjecture-based evaluation:** The first method is based on using the conjectures $H_{\text{text}}(m_{k,i}, e_{k,i,j})$ generated by the LLM as the reference. This approach involves comparing the simulated results directly against the expected outcome as inferred from the conjecture. However, this method produced largely erroneous results, and therefore has been abandoned. The root cause lies in the disconnect between the generation of the conjecture and the actual simulation model – since the conjecture is created before the simulation code is written, discrepancies are common. Often, the model does not fulfill the original assumptions made in the conjecture, leading to false negative evaluations.
*   **Direct evaluation:** The second method bypasses the conjecture entirely and instead evaluates the raw numerical simulation results using the selected evaluation method. Here, another LLM call is used to interpret the numerical data and determine whether the outcome is physically plausible and consistent with the task. This method yielded significantly more reliable results than the conjecture-based method and provided similar reasoning chains to those used in the conjecture-based approach.

In both approaches, the final step of the evaluation involves a dedicated LLM call. Given the model description $m_{k,i}$, the evaluation method $e_{k,i,j}$, sensor placement $s_{k,i,j}$, and outputs from the simulation $o_{k,i,j}$, the model is scored on a scale from 0 to 100. The score is encapsulated in the LLM output using tags (e.g., `<score>75</score>`). The numerical evaluation score, see also Fig. 5, is defined as 1/100 of score returned by the LLM,

$$v_{k,i,j} = \frac{1}{100} \text{score}_{k,i,j} = V(m_{k,i}, e_{k,i,j}, o_{k,i,j}) . \tag{10}$$

Note that the data for evaluation does not include information on $\text{code}_{k,i,j}$, as it would obviously show the intentionally wrong parameters.

Fig. 6 shows heatmaps with scores $v_{k,i,j}$ for each mechanical model $k$, using the evaluation method v-ID from Table 4 in columns. The figure shows the heatmap for simulation models generated by the LLM QwenCoder-32B-Q4 and evaluated by GPT-4o. For some models, there are no evaluation methods, which is due to the fact that either simulation models have been identified to be incorrect (using methods from Section 2.4), or evaluation methods failed (e.g., no or not valid score). In Fig. 6 there are two heat maps, one for models that have been identified as correct, and one for models that have been intentionally made incorrect, see Section 3.1. The comparison of both heatmaps shows that the LLM predominantly identifies wrong models, however, there are several correct models marked as incorrect. The latter fact is caused by misinterpretation of results or incorrect analysis. We also clearly see, that some evaluation methods, in particular method 9 – “Check if planar motion”, give very similar scores for correct and incorrect models and are thus not very suitable in the present case. For this reason, further evaluation methods such as “Evaluate system degree of freedom” have not been considered in the present framework, as they were mostly inappropriate for determining correct or incorrect models. We also like to note that some cases seem to be simpler to be evaluated, e.g., wrong models are identified rather clearly for indices $k \in \{1, 2, 17, 18, 29\}$ throughout several LLMs, including Phi-4 and GPT-4o. Common errors for wrong evaluation of correct models are calculation errors by the LLM, e.g., a parabolic equation evaluated numerically wrong, giving > 2% error even with GPT-4o. Further common errors are related to the expected position and reference points of bodies.

***

### Figure 6 Description (Evaluation Score Grid)
Figure 6 displays a side-by-side comparison of model evaluation score matrices assigned by GPT-4o across 35 simulation models (y-axis) and 18 evaluation methods (x-axis). 
- **Left plot ((correct) models):** Displays mostly dark blue elements, showing that the system successfully scores valid models highly.
- **Right plot (intentionally incorrect models):** Displays a large concentration of light red/pink elements, proving that the evaluation methods successfully assign low scores to models containing parameterized defects.

**Fig. 6:** Comparison of model evaluation scores generated by GPT-4o across 35 simulation models (rows) and the set of 18 evaluation methods (columns). The left subplot shows scores correct models, and the right subplot shows corresponding results for intentionally incorrect models. Darker (blue) indicates high scores, while light red marks low scores. Axis labels are grouped and sparsely sampled for clarity.

***

### 3.5 Validation of single simulation models
For each model $m_{k,i}$, which may either be a correct model (known by comparison with numerical ground truth), or an intentionally wrong model, we develop different metrics for final evaluation, requiring a minimum of five evaluations per model $m_{k,i}$ to be successful:

*   **Possible metric A)** Use the average of all individual evaluation scores. This provides a continuous measure of model quality, where higher averages indicate better agreement with simulation results.
*   **Metric B)** In the present paper, however, we focus on metric B) which uses the number of individual evaluation scores $v_{k,i,j} \le 0.5$ as a binary classification criterion. If a sufficient number of evaluation scores fall below this threshold, the model is classified as incorrect.

The metric B is based on the assumption that not all evaluation methods are equally sensitive to errors. Some aspects of the simulation may appear physically plausible even for a flawed model. For instance, the motion might still appear planar, even if the force directions or model parameters are incorrectly set. Therefore, relying on multiple evaluations increases robustness. Thus, we use a threshold-based decision rule: if more than $n_{\text{fails}}$ out of $n_e$ scores $\le 0.5$ (i.e., fail), the model is classified as incorrect. Empirically, we found $n_{\text{fails}} \in \{1, 2\}$ to be suitable “fails thresholds” for our experiments, see Table 5 for individual choices for different LLMs.

We apply this method to 140 different simulation scenarios in our virtual lab, consisting of 70 correct and 70 intentionally incorrect models. Each model undergoes $n_e \approx 8$ evaluation methods, leading to 960 scored evaluations for Table 5. We compute the evaluation metrics (confusion matrix):

*   True Positive (TP): correct model identified as correct
*   False Negative (FN): correct model identified as incorrect
*   False Positive (FP): intentionally incorrect model identified as correct
*   True Negative (TN): intentionally incorrect model identified as incorrect
*   $\text{F1-score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$

The well-known relations $\text{FPR} = \text{FP}/(\text{FP} + \text{TN})$, $\text{TPR} = \text{TP}/(\text{TP} + \text{FN})$, $\text{Recall} = \text{TP}/(\text{TP} + \text{FN})$, and $\text{Precision} = \text{TP}/(\text{TP} + \text{FP})$ are mentioned for completeness.

In order to ensure comparability, all validation experiments use the simulation code and evaluation methods produced by QwenCoder-32B-Q4, which showed consistently highest performance for code generation tasks. Table 5 presents the aggregated scores for different LLMs, indicating their ability to distinguish correct from incorrect models based on simulation output. In particular, we are interested in the FPR (false positive rate), which quantifies the risk of accepting an incorrect model as valid – a critical factor for safety and robustness in engineering applications. At the same time, we focus on the TPR (true positive rate), representing the proportion of trustworthy models that are correctly identified and thus can be reliably used by engineers or automated systems. Even though that TPR is only about 1/2 up to 2/3, we like to note that repeated generation may lead to a sufficient number of correct models. Finally, the F1-score shows the ability of a particular LLM to self-validate a certain model, ideally being 1. Thus, the F1-score itself is a metric to show the ability of an LLM to correctly evaluate simulation results based on the presented evaluation methods. Additionally, the “correct cases score”, which shows the averaged score for correct mechanical models may be used as another metric, as it should again achieve 1 with the best performing language model.

Among locally deployable models, Microsoft’s LLM Phi-4 demonstrates outstanding performance, outperforming larger models such as Llama3.1 70B in terms of F1-score and reliability, see Table 5. The best results overall were achieved using OpenAI’s GPT-4o accessed via API, achieving an F1-score of 0.72 and a low FPR of 0.09, making it already suitable for practical application in simulation model development and validation pipelines.

#### Table 5: Overview on final results of LLM agent regarding the ability to distinguish correct from wrong models; a total of 140 mechanical models have been evaluated, where 50% of the cases were correct and 50% have been intentionally made wrong.

| LLM name | eval. run time (min) | k-tokens generated | tokens per second | correct cases score | fails threshold | F1-score | FPR | TPR | TP | FN | FP | TN | non-decidable |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| FluentlyLM-Q4 | 595.3 | 478 | 27.4 | 0.81 | 1 | 0.53 | 0.35 | 0.49 | 28 | 29 | 20 | 37 | 26 |
| GPT-4o | 193.4 | 312 | 53.2 | 0.85 | 2 | 0.72 | 0.09 | 0.61 | 35 | 22 | 5 | 52 | 26 |
| Llama3.1-70B-HF | 619.7 | 182 | 10.1 | 0.68 | 2 | 0.58 | 0.21 | 0.49 | 28 | 29 | 12 | 45 | 26 |
| Llama3.3-70B-HF | 984.1 | 321 | 11.1 | 0.83 | 1 | 0.71 | 0.21 | 0.67 | 38 | 19 | 12 | 45 | 26 |
| Phi4-Q4 | 143.5 | 270 | 63.7 | 0.85 | 1 | 0.62 | 0.16 | 0.53 | 30 | 27 | 9 | 48 | 26 |
| Qwen2.5-32B-Q4 | 377.9 | 278 | 26.0 | 0.8 | 1 | 0.55 | 0.39 | 0.53 | 30 | 27 | 22 | 35 | 26 |
| Qwen2.5-72B-HF | 693.8 | 228 | 11.0 | 0.81 | 1 | 0.53 | 0.11 | 0.4 | 23 | 34 | 6 | 51 | 26 |
| QwenCoder-32B-Q4 | 348.7 | 284 | 27.8 | 0.8 | 2 | 0.65 | 0.29 | 0.62 | 35 | 21 | 16 | 40 | 28 |

---

## 4 Discussion

In general, our results show that LLMs are capable of generating Python code for simulation models that execute successfully and simulate correctly; some LLMs achieve very high scores regarding both code execution and model correctness. The automated evaluation of simulation model generation tasks using numerical ground truth proves extremely helpful for selecting appropriate LLMs for further tasks and for estimating their performance and capabilities in engineering applications. It has been demonstrated that the self-validation framework achieves sufficiently high scores to be considered useful. Notably, the number of true positives is substantially higher than the number of false negatives, indicating reliable performance in error detection.

Several characteristic error patterns and artifacts were identified in the LLM-generated models. For instance, the use of symbols such as $L$ (e.g., for a length parameter) led to significantly low performance as it was used but no value had been assigned, particularly with Phi-4. Geometric descriptions without accompanying figures (not considered in our framework) were frequently misinterpreted, especially with respect to local versus global coordinate systems, the positioning of centers of mass, and relative coordinates in joints.

Moreover, models often failed to fully adhere to the provided information and hints, particularly when distinguishing between reference configurations and initial conditions. A recurring error was the incorrect assumption that a free-falling mass point would interact with the ground, even if it was told that contact with ground shall be neglected. Consequently, in the test cases, the initial height was chosen sufficiently large to prevent contact with the ground during simulation.

Problems in determining the correct count of Degrees of Freedom (DOFs) were also observed, despite clear specifications that all mass points are modeled spatially with three DOFs. LLMs sometimes misinterpreted spring elements as constraints or incorrectly calculated DOFs. Therefore, evaluation methods based purely on DOFs assessment were not applied.

Another notable challenge involved the interpretation of directions: gravity was frequently assumed to act in the negative $y$ or $z$-direction, as they are common in simulations, even if explicitly stated different. Solver-related issues also occurred, particularly in randomized test cases where default solver settings were insufficient for convergence.

In order to balance token limitations and result precision, numerical ground truths were provided with reduced temporal resolution and limited to four significant digits. While generally effective, this sometimes obscured key effects, such as the decay behavior of a damped oscillator. In such cases, manual adjustment of the number of digits by the LLM would be beneficial.

An overarching difficulty encountered was that some model descriptions included commonly accepted, but not explicitly stated assumptions, leading to a lower performance, similar as with the problem of differentiation between reference and initial configurations. Although some LLMs were able to generate correct models by “intuitively” correct assumptions, such inconsistencies are hard to process automatically and represent an important area for future research and improvement. Without taking explicit notice, we assume that some generated simulation models were marked as incorrect due to differences with the numerical ground truth, but would be still acceptable as correct simulation models for practice.

We also like to note that we continuously refined the approaches and performed dozens of test runs with more than 40 different LLMs, leading to many 10 000s of generated models and hundreds of megabytes of data. Therefore, we could only sparsely perform human evaluation within the data – in particular for the best models, as even just for the final tests in Table 5 more than 2000 total erratic evaluations would have to be checked.

---

## 5 Conclusion

The specialized approach with in-context learning and a specific RAG-approach with tailored information gave remarkably high performance in automated simulation model generation with mass points, rigid bodies and joints.

More complex tasks, like flexible bodies, simulator coupling, complex contact problems or advanced user functions are tasks to be studied in the future, as available LLMs struggled with a few rigid bodies and joints.

Another approach would be to curate existing textual descriptions and simulation models of Exudyn and to synthetically generate a larger set of samples for finetuning of existing LLMs. However, basic tests showed that the in-context approach was more reliable than using specifically trained LLMs.

Our successful approach may shift integration of AI to simulation and modeling of mechanical systems to the next level. While we model commonly known mechanical models, future approaches could even be used for optimization or research tasks in order to solve open engineering problems.

---

## Declarations

*   **Funding:** Not applicable.
*   **Competing interests:** Not applicable.
*   **Ethics approval and consent to participate:** Not applicable.
*   **Code and data availability:** The LLM-based code generation, evaluation and self-validation code is available on GitHub: [https://github.com/jgerstmayr/AI-engineering-lab](https://github.com/jgerstmayr/AI-engineering-lab)
*   **Usage of AI in the present paper:** Being part of the research in this paper, LLMs have been used for code generation and as AI agents; apart from that, we used LLMs for spell-checking, text improvement and translation from our mother tongue to English.
*   **Author contributions:** J.G. contributed to conceptualization, methodology, software development, investigation, visualization, and writing – review and editing; P.M. software development, visualization, and writing – review and editing; T.M. conceptualization, methodology, software development, investigation, visualization, and writing – review and editing; M.P. software development, visualization, and writing – review and editing.

---

## References

[1] Abdin, M., Aneja, J., Behl, H., Bubeck, S., Eldan, R., Gunasekar, S., Harrison, M., Hewett, R.J., Javaheripi, M., Kauffmann, P., *et al.*: Phi-4 technical report. arXiv preprint (2024) [https://doi.org/10.48550/arXiv.2412.08905](https://doi.org/10.48550/arXiv.2412.08905)

[2] Anand, Y., Nussbaum, Z., Treat, A., Miller, A., Guo, R., Schmidt, B., Community, G., Duderstadt, B., Mulyar, A.: GPT4All: An Ecosystem of Open Source Compressed Language Models (2023). [https://doi.org/10.48550/arXiv.2311.04931](https://doi.org/10.48550/arXiv.2311.04931)

[3] Anthropic, A.: The Claude 3 model family: Opus, Sonnet, Haiku. Claude-3 Model Card (2024). online, accessed 17.4.2025

[4] Bran, A.M., Cox, S., Schilter, O., Baldassari, C., White, A.D., Schwaller, P.: Chemcrow: Augmenting large-language models with chemistry tools. arXiv preprint (2023) [https://doi.org/10.48550/arXiv.2304.05376](https://doi.org/10.48550/arXiv.2304.05376)

[5] Baumann, A., Eberhard, P.: Experiments with large language models on retrieval-augmented generation for closed-source simulation software. arXiv preprint (2025) [https://doi.org/10.48550/arXiv.2502.03916](https://doi.org/10.48550/arXiv.2502.03916)

[6] De Vries, H.J., Blind, K., Mangelsdorf, A.: Standards and innovation: A review and introduction to the special issue. Research Policy **52**(8), 104854 (2023) [https://doi.org/10.1016/j.respol.2023.104854](https://doi.org/10.1016/j.respol.2023.104854)

[7] Du, X., Yao, Y., Ma, K., Wang, B., Zheng, T., Zhu, K., Liu, M., Liang, Y., Jin, X., Wei, Z., *et al.*: SuperGPQA: Scaling LLM evaluation across 285 graduate disciplines. arXiv preprint (2025) [https://doi.org/10.48550/arXiv.2502.14739](https://doi.org/10.48550/arXiv.2502.14739)

[8] Dettmers, T., Zettlemoyer, L.: The case for 4-bit precision: k-bit inference scaling laws. In: International Conference on Machine Learning, pp. 7750–7774 (2023). [https://doi.org/10.48550/arXiv.2212.09720](https://doi.org/10.48550/arXiv.2212.09720) . PMLR

[9] Extance, A.: ChatGPT has entered the classroom: how LLMs could transform education. Nature **623**, 474–477 (2023) [https://doi.org/10.1038/d41586-023-03507-3](https://doi.org/10.1038/d41586-023-03507-3)

[10] Frantar, E., Ashkboos, S., Hoefler, T., Alistarh, D.: GPTQ: Accurate Post-Training Quantization for Generative Pre-Trained Transformers. In: The Eleventh International Conference on Learning Representations (2022). [https://doi.org/10.48550/arXiv.2210.17323](https://doi.org/10.48550/arXiv.2210.17323)

[11] Frenkel, M.E., Emara, H.: ChatGPT-3.5 and -4.0 and mechanical engineering: Examining performance on the FE mechanical engineering and undergraduate exams. Computer Applications in Engineering Education **32**(6), 22781 (2024) [https://doi.org/10.1002/cae.22781](https://doi.org/10.1002/cae.22781)

[12] Grattafiori, A., Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, A., Letman, A., Mathur, A., Schelten, A., Vaughan, A., *et al.*: The Llama 3 herd of models. arXiv preprint (2024) [https://doi.org/10.48550/arXiv.2407.21783](https://doi.org/10.48550/arXiv.2407.21783)

[13] Gerstmayr, J.: Exudyn–a C++-based Python package for flexible multibody systems. Multibody System Dynamics **60**(4), 533–561 (2024) [https://doi.org/10.1007/s11044-023-09937-1](https://doi.org/10.1007/s11044-023-09937-1)

[14] Gerstmayr, J., Manzl, P., Pieber, M.: Multibody models generated from natural language. Multibody System Dynamics **62**, 249–271 (2024) [https://doi.org/10.48550/arXiv.2404.01413](https://doi.org/10.48550/arXiv.2404.01413)

[15] Google, G.T.: Gemini: A Family of Highly Capable Multimodal Models (2024). [https://doi.org/10.48550/arXiv.2312.11805](https://doi.org/10.48550/arXiv.2312.11805)

[16] Grindrod, J.: Large language models and linguistic intentionality. Synthese **204**(71) (2024) [https://doi.org/10.1007/s11229-024-04723-8](https://doi.org/10.1007/s11229-024-04723-8)

[17] Guo, D., Yang, D., Zhang, H., Song, J., Zhang, R., Xu, R., Zhu, Q., Ma, S., Wang, P., Bi, X., *et al.*: Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint (2025) [https://doi.org/10.48550/arXiv.2501.12948](https://doi.org/10.48550/arXiv.2501.12948)

[18] Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., Steinhardt, J.: Measuring massive multitask language understanding. In: International Conference on Learning Representations (2021). [https://doi.org/10.48550/arXiv.2009.03300](https://doi.org/10.48550/arXiv.2009.03300)

[19] Hendrycks, D., Basart, S., Kadavath, S., Mazeika, M., Arora, A., Guo, E., Burns, C., Puranik, S., He, H., Song, D., Steinhardt, J.: Measuring Coding Challenge Competence With APPS. NeurIPS (2021) [https://doi.org/10.48550/arXiv.2105.09938](https://doi.org/10.48550/arXiv.2105.09938)

[20] Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart, S., Tang, E., Song, D., Steinhardt, J.: Measuring mathematical problem solving with the math dataset. In: Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (2021). [https://doi.org/10.48550/arXiv.2103.03874](https://doi.org/10.48550/arXiv.2103.03874)

[21] Jones, C.R., Bergen, B.K.: Large language models pass the Turing test. arXiv preprint (2025) [https://doi.org/10.48550/arXiv.2503.23674](https://doi.org/10.48550/arXiv.2503.23674)

[22] Jiang, A.Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D.S., Casas, D., Bou Hanna, E., Bressand, F., Lengyel, G., Guillaume, B., Lample, G., Lavaud, L.R., *et al.*: Mistral 7b. arXiv preprint (2023) [https://doi.org/10.48550/arXiv.2310.06825](https://doi.org/10.48550/arXiv.2310.06825)

[23] Kashefi, A., Mukerji, T.: ChatGPT for programming numerical methods. Journal of Machine Learning for Modeling and Computing **4**(2) (2023) [https://doi.org/10.1615/JMachLearnModelComput.2023048492](https://doi.org/10.1615/JMachLearnModelComput.2023048492)

[24] Lin, C.-Y.: ROUGE: A package for automatic evaluation of summaries. In: Text Summarization Branches Out, pp. 74–81. Association for Computational Linguistics, Barcelona, Spain (2004). [https://aclanthology.org/W04-1013](https://aclanthology.org/W04-1013)

[25] Liang, H., Kalaleh, M.T., Mei, Q.: Integrating large language models for automated structural analysis. arXiv preprint (2025) [https://doi.org/10.48550/arXiv.2504.09754](https://doi.org/10.48550/arXiv.2504.09754)

[26] Lai, Y., Li, C., Wang, Y., Zhang, T., Zhong, R., Zettlemoyer, L., Yih, W.-t., Fried, D., Wang, S., Yu, T.: DS-1000: a natural and reliable benchmark for data science code generation. In: Proceedings of the 40th International Conference on Machine Learning. ICML’23 (2023). [https://doi.org/10.48550/arXiv.2211.11501](https://doi.org/10.48550/arXiv.2211.11501)

[27] Lei, Y., Yang, B., Jiang, X., Jia, F., Li, N., Nandi, A.K.: Applications of machine learning to machine fault diagnosis: A review and roadmap. Mechanical Systems and Signal Processing **138** (2020) [https://doi.org/10.1016/j.ymssp.2019.106587](https://doi.org/10.1016/j.ymssp.2019.106587)

[28] Ni, B., Buehler, M.J.: Mechagents: Large language model multi-agent collaborations can solve mechanics problems, generate new data, and integrate knowledge. Extreme Mechanics Letters **67**, 102131 (2024) [https://doi.org/10.1016/j.eml.2024.102131](https://doi.org/10.1016/j.eml.2024.102131)

[29] OpenAI, Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F.L., Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S., *et al.*: GPT-4 Technical Report (2023). [https://doi.org/10.48550/arXiv.2303.08774](https://doi.org/10.48550/arXiv.2303.08774)

[30] OpenAI: Learning to reason with LLMs. Technical report (2024). [https://openai.com/index/learning-to-reason-with-llms](https://openai.com/index/learning-to-reason-with-llms)

[31] Phan, L., Gatti, A., Han, Z., Li, N., Hu, J., Zhang, H., Zhang, C.B.C., Shaaban, M., Ling, J., Shi, S., *et al.*: Humanity’s last exam. arXiv preprint (2025) [https://doi.org/10.48550/arXiv.2501.14249](https://doi.org/10.48550/arXiv.2501.14249)

[32] Peng, S., Kalliamvakou, E., Cihon, P., Demirer, M.: The impact of AI on developer productivity: Evidence from GitHub Copilot. arXiv preprint (2023) [https://doi.org/10.48550/arXiv.2302.06590](https://doi.org/10.48550/arXiv.2302.06590)

[33] Putta, P., Mills, E., Garg, N., Motwani, S., Finn, C., Garg, D., Rafailov, R.: Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents (2024). [https://doi.org/10.48550/arXiv.2408.07199](https://doi.org/10.48550/arXiv.2408.07199)

[34] Papineni, K., Roukos, S., Ward, T., Zhu, W.-J.: BLEU: a method for automatic evaluation of machine translation. In: Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics, pp. 311–318. Association for Computational Linguistics, Philadelphia, Pennsylvania, USA (2002). [https://doi.org/10.3115/1073083.1073135](https://doi.org/10.3115/1073083.1073135)

[35] Pryamikov, A.: Deep learning as a highly efficient tool for digital signal processing design. Light: Science & Applications **13** (2024) [https://doi.org/10.1038/s41377-024-01599-8](https://doi.org/10.1038/s41377-024-01599-8)

[36] Pandey, S., Xu, R., Wang, W., Chu, X.: OpenFOAMGPT: A retrieval-augmented large language model (LLM) agent for OpenFOAM-based computational fluid dynamics. Physics of Fluids **37**(3) (2025) [https://doi.org/10.1063/5.0257555](https://doi.org/10.1063/5.0257555)

[37] Qin, Y., Liang, S., Ye, Y., Zhu, K., Yan, L., Lu, Y., Lin, Y., Cong, X., Tang, X., Qian, B., *et al.*: ToolLLM: Facilitating large language models to master 16000+ real-world APIs. In: The Twelfth International Conference on Learning Representations (2023). [https://doi.org/10.48550/arXiv.2307.16789](https://doi.org/10.48550/arXiv.2307.16789)

[38] Rein, D., Hou, B.L., Stickland, A.C., Petty, J., Pang, R.Y., Dirani, J., Michael, J., Bowman, S.R.: GPQA: A graduate-level Google-proof Q&A benchmark. In: First Conference on Language Modeling (2024). [https://doi.org/10.48550/arXiv.2311.12022](https://doi.org/10.48550/arXiv.2311.12022)

[39] Russell, S.J., Norvig, P.: Artificial Intelligence: A Modern Approach, pp. 874–906. Pearson, USA (2016)

[40] Soori, M., Arezoo, B., Dastres, R.: Artificial intelligence, machine learning and deep learning in advanced robotics, a review. Cognitive Robotics **3**, 54–70 (2023) [https://doi.org/10.1016/j.cogr.2023.04.001](https://doi.org/10.1016/j.cogr.2023.04.001)

[41] Shi, Z., Xin, C., Huo, T., Jiang, Y., Wu, B., Chen, X., Qin, W., Ma, X., Huang, G., Wang, Z., *et al.*: A fine-tuned large language model based molecular dynamics agent for code generation to obtain material thermodynamic parameters. Scientific Reports **15**(1), 10295 (2025) [https://doi.org/10.1038/s41598-025-92337-6](https://doi.org/10.1038/s41598-025-92337-6)

[42] Wolf, T., Debut, L., Sanh, V., Chaumond, J., Delangue, C., Moi, A., Cistac, P., Rault, T., Louf, R., Funtowicz, M., Davison, J., Shleifer, S., Platen, P., Ma, C., Jernite, Y., Plu, J., Xu, C., Le Scao, T., Gugger, S., Drame, M., Lhoest, Q., Rush, A.: Transformers: State-of-the-art natural language processing. In: Liu, Q., Schlangen, D. (eds.) Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations, pp. 38–45. Association for Computational Linguistics, Online (2020). emnlp-demos.6

[43] Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., *et al.*: A survey on large language model based autonomous agents. Frontiers of Computer Science **18**(6), 186345 (2024) [https://doi.org/10.1007/s11704-024-40231-1](https://doi.org/10.1007/s11704-024-40231-1)

[44] Wang, Y., Ma, X., Zhang, G., Ni, Y., Chandra, A., Guo, S., Ren, W., Arulraj, A., He, X., Jiang, Z., Li, T., Ku, M., Wang, K., Zhuang, A., Fan, R., Yue, X., Chen, W.: MMLU-Pro: A more robust and challenging multi-task language understanding benchmark. In: The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track (NeurIPS) (2024). [https://doi.org/10.48550/arXiv.2406.01574](https://doi.org/10.48550/arXiv.2406.01574)

[45] Wang, A., Pruksachatkun, Y., Nangia, N., Singh, A., Michael, J., Hill, F., Levy, O., Bowman, S.: SuperGLUE: A stickier benchmark for general-purpose language understanding systems. Advances in neural information processing systems **32** (2019) [https://doi.org/10.48550/arXiv.1905.00537](https://doi.org/10.48550/arXiv.1905.00537)

[46] Wang, A., Singh, A., Michael, J., Hill, F., Levy, O., Bowman, S.R.: GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding (2019). [https://doi.org/10.48550/arXiv.1804.07461](https://doi.org/10.48550/arXiv.1804.07461)

[47] Wang, J., Zhang, H., Unjhawala, H.M., Negrut, P., Wang, S., Slaton, K., Serban, R., Wu, J.-L., Negrut, D.: SimBench: A Rule-Based Multi-Turn Interaction Benchmark for Evaluating an LLM’s Ability to Generate Digital Twins (2024). [https://doi.org/10.48550/arXiv.2408.11987](https://doi.org/10.48550/arXiv.2408.11987)

[48] Yujian, L., Bo, L.: A normalized Levenshtein distance metric. IEEE Transactions on Pattern Analysis and Machine Intelligence **29**(6), 1091–1095 (2007) [https://doi.org/10.1109/TPAMI.2007.1078](https://doi.org/10.1109/TPAMI.2007.1078)

[49] Yan, F., Mao, H., Ji, C.C.-J., Zhang, T., Patil, S.G., Stoica, I., Gonzalez, J.E.: Berkeley Function Calling Leaderboard. [https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html) (2024)

[50] Yao, S., Shinn, N., Razavi, P., Narasimhan, K.: *tau*-bench: A benchmark for tool-agent-user interaction in real-world domains. arXiv preprint (2024) [https://doi.org/10.48550/arXiv.2406.12045](https://doi.org/10.48550/arXiv.2406.12045)

[51] Zellers, R., Bisk, Y., Schwartz, R., Choi, Y.: Swag: A large-scale adversarial dataset for grounded commonsense inference. In: Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, pp. 93–104 (2018). [https://doi.org/10.18653/v1/D18-1009](https://doi.org/10.18653/v1/D18-1009)

[52] Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E.P., Zhang, H., Gonzalez, J.E., Stoica, I.: Judging llm-as-a-judge with mt-bench and chatbot arena. In: Proceedings of the 37th International Conference on Neural Information Processing Systems. NIPS ’23. Curran Associates Inc., Red Hook, NY, USA (2023). [https://doi.org/10.48550/arXiv.2306.05685](https://doi.org/10.48550/arXiv.2306.05685)

[53] Zellers, R., Holtzman, A., Bisk, Y., Farhadi, A., Choi, Y.: HellaSwag: Can a machine really finish your sentence? In: Korhonen, A., Traum, D., M`arquez, L. (eds.) Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, pp. 4791–4800. Association for Computational Linguistics, Florence, Italy (2019). [https://doi.org/10.48550/arXiv.1905.07830](https://doi.org/10.48550/arXiv.1905.07830)

[54] Zhou, J., Lu, T., Mishra, S., Brahma, S., Basu, S., Luan, Y., Zhou, D., Hou, L.: Instruction-following evaluation for large language models. arXiv preprint (2023) [https://doi.org/10.48550/arXiv.2311.07911](https://doi.org/10.48550/arXiv.2311.07911)
```