# AI Blog Corpus — What's Interesting

**Opinionated executive synthesis** across seven AI/developer-infrastructure companies: Anthropic, OpenAI, Databricks Mosaic AI, Cursor, Vercel, Cognition, and Thinking Machines. All-time, technical-substance-filtered.

**Master Sheet (sortable/filterable):** https://docs.google.com/spreadsheets/d/1td1T6wCEnw4EeG05I_hH1dK1aNkLR5HJZZ-4jr-Du9A/edit

**Markdown library:** `~/work_agent/ai-blog-corpus/` — one canonical file per company, plus cross-reference folders `by-technical-domain/`, `by-contribution-type/`, `by-year/`, `by-technique/`.

---

## Scope

| Company | In-scope posts | Coverage |
|---|---|---|
| OpenAI (research + engineering) | 187 | openai.com `/publication/` + `/engineering/` sitemaps |
| Vercel (engineering + AI-applied) | 127 | vercel.com/atom, filtered to engineering tag + AI regex (excludes changelog) |
| Anthropic (research + engineering) | 125 | anthropic.com sitemap, all `/research/*` and `/engineering/*` |
| Databricks Mosaic AI | 79 | en-blog-assets sitemap + blog-legacy-assets, filtered to Mosaic Research authors + AI research category (includes ~30 pre-acquisition MosaicML posts recovered via Wayback) |
| Cursor | 15 | cursor.com/blog `/topic/research` + technical-substance posts from the main blog |
| Cognition | 11 | cognition.ai/rss.xml, filtered to research + engineering methodology posts |
| Thinking Machines | 4 | thinkingmachines.ai/index.xml (all Connectionism research) |
| **Total** | **548** | |

Substance filter: dropped pure launches, customer stories, and company news (e.g., "Introducing X", "now available", "partnership with"), but **kept** technical launches with methodology detail (DBRX technical post, Claude system cards, GPT-5 research report).

---

## Categorization axes

Each post is tagged on five axes; you can pivot the Sheet or cd into `by-<axis>/` to slice.

- **Axis A — Contribution type** (1-of): new-method, empirical-study, dataset-benchmark, retrospective-case-study, infra-release, interpretability-finding, position-policy
- **Axis B — Technical domain** (1-of): pretraining, post-training, inference, agents, interpretability, safety-alignment, multimodal, evals-benchmarks, training-infra, serving-infra, applied-product
- **Axis C — Track**: research / engineering / applied
- **Axis D — Year**: publish year
- **Axis E — Techniques** (multi): SAE, MoE, speculative-decoding, RLHF, RLVR, DPO, constitutional-AI, long-context, Flash-Attention, KV-cache, quantization, distillation, tool-use, computer-use, coding-agents, prompt-caching, context-engineering, test-time-compute, reward-modeling, red-teaming, jailbreak, steering, probing, scaling-laws, retrieval-augmentation, MCP, and specific benchmarks (SWE-bench, Tau-Bench, BrowseComp, etc.)

---

## The temporal arc (what each year cared about)

- **2020–2022** (mostly Anthropic foundational, early Mosaic infra): scaling laws, constitutional methods, early interpretability, distributed training ergonomics.
- **2023**: Pretraining-at-scale public narratives — MPT, DBRX precursors, Composer, StreamingDataset. RLHF ubiquitous. First interpretability circuits (Anthropic). GPT-4 system card as a new genre.
- **2024**: Agents become real (tool-use, Claude artifacts, Devin, Cursor). Long-context (100k+). First production coding agents. SAE interpretability gains traction. Mosaic DBRX technical report.
- **2025**: Reasoning + test-time compute (o1 family). Computer use. Research on agent scaffolding vs. model capability. RLVR (verifiable rewards) overtakes RLHF in ambition. Interpretability moves from circuits → features → steering. Thinking Machines publishes "Connectionism" research.
- **2026** (YTD): Multi-agent systems shipping to prod. Agent harnesses as a discipline (Anthropic "Harness design", OpenAI "Harness engineering"). Eval awareness / sandbagging. RL over CUDA kernels (Cursor, Cognition Kevin-32B). Memory for agents. MCP everywhere.

---

## Cross-company themes (what each company says)

