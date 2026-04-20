# Post-training & Fine-tuning

RLHF, RLAIF, RLVR, DPO, SFT, LoRA, on-policy distillation, reward modeling, preference optimization.

**Post count:** 40

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
- LangChain: 1

**Subcategories:**

- [RLVR & verifiable-reward RL](#rlvr-verifiable-rewards) (3)
- [Classic RLHF (PPO, reward models)](#rlhf-classic) (8)
- [Direct preference (DPO, KTO, ORPO, SimPO)](#direct-preference) (1)
- [SFT & instruction tuning](#sft-and-instruction-tuning) (6)
- [Distillation](#distillation) (4)
- [Other post-training](#fallback-post-training) (18)

---

## <a id="rlvr-verifiable-rewards"></a>RLVR & verifiable-reward RL

_3 posts_

### The Power of RLVR: Training a Leading SQL Reasoning Model on Databricks

- **ID:** `dbx-r-power-rlvr-training-leading-sql-reasoning-model-databricks`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/power-rlvr-training-leading-sql-reasoning-model-databricks
- **Date:** 2025-07-30
- **Track:** research
- **Contribution type:** new-method
- **Signal:** H — L=H/N=H/A=H (priority 9.9)
- **Techniques:** RLVR

**Summary:**

- Databricks applies RLVR (RL with Verifiable Rewards) to train SOTA text-to-SQL model on BIRD benchmark
- Starting from Qwen2.5-32B-Coder-Instruct, achieved 73.5% (new SOTA single-model single-generation track, up from 71.8%)
- Used their standard RLVR stack with no proprietary augmentation, combined with TAO offline RL
- Later update (Aug 2025): adding self-consistency tops BIRD overall category
- Takeaway: RLVR is a powerful baseline for any verifiable-reward domain and is rolling out in Agent Bricks


### 🐯 Liger GRPO meets TRL

- **ID:** `hf-r-liger-grpo`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/liger-grpo
- **Date:** 2025-05-25
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- HF/Axolotl integrate Liger Kernel chunked loss into TRL's GRPOTrainer, cutting peak memory 40% during GRPO training with zero quality drop
- Trick: chunk inputs to lm_head and compute per-chunk gradients during forward pass to avoid storing full logits in memory
- FSDP and PEFT support added, enabling 1.5-1.8x larger batch sizes across Qwen3 model sizes with LoRA/QLoRA
- Verified on Qwen3-0.6B + gsm8k: rewards track standard TRL curves
- Enable with `use_liger_loss=True` in GRPOConfig
- vLLM integration for fast rollouts


### TAO: Using test-time compute to train efficient LLMs without labeled data

- **ID:** `dbx-r-tao-using-test-time-compute-train-efficient-llms-without-labeled-data`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/tao-using-test-time-compute-train-efficient-llms-without-labeled-data
- **Date:** 2025-03-25
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=H (priority 9.9)
- **Techniques:** test-time-compute

**Summary:**

- TAO tunes LLMs with only unlabeled enterprise usage data using RL + test-time compute for reward signal
- Outperforms supervised fine-tuning with thousands of labels on FinanceBench, DB Enterprise Arena, BIRD-SQL
- Brings Llama-quality close to expensive proprietary models without label collection
- Part of Databricks' Data Intelligence program
- Highly actionable tuning method for enterprises lacking labels


## <a id="rlhf-classic"></a>Classic RLHF (PPO, reward models)

_8 posts_

### Agent Learning from Human Feedback (ALHF): A Databricks Knowledge Assistant Case Study

- **ID:** `dbx-r-agent-learning-human-feedback-alhf-databricks-knowledge-assistant-case-study`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/agent-learning-human-feedback-alhf-databricks-knowledge-assistant-case-study
- **Date:** 2025-08-04
- **Track:** research
- **Contribution type:** retrospective-case-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Putting RL back in RLHF

- **ID:** `hf-r-putting_rl_back_in_rlhf_with_rloo`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/putting_rl_back_in_rlhf_with_rloo
- **Date:** 2024-06-12
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### The N Implementation Details of RLHF with PPO

- **ID:** `hf-r-the_n_implementation_details_of_rlhf_with_ppo`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/the_n_implementation_details_of_rlhf_with_ppo
- **Date:** 2023-10-24
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### StackLLaMA: A hands-on guide to train LLaMA with RLHF

- **ID:** `hf-r-stackllama`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/stackllama
- **Date:** 2023-04-05
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=L/A=H (priority 7.5)

**Summary:**

- Hands-on guide training LLaMA-7B on StackExchange with full RLHF pipeline (SFT + reward modeling + PPO), released as StackLLaMA model via TRL library
- StackExchange score derived as log2(1+upvotes) rounded + 1 if accepted, up to 10 pairs per question for reward modeling
- Efficient training via PEFT/LoRA + 8-bit loading (~1.2-1.4GB/B params), packing for SFT (concatenate texts with EOS, cut to context size)
- Data parallelism via accelerate or torchrun for multi-GPU training
- Rule-of-thumb memory math: bf16 7B needs ~70GB with Adam
- Canonical pre-smolagents RLHF tutorial


### Illustrating Reinforcement Learning from Human Feedback (RLHF)

- **ID:** `hf-r-rlhf`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/rlhf
- **Date:** 2022-12-09
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Proximal Policy Optimization (PPO)

- **ID:** `hf-r-deep-rl-ppo`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/deep-rl-ppo
- **Date:** 2022-08-05
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback

- **ID:** `ant-r-training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback
- **Date:** 2022-04-12
- **Track:** research
- **Contribution type:** new-method
- **Signal:** H — L=H/N=M/A=M (priority 7.7)

**Summary:**

- Classic Anthropic RLHF paper: preference modeling + RL to make helpful, harmless assistants
- Alignment training improves performance on almost all NLP evals and is compatible with specialized skills
- Iterated online RLHF with weekly cadence of fresh data yields continuous improvements
- Identifies roughly linear relation between RL reward and sqrt(KL divergence from init)
- Foundational RLHF reference alongside OpenAI's InstructGPT.


### Learning to summarize with human feedback

- **ID:** `oai-r-learning-to-summarize-with-human-feedback`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-to-summarize-with-human-feedback/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

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
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


## <a id="sft-and-instruction-tuning"></a>SFT & instruction tuning

_6 posts_

### LIMIT: Less Is More for Instruction Tuning

- **ID:** `dbx-r-limit-less-more-instruction-tuning`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/limit-less-more-instruction-tuning
- **Date:** 2024-02-10
- **Authors:** Aditi Jha|Jacob Portes
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)
- **Techniques:** fine-tuning

_Summary pending — see link for details._


### Camels In A Changing Climate Enhancing Lm Adaptation With Tulu 2 0Eb692698A78

- **ID:** `ai2-r-camels-in-a-changing-climate-enhancing-lm-adaptation-with-tulu-2-0eb692698a78`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/camels-in-a-changing-climate-enhancing-lm-adaptation-with-tulu-2-0eb692698a78
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Dr Tulu

- **ID:** `ai2-r-dr-tulu`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/dr-tulu
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Tulu 2

- **ID:** `ai2-r-tulu-2`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/tulu-2
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Tulu 3

- **ID:** `ai2-r-tulu-3`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/tulu-3
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Tulu 3 Technical

- **ID:** `ai2-r-tulu-3-technical`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/tulu-3-technical
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


## <a id="distillation"></a>Distillation

_4 posts_

### On-Policy Distillation

- **ID:** `tm-r-on-policy-distillation`
- **Company:** Thinking Machines
- **Link:** https://thinkingmachines.ai/blog/on-policy-distillation/
- **Date:** 2025-10-27
- **Authors:** Kevin Lu
- **Track:** research
- **Contribution type:** position-policy
- **Signal:** H — L=H/N=H/A=L (priority 7.9)
- **Techniques:** distillation

**Summary:**

- Thinking Machines post on on-policy distillation: sampling trajectories from the student model and using a strong teacher to grade each token, combining RL's on-policy relevance with distillation's dense reward
- Contrasts off-policy SFT distillation (teacher trajectories, suffers from distribution shift) vs. on-policy RL (sparse reward)
- Uses reverse KL per-token loss and the Tinker training API
- Replicates Qwen3's reasoning result at a fraction of RL cost and applies method to math reasoning and assistant training with domain knowledge
- Inspired by DAGGER and process reward modeling.


### Open-sourcing Knowledge Distillation Code and Weights of SD-Small and SD-Tiny

- **ID:** `hf-r-sd_distillation`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/sd_distillation
- **Date:** 2023-08-01
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Training Machine Learning Models More Efficiently with Dataset Distillation

- **ID:** `gr-r-training-machine-learning-models-more-efficiently-with-dataset-distillation`
- **Company:** Google Research
- **Link:** https://research.google/blog/training-machine-learning-models-more-efficiently-with-dataset-distillation/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Data Distillation Makes Omni Supervised Learning Possible

- **ID:** `meta-r-data-distillation-makes-omni-supervised-learning-possible`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/data-distillation-makes-omni-supervised-learning-possible/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


## <a id="fallback-post-training"></a>Other post-training

_18 posts_

### MemAlign: Building Better LLM Judges From Human Feedback With Scalable Memory

- **ID:** `dbx-r-memalign-building-better-llm-judges-human-feedback-scalable-memory`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/memalign-building-better-llm-judges-human-feedback-scalable-memory
- **Date:** 2026-02-03
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=H/A=M (priority 7.8)

**Summary:**

- Databricks introduces MemAlign, a framework that aligns LLM judges with human feedback using a lightweight dual-memory system instead of fine-tuning or prompt optimization
- Needs only a handful of natural-language feedback examples, beats SOTA prompt optimizers at orders-of-magnitude lower cost ($0.03 vs $1-5) and latency
- Introduces memory scaling: quality improves as feedback accumulates without re-optimization
- Available in open-source MLflow
- Matters for scaling domain-specific LLM-as-judge alignment in enterprise agent evaluation


### The Power of Fine-Tuning on Your Data: Quick Fixing Bugs with LLMs via Never Ending Learning (NEL)

- **ID:** `dbx-r-power-fine-tuning-your-data-quick-fixing-bugs-llms-never-ending-learning-nel`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/power-fine-tuning-your-data-quick-fixing-bugs-llms-never-ending-learning-nel
- **Date:** 2025-04-08
- **Authors:** Samantha Banchik|Ta-Chung Chi|Sam Havens|Dipendra Misra|Will Tipton|Jan van der Vegt|Matei Zaharia|Emanuel Zgraggen
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

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
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Cosmopedia: how to create large-scale synthetic data for pre-training Large Language Models

- **ID:** `hf-r-cosmopedia`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/cosmopedia
- **Date:** 2024-03-20
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=H/A=H (priority 8.8)

**Summary:**

- Cosmopedia: HuggingFace's attempt to reproduce Phi-1.5-style synthetic training data as an open 25B-token, 30M-file dataset generated by Mixtral-8x7B-Instruct
- Mostly web-seeded prompts (80%) clustered into 145 topics with audience/style variation
- Hand-curated sources (Stanford, Khan Academy, OpenStax, WikiHow) added for quality
- Shares llm-swarm for Slurm-distributed generation at scale (10K+ GPU hours)
- Details prompt engineering for diversity, explicit decontamination (10-gram overlap + SequenceMatcher) against MMLU/HellaSwag/ARC
- Includes open 1B model cosmo-1b


### Fine-Grained Human Feedback

- **ID:** `dbx-r-fine-grained-human-feedback`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/fine-grained-human-feedback
- **Date:** 2024-02-27
- **Authors:** Prithviraj (Raj) Ammanabrolu
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- Databricks/UW research on fine-grained RLHF using segment-level reward signals instead of holistic preferences
- Rewards are dense (per-sentence) and diverse (multiple reward models for factuality, relevance, toxicity)
- Shows higher inter-annotator agreement and cleaner data at lower labeling cost
- Adjusting reward model weights lets practitioners tailor LM behavior (e.g., short vs detailed outputs)
- Matters as improved RLHF recipe with more controllable outputs


### Synthetic data: save money, time and carbon with open source

- **ID:** `hf-r-synthetic-data-save-costs`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/synthetic-data-save-costs
- **Date:** 2024-02-16
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Learning complex goals with iterated amplification

- **ID:** `oai-r-learning-complex-goals-with-iterated-amplification`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-complex-goals-with-iterated-amplification/
- **Date:** 2024-02-14
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Proposes iterated amplification: generating training signals for tasks beyond direct human judgment by decomposing them into simpler sub-tasks
- Humans (or algorithms) give supervision on small pieces
- an AI trained on those pieces is then used to help humans solve larger pieces, iteratively bootstrapping training signal
- Related to expert iteration (AlphaGo Zero) and AI-safety-via-debate
- Initial experiments on toy algorithmic tasks (shortest path, union find, etc.) match supervised-learning performance without direct labels
- Seminal scalable oversight proposal by Christiano & Amodei.


### Summarizing books with human feedback

- **ID:** `oai-r-summarizing-books`
- **Company:** OpenAI
- **Link:** https://openai.com/index/summarizing-books/
- **Date:** 2024-02-14
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=M (priority 7.7)

**Summary:**

- Trains a book-summarization model via recursive task decomposition and human feedback (RLHF)
- Breaks book into sections, summarizes each, then summarizes summaries to produce whole-book summaries
- Targets scalable oversight for tasks too long for humans to evaluate end-to-end
- Shows RLHF scales to long-horizon tasks difficult to grade
- Matters as a proof-of-concept for scalable human oversight via recursive decomposition.


### Improving mathematical reasoning with process supervision

- **ID:** `oai-r-improving-mathematical-reasoning-with-process-supervision`
- **Company:** OpenAI
- **Link:** https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/
- **Date:** 2023-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Shows process supervision (rewarding each reasoning step) beats outcome supervision on MATH
- Produces PRM800K dataset of step-level human feedback (released)
- Achieves new SOTA on MATH when used to rerank solutions
- Reports negative alignment tax — process supervision is both safer and more performant
- Matters as a landmark paper on step-level reward modeling for reasoning (precursor to modern PRMs).


### Fine-tuning ChatGPT: Surpassing GPT-4 Summarization Performance–A 63% Cost Reduction and 11x Speed Enhancement using Synthetic Data and LangSmith

- **ID:** `lc-r-fine-tuning-chatgpt-surpassing-gpt-4-summarization`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/fine-tuning-chatgpt-surpassing-gpt-4-summarization
- **Date:** 2023-10-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### On first-order meta-learning algorithms

- **ID:** `oai-r-on-first-order-meta-learning-algorithms`
- **Company:** OpenAI
- **Link:** https://openai.com/index/on-first-order-meta-learning-algorithms/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=M (priority 7.7)

**Summary:**

- Formal paper accompanying Reptile: analyzes first-order meta-learning algorithms that only use first-order derivatives for meta-updates
- Generalizes first-order MAML and introduces Reptile (sample task, train, move initialization toward trained weights)
- Theoretical analysis of why these simple algorithms work on few-shot classification benchmarks
- Meta-learning foundations paper.


### Meta-learning for wrestling

- **ID:** `oai-r-meta-learning-for-wrestling`
- **Company:** OpenAI
- **Link:** https://openai.com/index/meta-learning-for-wrestling/
- **Date:** 2019-12-13
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=M/A=L (priority 6.7)

**Summary:**

- Extends MAML meta-learning to train agents that adapt mid-match against wrestling opponents
- Agents adapt policy parameters between rounds via gradient-ascent on collected reward
- Three morphologies tested (Ant, Bug, Spider)
- Adapting agents beat stronger non-meta-learning agents and handle limb malfunction
- Matters for meta-learning and fast adaptation in multi-agent RL.


### Third-person imitation learning

- **ID:** `oai-r-third-person-imitation-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/third-person-imitation-learning/
- **Date:** 2019-10-15
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=M (priority 7.7)

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
- **Signal:** H — L=H/N=M/A=M (priority 7.7)

**Summary:**

- Reptile: a simple first-order meta-learning algorithm — repeatedly sample a task, SGD on it, move initialization toward the trained weights
- Similar to first-order MAML but only needs black-box access to an SGD/Adam optimizer, with less computation/memory
- Analysis via Taylor expansion shows Reptile maximizes inner-product of gradients from different minibatches of the same task (improved generalization)
- Matches MAML on Omniglot and Mini-ImageNet few-shot benchmarks
- Influential meta-learning / initialization-finding method.


### One-shot imitation learning

- **ID:** `oai-r-one-shot-imitation-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/one-shot-imitation-learning/
- **Date:** 2019-10-15
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=M/A=L (priority 6.7)

**Summary:**

- Meta-learning framework for one-shot imitation: given a single new demo, a net produces a matching policy
- Trained on pairs of demos across many tasks/instantiations (e.g. block stacking configurations)
- Uses soft attention to generalize to unseen task instances
- Targets fast task acquisition without task-specific engineering
- Matters as early meta-imitation learning for robotics.


### Open Sourcing Polygames A New Framework For Training Ai Bots Through Self Play

- **ID:** `meta-r-open-sourcing-polygames-a-new-framework-for-training-ai-bots-through-self-play`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/open-sourcing-polygames-a-new-framework-for-training-ai-bots-through-self-play/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Creating Interactive Agents With Imitation Learning

- **ID:** `dm-r-creating-interactive-agents-with-imitation-learning`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/creating-interactive-agents-with-imitation-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Learning Through Human Feedback

- **ID:** `dm-r-learning-through-human-feedback`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/learning-through-human-feedback/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._

