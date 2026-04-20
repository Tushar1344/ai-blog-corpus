# Post-training & Fine-tuning

RLHF, RLAIF, RLVR, DPO, SFT, LoRA, on-policy distillation, reward modeling, preference optimization.

**Post count:** 39

**Contributors:**

- Hugging Face: 11
- OpenAI: 9
- Databricks Mosaic AI: 7
- Allen Institute for AI: 5
- Meta AI / FAIR: 2
- Google DeepMind: 2
- Anthropic: 1
- Thinking Machines: 1
- Google Research: 1

**Subcategories:**

- [RLVR & verifiable-reward RL](#rlvr-verifiable-rewards) (4)
- [Classic RLHF (PPO, reward models)](#rlhf-classic) (13)
- [Direct preference (DPO, KTO, ORPO, SimPO)](#direct-preference) (1)
- [SFT & instruction tuning](#sft-and-instruction-tuning) (13)
- [Distillation](#distillation) (5)

---

## <a id="rlvr-verifiable-rewards"></a>RLVR & verifiable-reward RL

_4 posts_

### The Power of RLVR: Training a Leading SQL Reasoning Model on Databricks

- **ID:** `dbx-r-power-rlvr-training-leading-sql-reasoning-model-databricks`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/power-rlvr-training-leading-sql-reasoning-model-databricks
- **Date:** 2025-07-30
- **Track:** research
- **Contribution type:** new-method
- **Techniques:** RLVR

_Summary pending — see link for details._


### 🐯 Liger GRPO meets TRL

- **ID:** `hf-r-liger-grpo`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/liger-grpo
- **Date:** 2025-05-25
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### TAO: Using test-time compute to train efficient LLMs without labeled data

- **ID:** `dbx-r-tao-using-test-time-compute-train-efficient-llms-without-labeled-data`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/tao-using-test-time-compute-train-efficient-llms-without-labeled-data
- **Date:** 2025-03-25
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** test-time-compute

_Summary pending — see link for details._


### Improving mathematical reasoning with process supervision

- **ID:** `oai-r-improving-mathematical-reasoning-with-process-supervision`
- **Company:** OpenAI
- **Link:** https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/
- **Date:** 2023-10-19
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Shows process supervision (rewarding each reasoning step) beats outcome supervision on MATH
- Produces PRM800K dataset of step-level human feedback (released)
- Achieves new SOTA on MATH when used to rerank solutions
- Reports negative alignment tax — process supervision is both safer and more performant
- Matters as a landmark paper on step-level reward modeling for reasoning (precursor to modern PRMs).


## <a id="rlhf-classic"></a>Classic RLHF (PPO, reward models)

_13 posts_

### Agent Learning from Human Feedback (ALHF): A Databricks Knowledge Assistant Case Study

- **ID:** `dbx-r-agent-learning-human-feedback-alhf-databricks-knowledge-assistant-case-study`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/agent-learning-human-feedback-alhf-databricks-knowledge-assistant-case-study
- **Date:** 2025-08-04
- **Track:** research
- **Contribution type:** retrospective-case-study

_Summary pending — see link for details._


### Putting RL back in RLHF

- **ID:** `hf-r-putting_rl_back_in_rlhf_with_rloo`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/putting_rl_back_in_rlhf_with_rloo
- **Date:** 2024-06-12
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Fine-Grained Human Feedback

- **ID:** `dbx-r-fine-grained-human-feedback`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/fine-grained-human-feedback
- **Date:** 2024-02-27
- **Authors:** Prithviraj (Raj) Ammanabrolu
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Databricks/UW research on fine-grained RLHF using segment-level reward signals instead of holistic preferences
- Rewards are dense (per-sentence) and diverse (multiple reward models for factuality, relevance, toxicity)
- Shows higher inter-annotator agreement and cleaner data at lower labeling cost
- Adjusting reward model weights lets practitioners tailor LM behavior (e.g., short vs detailed outputs)
- Matters as improved RLHF recipe with more controllable outputs


### Aligning language models to follow instructions

- **ID:** `oai-r-instruction-following`
- **Company:** OpenAI
- **Link:** https://openai.com/index/instruction-following/
- **Date:** 2024-02-14
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- InstructGPT: fine-tunes GPT-3 via RLHF (supervised fine-tuning, reward model from human comparisons, PPO) to follow user instructions while being more truthful and less toxic
- Labelers prefer 1.3B InstructGPT outputs over 175B GPT-3 despite >100x fewer params
- Addresses 'alignment tax' by mixing in pretraining data during RL
- Deployed as default API models at the time
- Canonical reference for RLHF applied to instruction-following language models.


### Summarizing books with human feedback

- **ID:** `oai-r-summarizing-books`
- **Company:** OpenAI
- **Link:** https://openai.com/index/summarizing-books/
- **Date:** 2024-02-14
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Trains a book-summarization model via recursive task decomposition and human feedback (RLHF)
- Breaks book into sections, summarizes each, then summarizes summaries to produce whole-book summaries
- Targets scalable oversight for tasks too long for humans to evaluate end-to-end
- Shows RLHF scales to long-horizon tasks difficult to grade
- Matters as a proof-of-concept for scalable human oversight via recursive decomposition.


### The N Implementation Details of RLHF with PPO

- **ID:** `hf-r-the_n_implementation_details_of_rlhf_with_ppo`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/the_n_implementation_details_of_rlhf_with_ppo
- **Date:** 2023-10-24
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### StackLLaMA: A hands-on guide to train LLaMA with RLHF

- **ID:** `hf-r-stackllama`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/stackllama
- **Date:** 2023-04-05
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### What Makes a Dialog Agent Useful?

- **ID:** `hf-r-dialog-agents`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/dialog-agents
- **Date:** 2023-01-24
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- Survey-style post breaking down the techniques behind ChatGPT: RLHF, SFT, instruction fine-tuning (IFT), chain-of-thought, red teaming
- compares LaMDA, BlenderBot 3, Sparrow, ChatGPT/InstructGPT, and Anthropic Assistant on access, data, architecture, and eval
- synthesizes what is known and what remains open about making dialog agents useful
- classified as rlhf-classic because the core framing is the RLHF pipeline behind ChatGPT.


### Illustrating Reinforcement Learning from Human Feedback (RLHF)

- **ID:** `hf-r-rlhf`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/rlhf
- **Date:** 2022-12-09
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Proximal Policy Optimization (PPO)

- **ID:** `hf-r-deep-rl-ppo`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/deep-rl-ppo
- **Date:** 2022-08-05
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback

- **ID:** `ant-r-training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback
- **Date:** 2022-04-12
- **Track:** research
- **Contribution type:** new-method

_Summary pending — see link for details._


### Learning Through Human Feedback

- **ID:** `dm-r-learning-through-human-feedback`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/learning-through-human-feedback/
- **Date:** 2017-06-12
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- Foundational (2017) DeepMind+OpenAI collaboration demonstrating RL from human preferences: non-expert humans teach an RL agent complex goals (including backflips) by comparing short trajectory clips
- as little as 30 minutes of feedback can suffice
- removes need to hand-specify reward functions, which could otherwise be mis-specified with dangerous consequences
- canonical RLHF precursor paper, hence rlhf-classic.


### Learning to summarize with human feedback

- **ID:** `oai-r-learning-to-summarize-with-human-feedback`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-to-summarize-with-human-feedback/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


## <a id="direct-preference"></a>Direct preference (DPO, KTO, ORPO, SimPO)

_1 posts_

### Fine-tune Llama 2 with DPO

- **ID:** `hf-r-dpo-trl`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/dpo-trl
- **Date:** 2023-08-08
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="sft-and-instruction-tuning"></a>SFT & instruction tuning

_13 posts_

### MemAlign: Building Better LLM Judges From Human Feedback With Scalable Memory

- **ID:** `dbx-r-memalign-building-better-llm-judges-human-feedback-scalable-memory`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/memalign-building-better-llm-judges-human-feedback-scalable-memory
- **Date:** 2026-02-03
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Databricks introduces MemAlign, a framework that aligns LLM judges with human feedback using a lightweight dual-memory system instead of fine-tuning or prompt optimization
- Needs only a handful of natural-language feedback examples, beats SOTA prompt optimizers at orders-of-magnitude lower cost ($0.03 vs $1-5) and latency
- Introduces memory scaling: quality improves as feedback accumulates without re-optimization
- Available in open-source MLflow
- Matters for scaling domain-specific LLM-as-judge alignment in enterprise agent evaluation


### Dr Tulu

- **ID:** `ai2-r-dr-tulu`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/dr-tulu
- **Date:** 2025-11-18
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### The Power of Fine-Tuning on Your Data: Quick Fixing Bugs with LLMs via Never Ending Learning (NEL)

- **ID:** `dbx-r-power-fine-tuning-your-data-quick-fixing-bugs-llms-never-ending-learning-nel`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/power-fine-tuning-your-data-quick-fixing-bugs-llms-never-ending-learning-nel
- **Date:** 2025-04-08
- **Authors:** Samantha Banchik|Ta-Chung Chi|Sam Havens|Dipendra Misra|Will Tipton|Jan van der Vegt|Matei Zaharia|Emanuel Zgraggen
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Databricks fine-tunes Llama 3.1 8B Instruct on internal telemetry-code interaction data for a Quick Fix program-repair agent
- Live A/B test shows fine-tuned Llama delivers 1.4x higher acceptance rate vs GPT-4o and 2x lower inference latency
- Introduces Never Ending Learning (NEL) paradigm for continuously learning from user interactions
- Demonstrates small open-source LLMs fine-tuned on org-specific data beat frontier models
- Matters as blueprint for enterprise code-assistant customization


### Introducing the Synthetic Data Generator - Build Datasets with Natural Language

- **ID:** `hf-r-synthetic-data-generator`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/synthetic-data-generator
- **Date:** 2024-12-16
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- HF launches Synthetic Data Generator: no-code UI that turns a natural-language description into a custom dataset using distilabel and HF text-generation API
- current tasks are text classification (requires categories) and chat datasets (conversations), with eval/RAG planned
- target is making dataset creation accessible to non-technical users in minutes
- classified as SFT/instruction-tuning since the generated datasets feed supervised fine-tuning pipelines.


### Tulu 3

- **ID:** `ai2-r-tulu-3`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/tulu-3
- **Date:** 2024-11-21
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Tulu 3 Technical

- **ID:** `ai2-r-tulu-3-technical`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/tulu-3-technical
- **Date:** 2024-11-21
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### LIMIT: Less Is More for Instruction Tuning

- **ID:** `dbx-r-limit-less-more-instruction-tuning`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/limit-less-more-instruction-tuning
- **Date:** 2024-02-10
- **Authors:** Aditi Jha|Jacob Portes
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** fine-tuning

_Summary pending — see link for details._


### Camels In A Changing Climate Enhancing Lm Adaptation With Tulu 2 0Eb692698A78

- **ID:** `ai2-r-camels-in-a-changing-climate-enhancing-lm-adaptation-with-tulu-2-0eb692698a78`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/camels-in-a-changing-climate-enhancing-lm-adaptation-with-tulu-2-0eb692698a78
- **Date:** 2023-12-08
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### On first-order meta-learning algorithms

- **ID:** `oai-r-on-first-order-meta-learning-algorithms`
- **Company:** OpenAI
- **Link:** https://openai.com/index/on-first-order-meta-learning-algorithms/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Formal paper accompanying Reptile: analyzes first-order meta-learning algorithms that only use first-order derivatives for meta-updates
- Generalizes first-order MAML and introduces Reptile (sample task, train, move initialization toward trained weights)
- Theoretical analysis of why these simple algorithms work on few-shot classification benchmarks
- Meta-learning foundations paper.


### Creating Interactive Agents With Imitation Learning

- **ID:** `dm-r-creating-interactive-agents-with-imitation-learning`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/creating-interactive-agents-with-imitation-learning/
- **Date:** 2021-12-08
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- DeepMind presents MIA (Multimodal Interactive Agent), trained via imitation learning in a 3D 'Playhouse' environment where humans and agents interact by locomoting, manipulating objects, and chatting
- extends Abramson et al. 2020 by combining vision, language, navigation, and manipulation
- produces a behavioral prior intended for later human-feedback refinement
- SFT-style imitation learning on human-agent interaction traces, hence sft-and-instruction-tuning.


### Third-person imitation learning

- **ID:** `oai-r-third-person-imitation-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/third-person-imitation-learning/
- **Date:** 2019-10-15
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- 2017 OpenAI paper on unsupervised third-person imitation learning for RL — learning a task from observing a teacher in a different viewpoint without state correspondence
- Uses domain-confusion techniques to produce viewpoint-agnostic features
- Addresses difficulty of collecting first-person demonstrations for robotics/RL
- Experiments on pointmass, reacher, inverted pendulum domains
- Historical classical-RL imitation-learning work.


### Reptile: A scalable meta-learning algorithm

- **ID:** `oai-r-reptile`
- **Company:** OpenAI
- **Link:** https://openai.com/index/reptile/
- **Date:** 2019-10-15
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Reptile: a simple first-order meta-learning algorithm — repeatedly sample a task, SGD on it, move initialization toward the trained weights
- Similar to first-order MAML but only needs black-box access to an SGD/Adam optimizer, with less computation/memory
- Analysis via Taylor expansion shows Reptile maximizes inner-product of gradients from different minibatches of the same task (improved generalization)
- Matches MAML on Omniglot and Mini-ImageNet few-shot benchmarks
- Influential meta-learning / initialization-finding method.


### Tulu 2

- **ID:** `ai2-r-tulu-2`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/tulu-2
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="distillation"></a>Distillation

_5 posts_

### On-Policy Distillation

- **ID:** `tm-r-on-policy-distillation`
- **Company:** Thinking Machines
- **Link:** https://thinkingmachines.ai/blog/on-policy-distillation/
- **Date:** 2025-10-27
- **Authors:** Kevin Lu
- **Track:** research
- **Contribution type:** position-policy
- **Techniques:** distillation

**Summary:**

- Thinking Machines post on on-policy distillation: sampling trajectories from the student model and using a strong teacher to grade each token, combining RL's on-policy relevance with distillation's dense reward
- Contrasts off-policy SFT distillation (teacher trajectories, suffers from distribution shift) vs. on-policy RL (sparse reward)
- Uses reverse KL per-token loss and the Tinker training API
- Replicates Qwen3's reasoning result at a fraction of RL cost and applies method to math reasoning and assistant training with domain knowledge
- Inspired by DAGGER and process reward modeling.


### Synthetic data: save money, time and carbon with open source

- **ID:** `hf-r-synthetic-data-save-costs`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/synthetic-data-save-costs
- **Date:** 2024-02-16
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- Case study: use an open-source LLM to generate synthetic labels, then train a small RoBERTa student on financial-sentiment task
- resulting model matches GPT-4 accuracy (94%, 0.94 F1) while costing $2.7 vs $3061, with 0.12 kg vs ~735-1100 kg CO2 and 0.13s latency
- argues synthetic-data distillation combines LLM convenience with specialized-model efficiency and control
- classified as distillation since the workflow is teacher-LLM -> student classifier.


### Open-sourcing Knowledge Distillation Code and Weights of SD-Small and SD-Tiny

- **ID:** `hf-r-sd_distillation`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/sd_distillation
- **Date:** 2023-08-01
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Training Machine Learning Models More Efficiently with Dataset Distillation

- **ID:** `gr-r-training-machine-learning-models-more-efficiently-with-dataset-distillation`
- **Company:** Google Research
- **Link:** https://research.google/blog/training-machine-learning-models-more-efficiently-with-dataset-distillation/
- **Date:** 2021-12-15
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Data Distillation Makes Omni Supervised Learning Possible

- **ID:** `meta-r-data-distillation-makes-omni-supervised-learning-possible`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/data-distillation-makes-omni-supervised-learning-possible/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._