### Agents (~38 posts)
- **Anthropic** frames agents around harnesses, context engineering, skills, and long-running loops. Concrete engineering emphasis — how to build production agents that don't fall over (context engineering, multi-agent research system, Claude Code sandboxing, harness design for long-running apps).
- **OpenAI** talks about agents through the lens of Codex/Sora/ChatGPT Atlas — product-framed engineering (harness engineering, OWL architecture for Atlas browser, Beyond Rate Limits scaling).
- **Cursor** publishes the most mechanically-specific agent research: multi-agent kernel RL, warp decode for MoE inference, fast regex indexing for agent tools, real-time RL for Composer, agent sandboxing, self-driving codebases.
- **Cognition** publishes the **opinionated** takes: "Don't Build Multi-Agents" (2025-06), "Coding Agents 101", Agent Trace. Distinctly against the grain on some specific architectural choices.
- **Databricks Mosaic** focuses on enterprise agents: Agentic Reasoning in Practice, Memory Scaling for AI Agents, Meet KARL (enterprise knowledge agent with custom RL), Governing Coding Agent Sprawl.
- **Thinking Machines**: no dedicated agent posts yet (scope is closer to model mechanics).

### Evals and benchmarks (~17 posts)
- **Anthropic**: Demystifying evals for AI agents, AI-resistant technical evaluations, Infrastructure noise in agentic coding evals, Eval awareness in BrowseComp.
- **OpenAI**: A large number of system cards and benchmark-report posts (GPT-5.x system cards, EVMbench, Advancing independent research on AI alignment).
- **Cursor**: Cursorbench — hybrid online/offline eval for coding agents.
- **Cognition**: SWE-bench technical report, SWE-Check, evaluating coding agents (review of o1).
- **Databricks**: OfficeQA enterprise benchmark.

### Inference (~11 posts)
- **Thinking Machines**: Defeating Nondeterminism in LLM Inference — surprising technical depth from a tiny team.
- **Databricks Mosaic**: Serving Quantized LLMs on H100, LLM Inference Performance Engineering, TensorRT-LLM integration, Fast PEFT Serving.
- **Cursor**: Warp decode for MoE inference.
- **OpenAI**: Beyond rate limits, From model to agent (Responses API).

### Interpretability (~13 posts)
- Almost entirely **Anthropic** — Circuits Updates series (monthly Sep 2024 onward), Towards Monosemanticity, SAEs, dictionary learning, steering, feature viz. This is the only company publishing mechanistic interpretability at scale.
- No other company in the corpus has dedicated interpretability posts. Divergence point.

### Pretraining / architecture (~24 posts)
- **Databricks Mosaic** owns this narrative — MPT (7B, 30B, long-context), DBRX, Composer, LLM Foundry, MegaBlocks, FP8 training, AMD MI250 benchmarks, Intel Gaudi 2.
- **Cursor**: Composer 2 technical report, Training Composer for longer horizons, Better MoE inference with warp decode.
- **Anthropic / OpenAI** don't publish pretraining details in detail (proprietary stance).

### Post-training / RL (~3 posts tagged, but much more distributed)
- **Thinking Machines**: On-Policy Distillation, LoRA Without Regret.
- **Cognition**: Kevin-32B (multi-turn RL for CUDA kernels).
- **OpenAI** and **Anthropic**: RLHF discussions often embedded in system cards or broader research posts, not isolated.

---

## Divergences (where companies publicly disagree)

1. **Multi-agent orchestration.** Anthropic published "How we built our multi-agent research system" (2025-06-13) championing the approach. Cognition published "Don't Build Multi-Agents" (2025-06-12) — literally the next day — arguing against it. A rare public disagreement on an architectural question.

2. **Benchmark trustworthiness.** Anthropic's "Eval awareness in Claude Opus 4.6's BrowseComp performance" (2026-03-06) and "Infrastructure noise in agentic coding evals" (2026-02-03) both publicly question whether benchmark scores reflect capability. OpenAI's system-card approach implicitly trusts the benchmarks.

3. **Agent harness vs. model capability.** Cursor's research agenda ("Better models, ambitious work") treats harness and model as jointly trainable (real-time RL for Composer). Anthropic's engineering ("Effective harnesses for long-running agents") treats them as decoupled concerns.

4. **Pretraining transparency.** Databricks Mosaic publishes full technical reports with hyperparameters, loss curves, and architecture details. OpenAI and Anthropic publish system cards with capability evals but no training details. Thinking Machines sits in the middle (Connectionism publishes mechanics but not full recipes).

---

## Standout posts (must-read shortlist, ~30)

