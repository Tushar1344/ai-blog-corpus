# AI Blog Corpus v2 — What's Interesting

**Opinionated executive synthesis** of 695 in-scope research/engineering posts across **12 AI organizations**: Anthropic, OpenAI, Databricks Mosaic AI, Cursor, Vercel, Cognition, Thinking Machines, Google Research, Google DeepMind, Meta FAIR, Hugging Face, Allen Institute for AI (AI2), and DeepSeek.

Organized around **8 focus areas** (primary axis). Company is a secondary axis. Published launches without technical substance and inference-optimization/kernel/serving-infra posts are explicitly excluded from v2.

**Master Sheet:** https://docs.google.com/spreadsheets/d/1td1T6wCEnw4EeG05I_hH1dK1aNkLR5HJZZ-4jr-Du9A/edit

**Markdown library:** https://github.com/Tushar1344/ai-blog-corpus

---

## Scope — v2 filter

**IN scope:** core model training, post-training & fine-tuning, alignment & safety, interpretability, evaluations, quantization/efficiency, agentic systems, harness/context engineering.

**OUT of scope:** inference optimization (speculative decoding, KV cache, Flash Attention internals), kernel work (CUDA/Triton), hardware benchmarks (H100/Gaudi), general serving infra, applied product stories without methodology.

Re-filtered 548 v1 posts → ~449 retained; added 247 new posts from Tier 1. Total 695.

### Distribution by focus area

| Focus area | Posts | Concentration |
|---|---|---|
| Pretraining & Architecture | 271 | Mostly Meta FAIR, HuggingFace, DeepMind, Databricks |
| Agentic Systems | 112 | Anthropic, OpenAI, Cursor, Cognition, Databricks |
| Alignment & Safety | 95 | Anthropic dominates; OpenAI system cards; DeepMind safety work |
| Evaluations & Benchmarks | 77 | Spread across all labs; AI2 leaderboard work |
| Harness & Context Engineering | 69 | Anthropic, OpenAI, Cursor, Vercel |
| Post-training & Fine-tuning | 34 | HuggingFace, Anthropic, DeepSeek, Thinking Machines |
| Quantization & Efficiency | 20 | HF bitsandbytes, MosaicML efficient-training |
| Interpretability | 17 | Almost entirely Anthropic |

### Distribution by company

| Company | Posts |
|---|---|
| OpenAI | 187 |
| Anthropic | 125 |
| Hugging Face | 115 |
| Databricks Mosaic | 76 |
| Meta FAIR | 61 |
| DeepMind | 34 |
| Vercel | 32 |
| AI2 | 18 |
| Cursor | 14 |
| DeepSeek | 13 |
| Cognition | 11 |
| Google Research | 5 |
| Thinking Machines | 4 |

---

## Cross-company takes by focus area

### Pretraining & Architecture (271 posts)

**Who transparency-publishes training recipes:**
- **Databricks Mosaic AI** (DBRX, MPT, Composer, LLM Foundry, MegaBlocks)
- **AI2** (OLMo, Dolma data, Tulu training recipe)
- **Meta FAIR** (Llama series technical reports, but less of the training data detail than MosaicML or AI2)
- **DeepSeek** (V3 technical report, V2 MoE, Coder-V2 — genuinely detailed)
- **Hugging Face** (as aggregator: FineWeb, Cosmopedia, SmolLM recipes)

**Who publishes architecture research but not training recipes:**
- **DeepMind** (Gemini posts at a high level; deeper on specific components like mixture-of-depths)
- **OpenAI** (system cards + capability evals; architecture kept proprietary)
- **Anthropic** (almost never publishes architecture)

**Novel architectures in the corpus:**
- DeepSeek V3 multi-head latent attention (MLA)
- DeepSeek V2/V3 MoE with fine-grained expert specialization
- DeepSeek-V3.2-Exp sparse attention
- Meta V-JEPA (video joint embedding predictive architecture)
- Meta Megablocks for MoE
- Cursor warp decode for MoE
- Databricks MixAttention
- HF Ultrapeed attention variants

### Alignment & Safety (95 posts)

- **Anthropic** (~60%): alignment faking, sleeper agents, constitutional classifiers, scalable oversight, sycophancy studies, responsible scaling policy, sabotage evals, influence functions, steering.
- **OpenAI** (~25%): Preparedness Framework updates, system cards (GPT-4/5/o1/o3), Model Spec, threat model posts, bio/cyber capability evals, chain-of-thought monitorability.
- **DeepMind**: Frontier Safety Framework, Gemini safety, safety for scientific agents. Less public than Anthropic.
- **Others**: HF contributes on red-teaming datasets; AI2 on Truthfulness. DeepSeek does not publish on alignment.

