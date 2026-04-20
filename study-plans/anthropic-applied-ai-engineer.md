# Anthropic Applied AI Engineer — study plan

A focused reading list for Applied AI Engineer interview prep at Anthropic. Ranked by relevance to the role (agent engineering / harness / context engineering / evals / deploying Claude for customers). Built from the full corpus (`../by-focus-area/`).

**Total scope:** ~30 hours of reading. Covers Anthropic's worldview plus the competitive landscape (OpenAI, Cursor, Cognition, LangChain, Databricks).

**Crash path (6-8 hrs):** jump to [Crash path](#crash-path-6-8-hrs) at the bottom.

---

## Tier 1 — Must read first (their daily work)

### Anthropic harness & agent engineering

| Priority | Title | Why |
|---|---|---|
| 9.9 | [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | Production multi-agent architecture |
| 8.9 | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | The context-engineering manifesto |
| 8.9 | [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) | Production agent harness patterns |
| 8.9 | [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Patterns for persistent agents |
| 8.9 | [Writing effective tools for AI agents—using AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Tool design guide |
| 8.9 | [Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents) | Core patterns — orchestration, parallel, routing |
| 8.9 | [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Skills framework |
| 8.9 | [Code execution with MCP: building more efficient AI agents](https://www.anthropic.com/engineering/code-execution-with-mcp) | MCP internals |
| 8.9 | [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents) | Brain/hands architecture |
| 8.9 | [Claude Code auto mode: a safer way to skip permissions](https://www.anthropic.com/engineering/claude-code-auto-mode) | Permission design for autonomous agents |
| 8.9 | [Making Claude Code more secure and autonomous with sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing) | Sandboxing strategy |
| 8.9 | [Contextual Retrieval in AI Systems](https://www.anthropic.com/research/contextual-retrieval) | Anthropic's RAG approach |
| 8.9 | [The "think" tool: Enabling Claude to stop and think](https://www.anthropic.com/engineering/claude-think-tool) | Scratchpad patterns |

### Anthropic's eval discipline

| Priority | Title | Why |
|---|---|---|
| 9.9 | [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/engineering/infrastructure-noise) | Depth on eval methodology |
| 8.9 | [Eval awareness in Claude Opus 4.6's BrowseComp performance](https://www.anthropic.com/engineering/eval-awareness-browsecomp) | How benchmarks can be gamed |
| 8.9 | [Designing AI resistant technical evaluations](https://www.anthropic.com/engineering/AI-resistant-technical-evaluations) | Eval design principles |
| 8.9 | [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Agent eval primer |

---

## Tier 2 — Anthropic's worldview & culture

### Alignment / character (Anthropic DNA)

| Priority | Title | Why |
|---|---|---|
| 9.9 | [Persona vectors: Monitoring and controlling character traits in language models](https://www.anthropic.com/research/persona-vectors) | Character-trait monitoring at scale |
| 9.9 | [Simple probes can catch sleeper agents](https://www.anthropic.com/research/probes-catch-sleeper-agents) | Alignment probing |
| 8.9 | [Alignment faking in large language models](https://www.anthropic.com/research/alignment-faking) | The canonical deceptive-alignment paper |
| 8.9 | [Constitutional AI: Harmlessness from AI Feedback](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) | Foundational Anthropic method |
| 8.9 | [Collective Constitutional AI: Aligning a Language Model with Public Input](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input) | Constitutional evolution |
| 8.9 | [Towards Understanding Sycophancy in Language Models](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models) | Core Anthropic concern |
| — | [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) | Safety framework |
| — | [Claude's Character](https://www.anthropic.com/research/claude-character) | How they think about Claude's personality |

### Interpretability sampler (shows research breadth)

| Title | Why |
|---|---|
| [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model) | The "AI microscope" — flagship interp |
| [Using dictionary learning features as classifiers](https://www.anthropic.com/research/features-as-classifiers) | Applied interp |
| [The engineering challenges of scaling interpretability](https://www.anthropic.com/research/engineering-challenges-interpretability) | What the interp team actually does |
| [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning) | The SAE paper |

---

## Tier 3 — Competitive landscape (interview edge)

### What other labs build (you'll compete / integrate with these)

| Company | Post | Why |
|---|---|---|
| **Cognition** | [Don't Build Multi-Agents](https://cognition.ai/blog/dont-build-multi-agents) | The contrarian view to Anthropic — published one day after Anthropic's multi-agent post |
| **Cognition** | [Agent Trace: Capturing the Context Graph of Code](https://cognition.ai/blog/agent-trace) | Agent observability |
| **Cognition** | [SWE-bench technical report](https://cognition.ai/blog/swe-bench-technical-report) | The coding-agent benchmark of record |
| **OpenAI** | [Unlocking the Codex harness: how we built the App Server](https://openai.com/index/unlocking-the-codex-harness/) | Direct Codex/Claude Code comparison |
| **OpenAI** | [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/) | OpenAI's harness POV |
| **OpenAI** | [How we built OWL, the new architecture behind ChatGPT-based browser Atlas](https://openai.com/index/building-chatgpt-atlas/) | Computer-use production architecture |
| **Cursor** | [A technical report on Composer 2](https://cursor.com/blog/composer-2-technical-report) | How Cursor trains their coding model |
| **Cursor** | [Implementing a secure sandbox for local agents](https://cursor.com/blog/agent-sandboxing) | Coding-agent sandbox design |
| **Cursor** | [Fast regex search: indexing text for agent tools](https://cursor.com/blog/fast-regex-search) | Tool design for speed |
| **LangChain** | [Improving deep agents with harness engineering](https://blog.langchain.com/improving-deep-agents-with-harness-engineering) | H/H/H — Top-5 Terminal Bench 2.0 via harness only |
| **Databricks** | [PGRM: Promptable Reward Model](https://www.databricks.com/blog/judging-confidence-meet-pgrm-promptable-reward-model) | Custom judges for agent eval |

---

## Tier 4 — Technique depth (know the field)

### Evals you'll likely encounter

| Source | Post | Relevance |
|---|---|---|
| OpenAI | [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://openai.com/index/mle-bench/) | ML engineering agent benchmark |
| OpenAI | [Why SWE-bench Verified no longer measures frontier coding capabilities](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) | Eval-methodology critique |

### Agent design debates

| Source | Post | Relevance |
|---|---|---|
| Anthropic | [A postmortem of three recent issues](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues) | Incident engineering — what went wrong |
| Anthropic | [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler) | Multi-agent in practice |

### Fine-tuning & post-training (know the stack)

| Source | Post | Relevance |
|---|---|---|
| Thinking Machines | [On-Policy Distillation](https://thinkingmachines.ai/blog/on-policy-distillation/) | Modern post-training |
| Thinking Machines | [LoRA Without Regret](https://thinkingmachines.ai/blog/lora/) | Efficient fine-tuning |
| Databricks | [The Power of RLVR: Training a Leading SQL Reasoning Model](https://www.databricks.com/blog/power-rlvr-training-leading-sql-reasoning-model-databricks) | Applied RLVR |
| Databricks | [TAO: Using test-time compute to train efficient LLMs without labeled data](https://www.databricks.com/blog/tao-using-test-time-compute-train-efficient-llms-without-labeled-data) | Novel training approach |

---

## Interview signal tips (from corpus patterns)

1. **Have a strong opinion on multi-agent vs. single-agent.** Anthropic's "How we built our multi-agent research system" (for) vs. Cognition's "Don't Build Multi-Agents" (against) — published one day apart in June 2025. Pick a side and defend it.

2. **Know the context engineering canon.** Anthropic's "Effective context engineering for AI agents" is the doc. Be able to discuss: memory, compaction, retrieval-augmented context, notepads, sub-agents as context managers.

3. **Know what an eval should and shouldn't measure.** "Infrastructure noise in agentic coding evals" and "Eval awareness in BrowseComp" signal Anthropic's eval discipline — they publicly doubt their own benchmarks. If you say "we measured SWE-bench and got 80%" without caveats, you'll sound naive.

4. **Understand MCP fluently.** 17+ posts in the corpus use MCP. Know the protocol, why it exists, how it relates to tool use, agent skills, and code execution.

5. **Be fluent in one alignment concept.** Persona vectors, alignment faking, or sleeper agents — pick one and have a 3-minute take. Shows you understand Anthropic's mission.

6. **Have a take on "harness vs. model capability."** Cursor's real-time RL for Composer treats them as jointly optimizable; Anthropic's "Effective harnesses for long-running agents" treats them as decoupled. Where do you stand?

---

## Crash path (6-8 hrs)

Read these 12 Anthropic posts in order — covers 80% of what matters for the role:

1. [Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents)
2. [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
3. [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
4. [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
5. [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
6. [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
7. [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
8. [Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode)
9. [Making Claude Code more secure and autonomous with sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing)
10. [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
11. [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/engineering/infrastructure-noise)
12. [Constitutional AI: Harmlessness from AI Feedback](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)

Then read **Cognition's [Don't Build Multi-Agents](https://cognition.ai/blog/dont-build-multi-agents)** as the contrarian take. That's enough to hold your own in the interview.

---

## One-click access in the corpus

Filter the [Google Sheet](https://docs.google.com/spreadsheets/d/1td1T6wCEnw4EeG05I_hH1dK1aNkLR5HJZZ-4jr-Du9A/edit) with:

```
company = anthropic
  AND focus_area IN (harness-and-context-engineering, agentic-systems, evals-and-benchmarks)
  AND signal_overall = H
```

Gives you the exact working set for this plan.

Browse directly: [`../by-company/anthropic.md`](../by-company/anthropic.md) · [`../by-focus-area/harness-and-context-engineering.md`](../by-focus-area/harness-and-context-engineering.md) · [`../by-focus-area/agentic-systems.md`](../by-focus-area/agentic-systems.md)
