# Agentic Systems

Agents, tool use, multi-agent, computer use, coding agents, agent benchmarks, agent traces, autonomous workflows.

**Post count:** 245

**Contributors:**

- LangChain: 125
- Hugging Face: 24
- Google DeepMind: 22
- Meta AI / FAIR: 18
- OpenAI: 11
- Vercel: 9
- Anthropic: 8
- Cognition: 6
- Databricks Mosaic AI: 5
- Cursor: 5
- AI21 Labs: 3
- Qwen (Alibaba): 2
- Mistral AI: 2
- Moonshot (Kimi): 2
- Google Research: 1
- Allen Institute for AI: 1
- Sakana AI: 1

**Subcategories:**

- [Coding agents](#coding-agents) (10)
- [Multi-agent orchestration](#multi-agent-orchestration) (26)
- [Computer use & browser use](#computer-use-and-browser-use) (4)
- [Tool use & function calling](#tool-use-and-function-calling) (5)
- [Enterprise agents](#enterprise-agents) (6)
- [Embodied agents & simulation](#embodied-and-simulation) (10)
- [Game-playing & RL agents](#game-and-rl-agents) (10)
- [Dialogue & conversational agents](#dialogue-and-conversational-agents) (3)
- [Agent frameworks & tooling](#agent-frameworks-and-tooling) (16)
- [Agent research applications (scientific, robotic)](#agent-research-applications) (3)
- [Agent traces & observability](#agent-traces-and-observability) (4)
- [Agent design & patterns / opinion pieces](#agent-design-and-patterns) (11)
- [General agentic systems](#agents-general) (78)
- [Other agentic systems](#fallback-agents) (59)

---

## <a id="coding-agents"></a>Coding agents

_10 posts_

### Claude Code auto mode: a safer way to skip permissions

- **ID:** `ant-e-claude-code-auto-mode`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/claude-code-auto-mode
- **Date:** 2026-03-25
- **Authors:** John Hughes
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Unrolling the Codex agent loop

- **ID:** `oai-e-unrolling-the-codex-agent-loop`
- **Company:** OpenAI
- **Link:** https://openai.com/index/unrolling-the-codex-agent-loop/
- **Date:** 2026-03-11
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Custom Kernels for All from Codex and Claude

- **ID:** `hf-r-custom-cuda-kernels-agent-skills`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/custom-cuda-kernels-agent-skills
- **Date:** 2026-02-13
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

_Summary pending — see link for details._


### Closing the Agent Loop: Devin Autofixes Review Comments

- **ID:** `cog-e-closing-the-agent-loop-devin-autofixes-review-comments`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/closing-the-agent-loop-devin-autofixes-review-comments
- **Date:** 2026-02-10
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=M/A=H (priority 7.6)
- **Techniques:** coding-agents

_Summary pending — see link for details._


### How we made v0 an effective coding agent

- **ID:** `vcl-a-how-we-made-v0-an-effective-coding-agent`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/how-we-made-v0-an-effective-coding-agent
- **Date:** 2026-01-07
- **Authors:** Max Leiter
- **Track:** applied
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=H (priority 6.4)
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Making Claude Code more secure and autonomous with sandboxing

- **ID:** `ant-e-claude-code-sandboxing`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/claude-code-sandboxing
- **Date:** 2025-10-20
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Rebuilding Devin for Claude Sonnet 4.5: Lessons and Challenges

- **ID:** `cog-e-devin-sonnet-4-5-lessons-and-challenges`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/devin-sonnet-4-5-lessons-and-challenges
- **Date:** 2025-09-29
- **Track:** engineering
- **Contribution type:** retrospective-case-study
- **Signal:** H — L=M/N=M/A=H (priority 7.6)
- **Techniques:** coding-agents

_Summary pending — see link for details._


### How to turn Claude Code into a domain specific coding agent

- **ID:** `lc-r-how-to-turn-claude-code-into-a-domain-specific-coding-agent`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-to-turn-claude-code-into-a-domain-specific-coding-agent
- **Date:** 2025-09-11
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Introducing Open SWE: An Open-Source Asynchronous Coding Agent

- **ID:** `lc-r-introducing-open-swe-an-open-source-asynchronous-coding-agent`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/introducing-open-swe-an-open-source-asynchronous-coding-agent
- **Date:** 2025-08-06
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Alphaevolve A Gemini Powered Coding Agent For Designing Advanced Algorithms

- **ID:** `dm-r-alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=H/A=M (priority 7.8)

_Summary pending — see link for details._


## <a id="multi-agent-orchestration"></a>Multi-agent orchestration

_26 posts_

### Speeding up GPU kernels by 38% with a multi-agent system

- **ID:** `cur-r-multi-agent-kernels`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/multi-agent-kernels
- **Date:** 2026-04-14
- **Authors:** Wilson, Sahil, Yuan & Edward
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)
- **Techniques:** coding-agents, multi-agent

_Summary pending — see link for details._


### How Kensho built a multi-agent framework with LangGraph to solve trusted financial data retrieval

- **ID:** `lc-r-customers-kensho`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-kensho
- **Date:** 2026-03-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Building Multi-Agent Applications with Deep Agents

- **ID:** `lc-r-building-multi-agent-applications-with-deep-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/building-multi-agent-applications-with-deep-agents
- **Date:** 2026-01-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Choosing the Right Multi-Agent Architecture

- **ID:** `lc-r-choosing-the-right-multi-agent-architecture`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture
- **Date:** 2026-01-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

_Summary pending — see link for details._


### How Bertelsmann Built a Multi-Agent System to Empower Creatives

- **ID:** `lc-r-customer-bertelsmann`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customer-bertelsmann
- **Date:** 2025-07-29
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Exa built a Web Research Multi-Agent System with LangGraph and LangSmith

- **ID:** `lc-r-exa`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/exa
- **Date:** 2025-06-30
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How and when to build multi-agent systems

- **ID:** `lc-r-how-and-when-to-build-multi-agent-systems`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems
- **Date:** 2025-06-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How we built our multi-agent research system

- **ID:** `ant-e-multi-agent-research-system`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/multi-agent-research-system
- **Date:** 2025-06-13
- **Authors:** Jeremy Hadfield|Barry Zhang|Kenneth Lien|Florian Scholz|Jeremy Fox|Daniel Ford
- **Track:** engineering
- **Contribution type:** retrospective-case-study
- **Signal:** H — L=M/N=H/A=H (priority 8.8)
- **Techniques:** multi-agent

_Summary pending — see link for details._


### Benchmarking Multi-Agent Architectures

- **ID:** `lc-r-benchmarking-multi-agent-architectures`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/benchmarking-multi-agent-architectures
- **Date:** 2025-06-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How DocentPro Built a Multi-Agent Travel Companion with LangGraph

- **ID:** `lc-r-customers-docentpro`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-docentpro
- **Date:** 2025-04-29
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Why Definely chose LangGraph for building their multi-agent AI system

- **ID:** `lc-r-customers-definely`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-definely
- **Date:** 2025-04-07
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Build.inc used LangGraph to launch a Multi-Agent Architecture for automating critical CRE workflows for Data Center Development.

- **ID:** `lc-r-how-build-inc-used-langgraph-to-launch-a-multi-agent-architecture-for-automating-critical-cre-workflows-for-data-center-development`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-build-inc-used-langgraph-to-launch-a-multi-agent-architecture-for-automating-critical-cre-workflows-for-data-center-development
- **Date:** 2025-03-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

_Summary pending — see link for details._


### How Minimal built a multi-agent customer support system with LangGraph & LangSmith

- **ID:** `lc-r-how-minimal-built-a-multi-agent-customer-support-system-with-langgraph-langsmith`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-minimal-built-a-multi-agent-customer-support-system-with-langgraph-langsmith
- **Date:** 2025-01-20
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Command: A new tool for building multi-agent architectures in LangGraph

- **ID:** `lc-r-command-a-new-tool-for-multi-agent-architectures-in-langgraph`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/command-a-new-tool-for-multi-agent-architectures-in-langgraph
- **Date:** 2024-12-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Chaos Labs built a multi-agent system for resolution in prediction markets

- **ID:** `lc-r-how-chaos-labs-built-a-multi-agent-system-for-resolution-in-prediction-markets`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-chaos-labs-built-a-multi-agent-system-for-resolution-in-prediction-markets
- **Date:** 2024-11-06
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How We Deployed our Multi-Agent Flow to LangGraph Cloud

- **ID:** `lc-r-how-we-deployed-our-multi-agent-flow-to-langgraph-cloud-2`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-we-deployed-our-multi-agent-flow-to-langgraph-cloud-2
- **Date:** 2024-07-15
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How to Build the Ultimate AI Automation with Multi-Agent Collaboration

- **ID:** `lc-r-how-to-build-the-ultimate-ai-automation-with-multi-agent-collaboration`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-to-build-the-ultimate-ai-automation-with-multi-agent-collaboration
- **Date:** 2024-05-09
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangGraph: Multi-Agent Workflows

- **ID:** `lc-r-langgraph-multi-agent-workflows`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langgraph-multi-agent-workflows
- **Date:** 2024-01-23
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Villagers x LangSmith: Simulating multi-agent social networks with LangSmith

- **ID:** `lc-r-villagers-x-langsmith-simulating-multi-agent-social-networks`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/villagers-x-langsmith-simulating-multi-agent-social-networks
- **Date:** 2023-08-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### GPTeam: A multi-agent simulation

- **ID:** `lc-r-gpteam-a-multi-agent-simulation`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/gpteam-a-multi-agent-simulation
- **Date:** 2023-06-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Emergence of grounded compositional language in multi-agent populations

- **ID:** `oai-r-emergence-of-grounded-compositional-language-in-multi-agent-populations`
- **Company:** OpenAI
- **Link:** https://openai.com/index/emergence-of-grounded-compositional-language-in-multi-agent-populations/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)
- **Techniques:** multi-agent

_Summary pending — see link for details._


### Egg A Toolkit For Multi Agent Language Emergence Simulations

- **ID:** `meta-r-egg-a-toolkit-for-multi-agent-language-emergence-simulations`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/egg-a-toolkit-for-multi-agent-language-emergence-simulations/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Using Multi Agent Reinforcement Learning To Improve Collaboration

- **ID:** `meta-r-using-multi-agent-reinforcement-learning-to-improve-collaboration`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/using-multi-agent-reinforcement-learning-to-improve-collaboration/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Alphastar Grandmaster Level In Starcraft Ii Using Multi Agent Reinforcement Learning

- **ID:** `dm-r-alphastar-grandmaster-level-in-starcraft-ii-using-multi-agent-reinforcement-learning`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/alphastar-grandmaster-level-in-starcraft-ii-using-multi-agent-reinforcement-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Emergent Bartering Behaviour In Multi Agent Reinforcement Learning

- **ID:** `dm-r-emergent-bartering-behaviour-in-multi-agent-reinforcement-learning`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/emergent-bartering-behaviour-in-multi-agent-reinforcement-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Game Theory Insights Into Asymmetric Multi Agent Games

- **ID:** `dm-r-game-theory-insights-into-asymmetric-multi-agent-games`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/game-theory-insights-into-asymmetric-multi-agent-games/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


## <a id="computer-use-and-browser-use"></a>Computer use & browser use

_4 posts_

### Cursor agents can now control their own computers

- **ID:** `cur-e-agent-computer-use`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/agent-computer-use
- **Date:** 2026-02-24
- **Authors:** Jonas & Alexi
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)
- **Techniques:** computer-use, coding-agents

_Summary pending — see link for details._


### Mitigating the risk of prompt injections in browser use

- **ID:** `ant-r-prompt-injection-defenses`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/prompt-injection-defenses
- **Date:** 2025-11-24
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Smol2Operator: Post-Training GUI Agents for Computer Use

- **ID:** `hf-r-smol2operator`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/smol2operator
- **Date:** 2025-09-23
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### ScreenEnv: Deploy your full stack Desktop Agent

- **ID:** `hf-r-screenenv`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/screenenv
- **Date:** 2025-07-10
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


## <a id="tool-use-and-function-calling"></a>Tool use & function calling

_5 posts_

### From model to agent: Equipping the Responses API with a computer environment

- **ID:** `oai-e-equip-responses-api-computer-environment`
- **Company:** OpenAI
- **Link:** https://openai.com/index/equip-responses-api-computer-environment/
- **Date:** 2026-02-13
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Writing effective tools for AI agents—using AI agents

- **ID:** `ant-e-writing-tools-for-agents`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/writing-tools-for-agents
- **Date:** 2025-09-11
- **Authors:** Zachary Witten|Daniel Jiang|Sami Al-Sheikh|Matt Bell|Maggie Vo)|MCP (Theodora Chu|David Soria Parra|Adam Jones)
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Tool Use, Unified

- **ID:** `hf-r-unified-tool-use`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/unified-tool-use
- **Date:** 2024-08-12
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Tool Calling with LangChain

- **ID:** `lc-r-tool-calling-with-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/tool-calling-with-langchain
- **Date:** 2024-04-11
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Benchmarking Agent Tool Use

- **ID:** `lc-r-benchmarking-agent-tool-use`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/benchmarking-agent-tool-use
- **Date:** 2023-12-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


## <a id="enterprise-agents"></a>Enterprise agents

_6 posts_

### Agentic Reasoning in Practice: Making Sense of Structured and Unstructured Data

- **ID:** `dbx-r-agentic-reasoning-practice-making-sense-structured-and-unstructured-data`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/agentic-reasoning-practice-making-sense-structured-and-unstructured-data
- **Date:** 2026-04-14
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Memory Scaling for AI Agents

- **ID:** `dbx-r-memory-scaling-ai-agents`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/memory-scaling-ai-agents
- **Date:** 2026-04-10
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Meet KARL: A Faster Agent for Enterprise Knowledge, powered by custom RL

- **ID:** `dbx-r-meet-karl-faster-agent-enterprise-knowledge-powered-custom-rl`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/meet-karl-faster-agent-enterprise-knowledge-powered-custom-rl
- **Date:** 2026-03-05
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Inside OpenAI’s in-house data agent

- **ID:** `oai-e-inside-our-in-house-data-agent`
- **Company:** OpenAI
- **Link:** https://openai.com/index/inside-our-in-house-data-agent/
- **Date:** 2026-01-23
- **Track:** engineering
- **Contribution type:** retrospective-case-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Instructed Retriever: Unlocking System-Level Reasoning in Search Agents

- **ID:** `dbx-r-instructed-retriever-unlocking-system-level-reasoning-search-agents`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/instructed-retriever-unlocking-system-level-reasoning-search-agents
- **Date:** 2026-01-06
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)
- **Techniques:** retrieval-augmentation

_Summary pending — see link for details._


### RAG Agent Solutions for Enterprises: How to Choose One

- **ID:** `a21-r-rag-agent-solutions`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/rag-agent-solutions/
- **Date:** 2025-06-15
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


## <a id="embodied-and-simulation"></a>Embodied agents & simulation

_10 posts_

### 2021 Habitat Challenge Launches To Advance Embodied Ai Research

- **ID:** `meta-r-2021-habitat-challenge-launches-to-advance-embodied-ai-research`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/2021-habitat-challenge-launches-to-advance-embodied-ai-research/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Ai Habitat State Of The Art Simulation Platform Adds Object Interactivity

- **ID:** `meta-r-ai-habitat-state-of-the-art-simulation-platform-adds-object-interactivity`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/ai-habitat-state-of-the-art-simulation-platform-adds-object-interactivity/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._


### Egomimic Project Aria Georgia Tech Ego4D Robotics Embodied Ai

- **ID:** `meta-r-egomimic-project-aria-georgia-tech-ego4d-robotics-embodied-ai`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/egomimic-project-aria-georgia-tech-ego4d-robotics-embodied-ai/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Embodied Question Answering A Goal Driven Approach To Autonomous Agents

- **ID:** `meta-r-embodied-question-answering-a-goal-driven-approach-to-autonomous-agents`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/embodied-question-answering-a-goal-driven-approach-to-autonomous-agents/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Habitat 20 Training Home Assistant Robots With Faster Simulation And New Benchmarks

- **ID:** `meta-r-habitat-20-training-home-assistant-robots-with-faster-simulation-and-new-benchmarks`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/habitat-20-training-home-assistant-robots-with-faster-simulation-and-new-benchmarks/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Habitat 3 Socially Intelligent Robots Siro

- **ID:** `meta-r-habitat-3-socially-intelligent-robots-siro`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/habitat-3-socially-intelligent-robots-siro/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Introducing The Habitat Matterport 3D Research Data Set For Training Embodied Ai

- **ID:** `meta-r-introducing-the-habitat-matterport-3d-research-data-set-for-training-embodied-ai`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/introducing-the-habitat-matterport-3d-research-data-set-for-training-embodied-ai/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### New Milestones In Embodied Ai

- **ID:** `meta-r-new-milestones-in-embodied-ai`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/new-milestones-in-embodied-ai/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Open Sourcing Ai Habitat A Simulation Platform For Embodied Ai Research

- **ID:** `meta-r-open-sourcing-ai-habitat-a-simulation-platform-for-embodied-ai-research`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/open-sourcing-ai-habitat-a-simulation-platform-for-embodied-ai-research/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Robocat A Self Improving Robotic Agent

- **ID:** `dm-r-robocat-a-self-improving-robotic-agent`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/robocat-a-self-improving-robotic-agent/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


## <a id="game-and-rl-agents"></a>Game-playing & RL agents

_10 posts_

### OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments

- **ID:** `hf-r-openenv-turing`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/openenv-turing
- **Date:** 2026-02-12
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Building the Open Agent Ecosystem Together: Introducing OpenEnv

- **ID:** `hf-r-openenv`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/openenv
- **Date:** 2025-10-23
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Gaia2 and ARE: Empowering the community to study agents

- **ID:** `hf-r-gaia2`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/gaia2
- **Date:** 2025-09-22
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Droidlet A One Stop Shop For Modularly Building Intelligent Agents

- **ID:** `meta-r-droidlet-a-one-stop-shop-for-modularly-building-intelligent-agents`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/droidlet-a-one-stop-shop-for-modularly-building-intelligent-agents/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

_Summary pending — see link for details._


### Read To Fight Monsters Using Rl To Teach Agents To Generalize To New Settings

- **ID:** `meta-r-read-to-fight-monsters-using-rl-to-teach-agents-to-generalize-to-new-settings`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/read-to-fight-monsters-using-rl-to-teach-agents-to-generalize-to-new-settings/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

_Summary pending — see link for details._


### Training Ai Agents To Solve Unfamiliar Tasks

- **ID:** `meta-r-training-ai-agents-to-solve-unfamiliar-tasks`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/training-ai-agents-to-solve-unfamiliar-tasks/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

_Summary pending — see link for details._


### Agents That Imagine And Plan

- **ID:** `dm-r-agents-that-imagine-and-plan`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/agents-that-imagine-and-plan/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Building Interactive Agents In Video Game Worlds

- **ID:** `dm-r-building-interactive-agents-in-video-game-worlds`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/building-interactive-agents-in-video-game-worlds/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Capture The Flag The Emergence Of Complex Cooperative Agents

- **ID:** `dm-r-capture-the-flag-the-emergence-of-complex-cooperative-agents`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/capture-the-flag-the-emergence-of-complex-cooperative-agents/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Generally Capable Agents Emerge From Open Ended Play

- **ID:** `dm-r-generally-capable-agents-emerge-from-open-ended-play`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/generally-capable-agents-emerge-from-open-ended-play/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


## <a id="dialogue-and-conversational-agents"></a>Dialogue & conversational agents

_3 posts_

### Ecom-RLVE: Adaptive Verifiable Environments for E-Commerce Conversational Agents

- **ID:** `hf-r-ecom-rlve`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/ecom-rlve
- **Date:** 2026-04-16
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### A Facebook Scale Simulator To Detect Harmful Behaviors

- **ID:** `meta-r-a-facebook-scale-simulator-to-detect-harmful-behaviors`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/a-facebook-scale-simulator-to-detect-harmful-behaviors/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Building Safer Dialogue Agents

- **ID:** `dm-r-building-safer-dialogue-agents`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/building-safer-dialogue-agents/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

_Summary pending — see link for details._


## <a id="agent-frameworks-and-tooling"></a>Agent frameworks & tooling

_16 posts_

### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

- **ID:** `lc-r-secure-agents-cisco-ai-defense`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/secure-agents-cisco-ai-defense
- **Date:** 2026-04-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Kimi Agent SDK

- **ID:** `mn-r-kimi-agent-sdk`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/kimi-agent-sdk
- **Date:** 2026-01-08
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### DeepMath: A lightweight math reasoning Agent with smolagents

- **ID:** `hf-r-intel-deepmath`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/intel-deepmath
- **Date:** 2025-12-04
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

_Summary pending — see link for details._


### Agent Frameworks, Runtimes, and Harnesses- oh my!

- **ID:** `lc-r-agent-frameworks-runtimes-and-harnesses-oh-my`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/agent-frameworks-runtimes-and-harnesses-oh-my
- **Date:** 2025-10-25
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### LangChain and LangGraph Agent Frameworks Reach v1.0 Milestones

- **ID:** `lc-r-langchain-langgraph-1dot0`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langchain-langgraph-1dot0
- **Date:** 2025-10-22
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Back to The Future: Evaluating AI Agents on Predicting Future Events

- **ID:** `hf-r-futurebench`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/futurebench
- **Date:** 2025-07-17
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

_Summary pending — see link for details._


### How to think about agent frameworks

- **ID:** `lc-r-how-to-think-about-agent-frameworks`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-to-think-about-agent-frameworks
- **Date:** 2025-04-20
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Trace & Evaluate your Agent with Arize Phoenix

- **ID:** `hf-r-smolagents-phoenix`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/smolagents-phoenix
- **Date:** 2025-02-28
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

_Summary pending — see link for details._


### Open-source DeepResearch – Freeing our search agents

- **ID:** `hf-r-open-deep-research`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/open-deep-research
- **Date:** 2025-02-04
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

_Summary pending — see link for details._


### Introducing smolagents: simple agents that write actions in code.

- **ID:** `hf-r-smolagents`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/smolagents
- **Date:** 2024-12-31
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

_Summary pending — see link for details._


### License to Call: Introducing Transformers Agents 2.0

- **ID:** `hf-r-agents`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/agents
- **Date:** 2024-05-13
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

_Summary pending — see link for details._


### Open-source LLMs as LangChain Agents

- **ID:** `hf-r-open-source-llms-as-agents`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/open-source-llms-as-agents
- **Date:** 2024-01-24
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

_Summary pending — see link for details._


### How to Safely Query Enterprise Data with LangChain Agents + SQL + OpenAI + Gretel

- **ID:** `lc-r-how-to-safely-query-enterprise-data-with-langchain-agents-sql-openai-gretel`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-to-safely-query-enterprise-data-with-langchain-agents-sql-openai-gretel
- **Date:** 2023-09-12
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Introducing Agents.js: Give tools to your LLMs using JavaScript

- **ID:** `hf-r-agents-js`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/agents-js
- **Date:** 2023-07-24
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** H — L=M/N=M/A=H (priority 7.6)

_Summary pending — see link for details._


### Agent Toolkits

- **ID:** `lc-r-agent-toolkits`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/agent-toolkits
- **Date:** 2023-03-01
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Open Coding Agents

- **ID:** `ai2-r-open-coding-agents`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/open-coding-agents
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


## <a id="agent-research-applications"></a>Agent research applications (scientific, robotic)

_3 posts_

### Improving the academic workflow: Introducing two AI agents for better figures and peer review

- **ID:** `gr-r-improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review`
- **Company:** Google Research
- **Link:** https://research.google/blog/improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Gemini Robotics 15 Brings Ai Agents Into The Physical World

- **ID:** `dm-r-gemini-robotics-15-brings-ai-agents-into-the-physical-world`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


### Opening Up A Physics Simulator For Robotics

- **ID:** `dm-r-opening-up-a-physics-simulator-for-robotics`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/opening-up-a-physics-simulator-for-robotics/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=L (priority 5.6)

_Summary pending — see link for details._


## <a id="agent-traces-and-observability"></a>Agent traces & observability

_4 posts_

### Agent Observability Powers Agent Evaluation

- **ID:** `lc-r-agent-observability-powers-agent-evaluation`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/agent-observability-powers-agent-evaluation
- **Date:** 2026-02-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### On Agent Frameworks and Agent Observability

- **ID:** `lc-r-on-agent-frameworks-and-agent-observability`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/on-agent-frameworks-and-agent-observability
- **Date:** 2026-02-12
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Agent Trace: Capturing the Context Graph of Code

- **ID:** `cog-r-agent-trace`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/agent-trace
- **Date:** 2026-01-29
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Monte Carlo: Building Data + AI Observability Agents with LangGraph and LangSmith

- **ID:** `lc-r-customers-monte-carlo`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-monte-carlo
- **Date:** 2025-09-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


## <a id="agent-design-and-patterns"></a>Agent design & patterns / opinion pieces

_11 posts_

### Trustworthy agents in practice

- **ID:** `ant-r-trustworthy-agents`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/trustworthy-agents
- **Date:** 2026-04-09
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=M (priority 7.7)

_Summary pending — see link for details._


### How we monitor internal coding agents for misalignment

- **ID:** `oai-r-how-we-monitor-internal-coding-agents-misalignment`
- **Company:** OpenAI
- **Link:** https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/
- **Date:** 2026-03-17
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=M (priority 7.7)

_Summary pending — see link for details._


### Coding Agents 101: The Art of Actually Getting Things Done

- **ID:** `cog-r-coding-agents-101-the-art-of-actually-getting-things-done`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/coding-agents-101-the-art-of-actually-getting-things-done
- **Date:** 2025-06-27
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Don’t Build Multi-Agents

- **ID:** `cog-r-dont-build-multi-agents`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/dont-build-multi-agents
- **Date:** 2025-06-12
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=M/N=H/A=M (priority 7.8)

_Summary pending — see link for details._


### AI Agents Are Here. What Now?

- **ID:** `hf-r-ethics-soc-7`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/ethics-soc-7
- **Date:** 2025-01-13
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

_Summary pending — see link for details._


### Building Effective AI Agents

- **ID:** `ant-e-building-effective-agents`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/building-effective-agents
- **Date:** 2024-12-19
- **Authors:** Erik S.|Barry Zhang
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=M (priority 7.7)

_Summary pending — see link for details._


### Building Effective AI Agents

- **ID:** `ant-r-building-effective-agents`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/building-effective-agents
- **Date:** 2024-12-19
- **Authors:** Erik S.|Barry Zhang
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=M (priority 7.7)

_Summary pending — see link for details._


### MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering

- **ID:** `oai-r-mle-bench`
- **Company:** OpenAI
- **Link:** https://openai.com/index/mle-bench/
- **Date:** 2024-10-10
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=M (priority 7.7)

_Summary pending — see link for details._


### A review of OpenAI’s o1 and how we evaluate coding agents

- **ID:** `cog-r-evaluating-coding-agents`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/evaluating-coding-agents
- **Date:** 2024-09-12
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)
- **Techniques:** test-time-compute

_Summary pending — see link for details._


### Build reliable agents in JavaScript with LangGraph.js v0.2: Now supporting Cloud and Studio

- **ID:** `lc-r-javascript-langgraph-v02-cloud-studio`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/javascript-langgraph-v02-cloud-studio
- **Date:** 2024-09-03
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Scalable Agent Architecture For Distributed Training

- **ID:** `dm-r-scalable-agent-architecture-for-distributed-training`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/scalable-agent-architecture-for-distributed-training/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=H/N=M/A=L (priority 6.7)

_Summary pending — see link for details._


## <a id="agents-general"></a>General agentic systems

_78 posts_

### Agentic Infrastructure

- **ID:** `vcl-e-agentic-infrastructure`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/agentic-infrastructure
- **Date:** 2026-04-09
- **Authors:** Tom Occhino
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- Vercel's CPO argues that LLMs/coding agents demand a new generation of infrastructure across three layers
- 30% of Vercel deployments are now initiated by coding agents (75% Claude Code), up 1000% in 6 months
- frames 'Agentic Infrastructure' as (1) infra for coding agents to deploy to, (2) infra for building/running agents, (3) infra that is itself agentic
- emphasizes immutable deploys, preview URLs, MCP, and programmatic surfaces as prerequisites for autonomous agent workflows
- positions Vercel's CLI/API/MCP/git integration as native surface for machine-driven software development.


### Human judgment in the agent improvement loop

- **ID:** `lc-r-human-judgment-in-the-agent-improvement-loop`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/human-judgment-in-the-agent-improvement-loop
- **Date:** 2026-04-09
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### How FLORA shipped a creative agent on Vercel's AI stack

- **ID:** `vcl-e-how-flora-shipped-a-creative-agent-on-vercels-ai-stack`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/how-flora-shipped-a-creative-agent-on-vercels-ai-stack
- **Date:** 2026-03-31
- **Authors:** Eric Dodds
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- Case study of FLORA's creative agent FAUNA built on Vercel's AI stack, orchestrating 50+ image models for fashion campaign visuals
- FAUNA replaces node-based workflow canvas with a conversational agent that picks references, chooses models, and generates variations from user intent
- claims 2x faster shipping to production and zero infrastructure debates after migration
- highlights Vercel AI SDK as the orchestration layer for multi-model creative workflows
- positions agents-as-design-partners as the shift from workflow tools to autonomous creative collaborators.


### Agent responsibly

- **ID:** `vcl-e-agent-responsibly`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/agent-responsibly
- **Date:** 2026-03-30
- **Authors:** Matthew Binshtok
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

**Summary:**

- Internal Vercel talk on disciplined deployment of agent-generated code to production
- argues green CI is no longer proof of safety because agents produce polished, convincing PRs that hide bad assumptions (e.g., full-table scans, retry thundering herds, caches with no TTL)
- warns agents lack production context (traffic patterns, failure modes, capacity limits)
- proposes a review/judgment framework for teams shipping with agents
- useful design-and-patterns guidance for agentic development discipline.


### Agent Evaluation Readiness Checklist

- **ID:** `lc-r-agent-evaluation-readiness-checklist`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/agent-evaluation-readiness-checklist
- **Date:** 2026-03-27
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Two different types of agent authorization

- **ID:** `lc-r-two-different-types-of-agent-authorization`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/two-different-types-of-agent-authorization
- **Date:** 2026-03-23
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Securing our codebase with autonomous agents

- **ID:** `cur-e-security-agents`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/security-agents
- **Date:** 2026-03-16
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=H (priority 6.4)
- **Techniques:** coding-agents

**Summary:**

- Cursor releases four Cursor Automations templates for security agents that continuously identify and repair vulnerabilities
- PR velocity grew 5x over 9 months, outpacing static-analysis/code-ownership approaches
- Agents use webhooks, GitHub PR responses, codebase monitoring plus a custom security MCP tool (serverless Lambda) for persistent data, dedup, and observability
- Matters as applied autonomous security-agent blueprint for engineering teams


### LangChain Announces Enterprise Agentic AI Platform Built with NVIDIA

- **ID:** `lc-r-nvidia-enterprise`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/nvidia-enterprise
- **Date:** 2026-03-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Autonomous context compression

- **ID:** `lc-r-autonomous-context-compression`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/autonomous-context-compression
- **Date:** 2026-03-11
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### How we built LangChain’s GTM Agent

- **ID:** `lc-r-how-we-built-langchains-gtm-agent`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-we-built-langchains-gtm-agent
- **Date:** 2026-03-09
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=L/A=H (priority 5.3)

_Summary pending — see link for details._


### You don’t know what your agent will do until it’s in production

- **ID:** `lc-r-you-dont-know-what-your-agent-will-do-until-its-in-production`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/you-dont-know-what-your-agent-will-do-until-its-in-production
- **Date:** 2026-02-25
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=L/A=H (priority 5.3)

_Summary pending — see link for details._


### Security boundaries in agentic architectures

- **ID:** `vcl-e-security-boundaries-in-agentic-architectures`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/security-boundaries-in-agentic-architectures
- **Date:** 2026-02-24
- **Authors:** Malte Ubl|Harpreet Arora
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=L/A=H (priority 7.5)

**Summary:**

- Argues most coding agents today run generated code with full access to secrets, conflating multiple trust domains into one security context
- recommends separating actors (user, agent, generated code) and placing boundaries between them
- proposes architecture for running agent and generated code in isolated contexts (sandboxes) to contain prompt-injection blast radius
- walks through an example agent debugging prod with a malicious log and how boundaries prevent compromise
- strong design-pattern guidance for production agent deployments.


### How we built Agent Builder’s memory system

- **ID:** `lc-r-how-we-built-agent-builders-memory-system`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-we-built-agent-builders-memory-system
- **Date:** 2026-02-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=L/A=H (priority 5.3)

_Summary pending — see link for details._


### How to Use Memory in Agent Builder

- **ID:** `lc-r-how-to-use-memory-in-agent-builder`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-to-use-memory-in-agent-builder
- **Date:** 2026-02-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Implementing a secure sandbox for local agents

- **ID:** `cur-r-agent-sandboxing`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/agent-sandboxing
- **Date:** 2026-02-18
- **Authors:** Ani, Yash & Alex
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)
- **Techniques:** coding-agents

**Summary:**

- Cursor introduces agent sandboxing on macOS, Linux, Windows for local coding agents
- Sandboxed agents run freely within controlled environment, only requesting approval when accessing internet, reducing approval fatigue
- Sandboxed agents stop 40% less often than unsandboxed
- Exposes a unified sandbox interface across OSes balancing security and usability (many commands need unexpected privileges)
- Matters as production safety pattern for auto-approved coding agents


### New in Agent Builder: all new agent chat, file uploads + tool registry

- **ID:** `lc-r-new-in-agent-builder-all-new-agent-chat-file-uploads-tool-registry`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/new-in-agent-builder-all-new-agent-chat-file-uploads-tool-registry
- **Date:** 2026-02-18
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Join us for Interrupt: The Agent Conference

- **ID:** `lc-r-join-us-for-interrupt-the-agent-conference`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/join-us-for-interrupt-the-agent-conference
- **Date:** 2026-02-12
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Kimi Agent (Rust)

- **ID:** `mn-r-kimi-agent-rs`
- **Company:** Moonshot (Kimi)
- **Link:** https://github.com/MoonshotAI/kimi-agent-rs
- **Date:** 2026-02-06
- **Authors:** Moonshot AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Making agent-friendly pages with content negotiation

- **ID:** `vcl-e-making-agent-friendly-pages-with-content-negotiation`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/making-agent-friendly-pages-with-content-negotiation
- **Date:** 2026-02-03
- **Authors:** Zach Cowan|Mitul Shah
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- Vercel shipped content negotiation on blog/changelog so agents requesting Accept: text/markdown receive clean markdown instead of full HTML
- argues HTML bloat (nav, CSS, JS bundles) wastes agent context window and makes fetches expensive
- walks through Next.js implementation and markdown sitemaps for agent discovery
- positions this as a pattern for 'agent-friendly' web content
- context-engineering/harness technique for serving content to LLM consumers.


### Deploy agents instantly with Agent Builder templates

- **ID:** `lc-r-introducing-agent-builder-template-library`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/introducing-agent-builder-template-library
- **Date:** 2026-01-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=L/A=H (priority 5.3)

_Summary pending — see link for details._


### From Traces to Insights: Understanding Agent Behavior at Scale

- **ID:** `lc-r-from-traces-to-insights-understanding-agent-behavior-at-scale`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/from-traces-to-insights-understanding-agent-behavior-at-scale
- **Date:** 2026-01-20
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Now GA: LangSmith Agent Builder

- **ID:** `lc-r-langsmith-agent-builder-generally-available`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langsmith-agent-builder-generally-available
- **Date:** 2026-01-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Sakana AI Agent Wins AtCoder Heuristic Contest (First AI to Place 1st)

- **ID:** `sk-r-ahc058`
- **Company:** Sakana AI
- **Link:** https://sakana.ai/ahc058/
- **Date:** 2026-01-05
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### We removed 80% of our agent’s tools

- **ID:** `vcl-e-we-removed-80-percent-of-our-agents-tools`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools
- **Date:** 2025-12-22
- **Authors:** Andrew Qu
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- Vercel's internal text-to-SQL agent d0 was rebuilt by stripping most specialized tools and replacing them with a single bash-execution tool (a file-system agent pattern using grep/cat/ls)
- success rate went from 80% to 100% with fewer steps and tokens
- thesis: simpler tool surfaces let Claude 'figure things out' better than hand-crafted guardrails
- removes pre-filtering, option-constraining, validation wrappers that were over-engineered
- strong design-pattern evidence that minimalism beats elaborate scaffolding for capable models.


### Introducing Polly: Your AI Agent Engineer

- **ID:** `lc-r-introducing-polly-your-ai-agent-engineer`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/introducing-polly-your-ai-agent-engineer
- **Date:** 2025-12-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Agent Engineering: A New Discipline

- **ID:** `lc-r-agent-engineering-a-new-discipline`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/agent-engineering-a-new-discipline
- **Date:** 2025-12-09
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Vercel Agent can now run AI investigations

- **ID:** `vcl-e-vercel-agent-can-now-run-ai-investigations`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/vercel-agent-can-now-run-ai-investigations
- **Date:** 2025-10-31
- **Authors:** Malavika Tadeusz|Liz Hurder
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

**Summary:**

- Launches Vercel Agent Investigations in Public Beta at Ship AI, adding incident-response capability to the existing code-review agent
- agent auto-detects issues, performs root-cause analysis, and produces actionable remediation plans combining anomaly alerts with investigations
- framed as reimagining incident response for the agentic age and cutting engineering time spent on alert triage
- product/enterprise-agent launch post.


### LangChain raises $125M to build the platform for agent engineering

- **ID:** `lc-r-series-b`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/series-b
- **Date:** 2025-10-20
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Securing your agents with authentication and authorization

- **ID:** `lc-r-agent-authorization-explainer`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/agent-authorization-explainer
- **Date:** 2025-10-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Accelerating Qwen3-8B Agent on Intel® Core™ Ultra with Depth-Pruned Draft Models

- **ID:** `hf-r-intel-qwen3-agent`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/intel-qwen3-agent
- **Date:** 2025-09-29
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Jupyter Agents: training LLMs to reason with notebooks

- **ID:** `hf-r-jupyter-agent-2`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/jupyter-agent-2
- **Date:** 2025-09-10
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Agent Middleware

- **ID:** `lc-r-agent-middleware`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/agent-middleware
- **Date:** 2025-09-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Building LangGraph: Designing an Agent Runtime from first principles

- **ID:** `lc-r-building-langgraph`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/building-langgraph
- **Date:** 2025-09-04
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Why agent infrastructure matters

- **ID:** `lc-r-why-agent-infrastructure`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/why-agent-infrastructure
- **Date:** 2025-07-27
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Qwen3-Coder: Agentic Coding in the World

- **ID:** `qw-r-qwen3-coder`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen3-coder/
- **Date:** 2025-07-22
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### How to Build an Agent

- **ID:** `lc-r-how-to-build-an-agent`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-to-build-an-agent
- **Date:** 2025-07-09
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### The no-nonsense approach to AI agent development

- **ID:** `vcl-e-the-no-nonsense-approach-to-ai-agent-development`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/the-no-nonsense-approach-to-ai-agent-development
- **Date:** 2025-06-04
- **Authors:** Malte Ubl
- **Track:** engineering
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

**Summary:**

- Practical playbook for building narrow, tightly-scoped, domain-specific AI agents
- step 1: prototype the agent manually before writing code, feeding real inputs to an LLM and watching which steps are mechanical vs judgment-heavy
- emphasizes structured inputs (e.g., Tailwind for HTML) over pure natural language
- draws on v0.dev experience where scope-narrowing beat waiting for better models
- patterns-focused guide for agent design.


### Why do I need LangGraph Platform for agent deployment?

- **ID:** `lc-r-why-langgraph-platform`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/why-langgraph-platform
- **Date:** 2025-05-22
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### How Webtoon Entertainment built agentic workflows with LangGraph to scale story understanding

- **ID:** `lc-r-customers-webtoon`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-webtoon
- **Date:** 2025-05-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Recap of Interrupt 2025: The AI Agent Conference by LangChain

- **ID:** `lc-r-interrupt-2025-recap`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/interrupt-2025-recap
- **Date:** 2025-05-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### How Outshift by Cisco achieved a 10x productivity boost with their Agentic AI Platform Engineer

- **ID:** `lc-r-cisco-outshift`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/cisco-outshift
- **Date:** 2025-05-04
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### How Harmonic built an investment agent with LangGraph and LangSmith— so VCs can focus on founders

- **ID:** `lc-r-customers-harmonic`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-harmonic
- **Date:** 2025-04-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### AI Agent Latency 101: How do I speed up my AI agent?

- **ID:** `lc-r-how-do-i-speed-up-my-agent`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-do-i-speed-up-my-agent
- **Date:** 2025-03-15
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Empowering product development with an agentic workflow

- **ID:** `mt-r-agentic-workflows-from-meetings-to-dev-tickets`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/agentic-workflows-from-meetings-to-dev-tickets/
- **Date:** 2025-03-04
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### The AI Agent Hype Is Real – But Many Are Still Just Glorified If-Else Statements

- **ID:** `a21-r-ai-agent`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/ai-agent/
- **Date:** 2025-02-25
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### Beyond RAG: Implementing Agent Search with LangGraph for Smarter Knowledge Retrieval

- **ID:** `lc-r-beyond-rag-implementing-agent-search-with-langgraph-for-smarter-knowledge-retrieval`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/beyond-rag-implementing-agent-search-with-langgraph-for-smarter-knowledge-retrieval
- **Date:** 2025-02-22
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=M/A=M (priority 5.5)

_Summary pending — see link for details._


### LangMem SDK for agent long-term memory

- **ID:** `lc-r-langmem-sdk-launch`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langmem-sdk-launch
- **Date:** 2025-02-18
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Benchmarking Single Agent Performance

- **ID:** `lc-r-react-agent-benchmarking`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/react-agent-benchmarking
- **Date:** 2025-02-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Introducing Interrupt: The AI Agent Conference by LangChain

- **ID:** `lc-r-introducing-interrupt-langchain-conference`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/introducing-interrupt-langchain-conference
- **Date:** 2025-02-03
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### How Captide is redefining equity research with agentic workflows running on LangGraph Platform

- **ID:** `lc-r-how-captide-is-redefining-equity-research-with-agentic-workflows-built-on-langgraph-and-langsmith`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-captide-is-redefining-equity-research-with-agentic-workflows-built-on-langgraph-and-langsmith
- **Date:** 2025-01-20
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Agent Protocol: Interoperability for LLM agents

- **ID:** `lc-r-agent-protocol-interoperability-for-llm-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/agent-protocol-interoperability-for-llm-agents
- **Date:** 2024-11-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Composio’s SWE agent advances open-source on SweBench with a 48.6% score using LangGraph and LangSmith

- **ID:** `lc-r-composio-swekit`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/composio-swekit
- **Date:** 2024-11-11
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LangGraph Platform in beta: New deployment options for scalable agent infrastructure

- **ID:** `lc-r-langgraph-platform-announce`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langgraph-platform-announce
- **Date:** 2024-10-31
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Pushing LangSmith to new limits with Replit Agent's complex workflows

- **ID:** `lc-r-customers-replit`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-replit
- **Date:** 2024-09-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Building a Data Visualization Agent with LangGraph Cloud

- **ID:** `lc-r-data-viz-agent`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/data-viz-agent
- **Date:** 2024-09-12
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### How Podium optimized agent behavior and reduced engineering intervention by 90% with LangSmith

- **ID:** `lc-r-customers-podium`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-podium
- **Date:** 2024-08-15
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LangGraph Studio: The first agent IDE

- **ID:** `lc-r-langgraph-studio-the-first-agent-ide`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langgraph-studio-the-first-agent-ide
- **Date:** 2024-08-01
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Why you should outsource your agentic infrastructure, but own your cognitive architecture

- **ID:** `lc-r-why-you-should-outsource-your-agentic-infrastructure-but-own-your-cognitive-architecture`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/why-you-should-outsource-your-agentic-infrastructure-but-own-your-cognitive-architecture
- **Date:** 2024-07-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Jockey: A Conversational Video Agent Powered by Twelve Labs APIs and LangGraph

- **ID:** `lc-r-jockey-twelvelabs-langgraph`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/jockey-twelvelabs-langgraph
- **Date:** 2024-07-03
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### What is an AI agent?

- **ID:** `lc-r-what-is-an-agent`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/what-is-an-agent
- **Date:** 2024-06-28
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Generalizing an LLM from 8k to 1M Context using Qwen-Agent

- **ID:** `qw-r-qwen-agent-2405`
- **Company:** Qwen (Alibaba)
- **Link:** https://qwenlm.github.io/blog/qwen-agent-2405/
- **Date:** 2024-06-06
- **Authors:** Qwen Team
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Jack of All Trades, Master of Some, a Multi-Purpose Transformer Agent

- **ID:** `hf-r-jat`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/jat
- **Date:** 2024-04-22
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Practices for Governing Agentic AI Systems

- **ID:** `oai-r-practices-for-governing-agentic-ai-systems`
- **Company:** OpenAI
- **Link:** https://openai.com/index/practices-for-governing-agentic-ai-systems/
- **Date:** 2024-02-14
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

**Summary:**

- White paper on governance practices for agentic AI systems
- Defines agentic systems and lifecycle parties (developers, deployers, users, third parties)
- Proposes baseline safety/responsibility practices per party
- Discusses indirect societal impacts from wide-scale agent adoption
- Accompanied by an agentic AI research grant program
- Matters as early governance framework specific to agents.


### Self-Reflective RAG with LangGraph

- **ID:** `lc-r-agentic-rag-with-langgraph`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/agentic-rag-with-langgraph
- **Date:** 2024-02-07
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### LLMs accelerate Adyen's support team through smart-ticket routing and support agent copilot

- **ID:** `lc-r-llms-accelerate-adyens-support-team-through-smart-ticket-routing-and-support-agent-copilot`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/llms-accelerate-adyens-support-team-through-smart-ticket-routing-and-support-agent-copilot
- **Date:** 2023-11-28
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### How to design an Agent for Production

- **ID:** `lc-r-how-to-design-an-agent-for-production`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-to-design-an-agent-for-production
- **Date:** 2023-10-15
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Unleashing the power of AI Collaboration with Parallelized LLM Agent Actor Trees

- **ID:** `lc-r-unleashing-the-power-of-ai-collaboration-with-parallelized-llm-agent-actor-trees`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/unleashing-the-power-of-ai-collaboration-with-parallelized-llm-agent-actor-trees
- **Date:** 2023-04-28
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Autonomous Agents & Agent Simulations

- **ID:** `lc-r-agents-round`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/agents-round
- **Date:** 2023-04-18
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### What Makes a Dialog Agent Useful?

- **ID:** `hf-r-dialog-agents`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/dialog-agents
- **Date:** 2023-01-24
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Learning policy representations in multiagent systems

- **ID:** `oai-r-learning-policy-representations-in-multiagent-systems`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-policy-representations-in-multiagent-systems/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** position-policy
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

**Summary:**

- Proposes unsupervised representation learning framework for modeling agents in multiagent systems
- Casts agent modeling as representation learning using imitation-learning-inspired and agent-identification objectives
- Validates on high-dim competitive continuous control and cooperative communication envs
- Supports downstream supervised prediction, clustering, and policy optimization
- Matters for opponent modeling and multi-agent RL.


### Introducing Pytorch Native Agentic Stack

- **ID:** `meta-r-introducing-pytorch-native-agentic-stack`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/introducing-pytorch-native-agentic-stack/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Practical Ai Agent Security

- **ID:** `meta-r-practical-ai-agent-security`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/practical-ai-agent-security/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### A Generalist Agent

- **ID:** `dm-r-a-generalist-agent`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/a-generalist-agent/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Discovering When An Agent Is Present In A System

- **ID:** `dm-r-discovering-when-an-agent-is-present-in-a-system`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/discovering-when-an-agent-is-present-in-a-system/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Introducing Codemender An Ai Agent For Code Security

- **ID:** `dm-r-introducing-codemender-an-ai-agent-for-code-security`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Safety First Ai For Autonomous Data Centre Cooling And Industrial Control

- **ID:** `dm-r-safety-first-ai-for-autonomous-data-centre-cooling-and-industrial-control`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/safety-first-ai-for-autonomous-data-centre-cooling-and-industrial-control/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Sima Generalist Ai Agent For 3D Virtual Environments

- **ID:** `dm-r-sima-generalist-ai-agent-for-3d-virtual-environments`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/sima-generalist-ai-agent-for-3d-virtual-environments/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=L (priority 3.3)

_Summary pending — see link for details._


### Understanding Agent Cooperation

- **ID:** `dm-r-understanding-agent-cooperation`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/understanding-agent-cooperation/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

_Summary pending — see link for details._


## <a id="fallback-agents"></a>Other agentic systems

_59 posts_

### Deep Agents Deploy: an open alternative to Claude Managed Agents

- **ID:** `lc-r-deep-agents-deploy-an-open-alternative-to-claude-managed-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/deep-agents-deploy-an-open-alternative-to-claude-managed-agents
- **Date:** 2026-04-09
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Previewing Interrupt 2026: Agents at Enterprise Scale

- **ID:** `lc-r-previewing-interrupt-2026-agents-at-enterprise-scale`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/previewing-interrupt-2026-agents-at-enterprise-scale
- **Date:** 2026-04-09
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Deep Agents v0.5

- **ID:** `lc-r-deep-agents-v0-5`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/deep-agents-v0-5
- **Date:** 2026-04-07
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Continual learning for AI agents

- **ID:** `lc-r-continual-learning-for-ai-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/continual-learning-for-ai-agents
- **Date:** 2026-04-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How My Agents Self-Heal in Production

- **ID:** `lc-r-how-my-agents-self-heal-in-production`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-my-agents-self-heal-in-production
- **Date:** 2026-04-03
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### How Moda Builds Production-Grade AI Design Agents with Deep Agents

- **ID:** `lc-r-how-moda-builds-production-grade-ai-design-agents-with-deep-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-moda-builds-production-grade-ai-design-agents-with-deep-agents
- **Date:** 2026-03-24
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Coding Agents Are Reshaping Engineering, Product and Design

- **ID:** `lc-r-how-coding-agents-are-reshaping-engineering-product-and-design`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/how-coding-agents-are-reshaping-engineering-product-and-design
- **Date:** 2026-03-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### The two patterns by which agents connect sandboxes

- **ID:** `lc-r-the-two-patterns-by-which-agents-connect-sandboxes`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/the-two-patterns-by-which-agents-connect-sandboxes
- **Date:** 2026-02-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Towards self-driving codebases

- **ID:** `cur-r-self-driving-codebases`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/self-driving-codebases
- **Date:** 2026-02-05
- **Authors:** Wilson Lin
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=M/A=M (priority 7.7)
- **Techniques:** coding-agents

**Summary:**

- Cursor research on scaling long-running autonomous coding agents
- Built harness that orchestrates thousands of agents
- Ran continuously for a week producing the vast majority of commits to an internal browser project
- Thousands of agents collaboratively produced mostly runnable code with minimal human intervention
- Discusses harness design overcoming Opus 4.5 failure modes (loss of track, premature declarations of success)
- Matters as state-of-the-art long-horizon autonomous coding demonstration


### Context Management for Deep Agents

- **ID:** `lc-r-context-management-for-deepagents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/context-management-for-deepagents
- **Date:** 2026-01-28
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### NVIDIA brings agents to life with DGX Spark and Reachy Mini

- **ID:** `hf-r-nvidia-reachy-mini`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/nvidia-reachy-mini
- **Date:** 2026-01-05
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Fastweb + Vodafone: Transforming Customer Experience with AI Agents using LangGraph and LangSmith

- **ID:** `lc-r-customers-vodafone-italy`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-vodafone-italy
- **Date:** 2025-12-16
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Debugging Deep Agents with LangSmith

- **ID:** `lc-r-debugging-deep-agents-with-langsmith`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/debugging-deep-agents-with-langsmith
- **Date:** 2025-12-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Evaluating Deep Agents CLI on Terminal Bench 2.0

- **ID:** `lc-r-evaluating-deepagents-cli-on-terminal-bench-2-0`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/evaluating-deepagents-cli-on-terminal-bench-2-0
- **Date:** 2025-12-05
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Evaluating Deep Agents: Our Learnings

- **ID:** `lc-r-evaluating-deep-agents-our-learnings`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/evaluating-deep-agents-our-learnings
- **Date:** 2025-12-03
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Using skills with Deep Agents

- **ID:** `lc-r-using-skills-with-deep-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/using-skills-with-deep-agents
- **Date:** 2025-11-25
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Execute Code with Sandboxes for Deep Agents

- **ID:** `lc-r-execute-code-with-sandboxes-for-deepagents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/execute-code-with-sandboxes-for-deepagents
- **Date:** 2025-11-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Introducing Deep Agents CLI

- **ID:** `lc-r-introducing-deepagents-cli`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/introducing-deepagents-cli
- **Date:** 2025-10-30
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Doubling down on Deep Agents

- **ID:** `lc-r-doubling-down-on-deepagents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/doubling-down-on-deepagents
- **Date:** 2025-10-28
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Building State-of-the-Art Enterprise Agents 90x Cheaper with Automated Prompt Optimization

- **ID:** `dbx-r-building-state-art-enterprise-agents-90x-cheaper-automated-prompt-optimization`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/building-state-art-enterprise-agents-90x-cheaper-automated-prompt-optimization
- **Date:** 2025-09-24
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=M/N=M/A=M (priority 6.6)

**Summary:**

- Databricks Agent Bricks uses automated prompt optimization (GEPA technique from Databricks/UC Berkeley) to push open-source gpt-oss-120b past Claude Sonnet 4/Opus 4.1 by ~3% while being 20x-90x cheaper to serve
- Same technique lifts Claude Opus 4.1 and Sonnet 4 baselines by 6-7%
- Matches or beats SFT while reducing serving costs 20%, and composes with SFT for further gains
- Benchmarks focused on enterprise information extraction
- Matters for building high-quality enterprise agents without fine-tuning


### Deep Agents

- **ID:** `lc-r-deep-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/deep-agents
- **Date:** 2025-07-30
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### How Captide agents running on LangGraph Platform compress investment research from days to seconds

- **ID:** `lc-r-captide`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/captide
- **Date:** 2025-06-24
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Build AI agents with the Mistral Agents API

- **ID:** `mt-r-agents-api`
- **Company:** Mistral AI
- **Link:** https://mistral.ai/news/agents-api/
- **Date:** 2025-05-27
- **Authors:** Mistral AI
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangGraph Platform is now Generally Available: Deploy & manage long-running, stateful Agents

- **ID:** `lc-r-langgraph-platform-ga`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langgraph-platform-ga
- **Date:** 2025-05-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### LangGraph 0.3 Release: Prebuilt Agents

- **ID:** `lc-r-langgraph-0-3-release-prebuilt-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langgraph-0-3-release-prebuilt-agents
- **Date:** 2025-02-27
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Introducing ambient agents

- **ID:** `lc-r-introducing-ambient-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/introducing-ambient-agents
- **Date:** 2025-01-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Top 5 LangGraph Agents in Production 2024

- **ID:** `lc-r-top-5-langgraph-agents-in-production-2024`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/top-5-langgraph-agents-in-production-2024
- **Date:** 2024-12-31
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=H (priority 6.4)

_Summary pending — see link for details._


### Making it easier to build human-in-the-loop agents with interrupt

- **ID:** `lc-r-making-it-easier-to-build-human-in-the-loop-agents-with-interrupt`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/making-it-easier-to-build-human-in-the-loop-agents-with-interrupt
- **Date:** 2024-12-14
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Airtop built web-automation for AI agents powered by the LangChain ecosystem

- **ID:** `lc-r-customers-airtop`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-airtop
- **Date:** 2024-11-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Memory for agents

- **ID:** `lc-r-memory-for-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/memory-for-agents
- **Date:** 2024-10-19
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Rexera’s AI agents drive quality control with LangGraph

- **ID:** `lc-r-customers-rexera`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-rexera
- **Date:** 2024-10-09
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Unify Launches Agents for Account Qualification using LangGraph and LangSmith

- **ID:** `lc-r-unify-launches-agents-for-account-qualification-using-langgraph-and-langsmith`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/unify-launches-agents-for-account-qualification-using-langgraph-and-langsmith
- **Date:** 2024-10-08
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Introducing Assistant Editor for configuring agents in LangGraph Studio

- **ID:** `lc-r-asssistant-editor`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/asssistant-editor
- **Date:** 2024-09-25
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Build stateful conversational AI agents with LangGraph and assistant-ui

- **ID:** `lc-r-assistant-ui`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/assistant-ui
- **Date:** 2024-09-11
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### How Paradigm runs and monitors thousands of agents in parallel with LangChain and LangSmith

- **ID:** `lc-r-customers-paradigm`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/customers-paradigm
- **Date:** 2024-09-04
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### UX for Agents, Part 3: Spreadsheet, Generative, and Collaborative UI/UX

- **ID:** `lc-r-ux-for-agents-part-3`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/ux-for-agents-part-3
- **Date:** 2024-08-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### UX for Agents, Part 2: Ambient

- **ID:** `lc-r-ux-for-agents-part-2-ambient`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/ux-for-agents-part-2-ambient
- **Date:** 2024-08-02
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### UX for Agents, Part 1: Chat

- **ID:** `lc-r-ux-for-agents-part-1-chat-2`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/ux-for-agents-part-1-chat-2
- **Date:** 2024-07-26
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Planning for Agents

- **ID:** `lc-r-planning-for-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/planning-for-agents
- **Date:** 2024-07-20
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Announcing LangGraph v0.1 & LangGraph Cloud: Running agents at scale, reliably

- **ID:** `lc-r-langgraph-cloud`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/langgraph-cloud
- **Date:** 2024-06-27
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=L/N=L/A=H (priority 5.3)

_Summary pending — see link for details._


### Reflection Agents

- **ID:** `lc-r-reflection-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/reflection-agents
- **Date:** 2024-02-21
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### JSON agents with Ollama & LangChain

- **ID:** `lc-r-json-based-agents-with-ollama-and-langchain`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/json-based-agents-with-ollama-and-langchain
- **Date:** 2024-02-20
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Plan-and-Execute Agents

- **ID:** `lc-r-planning-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/planning-agents
- **Date:** 2024-02-13
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### BCG X Releases AgentKit, a Full-Stack Starter Kit for Building Constrained Agents

- **ID:** `lc-r-bcg-x-releases-agentkit-a-full-stack-starter-kit-for-building-constrained-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/bcg-x-releases-agentkit-a-full-stack-starter-kit-for-building-constrained-agents
- **Date:** 2024-02-12
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Yeager.ai x LangChain: Exploring GenWorlds a Framework for Coordinating AI Agents

- **ID:** `lc-r-exploring-genworlds`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/exploring-genworlds
- **Date:** 2023-08-04
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Conversational Retrieval Agents

- **ID:** `lc-r-conversational-retrieval-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/conversational-retrieval-agents
- **Date:** 2023-08-03
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Plan-and-Execute Agents

- **ID:** `lc-r-plan-and-execute-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/plan-and-execute-agents
- **Date:** 2023-05-10
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Gradio & LLM Agents

- **ID:** `lc-r-gradio-llm-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/gradio-llm-agents
- **Date:** 2023-04-23
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Custom Agents

- **ID:** `lc-r-custom-agents`
- **Company:** LangChain
- **Link:** https://www.langchain.com/blog/custom-agents
- **Date:** 2023-04-03
- **Authors:** LangChain
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=L/A=M (priority 4.3)

_Summary pending — see link for details._


### Introducing ⚔️ AI vs. AI ⚔️ a deep reinforcement learning multi-agents competition system

- **ID:** `hf-r-aivsai`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/aivsai
- **Date:** 2023-02-07
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Learning to model other minds

- **ID:** `oai-r-learning-to-model-other-minds`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-to-model-other-minds/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

**Summary:**

- Introduces LOLA (Learning with Opponent-Learning Awareness) where each agent accounts for other agents' learning updates
- Discovers tit-for-tat in iterated prisoner's dilemma and solves coin game where independent PPO fails
- Differentiates through the anticipated learning step of opponents
- Can work with opponent modeling from observed trajectories
- Matters as early theory-of-mind-like multi-agent RL algorithm.


### Learning with opponent-learning awareness

- **ID:** `oai-r-learning-with-opponent-learning-awareness`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-with-opponent-learning-awareness/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** M — L=H/N=L/A=M (priority 6.5)

**Summary:**

- Companion paper to 'learning to model other minds': LOLA algorithm for multi-agent RL
- Each agent shapes the anticipated learning of its peers via a second-order update term
- Leads to tit-for-tat cooperation in iterated prisoner's dilemma and Nash in matching pennies
- Robust to exploitation by higher-order gradient methods
- Matters as a seminal opponent-aware multi-agent RL method.


### Learning to cooperate, compete, and communicate

- **ID:** `oai-r-learning-to-cooperate-compete-and-communicate`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-to-cooperate-compete-and-communicate/
- **Date:** 2022-10-19
- **Track:** research
- **Contribution type:** empirical-study
- **Signal:** H — L=H/N=L/A=H (priority 7.5)

**Summary:**

- Introduces MADDPG, centralized-training / decentralized-execution actor-critic for multi-agent RL
- Each agent's critic accesses peers' observations and actions during training
- Works across cooperative and competitive tasks including adversarial ones
- Outperforms DDPG on all tested multi-agent tasks
- Matters as a foundational multi-agent RL algorithm and particle-envs benchmark release.


### Introducing Snowball Fight ☃️, our first ML-Agents environment

- **ID:** `hf-r-snowball-fight`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/snowball-fight
- **Date:** 2021-12-02
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** M — L=M/N=L/A=M (priority 5.4)

_Summary pending — see link for details._


### Meta Fair Updates Agents Robustness Safety Architecture

- **ID:** `meta-r-meta-fair-updates-agents-robustness-safety-architecture`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/meta-fair-updates-agents-robustness-safety-architecture/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

_Summary pending — see link for details._


### Evaluating Multimodal Interactive Agents

- **ID:** `dm-r-evaluating-multimodal-interactive-agents`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/evaluating-multimodal-interactive-agents/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

_Summary pending — see link for details._


### Navigating With Grid Like Representations In Artificial Agents

- **ID:** `dm-r-navigating-with-grid-like-representations-in-artificial-agents`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/navigating-with-grid-like-representations-in-artificial-agents/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

_Summary pending — see link for details._


### Spurious Normativity Enhances Learning Of Compliance And Enforcement Behavior In Artificial Agents

- **ID:** `dm-r-spurious-normativity-enhances-learning-of-compliance-and-enforcement-behavior-in-artificial-agents`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/spurious-normativity-enhances-learning-of-compliance-and-enforcement-behavior-in-artificial-agents/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=M/N=L/A=L (priority 4.4)

_Summary pending — see link for details._


### Build Long Context Ai Apps With Jamba Powering The Future Of Ai Agents

- **ID:** `a21-r-build-long-context-ai-apps-with-jamba-powering-the-future-of-ai-agents`
- **Company:** AI21 Labs
- **Link:** https://www.ai21.com/blog/build-long-context-ai-apps-with-jamba-powering-the-future-of-ai-agents/
- **Date:** _date unknown_
- **Authors:** AI21 Labs
- **Track:** research
- **Contribution type:** _(uncategorized)_
- **Signal:** L — L=L/N=M/A=L (priority 4.5)

_Summary pending — see link for details._

