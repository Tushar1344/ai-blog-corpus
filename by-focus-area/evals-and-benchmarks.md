# Evaluations & Benchmarks

New eval suites, benchmark analyses, eval methodology (SWE-bench, Tau-Bench, BrowseComp, GPQA, HELM, etc.).

**Post count:** 87

**Contributors:**

- Hugging Face: 41
- OpenAI: 11
- Databricks Mosaic AI: 9
- Anthropic: 8
- Meta AI / FAIR: 7
- Google DeepMind: 4
- Cursor: 2
- Allen Institute for AI: 2
- Vercel: 1
- Cognition: 1
- Google Research: 1

**Subcategories:**

- [Agent evaluations](#agent-evals) (6)
- [Coding evaluations](#coding-evals) (7)
- [Reasoning & math evaluations](#reasoning-evals) (3)
- [Leaderboards & community evals](#leaderboards-and-community-evals) (27)
- [Judge models & eval methodology](#judge-models-and-methodology) (10)
- [Eval systems & harnesses](#eval-systems-and-harnesses) (11)
- [Benchmark releases](#benchmark-release) (6)
- [Domain-specific evals (speech, vision, science, medical)](#domain-specific-evals) (11)
- [Benchmark critique](#benchmark-critique) (5)

---

## <a id="agent-evals"></a>Agent evaluations

_6 posts_

### AGENTS.md outperforms skills in our agent evals

- **ID:** `vcl-e-agents-md-outperforms-skills-in-our-agent-evals`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
- **Date:** 2026-01-27
- **Authors:** Jude Gao
- **Track:** engineering
- **Contribution type:** dataset-benchmark
- **Techniques:** evals-eval-harness

**Summary:**

- Vercel built evals focused on Next.js 16 APIs and compared Skills (bundled prompts/tools/docs) against an embedded AGENTS.md approach
- finding: an 8KB compressed docs index in AGENTS.md hit 100% pass rate vs Skills maxing at 79% even with explicit invocation instructions
- without explicit instructions, Skills performed no better than no docs at all
- reframes 'always-on context' vs on-demand skills trade-off for framework-specific knowledge
- practical evidence for context-engineering choices in coding agents.


### Introducing OfficeQA: A Benchmark for End-to-End Grounded Reasoning

- **ID:** `dbx-r-introducing-officeqa-benchmark-end-to-end-grounded-reasoning`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/introducing-officeqa-benchmark-end-to-end-grounded-reasoning
- **Date:** 2025-12-09
- **Track:** research
- **Contribution type:** dataset-benchmark
- **Techniques:** evals-eval-harness

_Summary pending — see link for details._


### DABStep: Data Agent Benchmark for Multi-step Reasoning

- **ID:** `hf-r-dabstep`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/dabstep
- **Date:** 2025-02-04
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Our Transformers Code Agent beats the GAIA benchmark 🏅

- **ID:** `hf-r-beating-gaia`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/beating-gaia
- **Date:** 2024-07-01
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Evaluating Multimodal Interactive Agents

- **ID:** `dm-r-evaluating-multimodal-interactive-agents`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/evaluating-multimodal-interactive-agents/
- **Date:** 2022-05-27
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- DeepMind proposes the Standardised Test Suite (STS) for evaluating multimodal interactive agents in temporally extended 3D human interactions
- replays behavioral scenarios mined from real human-human interactions, lets the agent take control to finish the interaction, and has human raters annotate success
- rank agents by success rate across scenarios
- argues Atari-style RL metrics don't work for fluid human interaction
- classic agent-evals methodology contribution.


### BrowseComp: a benchmark for browsing agents

- **ID:** `oai-r-browsecomp`
- **Company:** OpenAI
- **Link:** https://openai.com/index/browsecomp/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** dataset-benchmark
- **Techniques:** BrowseComp, evals-eval-harness

_Summary pending — see link for details._


## <a id="coding-evals"></a>Coding evaluations

_7 posts_

### How we compare model quality in Cursor We use a hybrid online-offline eval process to keep our understanding of model quality aligned with what developers actually do. Naman Jain ·

- **ID:** `cur-r-cursorbench`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/cursorbench
- **Date:** 2026-03-11
- **Track:** research
- **Contribution type:** dataset-benchmark
- **Techniques:** coding-agents, evals-eval-harness

_Summary pending — see link for details._


### Designing AI resistant technical evaluations

- **ID:** `ant-e-ai-resistant-technical-evaluations`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/AI-resistant-technical-evaluations
- **Date:** 2026-01-21
- **Authors:** Tristan Hume
- **Track:** engineering
- **Contribution type:** empirical-study

**Summary:**

- Case study on redesigning a performance-engineering take-home test across three iterations as Claude models (Opus 4, 4.5) beat the prior version
- Candidates optimize code for a simulated accelerator
- over 1,000 have taken it and dozens now work at Anthropic
- Each Claude upgrade forced changes because Claude could match or beat top humans in the time limit
- Discusses what makes evaluations robust (or not) to AI assistance and releases the original take-home as an open challenge
- Relevant to designing AI-resistant hiring/coding evals in the agent era.


### PaperBench: Evaluating AI’s Ability to Replicate AI Research

- **ID:** `oai-r-paperbench`
- **Company:** OpenAI
- **Link:** https://openai.com/index/paperbench/
- **Date:** 2025-04-02
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Claude SWE-Bench Performance

- **ID:** `ant-e-swe-bench-sonnet`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/swe-bench-sonnet
- **Date:** 2025-01-06
- **Track:** engineering
- **Contribution type:** dataset-benchmark
- **Techniques:** coding-agents, SWE-bench

_Summary pending — see link for details._


### Claude SWE-Bench Performance

- **ID:** `ant-r-swe-bench-sonnet`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/swe-bench-sonnet
- **Date:** 2025-01-06
- **Track:** research
- **Contribution type:** dataset-benchmark
- **Techniques:** coding-agents, SWE-bench

_Summary pending — see link for details._


### BigCodeBench: The Next Generation of HumanEval

- **ID:** `hf-r-leaderboard-bigcodebench`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-bigcodebench
- **Date:** 2024-06-18
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### SWE-bench technical report

- **ID:** `cog-r-swe-bench-technical-report`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/swe-bench-technical-report
- **Date:** 2024-03-15
- **Track:** research
- **Contribution type:** dataset-benchmark
- **Techniques:** coding-agents, SWE-bench

_Summary pending — see link for details._


## <a id="reasoning-evals"></a>Reasoning & math evaluations

_3 posts_

### Olmo 1 7 7B A 24 Point Improvement On Mmlu 92B43F7D269D

- **ID:** `ai2-r-olmo-1-7-7b-a-24-point-improvement-on-mmlu-92b43f7d269d`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/olmo-1-7-7b-a-24-point-improvement-on-mmlu-92b43f7d269d
- **Date:** 2024-04-17
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Solving math word problems

- **ID:** `oai-r-solving-math-word-problems`
- **Company:** OpenAI
- **Link:** https://openai.com/index/solving-math-word-problems/
- **Date:** 2024-01-12
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Introduces GSM8K dataset (8.5K grade-school math word problems, 2-8 reasoning steps)
- Trains verifiers that rank 100 candidate solutions, selecting the highest-rated — gives roughly a 30x effective-model-size boost (6B verifier beats fine-tuned 175B)
- Demonstrates that verification scales better with data than pure fine-tuning
- Canonical reasoning benchmark + a precursor to process-reward-modeling and best-of-N approaches
- Matters for evaluating and improving multistep mathematical reasoning in LLMs.


### What's going on with the Open LLM Leaderboard?

- **ID:** `hf-r-open-llm-leaderboard-mmlu`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/open-llm-leaderboard-mmlu
- **Date:** 2023-06-23
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="leaderboards-and-community-evals"></a>Leaderboards & community evals

_27 posts_

### Community Evals: Because we're done trusting black-box leaderboards over the community

- **ID:** `hf-r-community-evals`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/community-evals
- **Date:** 2026-02-04
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Open ASR Leaderboard: Trends and Insights with New Multilingual & Long-Form Tracks

- **ID:** `hf-r-open-asr-leaderboard`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/open-asr-leaderboard
- **Date:** 2025-11-21
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### TimeScope: How Long Can Your Video Large Multimodal Model Go?

- **ID:** `hf-r-timescope-video-lmm-benchmark`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/timescope-video-lmm-benchmark
- **Date:** 2025-07-23
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Arabic Leaderboards: Introducing Arabic Instruction Following, Updating AraGen, and More

- **ID:** `hf-r-leaderboard-3c3h-aragen-ifeval`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-3c3h-aragen-ifeval
- **Date:** 2025-04-08
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Fixing Open LLM Leaderboard with Math-Verify

- **ID:** `hf-r-math_verify_leaderboard`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/math_verify_leaderboard
- **Date:** 2025-02-14
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### The Open Arabic LLM Leaderboard 2

- **ID:** `hf-r-leaderboard-arabic-v2`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-arabic-v2
- **Date:** 2025-02-10
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### CO₂ Emissions and Models Performance: Insights from the Open LLM Leaderboard

- **ID:** `hf-r-leaderboard-emissions-analysis`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-emissions-analysis
- **Date:** 2025-01-09
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Rethinking LLM Evaluation with 3C3H: AraGen Benchmark and Leaderboard

- **ID:** `hf-r-leaderboard-3c3h-aragen`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-3c3h-aragen
- **Date:** 2024-12-04
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing the Open Leaderboard for Japanese LLMs!

- **ID:** `hf-r-leaderboard-japanese`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-japanese
- **Date:** 2024-11-20
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing the Open FinLLM Leaderboard

- **ID:** `hf-r-leaderboard-finbench`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-finbench
- **Date:** 2024-10-04
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing the Open Arabic LLM Leaderboard

- **ID:** `hf-r-leaderboard-arabic`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-arabic
- **Date:** 2024-05-14
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing the Open Leaderboard for Hebrew LLMs!

- **ID:** `hf-r-leaderboard-hebrew`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-hebrew
- **Date:** 2024-05-05
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Bringing the Artificial Analysis LLM Performance Leaderboard to Hugging Face

- **ID:** `hf-r-leaderboard-artificial-analysis`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-artificial-analysis
- **Date:** 2024-05-03
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing the Open Chain of Thought Leaderboard

- **ID:** `hf-r-leaderboard-cot`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-cot
- **Date:** 2024-04-23
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### The Open Medical-LLM Leaderboard: Benchmarking Large Language Models in Healthcare

- **ID:** `hf-r-leaderboard-medicalllm`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-medicalllm
- **Date:** 2024-04-19
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Rewardbench The First Benchmark Leaderboard For Reward Models Used In Rlhf 1D4D7D04A90B

- **ID:** `ai2-r-rewardbench-the-first-benchmark-leaderboard-for-reward-models-used-in-rlhf-1d4d7d04a90b`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/rewardbench-the-first-benchmark-leaderboard-for-reward-models-used-in-rlhf-1d4d7d04a90b
- **Date:** 2024-03-20
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing ConTextual: How well can your Multimodal model jointly reason over text and image in text-rich scenes?

- **ID:** `hf-r-leaderboard-contextual`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-contextual
- **Date:** 2024-03-05
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing the Red-Teaming Resistance Leaderboard

- **ID:** `hf-r-leaderboard-haizelab`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-haizelab
- **Date:** 2024-02-23
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing the Open Ko-LLM Leaderboard: Leading the Korean LLM Evaluation Ecosystem

- **ID:** `hf-r-leaderboard-upstage`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-upstage
- **Date:** 2024-02-20
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### NPHardEval Leaderboard: Unveiling the Reasoning Abilities of Large Language Models through Complexity Classes and Dynamic Updates

- **ID:** `hf-r-leaderboard-nphardeval`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-nphardeval
- **Date:** 2024-02-02
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing the Enterprise Scenarios Leaderboard: a Leaderboard for Real World Use Cases

- **ID:** `hf-r-leaderboard-patronus`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-patronus
- **Date:** 2024-01-31
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### The Hallucinations Leaderboard, an Open Effort to Measure Hallucinations in Large Language Models

- **ID:** `hf-r-leaderboard-hallucinations`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-hallucinations
- **Date:** 2024-01-29
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### An Introduction to AI Secure LLM Safety Leaderboard

- **ID:** `hf-r-leaderboard-decodingtrust`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-decodingtrust
- **Date:** 2024-01-26
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### A guide to setting up your own Hugging Face leaderboard: an end-to-end example with Vectara's hallucination leaderboard

- **ID:** `hf-r-leaderboard-vectara`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-vectara
- **Date:** 2024-01-12
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Open LLM Leaderboard: DROP deep dive

- **ID:** `hf-r-open-llm-leaderboard-drop`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/open-llm-leaderboard-drop
- **Date:** 2023-12-01
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Object Detection Leaderboard

- **ID:** `hf-r-object-detection-leaderboard`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/object-detection-leaderboard
- **Date:** 2023-09-18
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Can foundation models label data like humans?

- **ID:** `hf-r-open-llm-leaderboard-rlhf`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/open-llm-leaderboard-rlhf
- **Date:** 2023-06-12
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="judge-models-and-methodology"></a>Judge models & eval methodology

_10 posts_

### Measuring AI agent autonomy in practice

- **ID:** `ant-r-measuring-agent-autonomy`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/measuring-agent-autonomy
- **Date:** 2026-02-18
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Measuring AI’s capability to accelerate biological research in the wet lab

- **ID:** `oai-r-accelerating-biological-research-in-the-wet-lab`
- **Company:** OpenAI
- **Link:** https://openai.com/index/accelerating-biological-research-in-the-wet-lab/
- **Date:** 2025-12-18
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### From Pilot to Production with Custom Judges

- **ID:** `dbx-r-pilot-production-custom-judges`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/pilot-production-custom-judges
- **Date:** 2025-11-04
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Judging with Confidence: Meet PGRM, the Promptable Reward Model

- **ID:** `dbx-r-judging-confidence-meet-pgrm-promptable-reward-model`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/judging-confidence-meet-pgrm-promptable-reward-model
- **Date:** 2025-08-12
- **Track:** research
- **Contribution type:** new-method
- **Techniques:** RLHF, reward-modeling

_Summary pending — see link for details._


### ScreenSuite - The most comprehensive evaluation suite for GUI Agents!

- **ID:** `hf-r-screensuite`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/screensuite
- **Date:** 2025-06-06
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Judge Arena: Benchmarking LLMs as Evaluators

- **ID:** `hf-r-arena-atla`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/arena-atla
- **Date:** 2024-11-19
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Expert Support case study: Bolstering a RAG app with LLM-as-a-Judge

- **ID:** `hf-r-digital-green-llm-judge`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/digital-green-llm-judge
- **Date:** 2024-10-28
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Launching the Artificial Analysis Text to Image Leaderboard & Arena

- **ID:** `hf-r-leaderboard-artificial-analysis2`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-artificial-analysis2
- **Date:** 2024-06-06
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### CyberSecEval 2 - A Comprehensive Evaluation Framework for Cybersecurity Risks and Capabilities of Large Language Models

- **ID:** `hf-r-leaderboard-llamaguard`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-llamaguard
- **Date:** 2024-05-24
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Melting Pot An Evaluation Suite For Multi Agent Reinforcement Learning

- **ID:** `dm-r-melting-pot-an-evaluation-suite-for-multi-agent-reinforcement-learning`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/melting-pot-an-evaluation-suite-for-multi-agent-reinforcement-learning/
- **Date:** 2021-07-14
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="eval-systems-and-harnesses"></a>Eval systems & harnesses

_11 posts_

### Evaluating AI’s ability to perform scientific research tasks

- **ID:** `oai-r-frontierscience`
- **Company:** OpenAI
- **Link:** https://openai.com/index/frontierscience/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Demystifying evals for AI agents

- **ID:** `ant-e-demystifying-evals-for-ai-agents`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- **Date:** 2026-01-09
- **Authors:** Mikaela Grace|Jeremy Hadfield|Rodrigo Olivares|Jiri De Jonghe
- **Track:** engineering
- **Contribution type:** dataset-benchmark
- **Techniques:** evals-eval-harness

_Summary pending — see link for details._


### Benchmarking Domain Intelligence

- **ID:** `dbx-r-benchmarking-domain-intelligence`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/benchmarking-domain-intelligence
- **Date:** 2024-12-17
- **Authors:** Pallavi Koppol|Erica Ji Yuen|Kartik Sreenivasan|Andy Zhang|Sam Havens|Michael Carbin|Matei Zaharia|Jonathan Frankle
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### A statistical approach to model evaluations

- **ID:** `ant-r-statistical-approach-to-model-evals`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/statistical-approach-to-model-evals
- **Date:** 2024-11-19
- **Track:** research
- **Contribution type:** dataset-benchmark
- **Techniques:** evals-eval-harness

_Summary pending — see link for details._


### Calibrating the Mosaic Evaluation Gauntlet

- **ID:** `dbx-r-calibrating-mosaic-evaluation-gauntlet`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/calibrating-mosaic-evaluation-gauntlet
- **Date:** 2024-04-30
- **Authors:** Tessa Barton
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Llama 2 on Amazon SageMaker a Benchmark

- **ID:** `hf-r-llama-sagemaker-benchmark`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/llama-sagemaker-benchmark
- **Date:** 2023-09-26
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- HF benchmarks Llama 2 deployment on Amazon SageMaker with HF LLM Inference Container across 60+ configs
- measures latency (ms/token) and throughput (tok/s) to identify best deployments for three profiles: cost-effective, lowest-latency, highest-throughput
- publishes code, raw data, and spreadsheet for reproducibility
- infrastructure/eval harness oriented rather than model-capability benchmarking.


### End-to-End Secure Evaluation of Code Generation Models

- **ID:** `dbx-r-secure-code-evaluation`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/secure-code-evaluation
- **Date:** 2023-08-10
- **Authors:** Rishab Parthasarathy
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Blazingly Fast LLM Evaluation for In-Context Learning

- **ID:** `dbx-r-llm-evaluation-for-icl`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/llm-evaluation-for-icl
- **Date:** 2023-02-02
- **Authors:** Jeremy Dohmann
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Faster Training and Inference: Habana Gaudi®2 vs Nvidia A100 80GB

- **ID:** `hf-r-habana-gaudi-2-benchmark`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/habana-gaudi-2-benchmark
- **Date:** 2022-12-14
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- Hardware benchmark comparing Habana Gaudi2 vs Gaudi vs Nvidia A100 80GB on BERT pretraining, Stable Diffusion inference, and T5-3B fine-tuning using Optimum Habana
- spoiler claim: Gaudi2 ~2x faster than A100 80GB for both training and inference
- walks through Intel Developer Cloud access and Optimum Habana workflow
- primarily an infra/hardware benchmark rather than model-capability eval.


### Very Large Language Models and How to Evaluate Them

- **ID:** `hf-r-zero-shot-eval-on-the-hub`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/zero-shot-eval-on-the-hub
- **Date:** 2022-10-03
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- Adds zero-shot evaluation for causal LMs to HF 'Evaluation on the Hub' powered by AutoTrain
- motivated by efforts like the Inverse Scaling Prize where zero-shot measurement across model sizes is central
- enables any causal LM on the Hub to be evaluated zero-shot without writing code, including 66B-param models that normally take 35+ minutes just to load
- infrastructure is upgraded to do this for free
- eval harness/tooling contribution.


### Announcing Evaluation on the Hub

- **ID:** `hf-r-eval-on-the-hub`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/eval-on-the-hub
- **Date:** 2022-06-28
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- Announces Evaluation on the Hub (AutoTrain-powered) letting users evaluate any model on any dataset on the Hub with no code
- motivation is the reproducibility/evaluation crisis: inconsistent implementations, self-reported results, metric sprawl
- goal is community best-practices and lowering friction
- (archived as of Nov 2023 with pointer to leaderboards collection)
- eval systems/harness post.


## <a id="benchmark-release"></a>Benchmark releases

_6 posts_

### Measuring the performance of our models on real-world tasks

- **ID:** `oai-r-gdpval`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gdpval/
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Introduces GDPval, a benchmark of 1,320 economically-valuable tasks (220 in an open gold set) across 44 occupations in the top 9 US GDP industries
- Tasks drawn from real professional work products (legal briefs, engineering blueprints, nursing care plans, etc.) vetted by experts with 14+ years experience
- Goes beyond academic benchmarks (MMLU, SWE-Bench) to economically realistic knowledge work
- One-shot only in v1
- deliverables span docs, slides, spreadsheets, diagrams, multimedia
- Intended to ground discussions of AI's real-world capability and economic impact.


### GamePad: A learning environment for theorem proving

- **ID:** `oai-r-gamepad`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gamepad/
- **Date:** 2024-03-21
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Introduces GamePad, a Coq-based learning environment for ML-driven theorem proving
- Trains baselines on Feit-Thompson formalization for position evaluation and tactic prediction
- Supports supervised step-by-step proof construction with machine-checkable proofs
- Provides a platform for studying interactive theorem proving with human supervision
- Matters as foundational environment for later neural theorem provers.


### Gotta Learn Fast: A new benchmark for generalization in RL

- **ID:** `oai-r-gotta-learn-fast`
- **Company:** OpenAI
- **Link:** https://openai.com/index/gotta-learn-fast/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** dataset-benchmark
- **Techniques:** evals-eval-harness

_Summary pending — see link for details._


### MTEB: Massive Text Embedding Benchmark

- **ID:** `hf-r-mteb`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/mteb
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- Introduces MTEB (Massive Text Embedding Benchmark): 56 datasets across 8 embedding tasks (retrieval, STS, classification, clustering, reranking, etc.) with 2000+ results on the leaderboard
- multilingual coverage up to 112 languages on Bitext Mining/Classification/STS
- extensible design for new tasks/datasets
- paper analyzes leaderboard results and model trade-offs
- canonical benchmark-release post.


### Ctrl And Mntdp A New Open Source Benchmark And Model For Continual Learning

- **ID:** `meta-r-ctrl-and-mntdp-a-new-open-source-benchmark-and-model-for-continual-learning`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/ctrl-and-mntdp-a-new-open-source-benchmark-and-model-for-continual-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- Title-only: Meta FAIR introduces CTrL benchmark and MNTDP model for continual learning
- frames as open-source benchmark + model release
- content blocked by Facebook login
- likely covers transfer and interference across task sequences and a modular network approach (Modular Networks with Task-Driven Prior)
- classified as benchmark-release due to 'new open source benchmark' wording.


### Introducing The Temporal Data Set A Benchmark For Recognizing Actions In Videos

- **ID:** `meta-r-introducing-the-temporal-data-set-a-benchmark-for-recognizing-actions-in-videos`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/introducing-the-temporal-data-set-a-benchmark-for-recognizing-actions-in-videos/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="domain-specific-evals"></a>Domain-specific evals (speech, vision, science, medical)

_11 posts_

### Better AI models enable more ambitious work

- **ID:** `cur-r-better-models-ambitious-work`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/better-models-ambitious-work
- **Date:** 2026-04-15
- **Authors:** Luke Melas-Kyriazi
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** coding-agents

**Summary:**

- Cursor and Prof. Suproteem Sarkar (Chicago Booth) study 500 companies using Cursor from July 2025-March 2026 across Opus 4.5 and GPT-5.2 releases
- AI usage grew 44% (avg weekly messages per user)
- Developers first did more work of similar complexity, later took on harder tasks
- Finance, media, software led adoption with 45-54% growth
- Jevons-like effect: better models increase AI demand rather than reducing it
- Matters as empirical evidence on how model quality drives developer behavior


### From Waveforms to Wisdom: The New Benchmark for Auditory Intelligence

- **ID:** `gr-r-from-waveforms-to-wisdom-the-new-benchmark-for-auditory-intelligence`
- **Company:** Google Research
- **Link:** https://research.google/blog/from-waveforms-to-wisdom-the-new-benchmark-for-auditory-intelligence/
- **Date:** 2025-12-03
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing the SWE-Lancer benchmark

- **ID:** `oai-r-swe-lancer`
- **Company:** OpenAI
- **Link:** https://openai.com/index/swe-lancer/
- **Date:** 2025-07-28
- **Track:** research
- **Contribution type:** dataset-benchmark
- **Techniques:** evals-eval-harness

_Summary pending — see link for details._


### Facts Grounding A New Benchmark For Evaluating The Factuality Of Large Language Models

- **ID:** `dm-r-facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/
- **Date:** 2024-12-17
- **Track:** research
- **Contribution type:** _(uncategorized)_

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

**Summary:**

- Databricks ran 2000+ experiments evaluating 13 LLMs (open and commercial) on long-context RAG across 4 datasets (DocsQA, FinanceBench, HotPotQA, Natural Questions)
- Retrieving more documents helps but most models degrade past a context length (Llama-3.1-405B after 32k, GPT-4-0125 after 64k)
- Identifies distinct failure modes like copyright refusal or always summarizing
- Suggests lack of long-context post-training
- Matters for practitioners tuning RAG systems with long-context LLMs


### Agent57 Outperforming The Human Atari Benchmark

- **ID:** `dm-r-agent57-outperforming-the-human-atari-benchmark`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/agent57-outperforming-the-human-atari-benchmark/
- **Date:** 2020-03-31
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### A New Open Benchmark For Speech Recognition With Limited Or No Supervision

- **ID:** `meta-r-a-new-open-benchmark-for-speech-recognition-with-limited-or-no-supervision`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/a-new-open-benchmark-for-speech-recognition-with-limited-or-no-supervision/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing Kilt A New Unified Benchmark For Knowledge Intensive Nlp Tasks

- **ID:** `meta-r-introducing-kilt-a-new-unified-benchmark-for-knowledge-intensive-nlp-tasks`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/introducing-kilt-a-new-unified-benchmark-for-knowledge-intensive-nlp-tasks/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing Unidentified Video Objects A New Benchmark For Open World Object Segmentation

- **ID:** `meta-r-introducing-unidentified-video-objects-a-new-benchmark-for-open-world-object-segmentation`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/introducing-unidentified-video-objects-a-new-benchmark-for-open-world-object-segmentation/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Muavic Audio Visual Speech Translation Benchmark

- **ID:** `meta-r-muavic-audio-visual-speech-translation-benchmark`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/muavic-audio-visual-speech-translation-benchmark/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Phyre A New Ai Benchmark For Physical Reasoning

- **ID:** `meta-r-phyre-a-new-ai-benchmark-for-physical-reasoning`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/phyre-a-new-ai-benchmark-for-physical-reasoning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="benchmark-critique"></a>Benchmark critique

_5 posts_

### Why SWE-bench Verified no longer measures frontier coding capabilities

- **ID:** `oai-r-why-we-no-longer-evaluate-swe-bench-verified`
- **Company:** OpenAI
- **Link:** https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- **Date:** 2026-03-25
- **Track:** research
- **Contribution type:** dataset-benchmark
- **Techniques:** coding-agents, SWE-bench

_Summary pending — see link for details._


### Quantifying infrastructure noise in agentic coding evals

- **ID:** `ant-e-infrastructure-noise`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/infrastructure-noise
- **Date:** 2026-02-03
- **Authors:** Gian Segato
- **Track:** engineering
- **Contribution type:** dataset-benchmark
- **Techniques:** evals-eval-harness

_Summary pending — see link for details._


### Beyond the Leaderboard: Unpacking Function Calling Evaluation

- **ID:** `dbx-r-unpacking-function-calling-eval`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/unpacking-function-calling-eval
- **Date:** 2024-08-16
- **Authors:** Kartik Sreenivasan|Jeffrey Chen|Pallavi Koppol|Eitan Turok|Bay Foley-Cox|Asfandyar Qureshi|Sam Havens
- **Track:** research
- **Contribution type:** dataset-benchmark
- **Techniques:** tool-use, evals-eval-harness

_Summary pending — see link for details._


### Introducing the LiveCodeBench Leaderboard - Holistic and Contamination-Free Evaluation of Code LLMs

- **ID:** `hf-r-leaderboard-livecodebench`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/leaderboard-livecodebench
- **Date:** 2024-04-16
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Challenges in evaluating AI systems

- **ID:** `ant-r-evaluating-ai-systems`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/evaluating-ai-systems
- **Date:** 2023-10-04
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Policy-oriented reflection on why robust AI evaluations are hard to build
- Walks through challenges at escalating difficulty: multiple-choice (MMLU, BBQ), third-party frameworks (BIG-bench, HELM), crowdworker red-teaming, expert national-security red-teaming, and LLM-as-evaluator
- Concrete examples: prompt-format sensitivity changing MMLU accuracy ~5%, BBQ bias-score misinterpretation when models weren't answering at all
- Concludes with policy recommendations for governance
- Foundational critique of evaluation methodology.

