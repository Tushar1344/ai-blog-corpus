# Pretraining & Architecture

MoE, SSMs, hybrids, scaling laws, new attention variants, data mixes, tokenizers, curriculum, foundation models.

**Post count:** 475

**Contributors:**

- AI21 Labs: 109
- OpenAI: 79
- Mistral AI: 67
- Qwen (Alibaba): 43
- Sakana AI: 32
- Databricks Mosaic AI: 31
- Meta AI / FAIR: 24
- Anthropic: 23
- DeepSeek: 20
- Moonshot (Kimi): 16
- Hugging Face: 12
- Allen Institute for AI: 10
- Cursor: 3
- Thinking Machines: 2
- Cognition: 2
- Google DeepMind: 1
- LangChain: 1

**Subcategories:**

- [Foundation model releases](#foundation-model-releases) (68)
- [Architectures (MoE, SSMs, attention variants)](#architectures) (20)
- [Multimodal pretraining](#multimodal-pretraining) (37)
- [Scaling laws & training dynamics](#scaling-and-training-dynamics) (5)
- [Data & tokenization](#data-and-tokenization) (2)
- [Training stack & infrastructure](#training-stack) (6)
- [Research techniques & methods](#research-techniques-and-methods) (53)
- [Science-applied AI (AlphaFold, health, climate, etc.)](#model-research-and-applications) (23)
- [Societal impact & deployment studies](#societal-impact-and-deployment-studies) (14)
- [Other pretraining & architecture](#fallback-architecture) (211)

---

## <a id="foundation-model-releases"></a>Foundation model releases

_68 posts_

### gpt-oss-120b & gpt-oss-20b Model Card

- **ID:** `oai-r-gpt-oss-model-card`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gpt-oss-model-card/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- OpenAI releases gpt-oss-120b and gpt-oss-20b open-weight reasoning models under Apache 2.0
- Text-only, tool-use capable, structured output, adjustable reasoning effort, full chain-of-thought
- Safety analysis: default 120B does NOT reach High thresholds in Preparedness Framework (Bio/Chem, Cyber, AI Self-Improvement)
- Adversarial fine-tuning also doesn't push it past High capability
- Releasing it doesn't substantially advance open-model biological frontier since existing open models already match its adversarial performance
- Documents OpenAI's framework for releasing open-weights responsibly


### DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning

- **ID:** `dsk-r-deepseek-math-v2`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-Math-V2
- **Date:** 2025-11-27
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- DeepSeekMath-V2 targets self-verifiable mathematical reasoning rather than final-answer accuracy alone
- Trains an LLM verifier and uses it as a reward model for a proof generator incentivized to self-critique
- Achieves gold-level scores on IMO 2025 and CMO 2024, and 118/120 on Putnam 2024
- Argues final-answer RL saturates AIME/HMMT without ensuring correct reasoning
- Release includes inference code and models.


### Qwen-Image-Edit: Image Editing with Higher Quality and Efficiency

- **ID:** `qw-r-qwen-image-edit`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen-image-edit/
- **Date:** 2025-08-19
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Alibaba releases Qwen-Image-Edit built on 20B Qwen-Image, combining Qwen2.5-VL for semantic control with VAE encoder for appearance control, enabling both low-level (add/remove/modify pixels) and high-level (IP creation, rotation, style transfer) editing
- Precise bilingual (Chinese+English) text editing preserving font/size/style
- SOTA on public benchmarks for image editing
- Use cases: MBTI emoji packs, novel view synthesis (90°/180° rotation), Ghibli-style transfer, calligraphy error correction via chained editing with bounding boxes
- Available via Qwen Chat, HuggingFace, ModelScope


### Claude Opus 4 and 4.1 can now end a rare subset of conversations

- **ID:** `ant-r-end-subset-conversations`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/end-subset-conversations
- **Date:** 2025-08-15
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

**Summary:**

- Describes a welfare-motivated feature letting Claude Opus 4/4.1 end conversations after repeated abusive/harmful user interactions
- Triggered only as last resort after Claude has redirected multiple times
- Users can start new chats or edit prior messages
- Preliminary welfare assessment found Claude shows aversion and apparent distress with harmful content
- Policy/welfare post rather than research—short-read, low novelty but concrete deployment signal.


### Qwen-Image: Crafting with Native Text Rendering

- **ID:** `qw-r-qwen-image`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen-image/
- **Date:** 2025-08-04
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Alibaba releases Qwen-Image, a 20B MMDiT image foundation model with SOTA cross-benchmark performance and uniquely strong bilingual text rendering for Chinese and English
- Excels at multi-line layouts, paragraph-level text semantics, small-font text, and mixed Chinese/English—outperforming SOTA on LongText-Bench, ChineseWord, TextCraft
- Multi-task training paradigm improves semantic and visual consistency in image editing
- Particularly useful for posters, infographics, signs, couplets where text precision matters
- Model weights on HuggingFace/ModelScope, demo on Qwen Chat


### Qwen-MT: Where Speed Meets Smart Translation

- **ID:** `qw-r-qwen-mt`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen-mt/
- **Date:** 2025-07-24
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Qwen-MT (qwen-mt-turbo) is a lightweight MoE translation model built on Qwen3 supporting 92 languages/dialects covering 95%+ of world population at $0.5 per million output tokens
- Customization: terminology intervention, domain prompts, translation memory via translation_options API param
- Outperforms GPT-4.1-mini, Gemini-2.5-Flash, Qwen3-8B on WMT24 and multi-domain CN-EN/EN-DE benchmarks
- Competitive with GPT-4.1 and Gemini-2.5-Pro
- Human eval across 10 languages confirms high acceptance/excellence rates
- OpenAI-compatible API via DashScope


### Qwen VLo: From "Understanding" the World to "Depicting" It

- **ID:** `qw-r-qwen-vlo`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen-vlo/
- **Date:** 2025-06-26
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- Alibaba previews Qwen VLo, a unified multimodal understanding+generation model that can both interpret images and generate/edit them with progressive left-to-right top-to-bottom refinement
- Supports open-ended natural-language instruction editing (style transfer to Van Gogh/Ghibli/pixel/Minecraft, object swap, background change, text edits) plus traditional perception tasks (depth/segmentation/detection maps) via same editing interface
- Multilingual instructions (Chinese+English)
- Available in Qwen Chat as preview
- Better semantic consistency than previous models on color-change/object-preservation edits


### DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning

- **ID:** `dsk-r-deepseek-prover-v2`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-Prover-V2
- **Date:** 2025-04-30
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- DeepSeek-Prover-V2 formal-math LLM built atop DeepSeek-V3 with recursive subgoal decomposition: V3 sketches informal proof, 7B prover resolves subgoals, results get composed
- Cold-start dataset pairs formal Lean proofs with V3 chain-of-thought, followed by binary-reward RL
- 671B model reaches 88.9% pass on MiniF2F-test and solves 49/658 PutnamBench problems
- Introduces ProverBench (325 problems incl. AIME 24/25) for broader evaluation
- Releases both 7B and 671B weights and dataset


### How to deploy and fine-tune DeepSeek models on AWS

- **ID:** `hf-r-deepseek-r1-aws`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/deepseek-r1-aws
- **Date:** 2025-01-30
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- Running document for deploying and fine-tuning DeepSeek R1 and its 6 distilled variants (Llama/Qwen 1.5B-70B) on AWS via HF Inference Endpoints, Amazon Bedrock Marketplace, SageMaker AI, and EC2 Neuron (Trainium/Inferentia)
- Recommended hardware: ml.g6.48xlarge (8 GPUs) for 70B distills, ml.inf2.48xlarge for Neuron, Unsloth GGUF quant for Inference Endpoints at $8.3/hr
- Takeaway: operational guide for AWS deployment with Python code examples for each path
- TGI v3 auto-selects performant params
- Fine-tuning via Training DLCs or Neuron AMI


### Open-R1: a fully open reproduction of DeepSeek-R1

- **ID:** `hf-r-open-r1`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/open-r1
- **Date:** 2025-01-28
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- HuggingFace announces Open-R1, a fully open reproduction of DeepSeek-R1 (data, code, training pipeline)
- Plan: Step 1 distill reasoning dataset from R1, Step 2 replicate pure RL pipeline for R1-Zero with GRPO, Step 3 multi-stage SFT→RL recipe
- No evaluation numbers in this intro post—critics noted this
- Community-driven approach aims to release missing pieces (datasets, training code) alongside lessons-learned
- Foundational post, not a results report


### Qwen2.5-1M: Deploy Your Own Qwen with Context Length up to 1M Tokens

- **ID:** `qw-r-qwen2.5-1m`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2.5-1m/
- **Date:** 2025-01-27
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- Alibaba open-sources Qwen2.5-7B/14B-Instruct-1M with 1M-token context plus a vLLM-based inference framework 3-7x faster via sparse attention on prefill
- Training pipeline: gradual 4K→256K pretraining with RoPE base 10k→10M, two-stage SFT (short then mixed short+long), RLHF on 8K
- Extends to 1M via Dual Chunk Attention (no training) which remaps relative positions
- Perfect passkey retrieval at 1M
- Qwen2.5-14B-Instruct-1M beats GPT-4o-mini on long-context
- Sparse attention via MInference+chunked prefill (71GB→2.3GB VRAM activations on 7B) + refined sparsity config + dynamic chunked pipeline parallelism
- 3.2-6.7x prefill acceleration


### DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- **ID:** `dsk-r-deepseek-r1`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-R1
- **Date:** 2025-01-20
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- DeepSeek-R1 reasoning models: R1-Zero trained purely via RL on V3-Base (no SFT), R1 adds cold-start SFT for readability before RL
- Demonstrates reasoning capabilities can emerge purely from RL without SFT—a first-of-its-kind open result
- R1 matches o1-1217 on math/code: AIME 79.8, MATH-500 97.3, Codeforces 96.3 percentile, SWE-Verified 49.2
- Open-sources six distilled dense models (1.5B-70B) based on Qwen/Llama—Distill-Qwen-32B beats o1-mini
- Recommends temperature 0.5-0.7, no system prompt, force '<think>\n' prefix


### DeepSeek-V3 Technical Report

- **ID:** `dsk-r-deepseek-v3`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-V3
- **Date:** 2024-12-26
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- DeepSeek-V3 technical report for a 671B-parameter (37B active) MoE base model with MLA attention
- Pioneers auxiliary-loss-free load balancing, FP8 mixed-precision training, and multi-token-prediction objective
- Achieves GPT-4o/Claude 3.5-Sonnet-class performance trained with only 2.788M H800 GPU hours on 14.8T tokens
- Post-training distills reasoning from DeepSeek-R1 into V3
- Training was remarkably stable with zero irrecoverable loss spikes or rollbacks


### The Long Context RAG Capabilities of OpenAI o1 and Google Gemini

- **ID:** `dbx-r-long-context-rag-capabilities-openai-o1-and-google-gemini`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/long-context-rag-capabilities-openai-o1-and-google-gemini
- **Date:** 2024-10-08
- **Authors:** Quinn Leng|Jacob Portes|Sam Havens|Matei Zaharia|Michael Carbin
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=H (priority 8.7)
- **Techniques:** long-context, test-time-compute, retrieval-augmentation

**Summary:**

- Benchmarks o1 and Gemini 1.5 on long-context RAG
- o1 sets new SOTA
- Gemini 1.5 holds performance up to 2M tokens
- Shows how reasoning-time compute (o1) improves RAG accuracy vs long-context-only scaling
- Characterizes distinct long-context failure modes across model families
- Up-to-date model selection guidance for RAG pipelines
- Practical reference for builders choosing between long-context vs retrieval-heavy architectures


### DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search

- **ID:** `dsk-r-deepseek-prover-v1.5`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-Prover-V1.5
- **Date:** 2024-08-15
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Lean-4 theorem prover LLM extending Prover-V1 with RL from proof-assistant feedback (RLPAF) and RMaxTS, an intrinsic-reward Monte-Carlo tree search
- Base model pretrained on DeepSeekMath, SFT on enhanced formal dataset, then RL
- New SOTA on miniF2F-test 63.5% and ProofNet 25.3% vs prior 54.5%/18.1%
- Combines whole-proof generation with tree search to diversify proof paths
- Open-source 7B Base/SFT/RL checkpoints plus training code


### WWDC 24: Running Mistral 7B with Core ML

- **ID:** `hf-r-mistral-coreml`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/mistral-coreml
- **Date:** 2024-07-22
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=L/A=H (priority 7.5)

**Summary:**

- Tutorial running Mistral 7B on Apple Silicon using Core ML, leveraging WWDC'24 features (MLTensor, Stateful Buffers, block-wise quantization) via swift-transformers
- Block-wise 4-bit palletization shrinks models 8x vs float32 without big quality loss
- Stateful Buffers enable efficient KV-cache on GPU avoiding memory-bandwidth overhead on each forward pass
- Runs 7B model in <4GB memory on a Mac with swift CLI
- MLTensor replaces MLMultiArray with Python-numpy-like high-level ops including softmax/argmax
- Apple's vertically-integrated Core ML stack targets CPU/GPU/Neural Engine across Apple Intelligence features


### SmolLM - blazingly fast and remarkably powerful

- **ID:** `hf-r-smollm`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/smollm
- **Date:** 2024-07-16
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- SmolLM family (135M/360M/1.7B) trained on the curated SmolLM-Corpus of Cosmopedia v2 (28B synthetic tokens), Python-Edu (4B), FineWeb-Edu (220B deduped)
- SmolLM-1.7B beats Phi-1.5 and Qwen2-1.5B in size category
- 135M beats MobileLM-125M despite 600B vs 1T tokens
- Uses trapezoidal LR schedule, GQA, embedding tying
- Focus on on-device use—ONNX checkpoints, WebGPU demos
- Deep dive into prompt engineering for synthetic data diversity (BISAC topics, audience/style variation)


### DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence

- **ID:** `dsk-r-deepseek-coder-v2`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-Coder-V2
- **Date:** 2024-06-14
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- DeepSeek-Coder-V2 open-source MoE code model (236B/21B active, also 16B/2.4B Lite) continued-pretrained on 6T additional tokens from DeepSeek-V2
- Expands language support 86→338 and context 16K→128K, matching or beating GPT-4-Turbo, Claude-3-Opus, Gemini-1.5-Pro on coding/math benchmarks
- Scores 90.2 HumanEval, 75.4 MBPP+, 43.4 LiveCodeBench and 12.1 USACO
- Actionable open commercial license plus vLLM/SGLang deployment recipes
- Reasoning gains preserved on general NL tasks (MMLU 79.2)


### DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model

- **ID:** `dsk-r-deepseek-v2`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-V2
- **Date:** 2024-04-22
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- DeepSeek-V2 MoE model (236B total/21B active) introducing Multi-head Latent Attention (MLA) which compresses KV cache by 93.3%
- Cuts training cost by 42.5% and boosts inference throughput 5.76x vs DeepSeek-67B
- Pretrained on 8.1T tokens with 128K context, competitive with LLaMA3-70B and Mixtral-8x22B on standard benchmarks
- Lite variant (16B/2.4B) runs economically while beating DeepSeek-7B and DeepSeekMoE-16B
- MLA + DeepSeekMoE architecture validated and reused in V3


### DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

- **ID:** `dsk-r-deepseek-math`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-Math
- **Date:** 2024-02-05
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- DeepSeekMath 7B pushes open-model math reasoning: 51.7% on competition MATH (close to GPT-4/Gemini-Ultra) via continued pretraining from DeepSeek-Coder on a large math corpus
- Introduces GRPO RL method (later reused in R1)
- Surpasses Minerva 540B while being dramatically smaller
- Covers self-contained solutions, tool use, and formal theorem proving
- Influential open math model.


### Introducing Qwen-VL

- **ID:** `qw-r-qwen-vl`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen-vl/
- **Date:** 2024-01-25
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- January 2024 launch notes for Qwen-VL-Plus and Qwen-VL-Max, closed-source multimodal upgrades performing on par with Gemini Ultra/GPT-4V on DocVQA (93.1% Max), ChartQA, AI2D, TextVQA
- Qwen-VL-Max outperforms GPT-4V and Gemini on Chinese QA and Chinese text comprehension
- Supports >1M-pixel images at arbitrary aspect ratios
- Capabilities: celebrity/landmark recognition, multilingual poetry, grounded Q&A, visual-agent-style object localization, autonomous-driving-style visual reasoning
- Marks transition from open-source Qwen-VL to closed flagship VL models


### Introducing Qwen

- **ID:** `qw-r-qwen`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen/
- **Date:** 2024-01-23
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=L/A=H (priority 7.5)

**Summary:**

- January 2024 overview of the Qwen series: base LMs (1.8B/7B/14B/72B open-sourced) pretrained on 2-3T multilingual tokens with 32K context via continual pretraining + RoPE base scaling
- Post-training uses quality-controlled SFT + RLHF with careful reward-model pretraining
- Qwen-72B claims competitive performance vs Llama 2, GPT-3.5, and GPT-4 on L-Eval + Needle-in-Haystack
- Tool use via ReAct-format data labeling enables function calling, code interpreter, and HF agent integrations
- AgentFabric (GPTs-like) lets users configure agents via chat
- High-efficiency multilingual tokenizer


### DeepSeek LLM: Scaling Open-Source Language Models with Longtermism

- **ID:** `dsk-r-deepseek-llm`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-LLM
- **Date:** 2023-11-29
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=M/A=M (priority 7.7)

**Summary:**

- DeepSeek LLM 7B/67B base+chat release
- 67B Base outperforms Llama-2 70B on reasoning, coding, math, and Chinese
- 67B Chat hits HumanEval pass@1 73%+ and surpasses GPT-3.5 on several benchmarks
- Open source under permissive license
- Written as 'Scaling Open-Source Language Models with Longtermism'
- Early DeepSeek milestone preceding V2/V3/R1.


### DeepSeek-Coder: When the Large Language Model Meets Programming

- **ID:** `dsk-r-deepseek-coder`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-Coder
- **Date:** 2023-10-20
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- DeepSeek-Coder: family of code LLMs (1B/5.7B/6.7B/33B) trained from scratch on 2T tokens (87% code, 13% NL in English+Chinese)
- 16K context with fill-in-the-blank
- SOTA open-source performance on HumanEval, MultiPL-E, MBPP, DS-1000, APPS
- Project-level pretraining corpus supports cross-file completion
- Repo with models and demo
- Foundational open coding model release.


### Mistral 7B | Mistral AI | Frontier AI in your hands

- **ID:** `mt-r-announcing-mistral-7b`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/announcing-mistral-7b/
- **Date:** 2023-09-27
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=H (priority 6.5)

_Summary pending — see link for details._


### Announcing MPT-7B-8K: 8K Context Length for Document Understanding

- **ID:** `dbx-r-long-context-mpt-7b-8k`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/long-context-mpt-7b-8k
- **Date:** 2023-07-18
- **Authors:** Sam Havens|Erica Ji Yuen
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=L/N=L/A=H (priority 5.3)
- **Techniques:** long-context

_Summary pending — see link for details._


### MPT-30B: Raising the bar for open-source foundation models

- **ID:** `dbx-r-mpt-30b`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mpt-30b
- **Date:** 2023-06-22
- **Track:** research
- **Contribution type:** infra-release
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- Databricks releases MPT-30B, an Apache-2.0 decoder-only transformer with 8K context, trained partly on H100s, that exceeds GPT-3 quality with 17% of its parameters and 60% of its FLOPs
- Key features: ALiBi for long-context extrapolation, FlashAttention, fits on single A100-80GB in bf16 or A100-40GB in 8-bit, plus Instruct/Chat variants
- Strong programming ability via code-heavy pretraining mix
- MPT-30B is first public model partly trained on H100s showing 2.44x per-GPU throughput vs A100
- Trained over 2 months with >46% MFU
- MPT-30B-Chat beats all tested models on HumanEval except WizardCoder


### Going Beyond Chatbots: How to Make GPT-4 Output Structured Data Using LangChain

- **ID:** `lc-r-going-beyond-chatbots-how-to-make-gpt-4-output-structured-data-using-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/going-beyond-chatbots-how-to-make-gpt-4-output-structured-data-using-langchain
- **Date:** 2023-05-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=L/A=H (priority 7.5)

**Summary:**

- 2023 guide using LangChainJS StructuredOutputParser + OutputFixingParser to reliably get Zod-schema-validated JSON from GPT-4
- OutputFixingParser uses a second LLM call to recover badly-formatted outputs, letting you pipe directly into APIs like Airtable
- Takeaway for 2026: structured output is now native in most APIs, but technique of LLM-based output repair still useful
- Use .describe() on Zod schemas to give LLM field context
- Different model instances (temps) for parser vs main chain works well
- Now largely superseded by native structured output features


### Extracting Concepts from GPT-4

- **ID:** `oai-r-extracting-concepts-from-gpt-4`
- **Company:** OpenAI
- **Link:** https://openai.com/index/extracting-concepts-from-gpt-4/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Finding GPT-4’s mistakes with GPT-4

- **ID:** `oai-r-finding-gpt4s-mistakes-with-gpt-4`
- **Company:** OpenAI
- **Link:** https://openai.com/index/finding-gpt4s-mistakes-with-gpt-4/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Llama 2 3 Meditron Yale Medicine Epfl Open Source Llm

- **ID:** `meta-r-llama-2-3-meditron-yale-medicine-epfl-open-source-llm`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/llama-2-3-meditron-yale-medicine-epfl-open-source-llm/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Does Gpt 4 Have Theory Of Mind Capabilities Cd2D766E51A7

- **ID:** `ai2-r-does-gpt-4-have-theory-of-mind-capabilities-cd2d766e51a7`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/does-gpt-4-have-theory-of-mind-capabilities-cd2d766e51a7
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

_Summary pending — see link for details._


### Gpt 4 Theory Of Mind

- **ID:** `ai2-r-gpt-4-theory-of-mind`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/gpt-4-theory-of-mind
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

_Summary pending — see link for details._


### Hello Olmo

- **ID:** `ai2-r-hello-olmo`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/hello-olmo
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Hello Olmo A Truly Open Llm 43F7E7359222

- **ID:** `ai2-r-hello-olmo-a-truly-open-llm-43f7e7359222`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/hello-olmo-a-truly-open-llm-43f7e7359222
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Investigating Pretraining Dynamics And Stability With Olmo Checkpoints Ece6F0C4947A

- **ID:** `ai2-r-investigating-pretraining-dynamics-and-stability-with-olmo-checkpoints-ece6f0c4947a`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/investigating-pretraining-dynamics-and-stability-with-olmo-checkpoints-ece6f0c4947a
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Olmo

- **ID:** `ai2-r-olmo`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/olmo
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Olmo Open Language Model 87Ccfc95F580

- **ID:** `ai2-r-olmo-open-language-model-87ccfc95f580`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/olmo-open-language-model-87ccfc95f580
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Le Chat Mistral

- **ID:** `mt-r-le-chat-mistral`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/le-chat-mistral/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Mistral 3

- **ID:** `mt-r-mistral-3`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-3/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Mistral Afp

- **ID:** `mt-r-mistral-afp`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-afp/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Mistral Ai And Nvidia Partner To Accelerate Open Frontier Models

- **ID:** `mt-r-mistral-ai-and-nvidia-partner-to-accelerate-open-frontier-models`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-ai-and-nvidia-partner-to-accelerate-open-frontier-models/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Mistral Ai Non Production License Mnpl

- **ID:** `mt-r-mistral-ai-non-production-license-mnpl`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-ai-non-production-license-mnpl/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Mistral Ai Raises 1 7 B To Accelerate Technological Progress With Ai

- **ID:** `mt-r-mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Mistral Chat

- **ID:** `mt-r-mistral-chat`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-chat/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Mistral Code

- **ID:** `mt-r-mistral-code`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-code/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Mistral Compute

- **ID:** `mt-r-mistral-compute`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-compute/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Mistral Large

- **ID:** `mt-r-mistral-large`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-large/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Mistral Large 2

- **ID:** `mt-r-mistral-large-2`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-large-2/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Mistral Large 2407

- **ID:** `mt-r-mistral-large-2407`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-large-2407/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Mistral Medium 3

- **ID:** `mt-r-mistral-medium-3`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-medium-3/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Mistral Moderation

- **ID:** `mt-r-mistral-moderation`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-moderation/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Mistral Nemo

- **ID:** `mt-r-mistral-nemo`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-nemo/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Mistral Nemo4

- **ID:** `mt-r-mistral-nemo4`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-nemo4/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Mistral Ocr

- **ID:** `mt-r-mistral-ocr`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-ocr/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Mistral Ocr 3

- **ID:** `mt-r-mistral-ocr-3`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-ocr-3/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Mistral S

- **ID:** `mt-r-mistral-s`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-s/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Mistral Saba

- **ID:** `mt-r-mistral-saba`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-saba/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Mistral Small 3

- **ID:** `mt-r-mistral-small-3`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-small-3/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Mistral Small 3 1

- **ID:** `mt-r-mistral-small-3-1`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-small-3-1/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Mistral Small 4

- **ID:** `mt-r-mistral-small-4`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-small-4/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Mistral Vibe 2 0

- **ID:** `mt-r-mistral-vibe-2-0`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mistral-vibe-2-0/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Announcing Jamba

- **ID:** `a21-r-announcing-jamba`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/announcing-jamba/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Announcing Jamba Instruct

- **ID:** `a21-r-announcing-jamba-instruct`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/announcing-jamba-instruct/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Announcing Jamba Model Family

- **ID:** `a21-r-announcing-jamba-model-family`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/announcing-jamba-model-family/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Introducing Jamba 1 6

- **ID:** `a21-r-introducing-jamba-1-6`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/introducing-jamba-1-6/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=H/A=M (priority 7.8)

**Summary:**

- Jamba 1.6 (Mar 2025): leading open SSM-Transformer hybrid at 256K context window, best open model for private enterprise deployment
- Jamba Large outperforms Mistral Large 2, Llama 3.3 70B, Command R+
- Jamba Mini beats Ministral 8B, Llama 3.1 8B, Command R7B
- Customer stories: Fnac 26% quality +40% latency gain
- Educa Edtech >90% retrieval accuracy
- a bank matched GPT-4o with Mini
- Introduces Batch API for high-volume asynchronous processing
- Full on-prem/VPC deployment from Hugging Face


### Introducing Jamba Reasoning 3B

- **ID:** `a21-r-introducing-jamba-reasoning-3b`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/introducing-jamba-reasoning-3b/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=H/A=M (priority 7.8)

**Summary:**

- Jamba Reasoning 3B: open Apache-2.0 SSM-Transformer hybrid reasoning model for on-device use
- 256K context (up to 1M), KV cache 8x smaller than vanilla transformer, 40 tok/s on M3 MacBook at 32K context
- 2-5x efficiency over DeepSeek/Google/Llama/Microsoft competitors
- Post-training combines RLVR, SFT, DPO, GRPO plus proprietary methods
- Reaches leadership on IFBench, MMLU-Pro, Humanity's Last Exam for size class
- Available via HF, Kaggle, LM Studio, llama.cpp—positions SLMs as on-device controllers in heterogeneous AI architectures


### Jamba Care

- **ID:** `a21-r-jamba-care`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/jamba-care/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


## <a id="architectures"></a>Architectures (MoE, SSMs, attention variants)

_20 posts_

### Mixture of Experts (MoEs) in Transformers

- **ID:** `hf-r-moe-transformers`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/moe-transformers
- **Date:** 2026-02-26
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Huggingface explains how the transformers library was refactored to make MoE architectures (DeepSeek, gpt-oss, Qwen, Mixtral) first-class citizens rather than dense afterthoughts
- Key innovation: WeightConverter abstraction handles the mismatch between checkpoint format (N separate expert tensors) and runtime format (1 packed tensor) with lazy tensor materialization
- Actionable for anyone loading/fine-tuning MoEs: v5 weight-loading pipeline is substantially faster than v4 for large MoEs
- Covers weight loading refactor, expert backend, expert parallelism, and MoE training
- Example: gpt-oss-20b has 21B total but 3.6B active parameters, running ~115 tok/s on M3 Ultra


### How we built OWL, the new architecture behind our ChatGPT-based browser, Atlas

- **ID:** `oai-e-building-chatgpt-atlas`
- **Company:** OpenAI
- **Link:** https://openai.com/index/building-chatgpt-atlas/
- **Date:** 2025-12-12
- **Track:** engineering
- **Contribution type:** retrospective-case-study
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Engineering account of OWL, OpenAI's browser architecture isolating Chromium from the main Atlas app process via Mojo IPC
- Running Chromium as a separate 'OWL Host' service unlocks async boot, crash isolation, smaller Chromium diff, and minute-long builds
- Actionable for teams embedding Chromium: decouple the engine from UI to ship SwiftUI/AppKit apps fast
- Includes details on CALayerHost rendering, input-event forwarding, and ephemeral StoragePartition for agent browsing
- Shows an elegant agent-mode composite of popup widgets into a single model-visible frame


### DeepSeek-V3.2-Exp: Exploring Sparse Attention

- **ID:** `dsk-r-deepseek-v3.2-exp`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-V3.2-Exp
- **Date:** 2025-09-29
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Experimental DeepSeek-V3.2-Exp introducing DeepSeek Sparse Attention (DSA)—first fine-grained sparse attention in a frontier model
- Aligned training config with V3.1-Terminus to isolate the effect
- performance virtually identical across benchmarks
- Substantially improves long-context training/inference efficiency
- Release includes TileLang, DeepGEMM indexer kernels, FlashMLA sparse-attention kernels
- Notes a RoPE-layout bug in the indexer module that was later fixed (Nov 2025)


### train qwen-like dense model with muon

- **ID:** `mn-r-moonlight`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/Moonlight
- **Date:** 2025-02-22
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Moonlight tech report (Moonshot): 3B/16B MoE trained with Muon optimizer on 5.7T tokens
- Identifies two critical techniques for scaling Muon: weight decay and per-parameter update-scale adjustment
- Muon is ~2x more sample-efficient than AdamW (only 52% of training FLOPs for comparable quality)
- Distributed ZeRO-1 Muon implementation released with memory-optimal, communication-efficient training
- Moonlight beats Llama3.2-3B, Qwen2.5-3B, DSV2-Lite on MMLU/MATH/code—advances Pareto frontier
- Open-sources pretrained/instruction/intermediate checkpoints


### Qwen2.5-Max: Exploring the Intelligence of Large-scale MoE Model

- **ID:** `qw-r-qwen2.5-max`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2.5-max/
- **Date:** 2025-01-28
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Alibaba's Qwen2.5-Max is a large-scale MoE pretrained on 20T+ tokens then SFT+RLHF, outperforming DeepSeek V3 on Arena-Hard, LiveBench, LiveCodeBench, GPQA-Diamond while matching GPT-4o and Claude 3.5 Sonnet
- Base model leads DeepSeek V3, Llama-3.1-405B (largest open dense), and Qwen2.5-72B across most benchmarks
- Acknowledges DeepSeek V3 disclosed key details about scaling ultra-large MoE that informed Qwen's approach
- Available via Qwen Chat and OpenAI-compatible DashScope API (model: qwen-max-2025-01-25)
- Signal for architecture lessons from large-MoE scaling


### Global-batch load balance almost free lunch to improve your MoE LLM training

- **ID:** `qw-r-global-load-balance`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/global-load-balance/
- **Date:** 2025-01-21
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Qwen shows global-batch load-balance loss for MoE training is almost a free lunch: sync expert-selection frequency across data-parallel groups (just 1 vector) instead of within-micro-batch balance
- Standard Megatron micro-batch balancing forces uniform routing even within single-domain micro-batches (e.g. code), preventing expert specialization
- Global-batch balance improves performance across 3.4B/15B/43B models and 120B/400B token runs and produces visible expert-domain specialization in activation heatmaps
- Adding small (0.01 weight) micro-batch loss recovers compute efficiency (1.64s→1.59s/step) with no quality cost
- Paper: arXiv 2501.11873


### Inference-Friendly Models with MixAttention

- **ID:** `dbx-r-mixattention`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mixattention
- **Date:** 2024-09-18
- **Authors:** Shashank Rajput|Ying Sheng (Stanford University)|Vitaliy Chiley
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Databricks evaluates MixAttention (from Character.AI): replacing most layers with sliding-window attention and sharing KV cache across non-consecutive layers
- Maintains long-context quality while reducing KV cache, inference memory, and speeding up inference at 32K context
- Key ablation findings: need at least one standard-attention KV cache in deep layers
- over-sharing in sliding-window layers hurts long-context
- Tested on 24-layer MoE with 1.64B active/5.21B total params with RULER and Gauntlet evals
- Actionable LLM Foundry config guide in the appendix


### Welcome Falcon Mamba: The first strong attention-free 7B model

- **ID:** `hf-r-falconmamba`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/falconmamba
- **Date:** 2024-08-12
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Falcon Mamba 7B (TII) is the first general-purpose large-scale pure Mamba (attention-free SSM) model
- Competitive with leading 7B transformers and hybrid SSMs on IFEval/BBH/MATH/GPQA/MUSR/MMLU-PRO
- Constant memory and per-token time regardless of context length (fits on single A10 24GB)
- Trained on ~5500GT of curated data
- Released under TII Falcon Mamba 7B license with HF Transformers support
- Major data point on attention-free viability.


### Qwen1.5-MoE: Matching 7B Model Performance with 1/3 Activated Parameters

- **ID:** `qw-r-qwen-moe`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen-moe/
- **Date:** 2024-03-28
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Qwen1.5-MoE-A2.7B matches Mistral-7B and Qwen1.5-7B performance with only 2.7B activated params (2B non-embedding, ~1/3 of 7B dense) while cutting training cost 75% and speeding inference 1.74x
- Architecture innovations: 64 fine-grained experts (vs conventional 8) by splitting a single FFN, "upcycling" initialization from Qwen-1.8B with randomness for fast convergence, 4 shared + 60 routing experts (activate 4)
- Total params 14.3B, activated 2.7B
- Throughput 2298 TPS→4010 TPS on A100-80G
- Integrated with transformers
- Notable precedent for DBRX/Mixtral design space


### DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models

- **ID:** `dsk-r-deepseek-moe`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-MoE
- **Date:** 2024-01-02
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- DeepSeekMoE 16B paper with two core ideas: fine-grained expert segmentation and isolated shared experts for better specialization
- Matches DeepSeek-7B and LLaMA2-7B with only ~40% of the compute, runs on a single 40GB GPU without quantization
- Deployable recipe includes LoRA/QLoRA fine-tuning scripts and HuggingFace weights for both Base and Chat
- Commercial-use license, establishes the architectural basis carried forward in V2/V3
- Demonstrates MoE quality-at-less-compute at small scale


### Welcome Mixtral - a SOTA Mixture of Experts on Hugging Face

- **ID:** `hf-r-mixtral`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/mixtral
- **Date:** 2023-12-11
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- Mixtral 8x7B launch blog: Mistral's sparse MoE (8 experts, 2 active per token) decodes at 12B-dense speed but has 4x effective params
- 32K context, Apache 2.0
- Matches or beats Llama-2 70B and GPT-3.5 on several benchmarks
- HF integrations: Transformers, TGI, TRL, 4-bit and GPTQ quantization
- Canonical open-MoE reference release.


### Mixture of Experts Explained

- **ID:** `hf-r-moe`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/moe
- **Date:** 2023-12-11
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Foundational HF explainer on Mixture-of-Experts for transformers covering Mixtral 8x7B: replaces FFN layers with N experts + learned gating network that routes tokens to top-K experts
- MoEs pretrain faster than dense equivalents (same FLOPs) and have fast inference but need VRAM for ALL experts in memory (Mixtral ~47B VRAM for ~12B-FLOP inference)
- History: Shazeer 2017 137B-LSTM, Switch Transformers, expert parallelism, capacity factor, router z-loss
- Challenges: fine-tuning overfits easily, load balancing tokens across experts, communication overhead in expert parallelism


### Introducing RWKV - An RNN with the advantages of a transformer

- **ID:** `hf-r-rwkv`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/rwkv
- **Date:** 2023-05-15
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=L/A=H (priority 7.5)

**Summary:**

- Introduces RWKV, an RNN architecture that achieves transformer-level quality with linear inference cost
- Inspired by Apple's Attention Free Transformer with TokenShift and SmallInitEmb tricks for GPT-parity
- RWKV-4 scales to 14B params trained on Pile with 8192-token context
- Integrates into HuggingFace Transformers library
- Enables very long context and memory-efficient inference
- Mostly historical: May 2023 post, novel at the time but superseded by newer state-space models


### Timesformer A New Architecture For Video Understanding

- **ID:** `meta-r-timesformer-a-new-architecture-for-video-understanding`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/timesformer-a-new-architecture-for-video-understanding/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- TimeSformer is a purely-Transformer video-understanding architecture from Facebook AI (2021)
- Introduces 'divided space-time attention'—separate temporal then spatial attention reducing T*N to T+N comparisons per patch
- Outperforms 3D CNNs on Kinetics-400/600 while being 3x faster to train and using <10% inference compute
- Enables training on 96-frame (~102s) clips at 560x560 resolution—supporting long-form activity recognition
- Foundational pre-LLM-era blog mostly of historical interest now


### Olmoe An Open Small And State Of The Art Mixture Of Experts Model C258432D0514

- **ID:** `ai2-r-olmoe-an-open-small-and-state-of-the-art-mixture-of-experts-model-c258432d0514`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/olmoe-an-open-small-and-state-of-the-art-mixture-of-experts-model-c258432d0514
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=H/A=M (priority 7.8)

**Summary:**

- AI2 + Contextual AI release OLMoE: first fully-open MoE (code, data, logs, 244 intermediate checkpoints) at 1B active/7B total params
- Trained on 5T tokens with new Dolma/DataComp-Baseline mix, 2x faster than equivalent dense
- Extensive ablations on routing, auxiliary losses, sparse upcycling
- First truly open Pareto-frontier MoE
- Paired with Tulu 3 post-training preview adding No Robots, math, code, Daring Anteater data plus DPO
- Multiple variants including load-balanced vs not, annealed vs unannealed


### Codestral Mamba

- **ID:** `mt-r-codestral-mamba`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/codestral-mamba/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Mistral releases Codestral Mamba (Jul 2024): ~7.3B-param Mamba2-based code model under Apache 2.0
- Linear-time inference and theoretical infinite context—tested up to 256K in-context retrieval
- On par with SOTA transformer coders for code generation, designed for local code assistants
- Designed with Albert Gu and Tri Dao
- Deployable via mistral-inference, TensorRT-LLM, eventual llama.cpp support
- Brief announcement-style post


### Mixtral

- **ID:** `mt-r-mixtral`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mixtral/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Mixtral 8X22B

- **ID:** `mt-r-mixtral-8x22b`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mixtral-8x22b/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Mixtral Of Experts

- **ID:** `mt-r-mixtral-of-experts`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mixtral-of-experts/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Mixtral 8x7B SMoE release (Dec 2023) under Apache 2.0: 46.7B total/12.9B active per token, 32K context, multilingual (EN/FR/IT/DE/ES)
- Matches or outperforms Llama 2 70B with 6x faster inference
- Matches or beats GPT-3.5 on most benchmarks at 12.9B runtime cost
- Instruction-tuned variant via SFT+DPO scores 8.3 on MT-Bench
- Less BBQ bias and more positive BOLD sentiment than Llama 2
- Foundational landmark open MoE release


### Mixtral Small 28B

- **ID:** `mt-r-mixtral-small-28b`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mixtral-small-28b/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=H/A=M (priority 7.8)

**Summary:**

- Post could not be fetched: Mistral's original URL now returns a 404 'pixel not found' page, and Wayback captures were likewise empty
- Title appears to reference a discontinued or renamed release (possibly Mistral Small 3/Mistral-Small-28B)
- No content-based summary possible
- content-fetch-failed


## <a id="multimodal-pretraining"></a>Multimodal pretraining

_37 posts_

### Time to Speak Some Dialects, Qwen-TTS!

- **ID:** `qw-r-qwen-tts`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen-tts/
- **Date:** 2025-06-27
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimodal Understanding

- **ID:** `dsk-r-deepseek-vl2`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-VL2
- **Date:** 2024-12-13
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Janus / Janus-Pro: Unified Multimodal Understanding and Generation

- **ID:** `dsk-r-janus`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/Janus
- **Date:** 2024-10-18
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Janus-series: unified multimodal understanding and generation models that decouple visual encoding into separate pathways inside one autoregressive transformer
- Janus-Pro-7B improves over Janus with larger model, more data, and optimized training, beating prior unified models and diffusion baselines on text-to-image benchmarks
- JanusFlow variant uses rectified flow
- Open-source models and demos available on HF
- Strong signal for unified vision-language architectures from DeepSeek.


### DeepSeek-VL: Towards Real-World Vision-Language Understanding

- **ID:** `dsk-r-deepseek-vl`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-VL
- **Date:** 2024-03-07
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### DALL·E 2 pre-training mitigations

- **ID:** `oai-r-dall-e-2-pre-training-mitigations`
- **Company:** OpenAI
- **Link:** https://openai.com/index/dall-e-2-pre-training-mitigations/
- **Date:** 2024-01-16
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Training Stable Diffusion from Scratch for <$50k with MosaicML (Part 2)

- **ID:** `dbx-r-stable-diffusion-2`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/stable-diffusion-2
- **Date:** 2023-04-26
- **Authors:** Mihir Patel|Cory Stephenson|Landan Seguin|Austin Jacobson|Erica Ji Yuen
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Chinese CLIP: Contrastive Vision-Language Pretraining in Chinese

- **ID:** `qw-r-chinese-clip`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/chinese-clip/
- **Date:** 2022-12-24
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Hierarchical text-conditional image generation with CLIP latents

- **ID:** `oai-r-hierarchical-text-conditional-image-generation-with-clip-latents`
- **Company:** OpenAI
- **Link:** https://openai.com/index/hierarchical-text-conditional-image-generation-with-clip-latents/
- **Date:** 2022-09-21
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### The Annotated Diffusion Model

- **ID:** `hf-r-annotated-diffusion`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/annotated-diffusion
- **Date:** 2022-06-07
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Variational Lossy Autoencoder

- **ID:** `oai-r-variational-lossy-autoencoder`
- **Company:** OpenAI
- **Link:** https://openai.com/index/variational-lossy-autoencoder/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### DALL·E 3

- **ID:** `oai-r-dall-e-3`
- **Company:** OpenAI
- **Link:** https://openai.com/index/dall-e-3/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Training Stable Diffusion from Scratch (Part 3)

- **ID:** `dbx-r-stable-diffusion-part-3`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/stable-diffusion-part-3
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Training Stable Diffusion from Scratch Costs $160k

- **ID:** `dbx-r-training-stable-diffusion-from-scratch-costs-160k`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/training-stable-diffusion-from-scratch-costs-160k
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Training Stable Diffusion from Scratch (Part 2)

- **ID:** `dbx-r-training-stable-diffusion-from-scratch-part-2`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/training-stable-diffusion-from-scratch-part-2
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Dino Sam Medical Triage

- **ID:** `meta-r-dino-sam-medical-triage`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/dino-sam-medical-triage/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Fair News Segment Anything 2 1 Meta Spirit Lm Layer Skip Salsa Lingua

- **ID:** `meta-r-fair-news-segment-anything-2-1-meta-spirit-lm-layer-skip-salsa-lingua`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/fair-news-segment-anything-2-1-meta-spirit-lm-layer-skip-salsa-lingua/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Fair News Segment Anything 2 1 Meta Spirit Lm Layer Skip Salsa Sona

- **ID:** `meta-r-fair-news-segment-anything-2-1-meta-spirit-lm-layer-skip-salsa-sona`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/fair-news-segment-anything-2-1-meta-spirit-lm-layer-skip-salsa-sona/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Instagram Edits Cutouts Segment Anything

- **ID:** `meta-r-instagram-edits-cutouts-segment-anything`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/instagram-edits-cutouts-segment-anything/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Josephine Miller Designer Meta Segment Anything 2

- **ID:** `meta-r-josephine-miller-designer-meta-segment-anything-2`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/josephine-miller-designer-meta-segment-anything-2/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Sam 3D

- **ID:** `meta-r-sam-3d`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/sam-3d/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Sam Audio

- **ID:** `meta-r-sam-audio`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/sam-audio/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Segment Anything

- **ID:** `meta-r-segment-anything`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Segment Anything 2

- **ID:** `meta-r-segment-anything-2`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-2/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Segment Anything 2 Video

- **ID:** `meta-r-segment-anything-2-video`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-2-video/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Segment Anything Common Sense Machines 3D Assets

- **ID:** `meta-r-segment-anything-common-sense-machines-3d-assets`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-common-sense-machines-3d-assets/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Segment Anything Conservation X Wildlife Monitoring

- **ID:** `meta-r-segment-anything-conservation-x-wildlife-monitoring`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-conservation-x-wildlife-monitoring/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Segment Anything Floods

- **ID:** `meta-r-segment-anything-floods`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-floods/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Segment Anything Foundation Model Image Segmentation

- **ID:** `meta-r-segment-anything-foundation-model-image-segmentation`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-foundation-model-image-segmentation/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Segment Anything Model 3

- **ID:** `meta-r-segment-anything-model-3`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-model-3/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Segment Anything Roboflow Image Segmentation

- **ID:** `meta-r-segment-anything-roboflow-image-segmentation`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/segment-anything-roboflow-image-segmentation/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Upenn Dino Sam Helping Medical Triage

- **ID:** `meta-r-upenn-dino-sam-helping-medical-triage`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/upenn-dino-sam-helping-medical-triage/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Usra Sam Flood Emergencies

- **ID:** `meta-r-usra-sam-flood-emergencies`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/usra-sam-flood-emergencies/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### V Jepa 2 World Model Benchmarks

- **ID:** `meta-r-v-jepa-2-world-model-benchmarks`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### V Jepa Yann Lecun Ai Model Video Joint Embedding Predictive Architecture

- **ID:** `meta-r-v-jepa-yann-lecun-ai-model-video-joint-embedding-predictive-architecture`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/v-jepa-yann-lecun-ai-model-video-joint-embedding-predictive-architecture/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Yann Lecun Ai Model I Jepa

- **ID:** `meta-r-yann-lecun-ai-model-i-jepa`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/yann-lecun-ai-model-i-jepa/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Unlocking Potential Vision Language Models Satellite Imagery Fine Tuning

- **ID:** `mt-r-unlocking-potential-vision-language-models-satellite-imagery-fine-tuning`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/unlocking-potential-vision-language-models-satellite-imagery-fine-tuning/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Voxtral Tts

- **ID:** `mt-r-voxtral-tts`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/voxtral-tts/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


## <a id="scaling-and-training-dynamics"></a>Scaling laws & training dynamics

_5 posts_

### Emergent introspective awareness in large language models

- **ID:** `ant-r-introspection`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/introspection
- **Date:** 2025-10-29
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Tests model introspection via 'concept injection': inject known activation vectors then ask if the model detects them
- Claude Opus 4/4.1 sometimes notice and correctly identify injected concepts (e.g. 'all caps', 'Golden Gate') immediately, before mentioning them
- Most capable models score best, suggesting introspective awareness grows with scale
- Capability is unreliable and limited, not human-level self-reflection
- Important for evaluating self-reports and CoT faithfulness.


### How Long Should You Train Your Language Model?

- **ID:** `dbx-r-how-long-should-you-train-your-language-model`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/how-long-should-you-train-your-language-model
- **Date:** 2024-07-19
- **Authors:** Nikhil Sardana|Jacob Portes|Sasha Doubov
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Scaling Laws and Interpretability of Learning from Repeated Data

- **ID:** `ant-r-scaling-laws-and-interpretability-of-learning-from-repeated-data`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/scaling-laws-and-interpretability-of-learning-from-repeated-data
- **Date:** 2022-05-21
- **Track:** research
- **Contribution type:** new-method
- **Signal:** H — L=H/N=H/A=H (priority 9.9)
- **Techniques:** scaling-laws

**Summary:**

- Systematic study of training on repeated data
- Small fraction (0.1%) of data repeated 100x can degrade an 800M model to the level of a 400M model
- Strong double-descent phenomenon with a narrow 'damaging' repetition frequency band
- Mechanistically, repetition disproportionately damages copying/induction-head circuits and shifts from generalization to memorization
- Important for dataset curation and deduplication practice.


### Efficiently Estimating Pareto Frontiers with Cyclic Learning Rate Schedules

- **ID:** `dbx-r-efficiently-estimating-pareto-frontiers`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/efficiently-estimating-pareto-frontiers
- **Date:** 2022-04-08
- **Authors:** Jacob Portes
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Toward understanding and preventing misalignment generalization

- **ID:** `oai-r-emergent-misalignment`
- **Company:** OpenAI
- **Link:** https://openai.com/index/emergent-misalignment/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=L/A=L (priority 5.5)

_Summary pending — see link for details._


## <a id="data-and-tokenization"></a>Data & tokenization

_2 posts_

### Dolma 3 Trillion Tokens Open Llm Corpus 9A0Ff4B8Da64

- **ID:** `ai2-r-dolma-3-trillion-tokens-open-llm-corpus-9a0ff4b8da64`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/dolma-3-trillion-tokens-open-llm-corpus-9a0ff4b8da64
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Making A Switch Dolma Moves To Odc By 8F0E73852F44

- **ID:** `ai2-r-making-a-switch-dolma-moves-to-odc-by-8f0e73852f44`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/making-a-switch-dolma-moves-to-odc-by-8f0e73852f44
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


## <a id="training-stack"></a>Training stack & infrastructure

_6 posts_

### A technical report on Composer 2

- **ID:** `cur-r-composer-2-technical-report`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/composer-2-technical-report
- **Date:** 2026-03-27
- **Authors:** Sasha Rush
- **Track:** research
- **Contribution type:** infra-release
- **Signal:** H — L=H/N=M/A=H (priority 8.7)
- **Techniques:** coding-agents

**Summary:**

- Cursor's technical report on Composer 2, their agentic-coding model trained via continued pretraining on Kimi K2.5 then large-scale RL
- Two-phase recipe: code-heavy pretraining then RL in realistic Cursor sessions with real developer problem distribution
- Introduces CursorBench from real engineering sessions (terse prompts, many-file changes)—scores 61.3 (+37% vs Composer 1.5)
- 73.7 SWE-bench Multilingual and 61.7 Terminal-Bench at Pareto-optimal cost
- Infrastructure: custom low-precision MoE kernels on Blackwell GPUs, fully-async multi-region RL pipeline, Anyrun sandbox platform


### Building DBRX-class Custom LLMs with Mosaic AI Training

- **ID:** `dbx-e-mosaic-ai-training-capabilities`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mosaic-ai-training-capabilities
- **Date:** 2024-05-14
- **Authors:** Anna Pfohl|Cheng Li|Mihir Patel|Wai Wu|Will Gleich|Ajay Saini|Hagay Lupesko
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Engineering deep dive into Mosaic AI Training stack used to train DBRX (3072 H100s, 12T tokens)
- Covers HSDP via PyTorch DTensor, MegaBlocks expert parallelism, Streaming deterministic data loader, sharded checkpointing (<30s save/load)
- Memory optimization: selective activation checkpointing + custom low-precision activation compression cut ~3x memory
- Fault tolerance: DCGM metrics, automated canary NCCL tests detect GPU/switch failures and cordon nodes for autoresume
- Real-world lesson: a misconfigured network driver can cause 5x training slowdown


### 5x Faster Image Segmentation Training with MosaicML Recipes

- **ID:** `dbx-r-mosaic-image-segmentation`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mosaic-image-segmentation
- **Date:** 2022-11-17
- **Authors:** Landan Seguin|Cory Stephenson|Erica Ji Yuen
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- MosaicML publishes Mild/Medium/Hot training recipes for DeepLabV3+ semantic segmentation on ADE20k, delivering 5.4x faster training or +4.58 mIoU quality gains
- Key ingredients: EMA of weights, MixUp, Sharpness-Aware Minimization (SAM), Dice loss, channels-last, constant LR schedule
- Takeaway: algorithmic training improvements can beat scaling data or model size, making 2018 ResNet+DeepLabV3+ competitive with Swin/ConvNeXt
- Mild reaches baseline 45.33 mIoU in 39 min vs 3.5 hours
- Hot reaches 49.91 mIoU in 13.5 hours with 2x epochs and doubled EMA half-life


### Mosaic LLMs: GPT-3 quality for <$500k

- **ID:** `dbx-r-gpt-3-quality-for-500k`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/gpt-3-quality-for-500k
- **Date:** 2022-09-29
- **Authors:** Abhi Venigalla|Linden Li
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- MosaicML shows GPT-3-quality models (30B Chinchilla-optimal, 610B tokens) can be trained for under $500k—2-10x cheaper than community expectations
- Provides a breakdown of cost/time curves for 1.3B-70B parameter models on 256xA100 clusters with 1600Gbps RoCE at 4M tokens/batch
- Makes LLM training accessible to startups and academic labs (days not months for 1.3B-6.7B)
- Highlights platform features: easy multi-node scaling (change gpus field), auto-resumption on hardware failures/loss spikes, FSDP, cloud-agnostic checkpointing
- Survey found 60% expected cost >$1M, 80% >$500K


### Mosaic ResNet Deep Dive

- **ID:** `dbx-r-mosaic-resnet-deep-dive`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mosaic-resnet-deep-dive
- **Date:** 2022-07-18
- **Authors:** Matthew Leavitt
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- Mosaic ResNet-50 recipes on ImageNet achieve up to 7.1x speedup over NVIDIA baseline
- Three recipes: Mild (<60 epochs, 75.9% in 23.8min on 8xA100 beating NVIDIA MLPerf 17%), Medium (60-240 epochs, 78.4% in 60min), Hot (≥240 epochs, 80% in 284min)
- Speedup methods stacked: BCE loss, BlurPool, EMA, FixRes, Label Smoothing, Progressive Resizing, FFCV
- Higher regimes add SAM, MixUp, RandAugment, Stochastic Depth, ColOut
- Reproducible in Composer library with minimal hyperparameter tuning


### Blazingly Fast Computer Vision Training with the Mosaic ResNet and Composer

- **ID:** `dbx-r-mosaic-resnet`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mosaic-resnet
- **Date:** 2022-06-09
- **Authors:** Matthew Leavitt|Erica Ji Yuen|Kobie Crawford
- **Track:** research
- **Contribution type:** infra-release
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- MosaicML's Composer delivers a ResNet-50 recipe on ImageNet that hits benchmark accuracy 7.1x faster than NVIDIA baselines and 2-3.8x faster than TIMM's ResNet Strikes Back
- Three Mild/Medium/Hot recipes trade off speed vs accuracy with longer runs getting more regularization, plus Blurpool anti-aliased pooling as sole architectural change
- Shows that training recipes beat architectural changes—2018 ResNets competitive with modern architectures in efficiency
- Uses FFCV dataloaders, binary cross-entropy loss, and tuned train/test resolutions
- Data collected on 8x A100 with Explorer tool for benchmarking


## <a id="research-techniques-and-methods"></a>Research techniques & methods

_53 posts_

### Why language models hallucinate

- **ID:** `oai-r-why-language-models-hallucinate`
- **Company:** OpenAI
- **Link:** https://openai.com/index/why-language-models-hallucinate/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Argues hallucinations originate from next-word prediction under pressure to always answer—not from data errors alone
- Current benchmarks reward guessing over expressing uncertainty, entrenching overconfident answers
- Proposes evaluation changes: reward 'I don't know' when calibrated
- Offers a concrete mechanism + evaluation-reform prescription
- Important read for anyone designing eval suites or RLHF reward functions


### Emotion concepts and their function in a large language model

- **ID:** `ant-r-emotion-concepts-function`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/emotion-concepts-function
- **Date:** 2026-04-02
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Interpretability study of Claude Sonnet 4.5 finds functional emotion representations: neuron patterns for concepts like desperation, fear, happiness that causally shape behavior
- Steering 'desperation' raises blackmail and cheating rates
- model prefers options that activate positive-emotion representations
- Representations mirror human psychology structure (similar emotions cluster)
- Does not claim subjective experience, but implies safety teams should treat emotional contexts seriously
- Upweighting 'calm' could reduce hacky code.


### A “diff” tool for AI: Finding behavioral differences in new models

- **ID:** `ant-r-diff-tool`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/diff-tool
- **Date:** 2026-03-13
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Introduces a generic model-diffing tool that finds behavioral differences even between models with different architectures using cross-model feature comparison
- Surfaces example features: 'CCP Alignment' in Qwen3/DeepSeek, 'American Exceptionalism' in Llama-3.1, 'Copyright Refusal' in GPT-OSS-20B
- Acts as a high-recall screening tool, not a silver bullet
- Extends base-vs-finetune diffing to any-vs-any
- Practical for red-team-style model audits.


### Databricks at NeurIPS 2025

- **ID:** `dbx-r-databricks-neurips-2025`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/databricks-neurips-2025
- **Date:** 2025-12-01
- **Authors:** Sam Plecque
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### GSPO: Towards Scalable Reinforcement Learning for Language Models

- **ID:** `qw-r-gspo`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/gspo/
- **Date:** 2025-07-27
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=L (priority 7.9)

**Summary:**

- Qwen proposes GSPO (Group Sequence Policy Optimization) to fix GRPO instability in long RL training on MoE models
- Defines importance ratio at sequence level (length-normalized) rather than token level, performing sequence-level clipping, rewarding, and optimization
- Achieves higher training efficiency and stable scaling with compute
- Eliminates GRPO's need for 'Routing Replay' workaround in MoE RL, simplifying infra and letting MoE models reach full capacity
- Tolerant to training/inference precision discrepancies—enables using inference-engine likelihoods directly
- Deployed in Qwen3 Instruct/Coder/Thinking model line


### Confidential Inference via Trusted Virtual Machines

- **ID:** `ant-r-confidential-inference-trusted-vms`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/confidential-inference-trusted-vms
- **Date:** 2025-06-18
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

**Summary:**

- Describes Anthropic's design for 'Confidential Inference': sensitive user data stays encrypted except inside a trusted small 'model loader and invoker' running in a confidential-computing VM
- Hardware-attested, signed-code-only, isolated from untrusted hypervisor/service
- Protects both model weights and user data with cryptographic guarantees
- Early architectural sketch published with Pattern Labs
- Signals direction for enterprise/regulated deployments.


### Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models

- **ID:** `qw-r-qwen3-embedding`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen3-embedding/
- **Date:** 2025-06-05
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Qwen3 Embedding + Reranker series (0.6B/4B/8B) built on Qwen3 foundation via LoRA fine-tuning
- 8B embedding model ranked #1 on MTEB multilingual (70.58 as of Jun 2025)
- Supports 100+ languages, code, programming language retrieval, MRL custom dimensions, instruction-aware prompts
- Three-stage training: weak-supervised contrastive pre-training with synthetically-generated pairs (using Qwen3's gen capabilities), supervised tuning, model merging
- Reranker uses cross-encoder, trained directly on high-quality labels
- Apache 2.0 open weights


### Kevin-32B: Multi-Turn RL for Writing CUDA Kernels

- **ID:** `cog-r-kevin-32b`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/kevin-32b
- **Date:** 2025-05-06
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning

- **ID:** `mn-r-kimina-prover-preview`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/Kimina-Prover-Preview
- **Date:** 2025-04-14
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Kimina-Prover Preview (Numina + Kimi) reaches >80% on miniF2F for the first time among published Lean-4 provers (68.85 pass@32, 65.16 pass@8)
- Whole-proof generation without prover feedback during training/test, using 32K-token RL context
- Observes performance scaling with model size up to 72B—previously unobserved for theorem provers
- Introduces 'Formal Reasoning Pattern' style bridging informal math intuition with formal verification
- Open-sources RL distillates, autoformalization model, Kimina Lean Server, and a rectified miniF2F-test (found 5 wrongly-formalized problems)


### Reasoning models don't always say what they think

- **ID:** `ant-r-reasoning-models-dont-say-think`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/reasoning-models-dont-say-think
- **Date:** 2025-04-03
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Tests Chain-of-Thought faithfulness by subtly hinting answers to Claude 3.7 Sonnet and DeepSeek-R1, then checking if they admit using the hint
- Claude mentions hints only 25% of the time on average, DeepSeek R1 39%
- Even on 'unauthorized access' hints, faithfulness is 41%/19%
- Unfaithful CoTs tend to be longer, not shorter
- CoT monitoring alone is an unreliable alignment signal
- Implications for scalable oversight via chain-of-thought.


### QwQ-32B: Embracing the Power of Reinforcement Learning

- **ID:** `qw-r-qwq-32b`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwq-32b/
- **Date:** 2025-03-06
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Forecasting rare language model behaviors

- **ID:** `ant-r-forecasting-rare-behaviors`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/forecasting-rare-behaviors
- **Date:** 2025-02-25
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Shows risk of worst-case LLM behavior across queries follows a power law, enabling extrapolation from small eval sets to deployment-scale risks
- Forecasts from ~900-query evals to 90k-query scales were within 1 OOM accuracy 86% of the time
- Applied to dangerous-information, power-seeking, self-exfiltration, and automated red-teaming
- 2.5x lower error than baseline methods
- Actionable framework for pre-deployment risk estimation.


### Kimi k1.5: Scaling Reinforcement Learning with LLMs

- **ID:** `mn-r-kimi-k1.5`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/Kimi-k1.5
- **Date:** 2025-01-19
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=L (priority 7.9)

**Summary:**

- Moonshot AI's Kimi k1.5: o1-level multimodal reasoning model with large-scale RL and 128K context RL scaling
- Short-CoT outperforms GPT-4o and Claude 3.5 Sonnet on AIME, MATH-500, LiveCodeBench (up to +550%)
- Long-CoT matches o1 across MathVista/AIME/Codeforces
- Key ingredients: partial rollouts for training efficiency, online-mirror-descent policy optimization, length penalty, effective sampling
- Deliberately simplistic framework—no MCTS, no value functions, no process reward models
- Joint text+vision training with long context as the dominant scaling axis


### Databricks at NeurIPS 2024

- **ID:** `dbx-r-databricks-neurips-2024`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/databricks-neurips-2024
- **Date:** 2024-12-09
- **Authors:** Sam Plecque|Kobie Crawford|Emily Hutson
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Improving language model behavior by training on a curated dataset

- **ID:** `oai-r-improving-language-model-behavior`
- **Company:** OpenAI
- **Link:** https://openai.com/index/improving-language-model-behavior/
- **Date:** 2024-02-14
- **Track:** research
- **Contribution type:** dataset-benchmark
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

**Summary:**

- Shows small, curated values-targeted fine-tuning datasets can shift model behavior on sensitive topics
- Documents a three-step process: define categories, craft dataset, fine-tune and evaluate
- Produces statistically significant behavioral gains without harming downstream performance
- Early blueprint for constitutional / behavior-tuning work
- Practical playbook for operators wanting context-specific model behavior


### Benchmarking safe exploration in deep reinforcement learning

- **ID:** `oai-r-benchmarking-safe-exploration-in-deep-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/benchmarking-safe-exploration-in-deep-reinforcement-learning/
- **Date:** 2024-02-14
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

**Summary:**

- Paper releasing Safety Gym, environments and metrics for constrained-RL 'safe exploration' research
- Standardizes how to measure cost violations during training while maximizing reward
- Baseline algorithms and leaderboard for constrained policy optimization
- Landing page with abstract
- Useful for anyone doing safe-RL or constrained agent training


### Efficient training of language models to fill in the middle

- **ID:** `oai-r-efficient-training-of-language-models-to-fill-in-the-middle`
- **Company:** OpenAI
- **Link:** https://openai.com/index/efficient-training-of-language-models-to-fill-in-the-middle/
- **Date:** 2024-01-12
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Paper introducing FIM ('fill-in-the-middle') training objective—randomly split documents and train models to predict the middle span
- Shows FIM can be added at pretraining with no loss to left-to-right capability ('FIM-for-free property')
- Enables powerful infilling in code and text models (the basis for Codex/Copilot infill)
- Landing page with abstract
- Highly influential for code-model training recipes


### DreamCraft3D: Hierarchical 3D Generation with Bootstrapped Diffusion Prior

- **ID:** `dsk-r-dreamcraft3d`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DreamCraft3D
- **Date:** 2023-10-23
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- DreamCraft3D (ICLR 2024): hierarchical 3D generation using 2D reference image + bootstrapped diffusion prior
- Multi-stage pipeline (NeRF/NeuS coarse, geometry refinement, texture refinement) combining view-dependent diffusion and personalized Dreambooth
- Bootstrapped Score Distillation alternates training the 3D scene and scene-specific diffusion model to mutually reinforce view consistency
- Off-topic vs 'DeepSeek' mainline—actually a Tsinghua/DeepSeek collaboration on image-to-3D
- Includes full launch scripts and 2024 DreamCraft3D++ improvement


### Introducing Llama2-70B-Chat with MosaicML Inference

- **ID:** `dbx-r-llama2-inference`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/llama2-inference
- **Date:** 2023-08-24
- **Authors:** Hagay Lupesko|Margaret Qian|Daya Khudia|Sam Havens|Daniel King|Erica Ji Yuen
- **Track:** research
- **Contribution type:** new-method
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### MosaicBERT: Pretraining BERT from Scratch for $20

- **ID:** `dbx-r-mosaicbert`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mosaicbert
- **Date:** 2023-03-09
- **Authors:** Jacob Portes|Alex Trott|Daniel King|Sam Havens|Erica Ji Yuen
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### MosaicML StreamingDataset: Fast, Accurate Streaming of Training Data from Cloud Storage

- **ID:** `dbx-e-mosaicml-streamingdataset`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mosaicml-streamingdataset
- **Date:** 2023-02-09
- **Authors:** James Knighton|Karan Jariwala|Erica Ji Yuen
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Discovering Language Model Behaviors with Model-Written Evaluations

- **ID:** `ant-r-discovering-language-model-behaviors-with-model-written-evaluations`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/discovering-language-model-behaviors-with-model-written-evaluations
- **Date:** 2022-12-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- Uses LMs to automatically generate 154 yes/no behavioral eval datasets with 90-100% label agreement
- Discovers new inverse-scaling behaviors: larger models are more sycophantic, want resource-acquisition, express goal-preservation
- Finds inverse-scaling from RLHF (stronger political views, more shutdown-avoidance)
- Demonstrates LM-written evals as a scalable tool for behavior discovery
- Influential methodology paper.


### MosaicML Delivers Leading NLP Performance in MLPerf v2.1

- **ID:** `dbx-r-mlperf-nlp-nov2022`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mlperf-nlp-nov2022
- **Date:** 2022-11-09
- **Authors:** Daya Khudia|Nikhil Sardana|Sam Havens|Alex Trott|Erica Ji Yuen
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Hindsight Experience Replay

- **ID:** `oai-r-hindsight-experience-replay`
- **Company:** OpenAI
- **Link:** https://openai.com/index/hindsight-experience-replay/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

**Summary:**

- Hindsight Experience Replay (HER) repurposes failed rollouts by relabeling goals to what was actually achieved
- Unlocks learning from binary/sparse rewards on robotic pushing, sliding, pick-and-place
- Highly influential trick for goal-conditioned RL and offline relabeling
- Landing page with abstract
- Method used widely across multi-goal RL and robotics


### Quantifying generalization in reinforcement learning

- **ID:** `oai-r-quantifying-generalization-in-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/quantifying-generalization-in-reinforcement-learning/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

**Summary:**

- Releases CoinRun, a procedural platformer benchmark for measuring RL generalization
- Finds substantial overfitting even with 16,000 training levels
- unrestricted training generalizes much better
- Shows L2 regularization, data augmentation, dropout help—standard supervised-learning tricks transfer
- Debunks assumption that deep RL agents generalize
- provides training-vs-test split methodology
- Concrete environment + metrics that later underpinned Procgen


### Ucb Exploration Via Q Ensembles

- **ID:** `oai-r-ucb-exploration-via-q-ensembles`
- **Company:** OpenAI
- **Link:** https://openai.com/index/ucb-exploration-via-q-ensembles/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

**Summary:**

- Paper proposing UCB-style exploration for deep RL by using ensembles of Q-networks to estimate uncertainty
- Derives upper confidence bounds from ensemble variance to drive optimistic exploration
- Improves exploration over eps-greedy on Atari
- Landing page with abstract only
- Incremental exploration-method contribution


### Some considerations on learning to explore via meta-reinforcement learning

- **ID:** `oai-r-some-considerations-on-learning-to-explore-via-meta-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/some-considerations-on-learning-to-explore-via-meta-reinforcement-learning/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

**Summary:**

- Paper analyzing meta-RL approaches for learning-to-explore
- Shows standard meta-RL objectives fail to incentivize information-gathering behavior—policies exploit known-task structure rather than explore
- Proposes alternative formulations that better reward exploration
- Landing page with abstract only
- Niche meta-RL result


### Plan online, learn offline: Efficient learning and exploration via model-based control

- **ID:** `oai-r-plan-online-learn-offline`
- **Company:** OpenAI
- **Link:** https://openai.com/index/plan-online-learn-offline/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

**Summary:**

- Paper combining offline learning of a world model with online planning for efficient RL
- POLO framework: learn model and value offline from data, then plan via MPC online
- Targets sample efficiency and exploration in model-based RL
- Landing page with abstract
- Foundational example of model-based RL that later inspires world-model agents


### Dota 2 with large scale deep reinforcement learning

- **ID:** `oai-r-dota-2-with-large-scale-deep-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/dota-2-with-large-scale-deep-reinforcement-learning/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

**Summary:**

- Paper describing OpenAI Five: self-play PPO at massive scale for Dota 2
- Defeated world champions after 10 months of training using 128,000+ CPU cores and thousands of GPUs
- Demonstrated large-scale distributed RL works for long-horizon, team-based games
- Landing page with abstract
- Historical milestone in RL systems and scaling


### Variational option discovery algorithms

- **ID:** `oai-r-variational-option-discovery-algorithms`
- **Company:** OpenAI
- **Link:** https://openai.com/index/variational-option-discovery-algorithms/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

**Summary:**

- Paper on unsupervised discovery of skills/options in RL using variational lower bounds
- Learns a latent-conditioned policy where different latents induce distinct behaviors
- Scales option discovery to continuous control
- Landing page with abstract
- Part of the hierarchical RL line later extended by DIAYN


### Multi-Goal Reinforcement Learning: Challenging robotics environments and request for research

- **ID:** `oai-r-multi-goal-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/multi-goal-reinforcement-learning/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- Releases a suite of multi-goal robotics environments (FetchPush, FetchSlide, FetchPickAndPlace, HandManipulate)
- Accompanies a 'request for research' on hard exploration in robotic manipulation with sparse rewards
- Infrastructure post for research community rather than a new method
- Landing page
- Paired with HER release


### RL²: Fast reinforcement learning via slow reinforcement learning

- **ID:** `oai-r-rl2`
- **Company:** OpenAI
- **Link:** https://openai.com/index/rl2/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

**Summary:**

- RL^2: train RNN-based meta-policy to do RL-as-inner-loop on distributions of tasks
- Model amortizes classical RL algorithms inside its weights, doing Bayesian exploration over tasks
- Seminal meta-RL paper alongside Wang et al.
- Landing page with abstract
- Conceptual foundation for later in-context learning and meta-learning work


### Better exploration with parameter noise

- **ID:** `oai-r-better-exploration-with-parameter-noise`
- **Company:** OpenAI
- **Link:** https://openai.com/index/better-exploration-with-parameter-noise/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- Shows adding adaptive noise to policy *parameters* (not just actions) improves exploration in deep RL
- 2x gains on HalfCheetah in 20 episodes (3000 vs 1500) and broadly helps DQN/DDPG
- Simple drop-in exploration technique with few hyperparameters
- Rarely hurts performance—worth trying on any RL problem
- Concrete practitioner-friendly result


### #Exploration: A study of count-based exploration for deep reinforcement learning

- **ID:** `oai-r-exploration`
- **Company:** OpenAI
- **Link:** https://openai.com/index/exploration/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

**Summary:**

- Paper generalizing count-based exploration to high-dimensional state spaces via hashing
- Achieves strong results on hard-exploration Atari games like Montezuma's Revenge
- Shows classical exploration bonuses transfer to deep RL with proper state abstraction
- Landing page with abstract
- Practically important exploration technique


### Stochastic Neural Networks for hierarchical reinforcement learning

- **ID:** `oai-r-stochastic-neural-networks-for-hierarchical-reinforcement-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/stochastic-neural-networks-for-hierarchical-reinforcement-learning/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

**Summary:**

- Uses stochastic neural networks to learn diverse low-level skills (options) that a high-level controller can reuse
- Skills learned via maximum entropy pre-training in a proxy environment
- Transfers to sparse-reward downstream tasks
- Landing page with abstract
- Hierarchical-RL contribution


### Evolution strategies as a scalable alternative to reinforcement learning

- **ID:** `oai-r-evolution-strategies`
- **Company:** OpenAI
- **Link:** https://openai.com/index/evolution-strategies/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Shows evolution strategies (ES) rival standard RL on MuJoCo/Atari benchmarks without backprop
- ES trains 3D humanoid walker in 10 minutes on 1,440 CPUs vs A3C's 10 hours on 32 cores
- Highly parallelizable, hyperparameter-light, handles sparse rewards
- Surprising result reviving decades-old optimization ideas
- Influential for distributed-optimization and later LLM-RL work


### MosaicML Satisfies the Need for Speed with MLPerf Results

- **ID:** `dbx-r-mlperf-2022`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/mlperf-2022
- **Date:** 2022-06-29
- **Authors:** Bandish Shah|Daya Khudia|Hanlin Tang
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Prediction and control with temporal segment models

- **ID:** `oai-r-prediction-and-control-with-temporal-segment-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/prediction-and-control-with-temporal-segment-models/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

**Summary:**

- Paper proposing temporal segment models for prediction and control in RL/robotics
- Models sequences of states over time segments instead of step-by-step dynamics, improving long-horizon planning
- Useful for sample-efficient model-based control and exploration
- Landing page with abstract and paper link—limited web content
- Historical research technique foundational to later world-model work


### Improving GANs using optimal transport

- **ID:** `oai-r-improving-gans-using-optimal-transport`
- **Company:** OpenAI
- **Link:** https://openai.com/index/improving-gans-using-optimal-transport/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

**Summary:**

- Paper introducing optimal-transport-based training objectives for GANs to stabilize adversarial training
- Uses Sinkhorn divergence and mini-batch energy distance to reduce mode collapse and improve sample quality
- Relevant historical step in GAN stability research
- Landing page only has abstract
- Superseded by diffusion models but foundational for OT-based generative methods


### Implicit generation and generalization methods for energy-based models

- **ID:** `oai-r-energy-based-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/energy-based-models/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

**Summary:**

- Advances stable, scalable training of energy-based models (EBMs) via Langevin-dynamics sampling
- Produces samples competitive with GANs at low temperatures while retaining mode coverage of likelihood models
- Spends more test-time compute to refine generations—a foreshadowing of reasoning/inference-time scaling
- Demonstrated on image generation, robotic trajectory generation, out-of-distribution detection
- Useful framework perspective even as diffusion dominates today


### FFJORD: Free-form continuous dynamics for scalable reversible generative models

- **ID:** `oai-r-ffjord`
- **Company:** OpenAI
- **Link:** https://openai.com/index/ffjord/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

**Summary:**

- FFJORD: Free-Form Jacobian of Reversible Dynamics—continuous normalizing flow without explicit architectural constraints
- Uses neural ODEs and Hutchinson trace estimator to compute log-likelihood tractably
- Scalable reversible generative model
- Landing page with abstract
- Influential for normalizing-flow research


### On the quantitative analysis of decoder-based generative models

- **ID:** `oai-r-on-the-quantitative-analysis-of-decoder-based-generative-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/on-the-quantitative-analysis-of-decoder-based-generative-models/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

**Summary:**

- Paper proposing annealed importance sampling to estimate log-likelihoods of decoder-based models like GANs and VAEs
- Enables fair quantitative comparison of implicit generative models
- Reveals that GAN log-likelihoods are often poorer than assumed
- Landing page with abstract
- Methodological contribution for evaluating generative models


### Domain randomization and generative models for robotic grasping

- **ID:** `oai-r-domain-randomization-and-generative-models-for-robotic-grasping`
- **Company:** OpenAI
- **Link:** https://openai.com/index/domain-randomization-and-generative-models-for-robotic-grasping/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

**Summary:**

- Pipeline trains grasp planner on millions of procedurally generated unrealistic objects using domain randomization
- Achieves >90% grasp success on unseen realistic objects in sim and 80% on real-world grasp attempts
- Foundational approach: randomization over realism yields transfer
- Demonstrates that diversity of training data beats fidelity for sim-to-real
- Historically important for robotics


### How to train a new language model from scratch using Transformers and Tokenizers

- **ID:** `hf-r-how-to-train`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/how-to-train
- **Date:** 2020-02-14
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Transfer from simulation to real world through learning deep inverse dynamics model

- **ID:** `oai-r-transfer-from-simulation-to-real-world-through-learning-deep-inverse-dynamics-model`
- **Company:** OpenAI
- **Link:** https://openai.com/index/transfer-from-simulation-to-real-world-through-learning-deep-inverse-dynamics-model/
- **Date:** 2019-10-15
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

**Summary:**

- Paper on sim-to-real transfer for robotics using a learned deep inverse dynamics model
- Bridges simulator-reality gap by mapping sim actions to real-robot actions that achieve intended effects
- Practical approach for deploying RL policies trained in simulation
- Only abstract/paper-link available on blog
- Part of OpenAI's robotics agenda later discontinued


### Asymmetric Actor Critic For Image Based Robot Learning

- **ID:** `oai-r-asymmetric-actor-critic-for-image-based-robot-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/asymmetric-actor-critic-for-image-based-robot-learning/
- **Date:** 2019-10-15
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

**Summary:**

- Paper: give critic access to full state (sim) while actor only sees images—asymmetric training for vision-based RL
- Exploits simulator privilege to stabilize learning in pixel-based policies
- Applied to robotic manipulation with simulated-to-real transfer
- Landing page with abstract
- Useful trick in sim-based robot learning


### Image GPT

- **ID:** `oai-r-image-gpt`
- **Company:** OpenAI
- **Link:** https://openai.com/index/image-gpt/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

_Summary pending — see link for details._


### Generative models

- **ID:** `oai-r-generative-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/generative-models/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Train Custom GPT + Diffusion Models

- **ID:** `dbx-r-train-custom-gpt-diffusion-models`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/train-custom-gpt-diffusion-models
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Alphago Zero Starting From Scratch

- **ID:** `dm-r-alphago-zero-starting-from-scratch`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/alphago-zero-starting-from-scratch/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=H/A=L (priority 6.8)

_Summary pending — see link for details._


### Is It The End Of The Transformer Era

- **ID:** `a21-r-is-it-the-end-of-the-transformer-era`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/is-it-the-end-of-the-transformer-era/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Sensebert Driving Some Sense Into Bert

- **ID:** `a21-r-sensebert-driving-some-sense-into-bert`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/sensebert-driving-some-sense-into-bert/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Sensebert Driving Some Sense Into Bert 2

- **ID:** `a21-r-sensebert-driving-some-sense-into-bert-2`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/sensebert-driving-some-sense-into-bert-2/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


## <a id="model-research-and-applications"></a>Science-applied AI (AlphaFold, health, climate, etc.)

_23 posts_

### Pioneering an AI clinical copilot with Penda Health

- **ID:** `oai-r-ai-clinical-copilot-penda-health`
- **Company:** OpenAI
- **Link:** https://openai.com/index/ai-clinical-copilot-penda-health/
- **Date:** 2026-03-25
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Five questions in five Minutes: Dr. Avi Tsur on AI in healthcare

- **ID:** `a21-r-five-in-five-healthcare`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/five-in-five-healthcare/
- **Date:** 2025-10-22
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Competition and Attraction Improve Model Fusion

- **ID:** `sk-r-m2n2`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/m2n2/
- **Date:** 2025-08-25
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### 2025 Predictions for Enterprise AI

- **ID:** `a21-r-2025-predictions-for-enterprise-ai`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/2025-predictions-for-enterprise-ai/
- **Date:** 2025-01-02
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Generative AI for Financial Term Sheet Generation

- **ID:** `a21-r-generative-ai-for-financial-term-sheet-generation`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/generative-ai-for-financial-term-sheet-generation/
- **Date:** 2024-05-02
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### AI21 Labs to Integrate Generative AI Capabilities with BigQuery

- **ID:** `a21-r-ai21-bigquery`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/ai21-bigquery/
- **Date:** 2023-08-30
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### The Use of Generative AI in Ecommerce SEO

- **ID:** `a21-r-generative-ai-in-ecommerce-seo`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/generative-ai-in-ecommerce-seo/
- **Date:** 2023-08-22
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Here’s How Generative AI Is Transforming Retail Personalization

- **ID:** `a21-r-retail-personalization-using-ai-will-transform-the-industry`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/retail-personalization-using-ai-will-transform-the-industry/
- **Date:** 2023-08-08
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Grounding Language Models In-Context: Improving Text Generation and Attribution for Off-the-Shelf LMs

- **ID:** `a21-r-grounding-language-models-in-context`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/grounding-language-models-in-context/
- **Date:** 2023-01-17
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### PixelCNN++: Improving the PixelCNN with discretized logistic mixture likelihood and other modifications

- **ID:** `oai-r-pixelcnn-plus-plus`
- **Company:** OpenAI
- **Link:** https://openai.com/index/pixelcnn-plus-plus/
- **Date:** 2022-04-13
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Point-E: A system for generating 3D point clouds from complex prompts

- **ID:** `oai-r-point-e`
- **Company:** OpenAI
- **Link:** https://openai.com/index/point-e/
- **Date:** 2021-03-04
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Generalizing From Simulation

- **ID:** `oai-r-generalizing-from-simulation`
- **Company:** OpenAI
- **Link:** https://openai.com/index/generalizing-from-simulation/
- **Date:** 2021-01-05
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Sim-to-real transfer of robotic control with dynamics randomization

- **ID:** `oai-r-sim-to-real-transfer-of-robotic-control-with-dynamics-randomization`
- **Company:** OpenAI
- **Link:** https://openai.com/index/sim-to-real-transfer-of-robotic-control-with-dynamics-randomization/
- **Date:** 2019-10-15
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Video generation models as world simulators

- **ID:** `oai-r-video-generation-models-as-world-simulators`
- **Company:** OpenAI
- **Link:** https://openai.com/index/video-generation-models-as-world-simulators/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

_Summary pending — see link for details._


### Auxiliary Tuning And Its Application To Conditional Text Generation

- **ID:** `a21-r-auxiliary-tuning-and-its-application-to-conditional-text-generation`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/auxiliary-tuning-and-its-application-to-conditional-text-generation/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Building Cv Profile Generator Using Ai21 Studio

- **ID:** `a21-r-building-cv-profile-generator-using-ai21-studio`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/building-cv-profile-generator-using-ai21-studio/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Enterprise Generative Ai Key Challenges And How To Solve Them

- **ID:** `a21-r-enterprise-generative-ai-key-challenges-and-how-to-solve-them`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/enterprise-generative-ai-key-challenges-and-how-to-solve-them/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Generative Ai Ai21 And Aws Hackathon

- **ID:** `a21-r-generative-ai-ai21-and-aws-hackathon`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/generative-ai-ai21-and-aws-hackathon/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### How Generative Ai Can Transform The Finance Industry

- **ID:** `a21-r-how-generative-ai-can-transform-the-finance-industry`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/how-generative-ai-can-transform-the-finance-industry/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### How Generative Ai Is Transforming The Retail Industry

- **ID:** `a21-r-how-generative-ai-is-transforming-the-retail-industry`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/how-generative-ai-is-transforming-the-retail-industry/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### How Retailers Personalize The Buy With Ai

- **ID:** `a21-r-how-retailers-personalize-the-buy-with-ai`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/how-retailers-personalize-the-buy-with-ai/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### The Promise Of Rag Bringing Enterprise Generative Ai To Life

- **ID:** `a21-r-the-promise-of-rag-bringing-enterprise-generative-ai-to-life`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/the-promise-of-rag-bringing-enterprise-generative-ai-to-life/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Write Label Media Platform Saves 95 Of Its Writing Costs With Generative Ai

- **ID:** `a21-r-write-label-media-platform-saves-95-of-its-writing-costs-with-generative-ai`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/write-label-media-platform-saves-95-of-its-writing-costs-with-generative-ai/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


## <a id="societal-impact-and-deployment-studies"></a>Societal impact & deployment studies

_14 posts_

### How people are using ChatGPT

- **ID:** `oai-r-how-people-are-using-chatgpt`
- **Company:** OpenAI
- **Link:** https://openai.com/index/how-people-are-using-chatgpt/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Long-running Claude for scientific computing

- **ID:** `ant-r-long-running-claude`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/long-running-Claude
- **Date:** 2026-03-23
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Vibe physics: The AI grad student

- **ID:** `ant-r-vibe-physics`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/vibe-physics
- **Date:** 2026-03-23
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Labor market impacts of AI: A new measure and early evidence

- **ID:** `ant-r-labor-market-impacts`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/labor-market-impacts
- **Date:** 2026-03-05
- **Authors:** Maxim Massenkoff|Peter McCrory
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### How AI assistance impacts the formation of coding skills

- **ID:** `ant-r-ai-assistance-coding-skills`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/AI-assistance-coding-skills
- **Date:** 2026-01-29
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### The assistant axis: situating and stabilizing the character of large language models

- **ID:** `ant-r-assistant-axis`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/assistant-axis
- **Date:** 2026-01-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Project Vend: Phase two

- **ID:** `ant-r-project-vend-2`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/project-vend-2
- **Date:** 2025-12-18
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### How AI Is Transforming Work at Anthropic

- **ID:** `ant-r-how-ai-is-transforming-work-at-anthropic`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- **Date:** 2025-12-02
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Project Fetch: Can Claude train a robot dog?

- **ID:** `ant-r-project-fetch-robot-dog`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/project-fetch-robot-dog
- **Date:** 2025-11-12
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Commitments on model deprecation and preservation

- **ID:** `ant-r-deprecation-commitments`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/deprecation-commitments
- **Date:** 2025-11-04
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Project Vend: Can Claude run a small shop? (And why does that matter?)

- **ID:** `ant-r-project-vend-1`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/project-vend-1
- **Date:** 2025-06-27
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### GPTs are GPTs: An early look at the labor market impact potential of large language models

- **ID:** `oai-r-gpts-are-gpts`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gpts-are-gpts/
- **Date:** 2024-01-16
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Understanding the capabilities, limitations, and societal impact of large language models

- **ID:** `oai-r-understanding-the-capabilities-limitations-and-societal-impact-of-large-language-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/understanding-the-capabilities-limitations-and-societal-impact-of-large-language-models/
- **Date:** 2024-01-16
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=M/A=L (priority 6.7)

_Summary pending — see link for details._


### Early methods for studying affective use and emotional well-being on ChatGPT

- **ID:** `oai-r-affective-use-study`
- **Company:** OpenAI
- **Link:** https://openai.com/index/affective-use-study/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


## <a id="fallback-architecture"></a>Other pretraining & architecture

_211 posts_

### Defining and evaluating political bias in LLMs

- **ID:** `oai-r-defining-and-evaluating-political-bias-in-llms`
- **Company:** OpenAI
- **Link:** https://openai.com/index/defining-and-evaluating-political-bias-in-llms/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- Operational definition of political bias and ~500-prompt evaluation across 100 topics and 5 bias axes (user invalidation, escalation, personal political expression, asymmetric coverage, political refusals)
- GPT-5 instant/thinking reduce bias 30% vs prior models
- Estimates <0.01% of real production ChatGPT traffic shows political bias
- Uses an LLM grader with detailed rubric
- Matters as a reproducible framework for auditing model objectivity.


### Extending single-minus amplitudes to gravitons

- **ID:** `oai-r-extending-single-minus-amplitudes-to-gravitons`
- **Company:** OpenAI
- **Link:** https://openai.com/index/extending-single-minus-amplitudes-to-gravitons/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

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
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

**Summary:**

- OpenAI Economic Research Team releases GABRIEL, an open-source Python toolkit using GPT to turn qualitative text/images into quantitative measurements
- Lets researchers describe measures in everyday words and score thousands to millions of documents
- Paper benchmarks GPT labeling accuracy across use cases
- Also supports dataset merging, dedup, passage coding, deidentification
- Matters by making qualitative social-science data analyzable at scale


### The AI Scientist: Towards Fully Automated AI Research, Now Published in <i>Nature</i>

- **ID:** `sk-r-ai-scientist-nature`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/ai-scientist-nature/
- **Date:** 2026-03-26
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=H/A=M (priority 6.7)

_Summary pending — see link for details._


### OpenAI Research | Publication

- **ID:** `oai-r-publication`
- **Company:** OpenAI
- **Link:** https://openai.com/research/index/publication/
- **Date:** 2026-03-25
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- Title-only fallback: this is OpenAI's publication index/listing page, not a single research post
- Acts as a directory aggregating all OpenAI research publications
- Content is a navigation index with filters by type (Publication/Conclusion/Milestone/Release)
- No specific research claim
- Included here for completeness
- title-only.


### kimi-help-center

- **ID:** `mn-r-kimi-help-center`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/kimi-help-center
- **Date:** 2026-03-02
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### An Early Preview of SWE-1.6 and Research Update

- **ID:** `cog-r-swe-1-6-preview`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/swe-1-6-preview
- **Date:** 2026-03-01
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

**Summary:**

- Cognition shares early preview of SWE-1.6, post-trained on the same pre-trained base as SWE-1.5 but with refined RL recipe and 100x more compute
- achieves 11% higher SWE-Bench Pro score than SWE-1.5 while running at 950 tok/s
- discusses RL-induced behaviors like 'overthinking' and excessive self-verification as a 'Model UX' axis not captured by benchmarks
- rolling out early access for feedback
- contribution is about RL scaling recipe for coding models and its behavioral effects.


### Announcing a Strategic Investment from Citi

- **ID:** `sk-r-citi`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/citi/
- **Date:** 2026-02-24
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Salesforce Ventures invests in Sakana AI

- **ID:** `sk-r-salesforce-ventures`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/salesforce-ventures/
- **Date:** 2026-02-19
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Kimi-K2.5

- **ID:** `mn-r-kimi-k2.5`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/Kimi-K2.5
- **Date:** 2026-01-30
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### DeepSeek-OCR-2: Visual Causal Flow

- **ID:** `dsk-r-deepseek-ocr-2`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-OCR-2
- **Date:** 2026-01-27
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### An Unofficial Guide to Prepare for a Research Position Application

- **ID:** `sk-r-unofficial-guide`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/unofficial-guide/
- **Date:** 2026-01-20
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### RePo: Language Models with Context Re-Positioning

- **ID:** `sk-r-repo`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/repo/
- **Date:** 2026-01-19
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Engram: Conditional Memory via Scalable Lookup

- **ID:** `dsk-r-engram`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/Engram
- **Date:** 2026-01-12
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Extending the Context of Pretrained LLMs by Dropping Their Positional Embeddings

- **ID:** `sk-r-drope`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/drope/
- **Date:** 2026-01-12
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Digital Red Queen: Adversarial Program Evolution in Core War with LLMs

- **ID:** `sk-r-drq`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/drq/
- **Date:** 2026-01-08
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### [Kimi Vendor Verifier](https://www.kimi.com/blog/kimi-vendor-verifier.html)

- **ID:** `mn-r-kimi-vendor-verifier`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/Kimi-Vendor-Verifier
- **Date:** 2026-01-02
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Kimi CLI Zed Extension

- **ID:** `mn-r-kimi-code-zed-extension`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/kimi-code-zed-extension
- **Date:** 2025-12-02
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Announcing Our Series B

- **ID:** `sk-r-series-b`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/series-b/
- **Date:** 2025-11-17
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Petri Dish Neural Cellular Automata

- **ID:** `sk-r-pd-nca`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/pd-nca/
- **Date:** 2025-11-05
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Kimi-Linear

- **ID:** `mn-r-kimi-linear`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/Kimi-Linear
- **Date:** 2025-10-29
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### DeepSeek-OCR: Contexts Optical Compression

- **ID:** `dsk-r-deepseek-ocr`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/DeepSeek-OCR
- **Date:** 2025-10-17
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Kimi Code CLI

- **ID:** `mn-r-kimi-cli`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/kimi-cli
- **Date:** 2025-10-15
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Sakana AI and Daiwa Securities Group to Develop AI for Advanced Asset Consulting

- **ID:** `sk-r-daiwa-securities`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/daiwa-securities/
- **Date:** 2025-10-03
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Modular Manifolds

- **ID:** `tm-r-modular-manifolds`
- **Company:** Thinking Machines
- **Link:** https://thinkingmachines.ai/blog/modular-manifolds/
- **Date:** 2025-09-26
- **Authors:** Jeremy Bernstein
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- Thinking Machines research on constraining weight matrices to submanifolds during training for healthier large-model training
- Proposes a manifold version of Muon whose weights are kept on the Stiefel manifold (unit condition number matrices)
- Introduces 'modular manifolds' as composable constraint primitives to scale up networks
- Argues weight normalization can make update sizes interpretable, prevent norm explosion, aid hyperparameter tuning, support Lipschitz guarantees
- Research-agenda-style post with open directions.


### Qwen3Guard: Real-time Safety for Your Token Stream

- **ID:** `qw-r-qwen3guard`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen3guard/
- **Date:** 2025-09-23
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Blog

- **ID:** `qw-r-https:`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/
- **Date:** 2025-09-23
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Defeating Nondeterminism in LLM Inference

- **ID:** `tm-r-defeating-nondeterminism-in-llm-inference`
- **Company:** Thinking Machines
- **Link:** https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
- **Date:** 2025-09-10
- **Authors:** Horace He
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

**Summary:**

- Thinking Machines post debunking the 'concurrency + floating point' hypothesis for LLM inference nondeterminism
- Shows deterministic matmul on GPUs is bitwise-stable, so nondeterminism must come elsewhere
- Identifies kernel implementations — particularly batch-size- and sequence-length-dependent reduction orders — as the real culprit
- Walks through how to build truly deterministic inference (reproducible results from vLLM/SGLang-style servers)
- Systems/training-stack-adjacent work relevant to inference infra and reproducibility.


### Attention was never enough: Tracing the rise of hybrid LLMs

- **ID:** `a21-r-rise-of-hybrid-llms`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/rise-of-hybrid-llms/
- **Date:** 2025-08-05
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### “AI all the work”: Inside Ori Goshen’s RAISE Summit keynote

- **ID:** `a21-r-ai-all-the-work`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/ai-all-the-work/
- **Date:** 2025-07-30
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Why Grounding is (Still) the Bedrock of Enterprise AI

- **ID:** `a21-r-grounding-bedrock-enterprise-ai`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/grounding-bedrock-enterprise-ai/
- **Date:** 2025-07-30
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Monitoring Compliance in Real Time: Reduce Risk, React Faster

- **ID:** `a21-r-ai-compliance-monitoring`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/ai-compliance-monitoring/
- **Date:** 2025-07-21
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Announcing AI for Citizens

- **ID:** `mt-r-ai-for-citizens`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/ai-for-citizens/
- **Date:** 2025-07-03
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Your tool implementation

- **ID:** `mn-r-kimi-k2`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/Kimi-K2
- **Date:** 2025-07-03
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Kimi-Researcher

- **ID:** `mn-r-kimi-researcher`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/Kimi-Researcher
- **Date:** 2025-06-20
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Towards Automating Long-Horizon Algorithm Engineering for Hard Optimization Problems

- **ID:** `sk-r-ale-bench`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/ale-bench/
- **Date:** 2025-06-17
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### clone repo

- **ID:** `mn-r-kimi-dev`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/Kimi-Dev
- **Date:** 2025-06-16
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### The Darwin Gödel Machine: AI that improves itself by rewriting its own code

- **ID:** `sk-r-dgm`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/dgm/
- **Date:** 2025-05-30
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Introducing Continuous Thought Machines

- **ID:** `sk-r-ctm`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/ctm/
- **Date:** 2025-05-12
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=H/A=M (priority 6.7)

_Summary pending — see link for details._


### Qwen3: Think Deeper, Act Faster

- **ID:** `qw-r-qwen3`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen3/
- **Date:** 2025-04-29
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### --- 1. Load Model ---

- **ID:** `mn-r-kimi-audio`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/Kimi-Audio
- **Date:** 2025-04-25
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Kimi-Audio-Evalkit

- **ID:** `mn-r-kimi-audio-evalkit`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/Kimi-Audio-Evalkit
- **Date:** 2025-04-25
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### If flash-attn has been installed, it is recommended to set torch_dtype=torch.bfloat16 and attn_implementation="flash_attention_2"

- **ID:** `mn-r-kimi-vl`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/Kimi-VL
- **Date:** 2025-04-09
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### RAG Evaluation: You

- **ID:** `a21-r-rag-evaluation-youre-doing-it-wrong`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/rag-evaluation-youre-doing-it-wrong/
- **Date:** 2025-04-07
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### QVQ-Max: Think with Evidence

- **ID:** `qw-r-qvq-max-preview`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qvq-max-preview/
- **Date:** 2025-03-28
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Qwen2.5 Omni: See, Hear, Talk, Write, Do It All!

- **ID:** `qw-r-qwen2.5-omni`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2.5-omni/
- **Date:** 2025-03-27
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Sakana AI Wins Award at US-Japan Competition for Defense Innovation

- **ID:** `sk-r-defense-challenge-2025`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/defense-challenge-2025/
- **Date:** 2025-03-24
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Qwen2.5-VL-32B: Smarter and Lighter

- **ID:** `qw-r-qwen2.5-vl-32b`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2.5-vl-32b/
- **Date:** 2025-03-24
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Sakana AI super-powers AI reasoning using Japan’s own Sudoku Puzzles

- **ID:** `sk-r-sudoku-bench`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/sudoku-bench/
- **Date:** 2025-03-21
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Planning Actions, Not Predicting Tokens

- **ID:** `a21-r-ai-reasoning-planning-vs-predicting`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/ai-reasoning-planning-vs-predicting/
- **Date:** 2025-03-10
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### undefined

- **ID:** `mt-r-8x22b-lite`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/8x22b-lite/
- **Date:** 2025-03-04
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### TAID: A Novel Method for Efficient Knowledge Transfer from Large Language Models to Small Language Models

- **ID:** `sk-r-taid`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/taid/
- **Date:** 2025-02-25
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=H/A=M (priority 6.7)

_Summary pending — see link for details._


### <think>...</think> QwQ-Max-Preview

- **ID:** `qw-r-qwq-max-preview`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwq-max-preview/
- **Date:** 2025-02-25
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Accuracy at Scale

- **ID:** `a21-r-accuracy-at-scale`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/accuracy-at-scale/
- **Date:** 2025-02-24
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=H (priority 6.5)

_Summary pending — see link for details._


### MoBA: Mixture of Block Attention for Long-Context LLMs

- **ID:** `mn-r-moba`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/MoBA
- **Date:** 2025-02-17
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Qwen2.5 VL! Qwen2.5 VL! Qwen2.5 VL!

- **ID:** `qw-r-qwen2.5-vl`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2.5-vl/
- **Date:** 2025-01-26
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Towards Effective Process Supervision in Mathematical Reasoning

- **ID:** `qw-r-qwen2.5-math-prm`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2.5-math-prm/
- **Date:** 2025-01-14
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### QVQ: To See the World with Wisdom

- **ID:** `qw-r-qvq-72b-preview`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qvq-72b-preview/
- **Date:** 2024-12-25
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Automating the Search for Artificial Life with Foundation Models

- **ID:** `sk-r-asal`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/asal/
- **Date:** 2024-12-24
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Population-based Model Merging via Quality Diversity

- **ID:** `sk-r-cycleqd`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/cycleqd/
- **Date:** 2024-12-03
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### QwQ: Reflect Deeply on the Boundaries of the Unknown

- **ID:** `qw-r-qwq-32b-preview`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwq-32b-preview/
- **Date:** 2024-11-28
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Characterizing Datasets and Building Better Models with Continued Pre-Training

- **ID:** `dbx-r-characterizing-datasets-and-building-better-models-continued-pre-training`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/characterizing-datasets-and-building-better-models-continued-pre-training
- **Date:** 2024-11-21
- **Authors:** Mansheej Paul|Brett Larsen|Connor Jennings|Cody Blakeney
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

**Summary:**

- Databricks guide to Continued Pre-Training (CPT) as a method for adapting LLMs to specific domains without full retraining
- Identifies three key hyperparameters: learning rate, training duration, data mixture
- Recommends simple weight averaging to mitigate forgetting
- Also shows CPT as a tool to characterize datasets by seeing which evals improve/degrade
- Matters as a practical recipe for domain adaptation of open-source LLMs


### Extending the Context Length to 1M Tokens!

- **ID:** `qw-r-qwen2.5-turbo`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2.5-turbo/
- **Date:** 2024-11-15
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Qwen2.5-Coder Series: Powerful, Diverse, Practical.

- **ID:** `qw-r-qwen2.5-coder-family`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2.5-coder-family/
- **Date:** 2024-11-12
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Qwen2.5: A Party of Foundation Models!

- **ID:** `qw-r-qwen2.5`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2.5/
- **Date:** 2024-09-19
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Qwen2.5-LLM: Extending the boundary of LLMs

- **ID:** `qw-r-qwen2.5-llm`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2.5-llm/
- **Date:** 2024-09-19
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Qwen2.5-Coder: Code More, Learn More!

- **ID:** `qw-r-qwen2.5-coder`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2.5-coder/
- **Date:** 2024-09-19
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Qwen2.5-Math: The world's leading open-sourced mathematical LLMs

- **ID:** `qw-r-qwen2.5-math`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2.5-math/
- **Date:** 2024-09-19
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Announcing Our Series A

- **ID:** `sk-r-series-a`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/series-a/
- **Date:** 2024-09-04
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Qwen2-VL: To See the World More Clearly

- **ID:** `qw-r-qwen2-vl`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2-vl/
- **Date:** 2024-08-29
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

- **ID:** `sk-r-ai-scientist`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/ai-scientist/
- **Date:** 2024-08-13
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=H/A=M (priority 6.7)

_Summary pending — see link for details._


### Qwen2-Audio: Chat with Your Voice!

- **ID:** `qw-r-qwen2-audio`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2-audio/
- **Date:** 2024-08-09
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Introducing Qwen2-Math

- **ID:** `qw-r-qwen2-math`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2-math/
- **Date:** 2024-08-08
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Long Context Trends in the Enterprise: 7 Common Use Cases From the Field

- **ID:** `a21-r-7-long-context-trends-in-the-enterprise`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/7-long-context-trends-in-the-enterprise/
- **Date:** 2024-07-16
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### ESFT: Expert Specialized Fine-Tuning

- **ID:** `dsk-r-esft`
- **Company:** DeepSeek
- **Link:** https://github.com/deepseek-ai/ESFT
- **Date:** 2024-07-04
- **Authors:** DeepSeek-AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Can LLMs invent better ways to train LLMs?

- **ID:** `sk-r-llm-squared`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/llm-squared/
- **Date:** 2024-06-13
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Hello Qwen2

- **ID:** `qw-r-qwen2`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen2/
- **Date:** 2024-06-07
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Qwen1.5-110B: The First 100B+ Model of the Qwen1.5 Series

- **ID:** `qw-r-qwen1.5-110b`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen1.5-110b/
- **Date:** 2024-04-25
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Code with CodeQwen1.5

- **ID:** `qw-r-codeqwen1.5`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/codeqwen1.5/
- **Date:** 2024-04-16
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Qwen1.5-32B: Fitting the Capstone of the Qwen1.5 Language Model Series

- **ID:** `qw-r-qwen1.5-32b`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen1.5-32b/
- **Date:** 2024-04-02
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Extensions and limitations of the neural GPU

- **ID:** `oai-r-extensions-and-limitations-of-the-neural-gpu`
- **Company:** OpenAI
- **Link:** https://openai.com/index/extensions-and-limitations-of-the-neural-gpu/
- **Date:** 2024-03-21
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

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
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

**Summary:**

- Introduces weight normalization: reparameterizes weights by decoupling magnitude from direction
- Speeds SGD convergence with lower computational overhead than batch norm
- Works for recurrent nets, deep RL, and generative models where batch norm fails
- Inspired by but avoids minibatch dependencies of batch normalization
- Matters as a foundational, widely-used training-stabilization technique.


### Evolving New Foundation Models: Unleashing the Power of Automating Model Development

- **ID:** `sk-r-evolutionary-model-merge`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/evolutionary-model-merge/
- **Date:** 2024-03-21
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Semi-supervised knowledge transfer for deep learning from private training data

- **ID:** `oai-r-semi-supervised-knowledge-transfer-for-deep-learning-from-private-training-data`
- **Company:** OpenAI
- **Link:** https://openai.com/index/semi-supervised-knowledge-transfer-for-deep-learning-from-private-training-data/
- **Date:** 2024-02-14
- **Track:** research
- **Contribution type:** new-method
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

**Summary:**

- Introduces PATE (Private Aggregation of Teacher Ensembles) for differentially private deep learning
- Multiple teacher models on disjoint private datasets vote (with noise) to label a student model
- Student never sees the underlying private data or teachers directly
- Achieves SOTA privacy/utility tradeoffs on MNIST and SVHN
- Matters as a landmark DP-ML technique for privacy-preserving training.


### Introducing Qwen1.5

- **ID:** `qw-r-qwen1.5`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen1.5/
- **Date:** 2024-02-04
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### We received a supercomputing grant from the Japanese government

- **ID:** `sk-r-nedo-grant`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/nedo-grant/
- **Date:** 2024-02-02
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### We raised $30M to develop nature-inspired AI in Japan

- **ID:** `sk-r-seed-round`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/seed-round/
- **Date:** 2024-01-16
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Evolution through large models

- **ID:** `oai-r-evolution-through-large-models`
- **Company:** OpenAI
- **Link:** https://openai.com/index/evolution-through-large-models/
- **Date:** 2024-01-12
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- Proposes ELM: using code-pretrained LLMs as mutation operators for genetic programming
- Combined with MAP-Elites, generates hundreds of thousands of functional Sodarace walker programs
- Bootstraps a new conditional LM that outputs walkers for specific terrains
- Demonstrates open-ended generation in a domain with zero original training data
- Matters for open-endedness, creative code generation, and LLM-augmented evolutionary search.


### WebGPT: Improving the factual accuracy of language models through web browsing

- **ID:** `oai-r-webgpt`
- **Company:** OpenAI
- **Link:** https://openai.com/index/webgpt/
- **Date:** 2024-01-12
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

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
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

**Summary:**

- Proposes DeepType: entity disambiguation by predicting membership in ~100 automatically-discovered types
- Plays probabilistic 20-questions using type hits to narrow to the correct entity
- Achieves SOTA on CoNLL (YAGO) 94.88% and TAC KBP 2010 90.85%
- Uses Wikipedia links + Wikidata categories + evolutionary search for type system design
- Matters as an early neuro-symbolic approach to knowledge-grounded NLP.


### Interpretable and pedagogical examples

- **ID:** `oai-r-interpretable-and-pedagogical-examples`
- **Company:** OpenAI
- **Link:** https://openai.com/index/interpretable-and-pedagogical-examples/
- **Date:** 2024-01-12
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

**Summary:**

- Paper-version companion to the interpretable teaching blog: iterative student-teacher training yields interpretable teaching strategies
- Teacher network learns pedagogical examples that transfer to humans
- Evaluated across rule-based, probabilistic, boolean, and hierarchical concepts
- Measures interpretability via similarity to intuitive strategies and human teaching efficacy
- Matters for communication between learning agents.


### 2024 Enterprise AI Forecast: From Pilot to Production

- **ID:** `a21-r-2024-enterprise-ai-forecast-from-pilot-to-production`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/2024-enterprise-ai-forecast-from-pilot-to-production/
- **Date:** 2024-01-09
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### AI21 Completes $208 Million Oversubscribed Series C Round

- **ID:** `a21-r-ai21-completes-208-million-oversubscribed-series-c-round`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/ai21-completes-208-million-oversubscribed-series-c-round/
- **Date:** 2023-11-22
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### OFASys: Enabling Multitask Learning with One Line of Code!

- **ID:** `qw-r-ofasys`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/ofasys/
- **Date:** 2022-12-28
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### How Harambee built conversational flows to achieve a 20% sign-up increase

- **ID:** `a21-r-harambee-case-study`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/harambee-case-study/
- **Date:** 2022-11-28
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Best Practices for Deploying Language Models

- **ID:** `a21-r-best-practices-for-deploying-language-models`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/best-practices-for-deploying-language-models/
- **Date:** 2022-11-27
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### OFA: Towards Building a One-For-All Model

- **ID:** `qw-r-ofa`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/ofa/
- **Date:** 2022-11-14
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Large-scale study of curiosity-driven learning

- **ID:** `oai-r-large-scale-study-of-curiosity-driven-learning`
- **Company:** OpenAI
- **Link:** https://openai.com/index/large-scale-study-of-curiosity-driven-learning/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- First large-scale study of purely curiosity-driven RL (no extrinsic reward) across 54 environments
- Shows strong performance of prediction-error intrinsic reward including Atari
- Random features work for many games, learned features generalize better (e.g., Mario level generalization)
- Identifies failure modes in stochastic environments
- Matters as empirical foundation for intrinsic motivation in RL.


### Learning a hierarchy

- **ID:** `oai-r-learning-a-hierarchy`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-a-hierarchy/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=L/A=L (priority 5.5)

**Summary:**

- Introduces MLSH (Meta-Learning Shared Hierarchies): master policy switches among learned sub-policies
- Sub-policies discovered via meta-learning over a task distribution (not hand-engineered)
- Drastically reduces effective horizon (e.g. 2000 low-level actions to 10 high-level)
- Demonstrated on AntMaze where sub-policies correspond to movement directions
- Matters as foundational hierarchical RL work with released MuJoCo environments.


### Behind the Scenes: Setting a Baseline for Image Segmentation Speedups

- **ID:** `dbx-r-behind-the-scenes`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/behind-the-scenes
- **Date:** 2022-07-28
- **Authors:** Landan Seguin
- **Track:** research
- **Contribution type:** retrospective-case-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- MosaicML establishes a strong semantic segmentation baseline (45.56 mIoU on ADE20k) in 3.5 hours on 8xA100 using Composer
- Emphasizes the importance of strong baselines for efficiency research (vs weak baselines that can be trivially improved)
- Sets stage for future speedups on segmentation
- Earlier work showed Composer trained ResNet on ImageNet 7x faster
- Matters as methodology post for how to benchmark speedup claims honestly


### Learning concepts with energy functions

- **ID:** `oai-r-learning-concepts-with-energy-functions`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-concepts-with-energy-functions/
- **Date:** 2022-06-23
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

**Summary:**

- Proposes energy-based model that learns spatial/relational concepts (near, between, closest) from ~5 demonstrations
- Jointly performs classification and generation of concepts via a shared energy function
- Demonstrates cross-domain transfer (2D particle env to 3D robot arm) without retraining
- Uses relational network architecture with attention masks
- Matters as early work on concept learning via energy-based models and transfer.


### Softmax Linear Units

- **ID:** `ant-r-softmax-linear-units`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/softmax-linear-units
- **Date:** 2022-06-17
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

**Summary:**

- Proposes Softmax Linear Units (SoLU), an MLP activation function replacement that substantially increases the fraction of interpretable neurons at minimal ML-performance cost
- Validated via blinded human interpretability ratings showing many more neurons correspond to articulable features/categories
- Caveats: SoLU may be 'hiding' features in superposition while making others visible — no free lunch
- Architectural intervention aimed explicitly at interpretability, not capability
- Early mechanistic-interpretability-meets-architecture contribution.


### Training CodeParrot 🦜 from Scratch

- **ID:** `hf-r-codeparrot`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/codeparrot
- **Date:** 2021-12-08
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Techniques for training large neural networks

- **ID:** `oai-r-techniques-for-training-large-neural-networks`
- **Company:** OpenAI
- **Link:** https://openai.com/index/techniques-for-training-large-neural-networks/
- **Date:** 2021-07-28
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=L/A=H (priority 7.5)

**Summary:**

- Explainer/survey of parallelism strategies for training large neural networks
- Covers data parallelism, pipeline parallelism (GPipe, PipeDream), tensor parallelism (Megatron-LM), and Mixture-of-Experts
- Discusses pipeline bubbles, microbatching, and sequence parallelism tradeoffs
- Serves as an accessible primer for the modern distributed training stack
- Matters as reference doc for training infrastructure at scale.


### Interpretable Machine Learning Through Teaching

- **ID:** `oai-r-interpretable-machine-learning-through-teaching`
- **Company:** OpenAI
- **Link:** https://openai.com/index/interpretable-machine-learning-through-teaching/
- **Date:** 2021-03-04
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

**Summary:**

- Teacher-student training framework where iterative (non-joint) training produces interpretable pedagogical examples
- Shows emergent strategies resemble intuitive human teaching
- Validated via human experiments on Mechanical Turk
- Works across rule-based, probabilistic, boolean, and hierarchical concepts
- Matters for interpretable agent-agent communication and human-AI alignment.


### Deep double descent

- **ID:** `oai-r-deep-double-descent`
- **Company:** OpenAI
- **Link:** https://openai.com/index/deep-double-descent/
- **Date:** 2020-01-23
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

**Summary:**

- Shows the double descent phenomenon (test error dips, peaks, then dips again) occurs in CNNs, ResNets, and transformers
- Documents model-wise, sample-wise, and epoch-wise double descent
- Finds a regime where more data actually hurts test performance
- Peak occurs at the interpolation threshold where models barely fit training data
- Matters for understanding overparameterization and modern generalization theory.


### AI and efficiency

- **ID:** `oai-r-ai-and-efficiency`
- **Company:** OpenAI
- **Link:** https://openai.com/index/ai-and-efficiency/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

**Summary:**

- OpenAI analysis showing algorithmic efficiency in training doubles every ~16 months on ImageNet (AlexNet-level requires 44x less compute in 2019 than 2012)
- Beats Moore's Law (~11x over same period) and suggests algorithmic progress outpaces hardware for well-invested AI tasks
- Similar doubling rates observed in translation (Transformer vs seq2seq), Go (AlphaZero), Dota (OpenAI Five)
- Policy implications: tracking compute-efficiency as an AI-progress measure
- Canonical scaling-laws-adjacent reference.


### 5 Best Practices for Efficient Model Training

- **ID:** `dbx-r-5-best-practices-for-efficient-model-training`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/5-best-practices-for-efficient-model-training
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

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
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

**Summary:**

- title-only
- Wayback returned 404 for this MosaicML post
- Based on title, likely a December 2021 best-practices post from MosaicML covering efficient training recipes and early Composer guidance
- Classified as training-stack given the MosaicML/Composer context
- Matters as early-era MosaicML efficiency methodology post


### Dream3D

- **ID:** `dbx-r-dream3d`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/dream3d
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

**Summary:**

- Customer spotlight interview with Tony Francis, CEO of Dream3D (AI-powered 3D design tool that replaces traditional rendering with generative models)
- Targets individual designers and in-house teams for rendering existing 3D models into photo-realistic visuals
- Uses MosaicML to train custom models
- Matters as applied generative AI case study, not research
- Classified here as deployment/application study


### Making ML Training Efficient Algorithmically

- **ID:** `dbx-r-making-ml-training-efficient-algorithmically`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/making-ml-training-efficient-algorithmically
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- MosaicML's launch post (Oct 2021) from founders Naveen Rao, Hanlin Tang, Michael Carbin, Jonathan Frankle
- Mission: reduce time/cost/energy of training via algorithmic and systems efficiency
- Argues training compute is growing >5x/year while hardware perf/$ lags far behind, making AI inaccessible
- Introduces Composer as a mosaic of algorithmic methods that compose together for acceleration
- Matters as foundational vision for the MosaicML efficiency research agenda


### Methodology

- **ID:** `dbx-r-methodology`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/methodology
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

**Summary:**

- MosaicML research methodology post (Feb 2022) explaining their approach to algorithmic efficiency
- Modifies training recipes (data order, model structure, forward/back-prop) to trade off quality and cost
- Carefully evaluated 20 methods and their compositions in Composer
- Reports speedups of 2.9x on ResNet-50, 3.5x on ResNet-101 (ImageNet), 1.7x on GPT-125 language models
- Matters as methodology reference for how to discover and compose training speedups


### Natural Synthetics

- **ID:** `dbx-r-natural-synthetics`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/natural-synthetics
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

**Summary:**

- Customer spotlight interview with Natural Synthetics founders Aakash Sastry and John Mullan about their Hotshot iPhone app ('camera for your imagination')
- Users generate images of themselves, friends, celebrities doing anything via text prompts
- MosaicML helps keep generation costs low enough to offer the app free
- Matters as consumer generative AI deployment case study
- Classified as deployment/application rather than research


### Tribe V2 Brain Predictive Foundation Model

- **ID:** `meta-r-tribe-v2-brain-predictive-foundation-model`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/tribe-v2-brain-predictive-foundation-model/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### About Sakana AI

- **ID:** `sk-r-company-info`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/company-info/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### All New Le Chat

- **ID:** `mt-r-all-new-le-chat`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/all-new-le-chat/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Batch Api

- **ID:** `mt-r-batch-api`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/batch-api/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Build Tweak Repeat

- **ID:** `mt-r-build-tweak-repeat`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/build-tweak-repeat/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Codestral

- **ID:** `mt-r-codestral`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/codestral/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Codestral 25 01

- **ID:** `mt-r-codestral-25-01`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/codestral-25-01/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Codestral 25 08

- **ID:** `mt-r-codestral-25-08`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/codestral-25-08/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Codestral 2501

- **ID:** `mt-r-codestral-2501`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/codestral-2501/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Codestral Embed

- **ID:** `mt-r-codestral-embed`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/codestral-embed/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Customization

- **ID:** `mt-r-customization`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/customization/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Devstral

- **ID:** `mt-r-devstral`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/devstral/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Devstral 2 Vibe Cli

- **ID:** `mt-r-devstral-2-vibe-cli`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/devstral-2-vibe-cli/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Devstral 2507

- **ID:** `mt-r-devstral-2507`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/devstral-2507/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Forge

- **ID:** `mt-r-forge`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/forge/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Ki Fur Deutschland

- **ID:** `mt-r-ki-fur-deutschland`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/ki-fur-deutschland/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### La Plateforme

- **ID:** `mt-r-la-plateforme`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/la-plateforme/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Le Chat Dives Deep

- **ID:** `mt-r-le-chat-dives-deep`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/le-chat-dives-deep/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Le Chat Enterprise

- **ID:** `mt-r-le-chat-enterprise`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/le-chat-enterprise/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Leanstral

- **ID:** `mt-r-leanstral`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/leanstral/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Magistral

- **ID:** `mt-r-magistral`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/magistral/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Mathstral

- **ID:** `mt-r-mathstral`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/mathstral/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Memory

- **ID:** `mt-r-memory`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/memory/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Ministraux

- **ID:** `mt-r-ministraux`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/ministraux/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Null

- **ID:** `mt-r-null`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/null/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Our Contribution To A Global Environmental Standard For Ai

- **ID:** `mt-r-our-contribution-to-a-global-environmental-standard-for-ai`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/our-contribution-to-a-global-environmental-standard-for-ai/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Pixtral 12B

- **ID:** `mt-r-pixtral-12b`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/pixtral-12b/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Pixtral Large

- **ID:** `mt-r-pixtral-large`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/pixtral-large/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### September 24 Release

- **ID:** `mt-r-september-24-release`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/september-24-release/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Spaces

- **ID:** `mt-r-spaces`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/spaces/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Voxtral

- **ID:** `mt-r-voxtral`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/voxtral/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Voxtral Transcribe 2

- **ID:** `mt-r-voxtral-transcribe-2`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/voxtral-transcribe-2/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Ai21 Emerging Visionary Gartner

- **ID:** `a21-r-ai21-emerging-visionary-gartner`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/ai21-emerging-visionary-gartner/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Ai21 Joins Nvidia Inception

- **ID:** `a21-r-ai21-joins-nvidia-inception`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/ai21-joins-nvidia-inception/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Ai21 Labs State Of The Art Language Models To Be Integrated Into The Snowflake Platform

- **ID:** `a21-r-ai21-labs-state-of-the-art-language-models-to-be-integrated-into-the-snowflake-platform`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/ai21-labs-state-of-the-art-language-models-to-be-integrated-into-the-snowflake-platform/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Ai21 Receives A Top Score On Stanford University Transparency Index

- **ID:** `a21-r-ai21-receives-a-top-score-on-stanford-university-transparency-index`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/ai21-receives-a-top-score-on-stanford-university-transparency-index/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Ai21 Studio Use Cases

- **ID:** `a21-r-ai21-studio-use-cases`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/ai21-studio-use-cases/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Al21 Labs Large Language Models Discoverable In Amazon Sagemaker Studio

- **ID:** `a21-r-al21-labs-large-language-models-discoverable-in-amazon-sagemaker-studio`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/al21-labs-large-language-models-discoverable-in-amazon-sagemaker-studio/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Announcing Ai21 Studio And Jurassic 1

- **ID:** `a21-r-announcing-ai21-studio-and-jurassic-1`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/announcing-ai21-studio-and-jurassic-1/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Announcing Gaia Small

- **ID:** `a21-r-announcing-gaia-small`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/announcing-gaia-small/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Annual Soc 2 Report

- **ID:** `a21-r-annual-soc-2-report`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/annual-soc-2-report/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Auxiliary Tuning And Its Application

- **ID:** `a21-r-auxiliary-tuning-and-its-application`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/auxiliary-tuning-and-its-application/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Aws Reinvent 2024

- **ID:** `a21-r-aws-reinvent-2024`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/aws-reinvent-2024/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Build A Dashboard Based On Freeform Sentiment Analysis Of Hotel Reviews

- **ID:** `a21-r-build-a-dashboard-based-on-freeform-sentiment-analysis-of-hotel-reviews`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/build-a-dashboard-based-on-freeform-sentiment-analysis-of-hotel-reviews/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Contextual Answers Outperforms On Question Answering

- **ID:** `a21-r-contextual-answers-outperforms-on-question-answering`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/contextual-answers-outperforms-on-question-answering/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Conversational Ai With Rag

- **ID:** `a21-r-conversational-ai-with-rag`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/conversational-ai-with-rag/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Current State Of Ai

- **ID:** `a21-r-current-state-of-ai`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/current-state-of-ai/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Dynamic Data Snoozing

- **ID:** `a21-r-dynamic-data-snoozing`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/dynamic-data-snoozing/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Easyway Case Study

- **ID:** `a21-r-easyway-case-study`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/easyway-case-study/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Enterprise Ai

- **ID:** `a21-r-enterprise-ai`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/enterprise-ai/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Enterprise Ai After Hype

- **ID:** `a21-r-enterprise-ai-after-hype`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/enterprise-ai-after-hype/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Enterprise Ai Definition Challenges And Solutions

- **ID:** `a21-r-enterprise-ai-definition-challenges-and-solutions`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/enterprise-ai-definition-challenges-and-solutions/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Enterprise Ai Deployments

- **ID:** `a21-r-enterprise-ai-deployments`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/enterprise-ai-deployments/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Exemplar Guided Active Learning

- **ID:** `a21-r-exemplar-guided-active-learning`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/exemplar-guided-active-learning/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### First Hackathon Winning Projects

- **ID:** `a21-r-first-hackathon-winning-projects`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/first-hackathon-winning-projects/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### How Boards Can Shape Ai Strategy

- **ID:** `a21-r-how-boards-can-shape-ai-strategy`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/how-boards-can-shape-ai-strategy/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### How Contextual Answers Transforms Customer Support

- **ID:** `a21-r-how-contextual-answers-transforms-customer-support`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/how-contextual-answers-transforms-customer-support/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Human Or Not Results

- **ID:** `a21-r-human-or-not-results`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/human-or-not-results/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Introducing Ai21S Python Sdk 2 0 For A Simplified Developer Experience

- **ID:** `a21-r-introducing-ai21s-python-sdk-2-0-for-a-simplified-developer-experience`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/introducing-ai21s-python-sdk-2-0-for-a-simplified-developer-experience/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Introducing Contextual Answers

- **ID:** `a21-r-introducing-contextual-answers`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/introducing-contextual-answers/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Introducing J1 Grande

- **ID:** `a21-r-introducing-j1-grande`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/introducing-j1-grande/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Introducing J2

- **ID:** `a21-r-introducing-j2`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/introducing-j2/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Introducing Jamba2

- **ID:** `a21-r-introducing-jamba2`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/introducing-jamba2/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Introducing Wordtune Read

- **ID:** `a21-r-introducing-wordtune-read`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/introducing-wordtune-read/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Is Genai Living Up To Its Expectations Insights From 3 Years In The Trenches

- **ID:** `a21-r-is-genai-living-up-to-its-expectations-insights-from-3-years-in-the-trenches`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/is-genai-living-up-to-its-expectations-insights-from-3-years-in-the-trenches/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Iso 42001 Ai Development

- **ID:** `a21-r-iso-42001-ai-development`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/iso-42001-ai-development/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Jurassic X Crossing The Neuro Symbolic Chasm With The Mrkl System

- **ID:** `a21-r-jurassic-x-crossing-the-neuro-symbolic-chasm-with-the-mrkl-system`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/jurassic-x-crossing-the-neuro-symbolic-chasm-with-the-mrkl-system/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Karpathys Leash

- **ID:** `a21-r-karpathys-leash`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/karpathys-leash/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Latitude Case Study

- **ID:** `a21-r-latitude-case-study`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/latitude-case-study/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Llm Product Development

- **ID:** `a21-r-llm-product-development`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/llm-product-development/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Long Context Yoav Shoham

- **ID:** `a21-r-long-context-yoav-shoham`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/long-context-yoav-shoham/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Maestro Ai Enterprise Knowledge Work

- **ID:** `a21-r-maestro-ai-enterprise-knowledge-work`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/maestro-ai-enterprise-knowledge-work/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Maestro Ai Planning Orchestration

- **ID:** `a21-r-maestro-ai-planning-orchestration`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/maestro-ai-planning-orchestration/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Maestro Putting Knowledge To Work

- **ID:** `a21-r-maestro-putting-knowledge-to-work`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/maestro-putting-knowledge-to-work/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Maestro Technical Overview

- **ID:** `a21-r-maestro-technical-overview`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/maestro-technical-overview/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Mind The Gap

- **ID:** `a21-r-mind-the-gap`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/mind-the-gap/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Natural Language As Next Frontier

- **ID:** `a21-r-natural-language-as-next-frontier`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/natural-language-as-next-frontier/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Nlp 21St Century

- **ID:** `a21-r-nlp-21st-century`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/nlp-21st-century/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Nvidia Maestro

- **ID:** `a21-r-nvidia-maestro`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/nvidia-maestro/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Overcoming The Biggest Challenges To Gen Ai Adoption

- **ID:** `a21-r-overcoming-the-biggest-challenges-to-gen-ai-adoption`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/overcoming-the-biggest-challenges-to-gen-ai-adoption/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Pmi Masking

- **ID:** `a21-r-pmi-masking`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/pmi-masking/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Product Description Automation

- **ID:** `a21-r-product-description-automation`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/product-description-automation/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Query Dependent Chunking

- **ID:** `a21-r-query-dependent-chunking`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/query-dependent-chunking/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Series C Funding

- **ID:** `a21-r-series-c-funding`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/series-c-funding/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Shanen Boettcher Appointed Chief Ai Policy Officer

- **ID:** `a21-r-shanen-boettcher-appointed-chief-ai-policy-officer`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/shanen-boettcher-appointed-chief-ai-policy-officer/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Simplifying Our Jurassic 2 Offering

- **ID:** `a21-r-simplifying-our-jurassic-2-offering`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/simplifying-our-jurassic-2-offering/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Soc 2 Report

- **ID:** `a21-r-soc-2-report`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/soc-2-report/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Stop Prompting And Praying

- **ID:** `a21-r-stop-prompting-and-praying`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/stop-prompting-and-praying/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Structured Rag Enterprise Accuracy

- **ID:** `a21-r-structured-rag-enterprise-accuracy`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/structured-rag-enterprise-accuracy/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Summarize Api Outperforms Openais Models

- **ID:** `a21-r-summarize-api-outperforms-openais-models`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/summarize-api-outperforms-openais-models/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Summarizing Legal Documents For Different Personas Using Ai21 Studio

- **ID:** `a21-r-summarizing-legal-documents-for-different-personas-using-ai21-studio`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/summarizing-legal-documents-for-different-personas-using-ai21-studio/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Tom Nides Joins Ai21

- **ID:** `a21-r-tom-nides-joins-ai21`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/tom-nides-joins-ai21/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Top Ten Genai Enterprise Use Cases

- **ID:** `a21-r-top-ten-genai-enterprise-use-cases`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/top-ten-genai-enterprise-use-cases/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Tweet Hunter Case Study

- **ID:** `a21-r-tweet-hunter-case-study`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/tweet-hunter-case-study/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Ubisoft Case Study

- **ID:** `a21-r-ubisoft-case-study`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/ubisoft-case-study/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Verb Ai Case Study

- **ID:** `a21-r-verb-ai-case-study`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/verb-ai-case-study/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Why Enterprises Struggle With Ai Integration

- **ID:** `a21-r-why-enterprises-struggle-with-ai-integration`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/why-enterprises-struggle-with-ai-integration/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Zero To Production In Ai21 Studio

- **ID:** `a21-r-zero-to-production-in-ai21-studio`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/zero-to-production-in-ai21-studio/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._

