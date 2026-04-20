# Pretraining & Architecture

MoE, SSMs, hybrids, scaling laws, new attention variants, data mixes, tokenizers, curriculum, foundation models.

**Post count:** 234

**Contributors:**

- OpenAI: 93
- Anthropic: 36
- Databricks Mosaic AI: 36
- Meta AI / FAIR: 24
- DeepSeek: 13
- Hugging Face: 12
- Allen Institute for AI: 10
- Cursor: 5
- Thinking Machines: 2
- Cognition: 2
- Google DeepMind: 1

**Subcategories:**

- [Foundation model releases](#foundation-model-releases) (32)
- [Architectures (MoE, SSMs, attention variants)](#architectures) (11)
- [Multimodal pretraining](#multimodal-pretraining) (31)
- [Scaling laws & training dynamics](#scaling-and-training-dynamics) (6)
- [Data & tokenization](#data-and-tokenization) (3)
- [Training stack & infrastructure](#training-stack) (8)
- [Research techniques & methods](#research-techniques-and-methods) (56)
- [Science-applied AI (AlphaFold, health, climate, etc.)](#model-research-and-applications) (7)
- [Societal impact & deployment studies](#societal-impact-and-deployment-studies) (14)
- [Other pretraining & architecture](#fallback-architecture) (66)

---

## <a id="foundation-model-releases"></a>Foundation model releases

_32 posts_

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


### DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

- **ID:** `dsk-r-deepseek-math`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-Math
- **Date:** 2024-02-05
- **Authors:** DeepSeek-AI
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


### Fine-tuning GPT-2 from human preferences

- **ID:** `oai-r-fine-tuning-gpt-2`
- **Company:** OpenAI
- **Link:** https://openai.com/index/fine-tuning-gpt-2/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### gpt-oss-120b & gpt-oss-20b Model Card

- **ID:** `oai-r-gpt-oss-model-card`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gpt-oss-model-card/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### GPT-2: 6-month follow-up

- **ID:** `oai-r-gpt-2-6-month-follow-up`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gpt-2-6-month-follow-up/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

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


### Does Gpt 4 Have Theory Of Mind Capabilities Cd2D766E51A7

- **ID:** `ai2-r-does-gpt-4-have-theory-of-mind-capabilities-cd2d766e51a7`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/does-gpt-4-have-theory-of-mind-capabilities-cd2d766e51a7
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


### Hello Olmo A Truly Open Llm 43F7E7359222

- **ID:** `ai2-r-hello-olmo-a-truly-open-llm-43f7e7359222`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/hello-olmo-a-truly-open-llm-43f7e7359222
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Investigating Pretraining Dynamics And Stability With Olmo Checkpoints Ece6F0C4947A

- **ID:** `ai2-r-investigating-pretraining-dynamics-and-stability-with-olmo-checkpoints-ece6f0c4947a`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/investigating-pretraining-dynamics-and-stability-with-olmo-checkpoints-ece6f0c4947a
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


### Olmo Open Language Model 87Ccfc95F580

- **ID:** `ai2-r-olmo-open-language-model-87ccfc95f580`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/olmo-open-language-model-87ccfc95f580
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="architectures"></a>Architectures (MoE, SSMs, attention variants)

_11 posts_

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


### Welcome Falcon Mamba: The first strong attention-free 7B model

- **ID:** `hf-r-falconmamba`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/falconmamba
- **Date:** 2024-08-12
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


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


### Introducing RWKV - An RNN with the advantages of a transformer

- **ID:** `hf-r-rwkv`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/rwkv
- **Date:** 2023-05-15
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Timesformer A New Architecture For Video Understanding

- **ID:** `meta-r-timesformer-a-new-architecture-for-video-understanding`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/timesformer-a-new-architecture-for-video-understanding/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Olmoe An Open Small And State Of The Art Mixture Of Experts Model C258432D0514

- **ID:** `ai2-r-olmoe-an-open-small-and-state-of-the-art-mixture-of-experts-model-c258432d0514`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/olmoe-an-open-small-and-state-of-the-art-mixture-of-experts-model-c258432d0514
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="multimodal-pretraining"></a>Multimodal pretraining

_31 posts_

### DeepSeek-VL: Towards Real-World Vision-Language Understanding

- **ID:** `dsk-r-deepseek-vl`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-VL
- **Date:** 2024-03-07
- **Authors:** DeepSeek-AI
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


### The Annotated Diffusion Model

- **ID:** `hf-r-annotated-diffusion`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/annotated-diffusion
- **Date:** 2022-06-07
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### DALL·E 3

- **ID:** `oai-r-dall-e-3`
- **Company:** OpenAI
- **Link:** https://openai.com/index/dall-e-3/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Variational Lossy Autoencoder

- **ID:** `oai-r-variational-lossy-autoencoder`
- **Company:** OpenAI
- **Link:** https://openai.com/index/variational-lossy-autoencoder/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### DALL·E 2 pre-training mitigations

- **ID:** `oai-r-dall-e-2-pre-training-mitigations`
- **Company:** OpenAI
- **Link:** https://openai.com/index/dall-e-2-pre-training-mitigations/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Hierarchical text-conditional image generation with CLIP latents

- **ID:** `oai-r-hierarchical-text-conditional-image-generation-with-clip-latents`
- **Company:** OpenAI
- **Link:** https://openai.com/index/hierarchical-text-conditional-image-generation-with-clip-latents/
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


### Sam 3D

- **ID:** `meta-r-sam-3d`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/sam-3d/
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


### Yann Lecun Ai Model I Jepa

- **ID:** `meta-r-yann-lecun-ai-model-i-jepa`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/yann-lecun-ai-model-i-jepa/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="scaling-and-training-dynamics"></a>Scaling laws & training dynamics

_6 posts_

### Emergent introspective awareness in large language models

- **ID:** `ant-r-introspection`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/introspection
- **Date:** 2025-10-29
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


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


### Scaling laws for neural language models

- **ID:** `oai-r-scaling-laws-for-neural-language-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/scaling-laws-for-neural-language-models/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** scaling-laws

_Summary pending — see link for details._


### Toward understanding and preventing misalignment generalization

- **ID:** `oai-r-emergent-misalignment`
- **Company:** OpenAI
- **Link:** https://openai.com/index/emergent-misalignment/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


## <a id="data-and-tokenization"></a>Data & tokenization

_3 posts_

### Teacher–student curriculum learning

- **ID:** `oai-r-teacher-student-curriculum-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/teacher-student-curriculum-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Dolma 3 Trillion Tokens Open Llm Corpus 9A0Ff4B8Da64

- **ID:** `ai2-r-dolma-3-trillion-tokens-open-llm-corpus-9a0ff4b8da64`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/dolma-3-trillion-tokens-open-llm-corpus-9a0ff4b8da64
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Making A Switch Dolma Moves To Odc By 8F0E73852F44

- **ID:** `ai2-r-making-a-switch-dolma-moves-to-odc-by-8f0e73852f44`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/making-a-switch-dolma-moves-to-odc-by-8f0e73852f44
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="training-stack"></a>Training stack & infrastructure

_8 posts_

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


## <a id="research-techniques-and-methods"></a>Research techniques & methods

_56 posts_

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


### MosaicML Satisfies the Need for Speed with MLPerf Results

- **ID:** `dbx-r-mlperf-2022`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mlperf-2022
- **Date:** 2022-06-29
- **Authors:** Bandish Shah|Daya Khudia|Hanlin Tang
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


### How to train a new language model from scratch using Transformers and Tokenizers

- **ID:** `hf-r-how-to-train`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/how-to-train
- **Date:** 2020-02-14
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Prediction and control with temporal segment models

- **ID:** `oai-r-prediction-and-control-with-temporal-segment-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/prediction-and-control-with-temporal-segment-models/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Improving language model behavior by training on a curated dataset

- **ID:** `oai-r-improving-language-model-behavior`
- **Company:** OpenAI
- **Link:** https://openai.com/index/improving-language-model-behavior/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** dataset-benchmark

_Summary pending — see link for details._


### Improving GANs using optimal transport

- **ID:** `oai-r-improving-gans-using-optimal-transport`
- **Company:** OpenAI
- **Link:** https://openai.com/index/improving-gans-using-optimal-transport/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Transfer from simulation to real world through learning deep inverse dynamics model

- **ID:** `oai-r-transfer-from-simulation-to-real-world-through-learning-deep-inverse-dynamics-model`
- **Company:** OpenAI
- **Link:** https://openai.com/index/transfer-from-simulation-to-real-world-through-learning-deep-inverse-dynamics-model/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Consistency Models

- **ID:** `oai-r-consistency-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/consistency-models/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Text and code embeddings by contrastive pre-training

- **ID:** `oai-r-text-and-code-embeddings-by-contrastive-pre-training`
- **Company:** OpenAI
- **Link:** https://openai.com/index/text-and-code-embeddings-by-contrastive-pre-training/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Teaching models to express their uncertainty in words

- **ID:** `oai-r-teaching-models-to-express-their-uncertainty-in-words`
- **Company:** OpenAI
- **Link:** https://openai.com/index/teaching-models-to-express-their-uncertainty-in-words/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Hindsight Experience Replay

- **ID:** `oai-r-hindsight-experience-replay`
- **Company:** OpenAI
- **Link:** https://openai.com/index/hindsight-experience-replay/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Quantifying generalization in reinforcement learning

- **ID:** `oai-r-quantifying-generalization-in-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/quantifying-generalization-in-reinforcement-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Understanding the source of what we see and hear online

- **ID:** `oai-r-understanding-the-source-of-what-we-see-and-hear-online`
- **Company:** OpenAI
- **Link:** https://openai.com/index/understanding-the-source-of-what-we-see-and-hear-online/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Ucb Exploration Via Q Ensembles

- **ID:** `oai-r-ucb-exploration-via-q-ensembles`
- **Company:** OpenAI
- **Link:** https://openai.com/index/ucb-exploration-via-q-ensembles/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Efficient training of language models to fill in the middle

- **ID:** `oai-r-efficient-training-of-language-models-to-fill-in-the-middle`
- **Company:** OpenAI
- **Link:** https://openai.com/index/efficient-training-of-language-models-to-fill-in-the-middle/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Benchmarking safe exploration in deep reinforcement learning

- **ID:** `oai-r-benchmarking-safe-exploration-in-deep-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/benchmarking-safe-exploration-in-deep-reinforcement-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Implicit generation and generalization methods for energy-based models

- **ID:** `oai-r-energy-based-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/energy-based-models/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Some considerations on learning to explore via meta-reinforcement learning

- **ID:** `oai-r-some-considerations-on-learning-to-explore-via-meta-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/some-considerations-on-learning-to-explore-via-meta-reinforcement-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Image GPT

- **ID:** `oai-r-image-gpt`
- **Company:** OpenAI
- **Link:** https://openai.com/index/image-gpt/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Plan online, learn offline: Efficient learning and exploration via model-based control

- **ID:** `oai-r-plan-online-learn-offline`
- **Company:** OpenAI
- **Link:** https://openai.com/index/plan-online-learn-offline/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Generative modeling with sparse transformers

- **ID:** `oai-r-sparse-transformer`
- **Company:** OpenAI
- **Link:** https://openai.com/index/sparse-transformer/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Dota 2 with large scale deep reinforcement learning

- **ID:** `oai-r-dota-2-with-large-scale-deep-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/dota-2-with-large-scale-deep-reinforcement-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### FFJORD: Free-form continuous dynamics for scalable reversible generative models

- **ID:** `oai-r-ffjord`
- **Company:** OpenAI
- **Link:** https://openai.com/index/ffjord/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Variational option discovery algorithms

- **ID:** `oai-r-variational-option-discovery-algorithms`
- **Company:** OpenAI
- **Link:** https://openai.com/index/variational-option-discovery-algorithms/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Multi-Goal Reinforcement Learning: Challenging robotics environments and request for research

- **ID:** `oai-r-multi-goal-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/multi-goal-reinforcement-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Asymmetric Actor Critic For Image Based Robot Learning

- **ID:** `oai-r-asymmetric-actor-critic-for-image-based-robot-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/asymmetric-actor-critic-for-image-based-robot-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### On the quantitative analysis of decoder-based generative models

- **ID:** `oai-r-on-the-quantitative-analysis-of-decoder-based-generative-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/on-the-quantitative-analysis-of-decoder-based-generative-models/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Domain randomization and generative models for robotic grasping

- **ID:** `oai-r-domain-randomization-and-generative-models-for-robotic-grasping`
- **Company:** OpenAI
- **Link:** https://openai.com/index/domain-randomization-and-generative-models-for-robotic-grasping/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### RL²: Fast reinforcement learning via slow reinforcement learning

- **ID:** `oai-r-rl2`
- **Company:** OpenAI
- **Link:** https://openai.com/index/rl2/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Better exploration with parameter noise

- **ID:** `oai-r-better-exploration-with-parameter-noise`
- **Company:** OpenAI
- **Link:** https://openai.com/index/better-exploration-with-parameter-noise/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### #Exploration: A study of count-based exploration for deep reinforcement learning

- **ID:** `oai-r-exploration`
- **Company:** OpenAI
- **Link:** https://openai.com/index/exploration/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Stochastic Neural Networks for hierarchical reinforcement learning

- **ID:** `oai-r-stochastic-neural-networks-for-hierarchical-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/stochastic-neural-networks-for-hierarchical-reinforcement-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Evolution strategies as a scalable alternative to reinforcement learning

- **ID:** `oai-r-evolution-strategies`
- **Company:** OpenAI
- **Link:** https://openai.com/index/evolution-strategies/
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


### Improved Techniques for Training Consistency Models

- **ID:** `oai-r-improved-techniques-for-training-consistency-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/improved-techniques-for-training-consistency-models/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** new-method

_Summary pending — see link for details._


### Early experiments in accelerating science with GPT-5

- **ID:** `oai-r-accelerating-science-gpt-5`
- **Company:** OpenAI
- **Link:** https://openai.com/index/accelerating-science-gpt-5/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Advancing science and math with GPT-5.2

- **ID:** `oai-r-gpt-5-2-for-science-and-math`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gpt-5-2-for-science-and-math/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Why language models hallucinate

- **ID:** `oai-r-why-language-models-hallucinate`
- **Company:** OpenAI
- **Link:** https://openai.com/index/why-language-models-hallucinate/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### GPT-5 lowers the cost of cell-free protein synthesis

- **ID:** `oai-r-gpt-5-lowers-protein-synthesis-cost`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gpt-5-lowers-protein-synthesis-cost/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### GPT-5.2 derives a new result in theoretical physics

- **ID:** `oai-r-new-result-theoretical-physics`
- **Company:** OpenAI
- **Link:** https://openai.com/index/new-result-theoretical-physics/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Train Custom GPT + Diffusion Models

- **ID:** `dbx-r-train-custom-gpt-diffusion-models`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/train-custom-gpt-diffusion-models
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Alphago Zero Starting From Scratch

- **ID:** `dm-r-alphago-zero-starting-from-scratch`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/alphago-zero-starting-from-scratch/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="model-research-and-applications"></a>Science-applied AI (AlphaFold, health, climate, etc.)

_7 posts_

### Pioneering an AI clinical copilot with Penda Health

- **ID:** `oai-r-ai-clinical-copilot-penda-health`
- **Company:** OpenAI
- **Link:** https://openai.com/index/ai-clinical-copilot-penda-health/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Accelerating life sciences research

- **ID:** `oai-r-accelerating-life-sciences-research-with-retro-biosciences`
- **Company:** OpenAI
- **Link:** https://openai.com/index/accelerating-life-sciences-research-with-retro-biosciences/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** retrospective-case-study

_Summary pending — see link for details._


### Point-E: A system for generating 3D point clouds from complex prompts

- **ID:** `oai-r-point-e`
- **Company:** OpenAI
- **Link:** https://openai.com/index/point-e/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Generalizing From Simulation

- **ID:** `oai-r-generalizing-from-simulation`
- **Company:** OpenAI
- **Link:** https://openai.com/index/generalizing-from-simulation/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Sim-to-real transfer of robotic control with dynamics randomization

- **ID:** `oai-r-sim-to-real-transfer-of-robotic-control-with-dynamics-randomization`
- **Company:** OpenAI
- **Link:** https://openai.com/index/sim-to-real-transfer-of-robotic-control-with-dynamics-randomization/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### PixelCNN++: Improving the PixelCNN with discretized logistic mixture likelihood and other modifications

- **ID:** `oai-r-pixelcnn-plus-plus`
- **Company:** OpenAI
- **Link:** https://openai.com/index/pixelcnn-plus-plus/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Video generation models as world simulators

- **ID:** `oai-r-video-generation-models-as-world-simulators`
- **Company:** OpenAI
- **Link:** https://openai.com/index/video-generation-models-as-world-simulators/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


## <a id="societal-impact-and-deployment-studies"></a>Societal impact & deployment studies

_14 posts_

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


### Early methods for studying affective use and emotional well-being on ChatGPT

- **ID:** `oai-r-affective-use-study`
- **Company:** OpenAI
- **Link:** https://openai.com/index/affective-use-study/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### How people are using ChatGPT

- **ID:** `oai-r-how-people-are-using-chatgpt`
- **Company:** OpenAI
- **Link:** https://openai.com/index/how-people-are-using-chatgpt/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### GPTs are GPTs: An early look at the labor market impact potential of large language models

- **ID:** `oai-r-gpts-are-gpts`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gpts-are-gpts/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Understanding the capabilities, limitations, and societal impact of large language models

- **ID:** `oai-r-understanding-the-capabilities-limitations-and-societal-impact-of-large-language-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/understanding-the-capabilities-limitations-and-societal-impact-of-large-language-models/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


## <a id="fallback-architecture"></a>Other pretraining & architecture

_66 posts_

### Better AI models enable more ambitious work

- **ID:** `cur-r-better-models-ambitious-work`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/better-models-ambitious-work
- **Date:** 2026-04-15
- **Authors:** Luke Melas-Kyriazi
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** coding-agents

_Summary pending — see link for details._


### An Early Preview of SWE-1.6 and Research Update

- **ID:** `cog-r-swe-1-6-preview`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/swe-1-6-preview
- **Date:** 2026-03-01
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Towards self-driving codebases

- **ID:** `cur-r-self-driving-codebases`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/self-driving-codebases
- **Date:** 2026-02-05
- **Authors:** Wilson Lin
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Scaling Small LLMs with NVIDIA MPS

- **ID:** `dbx-r-scaling-small-llms-nvidia-mps`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/scaling-small-llms-nvidia-mps
- **Date:** 2026-01-26
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

_Summary pending — see link for details._


### Defeating Nondeterminism in LLM Inference

- **ID:** `tm-r-defeating-nondeterminism-in-llm-inference`
- **Company:** Thinking Machines
- **Link:** https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
- **Date:** 2025-09-10
- **Authors:** Horace He
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### The Power of Fine-Tuning on Your Data: Quick Fixing Bugs with LLMs via Never Ending Learning (NEL)

- **ID:** `dbx-r-power-fine-tuning-your-data-quick-fixing-bugs-llms-never-ending-learning-nel`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/power-fine-tuning-your-data-quick-fixing-bugs-llms-never-ending-learning-nel
- **Date:** 2025-04-08
- **Authors:** Samantha Banchik|Ta-Chung Chi|Sam Havens|Dipendra Misra|Will Tipton|Jan van der Vegt|Matei Zaharia|Emanuel Zgraggen
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Characterizing Datasets and Building Better Models with Continued Pre-Training

- **ID:** `dbx-r-characterizing-datasets-and-building-better-models-continued-pre-training`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/characterizing-datasets-and-building-better-models-continued-pre-training
- **Date:** 2024-11-21
- **Authors:** Mansheej Paul|Brett Larsen|Connor Jennings|Cody Blakeney
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Long Context RAG Performance of LLMs

- **ID:** `dbx-r-long-context-rag-performance-llms`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/long-context-rag-performance-llms
- **Date:** 2024-08-12
- **Authors:** Quinn Leng|Jacob Portes|Sam Havens|Matei Zaharia|Michael Carbin
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** long-context, retrieval-augmentation

_Summary pending — see link for details._


### Optimizing Databricks LLM Pipelines with DSPy

- **ID:** `dbx-r-optimizing-databricks-llm-pipelines-dspy`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/optimizing-databricks-llm-pipelines-dspy
- **Date:** 2024-05-23
- **Authors:** Arnav Singhvi|Daniel Pechi (JetBlue)
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Mapping the Mind of a Large Language Model

- **ID:** `ant-r-mapping-mind-language-model`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/mapping-mind-language-model
- **Date:** 2024-05-21
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Measuring the Persuasiveness of Language Models

- **ID:** `ant-r-measuring-model-persuasiveness`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/measuring-model-persuasiveness
- **Date:** 2024-04-09
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### DSPy on Databricks

- **ID:** `dbx-r-dspy-databricks`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/dspy-databricks
- **Date:** 2024-04-08
- **Authors:** Arnav Singhvi|Michael Carbin|Matei Zaharia
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Evaluating and Mitigating Discrimination in Language Model Decisions

- **ID:** `ant-r-evaluating-and-mitigating-discrimination-in-language-model-decisions`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/evaluating-and-mitigating-discrimination-in-language-model-decisions
- **Date:** 2023-12-07
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Towards Understanding Sycophancy in Language Models

- **ID:** `ant-r-towards-understanding-sycophancy-in-language-models`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models
- **Date:** 2023-10-23
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Decomposing Language Models Into Understandable Components

- **ID:** `ant-r-decomposing-language-models-into-understandable-components`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/decomposing-language-models-into-understandable-components
- **Date:** 2023-10-05
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Towards Monosemanticity: Decomposing Language Models With Dictionary Learning

- **ID:** `ant-r-towards-monosemanticity-decomposing-language-models-with-dictionary-learning`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning
- **Date:** 2023-10-05
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** interpretability-features

_Summary pending — see link for details._


### Challenges in evaluating AI systems

- **ID:** `ant-r-evaluating-ai-systems`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/evaluating-ai-systems
- **Date:** 2023-10-04
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Tracing Model Outputs to the Training Data

- **ID:** `ant-r-influence-functions`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/influence-functions
- **Date:** 2023-08-08
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Measuring Faithfulness in Chain-of-Thought Reasoning

- **ID:** `ant-r-measuring-faithfulness-in-chain-of-thought-reasoning`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning
- **Date:** 2023-07-18
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** chain-of-thought

_Summary pending — see link for details._


### Towards Measuring the Representation of Subjective Global Opinions in Language Models

- **ID:** `ant-r-towards-measuring-the-representation-of-subjective-global-opinions-in-language-models`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models
- **Date:** 2023-06-29
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Interpretability Dreams

- **ID:** `ant-r-interpretability-dreams`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/interpretability-dreams
- **Date:** 2023-05-24
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### The Capacity for Moral Self-Correction in Large Language Models

- **ID:** `ant-r-the-capacity-for-moral-self-correction-in-large-language-models`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/the-capacity-for-moral-self-correction-in-large-language-models
- **Date:** 2023-02-15
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

_Summary pending — see link for details._


### Language Models (Mostly) Know What They Know

- **ID:** `ant-r-language-models-mostly-know-what-they-know`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/language-models-mostly-know-what-they-know
- **Date:** 2022-07-11
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Softmax Linear Units

- **ID:** `ant-r-softmax-linear-units`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/softmax-linear-units
- **Date:** 2022-06-17
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

_Summary pending — see link for details._


### AI and efficiency

- **ID:** `oai-r-ai-and-efficiency`
- **Company:** OpenAI
- **Link:** https://openai.com/index/ai-and-efficiency/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Computational limitations in robust classification and win-win results

- **ID:** `oai-r-computational-limitations-in-robust-classification-and-win-win-results`
- **Company:** OpenAI
- **Link:** https://openai.com/index/computational-limitations-in-robust-classification-and-win-win-results/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Preparing for malicious uses of AI

- **ID:** `oai-r-preparing-for-malicious-uses-of-ai`
- **Company:** OpenAI
- **Link:** https://openai.com/index/preparing-for-malicious-uses-of-ai/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Language models can explain neurons in language models

- **ID:** `oai-r-language-models-can-explain-neurons-in-language-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/language-models-can-explain-neurons-in-language-models/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Techniques for training large neural networks

- **ID:** `oai-r-techniques-for-training-large-neural-networks`
- **Company:** OpenAI
- **Link:** https://openai.com/index/techniques-for-training-large-neural-networks/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Evolution through large models

- **ID:** `oai-r-evolution-through-large-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/evolution-through-large-models/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Measuring Goodhart’s law

- **ID:** `oai-r-measuring-goodharts-law`
- **Company:** OpenAI
- **Link:** https://openai.com/index/measuring-goodharts-law/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### WebGPT: Improving the factual accuracy of language models through web browsing

- **ID:** `oai-r-webgpt`
- **Company:** OpenAI
- **Link:** https://openai.com/index/webgpt/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Deep double descent

- **ID:** `oai-r-deep-double-descent`
- **Company:** OpenAI
- **Link:** https://openai.com/index/deep-double-descent/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Improving verifiability in AI development

- **ID:** `oai-r-improving-verifiability`
- **Company:** OpenAI
- **Link:** https://openai.com/index/improving-verifiability/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Testing robustness against unforeseen adversaries

- **ID:** `oai-r-testing-robustness`
- **Company:** OpenAI
- **Link:** https://openai.com/index/testing-robustness/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Learning concepts with energy functions

- **ID:** `oai-r-learning-concepts-with-energy-functions`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-concepts-with-energy-functions/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Large-scale study of curiosity-driven learning

- **ID:** `oai-r-large-scale-study-of-curiosity-driven-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/large-scale-study-of-curiosity-driven-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Discovering types for entity disambiguation

- **ID:** `oai-r-discovering-types-for-entity-disambiguation`
- **Company:** OpenAI
- **Link:** https://openai.com/index/discovering-types-for-entity-disambiguation/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Estimating worst case frontier risks of open weight LLMs

- **ID:** `oai-r-estimating-worst-case-frontier-risks-of-open-weight-llms`
- **Company:** OpenAI
- **Link:** https://openai.com/index/estimating-worst-case-frontier-risks-of-open-weight-llms/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Interpretable Machine Learning Through Teaching

- **ID:** `oai-r-interpretable-machine-learning-through-teaching`
- **Company:** OpenAI
- **Link:** https://openai.com/index/interpretable-machine-learning-through-teaching/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Learning to model other minds

- **ID:** `oai-r-learning-to-model-other-minds`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-to-model-other-minds/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Learning sparse neural networks through L₀ regularization

- **ID:** `oai-r-learning-sparse-neural-networks-through-l0-regularization`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-sparse-neural-networks-through-l0-regularization/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Interpretable and pedagogical examples

- **ID:** `oai-r-interpretable-and-pedagogical-examples`
- **Company:** OpenAI
- **Link:** https://openai.com/index/interpretable-and-pedagogical-examples/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Semi-supervised knowledge transfer for deep learning from private training data

- **ID:** `oai-r-semi-supervised-knowledge-transfer-for-deep-learning-from-private-training-data`
- **Company:** OpenAI
- **Link:** https://openai.com/index/semi-supervised-knowledge-transfer-for-deep-learning-from-private-training-data/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** new-method

_Summary pending — see link for details._


### Learning with opponent-learning awareness

- **ID:** `oai-r-learning-with-opponent-learning-awareness`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-with-opponent-learning-awareness/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Learning to cooperate, compete, and communicate

- **ID:** `oai-r-learning-to-cooperate-compete-and-communicate`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-to-cooperate-compete-and-communicate/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Extensions and limitations of the neural GPU

- **ID:** `oai-r-extensions-and-limitations-of-the-neural-gpu`
- **Company:** OpenAI
- **Link:** https://openai.com/index/extensions-and-limitations-of-the-neural-gpu/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Weight normalization: A simple reparameterization to accelerate training of deep neural networks

- **ID:** `oai-r-weight-normalization`
- **Company:** OpenAI
- **Link:** https://openai.com/index/weight-normalization/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### A Holistic Approach to Undesired Content Detection in the Real World

- **ID:** `oai-r-a-holistic-approach-to-undesired-content-detection-in-the-real-world`
- **Company:** OpenAI
- **Link:** https://openai.com/index/a-holistic-approach-to-undesired-content-detection-in-the-real-world/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Learning a hierarchy

- **ID:** `oai-r-learning-a-hierarchy`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-a-hierarchy/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Defining and evaluating political bias in LLMs

- **ID:** `oai-r-defining-and-evaluating-political-bias-in-llms`
- **Company:** OpenAI
- **Link:** https://openai.com/index/defining-and-evaluating-political-bias-in-llms/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### OpenAI Research | Publication

- **ID:** `oai-r-publication`
- **Company:** OpenAI
- **Link:** https://openai.com/research/index/publication/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Improving mathematical reasoning with process supervision

- **ID:** `oai-r-improving-mathematical-reasoning-with-process-supervision`
- **Company:** OpenAI
- **Link:** https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Reasoning models struggle to control their chains of thought, and that’s good

- **ID:** `oai-r-reasoning-models-chain-of-thought-controllability`
- **Company:** OpenAI
- **Link:** https://openai.com/index/reasoning-models-chain-of-thought-controllability/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** chain-of-thought

_Summary pending — see link for details._


### Extending single-minus amplitudes to gravitons

- **ID:** `oai-r-extending-single-minus-amplitudes-to-gravitons`
- **Company:** OpenAI
- **Link:** https://openai.com/index/extending-single-minus-amplitudes-to-gravitons/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Scaling social science research

- **ID:** `oai-r-scaling-social-science-research`
- **Company:** OpenAI
- **Link:** https://openai.com/index/scaling-social-science-research/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### 5 Best Practices for Efficient Model Training

- **ID:** `dbx-r-5-best-practices-for-efficient-model-training`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/5-best-practices-for-efficient-model-training
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Best Practices (Dec 2021)

- **ID:** `dbx-r-best-practices-dec-2021`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/best-practices-dec-2021
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

_Summary pending — see link for details._


### Making ML Training Efficient Algorithmically

- **ID:** `dbx-r-making-ml-training-efficient-algorithmically`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/making-ml-training-efficient-algorithmically
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

_Summary pending — see link for details._


### Natural Synthetics

- **ID:** `dbx-r-natural-synthetics`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/natural-synthetics
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Tribe V2 Brain Predictive Foundation Model

- **ID:** `meta-r-tribe-v2-brain-predictive-foundation-model`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/tribe-v2-brain-predictive-foundation-model/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._