Curated by reading titles + applying heuristic rules; will refine during summarization pass. In no particular order:

**Interpretability**
- Anthropic — Towards Monosemanticity
- Anthropic — Circuits Updates (Sep/Oct 2024 onward, monthly cadence)
- Anthropic — Steering Claude

**Pretraining / architecture**
- Databricks — DBRX technical report (full architecture + training disclosure)
- Databricks — MPT-30B, MPT-7B-8k (long-context MPT)
- Databricks — Turbocharged Training with FP8
- Databricks — MegaBlocks on Databricks (MoE kernels)
- Cursor — Composer 2 technical report
- Cursor — Better MoE inference with warp decode

**Post-training / RL / distillation**
- Thinking Machines — On-Policy Distillation
- Thinking Machines — LoRA Without Regret
- Cognition — Kevin-32B: Multi-Turn RL for CUDA Kernels
- Cursor — Improving Composer through real-time RL

**Inference mechanics**
- Thinking Machines — Defeating Nondeterminism in LLM Inference
- Databricks — LLM Inference Performance Engineering: Best Practices
- OpenAI — Harness engineering: leveraging Codex in an agent-first world

**Agent harness / context engineering**
- Anthropic — Effective context engineering for AI agents
- Anthropic — Harness design for long-running application development
- Anthropic — Effective harnesses for long-running agents
- Anthropic — Writing effective tools for AI agents—using AI agents
- OpenAI — Unlocking the Codex harness: how we built the App Server
- OpenAI — How we built OWL, the new architecture behind ChatGPT-based browser Atlas
- Cursor — Implementing a secure sandbox for local agents
- Cursor — Fast regex search: indexing text for agent tools

**Multi-agent + eval-critical**
- Anthropic — How we built our multi-agent research system
- Cognition — Don't Build Multi-Agents (counter-take)
- Anthropic — Eval awareness in Claude Opus 4.6's BrowseComp performance
- Anthropic — Quantifying infrastructure noise in agentic coding evals
- Cognition — SWE-bench technical report

**Safety / alignment**
- Anthropic — Alignment faking series
- Anthropic — Responsible Scaling Policy (and updates)
- Anthropic — Sleeper Agents

---

## Gaps — what nobody writes about

Across all 548 posts, these topics are conspicuously absent or thin:

- **Inference cost economics in production.** Almost nobody publishes actual dollar-cost breakdowns of serving LLMs at real scale.
- **Bad post-training experiments that failed.** Almost all posts are success stories. Negative results (what didn't work) are rare.
- **Honest retrospectives on deprecated techniques.** Nobody's written "We tried X, then dropped it because Y."
- **Data cleaning pipelines.** A lot of posts on training, very few on the actual data prep (deduping, filtering, PII removal).
- **On-device / small-model work.** The corpus skews heavily toward frontier/cloud. Almost no small-model work.
- **Evaluation reproducibility.** Posts discuss their evals but rarely the reproducibility checks.

---

## How to iterate

This is a source-of-truth Sheet + regenerable Markdown setup:

- **Add a source:** drop rows into the Sheet, re-run `_data/generate_markdown.py` to regenerate all cross-ref files. No re-crawl of existing data.
- **Re-categorize:** edit `contribution_type`, `technical_domain`, or `techniques` columns in the Sheet; re-run the generator; markdown updates.
- **Rewrite a summary:** edit the entry in `by-company/*.md` (canonical); cross-refs still resolve via the ID anchor.
- **New axis:** add a column to the Sheet; add a `by-{axis}/` folder; extend the generator to emit it.
- **Refresh cadence:** weekly cron that polls each source's RSS/sitemap, diffs against the Sheet, summarizes and categorizes new posts only.

---

## Current completion state

- [x] Corpus enumeration (1054 total, 548 in-scope)
- [x] Phase 2 substance filter (dropped ~500 pure launches / customer / company-news)
- [x] Heuristic first-pass categorization on all 5 axes
- [x] Google Sheet populated with all rows
- [x] Company markdown files (title, URL, date, authors, heuristic tags)
- [x] Cross-reference files (by domain / type / year / technique)
- [x] This synthesis doc
- [ ] **3-5 bullet per-post summaries** (pending — summarization pass needs to fetch and read each post's content)
- [ ] Refined category tags (heuristic → content-aware)

---

*Generated 2026-04-19. To refresh, re-run the scripts in `_data/`.*