**Emerging consensus:** frontier labs now disclose dangerous-capability evals (bio, cyber, persuasion, autonomy) before launch. **Emerging divergence:** Anthropic's "alignment faking" research vs. OpenAI's tendency to frame similar findings as "policy violations" or "chain-of-thought monitoring."

### Interpretability (17 posts)

Almost exclusively **Anthropic** — SAE research, circuits updates (monthly series May 2023–Oct 2024), dictionary learning, feature viz, steering, monosemanticity.

Rare contributors: DeepMind has one Gemma Scope post. HuggingFace hosts a few interpretability tutorials. No other company publishes mechanistic interpretability at scale.

**This is the sharpest industry divergence in the corpus** — interpretability is essentially a one-lab field.

### Agentic Systems (112 posts)

Most active focus area. Several sub-clusters:

- **Coding agents as production practice**: Anthropic (Claude Code, multi-agent research system, skills, sandboxing), OpenAI (Codex harness, in-house data agent, Atlas), Cursor (Composer, Bugbot, agent-computer-use), Cognition (Devin engineering, Agent Trace, SWE-grep), GitHub Copilot (adjacent but out of corpus).
- **Enterprise agents**: Databricks (KARL, Agentic Reasoning in Practice, Memory Scaling), HuggingFace (agent framework posts).
- **Embodied / simulation**: Meta FAIR (Habitat challenges, embodied AI research).
- **Browser/computer use**: OpenAI (Operator, Atlas), Anthropic (computer use), Cursor (agent-computer-use).

**Public disagreement:** Anthropic "How we built our multi-agent research system" (2025-06-13) vs. Cognition "Don't Build Multi-Agents" (2025-06-12). Literally adjacent days, opposite conclusions.

### Evaluations & Benchmarks (77 posts)

- **Benchmark creation:** SWE-bench (Cognition technical report), Tau-Bench (Anthropic), BrowseComp (OpenAI), GPQA-adjacent work (Anthropic), OfficeQA (Databricks), Paloma (AI2), HumanEval/MBPP adjacent (HF).
- **Benchmark critique:** Anthropic "Eval awareness in Claude Opus 4.6's BrowseComp", "Quantifying infrastructure noise in agentic coding evals", OpenAI "Why SWE-bench Verified no longer measures frontier coding capabilities". A new genre: publicly doubting your own benchmarks.
- **LLM-as-judge methodology:** Databricks (Custom Judges, PGRM reward model, Judge with Confidence), HF (TRL evaluations), Anthropic (eval infrastructure).
- **Capability evals for safety:** OpenAI (Preparedness), Anthropic (dangerous capability evals), DeepMind (Frontier Safety evals).

### Post-training & Fine-tuning (34 posts)

**Undercounted because many posts in pretraining-and-architecture are actually about mixed pre/post training.** The 34 tightly-matched posts:

- **RLVR** (verifiable rewards): Thinking Machines (LoRA Without Regret, On-Policy Distillation), Cognition (Kevin-32B CUDA kernels), Databricks (RLVR SQL Reasoning, TAO).
- **RLHF classics**: OpenAI (Fine-tuning GPT-2 from preferences, Learning to Summarize with Human Feedback, WebGPT, InstructGPT history).
- **DPO and successors**: HuggingFace posts on Zephyr-ORPO, KTO.
- **Distillation**: Thinking Machines On-Policy Distillation, DeepSeek distillation from R1.
- **Data for post-training**: AI2 Tulu-3, HuggingFace UltraFeedback/UltraChat.

### Quantization & Efficiency (20 posts)

Small corpus — most inference-specific quantization was dropped. What remains:
- Databricks FP8 training
- HuggingFace bitsandbytes series, AWQ/GPTQ explainers
- PEFT (LoRA) training/serving
- Anthropic Matryoshka scaling (not in this category directly — landed in pretraining)
- Mosaic quantized training posts

### Harness & Context Engineering (69 posts)

A relatively new discipline ('24-'26). Leaders:
- **Anthropic**: Harness design for long-running apps, Effective context engineering, Writing effective tools, Claude Code sandboxing, Skills, MCP posts (8+).
- **OpenAI**: Harness engineering (Codex), Unlocking the Codex harness, Inside in-house data agent.
- **Cursor**: agent sandboxing, long-running agents, fast regex, self-summarization.
- **Vercel**: Durable execution programming model, Agent responsibly, AI SDK.
- **HuggingFace**: `smolagents` framework, tool-use tutorials.

