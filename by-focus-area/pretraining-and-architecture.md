# Pretraining & Architecture

MoE, SSMs, hybrids, scaling laws, new attention variants, data mixes, tokenizers, curriculum, foundation models.

**Post count:** 203

**Contributors:**

- OpenAI: 79
- Databricks Mosaic AI: 31
- Meta AI / FAIR: 25
- Anthropic: 23
- Hugging Face: 13
- DeepSeek: 13
- Allen Institute for AI: 10
- Cursor: 3
- Thinking Machines: 2
- Cognition: 2
- Google DeepMind: 2

**Subcategories:**

- [Foundation model releases](#foundation-model-releases) (32)
- [Architectures (MoE, SSMs, attention variants)](#architectures) (14)
- [Multimodal pretraining](#multimodal-pretraining) (31)
- [Scaling laws & training dynamics](#scaling-and-training-dynamics) (10)
- [Data & tokenization](#data-and-tokenization) (5)
- [Training stack & infrastructure](#training-stack) (13)
- [Research techniques & methods](#research-techniques-and-methods) (64)
- [Science-applied AI (AlphaFold, health, climate, etc.)](#model-research-and-applications) (15)
- [Societal impact & deployment studies](#societal-impact-and-deployment-studies) (18)

---

## <a id="foundation-model-releases"></a>Foundation model releases

_32 posts_

### gpt-oss-120b & gpt-oss-20b Model Card

- **ID:** `oai-r-gpt-oss-model-card`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gpt-oss-model-card/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### An update on our model deprecation commitments for Claude Opus 3

- **ID:** `ant-r-deprecation-updates-opus-3`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/deprecation-updates-opus-3
- **Date:** 2026-02-25
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning

- **ID:** `dsk-r-deepseek-math-v2`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-Math-V2
- **Date:** 2025-11-27
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Claude Opus 4 and 4.1 can now end a rare subset of conversations

- **ID:** `ant-r-end-subset-conversations`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/end-subset-conversations
- **Date:** 2025-08-15
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning

- **ID:** `dsk-r-deepseek-prover-v2`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-Prover-V2
- **Date:** 2025-04-30
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### How to deploy and fine-tune DeepSeek models on AWS

- **ID:** `hf-r-deepseek-r1-aws`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/deepseek-r1-aws
- **Date:** 2025-01-30
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Open-R1: a fully open reproduction of DeepSeek-R1

- **ID:** `hf-r-open-r1`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/open-r1
- **Date:** 2025-01-28
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- **ID:** `dsk-r-deepseek-r1`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-R1
- **Date:** 2025-01-20
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### DeepSeek-V3 Technical Report

- **ID:** `dsk-r-deepseek-v3`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-V3
- **Date:** 2024-12-26
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### The Long Context RAG Capabilities of OpenAI o1 and Google Gemini

- **ID:** `dbx-r-long-context-rag-capabilities-openai-o1-and-google-gemini`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/long-context-rag-capabilities-openai-o1-and-google-gemini
- **Date:** 2024-10-08
- **Authors:** Quinn Leng|Jacob Portes|Sam Havens|Matei Zaharia|Michael Carbin
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** long-context, test-time-compute, retrieval-augmentation

_Summary pending — see link for details._


### Investigating Pretraining Dynamics And Stability With Olmo Checkpoints Ece6F0C4947A

- **ID:** `ai2-r-investigating-pretraining-dynamics-and-stability-with-olmo-checkpoints-ece6f0c4947a`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/investigating-pretraining-dynamics-and-stability-with-olmo-checkpoints-ece6f0c4947a
- **Date:** 2024-10-02
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search

- **ID:** `dsk-r-deepseek-prover-v1.5`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-Prover-V1.5
- **Date:** 2024-08-15
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### WWDC 24: Running Mistral 7B with Core ML

- **ID:** `hf-r-mistral-coreml`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/mistral-coreml
- **Date:** 2024-07-22
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### SmolLM - blazingly fast and remarkably powerful

- **ID:** `hf-r-smollm`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/smollm
- **Date:** 2024-07-16
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence

- **ID:** `dsk-r-deepseek-coder-v2`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-Coder-V2
- **Date:** 2024-06-14
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model

- **ID:** `dsk-r-deepseek-v2`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-V2
- **Date:** 2024-04-22
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Fine-tuning GPT-2 from human preferences

- **ID:** `oai-r-fine-tuning-gpt-2`
- **Company:** OpenAI
- **Link:** https://openai.com/index/fine-tuning-gpt-2/
- **Date:** 2024-02-14
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

- **ID:** `dsk-r-deepseek-math`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-Math
- **Date:** 2024-02-05
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Hello Olmo A Truly Open Llm 43F7E7359222

- **ID:** `ai2-r-hello-olmo-a-truly-open-llm-43f7e7359222`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/hello-olmo-a-truly-open-llm-43f7e7359222
- **Date:** 2024-02-01
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Olmo Open Language Model 87Ccfc95F580

- **ID:** `ai2-r-olmo-open-language-model-87ccfc95f580`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/olmo-open-language-model-87ccfc95f580
- **Date:** 2024-02-01
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### GPT-2: 6-month follow-up

- **ID:** `oai-r-gpt-2-6-month-follow-up`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gpt-2-6-month-follow-up/
- **Date:** 2024-01-16
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Does Gpt 4 Have Theory Of Mind Capabilities Cd2D766E51A7

- **ID:** `ai2-r-does-gpt-4-have-theory-of-mind-capabilities-cd2d766e51a7`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/does-gpt-4-have-theory-of-mind-capabilities-cd2d766e51a7
- **Date:** 2023-11-30
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### DeepSeek LLM: Scaling Open-Source Language Models with Longtermism

- **ID:** `dsk-r-deepseek-llm`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-LLM
- **Date:** 2023-11-29
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### DeepSeek-Coder: When the Large Language Model Meets Programming

- **ID:** `dsk-r-deepseek-coder`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-Coder
- **Date:** 2023-10-20
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Announcing MPT-7B-8K: 8K Context Length for Document Understanding

- **ID:** `dbx-r-long-context-mpt-7b-8k`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/long-context-mpt-7b-8k
- **Date:** 2023-07-18
- **Authors:** Sam Havens|Erica Ji Yuen
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** long-context

_Summary pending — see link for details._


### MPT-30B: Raising the bar for open-source foundation models

- **ID:** `dbx-r-mpt-30b`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mpt-30b
- **Date:** 2023-06-22
- **Track:** research
- **Contribution type:** infra-release

_Summary pending — see link for details._


### Extracting Concepts from GPT-4

- **ID:** `oai-r-extracting-concepts-from-gpt-4`
- **Company:** OpenAI
- **Link:** https://openai.com/index/extracting-concepts-from-gpt-4/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Finding GPT-4’s mistakes with GPT-4

- **ID:** `oai-r-finding-gpt4s-mistakes-with-gpt-4`
- **Company:** OpenAI
- **Link:** https://openai.com/index/finding-gpt4s-mistakes-with-gpt-4/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Llama 2 3 Meditron Yale Medicine Epfl Open Source Llm

- **ID:** `meta-r-llama-2-3-meditron-yale-medicine-epfl-open-source-llm`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/llama-2-3-meditron-yale-medicine-epfl-open-source-llm/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Gpt 4 Theory Of Mind

- **ID:** `ai2-r-gpt-4-theory-of-mind`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/gpt-4-theory-of-mind
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Hello Olmo

- **ID:** `ai2-r-hello-olmo`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/hello-olmo
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Olmo

- **ID:** `ai2-r-olmo`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/olmo
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="architectures"></a>Architectures (MoE, SSMs, attention variants)

_14 posts_

### Mixture of Experts (MoEs) in Transformers

- **ID:** `hf-r-moe-transformers`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/moe-transformers
- **Date:** 2026-02-26
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### How we built OWL, the new architecture behind our ChatGPT-based browser, Atlas

- **ID:** `oai-e-building-chatgpt-atlas`
- **Company:** OpenAI
- **Link:** https://openai.com/index/building-chatgpt-atlas/
- **Date:** 2025-12-12
- **Track:** engineering
- **Contribution type:** retrospective-case-study

_Summary pending — see link for details._


### DeepSeek-V3.2-Exp: Exploring Sparse Attention

- **ID:** `dsk-r-deepseek-v3.2-exp`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-V3.2-Exp
- **Date:** 2025-09-29
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Inference-Friendly Models with MixAttention

- **ID:** `dbx-r-mixattention`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mixattention
- **Date:** 2024-09-18
- **Authors:** Shashank Rajput|Ying Sheng (Stanford University)|Vitaliy Chiley
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Olmoe An Open Small And State Of The Art Mixture Of Experts Model C258432D0514

- **ID:** `ai2-r-olmoe-an-open-small-and-state-of-the-art-mixture-of-experts-model-c258432d0514`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/olmoe-an-open-small-and-state-of-the-art-mixture-of-experts-model-c258432d0514
- **Date:** 2024-09-04
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Welcome Falcon Mamba: The first strong attention-free 7B model

- **ID:** `hf-r-falconmamba`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/falconmamba
- **Date:** 2024-08-12
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Extensions and limitations of the neural GPU

- **ID:** `oai-r-extensions-and-limitations-of-the-neural-gpu`
- **Company:** OpenAI
- **Link:** https://openai.com/index/extensions-and-limitations-of-the-neural-gpu/
- **Date:** 2024-03-21
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Improves Neural GPU via curriculum learning and larger memory-efficient models
- Can learn all decimal arithmetic operations that generalize to arbitrarily long numbers
- Learns to evaluate arithmetic expressions with operator precedence (binary rep, imperfect)
- Reveals adversarial-like failure modes on highly-symmetric inputs
- Matters as an early study of algorithmic learning and generalization limits.


### Weight normalization: A simple reparameterization to accelerate training of deep neural networks

- **ID:** `oai-r-weight-normalization`
- **Company:** OpenAI
- **Link:** https://openai.com/index/weight-normalization/
- **Date:** 2024-03-21
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Introduces weight normalization: reparameterizes weights by decoupling magnitude from direction
- Speeds SGD convergence with lower computational overhead than batch norm
- Works for recurrent nets, deep RL, and generative models where batch norm fails
- Inspired by but avoids minibatch dependencies of batch normalization
- Matters as a foundational, widely-used training-stabilization technique.


### DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models

- **ID:** `dsk-r-deepseek-moe`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-MoE
- **Date:** 2024-01-02
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Welcome Mixtral - a SOTA Mixture of Experts on Hugging Face

- **ID:** `hf-r-mixtral`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/mixtral
- **Date:** 2023-12-11
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Mixture of Experts Explained

- **ID:** `hf-r-moe`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/moe
- **Date:** 2023-12-11
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Timesformer A New Architecture For Video Understanding

- **ID:** `meta-r-timesformer-a-new-architecture-for-video-understanding`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/timesformer-a-new-architecture-for-video-understanding/
- **Date:** 2023-10-04
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing RWKV - An RNN with the advantages of a transformer

- **ID:** `hf-r-rwkv`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/rwkv
- **Date:** 2023-05-15
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Softmax Linear Units

- **ID:** `ant-r-softmax-linear-units`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/softmax-linear-units
- **Date:** 2022-06-17
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Proposes Softmax Linear Units (SoLU), an MLP activation function replacement that substantially increases the fraction of interpretable neurons at minimal ML-performance cost
- Validated via blinded human interpretability ratings showing many more neurons correspond to articulable features/categories
- Caveats: SoLU may be 'hiding' features in superposition while making others visible — no free lunch
- Architectural intervention aimed explicitly at interpretability, not capability
- Early mechanistic-interpretability-meets-architecture contribution.


## <a id="multimodal-pretraining"></a>Multimodal pretraining

_31 posts_

### Sam 3D

- **ID:** `meta-r-sam-3d`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/sam-3d/
- **Date:** 2025-11-19
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### DeepSeek-VL: Towards Real-World Vision-Language Understanding

- **ID:** `dsk-r-deepseek-vl`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-VL
- **Date:** 2024-03-07
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### DALL·E 2 pre-training mitigations

- **ID:** `oai-r-dall-e-2-pre-training-mitigations`
- **Company:** OpenAI
- **Link:** https://openai.com/index/dall-e-2-pre-training-mitigations/
- **Date:** 2024-01-16
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Yann Lecun Ai Model I Jepa

- **ID:** `meta-r-yann-lecun-ai-model-i-jepa`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/yann-lecun-ai-model-i-jepa/
- **Date:** 2023-07-12
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Training Stable Diffusion from Scratch for <$50k with MosaicML (Part 2)

- **ID:** `dbx-r-stable-diffusion-2`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/stable-diffusion-2
- **Date:** 2023-04-26
- **Authors:** Mihir Patel|Cory Stephenson|Landan Seguin|Austin Jacobson|Erica Ji Yuen
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Hierarchical text-conditional image generation with CLIP latents

- **ID:** `oai-r-hierarchical-text-conditional-image-generation-with-clip-latents`
- **Company:** OpenAI
- **Link:** https://openai.com/index/hierarchical-text-conditional-image-generation-with-clip-latents/
- **Date:** 2022-09-21
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### The Annotated Diffusion Model

- **ID:** `hf-r-annotated-diffusion`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/annotated-diffusion
- **Date:** 2022-06-07
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Variational Lossy Autoencoder

- **ID:** `oai-r-variational-lossy-autoencoder`
- **Company:** OpenAI
- **Link:** https://openai.com/index/variational-lossy-autoencoder/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### DALL·E 3

- **ID:** `oai-r-dall-e-3`
- **Company:** OpenAI
- **Link:** https://openai.com/index/dall-e-3/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Training Stable Diffusion from Scratch (Part 3)

- **ID:** `dbx-r-stable-diffusion-part-3`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/stable-diffusion-part-3
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Training Stable Diffusion from Scratch Costs $160k

- **ID:** `dbx-r-training-stable-diffusion-from-scratch-costs-160k`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/training-stable-diffusion-from-scratch-costs-160k
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Training Stable Diffusion from Scratch (Part 2)

- **ID:** `dbx-r-training-stable-diffusion-from-scratch-part-2`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/training-stable-diffusion-from-scratch-part-2
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Dino Sam Medical Triage

- **ID:** `meta-r-dino-sam-medical-triage`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/dino-sam-medical-triage/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Fair News Segment Anything 2 1 Meta Spirit Lm Layer Skip Salsa Lingua

- **ID:** `meta-r-fair-news-segment-anything-2-1-meta-spirit-lm-layer-skip-salsa-lingua`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/fair-news-segment-anything-2-1-meta-spirit-lm-layer-skip-salsa-lingua/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Fair News Segment Anything 2 1 Meta Spirit Lm Layer Skip Salsa Sona

- **ID:** `meta-r-fair-news-segment-anything-2-1-meta-spirit-lm-layer-skip-salsa-sona`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/fair-news-segment-anything-2-1-meta-spirit-lm-layer-skip-salsa-sona/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Instagram Edits Cutouts Segment Anything

- **ID:** `meta-r-instagram-edits-cutouts-segment-anything`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/instagram-edits-cutouts-segment-anything/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Josephine Miller Designer Meta Segment Anything 2

- **ID:** `meta-r-josephine-miller-designer-meta-segment-anything-2`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/josephine-miller-designer-meta-segment-anything-2/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Sam Audio

- **ID:** `meta-r-sam-audio`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/sam-audio/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Segment Anything

- **ID:** `meta-r-segment-anything`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Segment Anything 2

- **ID:** `meta-r-segment-anything-2`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-2/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Segment Anything 2 Video

- **ID:** `meta-r-segment-anything-2-video`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-2-video/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Segment Anything Common Sense Machines 3D Assets

- **ID:** `meta-r-segment-anything-common-sense-machines-3d-assets`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-common-sense-machines-3d-assets/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Segment Anything Conservation X Wildlife Monitoring

- **ID:** `meta-r-segment-anything-conservation-x-wildlife-monitoring`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-conservation-x-wildlife-monitoring/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Segment Anything Floods

- **ID:** `meta-r-segment-anything-floods`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-floods/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Segment Anything Foundation Model Image Segmentation

- **ID:** `meta-r-segment-anything-foundation-model-image-segmentation`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-foundation-model-image-segmentation/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Segment Anything Model 3

- **ID:** `meta-r-segment-anything-model-3`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-model-3/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Segment Anything Roboflow Image Segmentation

- **ID:** `meta-r-segment-anything-roboflow-image-segmentation`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-roboflow-image-segmentation/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Upenn Dino Sam Helping Medical Triage

- **ID:** `meta-r-upenn-dino-sam-helping-medical-triage`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/upenn-dino-sam-helping-medical-triage/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Usra Sam Flood Emergencies

- **ID:** `meta-r-usra-sam-flood-emergencies`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/usra-sam-flood-emergencies/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### V Jepa 2 World Model Benchmarks

- **ID:** `meta-r-v-jepa-2-world-model-benchmarks`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### V Jepa Yann Lecun Ai Model Video Joint Embedding Predictive Architecture

- **ID:** `meta-r-v-jepa-yann-lecun-ai-model-video-joint-embedding-predictive-architecture`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/v-jepa-yann-lecun-ai-model-video-joint-embedding-predictive-architecture/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="scaling-and-training-dynamics"></a>Scaling laws & training dynamics

_10 posts_

### Emergent introspective awareness in large language models

- **ID:** `ant-r-introspection`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/introspection
- **Date:** 2025-10-29
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Modular Manifolds

- **ID:** `tm-r-modular-manifolds`
- **Company:** Thinking Machines
- **Link:** https://thinkingmachines.ai/blog/modular-manifolds/
- **Date:** 2025-09-26
- **Authors:** Jeremy Bernstein
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Thinking Machines research on constraining weight matrices to submanifolds during training for healthier large-model training
- Proposes a manifold version of Muon whose weights are kept on the Stiefel manifold (unit condition number matrices)
- Introduces 'modular manifolds' as composable constraint primitives to scale up networks
- Argues weight normalization can make update sizes interpretable, prevent norm explosion, aid hyperparameter tuning, support Lipschitz guarantees
- Research-agenda-style post with open directions.


### Characterizing Datasets and Building Better Models with Continued Pre-Training

- **ID:** `dbx-r-characterizing-datasets-and-building-better-models-continued-pre-training`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/characterizing-datasets-and-building-better-models-continued-pre-training
- **Date:** 2024-11-21
- **Authors:** Mansheej Paul|Brett Larsen|Connor Jennings|Cody Blakeney
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Databricks guide to Continued Pre-Training (CPT) as a method for adapting LLMs to specific domains without full retraining
- Identifies three key hyperparameters: learning rate, training duration, data mixture
- Recommends simple weight averaging to mitigate forgetting
- Also shows CPT as a tool to characterize datasets by seeing which evals improve/degrade
- Matters as a practical recipe for domain adaptation of open-source LLMs


### How Long Should You Train Your Language Model?

- **ID:** `dbx-r-how-long-should-you-train-your-language-model`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/how-long-should-you-train-your-language-model
- **Date:** 2024-07-19
- **Authors:** Nikhil Sardana|Jacob Portes|Sasha Doubov
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Scaling Laws and Interpretability of Learning from Repeated Data

- **ID:** `ant-r-scaling-laws-and-interpretability-of-learning-from-repeated-data`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/scaling-laws-and-interpretability-of-learning-from-repeated-data
- **Date:** 2022-05-21
- **Track:** research
- **Contribution type:** new-method
- **Techniques:** scaling-laws

_Summary pending — see link for details._


### Efficiently Estimating Pareto Frontiers with Cyclic Learning Rate Schedules

- **ID:** `dbx-r-efficiently-estimating-pareto-frontiers`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/efficiently-estimating-pareto-frontiers
- **Date:** 2022-04-08
- **Authors:** Jacob Portes
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Deep double descent

- **ID:** `oai-r-deep-double-descent`
- **Company:** OpenAI
- **Link:** https://openai.com/index/deep-double-descent/
- **Date:** 2020-01-23
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Shows the double descent phenomenon (test error dips, peaks, then dips again) occurs in CNNs, ResNets, and transformers
- Documents model-wise, sample-wise, and epoch-wise double descent
- Finds a regime where more data actually hurts test performance
- Peak occurs at the interpolation threshold where models barely fit training data
- Matters for understanding overparameterization and modern generalization theory.


### Scaling laws for neural language models

- **ID:** `oai-r-scaling-laws-for-neural-language-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/scaling-laws-for-neural-language-models/
- **Date:** 2019-12-05
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** scaling-laws

_Summary pending — see link for details._


### AI and efficiency

- **ID:** `oai-r-ai-and-efficiency`
- **Company:** OpenAI
- **Link:** https://openai.com/index/ai-and-efficiency/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- OpenAI analysis showing algorithmic efficiency in training doubles every ~16 months on ImageNet (AlexNet-level requires 44x less compute in 2019 than 2012)
- Beats Moore's Law (~11x over same period) and suggests algorithmic progress outpaces hardware for well-invested AI tasks
- Similar doubling rates observed in translation (Transformer vs seq2seq), Go (AlphaZero), Dota (OpenAI Five)
- Policy implications: tracking compute-efficiency as an AI-progress measure
- Canonical scaling-laws-adjacent reference.


### Toward understanding and preventing misalignment generalization

- **ID:** `oai-r-emergent-misalignment`
- **Company:** OpenAI
- **Link:** https://openai.com/index/emergent-misalignment/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


## <a id="data-and-tokenization"></a>Data & tokenization

_5 posts_

### Making A Switch Dolma Moves To Odc By 8F0E73852F44

- **ID:** `ai2-r-making-a-switch-dolma-moves-to-odc-by-8f0e73852f44`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/making-a-switch-dolma-moves-to-odc-by-8f0e73852f44
- **Date:** 2024-04-15
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Cosmopedia: how to create large-scale synthetic data for pre-training Large Language Models

- **ID:** `hf-r-cosmopedia`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/cosmopedia
- **Date:** 2024-03-20
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- HF introduces Cosmopedia, billions-of-tokens synthetic dataset generated to replicate Phi-1.5-style pretraining data
- blog tackles challenges of scaling synthetic generation from thousands to millions of samples specifically for pre-training (not instruction tuning)
- outlines prompt design, deduplication, and topic coverage strategies
- positions the release as a community alternative to closed Phi training data
- primarily a pretraining-data/tokenization contribution.


### Dolma 3 Trillion Tokens Open Llm Corpus 9A0Ff4B8Da64

- **ID:** `ai2-r-dolma-3-trillion-tokens-open-llm-corpus-9a0ff4b8da64`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/dolma-3-trillion-tokens-open-llm-corpus-9a0ff4b8da64
- **Date:** 2023-08-18
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Teacher–student curriculum learning

- **ID:** `oai-r-teacher-student-curriculum-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/teacher-student-curriculum-learning/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Training CodeParrot 🦜 from Scratch

- **ID:** `hf-r-codeparrot`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/codeparrot
- **Date:** 2021-12-08
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- Step-by-step tutorial for training CodeParrot (GPT-2-scale code LM) from scratch to approximate GitHub Copilot behavior for Python
- built a 180GB GitHub Python dataset via BigQuery, found extreme duplication (0.1% of files = 15% of corpus) and applied Codex-paper deduplication/cleaning to yield 50GB clean dataset on HF Hub
- covers training a code-specific tokenizer from GPT-2 init and the model training loop
- strongest fit is pretraining data-and-tokenization since data curation dominates.


## <a id="training-stack"></a>Training stack & infrastructure

_13 posts_

### A technical report on Composer 2

- **ID:** `cur-r-composer-2-technical-report`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/composer-2-technical-report
- **Date:** 2026-03-27
- **Authors:** Sasha Rush
- **Track:** research
- **Contribution type:** infra-release
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Improving Composer through real-time RL

- **ID:** `cur-r-real-time-rl-for-composer`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/real-time-rl-for-composer
- **Date:** 2026-03-26
- **Authors:** Jacob, Ben, Nathan & Wanqi
- **Track:** research
- **Contribution type:** infra-release
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Training Composer for longer horizons

- **ID:** `cur-r-self-summarization`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/self-summarization
- **Date:** 2026-03-17
- **Authors:** Federico & Sasha
- **Track:** research
- **Contribution type:** infra-release
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Defeating Nondeterminism in LLM Inference

- **ID:** `tm-r-defeating-nondeterminism-in-llm-inference`
- **Company:** Thinking Machines
- **Link:** https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
- **Date:** 2025-09-10
- **Authors:** Horace He
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Thinking Machines post debunking the 'concurrency + floating point' hypothesis for LLM inference nondeterminism
- Shows deterministic matmul on GPUs is bitwise-stable, so nondeterminism must come elsewhere
- Identifies kernel implementations — particularly batch-size- and sequence-length-dependent reduction orders — as the real culprit
- Walks through how to build truly deterministic inference (reproducible results from vLLM/SGLang-style servers)
- Systems/training-stack-adjacent work relevant to inference infra and reproducibility.


### Building DBRX-class Custom LLMs with Mosaic AI Training

- **ID:** `dbx-e-mosaic-ai-training-capabilities`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mosaic-ai-training-capabilities
- **Date:** 2024-05-14
- **Authors:** Anna Pfohl|Cheng Li|Mihir Patel|Wai Wu|Will Gleich|Ajay Saini|Hagay Lupesko
- **Track:** engineering
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### 5x Faster Image Segmentation Training with MosaicML Recipes

- **ID:** `dbx-r-mosaic-image-segmentation`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mosaic-image-segmentation
- **Date:** 2022-11-17
- **Authors:** Landan Seguin|Cory Stephenson|Erica Ji Yuen
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Mosaic LLMs: GPT-3 quality for <$500k

- **ID:** `dbx-r-gpt-3-quality-for-500k`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/gpt-3-quality-for-500k
- **Date:** 2022-09-29
- **Authors:** Abhi Venigalla|Linden Li
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Mosaic ResNet Deep Dive

- **ID:** `dbx-r-mosaic-resnet-deep-dive`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mosaic-resnet-deep-dive
- **Date:** 2022-07-18
- **Authors:** Matthew Leavitt
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Blazingly Fast Computer Vision Training with the Mosaic ResNet and Composer

- **ID:** `dbx-r-mosaic-resnet`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mosaic-resnet
- **Date:** 2022-06-09
- **Authors:** Matthew Leavitt|Erica Ji Yuen|Kobie Crawford
- **Track:** research
- **Contribution type:** infra-release

_Summary pending — see link for details._


### Techniques for training large neural networks

- **ID:** `oai-r-techniques-for-training-large-neural-networks`
- **Company:** OpenAI
- **Link:** https://openai.com/index/techniques-for-training-large-neural-networks/
- **Date:** 2021-07-28
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Explainer/survey of parallelism strategies for training large neural networks
- Covers data parallelism, pipeline parallelism (GPipe, PipeDream), tensor parallelism (Megatron-LM), and Mixture-of-Experts
- Discusses pipeline bubbles, microbatching, and sequence parallelism tradeoffs
- Serves as an accessible primer for the modern distributed training stack
- Matters as reference doc for training infrastructure at scale.


### 5 Best Practices for Efficient Model Training

- **ID:** `dbx-r-5-best-practices-for-efficient-model-training`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/5-best-practices-for-efficient-model-training
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- MosaicML post summarizing 5 best practices for efficient CNN training
- Recommends Composer library and MosaicML docker image, with --algorithms channels_last for speedup
- Covers mixed precision training as foundational technique
- Claimed speedups: 3.4x for vision, 1.6x for NLP on standard benchmarks
- Goal: 4x annual speedup
- Matters as entry-level efficiency guide for ML practitioners


### Best Practices (Dec 2021)

- **ID:** `dbx-r-best-practices-dec-2021`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/best-practices-dec-2021
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- title-only
- Wayback returned 404 for this MosaicML post
- Based on title, likely a December 2021 best-practices post from MosaicML covering efficient training recipes and early Composer guidance
- Classified as training-stack given the MosaicML/Composer context
- Matters as early-era MosaicML efficiency methodology post


### Making ML Training Efficient Algorithmically

- **ID:** `dbx-r-making-ml-training-efficient-algorithmically`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/making-ml-training-efficient-algorithmically
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- MosaicML's launch post (Oct 2021) from founders Naveen Rao, Hanlin Tang, Michael Carbin, Jonathan Frankle
- Mission: reduce time/cost/energy of training via algorithmic and systems efficiency
- Argues training compute is growing >5x/year while hardware perf/$ lags far behind, making AI inaccessible
- Introduces Composer as a mosaic of algorithmic methods that compose together for acceleration
- Matters as foundational vision for the MosaicML efficiency research agenda


## <a id="research-techniques-and-methods"></a>Research techniques & methods

_64 posts_

### Early experiments in accelerating science with GPT-5

- **ID:** `oai-r-accelerating-science-gpt-5`
- **Company:** OpenAI
- **Link:** https://openai.com/index/accelerating-science-gpt-5/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Advancing science and math with GPT-5.2

- **ID:** `oai-r-gpt-5-2-for-science-and-math`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gpt-5-2-for-science-and-math/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Why language models hallucinate

- **ID:** `oai-r-why-language-models-hallucinate`
- **Company:** OpenAI
- **Link:** https://openai.com/index/why-language-models-hallucinate/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### GPT-5 lowers the cost of cell-free protein synthesis

- **ID:** `oai-r-gpt-5-lowers-protein-synthesis-cost`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gpt-5-lowers-protein-synthesis-cost/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### GPT-5.2 derives a new result in theoretical physics

- **ID:** `oai-r-new-result-theoretical-physics`
- **Company:** OpenAI
- **Link:** https://openai.com/index/new-result-theoretical-physics/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Emotion concepts and their function in a large language model

- **ID:** `ant-r-emotion-concepts-function`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/emotion-concepts-function
- **Date:** 2026-04-02
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### A “diff” tool for AI: Finding behavioral differences in new models

- **ID:** `ant-r-diff-tool`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/diff-tool
- **Date:** 2026-03-13
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Databricks at NeurIPS 2025

- **ID:** `dbx-r-databricks-neurips-2025`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/databricks-neurips-2025
- **Date:** 2025-12-01
- **Authors:** Sam Plecque
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Confidential Inference via Trusted Virtual Machines

- **ID:** `ant-r-confidential-inference-trusted-vms`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/confidential-inference-trusted-vms
- **Date:** 2025-06-18
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Kevin-32B: Multi-Turn RL for Writing CUDA Kernels

- **ID:** `cog-r-kevin-32b`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/kevin-32b
- **Date:** 2025-05-06
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Reasoning models don't always say what they think

- **ID:** `ant-r-reasoning-models-dont-say-think`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/reasoning-models-dont-say-think
- **Date:** 2025-04-03
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Forecasting rare language model behaviors

- **ID:** `ant-r-forecasting-rare-behaviors`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/forecasting-rare-behaviors
- **Date:** 2025-02-25
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Databricks at NeurIPS 2024

- **ID:** `dbx-r-databricks-neurips-2024`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/databricks-neurips-2024
- **Date:** 2024-12-09
- **Authors:** Sam Plecque|Kobie Crawford|Emily Hutson
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Understanding the source of what we see and hear online

- **ID:** `oai-r-understanding-the-source-of-what-we-see-and-hear-online`
- **Company:** OpenAI
- **Link:** https://openai.com/index/understanding-the-source-of-what-we-see-and-hear-online/
- **Date:** 2024-08-04
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Consistency Models

- **ID:** `oai-r-consistency-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/consistency-models/
- **Date:** 2024-06-20
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Improved Techniques for Training Consistency Models

- **ID:** `oai-r-improved-techniques-for-training-consistency-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/improved-techniques-for-training-consistency-models/
- **Date:** 2024-06-20
- **Track:** research
- **Contribution type:** new-method

_Summary pending — see link for details._


### Improving language model behavior by training on a curated dataset

- **ID:** `oai-r-improving-language-model-behavior`
- **Company:** OpenAI
- **Link:** https://openai.com/index/improving-language-model-behavior/
- **Date:** 2024-02-14
- **Track:** research
- **Contribution type:** dataset-benchmark

_Summary pending — see link for details._


### Benchmarking safe exploration in deep reinforcement learning

- **ID:** `oai-r-benchmarking-safe-exploration-in-deep-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/benchmarking-safe-exploration-in-deep-reinforcement-learning/
- **Date:** 2024-02-14
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Text and code embeddings by contrastive pre-training

- **ID:** `oai-r-text-and-code-embeddings-by-contrastive-pre-training`
- **Company:** OpenAI
- **Link:** https://openai.com/index/text-and-code-embeddings-by-contrastive-pre-training/
- **Date:** 2024-01-12
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Teaching models to express their uncertainty in words

- **ID:** `oai-r-teaching-models-to-express-their-uncertainty-in-words`
- **Company:** OpenAI
- **Link:** https://openai.com/index/teaching-models-to-express-their-uncertainty-in-words/
- **Date:** 2024-01-12
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Efficient training of language models to fill in the middle

- **ID:** `oai-r-efficient-training-of-language-models-to-fill-in-the-middle`
- **Company:** OpenAI
- **Link:** https://openai.com/index/efficient-training-of-language-models-to-fill-in-the-middle/
- **Date:** 2024-01-12
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Evolution through large models

- **ID:** `oai-r-evolution-through-large-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/evolution-through-large-models/
- **Date:** 2024-01-12
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Proposes ELM: using code-pretrained LLMs as mutation operators for genetic programming
- Combined with MAP-Elites, generates hundreds of thousands of functional Sodarace walker programs
- Bootstraps a new conditional LM that outputs walkers for specific terrains
- Demonstrates open-ended generation in a domain with zero original training data
- Matters for open-endedness, creative code generation, and LLM-augmented evolutionary search.


### Interpretable and pedagogical examples

- **ID:** `oai-r-interpretable-and-pedagogical-examples`
- **Company:** OpenAI
- **Link:** https://openai.com/index/interpretable-and-pedagogical-examples/
- **Date:** 2024-01-12
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Paper-version companion to the interpretable teaching blog: iterative student-teacher training yields interpretable teaching strategies
- Teacher network learns pedagogical examples that transfer to humans
- Evaluated across rule-based, probabilistic, boolean, and hierarchical concepts
- Measures interpretability via similarity to intuitive strategies and human teaching efficacy
- Matters for communication between learning agents.


### Introducing Llama2-70B-Chat with MosaicML Inference

- **ID:** `dbx-r-llama2-inference`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/llama2-inference
- **Date:** 2023-08-24
- **Authors:** Hagay Lupesko|Margaret Qian|Daya Khudia|Sam Havens|Daniel King|Erica Ji Yuen
- **Track:** research
- **Contribution type:** new-method

_Summary pending — see link for details._


### MosaicBERT: Pretraining BERT from Scratch for $20

- **ID:** `dbx-r-mosaicbert`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mosaicbert
- **Date:** 2023-03-09
- **Authors:** Jacob Portes|Alex Trott|Daniel King|Sam Havens|Erica Ji Yuen
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### MosaicML StreamingDataset: Fast, Accurate Streaming of Training Data from Cloud Storage

- **ID:** `dbx-e-mosaicml-streamingdataset`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mosaicml-streamingdataset
- **Date:** 2023-02-09
- **Authors:** James Knighton|Karan Jariwala|Erica Ji Yuen
- **Track:** engineering
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Discovering Language Model Behaviors with Model-Written Evaluations

- **ID:** `ant-r-discovering-language-model-behaviors-with-model-written-evaluations`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/discovering-language-model-behaviors-with-model-written-evaluations
- **Date:** 2022-12-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### MosaicML Delivers Leading NLP Performance in MLPerf v2.1

- **ID:** `dbx-r-mlperf-nlp-nov2022`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mlperf-nlp-nov2022
- **Date:** 2022-11-09
- **Authors:** Daya Khudia|Nikhil Sardana|Sam Havens|Alex Trott|Erica Ji Yuen
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Hindsight Experience Replay

- **ID:** `oai-r-hindsight-experience-replay`
- **Company:** OpenAI
- **Link:** https://openai.com/index/hindsight-experience-replay/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Quantifying generalization in reinforcement learning

- **ID:** `oai-r-quantifying-generalization-in-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/quantifying-generalization-in-reinforcement-learning/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Ucb Exploration Via Q Ensembles

- **ID:** `oai-r-ucb-exploration-via-q-ensembles`
- **Company:** OpenAI
- **Link:** https://openai.com/index/ucb-exploration-via-q-ensembles/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Some considerations on learning to explore via meta-reinforcement learning

- **ID:** `oai-r-some-considerations-on-learning-to-explore-via-meta-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/some-considerations-on-learning-to-explore-via-meta-reinforcement-learning/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Plan online, learn offline: Efficient learning and exploration via model-based control

- **ID:** `oai-r-plan-online-learn-offline`
- **Company:** OpenAI
- **Link:** https://openai.com/index/plan-online-learn-offline/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Dota 2 with large scale deep reinforcement learning

- **ID:** `oai-r-dota-2-with-large-scale-deep-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/dota-2-with-large-scale-deep-reinforcement-learning/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Large-scale study of curiosity-driven learning

- **ID:** `oai-r-large-scale-study-of-curiosity-driven-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/large-scale-study-of-curiosity-driven-learning/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- First large-scale study of purely curiosity-driven RL (no extrinsic reward) across 54 environments
- Shows strong performance of prediction-error intrinsic reward including Atari
- Random features work for many games, learned features generalize better (e.g., Mario level generalization)
- Identifies failure modes in stochastic environments
- Matters as empirical foundation for intrinsic motivation in RL.


### Variational option discovery algorithms

- **ID:** `oai-r-variational-option-discovery-algorithms`
- **Company:** OpenAI
- **Link:** https://openai.com/index/variational-option-discovery-algorithms/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Multi-Goal Reinforcement Learning: Challenging robotics environments and request for research

- **ID:** `oai-r-multi-goal-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/multi-goal-reinforcement-learning/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### RL²: Fast reinforcement learning via slow reinforcement learning

- **ID:** `oai-r-rl2`
- **Company:** OpenAI
- **Link:** https://openai.com/index/rl2/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Better exploration with parameter noise

- **ID:** `oai-r-better-exploration-with-parameter-noise`
- **Company:** OpenAI
- **Link:** https://openai.com/index/better-exploration-with-parameter-noise/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### #Exploration: A study of count-based exploration for deep reinforcement learning

- **ID:** `oai-r-exploration`
- **Company:** OpenAI
- **Link:** https://openai.com/index/exploration/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Stochastic Neural Networks for hierarchical reinforcement learning

- **ID:** `oai-r-stochastic-neural-networks-for-hierarchical-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/stochastic-neural-networks-for-hierarchical-reinforcement-learning/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Evolution strategies as a scalable alternative to reinforcement learning

- **ID:** `oai-r-evolution-strategies`
- **Company:** OpenAI
- **Link:** https://openai.com/index/evolution-strategies/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Learning a hierarchy

- **ID:** `oai-r-learning-a-hierarchy`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-a-hierarchy/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Introduces MLSH (Meta-Learning Shared Hierarchies): master policy switches among learned sub-policies
- Sub-policies discovered via meta-learning over a task distribution (not hand-engineered)
- Drastically reduces effective horizon (e.g. 2000 low-level actions to 10 high-level)
- Demonstrated on AntMaze where sub-policies correspond to movement directions
- Matters as foundational hierarchical RL work with released MuJoCo environments.


### Generative modeling with sparse transformers

- **ID:** `oai-r-sparse-transformer`
- **Company:** OpenAI
- **Link:** https://openai.com/index/sparse-transformer/
- **Date:** 2022-09-21
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Behind the Scenes: Setting a Baseline for Image Segmentation Speedups

- **ID:** `dbx-r-behind-the-scenes`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/behind-the-scenes
- **Date:** 2022-07-28
- **Authors:** Landan Seguin
- **Track:** research
- **Contribution type:** retrospective-case-study

**Summary:**

- MosaicML establishes a strong semantic segmentation baseline (45.56 mIoU on ADE20k) in 3.5 hours on 8xA100 using Composer
- Emphasizes the importance of strong baselines for efficiency research (vs weak baselines that can be trivially improved)
- Sets stage for future speedups on segmentation
- Earlier work showed Composer trained ResNet on ImageNet 7x faster
- Matters as methodology post for how to benchmark speedup claims honestly


### MosaicML Satisfies the Need for Speed with MLPerf Results

- **ID:** `dbx-r-mlperf-2022`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mlperf-2022
- **Date:** 2022-06-29
- **Authors:** Bandish Shah|Daya Khudia|Hanlin Tang
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Learning concepts with energy functions

- **ID:** `oai-r-learning-concepts-with-energy-functions`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-concepts-with-energy-functions/
- **Date:** 2022-06-23
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Proposes energy-based model that learns spatial/relational concepts (near, between, closest) from ~5 demonstrations
- Jointly performs classification and generation of concepts via a shared energy function
- Demonstrates cross-domain transfer (2D particle env to 3D robot arm) without retraining
- Uses relational network architecture with attention masks
- Matters as early work on concept learning via energy-based models and transfer.


### Prediction and control with temporal segment models

- **ID:** `oai-r-prediction-and-control-with-temporal-segment-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/prediction-and-control-with-temporal-segment-models/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Improving GANs using optimal transport

- **ID:** `oai-r-improving-gans-using-optimal-transport`
- **Company:** OpenAI
- **Link:** https://openai.com/index/improving-gans-using-optimal-transport/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Implicit generation and generalization methods for energy-based models

- **ID:** `oai-r-energy-based-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/energy-based-models/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### FFJORD: Free-form continuous dynamics for scalable reversible generative models

- **ID:** `oai-r-ffjord`
- **Company:** OpenAI
- **Link:** https://openai.com/index/ffjord/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### On the quantitative analysis of decoder-based generative models

- **ID:** `oai-r-on-the-quantitative-analysis-of-decoder-based-generative-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/on-the-quantitative-analysis-of-decoder-based-generative-models/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Domain randomization and generative models for robotic grasping

- **ID:** `oai-r-domain-randomization-and-generative-models-for-robotic-grasping`
- **Company:** OpenAI
- **Link:** https://openai.com/index/domain-randomization-and-generative-models-for-robotic-grasping/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### In-context Learning and Induction Heads

- **ID:** `ant-r-in-context-learning-and-induction-heads`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/in-context-learning-and-induction-heads
- **Date:** 2022-03-08
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Predictability and Surprise in Large Generative Models

- **ID:** `ant-r-predictability-and-surprise-in-large-generative-models`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/predictability-and-surprise-in-large-generative-models
- **Date:** 2022-02-15
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Interpretable Machine Learning Through Teaching

- **ID:** `oai-r-interpretable-machine-learning-through-teaching`
- **Company:** OpenAI
- **Link:** https://openai.com/index/interpretable-machine-learning-through-teaching/
- **Date:** 2021-03-04
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Teacher-student training framework where iterative (non-joint) training produces interpretable pedagogical examples
- Shows emergent strategies resemble intuitive human teaching
- Validated via human experiments on Mechanical Turk
- Works across rule-based, probabilistic, boolean, and hierarchical concepts
- Matters for interpretable agent-agent communication and human-AI alignment.


### How to train a new language model from scratch using Transformers and Tokenizers

- **ID:** `hf-r-how-to-train`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/how-to-train
- **Date:** 2020-02-14
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Transfer from simulation to real world through learning deep inverse dynamics model

- **ID:** `oai-r-transfer-from-simulation-to-real-world-through-learning-deep-inverse-dynamics-model`
- **Company:** OpenAI
- **Link:** https://openai.com/index/transfer-from-simulation-to-real-world-through-learning-deep-inverse-dynamics-model/
- **Date:** 2019-10-15
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Asymmetric Actor Critic For Image Based Robot Learning

- **ID:** `oai-r-asymmetric-actor-critic-for-image-based-robot-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/asymmetric-actor-critic-for-image-based-robot-learning/
- **Date:** 2019-10-15
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Alphago Zero Starting From Scratch

- **ID:** `dm-r-alphago-zero-starting-from-scratch`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/alphago-zero-starting-from-scratch/
- **Date:** 2017-10-18
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Image GPT

- **ID:** `oai-r-image-gpt`
- **Company:** OpenAI
- **Link:** https://openai.com/index/image-gpt/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Generative models

- **ID:** `oai-r-generative-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/generative-models/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Methodology

- **ID:** `dbx-r-methodology`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/methodology
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- MosaicML research methodology post (Feb 2022) explaining their approach to algorithmic efficiency
- Modifies training recipes (data order, model structure, forward/back-prop) to trade off quality and cost
- Carefully evaluated 20 methods and their compositions in Composer
- Reports speedups of 2.9x on ResNet-50, 3.5x on ResNet-101 (ImageNet), 1.7x on GPT-125 language models
- Matters as methodology reference for how to discover and compose training speedups


### Train Custom GPT + Diffusion Models

- **ID:** `dbx-r-train-custom-gpt-diffusion-models`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/train-custom-gpt-diffusion-models
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


## <a id="model-research-and-applications"></a>Science-applied AI (AlphaFold, health, climate, etc.)

_15 posts_

### Extending single-minus amplitudes to gravitons

- **ID:** `oai-r-extending-single-minus-amplitudes-to-gravitons`
- **Company:** OpenAI
- **Link:** https://openai.com/index/extending-single-minus-amplitudes-to-gravitons/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- OpenAI preprint using GPT-5.2 Pro to derive new scattering-amplitude results in quantum gravity
- Extends gluon single-minus amplitudes to gravitons and shows they are nonzero in a half-collinear regime
- GPT-5.2 Pro produced the derivation (matrix-tree theorem) and draft from the gluon paper as context
- Demonstrates LLM-assisted theoretical physics research
- Matters as case study for AI accelerating mathematical/scientific discovery


### Scaling social science research

- **ID:** `oai-r-scaling-social-science-research`
- **Company:** OpenAI
- **Link:** https://openai.com/index/scaling-social-science-research/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- OpenAI Economic Research Team releases GABRIEL, an open-source Python toolkit using GPT to turn qualitative text/images into quantitative measurements
- Lets researchers describe measures in everyday words and score thousands to millions of documents
- Paper benchmarks GPT labeling accuracy across use cases
- Also supports dataset merging, dedup, passage coding, deidentification
- Matters by making qualitative social-science data analyzable at scale


### Tribe V2 Brain Predictive Foundation Model

- **ID:** `meta-r-tribe-v2-brain-predictive-foundation-model`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/tribe-v2-brain-predictive-foundation-model/
- **Date:** 2026-03-26
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- Meta introduces TRIBE v2, a predictive foundation model that acts as a 'digital twin' of human neural activity
- trained on fMRI data from 700+ volunteers responding to images, podcasts, videos, and text
- claims 70x resolution increase and SOTA speed/accuracy vs similar models
- open-releases model, code, paper, and interactive demo
- aims to let neuroscientists test theories without human subjects and guide AI development from neuroscientific principles.


### Pioneering an AI clinical copilot with Penda Health

- **ID:** `oai-r-ai-clinical-copilot-penda-health`
- **Company:** OpenAI
- **Link:** https://openai.com/index/ai-clinical-copilot-penda-health/
- **Date:** 2026-03-25
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Accelerating life sciences research

- **ID:** `oai-r-accelerating-life-sciences-research-with-retro-biosciences`
- **Company:** OpenAI
- **Link:** https://openai.com/index/accelerating-life-sciences-research-with-retro-biosciences/
- **Date:** 2026-03-25
- **Track:** research
- **Contribution type:** retrospective-case-study

_Summary pending — see link for details._


### OpenAI Research | Publication

- **ID:** `oai-r-publication`
- **Company:** OpenAI
- **Link:** https://openai.com/research/index/publication/
- **Date:** 2026-03-25
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Title-only fallback: this is OpenAI's publication index/listing page, not a single research post
- Acts as a directory aggregating all OpenAI research publications
- Content is a navigation index with filters by type (Publication/Conclusion/Milestone/Release)
- No specific research claim
- Included here for completeness
- title-only.


### WebGPT: Improving the factual accuracy of language models through web browsing

- **ID:** `oai-r-webgpt`
- **Company:** OpenAI
- **Link:** https://openai.com/index/webgpt/
- **Date:** 2024-01-12
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Fine-tunes GPT-3 with a text-based web browser to answer open-ended questions with citations
- Trained via behavior cloning plus reward-modeling with RL/rejection sampling
- Outperforms human demonstrators on ELI5 (56% preference) and beats GPT-3 on TruthfulQA
- Model must search, click, quote, and compose answers with references
- Matters as an early browsing LLM and precursor to modern agentic RAG systems.


### Discovering types for entity disambiguation

- **ID:** `oai-r-discovering-types-for-entity-disambiguation`
- **Company:** OpenAI
- **Link:** https://openai.com/index/discovering-types-for-entity-disambiguation/
- **Date:** 2024-01-12
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Proposes DeepType: entity disambiguation by predicting membership in ~100 automatically-discovered types
- Plays probabilistic 20-questions using type hits to narrow to the correct entity
- Achieves SOTA on CoNLL (YAGO) 94.88% and TAC KBP 2010 90.85%
- Uses Wikipedia links + Wikidata categories + evolutionary search for type system design
- Matters as an early neuro-symbolic approach to knowledge-grounded NLP.


### PixelCNN++: Improving the PixelCNN with discretized logistic mixture likelihood and other modifications

- **ID:** `oai-r-pixelcnn-plus-plus`
- **Company:** OpenAI
- **Link:** https://openai.com/index/pixelcnn-plus-plus/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Point-E: A system for generating 3D point clouds from complex prompts

- **ID:** `oai-r-point-e`
- **Company:** OpenAI
- **Link:** https://openai.com/index/point-e/
- **Date:** 2021-03-04
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Generalizing From Simulation

- **ID:** `oai-r-generalizing-from-simulation`
- **Company:** OpenAI
- **Link:** https://openai.com/index/generalizing-from-simulation/
- **Date:** 2021-01-05
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Sim-to-real transfer of robotic control with dynamics randomization

- **ID:** `oai-r-sim-to-real-transfer-of-robotic-control-with-dynamics-randomization`
- **Company:** OpenAI
- **Link:** https://openai.com/index/sim-to-real-transfer-of-robotic-control-with-dynamics-randomization/
- **Date:** 2019-10-15
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Navigating With Grid Like Representations In Artificial Agents

- **ID:** `dm-r-navigating-with-grid-like-representations-in-artificial-agents`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/navigating-with-grid-like-representations-in-artificial-agents/
- **Date:** 2018-05-09
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- DeepMind shows that artificial agents trained to perform path integration develop grid-cell-like hexagonal representations, matching a neural substrate discovered in mammals (2014 Nobel)
- uses these grid-like units to support vector-based navigation (direct 'as the crow flies' routing) in complex environments
- frames results as evidence that grid cells enable vector-based navigation and as a bridge between deep RL and neuroscience
- best fit is model-research-and-applications (representation learning with neuro analogue) rather than pure agent systems.


### Video generation models as world simulators

- **ID:** `oai-r-video-generation-models-as-world-simulators`
- **Company:** OpenAI
- **Link:** https://openai.com/index/video-generation-models-as-world-simulators/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Meta Fair Updates Agents Robustness Safety Architecture

- **ID:** `meta-r-meta-fair-updates-agents-robustness-safety-architecture`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/meta-fair-updates-agents-robustness-safety-architecture/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- Meta FAIR December 2024 research drop bundling agents, robustness/safety, and architecture work
- headline artifacts include Meta Motivo (foundation model for controlling embodied virtual agents), Meta Video Seal (open-source video watermarking building on Audio Seal), and methods for scaling memory layers
- framed as democratizing SOTA tech via open release
- best fit is model-research-and-applications since it bundles multiple model releases across areas.


## <a id="societal-impact-and-deployment-studies"></a>Societal impact & deployment studies

_18 posts_

### How people are using ChatGPT

- **ID:** `oai-r-how-people-are-using-chatgpt`
- **Company:** OpenAI
- **Link:** https://openai.com/index/how-people-are-using-chatgpt/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Defining and evaluating political bias in LLMs

- **ID:** `oai-r-defining-and-evaluating-political-bias-in-llms`
- **Company:** OpenAI
- **Link:** https://openai.com/index/defining-and-evaluating-political-bias-in-llms/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Operational definition of political bias and ~500-prompt evaluation across 100 topics and 5 bias axes (user invalidation, escalation, personal political expression, asymmetric coverage, political refusals)
- GPT-5 instant/thinking reduce bias 30% vs prior models
- Estimates <0.01% of real production ChatGPT traffic shows political bias
- Uses an LLM grader with detailed rubric
- Matters as a reproducible framework for auditing model objectivity.


### Long-running Claude for scientific computing

- **ID:** `ant-r-long-running-claude`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/long-running-Claude
- **Date:** 2026-03-23
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Vibe physics: The AI grad student

- **ID:** `ant-r-vibe-physics`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/vibe-physics
- **Date:** 2026-03-23
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Labor market impacts of AI: A new measure and early evidence

- **ID:** `ant-r-labor-market-impacts`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/labor-market-impacts
- **Date:** 2026-03-05
- **Authors:** Maxim Massenkoff|Peter McCrory
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### How AI assistance impacts the formation of coding skills

- **ID:** `ant-r-ai-assistance-coding-skills`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/AI-assistance-coding-skills
- **Date:** 2026-01-29
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### The assistant axis: situating and stabilizing the character of large language models

- **ID:** `ant-r-assistant-axis`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/assistant-axis
- **Date:** 2026-01-19
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Project Vend: Phase two

- **ID:** `ant-r-project-vend-2`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/project-vend-2
- **Date:** 2025-12-18
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### How AI Is Transforming Work at Anthropic

- **ID:** `ant-r-how-ai-is-transforming-work-at-anthropic`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- **Date:** 2025-12-02
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Project Fetch: Can Claude train a robot dog?

- **ID:** `ant-r-project-fetch-robot-dog`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/project-fetch-robot-dog
- **Date:** 2025-11-12
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Commitments on model deprecation and preservation

- **ID:** `ant-r-deprecation-commitments`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/deprecation-commitments
- **Date:** 2025-11-04
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Project Vend: Can Claude run a small shop? (And why does that matter?)

- **ID:** `ant-r-project-vend-1`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/project-vend-1
- **Date:** 2025-06-27
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Semi-supervised knowledge transfer for deep learning from private training data

- **ID:** `oai-r-semi-supervised-knowledge-transfer-for-deep-learning-from-private-training-data`
- **Company:** OpenAI
- **Link:** https://openai.com/index/semi-supervised-knowledge-transfer-for-deep-learning-from-private-training-data/
- **Date:** 2024-02-14
- **Track:** research
- **Contribution type:** new-method

**Summary:**

- Introduces PATE (Private Aggregation of Teacher Ensembles) for differentially private deep learning
- Multiple teacher models on disjoint private datasets vote (with noise) to label a student model
- Student never sees the underlying private data or teachers directly
- Achieves SOTA privacy/utility tradeoffs on MNIST and SVHN
- Matters as a landmark DP-ML technique for privacy-preserving training.


### GPTs are GPTs: An early look at the labor market impact potential of large language models

- **ID:** `oai-r-gpts-are-gpts`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gpts-are-gpts/
- **Date:** 2024-01-16
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Understanding the capabilities, limitations, and societal impact of large language models

- **ID:** `oai-r-understanding-the-capabilities-limitations-and-societal-impact-of-large-language-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/understanding-the-capabilities-limitations-and-societal-impact-of-large-language-models/
- **Date:** 2024-01-16
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Early methods for studying affective use and emotional well-being on ChatGPT

- **ID:** `oai-r-affective-use-study`
- **Company:** OpenAI
- **Link:** https://openai.com/index/affective-use-study/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Dream3D

- **ID:** `dbx-r-dream3d`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/dream3d
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Customer spotlight interview with Tony Francis, CEO of Dream3D (AI-powered 3D design tool that replaces traditional rendering with generative models)
- Targets individual designers and in-house teams for rendering existing 3D models into photo-realistic visuals
- Uses MosaicML to train custom models
- Matters as applied generative AI case study, not research
- Classified here as deployment/application study


### Natural Synthetics

- **ID:** `dbx-r-natural-synthetics`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/natural-synthetics
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Customer spotlight interview with Natural Synthetics founders Aakash Sastry and John Mullan about their Hotshot iPhone app ('camera for your imagination')
- Users generate images of themselves, friends, celebrities doing anything via text prompts
- MosaicML helps keep generation costs low enough to offer the app free
- Matters as consumer generative AI deployment case study
- Classified as deployment/application rather than research

