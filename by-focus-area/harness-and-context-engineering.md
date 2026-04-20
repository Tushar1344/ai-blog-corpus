# Harness & Context Engineering

Agent scaffolding, context engineering, long-running harnesses, prompt caching strategy, agent skills, MCP integrations.

**Post count:** 314

**Contributors:**

- LangChain: 238
- Vercel: 22
- Databricks Mosaic AI: 21
- Anthropic: 11
- Hugging Face: 9
- OpenAI: 5
- Cursor: 4
- Cognition: 2
- Mistral AI: 1
- AI21 Labs: 1

**Subcategories:**

- [MCP & tool protocols](#mcp-and-tool-protocols) (20)
- [Product engineering case studies (Codex, Sora, Atlas)](#codex-and-sora-harness) (5)
- [Long-running harnesses](#long-running-harnesses) (6)
- [Context engineering](#context-engineering) (22)
- [Scaffolding patterns](#scaffolding-patterns) (1)
- [Agent skills & prompt libraries](#agent-skills-and-prompt-libraries) (1)
- [AI SDK & product tooling (Vercel v0, AI SDK)](#ai-sdk-and-product-tooling) (23)
- [Workflow agents (data analyst, code review, Bugbot)](#data-analyst-and-workflow-agents) (4)
- [Databricks training stack (misplaced; should be pretraining/training-stack)](#databricks-training-stack-misc) (12)
- [Other harness & context engineering](#fallback-harness) (219)

---

## <a id="mcp-and-tool-protocols"></a>MCP & tool protocols

_20 posts_

### Code execution with MCP: building more efficient AI agents

- **ID:** `ant-e-code-execution-with-mcp`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/code-execution-with-mcp
- **Date:** 2025-11-04
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)
- **Techniques:** tool-use, MCP

_Summary pending — see link for details._


### Addressing security and quality issues with MCP tools in AI Agent

- **ID:** `vcl-a-generate-static-ai-sdk-tools-from-mcp-servers-with-mcp-to-ai-sdk`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/generate-static-ai-sdk-tools-from-mcp-servers-with-mcp-to-ai-sdk
- **Date:** 2025-09-17
- **Authors:** Malte Ubl|Andrew Qu
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** M — L=M/N=L/A=H (priority 6.4)
- **Techniques:** tool-use, MCP

_Summary pending — see link for details._


### The second wave of MCP: Building for LLMs, not developers

- **ID:** `vcl-e-the-second-wave-of-mcp-building-for-llms-not-developers`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/the-second-wave-of-mcp-building-for-llms-not-developers
- **Date:** 2025-09-09
- **Authors:** Andrew Qu
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=H (priority 6.4)
- **Techniques:** tool-use, MCP

_Summary pending — see link for details._


### Generate Images with Claude and Hugging Face

- **ID:** `hf-r-claude-and-mcp`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/claude-and-mcp
- **Date:** 2025-08-19
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

**Summary:**

- HF shows how to generate images with Claude via HF's MCP server by enabling FLUX.1-Krea-dev or Qwen-Image as Space Tools in hf.co/mcp settings
- Advantages: Claude helps craft prompts, sees outputs to iterate, and you can swap models easily
- Practical: add Spaces via huggingface.co/mcp/settings
- Claude Desktop requires custom connector URL after Anthropic policy update
- Krea targets natural photographic realism (no AI plastic look)
- Qwen-Image excels at accurate text rendering for posters/signs/infographics


### MCP for Research: How to Connect AI to Research Tools

- **ID:** `hf-r-mcp-for-research`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/mcp-for-research
- **Date:** 2025-08-18
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

**Summary:**

- Conceptual post on using MCP for academic research discovery (arXiv, GitHub, HF) via natural-language commands across three abstraction layers: manual, scripted, MCP
- Shows a Research Tracker MCP that finds papers, implementations, and related models/datasets in one agent call
- Takeaway: Software 3.0 analogy—natural language is the new programming language, but still error-prone without human oversight
- Setup via huggingface.co/settings/mcp by adding `research-tracker-mcp` and following client-specific config
- Light on code details, mostly conceptual framing


### Implementing MCP Servers in Python: An AI Shopping Assistant with Gradio

- **ID:** `hf-r-gradio-vton-mcp`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/gradio-vton-mcp
- **Date:** 2025-07-31
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

**Summary:**

- Tutorial building an AI shopping assistant that combines Gradio MCP server + IDM-VTON virtual try-on diffusion model + Playwright MCP + VS Code chat
- Shows how `mcp_server=True` in gr.Interface.launch() auto-converts Python functions to MCP tools with docstring-generated schemas
- Assistant browses stores with Playwright and calls vton_generation to show how clothes look on the user
- Practical value: concrete end-to-end integration with code for adding AI features to existing Gradio apps
- Requires Node.js for Playwright MCP server


### Model Context Protocol (MCP) explained: An FAQ

- **ID:** `vcl-e-model-context-protocol-mcp-explained`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/model-context-protocol-mcp-explained
- **Date:** 2025-07-25
- **Authors:** Dan Fein|Andrew Qu
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=H (priority 6.4)
- **Techniques:** tool-use, MCP

_Summary pending — see link for details._


### Grep a million GitHub repositories via MCP

- **ID:** `vcl-e-grep-a-million-github-repositories-via-mcp`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/grep-a-million-github-repositories-via-mcp
- **Date:** 2025-07-17
- **Authors:** Dan Fox|Andrew Qu
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=H (priority 6.4)
- **Techniques:** tool-use, MCP

_Summary pending — see link for details._


### Five Big Improvements to Gradio MCP Servers

- **ID:** `hf-r-gradio-mcp-updates`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/gradio-mcp-updates
- **Date:** 2025-07-17
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- Gradio 5.38.0 adds five MCP server improvements: seamless local file upload MCP server, real-time progress notifications, gr.load_openapi for OpenAPI→MCP in one line, gr.Header typed args for auth, and custom api_description
- File Upload server solves remote Gradio servers needing public URLs for file inputs
- OpenAPI→MCP means existing REST backends become LLM-accessible with minimal code
- gr.Header auto-extracts headers and surfaces them in connection docs
- Progress notifications stream status to MCP clients for long-running tasks


### Building the Hugging Face MCP Server

- **ID:** `hf-r-building-hf-mcp`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/building-hf-mcp
- **Date:** 2025-07-10
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- HF details architecture choices building hf.co/mcp MCP Server: picked Streamable HTTP (stateless, direct response) over deprecated SSE for simple scaling
- Walks through 3 MCP communication patterns (direct response, request-scoped streams, server push streams) and tradeoffs
- Practical for MCP server builders: stateless direct-response is lowest-overhead when you don't need sampling/elicitation
- Observability dashboard shows client connection behaviors
- MCP has had 3 protocol revisions in 9 months creating client-compat challenges
- Supports dynamic per-user tools and thousands of Gradio-backed Spaces


### Upskill your LLMs With Gradio MCP Servers

- **ID:** `hf-r-gradio-mcp-servers`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/gradio-mcp-servers
- **Date:** 2025-07-09
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

**Summary:**

- HF pitches HF Spaces as the ''MCP App Store''—thousands of Gradio-powered AI apps are now MCP-compatible and installable into any LLM client
- Walkthrough: enable Flux.1-Kontext-Dev in HF MCP settings, then configure Cursor to use it for image editing via natural-language prompts
- Takeaway: MCP + Spaces lets any LLM gain specialized abilities (image edit, OCR, TTS) without building integrations
- Filter for MCP-compatible Spaces on HF
- Pro account needed to duplicate ZeroGPU Spaces for private use


### Claude Desktop Extensions: One-click MCP server installation for Claude Desktop

- **ID:** `ant-e-desktop-extensions`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/desktop-extensions
- **Date:** 2025-06-26
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)
- **Techniques:** tool-use, MCP

_Summary pending — see link for details._


### Building efficient MCP servers

- **ID:** `vcl-e-building-efficient-mcp-servers`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/building-efficient-mcp-servers
- **Date:** 2025-06-12
- **Authors:** Andrew Qu
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=H (priority 6.4)
- **Techniques:** tool-use, MCP

_Summary pending — see link for details._


### Tiny Agents in Python: a MCP-powered agent in ~70 lines of code

- **ID:** `hf-r-python-tiny-agents`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/python-tiny-agents
- **Date:** 2025-05-23
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- HF ports Tiny Agents to Python in ~70 lines: extends huggingface_hub with an MCPClient so huggingface_hub acts as MCP client feeding tools to LLMs during chat completions
- Core insight: an agent is just a while loop on top of an MCP Client
- CLI `tiny-agents run` loads agent.json configs from HF Dataset or local path, connects to multiple MCP servers (filesystem, Playwright, Gradio Spaces) simultaneously
- Default config uses Qwen2.5-72B via Nebius provider
- Now supports AGENTS.md standard
- Full MCPClient adds/runs tools via OpenAI-compatible tool-calling interface


### How Vapi built their MCP server on Vercel

- **ID:** `vcl-e-vapi-mcp-server-on-vercel`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/vapi-mcp-server-on-vercel
- **Date:** 2025-05-21
- **Authors:** Elizabeth Trykin|Andrew Qu
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=H (priority 6.4)
- **Techniques:** tool-use, MCP

_Summary pending — see link for details._


### How to Build an MCP Server with Gradio

- **ID:** `hf-r-gradio-mcp`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/gradio-mcp
- **Date:** 2025-04-30
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- Gradio makes building an MCP server 5 lines: set mcp_server=True in gr.Interface.launch() and any Python function becomes an LLM-callable tool
- Docstring generates the tool description, endpoints appear at /gradio_api/mcp/sse
- Also covers Resources, Prompts (gr.mcp.resource, gr.mcp.prompt decorators), MCP-only functions via gr.api(), auto file upload, performance analytics, and free hosting on HF Spaces
- For Claude Desktop use mcp-remote as a shim since it doesn't support SSE directly
- Concrete toy example: letter-counting tool to help LLMs count 'r's in 'strawberry'


### Tiny Agents: an MCP-powered agent in 50 lines of code

- **ID:** `hf-r-tiny-agents`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/tiny-agents
- **Date:** 2025-04-25
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- Original JS Tiny Agents: MCP-powered agent in 50 lines of TypeScript on top of @huggingface/inference, running via `npx @huggingface/mcp-client`
- Key insight: once you have an MCP Client, an Agent is just a while loop on top of it
- Default model Qwen2.5-72B on Nebius
- Connects to local filesystem and Playwright MCP servers by default and passes tools via OpenAI-compatible tool_choice:auto chat completions
- Shows haiku-writing and web-search demos
- Uses async generators for streaming LLM output


### MCP: Flash in the Pan or Future Standard?

- **ID:** `lc-r-mcp-fad-or-fixture`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/mcp-fad-or-fixture
- **Date:** 2025-03-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Le Chat Mcp Connectors Memories

- **ID:** `mt-r-le-chat-mcp-connectors-memories`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/le-chat-mcp-connectors-memories/
- **Date:** _date unknown_
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Stateful Agent Workspaces Mcp

- **ID:** `a21-r-stateful-agent-workspaces-mcp`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/stateful-agent-workspaces-mcp/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


## <a id="codex-and-sora-harness"></a>Product engineering case studies (Codex, Sora, Atlas)

_5 posts_

### Scaling PostgreSQL to power 800 million ChatGPT users

- **ID:** `oai-e-scaling-postgresql`
- **Company:** OpenAI
- **Link:** https://openai.com/index/scaling-postgresql/
- **Date:** 2026-03-11
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Building a C compiler with a team of parallel Claudes

- **ID:** `ant-e-building-c-compiler`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/building-c-compiler
- **Date:** 2026-02-05
- **Authors:** Nicholas Carlini
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Unlocking the Codex harness: how we built the App Server

- **ID:** `oai-e-unlocking-the-codex-harness`
- **Company:** OpenAI
- **Link:** https://openai.com/index/unlocking-the-codex-harness/
- **Date:** 2026-01-29
- **Track:** engineering
- **Contribution type:** dataset-benchmark
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- OpenAI shares how they built the Codex App Server—a JSON-RPC protocol and long-lived process hosting Codex core threads—that powers CLI, VS Code, JetBrains, Xcode, macOS app, web all via the same agent harness
- Started as internal tool for IDE extension, evolved after MCP semantics proved awkward for VS Code
- Three core primitives: Item (atomic input/output with started/delta/completed lifecycle), Turn (one user-initiated unit of work), Thread (durable session container)
- Bidirectional: server can initiate requests (approvals) mid-turn
- Backward-compat designed so partner integrations can depend on it safely
- Architecture: stdio reader + message processor + thread manager + core threads


### How we used Codex to build Sora for Android in 28 days

- **ID:** `oai-e-shipping-sora-for-android-with-codex`
- **Company:** OpenAI
- **Link:** https://openai.com/index/shipping-sora-for-android-with-codex/
- **Date:** 2025-10-30
- **Track:** engineering
- **Contribution type:** retrospective-case-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### A postmortem of three recent issues

- **ID:** `ant-e-a-postmortem-of-three-recent-issues`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues
- **Date:** 2025-09-17
- **Authors:** Sam McAllister|Jonathan Gray|Kashyap Murali|Brennan Saeta|Oliver Rausch|Alex Palcuie
- **Track:** engineering
- **Contribution type:** retrospective-case-study
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- Anthropic postmortem on three independent infrastructure bugs that degraded Claude responses Aug-Sep 2025
- Root causes: context-window routing error, output corruption, and approximate top-k XLA:TPU miscompilation
- Explicitly states quality was never reduced for load/demand reasons—only bugs
- Details how detection was delayed because user feedback is noisy
- Excellent engineering case study on debugging production model-quality issues


## <a id="long-running-harnesses"></a>Long-running harnesses

_6 posts_

### Harness design for long-running application development

- **ID:** `ant-e-harness-design-long-running-apps`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/harness-design-long-running-apps
- **Date:** 2026-03-24
- **Authors:** Prithvi Rajasekaran
- **Track:** engineering
- **Contribution type:** dataset-benchmark
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- Anthropic's Prithvi Rajasekaran on harness design pushing frontend design and long-running autonomous coding
- GAN-inspired generator/evaluator agent structure with explicit criteria makes subjective design 'gradable'
- Full three-agent (planner/generator/evaluator) architecture with sprint contracts yields rich multi-hour full-stack apps
- Addresses 'context anxiety' (premature wrapping-up) via context resets or upgraded Opus 4.5
- Evaluator weighs design/originality over craft/functionality to escape AI-slop defaults
- Uses Playwright MCP for live-page inspection to catch real UI bugs that static screenshots miss


### Improving Deep Agents with harness engineering

- **ID:** `lc-r-improving-deep-agents-with-harness-engineering`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
- **Date:** 2026-02-17
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=H/A=H (priority 9.9)

**Summary:**

- LangChain's deepagents-cli jumped from Top 30 to Top 5 on Terminal Bench 2.0 (52.8→66.5) by only changing the harness (system prompt, tools, middleware) with gpt-5.2-codex fixed
- Key tactics: PreCompletionChecklistMiddleware forces verification before exit (Ralph Wiggum loop), LocalContextMiddleware injects cwd map at start, LoopDetectionMiddleware breaks doom loops after N edits, reasoning-mode budget tuning (low/med/high/xhigh)
- Process: Trace Analyzer Skill fetches LangSmith traces, spawns parallel error-analysis agents, synthesizes harness changes
- Testing emphasis and test writing are key hill-climbing signals for autonomous coding


### Expanding our long-running agents research preview

- **ID:** `cur-e-long-running-agents`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/long-running-agents
- **Date:** 2026-02-12
- **Authors:** Cursor Team
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=H (priority 8.7)
- **Techniques:** coding-agents

**Summary:**

- Cursor expands long-running agents research preview to all Ultra/Teams/Enterprise users at cursor.com/agents
- Custom harness tackles frontier-model failures on long-horizon tasks seen in their web-browser experiment
- Example runs: 36-hour new chat platform build, 30-hour mobile port, 25-hour auth/RBAC refactor
- Principles include planning before execution and model-specific scaffolding
- Matters as productionization of long-horizon agent harness with PR-merge-rate parity to shorter agents


### Harness engineering: leveraging Codex in an agent-first world

- **ID:** `oai-e-harness-engineering`
- **Company:** OpenAI
- **Link:** https://openai.com/index/harness-engineering/
- **Date:** 2026-02-04
- **Track:** engineering
- **Contribution type:** dataset-benchmark
- **Signal:** H — L=H/N=H/A=M (priority 8.9)

**Summary:**

- OpenAI's 5-month experiment: shipped ~1M-line internal product with zero human-written code using Codex agents (3→7 engineers, 1,500 PRs, 3.5 PRs/engineer/day)
- Core insight: engineer's job becomes designing environments, specifications, and feedback loops—not coding
- Agent-legibility principles: repository as system of record (structured docs/, short AGENTS.md as TOC), enforced architectural layers via custom linters, Chrome DevTools/observability exposed to agents
- Minimal blocking merge gates, ~6-hour autonomous Codex runs via Ralph-Wiggum self-review loops
- Humans provide taste and steer, agents execute at 10x velocity


### Effective harnesses for long-running agents

- **ID:** `ant-e-effective-harnesses-for-long-running-agents`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **Date:** 2025-11-26
- **Authors:** Justin Young
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### OpenRecovery: Transforming addiction recovery with LangGraph Platform

- **ID:** `lc-r-customers-openrecovery`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-openrecovery
- **Date:** 2024-10-03
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


## <a id="context-engineering"></a>Context engineering

_22 posts_

### How agents can use filesystems for context engineering

- **ID:** `lc-r-how-agents-can-use-filesystems-for-context-engineering`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-agents-can-use-filesystems-for-context-engineering
- **Date:** 2025-11-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- LangChain argues filesystems are a first-class context-engineering tool for deep agents: ls/glob/grep/read/edit/write tools let agents store unlimited context and retrieve only what's needed
- Solves 4 context failure modes: too many tokens (offload tool results to files), needs large context (plans/sub-agent knowledge persisted to disk), niche info lookup (grep beats semantic search on structured data like code/APIs), and learning over time (user clues saved as files)
- Claude Code heavily uses glob/grep
- Modern LLMs are trained to traverse filesystems
- Manus referenced as early public example


### Effective context engineering for AI agents

- **ID:** `ant-e-effective-context-engineering-for-ai-agents`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Date:** 2025-09-29
- **Authors:** Prithvi Rajasekaran|Ethan Dixon|Carly Ryan|Jeremy Hadfield|Hannah Moran|Cal Rueb|Connor Jennings
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=H/A=M (priority 8.9)
- **Techniques:** context-engineering

**Summary:**

- Anthropic reframes prompt engineering as 'context engineering'—curating the minimal high-signal token set for LLM agents
- Claims context rot (attention budget decay with length) requires treating context as finite
- Recommends 'just-in-time' retrieval via lightweight identifiers and tool-driven exploration over pre-computed RAG
- For long-horizon tasks uses compaction, structured note-taking, multi-agent architectures
- Advocates clear altitude in system prompts, minimal tool sets, and canonical few-shot examples over exhaustive edge-case lists


### Context Engineering

- **ID:** `lc-r-context-engineering-for-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/context-engineering-for-agents
- **Date:** 2025-07-02
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- LangChain's framework for context engineering: four strategies—write, select, compress, isolate—for managing the LLM context window (like OS-managed RAM per Karpathy)
- Covers scratchpads, short/long-term memories (episodic/procedural/semantic), tool-RAG (3x improvement in selection), code-agent RAG (Cursor/Windsurf challenges)
- Takeaway for agent builders: context engineering is #1 skill because long-running agents suffer context poisoning/distraction/confusion/clash
- LangGraph designed to enable all four strategies
- Memory selection is challenging—ChatGPT leaking locations into images is a cautionary tale


### The rise of "context engineering"

- **ID:** `lc-r-the-rise-of-context-engineering`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/the-rise-of-context-engineering
- **Date:** 2025-06-23
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- Harrison Chase defines context engineering as ''building dynamic systems to provide the right information and tools in the right format such that the LLM can plausibly accomplish the task''
- Argues it's the most important AI engineering skill, subsuming prompt engineering
- Failure modes split into model-ability issues vs context-delivery issues—often the latter
- Examples: tool use (with digestible outputs), short/long-term memory, retrieval, instructions
- LangGraph is designed to enable full control over what goes into the LLM
- References 12-Factor Agents and ''Communication is all you need''


### Contextual Retrieval in AI Systems

- **ID:** `ant-e-contextual-retrieval`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/contextual-retrieval
- **Date:** 2024-09-19
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- Describes Contextual Retrieval: prepend per-chunk LLM-generated context before embedding and BM25 indexing
- Combined with reranking, cuts retrieval failure rate by 67% (49% without rerank)
- Practical RAG upgrade actionable via cookbook
- Notes prompt caching makes contextualization cheap
- For sub-200k-token corpora, simply stuff into prompt with caching
- Strong actionable RAG playbook.


### Graph-based metadata filtering for improving vector search in RAG applications

- **ID:** `lc-r-graph-based-metadata-filtering-for-improving-vector-search-in-rag-applications`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/graph-based-metadata-filtering-for-improving-vector-search-in-rag-applications
- **Date:** 2024-04-25
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### LangChain Integrates NVIDIA NIM for GPU-optimized LLM Inference in RAG

- **ID:** `lc-r-nvidia-nim`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/nvidia-nim
- **Date:** 2024-03-18
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Enhancing RAG-based application accuracy by constructing and leveraging knowledge graphs

- **ID:** `lc-r-enhancing-rag-based-applications-accuracy-by-constructing-and-leveraging-knowledge-graphs`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/enhancing-rag-based-applications-accuracy-by-constructing-and-leveraging-knowledge-graphs
- **Date:** 2024-03-15
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Build and deploy a RAG app with Pinecone Serverless

- **ID:** `lc-r-pinecone-serverless`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/pinecone-serverless
- **Date:** 2024-01-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Benchmarking RAG on tables

- **ID:** `lc-r-benchmarking-rag-on-tables`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/benchmarking-rag-on-tables
- **Date:** 2023-12-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Multi-modal RAG on slide decks

- **ID:** `lc-r-multi-modal-rag-template`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/multi-modal-rag-template
- **Date:** 2023-12-06
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Deconstructing RAG

- **ID:** `lc-r-deconstructing-rag`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/deconstructing-rag
- **Date:** 2023-11-30
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Applying OpenAI's RAG Strategies

- **ID:** `lc-r-applying-openai-rag`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/applying-openai-rag
- **Date:** 2023-11-17
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Implementing advanced RAG strategies with Neo4j

- **ID:** `lc-r-implementing-advanced-retrieval-rag-strategies-with-neo4j`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/implementing-advanced-retrieval-rag-strategies-with-neo4j
- **Date:** 2023-11-07
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Embeddings Drive the Quality of RAG: Voyage AI in Chat LangChain

- **ID:** `lc-r-voyage-embeddings-in-langchain-and-chat-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/voyage-embeddings-in-langchain-and-chat-langchain
- **Date:** 2023-11-02
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Multi-Vector Retriever for RAG on tables, text, and images

- **ID:** `lc-r-semi-structured-multi-modal-rag`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/semi-structured-multi-modal-rag
- **Date:** 2023-10-20
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### A Chunk by Any Other Name: Structured Text Splitting and Metadata-enhanced RAG

- **ID:** `lc-r-a-chunk-by-any-other-name`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/a-chunk-by-any-other-name
- **Date:** 2023-10-18
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Using a Knowledge Graph to implement a DevOps RAG application

- **ID:** `lc-r-using-a-knowledge-graph-to-implement-a-devops-rag-application`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/using-a-knowledge-graph-to-implement-a-devops-rag-application
- **Date:** 2023-10-04
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Kay x Cybersyn x LangChain: Embedding SEC Filings for RAG

- **ID:** `lc-r-kay-x-cybersyn-x-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/kay-x-cybersyn-x-langchain
- **Date:** 2023-10-03
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Epsilla x LangChain: Retrieval Augmented Generation (RAG) in LLM-Powered Question-Answering Pipelines

- **ID:** `lc-r-espilla-x-langchain-retrieval-augmented-generation-rag-in-llm-powered-question-answering-pipelines`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/espilla-x-langchain-retrieval-augmented-generation-rag-in-llm-powered-question-answering-pipelines
- **Date:** 2023-08-23
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Evaluating RAG pipelines with Ragas + LangSmith

- **ID:** `lc-r-evaluating-rag-pipelines-with-ragas-langsmith`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/evaluating-rag-pipelines-with-ragas-langsmith
- **Date:** 2023-08-23
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Auto-Evaluation of Anthropic 100k Context Window

- **ID:** `lc-r-auto-evaluation-of-anthropic-100k-context-window`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/auto-evaluation-of-anthropic-100k-context-window
- **Date:** 2023-05-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


## <a id="scaffolding-patterns"></a>Scaffolding patterns

_1 posts_

### The "think" tool: Enabling Claude to stop and think

- **ID:** `ant-e-claude-think-tool`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/claude-think-tool
- **Date:** 2025-03-20
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


## <a id="agent-skills-and-prompt-libraries"></a>Agent skills & prompt libraries

_1 posts_

### Equipping agents for the real world with Agent Skills

- **ID:** `ant-e-equipping-agents-for-the-real-world-with-agent-skills`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- **Date:** 2025-10-16
- **Authors:** Barry Zhang|Keith Lazuka|Mahesh Murag
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


## <a id="ai-sdk-and-product-tooling"></a>AI SDK & product tooling (Vercel v0, AI SDK)

_23 posts_

### A new programming model for durable execution

- **ID:** `vcl-e-a-new-programming-model-for-durable-execution`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/a-new-programming-model-for-durable-execution
- **Date:** 2026-04-16
- **Authors:** Pranay Prakash
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Agent skills explained: An FAQ

- **ID:** `vcl-e-agent-skills-explained-an-faq`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/agent-skills-explained-an-faq
- **Date:** 2026-01-26
- **Authors:** Eric Dodds|Andrew Qu
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### How Mux shipped durable video workflows with their @mux/ai SDK

- **ID:** `vcl-a-how-mux-shipped-durable-video-workflows-with-their-mux-ai-sdk`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/how-mux-shipped-durable-video-workflows-with-their-mux-ai-sdk
- **Date:** 2026-01-12
- **Authors:** Dylan Jhaveri
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### AI SDK 6

- **ID:** `vcl-a-ai-sdk-6`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/ai-sdk-6
- **Date:** 2025-12-22
- **Authors:** Gregor Martynus|Lars Grammel|Aayush Kapoor|Josh Singh|Nico Albanese
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### AI SDK 5

- **ID:** `vcl-a-ai-sdk-5`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/ai-sdk-5
- **Date:** 2025-07-31
- **Authors:** Lars Grammel|Nico Albanese|Josh Singh
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### AI SDK 4.2

- **ID:** `vcl-a-ai-sdk-4-2`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/ai-sdk-4-2
- **Date:** 2025-03-21
- **Authors:** Lars Grammel|Jared Palmer|Nico Albanese
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Using the AI SDK to build Sitecore Stream's AI-powered brand aware assistant

- **ID:** `vcl-a-using-the-ai-sdk-to-build-sitecore-streams-ai-powered-brand-aware-assistant`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/using-the-ai-sdk-to-build-sitecore-streams-ai-powered-brand-aware-assistant
- **Date:** 2025-03-03
- **Authors:** Alli Pope
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### AI SDK 4.1

- **ID:** `vcl-a-ai-sdk-4-1`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/ai-sdk-4-1
- **Date:** 2025-01-20
- **Authors:** Lars Grammel|Jared Palmer|Nico Albanese|Walter Korman
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Easier evaluations with LangSmith SDK v0.2

- **ID:** `lc-r-easier-evaluations-with-langsmith-sdk-v0-2`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/easier-evaluations-with-langsmith-sdk-v0-2
- **Date:** 2024-12-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### AI SDK 4.0

- **ID:** `vcl-a-ai-sdk-4-0`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/ai-sdk-4-0
- **Date:** 2024-11-18
- **Authors:** Lars Grammel|Jared Palmer|Nico Albanese|Walter Korman
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Leveraging Vercel and the AI SDK to deliver a seamless, AI-powered experience as a solo founder

- **ID:** `vcl-a-leveraging-vercel-and-the-ai-sdk-to-deliver-a-seamless-ai-powered-experience`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/leveraging-vercel-and-the-ai-sdk-to-deliver-a-seamless-ai-powered-experience
- **Date:** 2024-10-09
- **Authors:** Alli Pope
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### How Chatbase scaled rapidly with Vercel's developer experience and AI SDK

- **ID:** `vcl-a-how-chatbase-scaled-rapidly-with-vercels-developer-experience-and-ai-sdk`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/how-chatbase-scaled-rapidly-with-vercels-developer-experience-and-ai-sdk
- **Date:** 2024-10-09
- **Authors:** Alli Pope
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### AI SDK 3.4

- **ID:** `vcl-a-ai-sdk-3-4`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/ai-sdk-3-4
- **Date:** 2024-09-20
- **Authors:** Lars Grammel|Jared Palmer|Jeremy Philemon|Nico Albanese
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Announcing LangChain v0.3

- **ID:** `lc-r-announcing-langchain-v0-3`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/announcing-langchain-v0-3
- **Date:** 2024-09-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Using the AI SDK to fix edge-case errors in our code

- **ID:** `vcl-a-using-the-ai-sdk-to-fix-edge-case-errors-in-our-code`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/using-the-ai-sdk-to-fix-edge-case-errors-in-our-code
- **Date:** 2024-08-15
- **Authors:** Rickey McGregor|Dillon Mulroy
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LangGraph v0.2: Increased customization with new checkpointer libraries

- **ID:** `lc-r-langgraph-v0-2`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langgraph-v0-2
- **Date:** 2024-08-07
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Vercel AI SDK 3.3

- **ID:** `vcl-a-vercel-ai-sdk-3-3`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/vercel-ai-sdk-3-3
- **Date:** 2024-08-06
- **Authors:** Lars Grammel|Jared Palmer|Jeremy Philemon|Nico Albanese
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Documentation Refresh for LangChain v0.2

- **ID:** `lc-r-documentation-refresh-for-langchain-v0-2`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/documentation-refresh-for-langchain-v0-2
- **Date:** 2024-05-20
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LangChain v0.2: A Leap Towards Stability

- **ID:** `lc-r-langchain-v02-leap-to-stability`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-v02-leap-to-stability
- **Date:** 2024-05-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Vercel AI SDK 3.1: ModelFusion joins the team

- **ID:** `vcl-a-vercel-ai-sdk-3-1-modelfusion-joins-the-team`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/vercel-ai-sdk-3-1-modelfusion-joins-the-team
- **Date:** 2024-05-02
- **Authors:** Jared Palmer|Lars Grammel
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Composable AI for ecommerce: Hands-on with Vercel’s AI SDK

- **ID:** `vcl-a-composable-ai-for-ecommerce-hands-on-with-vercels-ai-sdk`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/composable-ai-for-ecommerce-hands-on-with-vercels-ai-sdk
- **Date:** 2024-04-09
- **Authors:** Malte Ubl
- **Track:** applied
- **Contribution type:** infra-release
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LangChain v0.1.0

- **ID:** `lc-r-langchain-v0-1-0`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-v0-1-0
- **Date:** 2024-01-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Towards LangChain 0.1: LangChain-Core and LangChain-Community

- **ID:** `lc-r-the-new-langchain-architecture-langchain-core-v0-1-langchain-community-and-a-path-to-langchain-v0-1`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/the-new-langchain-architecture-langchain-core-v0-1-langchain-community-and-a-path-to-langchain-v0-1
- **Date:** 2023-12-12
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


## <a id="data-analyst-and-workflow-agents"></a>Workflow agents (data analyst, code review, Bugbot)

_4 posts_

### Bugbot now self-improves with learned rules

- **ID:** `cur-e-bugbot-learning`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/bugbot-learning
- **Date:** 2026-04-08
- **Authors:** Michael Zhao
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Closing the code review loop with Bugbot

- **ID:** `cur-e-bugbot-autofix`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/bugbot-autofix
- **Date:** 2026-02-26
- **Authors:** Autofix Jon Kaplan
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Build Your Own AI Data Analyst

- **ID:** `cog-e-ai-data-analyst`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/ai-data-analyst
- **Date:** 2025-08-28
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Blockdiff: How we built our own file format for VM disk snapshots

- **ID:** `cog-e-blockdiff`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/blockdiff
- **Date:** 2025-06-23
- **Track:** engineering
- **Contribution type:** retrospective-case-study
- **Signal:** M — L=L/N=M/A=H (priority 6.5)

_Summary pending — see link for details._


## <a id="databricks-training-stack-misc"></a>Databricks training stack (misplaced; should be pretraining/training-stack)

_12 posts_

### Training MoEs at Scale with PyTorch and Databricks

- **ID:** `dbx-e-training-moes-scale-pytorch-and-databricks`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/training-moes-scale-pytorch-and-databricks
- **Date:** 2024-07-01
- **Authors:** Brian Chu|Mihir Patel|Vitaliy Chiley|Evan Racah
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=H/A=H (priority 8.8)

**Summary:**

- Databricks and Meta researchers describe tools for scaling Mixture-of-Experts training in PyTorch
- MegaBlocks (maintained by Databricks) is integrated with LLM Foundry for distributed MoE training to thousands of GPUs
- Uses PyTorch DTensor for parallelism, FSDP/HSDP for sharding to balance memory and communication, elastic sharded checkpointing for fault tolerance
- Backs DBRX training
- Matters as the open-source MoE training stack behind DBRX


### Bringing MegaBlocks to Databricks

- **ID:** `dbx-e-bringing-megablocks-databricks`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/bringing-megablocks-databricks
- **Date:** 2024-04-09
- **Authors:** Mihir Patel|Trevor Gale|Vitaliy Chiley
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- Databricks announces MegaBlocks (open-source MoE training library used to train DBRX) becoming an official Databricks project
- Releases MegaBlocks integration into LLM Foundry training stack and onboards customers to optimized internal versions
- Explains MoE architecture: multiple experts + gating network, replacing feed-forward blocks for parameter-efficient capacity (DBRX is 132B but computes like 36B)
- Matters as core infrastructure for training MoE LLMs at Databricks


### Fast, Secure and Reliable: Enterprise-grade LLM Inference

- **ID:** `dbx-e-fast-secure-and-reliable-enterprise-grade-llm-inference`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/fast-secure-and-reliable-enterprise-grade-llm-inference
- **Date:** 2024-03-20
- **Authors:** Linden Li|Jeffrey Chen|Megha Agarwal|Margaret Qian|Daya Khudia
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=H/A=H (priority 8.8)

**Summary:**

- Databricks describes design of their enterprise-grade LLM inference API
- Focuses on innovative scheduling (beyond simple batching) to optimize time-to-first-token and GPU utilization across diverse workloads on A100/H100/MI300/Gaudi/Inferentia
- Discusses security and reliability considerations for production
- Builds on earlier MosaicML inference work
- Matters as production LLM serving best-practices case study


### LLM Training and Inference with Intel Gaudi 2 AI Accelerators

- **ID:** `dbx-e-llm-training-and-inference-intel-gaudi2-ai-accelerators`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/llm-training-and-inference-intel-gaudi2-ai-accelerators
- **Date:** 2024-01-04
- **Authors:** Abhi Venigalla|Daya Khudia
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- Databricks profiles Intel Gaudi 2 accelerators for LLM training and inference with LLM Foundry and Optimum Habana
- Finds Gaudi 2 is second-best training performance-per-chip (after H100), >260 TFLOP/s/device on MPT-7B with near-linear multi-node scaling
- For LLaMa2-70B inference, 8xGaudi 2 matches 8xH100 on decode latency
- Competitive performance-per-dollar vs cloud alternatives
- Matters as hardware diversification option away from NVIDIA


### Training LLMs at Scale with AMD MI250 GPUs

- **ID:** `dbx-e-training-llms-scale-amd-mi250-gpus`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/training-llms-scale-amd-mi250-gpus
- **Date:** 2023-10-30
- **Authors:** Abhi Venigalla
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- Databricks/MosaicML benchmark training MPT-7B on 128 AMD MI250 GPUs (AMD Accelerator Cloud)
- Near-linear scaling from 4 to 128 MI250s
- ROCm 5.7 + FlashAttention-2 gives 1.13x higher training performance vs earlier ROCm 5.4
- Notes AMD's contributions to Triton compiler for cross-vendor kernels
- Demonstrates AMD as viable large-scale LLM training platform
- Matters as hardware competition/option for NVIDIA alternatives


### LLM Training on Unity Catalog data with MosaicML Streaming Dataset

- **ID:** `dbx-e-llm-training-unity-catalog-data-mosaicml-streaming-dataset`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/llm-training-unity-catalog-data-mosaicml-streaming-dataset
- **Date:** 2023-10-17
- **Authors:** Xiaohan Zhang|Maddie Dawson|Karan Jariwala
- **Track:** engineering
- **Contribution type:** dataset-benchmark
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- Databricks integrates MosaicML StreamingDataset with Unity Catalog for LLM training data pipelines
- Introduces Mosaic Data Shard (MDS) format optimized for training (fast random access, good shuffling, compressibility) vs CSV/JSON/Parquet
- Uses Spark on UC for filtering/tokenization/encoding at scale, then streams directly to GPU training
- Matters as data-governance + streaming training workflow for enterprise LLMs


### LLM Inference Performance Engineering: Best Practices

- **ID:** `dbx-e-llm-inference-performance-engineering-best-practices`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices
- **Date:** 2023-10-12
- **Authors:** Megha Agarwal|Asfandyar Qureshi|Nikhil Sardana|Linden Li|Julian Quevedo|Daya Khudia
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- MosaicML engineering post on best practices for production LLM inference
- Explains prefill vs decode stages of text generation
- Covers four key metrics: Time To First Token, time per output token, latency, throughput
- Draws on experience with FasterTransformer, vLLM, TensorRT-LLM backends
- Provides guidelines for model and hardware selection
- Matters as foundational performance-engineering guide for LLM serving


### Training LLMs with AMD MI250 GPUs and MosaicML

- **ID:** `dbx-e-amd-mi250`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/amd-mi250
- **Date:** 2023-06-30
- **Authors:** Abhi Venigalla
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- MosaicML announces LLM training works out-of-the-box on AMD MI250 with ROCm 5.4 and PyTorch 2.0, zero code changes
- MPT-1B training on MI250 vs A100 produces nearly identical loss curves (can switch mid-run)
- Per-GPU throughput 80% of A100-40GB and 73% of A100-80GB with expectations to close gap
- Uses LLM Foundry stack
- Matters as first validation of AMD as drop-in NVIDIA alternative for LLM training


### Cloudflare R2 and MosaicML: Train LLMs on Any Compute with Zero Switching Costs

- **ID:** `dbx-e-cloudflare-r2-mosaicml`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/cloudflare-r2-mosaicml
- **Date:** 2023-05-23
- **Authors:** Abhinav Venigalla
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

**Summary:**

- Short announcement of Cloudflare R2 + MosaicML integration for LLM training storage
- StreamingDataset and Composer libraries stream training data and checkpoints from R2
- R2's zero-egress pricing + MosaicML's cloud-agnostic platform enable moving jobs across compute providers without transfer fees
- Matters for cost-effective multi-cloud LLM training


### How We Trained Stable Diffusion for Less than $50k (Part 3)

- **ID:** `dbx-r-diffusion`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/diffusion
- **Date:** 2023-04-28
- **Authors:** Mihir Patel|Erica Ji Yuen|Cory Stephenson|Landan Seguin
- **Track:** research
- **Contribution type:** retrospective-case-study
- **Signal:** H — L=H/N=M/A=H (priority 8.7)

**Summary:**

- Technical deep-dive on how MosaicML trained Stable Diffusion 2 base from scratch in 6.8 days for <$50k
- Covers xFormers FlashAttention for faster cross-attention, fusions, and sharding strategies
- 8x speedup vs StabilityAI's reported number and 3x vs MosaicML's own baseline
- Code open-sourced
- Matters as reproducible recipe for affordable diffusion model pretraining


### Farewell, CUDA OOM: Automatic Gradient Accumulation

- **ID:** `dbx-e-farewell-oom`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/farewell-oom
- **Date:** 2022-06-23
- **Authors:** Mihir Patel|Erica Ji Yuen
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=M/A=H (priority 7.6)
- **Techniques:** training-dynamics

**Summary:**

- MosaicML Composer introduces automatic gradient accumulation: catches CUDA OOM during training and dynamically adjusts grad-accum steps to fit memory
- Lets users change GPU type/count without re-tuning batch size
- Demonstrated on GPT3-125M across 1/8/32 A100s with identical convergence
- Matters as quality-of-life feature that eliminates manual hyperparameter tuning for OOM avoidance


### How We Trained Stable Diffusion for Less than $50k (Part 1)

- **ID:** `dbx-r-stable-diffusion-1`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/stable-diffusion-1
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** retrospective-case-study
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

**Summary:**

- MosaicML Part 1: training Stable Diffusion from scratch for <$160k (updated to $125k) in 79,000 A100-hours over 13 days
- Uses Streaming datasets, Composer, MosaicML platform
- 2.5x reduction in time/cost vs baseline
- Argues tooling democratizes access beyond a few organizations and gives data control to enterprises
- Matters as reproducible recipe establishing cost floor for diffusion training


## <a id="fallback-harness"></a>Other harness & context engineering

_219 posts_

### Reusable Evaluators and Evaluator Templates in LangSmith

- **ID:** `lc-r-reusable-langsmith-evaluator-templates`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/reusable-langsmith-evaluator-templates
- **Date:** 2026-04-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Running Subagents in the Background

- **ID:** `lc-r-running-subagents-in-the-background`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/running-subagents-in-the-background
- **Date:** 2026-04-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How We Made Our Docs Test Themselves

- **ID:** `lc-r-our-docs-test-themselves`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/our-docs-test-themselves
- **Date:** 2026-04-15
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Your harness, your memory

- **ID:** `lc-r-your-harness-your-memory`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/your-harness-your-memory
- **Date:** 2026-04-11
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Open Models have crossed a threshold

- **ID:** `lc-r-open-models-have-crossed-a-threshold`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/open-models-have-crossed-a-threshold
- **Date:** 2026-04-02
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### March 2026: LangChain Newsletter

- **ID:** `lc-r-march-2026-langchain-newsletter`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/march-2026-langchain-newsletter
- **Date:** 2026-04-01
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Middleware Lets You Customize Your Agent Harness

- **ID:** `lc-r-how-middleware-lets-you-customize-your-agent-harness`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-middleware-lets-you-customize-your-agent-harness
- **Date:** 2026-03-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Skills in LangSmith Fleet

- **ID:** `lc-r-skills-in-langsmith-fleet`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/skills-in-langsmith-fleet
- **Date:** 2026-03-25
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Fast regex search: indexing text for agent tools

- **ID:** `cur-r-fast-regex-search`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/fast-regex-search
- **Date:** 2026-03-23
- **Authors:** Vicent Marti
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=L/A=M (priority 6.5)
- **Techniques:** coding-agents

**Summary:**

- Cursor research on indexing text to accelerate agent regex search
- Notes agents love to use grep despite decades of more specialized tools (ctags, LSP)
- Cursor default harness uses ripgrep but filesystem I/O is bottleneck
- Describes building an index that enables agent tools to run regex queries far faster than traditional ripgrep-over-files
- Matters as concrete context-engineering optimization for coding-agent tool call latency


### Polly is generally available everywhere you work in LangSmith

- **ID:** `lc-r-polly-langsmith-ga`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/polly-langsmith-ga
- **Date:** 2026-03-18
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Introducing deploy cli

- **ID:** `lc-r-introducing-deploy-cli`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/introducing-deploy-cli
- **Date:** 2026-03-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### The Anatomy of an Agent Harness

- **ID:** `lc-r-the-anatomy-of-an-agent-harness`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/the-anatomy-of-an-agent-harness
- **Date:** 2026-03-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Evaluating Skills

- **ID:** `lc-r-evaluating-skills`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/evaluating-skills
- **Date:** 2026-03-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain Skills

- **ID:** `lc-r-langchain-skills`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-skills
- **Date:** 2026-03-04
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangSmith CLI & Skills

- **ID:** `lc-r-langsmith-cli-skills`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langsmith-cli-skills
- **Date:** 2026-03-04
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### February 2026: LangChain Newsletter

- **ID:** `lc-r-febraury-2026-langchain-newsletter`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/febraury-2026-langchain-newsletter
- **Date:** 2026-03-03
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### monday Service + LangSmith: Building a Code-First Evaluation Strategy from Day 1

- **ID:** `lc-r-customers-monday`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-monday
- **Date:** 2026-02-18
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Scaling Managed Agents: Decoupling the brain from the hands

- **ID:** `ant-e-managed-agents`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/managed-agents
- **Date:** 2026-02-04
- **Authors:** Lance Martin|Gabe Cemaj|Michael Cohen
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

**Summary:**

- Introduces Anthropic's Managed Agents: a hosted service running long-horizon agent work behind stable interfaces
- Decouples 'brain' (Claude + harness) from 'hands' (sandbox/tools) and 'session' (event log) so each can fail or be replaced independently
- Argues harness assumptions go stale as models improve (e.g., context resets no longer needed on Opus 4.5), so interfaces should outlast implementations
- Applies OS-style virtualization (process/file analogs) to agents: session, harness, sandbox as swappable components
- Matters for building durable, maintainable agent infrastructure in production.


### January 2026: LangChain Newsletter

- **ID:** `lc-r-january-2026-langchain-newsletter`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/january-2026-langchain-newsletter
- **Date:** 2026-01-29
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### In software, the code documents the app. In AI, the traces do.

- **ID:** `lc-r-in-software-the-code-documents-the-app-in-ai-the-traces-do`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/in-software-the-code-documents-the-app-in-ai-the-traces-do
- **Date:** 2026-01-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Jimdo empower solopreneurs with AI-powered business assistance

- **ID:** `lc-r-customers-jimdo`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-jimdo
- **Date:** 2025-11-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Why We Rebuilt LangChain’s Chatbot and What We Learned

- **ID:** `lc-r-rebuilding-chat-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/rebuilding-chat-langchain
- **Date:** 2025-11-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Reflections on Three Years of Building LangChain

- **ID:** `lc-r-three-years-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/three-years-langchain
- **Date:** 2025-10-20
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Not Another Workflow Builder

- **ID:** `lc-r-not-another-workflow-builder`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/not-another-workflow-builder
- **Date:** 2025-10-07
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Standard message content

- **ID:** `lc-r-standard-message-content`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/standard-message-content
- **Date:** 2025-09-03
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain & LangGraph 1.0 alpha releases

- **ID:** `lc-r-langchain-langchain-1-0-alpha-releases`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-langchain-1-0-alpha-releases
- **Date:** 2025-09-02
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Open Deep Research

- **ID:** `lc-r-open-deep-research`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/open-deep-research
- **Date:** 2025-07-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### The Hidden Metric That Determines AI Product Success

- **ID:** `lc-r-the-hidden-metric-that-determines-ai-product-success`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/the-hidden-metric-that-determines-ai-product-success
- **Date:** 2025-06-12
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangGraph Release Week Recap

- **ID:** `lc-r-langgraph-release-week-recap`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langgraph-release-week-recap
- **Date:** 2025-06-09
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangSmith Incident on May 1, 2025

- **ID:** `lc-r-langsmith-incident-on-may-1-2025`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langsmith-incident-on-may-1-2025
- **Date:** 2025-05-01
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Catch production failures early with LangSmith Alerts

- **ID:** `lc-r-langsmith-alerts`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langsmith-alerts
- **Date:** 2025-04-22
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Trellix cut log parsing time from days to minutes with LangGraph Studio and LangSmith

- **ID:** `lc-r-customers-trellix`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-trellix
- **Date:** 2025-04-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### TAMM AI Assistant: Transforming Government Services in Abu Dhabi with LangChain and LangGraph"

- **ID:** `lc-r-customers-abu-dhabi-government`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-abu-dhabi-government
- **Date:** 2025-04-15
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Introducing End-to-End OpenTelemetry Support in LangSmith

- **ID:** `lc-r-end-to-end-opentelemetry-langsmith`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/end-to-end-opentelemetry-langsmith
- **Date:** 2025-03-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Vodafone transforms data operations with AI using LangChain and LangGraph

- **ID:** `lc-r-customers-vodafone`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-vodafone
- **Date:** 2025-03-23
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Inconvo is improving customer-facing analytics with conversational AI built on LangGraph

- **ID:** `lc-r-customers-inconvo`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-inconvo
- **Date:** 2025-03-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How C.H. Robinson is transforming the logistics industry with LangChain

- **ID:** `lc-r-customers-chrobinson`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-chrobinson
- **Date:** 2025-03-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How MUFG Bank increased sales efficiency by 10x with LangChain

- **ID:** `lc-r-customers-mufgbank`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-mufgbank
- **Date:** 2025-02-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Quickly Start Evaluating LLMs With OpenEvals

- **ID:** `lc-r-evaluating-llms-with-openevals`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/evaluating-llms-with-openevals
- **Date:** 2025-02-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Klarna's AI assistant redefined customer support at scale for 85 million active users

- **ID:** `lc-r-customers-klarna`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-klarna
- **Date:** 2025-02-12
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### How Vizient empowers healthcare providers with reliable GenAI insights using LangGraph and LangSmith

- **ID:** `lc-r-customers-vizient`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-vizient
- **Date:** 2025-02-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Infor is Transforming Enterprise AI using LangGraph and LangSmith

- **ID:** `lc-r-customers-infor`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-infor
- **Date:** 2025-02-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Is LangGraph Used In Production?

- **ID:** `lc-r-is-langgraph-used-in-production`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/is-langgraph-used-in-production
- **Date:** 2025-02-04
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Introducing the LangGraph Functional API

- **ID:** `lc-r-introducing-the-langgraph-functional-api`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/introducing-the-langgraph-functional-api
- **Date:** 2025-01-29
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Exploring Prompt Optimization

- **ID:** `lc-r-exploring-prompt-optimization`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/exploring-prompt-optimization
- **Date:** 2025-01-28
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Structured Report Generation Blueprint with NVIDIA AI

- **ID:** `lc-r-structured-report-generation-blueprint`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/structured-report-generation-blueprint
- **Date:** 2025-01-06
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain State of AI 2024 Report

- **ID:** `lc-r-langchain-state-of-ai-2024`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-state-of-ai-2024
- **Date:** 2024-12-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How AppFolio transformed property management workflows with Realm-X, built using LangGraph and LangSmith

- **ID:** `lc-r-customers-appfolio`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-appfolio
- **Date:** 2024-12-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Introducing OpenTelemetry support for LangSmith

- **ID:** `lc-r-opentelemetry-langsmith`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/opentelemetry-langsmith
- **Date:** 2024-12-09
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Semantic Search for LangGraph Memory

- **ID:** `lc-r-semantic-search-for-langgraph-memory`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/semantic-search-for-langgraph-memory
- **Date:** 2024-12-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Cleric’s AI SRE leveled up with continuous learning through LangSmith

- **ID:** `lc-r-customers-cleric`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-cleric
- **Date:** 2024-12-02
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangSmith: Redesigned product homepage and Resource Tags for better organization

- **ID:** `lc-r-langsmith-homepage-redesign-and-resource-tags`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langsmith-homepage-redesign-and-resource-tags
- **Date:** 2024-11-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Promptim: an experimental library for prompt optimization

- **ID:** `lc-r-promptim`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/promptim
- **Date:** 2024-11-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Introducing Prompt Canvas: a Novel UX for Developing Prompts

- **ID:** `lc-r-introducing-prompt-canvas`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/introducing-prompt-canvas
- **Date:** 2024-11-12
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### SCIPE - Systematic Chain Improvement and Problem Evaluation

- **ID:** `lc-r-scipe-systematic-chain-improvement-and-problem-evaluation`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/scipe-systematic-chain-improvement-and-problem-evaluation
- **Date:** 2024-11-07
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Communication is all you need

- **ID:** `lc-r-communication-is-all-you-need`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/communication-is-all-you-need
- **Date:** 2024-10-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain's Second Birthday

- **ID:** `lc-r-langchain-second-birthday`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-second-birthday
- **Date:** 2024-10-24
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Launching Long-Term Memory Support in LangGraph

- **ID:** `lc-r-launching-long-term-memory-support-in-langgraph`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/launching-long-term-memory-support-in-langgraph
- **Date:** 2024-10-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### How Tradestack launched their MVP in 6 weeks using LangGraph Cloud

- **ID:** `lc-r-customers-tradestack`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-tradestack
- **Date:** 2024-09-25
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Launching LangGraph Templates

- **ID:** `lc-r-launching-langgraph-templates`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/launching-langgraph-templates
- **Date:** 2024-09-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LangChain Integration Docs: Find information faster with revamped pages & API references

- **ID:** `lc-r-langchain-integration-docs-revamped`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-integration-docs-revamped
- **Date:** 2024-08-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Dataset schemas for fast and iterative data curation in LangSmith

- **ID:** `lc-r-dataset-schemas`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/dataset-schemas
- **Date:** 2024-07-31
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Few-shot prompting to improve tool-calling performance

- **ID:** `lc-r-few-shot-prompting-to-improve-tool-calling-performance`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/few-shot-prompting-to-improve-tool-calling-performance
- **Date:** 2024-07-24
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Athena Intelligence optimized research reports with LangSmith, LangChain, and LangGraph

- **ID:** `lc-r-customers-athena-intelligence`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-athena-intelligence
- **Date:** 2024-07-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Improving core tool interfaces and docs in LangChain

- **ID:** `lc-r-improving-core-tool-interfaces-and-docs-in-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/improving-core-tool-interfaces-and-docs-in-langchain
- **Date:** 2024-07-18
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### [Week of 7/8] LangChain Release Notes

- **ID:** `lc-r-week-of-7-8-langchain-release-notes`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/week-of-7-8-langchain-release-notes
- **Date:** 2024-07-12
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangSmith for the full product lifecycle: How Wordsmith quickly builds, debugs, and evaluates LLM performance in production

- **ID:** `lc-r-customers-wordsmith`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-wordsmith
- **Date:** 2024-07-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### What is a "cognitive architecture"?

- **ID:** `lc-r-what-is-a-cognitive-architecture`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/what-is-a-cognitive-architecture
- **Date:** 2024-07-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

_Summary pending — see link for details._


### Improving Memory Retrieval: How New Computer achieved 50% higher recall with LangSmith

- **ID:** `lc-r-customers-new-computer`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-new-computer
- **Date:** 2024-07-02
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Factory used LangSmith to automate their feedback loop and improve iteration speed by 2x

- **ID:** `lc-r-customers-factory`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-factory
- **Date:** 2024-06-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Optimizing Databricks LLM Pipelines with DSPy

- **ID:** `dbx-r-optimizing-databricks-llm-pipelines-dspy`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/optimizing-databricks-llm-pipelines-dspy
- **Date:** 2024-05-23
- **Authors:** Arnav Singhvi|Daniel Pechi (JetBlue)
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- Databricks post introduces DSPy (from Matei Zaharia's Stanford lab) for compiling declarative LLM calls into self-improving pipelines
- Walks through building a custom multi-tool LLM agent using Databricks Marketplace models in DSPy
- Shows deployment via Databricks Model Serving
- Case study: JetBlue using DSPy for customer feedback classification and RAG-powered predictive maintenance chatbots
- Matters as an end-to-end pattern replacing manual prompt tuning


### Integrating LangChain with Azure Container Apps dynamic sessions

- **ID:** `lc-r-integrating-langchain-with-azure-container-apps-dynamic-sessions`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/integrating-langchain-with-azure-container-apps-dynamic-sessions
- **Date:** 2024-05-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Pairwise Evaluations with LangSmith

- **ID:** `lc-r-pairwise-evaluations-with-langsmith`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/pairwise-evaluations-with-langsmith
- **Date:** 2024-05-15
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Dosu Used LangSmith to Achieve a 30% Accuracy Improvement with No Prompt Engineering

- **ID:** `lc-r-dosu-langsmith-no-prompt-eng`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/dosu-langsmith-no-prompt-eng
- **Date:** 2024-05-02
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Regression Testing with LangSmith

- **ID:** `lc-r-regression-testing`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/regression-testing
- **Date:** 2024-05-01
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Announcing LangSmith is now a transactable offering in the Azure Marketplace

- **ID:** `lc-r-announcing-langsmith-is-now-a-transactable-offering-in-the-azure-marketplace`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/announcing-langsmith-is-now-a-transactable-offering-in-the-azure-marketplace
- **Date:** 2024-04-24
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Empowering Development with FlowTestAI: Bridging APIs and LLMs for Enhanced Testing and Privacy

- **ID:** `lc-r-empowering-development-with-flowtestai`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/empowering-development-with-flowtestai
- **Date:** 2024-04-22
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### DSPy on Databricks

- **ID:** `dbx-r-dspy-databricks`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/dspy-databricks
- **Date:** 2024-04-08
- **Authors:** Arnav Singhvi|Michael Carbin|Matei Zaharia
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- Short announcement that DSPy now integrates with Databricks Model Serving and Vector Search
- Supports DBRX Instruct, Mixtral-8x7B, Llama 2 70B Chat, MPT 7B, BGE Large embeddings via dspy.Databricks
- Adds dspy.DatabricksRM for retriever endpoints
- Enables end-to-end DSPy evaluation on Databricks-hosted models for RAG and other pipelines
- Matters as first-class integration of DSPy compilation with Databricks endpoints


### Rethinking Our Documentation

- **ID:** `lc-r-langchain-documentation-refresh`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-documentation-refresh
- **Date:** 2024-04-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangSmith: Production Monitoring & Automations

- **ID:** `lc-r-langsmith-production-logging-automations`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langsmith-production-logging-automations
- **Date:** 2024-04-02
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangFriend: a Journal with Long-Term Memory

- **ID:** `lc-r-langfriend`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langfriend
- **Date:** 2024-03-28
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Open Source Extraction Service

- **ID:** `lc-r-open-source-extraction-service`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/open-source-extraction-service
- **Date:** 2024-03-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Using Feedback to Improve Your Application: Self Learning GPTs

- **ID:** `lc-r-self-learning-gpts`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/self-learning-gpts
- **Date:** 2024-03-20
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Benchmarking Query Analysis in High Cardinality Situations

- **ID:** `lc-r-high-cardinality`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/high-cardinality
- **Date:** 2024-03-15
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Multi Needle in a Haystack

- **ID:** `lc-r-multi-needle-in-a-haystack`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/multi-needle-in-a-haystack
- **Date:** 2024-03-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Iterating Towards LLM Reliability with Evaluation Driven Development

- **ID:** `lc-r-iterating-towards-llm-reliability-with-evaluation-driven-development`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/iterating-towards-llm-reliability-with-evaluation-driven-development
- **Date:** 2024-03-11
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Use Case Accelerant: Extraction Service

- **ID:** `lc-r-use-case-accelerant-extraction-service`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/use-case-accelerant-extraction-service
- **Date:** 2024-03-06
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangGraph for Code Generation

- **ID:** `lc-r-code-execution-with-langgraph`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/code-execution-with-langgraph
- **Date:** 2024-02-27
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Supercharging If-Statements With Prompt Classification Using Ollama and LangChain

- **ID:** `lc-r-supercharging-if-statements-with-prompt-classification-using-ollama-and-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/supercharging-if-statements-with-prompt-classification-using-ollama-and-langchain
- **Date:** 2024-02-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Winning in AI means mastering the new stack

- **ID:** `lc-r-winning-in-ai-means-mastering-the-new-stack`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/winning-in-ai-means-mastering-the-new-stack
- **Date:** 2024-02-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Rakuten Group builds with LangChain and LangSmith to deliver premium products for its business clients and employees

- **ID:** `lc-r-customers-rakuten`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-rakuten
- **Date:** 2024-02-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Dataherald Makes Natural Language to SQL Easy

- **ID:** `lc-r-dataherald`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/dataherald
- **Date:** 2024-02-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Human-in-the-loop with OpenGPTs and LangGraph

- **ID:** `lc-r-human-in-the-loop-with-opengpts-and-langgraph`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/human-in-the-loop-with-opengpts-and-langgraph
- **Date:** 2024-02-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain Partners with CommandBar on their Copilot User Assistant

- **ID:** `lc-r-langchain-partners-with-commandbar-on-their-copilot-user-assistant`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-partners-with-commandbar-on-their-copilot-user-assistant
- **Date:** 2024-02-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Meet Connery: An Open-Source Plugin Infrastructure for OpenGPTs and LLM apps

- **ID:** `lc-r-meet-connery-an-open-source-plugin-infrastructure-for-opengpts-and-llm-apps`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/meet-connery-an-open-source-plugin-infrastructure-for-opengpts-and-llm-apps
- **Date:** 2024-02-07
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Generating Usable Text with AI

- **ID:** `lc-r-generating-usable-text-with-ai`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/generating-usable-text-with-ai
- **Date:** 2024-02-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### OpenGPTs

- **ID:** `lc-r-opengpts`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/opengpts
- **Date:** 2024-01-31
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LangSmith's Latest Feature: Grouped Monitoring Charts

- **ID:** `lc-r-grouped-monitoring-charts`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/grouped-monitoring-charts
- **Date:** 2024-01-30
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain partners with Elastic to launch the Elastic AI Assistant

- **ID:** `lc-r-langchain-partners-with-elastic-to-launch-the-elastic-ai-assistant`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-partners-with-elastic-to-launch-the-elastic-ai-assistant
- **Date:** 2024-01-30
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Mental Health Therapy as an LLM State Machine

- **ID:** `lc-r-mental-health-therapy-as-an-llm-state-machine`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/mental-health-therapy-as-an-llm-state-machine
- **Date:** 2024-01-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Mendable leverages LangSmith to debug Tools & Actions

- **ID:** `lc-r-how-mendable-leverages-langsmith-to-debug-tools-actions`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-mendable-leverages-langsmith-to-debug-tools-actions
- **Date:** 2024-01-25
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangGraph

- **ID:** `lc-r-langgraph`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langgraph
- **Date:** 2024-01-17
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LangChain State of AI 2023

- **ID:** `lc-r-langchain-state-of-ai-2023`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-state-of-ai-2023
- **Date:** 2023-12-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Rubric Labs and Graphite leveraged LLMs to create personalized videos at scale

- **ID:** `lc-r-rubric-labs-graphite-personalized-video-at-scale`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/rubric-labs-graphite-personalized-video-at-scale
- **Date:** 2023-12-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Extraction Benchmarking

- **ID:** `lc-r-extraction-benchmarking`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/extraction-benchmarking
- **Date:** 2023-12-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Transforming Mortgage Ops with LangChain & LangSmith

- **ID:** `lc-r-transforming-mortgage-ops-with-langchain-langsmith`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/transforming-mortgage-ops-with-langchain-langsmith
- **Date:** 2023-12-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Adding Long Term Memory to OpenGPTs

- **ID:** `lc-r-adding-long-term-memory-to-opengpts`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/adding-long-term-memory-to-opengpts
- **Date:** 2023-11-29
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### OpenAI's Bet on a Cognitive Architecture

- **ID:** `lc-r-openais-bet-on-a-cognitive-architecture`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/openais-bet-on-a-cognitive-architecture
- **Date:** 2023-11-28
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

_Summary pending — see link for details._


### Sharing LangSmith Benchmarks

- **ID:** `lc-r-public-langsmith-benchmarks`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/public-langsmith-benchmarks
- **Date:** 2023-11-22
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Introducing Dream – an AI no-code tool to build fully functional web apps and components with natural language

- **ID:** `lc-r-introducing-dream`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/introducing-dream
- **Date:** 2023-11-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Introducing Tuna - A Tool for Rapidly Generating Synthetic Fine-Tuning Datasets

- **ID:** `lc-r-introducing-tuna-a-tool-for-rapidly-generating-synthetic-fine-tuning-datasets`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/introducing-tuna-a-tool-for-rapidly-generating-synthetic-fine-tuning-datasets
- **Date:** 2023-11-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### "Research Assistant": Exploring UXs Besides Chat

- **ID:** `lc-r-exploring-uxs-besides-chat-with-research-assistant`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/exploring-uxs-besides-chat-with-research-assistant
- **Date:** 2023-11-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain Expands Collaboration with Microsoft

- **ID:** `lc-r-langchain-expands-collaboration-with-microsoft`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-expands-collaboration-with-microsoft
- **Date:** 2023-11-15
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Morningstar Intelligence Engine puts personalized investment insights at analysts' fingertips

- **ID:** `lc-r-morningstar-intelligence-engine-puts-personalized-investment-insights-at-analysts-fingertips`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/morningstar-intelligence-engine-puts-personalized-investment-insights-at-analysts-fingertips
- **Date:** 2023-11-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Query Construction

- **ID:** `lc-r-query-construction`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/query-construction
- **Date:** 2023-11-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Parallel Function Calling for Structured Data Extraction

- **ID:** `lc-r-parallel-function-calling-extraction`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/parallel-function-calling-extraction
- **Date:** 2023-11-09
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain Templates

- **ID:** `lc-r-langchain-templates`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-templates
- **Date:** 2023-10-31
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Announcing Data Annotation Queues

- **ID:** `lc-r-announcing-data-annotation-queue`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/announcing-data-annotation-queue
- **Date:** 2023-10-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LangChain's First Birthday

- **ID:** `lc-r-langchains-first-birthday`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchains-first-birthday
- **Date:** 2023-10-24
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Query Transformations

- **ID:** `lc-r-query-transformations`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/query-transformations
- **Date:** 2023-10-24
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Beyond Text: Making GenAI Applications Accessible to All

- **ID:** `lc-r-beyond-text-making-genai-applications-accessible-to-all`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/beyond-text-making-genai-applications-accessible-to-all
- **Date:** 2023-10-23
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Robocorp’s code generation assistant makes building Python automation easy for developers

- **ID:** `lc-r-robocorps-code-gen-assistant-makes-building-python-automation-easy-for-developers`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/robocorps-code-gen-assistant-makes-building-python-automation-easy-for-developers
- **Date:** 2023-10-22
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Constructing knowledge graphs from text using OpenAI functions: Leveraging knowledge graphs to power LangChain Applications

- **ID:** `lc-r-constructing-knowledge-graphs-from-text-using-openai-functions`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/constructing-knowledge-graphs-from-text-using-openai-functions
- **Date:** 2023-10-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangServe Playground and Configurability

- **ID:** `lc-r-langserve-playground-and-configurability`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langserve-playground-and-configurability
- **Date:** 2023-10-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### The Prompt Landscape

- **ID:** `lc-r-the-prompt-landscape`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/the-prompt-landscape
- **Date:** 2023-10-18
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### You.com x LangChain

- **ID:** `lc-r-you-com-x-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/you-com-x-langchain
- **Date:** 2023-10-18
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Test Run Comparisons

- **ID:** `lc-r-test-run-comparisons`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/test-run-comparisons
- **Date:** 2023-10-17
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Testing Fine Tuned Open Source Models in LangSmith

- **ID:** `lc-r-testing-fine-tuned-open-source-models-in-langsmith`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/testing-fine-tuned-open-source-models-in-langsmith
- **Date:** 2023-10-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Building LLM-Powered Web Apps with Client-Side Technology

- **ID:** `lc-r-building-llm-powered-web-apps-with-client-side-technology`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/building-llm-powered-web-apps-with-client-side-technology
- **Date:** 2023-10-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Introducing LangServe, the best way to deploy your LangChains

- **ID:** `lc-r-introducing-langserve`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/introducing-langserve
- **Date:** 2023-10-12
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Building (and Breaking) WebLangChain

- **ID:** `lc-r-weblangchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/weblangchain
- **Date:** 2023-10-04
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Handling PII data in LangChain

- **ID:** `lc-r-handling-pii-data-in-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/handling-pii-data-in-langchain
- **Date:** 2023-10-03
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Bringing Free OSS Models to the Playground with Fireworks AI

- **ID:** `lc-r-bringing-free-oss-models-to-the-playground-with-fireworks-ai`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/bringing-free-oss-models-to-the-playground-with-fireworks-ai
- **Date:** 2023-10-02
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How "Correct" are LLM Evaluators?

- **ID:** `lc-r-how-correct-are-llm-evaluators`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-correct-are-llm-evaluators
- **Date:** 2023-09-28
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Building Chat LangChain

- **ID:** `lc-r-building-chat-langchain-2`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/building-chat-langchain-2
- **Date:** 2023-09-27
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Fine-tune your LLMs with LangSmith and Lilac

- **ID:** `lc-r-fine-tune-your-llms-with-langsmith-and-lilac`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/fine-tune-your-llms-with-langsmith-and-lilac
- **Date:** 2023-09-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Timescale Vector x LangChain: Making PostgreSQL A Better Vector Database for AI Applications

- **ID:** `lc-r-timescale-vector-x-langchain-making-postgresql-a-better-vector-database-for-ai-applications`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/timescale-vector-x-langchain-making-postgresql-a-better-vector-database-for-ai-applications
- **Date:** 2023-09-24
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Eden AI x LangChain: Harnessing LLMs, Embeddings, and AI

- **ID:** `lc-r-eden-ai-x-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/eden-ai-x-langchain
- **Date:** 2023-09-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain and Scrimba Partner to help Web Devs become AI Engineers

- **ID:** `lc-r-langchain-and-scrimba-partner-to-help-web-devs-become-ai-engineers`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-and-scrimba-partner-to-help-web-devs-become-ai-engineers
- **Date:** 2023-09-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Peering Into the Soul of AI Decision-Making with LangSmith

- **ID:** `lc-r-peering-into-the-soul-of-ai-decision-making-with-langsmith`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/peering-into-the-soul-of-ai-decision-making-with-langsmith
- **Date:** 2023-09-20
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### TED AI Hackathon Kickoff (and projects we’d love to see)

- **ID:** `lc-r-ted-ai-hackathon-kickoff`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/ted-ai-hackathon-kickoff
- **Date:** 2023-09-18
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### OpaquePrompts x LangChain: Enhance the privacy of your LangChain application with just one code change

- **ID:** `lc-r-opaqueprompts-x-langchain-enhance-the-privacy-of-your-langchain-application-with-just-one-code-change`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/opaqueprompts-x-langchain-enhance-the-privacy-of-your-langchain-application-with-just-one-code-change
- **Date:** 2023-09-12
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Neo4j x LangChain: Deep dive into the new Vector index implementation

- **ID:** `lc-r-neo4j-x-langchain-new-vector-index`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/neo4j-x-langchain-new-vector-index
- **Date:** 2023-09-07
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

_Summary pending — see link for details._


### Announcing our Student Hacker in Residence Program, Fall '23 Semester

- **ID:** `lc-r-student-hacker-in-residence-fall-23`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/student-hacker-in-residence-fall-23
- **Date:** 2023-09-06
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Syncing data sources to vector stores

- **ID:** `lc-r-syncing-data-sources-to-vector-stores`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/syncing-data-sources-to-vector-stores
- **Date:** 2023-09-06
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Incorporating domain specific knowledge in SQL-LLM solutions

- **ID:** `lc-r-incorporating-domain-specific-knowledge-in-sql-llm-solutions`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/incorporating-domain-specific-knowledge-in-sql-llm-solutions
- **Date:** 2023-09-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Announcing LangChain Hub

- **ID:** `lc-r-langchain-prompt-hub`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-prompt-hub
- **Date:** 2023-09-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Streamlit LLM Hackathon Kickoff (and projects we’d love to see)

- **ID:** `lc-r-streamlit-llm-hackathon-kickoff-and-projects-wed-love-to-see-2`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/streamlit-llm-hackathon-kickoff-and-projects-wed-love-to-see-2
- **Date:** 2023-09-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### TitanTakeoff x LangChain: Supercharged Local Inference for LLMs

- **ID:** `lc-r-titantakeoff-x-langchain-supercharged-local-inference-for-llms-2`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/titantakeoff-x-langchain-supercharged-local-inference-for-llms-2
- **Date:** 2023-08-30
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Boost Your Bottom Line and Performance: OpenAI’s 3.5T Fine-Tuning with LangSmith

- **ID:** `lc-r-chatopensource-x-langchain-the-future-is-fine-tuning-2`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/chatopensource-x-langchain-the-future-is-fine-tuning-2
- **Date:** 2023-08-29
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Xata x LangChain: new vector store and memory store integrations

- **ID:** `lc-r-xata-x-langchain-new-vector-store-and-memory-store-integrations`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/xata-x-langchain-new-vector-store-and-memory-store-integrations
- **Date:** 2023-08-29
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Chat Loaders: Fine-tune a ChatModel in your Voice

- **ID:** `lc-r-chat-loaders-finetune-a-chatmodel-in-your-voice`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/chat-loaders-finetune-a-chatmodel-in-your-voice
- **Date:** 2023-08-25
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Summarizing and Querying Data from Excel Spreadsheets Using eparse and a Large Language Model

- **ID:** `lc-r-summarizing-and-querying-data-from-excel-spreadsheets-using-eparse-and-a-large-language-model`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/summarizing-and-querying-data-from-excel-spreadsheets-using-eparse-and-a-large-language-model
- **Date:** 2023-08-24
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Cube x LangChain: Building AI experiences with LLMs and the semantic layer

- **ID:** `lc-r-cube-x-langchain-building-ai-experiences-with-llms-and-the-semantic-layer`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/cube-x-langchain-building-ai-experiences-with-llms-and-the-semantic-layer
- **Date:** 2023-08-23
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Tavrn x LangChain: Integrating Noah: ChatGPT with Google Drive and Notion data

- **ID:** `lc-r-integrating-chatgpt-with-google-drive-and-notion-data`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/integrating-chatgpt-with-google-drive-and-notion-data
- **Date:** 2023-08-23
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Using LangSmith to Support Fine-tuning

- **ID:** `lc-r-using-langsmith-to-support-fine-tuning-of-open-source-llms`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/using-langsmith-to-support-fine-tuning-of-open-source-llms
- **Date:** 2023-08-23
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Introducing Airbyte sources within LangChain

- **ID:** `lc-r-introducing-airbyte-sources-within-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/introducing-airbyte-sources-within-langchain
- **Date:** 2023-08-22
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain 🤝 DemoGPT: New Era for Gen-AI Applications

- **ID:** `lc-r-langchain-demogpt-new-era-for-gen-ai-applications`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-demogpt-new-era-for-gen-ai-applications
- **Date:** 2023-08-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Langchain x Predibase: The easiest way to fine-tune and productionize OSS LLMs

- **ID:** `lc-r-langchain-predibase-the-easiest-way-to-fine-tune-and-productionize-oss-llms`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-predibase-the-easiest-way-to-fine-tune-and-productionize-oss-llms
- **Date:** 2023-08-17
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Zep x LangSmith: Foundations of LLM app development with LangChain.js and Zep

- **ID:** `lc-r-zep-x-langsmith-foundations-of-llm-app-development-with-langchain-js-and-zep`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/zep-x-langsmith-foundations-of-llm-app-development-with-langchain-js-and-zep
- **Date:** 2023-08-17
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Qdrant x LangChain: Endgame Performance

- **ID:** `lc-r-qdrant-x-langchain-endgame-performance`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/qdrant-x-langchain-endgame-performance
- **Date:** 2023-08-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### MultiOn x LangChain: Powering Next-Gen Web Automation & Navigation with AI

- **ID:** `lc-r-multion-x-langchain-powering-next-gen-web-automation-navigation-with-ai`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/multion-x-langchain-powering-next-gen-web-automation-navigation-with-ai
- **Date:** 2023-08-15
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Benchmarking Question/Answering Over CSV Data

- **ID:** `lc-r-benchmarking-question-answering-over-csv-data`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/benchmarking-question-answering-over-csv-data
- **Date:** 2023-08-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Label Studio x LangChain: From Foundation Models to Fine-Tuned Applications Using Label Studio

- **ID:** `lc-r-from-foundation-models-to-fine-tuned-applications-using-label-studio`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/from-foundation-models-to-fine-tuned-applications-using-label-studio
- **Date:** 2023-08-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### GPT Researcher x LangChain

- **ID:** `lc-r-gpt-researcher-x-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/gpt-researcher-x-langchain
- **Date:** 2023-08-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### NeumAI x LangChain: Efficiently maintaining context in sync for AI applications

- **ID:** `lc-r-neum-x-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/neum-x-langchain
- **Date:** 2023-08-09
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Chat with your data using OpenAI, Pinecone, Airbyte and Langchain

- **ID:** `lc-r-chat-with-your-data-using-openai-pinecone-airbyte-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/chat-with-your-data-using-openai-pinecone-airbyte-langchain
- **Date:** 2023-08-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Making Data Ingestion Production Ready: a LangChain-Powered Airbyte Destination

- **ID:** `lc-r-making-data-ingestion-production-ready-a-langchain-powered-airbyte-destination`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/making-data-ingestion-production-ready-a-langchain-powered-airbyte-destination
- **Date:** 2023-08-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Unifying AI endpoints with Genoss, powered by LangChain

- **ID:** `lc-r-unifying-ai-endpoints-with-genoss`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/unifying-ai-endpoints-with-genoss
- **Date:** 2023-08-02
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain Expression Language

- **ID:** `lc-r-langchain-expression-language`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-expression-language
- **Date:** 2023-08-01
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Goodbye CVEs, Hello `langchain_experimental`

- **ID:** `lc-r-goodbye-cves-hello-langchain-experimental`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/goodbye-cves-hello-langchain-experimental
- **Date:** 2023-07-31
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Automating Web Research

- **ID:** `lc-r-automating-web-research`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/automating-web-research
- **Date:** 2023-07-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Zep x LangChain: Diagnosing and Fixing Slow Chatbots

- **ID:** `lc-r-zep-x-langchain-slow-chatbots`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/zep-x-langchain-slow-chatbots
- **Date:** 2023-07-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Lepton x LangChain: Earning Sage, How to Transform AI into a Savvy CFO

- **ID:** `lc-r-lepton-x-langchain-earning-sage`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/lepton-x-langchain-earning-sage
- **Date:** 2023-07-24
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### RealChar x LangSmith: Using Open Source tools to create an AI companion

- **ID:** `lc-r-realchar-x-langsmith-ai-companions`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/realchar-x-langsmith-ai-companions
- **Date:** 2023-07-24
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Announcing LangSmith, a unified platform for debugging, testing, evaluating, and monitoring your LLM applications

- **ID:** `lc-r-announcing-langsmith`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/announcing-langsmith
- **Date:** 2023-07-18
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Code Interpreter API

- **ID:** `lc-r-code-interpreter-api`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/code-interpreter-api
- **Date:** 2023-07-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Analyzing User Interactions with LLMs to Improve our Documentation

- **ID:** `lc-r-llms-to-improve-documentation`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/llms-to-improve-documentation
- **Date:** 2023-07-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain x Context: Building Better Chat Products With User Analytics

- **ID:** `lc-r-langchain-x-context-building-better-chat-products-with-user-analytics`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-x-context-building-better-chat-products-with-user-analytics
- **Date:** 2023-07-12
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain 🤝 Streamlit

- **ID:** `lc-r-langchain-streamlit`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-streamlit
- **Date:** 2023-07-11
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### 🎉 Prem Challenge🎉

- **ID:** `lc-r-prem-challenge-with-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/prem-challenge-with-langchain
- **Date:** 2023-06-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain <> MongoDB Atlas

- **ID:** `lc-r-langchain-x-mongodb-atlas`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-x-mongodb-atlas
- **Date:** 2023-06-22
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Data-Driven Characters

- **ID:** `lc-r-data-driven-characters`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/data-driven-characters
- **Date:** 2023-06-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain + Vectara: better together

- **ID:** `lc-r-langchain-vectara-better-together`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-vectara-better-together
- **Date:** 2023-06-06
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Rebuff: Detecting Prompt Injection Attacks

- **ID:** `lc-r-rebuff`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/rebuff
- **Date:** 2023-05-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Feature Stores and LLMs

- **ID:** `lc-r-feature-stores-and-llms`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/feature-stores-and-llms
- **Date:** 2023-05-09
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Structured Tools

- **ID:** `lc-r-structured-tools`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/structured-tools
- **Date:** 2023-05-02
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Auto-Evaluator Opportunities

- **ID:** `lc-r-auto-evaluator-opportunities`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/auto-evaluator-opportunities
- **Date:** 2023-05-01
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Callbacks Improvements

- **ID:** `lc-r-callbacks`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/callbacks
- **Date:** 2023-05-01
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### RecAlign - The smart content filter for social media feed

- **ID:** `lc-r-recalign-the-smart-content-filter-for-social-media-feed`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/recalign-the-smart-content-filter-for-social-media-feed
- **Date:** 2023-04-22
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Improving Document Retrieval with Contextual Compression

- **ID:** `lc-r-improving-document-retrieval-with-contextual-compression`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/improving-document-retrieval-with-contextual-compression
- **Date:** 2023-04-20
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Announcing LangChainJS Support for Multiple JS Environments

- **ID:** `lc-r-js-envs`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/js-envs
- **Date:** 2023-04-11
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LangChain x Supabase

- **ID:** `lc-r-langchain-x-supabase`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-x-supabase
- **Date:** 2023-04-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Retrieval

- **ID:** `lc-r-retrieval`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/retrieval
- **Date:** 2023-03-23
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LangChain + Zapier Natural Language Actions (NLA)

- **ID:** `lc-r-langchain-zapier-nla`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-zapier-nla
- **Date:** 2023-03-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LLMs and SQL

- **ID:** `lc-r-llms-and-sql`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/llms-and-sql
- **Date:** 2023-03-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Origin Web Browser

- **ID:** `lc-r-origin-web-browser`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/origin-web-browser
- **Date:** 2023-03-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Prompt Selectors

- **ID:** `lc-r-prompt-selectors`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/prompt-selectors
- **Date:** 2023-03-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Chat Models

- **ID:** `lc-r-chat-models`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/chat-models
- **Date:** 2023-03-06
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Using the ChatGPT API to evaluate the ChatGPT API

- **ID:** `lc-r-using-chatgpt-api-to-evaluate-chatgpt`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/using-chatgpt-api-to-evaluate-chatgpt
- **Date:** 2023-03-02
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### TypeScript Support

- **ID:** `lc-r-typescript-support`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/typescript-support
- **Date:** 2023-02-17
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Streaming Support in LangChain

- **ID:** `lc-r-streaming-support-in-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/streaming-support-in-langchain
- **Date:** 2023-02-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Chat-Your-Data Submissions

- **ID:** `lc-r-chat-your-data-submissions`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/chat-your-data-submissions
- **Date:** 2023-02-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain + Chroma

- **ID:** `lc-r-langchain-chroma`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-chroma
- **Date:** 2023-02-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Async Support in LangChain

- **ID:** `lc-r-async-api`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/async-api
- **Date:** 2023-02-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Chat-Your-Data Challenge

- **ID:** `lc-r-chat-your-data-challenge`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/chat-your-data-challenge
- **Date:** 2023-02-06
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangChain <> Unstructured

- **ID:** `lc-r-langchain-unstructured`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-unstructured
- **Date:** 2023-02-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Tutorial: ChatGPT Over Your Data

- **ID:** `lc-r-tutorial-chatgpt-over-your-data`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/tutorial-chatgpt-over-your-data
- **Date:** 2023-02-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### GPTwitter

- **ID:** `lc-r-gptwitter`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/gptwitter
- **Date:** 2023-02-01
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Tracing

- **ID:** `lc-r-tracing`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/tracing
- **Date:** 2023-01-29
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LangChainHub

- **ID:** `lc-r-langchainhub`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchainhub
- **Date:** 2023-01-23
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LangChain Chat

- **ID:** `lc-r-langchain-chat`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-chat
- **Date:** 2023-01-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Mosaic LLMs (Part 1): Billion-Parameter GPT Training Made Easy

- **ID:** `dbx-e-billion-parameter-gpt-training-made-easy`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/billion-parameter-gpt-training-made-easy
- **Date:** 2022-08-11
- **Authors:** Abhi Venigalla|Linden Li
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

**Summary:**

- Part 1 of MosaicML LLM series: training GPT-3-style models up to 1.3B params
- Near-linear strong scaling (14.4x speedup on 16x GPUs for 1.3B model on 1B tokens)
- Observes larger models can train more efficiently than smaller ones on modern hardware (10x params ~ 5x training time)
- Covers techniques like activation checkpointing, micro-batching, gang scheduling via MosaicML platform
- Matters as accessible billion-parameter GPT training recipe


### Composer on AWS

- **ID:** `dbx-e-aws-composer`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/aws-composer
- **Date:** _date unknown_
- **Track:** engineering
- **Contribution type:** infra-release
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

**Summary:**

- Short announcement: MosaicML Composer on AWS trains ResNet-50 on ImageNet to 76.6% top-1 accuracy in 27 minutes on an EC2 instance for less than the cost of a pizza
- Points readers to AWS blog post and Composer GitHub/community
- Matters as demonstration of cheap, fast production image classification training on cloud


### Composer 0.10 Release

- **ID:** `dbx-e-composer-0-10-release`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/composer-0-10-release
- **Date:** _date unknown_
- **Track:** engineering
- **Contribution type:** infra-release
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- MosaicML Composer 0.10 release notes: adds CometML integration for experiment tracking, automated evaluation batch-size selection to avoid OOMs, Streaming dataset library preview, API improvements across Metrics/Logging/Evaluation
- Composer is PyTorch training library with 20+ speedup methods
- Matters as incremental release improving MosaicML's open-source training toolkit


### Composer 0.11 Release

- **ID:** `dbx-e-composer-0-11-release`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/composer-0-11-release
- **Date:** _date unknown_
- **Track:** engineering
- **Contribution type:** infra-release
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- MosaicML Composer 0.11 release notes: adds FSDP support, Streaming v0.1 release, simplified checkpointing and distributed experience
- Composer is the open-source PyTorch training library with speedup recipes
- Matters as major release bringing FSDP (sharded data parallelism) into the Composer training stack


### Composer 0.9 Release

- **ID:** `dbx-e-composer-0-9-release`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/composer-0-9-release
- **Date:** _date unknown_
- **Track:** engineering
- **Contribution type:** infra-release
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

**Summary:**

- MosaicML Composer 0.9 release notes: ONNX/TorchScript inference export, ALiBi support for efficient BERT training, GLUE pre-training and fine-tuning entry point, TPU beta support, Apple M1 beta, Composer contrib repo for experimentation
- Matters as release adding inference export, new attention variants, and broader hardware support


### Composer + FFCV: Faster Together

- **ID:** `dbx-e-composer-ffcv-faster-together`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/composer-ffcv-faster-together
- **Date:** _date unknown_
- **Track:** engineering
- **Contribution type:** infra-release
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

**Summary:**

- MosaicML integrates Composer with FFCV, a fast dataloading library from MIT (Aleks Madry's lab)
- Addresses dataloader CPU bottleneck unblocking speedups like Progressive Image Resizing
- FFCV is an ingredient of the Mosaic ResNet recipe showing algorithmic speedup potential
- Baseline ResNet-50 on 8xA100 runs at ~16,200 images/sec
- Matters as training-throughput optimization removing dataloader bottlenecks


### Supercharge Training with Composer

- **ID:** `dbx-e-supercharge-training-composer`
- **Company:** Databricks Mosaic AI
- **Link:** https://web.archive.org/web/2023/https://www.mosaicml.com/blog/supercharge-training-composer
- **Date:** _date unknown_
- **Track:** engineering
- **Contribution type:** infra-release
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- MosaicML overview of Composer library for training PyTorch neural networks faster, cheaper, and more accurately
- Recap of Hagay Lupesko's 2022 PyTorch Developer Conference talk
- Motivates need by exponential growth of SOTA LM sizes over 4 years
- Highlights Composer's 20+ speedup methods and easy-to-use trainer
- Matters as accessible introduction to MosaicML's open-source efficient-training library