---

## Companies with distinct profiles

### DeepSeek (13 in-scope)
Pure model-technical-report lab. Every release is a methodologically-dense paper — V3 MLA attention, R1 reasoning via RL, Prover-V2 formal math via MCTS, Coder-V2 repo training. Highest signal density per post of any company in the corpus.

### Hugging Face (115 in-scope)
Acts as the **applied-engineering aggregator** for everyone else's models. Posts include: reproduction recipes (Zephyr-ORPO for Mistral/Mixtral post-training), tutorials for new techniques (TRL, PEFT), dataset releases (FineWeb, Cosmopedia, UltraChat), and the community's "how to actually use" layer on top of every frontier release. Sits between research and practitioner.

### AI2 / Allen Institute (18 in-scope after filter)
The **reproducibility lab**. OLMo, Dolma, Tulu, Paloma — only org that ships full training data + recipe for frontier-scale models. Small number of corpus posts but every one matters.

### Meta FAIR (61 in-scope)
Long tail of published research (600+ blog entries all-time, 61 survived v2 filter). Strongest in: multimodal (SAM, SAM 2, DINO, V-JEPA, ImageBind), embodied AI (Habitat, Meta robot), and the Llama model releases. Lighter on post-training public-facing research compared to OpenAI/Anthropic.

### Google DeepMind (34 in-scope)
Broader science-applied AI coverage. Strong on: foundation-model-for-science (AlphaFold, AlphaGeometry, AlphaProof, Aeneas), agentic reasoning (Gemini Deep Think for IMO/IOI), and safety policy. Publishes less training detail than FAIR/AI2.

### Google Research (5 in-scope)
Separate from DeepMind since the 2023 merge. Most of the "Google Research blog" content is applied ML (device ML, translation, healthcare) — only a handful survive v2's LLM-research filter.

---

## Divergences

1. **Multi-agent orchestration** — Anthropic "How we built our multi-agent research system" (2025-06-13) vs. Cognition "Don't Build Multi-Agents" (2025-06-12).
2. **Benchmark trustworthiness** — Anthropic ("Eval awareness in BrowseComp", "Infrastructure noise") and OpenAI ("Why SWE-bench Verified no longer measures frontier coding") both public-doubt benchmarks, but phrase it differently: Anthropic as a methodology concern, OpenAI as "time for a new benchmark."
3. **Agent harness vs. model capability** — Cursor treats harness + model as jointly trainable (real-time RL for Composer). Anthropic treats them as decoupled (Effective harnesses, Harness design for long-running apps).
4. **Pretraining transparency** — AI2 ships data + recipe (OLMo, Dolma). Databricks Mosaic ships architecture + hyperparameters (DBRX, MPT). DeepSeek ships architecture + training methodology (V3, R1). Meta FAIR ships model weights + paper but less data/recipe detail. OpenAI/Anthropic ship neither.
5. **Interpretability** — Anthropic is alone. A strategic bet or blind spot for the rest of the industry.
6. **Post-training** — OpenAI/Anthropic framings focus on alignment; Thinking Machines/HuggingFace frame it as capability; AI2 as reproducibility.

## Temporal arc (revised)

- **2017–2021**: Foundation research — scaling laws, early RLHF (OpenAI), Transformers iteration, meta-learning. Most of Google Research + FAIR early posts.
- **2022**: InstructGPT era; Meta Llama 1; early MosaicML efficiency work.
- **2023**: RLHF ubiquitous. MPT, Llama 2, DBRX precursors. First Circuits posts (Anthropic). System cards emerge as a genre. DeepSeek-LLM, DeepSeek-Math first releases.
- **2024**: Agents go production. DBRX technical report. Long context. Reasoning begins (o1 family). Alignment faking paper. DeepSeek-V2/V3, Coder-V2 ship.
- **2025**: RLVR overtakes RLHF. Test-time compute. Thinking Machines launches. DeepSeek-R1 reasoning. Tulu-3 reproducibility. Computer use. Anthropic Skills + MCP. Multi-agent debate.
- **2026 YTD**: Agent harness as a discipline. Enterprise agents at scale. Eval awareness/sandbagging studies. MCP everywhere. Agent sandboxing normalized. Kernel-RL (Cognition Kevin-32B, Cursor multi-agent kernels — though those cross into our excluded category).

