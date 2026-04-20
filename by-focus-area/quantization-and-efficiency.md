# Quantization & Efficiency

FP8/INT8 training, post-training quantization, distillation for size, parameter-efficient methods (LoRA/PEFT).

**Post count:** 24

**Contributors:**

- Hugging Face: 14
- Databricks Mosaic AI: 3
- Meta AI / FAIR: 2
- Sakana AI: 2
- Thinking Machines: 1
- OpenAI: 1
- Google Research: 1

**Subcategories:**

- [Post-training quantization](#post-training-quantization) (3)
- [Parameter-efficient training (LoRA/PEFT)](#parameter-efficient-training) (16)
- [Pruning & sparsity](#pruning-and-sparsity) (2)
- [Other efficiency](#fallback-efficiency) (3)

---

## <a id="post-training-quantization"></a>Post-training quantization

_3 posts_

### Making LLMs lighter with AutoGPTQ and transformers

- **ID:** `hf-r-gptq-integration`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/gptq-integration
- **Date:** 2023-08-23
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Making LLMs even more accessible with bitsandbytes, 4-bit quantization and QLoRA

- **ID:** `hf-r-4bit-transformers-bitsandbytes`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/4bit-transformers-bitsandbytes
- **Date:** 2023-05-24
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### A Gentle Introduction to 8-bit Matrix Multiplication for transformers at scale using transformers, accelerate and bitsandbytes

- **ID:** `hf-r-hf-bitsandbytes-integration`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/hf-bitsandbytes-integration
- **Date:** 2022-08-17
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="parameter-efficient-training"></a>Parameter-efficient training (LoRA/PEFT)

_16 posts_

### Instant LLM Updates with Doc-to-LoRA and Text-to-LoRA

- **ID:** `sk-r-doc-to-lora`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/doc-to-lora/
- **Date:** 2026-02-27
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Fast PEFT Serving at Scale

- **ID:** `dbx-e-fast-peft-serving-scale`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/fast-peft-serving-scale
- **Date:** 2025-10-21
- **Track:** engineering
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### LoRA Without Regret

- **ID:** `tm-r-lora`
- **Company:** Thinking Machines
- **Link:** https://thinkingmachines.ai/blog/lora/
- **Date:** 2025-09-29
- **Authors:** John Schulman
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** fine-tuning

_Summary pending — see link for details._


### Fast LoRA inference for Flux with Diffusers and PEFT

- **ID:** `hf-r-lora-fast`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/lora-fast
- **Date:** 2025-07-23
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### (LoRA) Fine-Tuning FLUX.1-dev on Consumer Hardware

- **ID:** `hf-r-flux-qlora`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/flux-qlora
- **Date:** 2025-06-19
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Text-to-LoRA: Instant Transformer Adaption

- **ID:** `sk-r-text-to-lora`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/text-to-lora/
- **Date:** 2025-06-12
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Fine-Tuning Gemma Models in Hugging Face

- **ID:** `hf-r-gemma-peft`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/gemma-peft
- **Date:** 2024-02-23
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### 🤗 PEFT welcomes new merging methods

- **ID:** `hf-r-peft_merging`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/peft_merging
- **Date:** 2024-02-19
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### LoRA training scripts of the world, unite!

- **ID:** `hf-r-sdxl_lora_advanced_script`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/sdxl_lora_advanced_script
- **Date:** 2024-01-02
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Goodbye cold boot - how we made LoRA Inference 300% faster

- **ID:** `hf-r-lora-adapters-dynamic-loading`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/lora-adapters-dynamic-loading
- **Date:** 2023-12-05
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Comparing the Performance of LLMs: A Deep Dive into Roberta, Llama 2, and Mistral for Disaster Tweets Analysis with Lora

- **ID:** `hf-r-Lora-for-sequence-classification-with-Roberta-Llama-Mistral`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/Lora-for-sequence-classification-with-Roberta-Llama-Mistral
- **Date:** 2023-11-07
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Fine-Tune MMS Adapter Models for low-resource ASR

- **ID:** `hf-r-mms_adapters`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/mms_adapters
- **Date:** 2023-06-19
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Fine-tuning 20B LLMs with RLHF on a 24GB consumer GPU

- **ID:** `hf-r-trl-peft`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/trl-peft
- **Date:** 2023-03-09
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Parameter-Efficient Fine-Tuning using 🤗 PEFT

- **ID:** `hf-r-peft`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/peft
- **Date:** 2023-02-10
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Using LoRA for Efficient Stable Diffusion Fine-Tuning

- **ID:** `hf-r-lora`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/lora
- **Date:** 2023-01-26
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### How To Fine Tune Llms Peft Dataset Curation

- **ID:** `meta-r-how-to-fine-tune-llms-peft-dataset-curation`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/how-to-fine-tune-llms-peft-dataset-curation/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="pruning-and-sparsity"></a>Pruning & sparsity

_2 posts_

### Sparsity-preserving differentially private training

- **ID:** `gr-r-sparsity-preserving-differentially-private-training`
- **Company:** Google Research
- **Link:** https://research.google/blog/sparsity-preserving-differentially-private-training/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Training With Quantization Noise For Extreme Model Compression

- **ID:** `meta-r-training-with-quantization-noise-for-extreme-model-compression`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/training-with-quantization-noise-for-extreme-model-compression/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="fallback-efficiency"></a>Other efficiency

_3 posts_

### Scaling Small LLMs with NVIDIA MPS

- **ID:** `dbx-r-scaling-small-llms-nvidia-mps`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/scaling-small-llms-nvidia-mps
- **Date:** 2026-01-26
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Databricks tests NVIDIA Multi-Process Service (MPS) for serving small LLMs more efficiently on GPUs
- MPS lets multiple inference processes share a single GPU context, overlapping kernels
- Finds meaningful throughput wins for small models (<=3B params) with short context, prefill-only workloads, and CPU-bottlenecked engines
- Explains wins via GPU kernel overlap when engines under-utilize compute/memory bandwidth, plus CPU-sharding benefits
- Matters for cost-effective production serving of small LLMs


### Turbocharged Training: Optimizing the Databricks Mosaic AI Stack With FP8

- **ID:** `dbx-e-turbocharged-training-optimizing-databricks-mosaic-ai-stack-fp8`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/turbocharged-training-optimizing-databricks-mosaic-ai-stack-fp8
- **Date:** 2024-03-21
- **Authors:** Mihir Patel|Cheng Li|Saaketh Narayan
- **Track:** engineering
- **Contribution type:** empirical-study
- **Techniques:** quantization

**Summary:**

- Databricks describes FP8 training optimizations in the Mosaic AI stack on NVIDIA H100s
- Achieves 1.4x-1.5x speedup over BF16 at >50% MFU (highest reported among LLM training frameworks)
- Shows FP8 and BF16 loss curves track closely, minimal impact on convergence
- Covers techniques that enable scaling to thousands of GPUs
- Matters for cost-effective large-scale pretraining


### Learning sparse neural networks through L₀ regularization

- **ID:** `oai-r-learning-sparse-neural-networks-through-l0-regularization`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-sparse-neural-networks-through-l0-regularization/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Proposes practical L0-norm regularization to prune weights during training by forcing them exactly to zero
- Uses stochastic gates with a novel hard-concrete distribution to get a differentiable surrogate
- Enables joint optimization of gates with network parameters
- Improves generalization and allows conditional computation
- Matters as a foundational differentiable-pruning method.

