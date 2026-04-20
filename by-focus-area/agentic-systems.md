# Agentic Systems

Agents, tool use, multi-agent, computer use, coding agents, agent benchmarks, agent traces, autonomous workflows.

**Post count:** 103

**Contributors:**

- Hugging Face: 22
- Google DeepMind: 19
- Meta AI / FAIR: 16
- OpenAI: 11
- Vercel: 9
- Anthropic: 8
- Cognition: 6
- Databricks Mosaic AI: 5
- Cursor: 5
- Google Research: 1
- Allen Institute for AI: 1

**Subcategories:**

- [Coding agents](#coding-agents) (10)
- [Multi-agent orchestration](#multi-agent-orchestration) (9)
- [Computer use & browser use](#computer-use-and-browser-use) (4)
- [Tool use & function calling](#tool-use-and-function-calling) (3)
- [Enterprise agents](#enterprise-agents) (8)
- [Embodied agents & simulation](#embodied-and-simulation) (12)
- [Game-playing & RL agents](#game-and-rl-agents) (15)
- [Dialogue & conversational agents](#dialogue-and-conversational-agents) (3)
- [Agent frameworks & tooling](#agent-frameworks-and-tooling) (10)
- [Agent research applications (scientific, robotic)](#agent-research-applications) (8)
- [Agent traces & observability](#agent-traces-and-observability) (1)
- [Agent design & patterns / opinion pieces](#agent-design-and-patterns) (14)
- [General agentic systems](#agents-general) (3)

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
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Custom Kernels for All from Codex and Claude

- **ID:** `hf-r-custom-cuda-kernels-agent-skills`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/custom-cuda-kernels-agent-skills
- **Date:** 2026-02-13
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Closing the Agent Loop: Devin Autofixes Review Comments

- **ID:** `cog-e-closing-the-agent-loop-devin-autofixes-review-comments`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/closing-the-agent-loop-devin-autofixes-review-comments
- **Date:** 2026-02-10
- **Track:** engineering
- **Contribution type:** empirical-study
- **Techniques:** coding-agents

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

**Summary:**

- Cursor research on scaling long-running autonomous coding agents
- Built harness that orchestrates thousands of agents
- Ran continuously for a week producing the vast majority of commits to an internal browser project
- Thousands of agents collaboratively produced mostly runnable code with minimal human intervention
- Discusses harness design overcoming Opus 4.5 failure modes (loss of track, premature declarations of success)
- Matters as state-of-the-art long-horizon autonomous coding demonstration


### How we made v0 an effective coding agent

- **ID:** `vcl-a-how-we-made-v0-an-effective-coding-agent`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/how-we-made-v0-an-effective-coding-agent
- **Date:** 2026-01-07
- **Authors:** Max Leiter
- **Track:** applied
- **Contribution type:** empirical-study
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Making Claude Code more secure and autonomous with sandboxing

- **ID:** `ant-e-claude-code-sandboxing`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/claude-code-sandboxing
- **Date:** 2025-10-20
- **Track:** engineering
- **Contribution type:** empirical-study
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Rebuilding Devin for Claude Sonnet 4.5: Lessons and Challenges

- **ID:** `cog-e-devin-sonnet-4-5-lessons-and-challenges`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/devin-sonnet-4-5-lessons-and-challenges
- **Date:** 2025-09-29
- **Track:** engineering
- **Contribution type:** retrospective-case-study
- **Techniques:** coding-agents

_Summary pending — see link for details._


### Unrolling the Codex agent loop

- **ID:** `oai-e-unrolling-the-codex-agent-loop`
- **Company:** OpenAI
- **Link:** https://openai.com/index/unrolling-the-codex-agent-loop/
- **Date:** _date unknown_
- **Track:** engineering
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Alphaevolve A Gemini Powered Coding Agent For Designing Advanced Algorithms

- **ID:** `dm-r-alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing Codemender An Ai Agent For Code Security

- **ID:** `dm-r-introducing-codemender-an-ai-agent-for-code-security`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- DeepMind unveils CodeMender, an AI agent that autonomously finds and patches software security vulnerabilities using Gemini Deep Think reasoning
- both reactive (patching new vulns) and proactive (rewriting code to eliminate vuln classes)
- has already upstreamed 72 security fixes to open source, including 4.5M-LOC projects
- equipped with tools for reasoning about code before modifying
- direct coding-agent application focused on security.


## <a id="multi-agent-orchestration"></a>Multi-agent orchestration

_9 posts_

### Speeding up GPU kernels by 38% with a multi-agent system

- **ID:** `cur-r-multi-agent-kernels`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/multi-agent-kernels
- **Date:** 2026-04-14
- **Authors:** Wilson, Sahil, Yuan & Edward
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** coding-agents, multi-agent

_Summary pending — see link for details._


### How we built our multi-agent research system

- **ID:** `ant-e-multi-agent-research-system`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/multi-agent-research-system
- **Date:** 2025-06-13
- **Authors:** Jeremy Hadfield|Barry Zhang|Kenneth Lien|Florian Scholz|Jeremy Fox|Daniel Ford
- **Track:** engineering
- **Contribution type:** retrospective-case-study
- **Techniques:** multi-agent

_Summary pending — see link for details._


### Emergence of grounded compositional language in multi-agent populations

- **ID:** `oai-r-emergence-of-grounded-compositional-language-in-multi-agent-populations`
- **Company:** OpenAI
- **Link:** https://openai.com/index/emergence-of-grounded-compositional-language-in-multi-agent-populations/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** multi-agent

_Summary pending — see link for details._


### Egg A Toolkit For Multi Agent Language Emergence Simulations

- **ID:** `meta-r-egg-a-toolkit-for-multi-agent-language-emergence-simulations`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/egg-a-toolkit-for-multi-agent-language-emergence-simulations/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Using Multi Agent Reinforcement Learning To Improve Collaboration

- **ID:** `meta-r-using-multi-agent-reinforcement-learning-to-improve-collaboration`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/using-multi-agent-reinforcement-learning-to-improve-collaboration/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Alphastar Grandmaster Level In Starcraft Ii Using Multi Agent Reinforcement Learning

- **ID:** `dm-r-alphastar-grandmaster-level-in-starcraft-ii-using-multi-agent-reinforcement-learning`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/alphastar-grandmaster-level-in-starcraft-ii-using-multi-agent-reinforcement-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Emergent Bartering Behaviour In Multi Agent Reinforcement Learning

- **ID:** `dm-r-emergent-bartering-behaviour-in-multi-agent-reinforcement-learning`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/emergent-bartering-behaviour-in-multi-agent-reinforcement-learning/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Game Theory Insights Into Asymmetric Multi Agent Games

- **ID:** `dm-r-game-theory-insights-into-asymmetric-multi-agent-games`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/game-theory-insights-into-asymmetric-multi-agent-games/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Understanding Agent Cooperation

- **ID:** `dm-r-understanding-agent-cooperation`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/understanding-agent-cooperation/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- DeepMind uses deep multi-agent RL to study emergence of cooperation via 'sequential social dilemmas' (repeated Prisoner's-Dilemma-like games with temporal structure)
- shows cooperation vs defection depends on environment structure and agents' cognitive capacity
- aims to illuminate control of complex multi-agent systems (economy, traffic, climate)
- classic multi-agent cooperation research.


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
- **Techniques:** computer-use, coding-agents

_Summary pending — see link for details._


### Mitigating the risk of prompt injections in browser use

- **ID:** `ant-r-prompt-injection-defenses`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/prompt-injection-defenses
- **Date:** 2025-11-24
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Smol2Operator: Post-Training GUI Agents for Computer Use

- **ID:** `hf-r-smol2operator`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/smol2operator
- **Date:** 2025-09-23
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### ScreenEnv: Deploy your full stack Desktop Agent

- **ID:** `hf-r-screenenv`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/screenenv
- **Date:** 2025-07-10
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="tool-use-and-function-calling"></a>Tool use & function calling

_3 posts_

### From model to agent: Equipping the Responses API with a computer environment

- **ID:** `oai-e-equip-responses-api-computer-environment`
- **Company:** OpenAI
- **Link:** https://openai.com/index/equip-responses-api-computer-environment/
- **Date:** 2026-02-13
- **Track:** engineering
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Writing effective tools for AI agents—using AI agents

- **ID:** `ant-e-writing-tools-for-agents`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/writing-tools-for-agents
- **Date:** 2025-09-11
- **Authors:** Zachary Witten|Daniel Jiang|Sami Al-Sheikh|Matt Bell|Maggie Vo)|MCP (Theodora Chu|David Soria Parra|Adam Jones)
- **Track:** engineering
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Tool Use, Unified

- **ID:** `hf-r-unified-tool-use`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/unified-tool-use
- **Date:** 2024-08-12
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="enterprise-agents"></a>Enterprise agents

_8 posts_

### Agentic Reasoning in Practice: Making Sense of Structured and Unstructured Data

- **ID:** `dbx-r-agentic-reasoning-practice-making-sense-structured-and-unstructured-data`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/agentic-reasoning-practice-making-sense-structured-and-unstructured-data
- **Date:** 2026-04-14
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Memory Scaling for AI Agents

- **ID:** `dbx-r-memory-scaling-ai-agents`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/memory-scaling-ai-agents
- **Date:** 2026-04-10
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Securing our codebase with autonomous agents

- **ID:** `cur-e-security-agents`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/security-agents
- **Date:** 2026-03-16
- **Track:** engineering
- **Contribution type:** empirical-study
- **Techniques:** coding-agents

**Summary:**

- Cursor releases four Cursor Automations templates for security agents that continuously identify and repair vulnerabilities
- PR velocity grew 5x over 9 months, outpacing static-analysis/code-ownership approaches
- Agents use webhooks, GitHub PR responses, codebase monitoring plus a custom security MCP tool (serverless Lambda) for persistent data, dedup, and observability
- Matters as applied autonomous security-agent blueprint for engineering teams


### Meet KARL: A Faster Agent for Enterprise Knowledge, powered by custom RL

- **ID:** `dbx-r-meet-karl-faster-agent-enterprise-knowledge-powered-custom-rl`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/meet-karl-faster-agent-enterprise-knowledge-powered-custom-rl
- **Date:** 2026-03-05
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Inside OpenAI’s in-house data agent

- **ID:** `oai-e-inside-our-in-house-data-agent`
- **Company:** OpenAI
- **Link:** https://openai.com/index/inside-our-in-house-data-agent/
- **Date:** 2026-01-23
- **Track:** engineering
- **Contribution type:** retrospective-case-study

_Summary pending — see link for details._


### Instructed Retriever: Unlocking System-Level Reasoning in Search Agents

- **ID:** `dbx-r-instructed-retriever-unlocking-system-level-reasoning-search-agents`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/instructed-retriever-unlocking-system-level-reasoning-search-agents
- **Date:** 2026-01-06
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** retrieval-augmentation

_Summary pending — see link for details._


### Vercel Agent can now run AI investigations

- **ID:** `vcl-e-vercel-agent-can-now-run-ai-investigations`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/vercel-agent-can-now-run-ai-investigations
- **Date:** 2025-10-31
- **Authors:** Malavika Tadeusz|Liz Hurder
- **Track:** engineering
- **Contribution type:** empirical-study

**Summary:**

- Launches Vercel Agent Investigations in Public Beta at Ship AI, adding incident-response capability to the existing code-review agent
- agent auto-detects issues, performs root-cause analysis, and produces actionable remediation plans combining anomaly alerts with investigations
- framed as reimagining incident response for the agentic age and cutting engineering time spent on alert triage
- product/enterprise-agent launch post.


### Building State-of-the-Art Enterprise Agents 90x Cheaper with Automated Prompt Optimization

- **ID:** `dbx-r-building-state-art-enterprise-agents-90x-cheaper-automated-prompt-optimization`
- **Company:** Databricks Mosaic AI
- **Link:** https://www.databricks.com/blog/building-state-art-enterprise-agents-90x-cheaper-automated-prompt-optimization
- **Date:** 2025-09-24
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Databricks Agent Bricks uses automated prompt optimization (GEPA technique from Databricks/UC Berkeley) to push open-source gpt-oss-120b past Claude Sonnet 4/Opus 4.1 by ~3% while being 20x-90x cheaper to serve
- Same technique lifts Claude Opus 4.1 and Sonnet 4 baselines by 6-7%
- Matches or beats SFT while reducing serving costs 20%, and composes with SFT for further gains
- Benchmarks focused on enterprise information extraction
- Matters for building high-quality enterprise agents without fine-tuning


## <a id="embodied-and-simulation"></a>Embodied agents & simulation

_12 posts_

### NVIDIA brings agents to life with DGX Spark and Reachy Mini

- **ID:** `hf-r-nvidia-reachy-mini`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/nvidia-reachy-mini
- **Date:** 2026-01-05
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- HuggingFace + NVIDIA CES 2026 demo: bring a personal AI agent to life on DGX Spark running Reachy Mini robot
- stack uses NVIDIA Nemotron 3 Nano (reasoning), Nemotron Nano 2 VL (vision), ElevenLabs TTS, running locally with ~65GB+28GB disk
- step-by-step replication guide for an embodied 'desk R2D2' you can talk to
- frames NVIDIA's open models (Nemotron, Isaac GR00T N1.6 VLA, Cosmos world models) as building blocks for embodied agents.


### 2021 Habitat Challenge Launches To Advance Embodied Ai Research

- **ID:** `meta-r-2021-habitat-challenge-launches-to-advance-embodied-ai-research`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/2021-habitat-challenge-launches-to-advance-embodied-ai-research/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Ai Habitat State Of The Art Simulation Platform Adds Object Interactivity

- **ID:** `meta-r-ai-habitat-state-of-the-art-simulation-platform-adds-object-interactivity`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/ai-habitat-state-of-the-art-simulation-platform-adds-object-interactivity/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Egomimic Project Aria Georgia Tech Ego4D Robotics Embodied Ai

- **ID:** `meta-r-egomimic-project-aria-georgia-tech-ego4d-robotics-embodied-ai`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/egomimic-project-aria-georgia-tech-ego4d-robotics-embodied-ai/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Embodied Question Answering A Goal Driven Approach To Autonomous Agents

- **ID:** `meta-r-embodied-question-answering-a-goal-driven-approach-to-autonomous-agents`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/embodied-question-answering-a-goal-driven-approach-to-autonomous-agents/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Habitat 20 Training Home Assistant Robots With Faster Simulation And New Benchmarks

- **ID:** `meta-r-habitat-20-training-home-assistant-robots-with-faster-simulation-and-new-benchmarks`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/habitat-20-training-home-assistant-robots-with-faster-simulation-and-new-benchmarks/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Habitat 3 Socially Intelligent Robots Siro

- **ID:** `meta-r-habitat-3-socially-intelligent-robots-siro`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/habitat-3-socially-intelligent-robots-siro/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing The Habitat Matterport 3D Research Data Set For Training Embodied Ai

- **ID:** `meta-r-introducing-the-habitat-matterport-3d-research-data-set-for-training-embodied-ai`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/introducing-the-habitat-matterport-3d-research-data-set-for-training-embodied-ai/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### New Milestones In Embodied Ai

- **ID:** `meta-r-new-milestones-in-embodied-ai`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/new-milestones-in-embodied-ai/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Open Sourcing Ai Habitat A Simulation Platform For Embodied Ai Research

- **ID:** `meta-r-open-sourcing-ai-habitat-a-simulation-platform-for-embodied-ai-research`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/open-sourcing-ai-habitat-a-simulation-platform-for-embodied-ai-research/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Robocat A Self Improving Robotic Agent

- **ID:** `dm-r-robocat-a-self-improving-robotic-agent`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/robocat-a-self-improving-robotic-agent/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Sima Generalist Ai Agent For 3D Virtual Environments

- **ID:** `dm-r-sima-generalist-ai-agent-for-3d-virtual-environments`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/sima-generalist-ai-agent-for-3d-virtual-environments/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- DeepMind introduces SIMA (Scalable Instructable Multiworld Agent), a generalist AI agent that follows natural-language instructions across many commercial 3D video games
- partnered with game developers to train on varied games
- focus is not score-maximization but instruction-following across diverse environments, as a path to useful embodied agents
- positions video games as sandboxes for AI-agent research
- embodied/simulation agent work.


## <a id="game-and-rl-agents"></a>Game-playing & RL agents

_15 posts_

### OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments

- **ID:** `hf-r-openenv-turing`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/openenv-turing
- **Date:** 2026-02-12
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Building the Open Agent Ecosystem Together: Introducing OpenEnv

- **ID:** `hf-r-openenv`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/openenv
- **Date:** 2025-10-23
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Gaia2 and ARE: Empowering the community to study agents

- **ID:** `hf-r-gaia2`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/gaia2
- **Date:** 2025-09-22
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing Snowball Fight ☃️, our first ML-Agents environment

- **ID:** `hf-r-snowball-fight`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/snowball-fight
- **Date:** 2021-12-02
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- HF launches its first custom Deep RL environment, Snowball Fight 1v1, built with Unity ML-Agents and playable on Spaces
- announces a broader ecosystem for sharing custom ML-Agents environments, models, and demos on the Hub
- invites community contributions and a Discord
- agent/RL-environment tooling post oriented at hobbyist/game-RL community.


### Learning policy representations in multiagent systems

- **ID:** `oai-r-learning-policy-representations-in-multiagent-systems`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-policy-representations-in-multiagent-systems/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** position-policy

**Summary:**

- Proposes unsupervised representation learning framework for modeling agents in multiagent systems
- Casts agent modeling as representation learning using imitation-learning-inspired and agent-identification objectives
- Validates on high-dim competitive continuous control and cooperative communication envs
- Supports downstream supervised prediction, clustering, and policy optimization
- Matters for opponent modeling and multi-agent RL.


### Learning to model other minds

- **ID:** `oai-r-learning-to-model-other-minds`
- **Company:** OpenAI
- **Link:** https://openai.com/index/learning-to-model-other-minds/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

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
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

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
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- Introduces MADDPG, centralized-training / decentralized-execution actor-critic for multi-agent RL
- Each agent's critic accesses peers' observations and actions during training
- Works across cooperative and competitive tasks including adversarial ones
- Outperforms DDPG on all tested multi-agent tasks
- Matters as a foundational multi-agent RL algorithm and particle-envs benchmark release.


### Droidlet A One Stop Shop For Modularly Building Intelligent Agents

- **ID:** `meta-r-droidlet-a-one-stop-shop-for-modularly-building-intelligent-agents`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/droidlet-a-one-stop-shop-for-modularly-building-intelligent-agents/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Read To Fight Monsters Using Rl To Teach Agents To Generalize To New Settings

- **ID:** `meta-r-read-to-fight-monsters-using-rl-to-teach-agents-to-generalize-to-new-settings`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/read-to-fight-monsters-using-rl-to-teach-agents-to-generalize-to-new-settings/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Training Ai Agents To Solve Unfamiliar Tasks

- **ID:** `meta-r-training-ai-agents-to-solve-unfamiliar-tasks`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/training-ai-agents-to-solve-unfamiliar-tasks/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Agents That Imagine And Plan

- **ID:** `dm-r-agents-that-imagine-and-plan`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/agents-that-imagine-and-plan/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Building Interactive Agents In Video Game Worlds

- **ID:** `dm-r-building-interactive-agents-in-video-game-worlds`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/building-interactive-agents-in-video-game-worlds/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Capture The Flag The Emergence Of Complex Cooperative Agents

- **ID:** `dm-r-capture-the-flag-the-emergence-of-complex-cooperative-agents`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/capture-the-flag-the-emergence-of-complex-cooperative-agents/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Generally Capable Agents Emerge From Open Ended Play

- **ID:** `dm-r-generally-capable-agents-emerge-from-open-ended-play`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/generally-capable-agents-emerge-from-open-ended-play/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

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

_Summary pending — see link for details._


### A Facebook Scale Simulator To Detect Harmful Behaviors

- **ID:** `meta-r-a-facebook-scale-simulator-to-detect-harmful-behaviors`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/a-facebook-scale-simulator-to-detect-harmful-behaviors/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Building Safer Dialogue Agents

- **ID:** `dm-r-building-safer-dialogue-agents`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/building-safer-dialogue-agents/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="agent-frameworks-and-tooling"></a>Agent frameworks & tooling

_10 posts_

### DeepMath: A lightweight math reasoning Agent with smolagents

- **ID:** `hf-r-intel-deepmath`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/intel-deepmath
- **Date:** 2025-12-04
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Back to The Future: Evaluating AI Agents on Predicting Future Events

- **ID:** `hf-r-futurebench`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/futurebench
- **Date:** 2025-07-17
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Trace & Evaluate your Agent with Arize Phoenix

- **ID:** `hf-r-smolagents-phoenix`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/smolagents-phoenix
- **Date:** 2025-02-28
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Open-source DeepResearch – Freeing our search agents

- **ID:** `hf-r-open-deep-research`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/open-deep-research
- **Date:** 2025-02-04
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing smolagents: simple agents that write actions in code.

- **ID:** `hf-r-smolagents`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/smolagents
- **Date:** 2024-12-31
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### License to Call: Introducing Transformers Agents 2.0

- **ID:** `hf-r-agents`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/agents
- **Date:** 2024-05-13
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Open-source LLMs as LangChain Agents

- **ID:** `hf-r-open-source-llms-as-agents`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/open-source-llms-as-agents
- **Date:** 2024-01-24
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing Agents.js: Give tools to your LLMs using JavaScript

- **ID:** `hf-r-agents-js`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/agents-js
- **Date:** 2023-07-24
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Introducing Pytorch Native Agentic Stack

- **ID:** `meta-r-introducing-pytorch-native-agentic-stack`
- **Company:** Meta AI / FAIR
- **Link:** https://ai.meta.com/blog/introducing-pytorch-native-agentic-stack/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- Meta unveils five PyTorch-native projects at PyTorch Conference 2025: ExecuTorch 1.0, Torchforge, Monarch, TorchComms, Helion, plus OpenEnv (with HF) for RL environment hub
- stack spans kernel languages, distributed systems, RL, agentic frameworks, and edge deployment
- scales from thousands to hundreds of thousands of GPUs across heterogeneous hardware
- publishes RFC for standard environment interface
- covers full agentic AI lifecycle from post-trained LLM deployment to RL training.


### Open Coding Agents

- **ID:** `ai2-r-open-coding-agents`
- **Company:** Allen Institute for AI
- **Link:** https://allenai.org/blog/open-coding-agents
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="agent-research-applications"></a>Agent research applications (scientific, robotic)

_8 posts_

### Jack of All Trades, Master of Some, a Multi-Purpose Transformer Agent

- **ID:** `hf-r-jat`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/jat
- **Date:** 2024-04-22
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- HF releases Jack of All Trades (JAT), an open reproduction and extension of DeepMind's Gato
- contributions: release of many expert RL policies across Atari/BabyAI/Meta-World/MuJoCo, the JAT dataset (hundreds of thousands of expert trajectories for generalist-agent training), and a multimodal Transformer agent capable of video games, robot control, navigation, and language
- introduces improvements over Gato for sequential data and continuous-value handling
- generalist agent research.


### Practices for Governing Agentic AI Systems

- **ID:** `oai-r-practices-for-governing-agentic-ai-systems`
- **Company:** OpenAI
- **Link:** https://openai.com/index/practices-for-governing-agentic-ai-systems/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

**Summary:**

- White paper on governance practices for agentic AI systems
- Defines agentic systems and lifecycle parties (developers, deployers, users, third parties)
- Proposes baseline safety/responsibility practices per party
- Discusses indirect societal impacts from wide-scale agent adoption
- Accompanied by an agentic AI research grant program
- Matters as early governance framework specific to agents.


### Improving the academic workflow: Introducing two AI agents for better figures and peer review

- **ID:** `gr-r-improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review`
- **Company:** Google Research
- **Link:** https://research.google/blog/improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### A Generalist Agent

- **ID:** `dm-r-a-generalist-agent`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/a-generalist-agent/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- DeepMind introduces Gato, a single generalist multi-modal, multi-task, multi-embodiment transformer policy: same network/weights plays Atari, captions images, chats, stacks blocks on a real robot, etc.
- tokenizes all modalities (actions, observations, text, images) into a flat sequence and trains via language-model-style next-token prediction with action/text losses
- scales transformer recipe across many datasets
- 1024-token context of observations and actions
- landmark generalist-agent paper.


### Gemini Robotics 15 Brings Ai Agents Into The Physical World

- **ID:** `dm-r-gemini-robotics-15-brings-ai-agents-into-the-physical-world`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Opening Up A Physics Simulator For Robotics

- **ID:** `dm-r-opening-up-a-physics-simulator-for-robotics`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/opening-up-a-physics-simulator-for-robotics/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Safety First Ai For Autonomous Data Centre Cooling And Industrial Control

- **ID:** `dm-r-safety-first-ai-for-autonomous-data-centre-cooling-and-industrial-control`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/safety-first-ai-for-autonomous-data-centre-cooling-and-industrial-control/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- DeepMind deploys a cloud-based AI control system that directly controls cooling in Google data centres (not just recommends), under operator supervision
- every five minutes it ingests sensor snapshots and predicts energy outcomes of candidate action combinations via deep neural networks, then picks the minimal-energy action satisfying safety constraints
- first-of-its-kind deployment delivering energy savings across multiple data centres
- classified as agent-research-applications since it is a deployed autonomous control agent.


### Spurious Normativity Enhances Learning Of Compliance And Enforcement Behavior In Artificial Agents

- **ID:** `dm-r-spurious-normativity-enhances-learning-of-compliance-and-enforcement-behavior-in-artificial-agents`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/spurious-normativity-enhances-learning-of-compliance-and-enforcement-behavior-in-artificial-agents/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

**Summary:**

- DeepMind paper on multi-agent deep RL as a model of complex social interactions (norm formation)
- shows spurious norms (arbitrary rules with no intrinsic payoff) can accelerate learning of compliance-and-enforcement behaviors and thereby support emergence of socially beneficial norms
- framed as a path to richer simulations of social-ecological systems (cooperation, resource management, governance)
- multi-agent RL research on social norm emergence.


## <a id="agent-traces-and-observability"></a>Agent traces & observability

_1 posts_

### Agent Trace: Capturing the Context Graph of Code

- **ID:** `cog-r-agent-trace`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/agent-trace
- **Date:** 2026-01-29
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


## <a id="agent-design-and-patterns"></a>Agent design & patterns / opinion pieces

_14 posts_

### Trustworthy agents in practice

- **ID:** `ant-r-trustworthy-agents`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/trustworthy-agents
- **Date:** 2026-04-09
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Security boundaries in agentic architectures

- **ID:** `vcl-e-security-boundaries-in-agentic-architectures`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/security-boundaries-in-agentic-architectures
- **Date:** 2026-02-24
- **Authors:** Malte Ubl|Harpreet Arora
- **Track:** engineering
- **Contribution type:** empirical-study

**Summary:**

- Argues most coding agents today run generated code with full access to secrets, conflating multiple trust domains into one security context
- recommends separating actors (user, agent, generated code) and placing boundaries between them
- proposes architecture for running agent and generated code in isolated contexts (sandboxes) to contain prompt-injection blast radius
- walks through an example agent debugging prod with a malicious log and how boundaries prevent compromise
- strong design-pattern guidance for production agent deployments.


### Implementing a secure sandbox for local agents

- **ID:** `cur-r-agent-sandboxing`
- **Company:** Cursor
- **Link:** https://cursor.com/blog/agent-sandboxing
- **Date:** 2026-02-18
- **Authors:** Ani, Yash & Alex
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** coding-agents

**Summary:**

- Cursor introduces agent sandboxing on macOS, Linux, Windows for local coding agents
- Sandboxed agents run freely within controlled environment, only requesting approval when accessing internet, reducing approval fatigue
- Sandboxed agents stop 40% less often than unsandboxed
- Exposes a unified sandbox interface across OSes balancing security and usability (many commands need unexpected privileges)
- Matters as production safety pattern for auto-approved coding agents


### We removed 80% of our agent’s tools

- **ID:** `vcl-e-we-removed-80-percent-of-our-agents-tools`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools
- **Date:** 2025-12-22
- **Authors:** Andrew Qu
- **Track:** engineering
- **Contribution type:** empirical-study

**Summary:**

- Vercel's internal text-to-SQL agent d0 was rebuilt by stripping most specialized tools and replacing them with a single bash-execution tool (a file-system agent pattern using grep/cat/ls)
- success rate went from 80% to 100% with fewer steps and tokens
- thesis: simpler tool surfaces let Claude 'figure things out' better than hand-crafted guardrails
- removes pre-filtering, option-constraining, validation wrappers that were over-engineered
- strong design-pattern evidence that minimalism beats elaborate scaffolding for capable models.


### Coding Agents 101: The Art of Actually Getting Things Done

- **ID:** `cog-r-coding-agents-101-the-art-of-actually-getting-things-done`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/coding-agents-101-the-art-of-actually-getting-things-done
- **Date:** 2025-06-27
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Don’t Build Multi-Agents

- **ID:** `cog-r-dont-build-multi-agents`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/dont-build-multi-agents
- **Date:** 2025-06-12
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### The no-nonsense approach to AI agent development

- **ID:** `vcl-e-the-no-nonsense-approach-to-ai-agent-development`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/the-no-nonsense-approach-to-ai-agent-development
- **Date:** 2025-06-04
- **Authors:** Malte Ubl
- **Track:** engineering
- **Contribution type:** empirical-study

**Summary:**

- Practical playbook for building narrow, tightly-scoped, domain-specific AI agents
- step 1: prototype the agent manually before writing code, feeding real inputs to an LLM and watching which steps are mechanical vs judgment-heavy
- emphasizes structured inputs (e.g., Tailwind for HTML) over pure natural language
- draws on v0.dev experience where scope-narrowing beat waiting for better models
- patterns-focused guide for agent design.


### AI Agents Are Here. What Now?

- **ID:** `hf-r-ethics-soc-7`
- **Company:** Hugging Face
- **Link:** https://huggingface.co/blog/ethics-soc-7
- **Date:** 2025-01-13
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


### Building Effective AI Agents

- **ID:** `ant-e-building-effective-agents`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/engineering/building-effective-agents
- **Date:** 2024-12-19
- **Authors:** Erik S.|Barry Zhang
- **Track:** engineering
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Building Effective AI Agents

- **ID:** `ant-r-building-effective-agents`
- **Company:** Anthropic
- **Link:** https://www.anthropic.com/research/building-effective-agents
- **Date:** 2024-12-19
- **Authors:** Erik S.|Barry Zhang
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### A review of OpenAI’s o1 and how we evaluate coding agents

- **ID:** `cog-r-evaluating-coding-agents`
- **Company:** Cognition
- **Link:** https://cognition.ai/blog/evaluating-coding-agents
- **Date:** 2024-09-12
- **Track:** research
- **Contribution type:** empirical-study
- **Techniques:** test-time-compute

_Summary pending — see link for details._


### How we monitor internal coding agents for misalignment

- **ID:** `oai-r-how-we-monitor-internal-coding-agents-misalignment`
- **Company:** OpenAI
- **Link:** https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering

- **ID:** `oai-r-mle-bench`
- **Company:** OpenAI
- **Link:** https://openai.com/index/mle-bench/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** empirical-study

_Summary pending — see link for details._


### Scalable Agent Architecture For Distributed Training

- **ID:** `dm-r-scalable-agent-architecture-for-distributed-training`
- **Company:** Google DeepMind
- **Link:** https://deepmind.google/discover/blog/scalable-agent-architecture-for-distributed-training/
- **Date:** _date unknown_
- **Track:** research
- **Contribution type:** _(uncategorized)_

_Summary pending — see link for details._


## <a id="agents-general"></a>General agentic systems

_3 posts_

### Agentic Infrastructure

- **ID:** `vcl-e-agentic-infrastructure`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/agentic-infrastructure
- **Date:** 2026-04-09
- **Authors:** Tom Occhino
- **Track:** engineering
- **Contribution type:** empirical-study

**Summary:**

- Vercel's CPO argues that LLMs/coding agents demand a new generation of infrastructure across three layers
- 30% of Vercel deployments are now initiated by coding agents (75% Claude Code), up 1000% in 6 months
- frames 'Agentic Infrastructure' as (1) infra for coding agents to deploy to, (2) infra for building/running agents, (3) infra that is itself agentic
- emphasizes immutable deploys, preview URLs, MCP, and programmatic surfaces as prerequisites for autonomous agent workflows
- positions Vercel's CLI/API/MCP/git integration as native surface for machine-driven software development.


### How FLORA shipped a creative agent on Vercel's AI stack

- **ID:** `vcl-e-how-flora-shipped-a-creative-agent-on-vercels-ai-stack`
- **Company:** Vercel
- **Link:** https://vercel.com/blog/how-flora-shipped-a-creative-agent-on-vercels-ai-stack
- **Date:** 2026-03-31
- **Authors:** Eric Dodds
- **Track:** engineering
- **Contribution type:** empirical-study

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

**Summary:**

- Internal Vercel talk on disciplined deployment of agent-generated code to production
- argues green CI is no longer proof of safety because agents produce polished, convincing PRs that hide bad assumptions (e.g., full-table scans, retry thundering herds, caches with no TTL)
- warns agents lack production context (traffic patterns, failure modes, capacity limits)
- proposes a review/judgment framework for teams shipping with agents
- useful design-and-patterns guidance for agentic development discipline.