---

## Standout posts (must-read shortlist, ~40)

**Pretraining / architecture:** DBRX Technical Report (Databricks) · MPT-30B (Databricks) · OLMo-1 & OLMo-2 (AI2) · Llama 3 Paper (Meta) · DeepSeek-V3 (DeepSeek) · DeepSeek-MoE (DeepSeek) · FineWeb (HuggingFace) · Dolma 1.7 (AI2) · SAM 2 (Meta) · V-JEPA (Meta)

**Post-training & fine-tuning:** On-Policy Distillation (Thinking Machines) · LoRA Without Regret (Thinking Machines) · DeepSeek-R1 (DeepSeek) · Kevin-32B (Cognition) · Tulu-3 (AI2) · Constitutional Classifiers (Anthropic) · PGRM (Databricks)

**Alignment & safety:** Alignment faking in LLMs (Anthropic) · Sleeper Agents (Anthropic) · Responsible Scaling Policy updates (Anthropic) · Preparedness Framework (OpenAI) · Frontier Safety Framework (DeepMind) · Chain-of-thought monitorability (OpenAI) · Model Spec (OpenAI) · Influence Functions (Anthropic)

**Interpretability:** Towards Monosemanticity (Anthropic) · Circuits Updates series (Anthropic, monthly) · Gemma Scope (DeepMind) · Steering Claude (Anthropic)

**Agentic systems:** How we built our multi-agent research system (Anthropic) · Don't Build Multi-Agents (Cognition) · Effective harnesses for long-running agents (Anthropic) · Harness engineering (OpenAI) · SWE-bench technical report (Cognition) · Agent Trace (Cognition) · Claude Code sandboxing (Anthropic) · Writing effective tools for AI agents (Anthropic) · Habitat Challenges series (Meta) · Cursor agents can now control their own computers

**Evals:** Demystifying evals (Anthropic) · Eval awareness in BrowseComp (Anthropic) · Paloma (AI2) · OfficeQA (Databricks) · Why SWE-bench Verified no longer measures frontier (OpenAI)

**Harness:** Effective context engineering (Anthropic) · Harness design for long-running apps (Anthropic) · Unlocking the Codex harness (OpenAI) · OWL / Atlas architecture (OpenAI)

---

## Gaps (still)

- Honest retrospectives on deprecated techniques (what DIDN'T work).
- Pure economics of inference at frontier scale.
- Data cleaning pipelines (depuping, PII, filtering) — despite FineWeb + Dolma being exceptions, most labs don't detail this.
- Small-model work beyond HuggingFace's SmolLM line.
- Quantization-at-training (FP8 era details) — Databricks is alone here.
- Evaluation reproducibility — everyone talks about evals, nobody ships a reproducible test harness.
- Sample-efficiency research — RL-style sample efficiency work from pre-LLM era hasn't been carried forward.

## Limitations of v2

1. **Classification is heuristic.** ~271 posts land in "pretraining-and-architecture" including many that belong elsewhere (especially OpenAI research posts that default to pretraining when no specific rule matches). Summaries will refine this.
2. **Summaries pending.** Each entry in `by-focus-area/*.md` has a "Summary pending" slot. A follow-up pass is needed to populate 3-5 bullet summaries per post (the main remaining work).
3. **Meta / DeepMind / Google Research slug-derived titles.** Wayback-based enumeration means titles are slug-derived; real titles can be backfilled by fetching post pages via headless browser.
4. **DeepMind 34 vs. expected ~100.** Current filter is tight — expect to add ~50-70 more on a second pass with looser rules.
5. **AI2 18 vs expected ~100.** Their blog is heavily scientific-discovery content (not LLM), and my filter drops most. Retaining OLMo / Tulu / Dolma / Paloma.

## Iteration workflow

- Re-filter the sheet: edit rules in `_data/consolidate_v2.py` or `_data/assign_focus_area.py`, re-run.
- Regenerate markdown: `python3 _data/generate_markdown_v2.py`.
- Re-upload sheet: `python3 _data/upload_sheet.py`.
- Add a new company: drop rows into a new `enum-{name}.csv`, re-run consolidate + generator.

---

*v2 generated 2026-04-19 — re-scoped around 8 focus areas, added 5 Tier 1 labs (DeepMind, Meta FAIR, HuggingFace, AI2, DeepSeek), tightened out of inference/kernel/serving noise.*
