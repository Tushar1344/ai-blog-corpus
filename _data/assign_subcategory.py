#!/usr/bin/env python3
"""Assign subcategory (1-of-N) to each in-scope post, within its focus_area.

~47 subcategories across 8 focus areas. See SUB_RULES below.

Applies to master.csv in-place. Adds `subcategory` column if not present.
"""
import csv
import re
from pathlib import Path
from collections import Counter

DATA = Path(__file__).parent

# Rule format: focus_area -> list of (subcategory, regex). First match wins.
# Each focus area ends with a fallback subcategory (catches anything not matched by specific rules).
SUB_RULES = {
    "pretraining-and-architecture": [
        ("architectures", r"\b(moe\b|mixture of experts|mixtral|\bmamba\b|state space|\bssm\b|hyena|rwkv|\bs4\b|new (attention|layer|architecture|model architecture)|attention variant|linear attention|sliding window attention|\brope\b|rotary|multi[- ]head latent|hybrid (architecture|model)|dense model|transformer improvement|mixattention|warp decode|\bmla\b|\bgqa\b|grouped query attention|\bmod\b|mixture of depths|expert parallel|sparse attention|activation function|novel layer|position embedd|continuous autoregressive|diffusion transformer|dit\b|autoregressive model|encoder architecture|decoder architecture)\b"),
        ("scaling-and-training-dynamics", r"\b(scaling laws?|chinchilla|loss landscape|loss curve|training dynamic|optimizer|\bmuon\b|\badam-?w?\b|\bsgd\b|learning rate|gradient clipping|hyperparameter|training (stability|instability)|compute optimal|emergent|phase transition|grokking|compute-optimal|how long should you train)\b"),
        ("data-and-tokenization", r"\b(data mix(ing|ture)|tokeniz|curriculum learning|pretrain(ing)? data|data (pipeline|quality|filter|dedup|synth)|dolma|fineweb|cosmopedia|ultrachat|ultrafeedback|finepdf|the pile|redpajama|slimpajama|c4\b|webdata|corpus|fine.?web|synthetic data|web[- ]scale data|open (data|dataset)|multilingual (data|corpus)|data for (pretrain|training))\b"),
        ("training-stack", r"\b(composer|llm foundry|streaming dataset|megablocks|distributed training|training stack|fp8 training|bf16 training|pipeline parallel|tensor parallel|sequence parallel|ulysses|\bmfu\b|model flop|training efficien|gradient accumulation|mixed precision|from scratch training|training recipe|training at scale|training (infra|infrastructure)|\bmosaic\b|megatron|deepspeed|\bfsdp\b|cloud training|train at scale)\b"),
        ("multimodal-pretraining", r"\b(multi[- ]?modal|vision[- ]?language|\bvlm\b|image encoder|image pretrain|video pretrain|audio pretrain|\bsam\b|\bsam2\b|segment anything|\bdinov\d?\b|\bdino\b|\bjepa\b|v-jepa|ijepa|imagebind|embodied multimodal|speech recognition|whisper|text-to-image|text-to-video|text-to-speech|\btts\b|\basr\b|image generation|diffusion model|\bsora\b|dalle|dall.?e|dalle[- ]?\d|stable diffusion|latent diffusion|autoencoder|\bvideo model\b|voice (model|synthesis)|clip\b|vision transformer|\bvit\b)\b"),
        ("foundation-model-releases", r"\b(\bdbrx\b|\bmpt[- ]?\d?\b|\bolmo[- ]?\d?\b|gemini|gemma|llama|\bmistral\b|mixtral|deepseek-(v\d|r\d|coder|math|prover|moe|vl|llm)|claude [234]|opus \d|sonnet \d|haiku \d|grok-?\d|qwen|phi-?\d|falcon|\byi-?\d|\baya\b|command[-\s]r|smollm|\btulu\b|\bgpt-[234]\b|gpt-oss|\breka\b|stablelm|persimmon|\borca\b|molmo|\bjamba\b|minerva|\bpali\b|chinchilla model|technical report|model (release|card)|introducing (our|the) new .* (model|llm)|welcome gemma|welcome llama|hello olmo|introducing .{0,30}(llm|model))\b"),
        ("societal-impact-and-deployment-studies", r"\b(economic impact|economic index|labor market|societal impact|productivity (gain|impact)|usage stud|deployment stud|real-world (usage|impact)|\bhow (australia|india|uk|us|europe) uses?\b|country brief|ai fluency|disempowerment|how (ai|claude) assistance|how ai is transforming|scientific computing|how people are using|learning curves|formation of coding skills|education (report|index)|commitments on model|project vend|project fetch|vibe physics|assistant axis|affective use)\b"),
        ("research-techniques-and-methods", r"(emotion concept|behavioral differences|diff tool for ai|language model (behaviour|behavior)|model behaviour|consistency model|energy-based|generative (model|qa)|word embedding|text embedding|contrastive pre|masked (autoencoder|pretrain)|self-supervised|meta.?learning|few-shot|zero-shot|in-context learning|\bicl\b|retrieval.?pretrain|long range memory|GAN\b|generative adversarial|optimal transport|hindsight experience|reinforcement learning|\brl\b|policy gradient|q[- ]learning|actor[- ]critic|\bvae\b|variational|\bgan\b|exploration|imitation learning|transfer (learning|from simulation)|temporal segment|augment(ed)? data|data augment|\baiming for|ucb\b|\bmcts\b|monte carlo|neural architecture search|\bnas\b|alphago|alphazero|alphagymnasium|muzero|open.?ai gym|neurips|icml|iclr|\bcogsci\b|attention is all|transformer|\bbert\b|\bgpt\b|roberta|electra|deberta|\bgan\b|diffusion|dreambooth|image gpt|hindsight|fill in the middle|prediction and control|learn to reason|reasoning models? don.?t|model evaluations?|teaching models to express|models? express|behavioural|behavioral|hallucinat|confident|calibrat|uncertain|generalization (in|of)|scaling to|understanding the source|source of what|identifying ai-generated|detecting ai-generated|ai-generated|algorithm (for|design)|new algorithm|novel algorithm)"),
        ("model-research-and-applications", r"(scientific research|life sciences|health|medical|medicin|clinical|cyber|security|biomed|drug (design|discovery)|genome|gene|protein|alphafold|alphamissense|alphaproteo|alphaevolve|alphatensor|alphageomet|alphaproof|alphaz|materials science|weather|climate model|sustainability|chemistry|atomic|molecul|prediction|forecasting|nowcast|fusion|plasma|robot(ic)?|physics|retro biosciences|penda health|epidemic|cancer|disease|eye disease|diabet|mri|radiolog|pathology|olympic|imo|ioi|iais|ipho|math olymp|retail|logist|supply chain|financial)"),
        ("fallback-architecture", r".*"),  # catch-all
    ],
    "post-training-and-fine-tuning": [
        ("rlhf-classic", r"\b(rlhf|rlaif|\bppo\b|reward model(ing)?|preference data|instruct.?gpt|webgpt|helpful harmless|summariz(e|ation) (from|with) (human|feedback)|learn(ing)? (to summarize|from human)|human preferences)\b"),
        ("rlvr-verifiable-rewards", r"\b(rlvr|verifiable reward|grpo|\br1\b|reasoning model|test[- ]time compute|best[- ]of[- ]n|process reward|step[- ]level reward|prm\b|deepseek-r1|kevin-32b|reasoning chain|\btao\b)\b"),
        ("direct-preference", r"\b(\bdpo\b|\bkto\b|\borpo\b|simpo|direct preference|preference optim|iterative dpo|offline (preference|rl))\b"),
        ("sft-and-instruction-tuning", r"\b(\bsft\b|instruction tuning|instruction.?follow|tulu|ultrachat|alpaca|sharegpt|openassistant|supervised fine[- ]tun|curated dataset)\b"),
        ("distillation", r"\b(distillation|distill|student model|teacher model|on[- ]policy distillation|knowledge transfer|minimize kl)\b"),
        ("fallback-post-training", r".*"),
    ],
    "alignment-and-safety": [
        # Order matters — more specific first, broader later
        # NOTE: avoid trailing \b after terms that can have plural/gerund (jailbreak→jailbreaking, classifier→classifiers)
        ("system-cards", r"(system card|model card\b|sora system card|gpt-\d.*system card|opus .* system card|sonnet .* system card|claude .* system card|addendum to gpt|addendum to .* system card|update to gpt|update to .* system card|preparedness report|capability evaluation report)"),
        ("deceptive-alignment", r"(alignment faking|deceptive alignment|sleeper agent|sandbag|scheming|treacherous|mesa.?optim|model organism|latent misalign|encoded reasoning|hidden reasoning|\btrojan\b|backdoor|poison|model poisoning|insider threat|agentic misalignment|probes can catch|simple probes|influence function|auditing (language )?models?|hidden objectives|shortcuts to sabotage|emergent misalign|deliberative alignment)"),
        ("red-teaming-and-jailbreaking", r"(red[- ]?team|jailbreak|jail-break|adversarial prompt|adversarial suffix|many-shot|universal jailbreak|prompt injection|injection attack|glitch token|prefix attack|auditing tool|\bpetri\b|constitutional classifier|next[- ]generation constitutional)"),
        ("capability-evals-for-safety", r"(bioweapon|biosecur|\bcbrn\b|cyber (eval|capability|offens|defender)|persuasion eval|autonomy (eval|capability)|self.?exfiltration|situational awareness|dangerous capability|agi evals|uplift eval|sabotage eval|building ai for cyber|for cyber defender|weapons of|biological research.?wet lab)"),
        ("scalable-oversight", r"(scalable oversight|iterated amplification|\bdebate\b|recursive reward|weak[- ]to[- ]strong|factored cognition|amplification|ai safety via debate|super.?human (oversight|assist))"),
        ("responsible-scaling-and-policy", r"(\brsp\b|responsible scaling|preparedness framework|frontier safety framework|model spec|safety policy|governance|responsible ai|accountability|policy enforcement|responsible disclosure|transparency report|safeguard policy|\baup\b|core views|commitments on|economic impact|deployment polic|societal impact|labor market|economic index|democratic input|ai values|value alignment|values and alignment|mapping .*misuse|malicious use)"),
        ("constitutional-and-self-critique", r"(constitutional ai|constitutional approach|constitutional classifier|self[- ]critique|ai-written critique|claude\'s character|character training|\bpersona\b|self[- ]correction|model welfare|instruction hierarchy|assistant axis)"),
        ("reward-hacking-and-sycophancy", r"(reward hack|reward gaming|specification gaming|sycophan|mode collapse|exploration collapse|prover[- ]verifier|faithful(ness)? of|chain.of.thought monitor|monitor(ability|ing)|eval awareness|honest|truthful|disempowerment|shortcut|\blie\b|\blies\b|lying|reasoning models don.?t always|don.?t always say what they think|models generally tell)"),
        ("safety-research-general", r"(safety (research|training|techniques|eval)|alignment (research|lab|technique)|general (language|ai) assistant|harm reduction|toxicity|\bbias\b|\bfair(ness)?\b|responsible|\bethics\b|ethical|values in the wild|emotion concept|tracing (the )?thoughts|vision language model alignment|self-alignment|alignment behavio|behavioral disposition|ai system cards)"),
        ("fallback-alignment", r".*"),
    ],
    "interpretability": [
        ("saes-and-dictionary-learning", r"\b(\bsae\b|sparse autoencoder|dictionary learn|monosemanti|superposition|scaling monosemanticity|feature activations)\b"),
        ("circuits-and-mechanistic", r"\b(circuit(s)?\b|mechanistic|induction head|in-context circuit|feature visualization|circuit.tracing|transformer circuit|attention circuit)\b"),
        ("feature-viz-and-probing", r"\b(probing|probe\b|linear probe|concept probing|feature viz|neuron visualiz|activation visualiz|representation probing|tracing thoughts)\b"),
        ("steering-and-intervention", r"\b(steer(ing)?|activation steering|vector steering|residual stream|intervention|causal intervention|patching|activation patching|concept erasure)\b"),
        ("attention-and-induction-heads", r"\b(attention pattern|induction head|attention head|in-context head|super-position\b)\b"),
        ("fallback-interp", r".*"),
    ],
    "evals-and-benchmarks": [
        ("benchmark-critique", r"\b(why (swe-bench|eval) (verified )?no longer|benchmark critique|benchmark (is broken|flaw)|eval awareness|contamination|data contamination|leaderboard (is|are) (broken|misleading)|measuring is hard|infrastructure noise|noise in eval|unpacking)\b"),
        ("coding-evals", r"\b(swe-bench|swe bench|humaneval|mbpp|livecodebench|codecontest|\bapps\b|code eval|coding benchmark|swe.?gym|code gen eval|cursorbench|paperbench|code agent benchmark|swe-check|swe-?grep|bug detection benchmark|code-?bench)\b"),
        ("reasoning-evals", r"\b(gpqa|mmlu|mmlu-pro|frontiermath|arc-agi|math eval|competitive math|aime|usamo|olympiad|reasoning benchmark|\bgsm8k\b|big.?bench|humanity.?s.?last|cybench|science benchmark|paperbench)\b"),
        ("agent-evals", r"\b(tau-bench|browsecomp|agentcompany|officeqa|agent benchmark|agent eval|web agent benchmark|osworld|agent.?bench|\bgaia\b|mle.?bench|function calling evaluation|function.calling eval)\b"),
        ("multimodal-evals", r"\b(vqa|video.?qa|vision benchmark|multimodal benchmark|imagenet|coco benchmark|msvtt|mme\b|mmmu|visual eval|audio eval|speech eval)\b"),
        ("judge-models-and-methodology", r"\b(judge(s)?\b|judge.?model|\bpgrm\b|reward model eval|llm-as-judge|llm-as-a-judge|judge bench|pairwise comparison|\belo\b|chatbot arena|\barena\b|reliable judge|judge accuracy|custom judges?|evaluation (framework|suite|methodology)|eval methodology|continuous eval|measuring (ai|model))\b"),
        ("eval-systems-and-harnesses", r"(demystifying eval|evaluation framework|eval harness|evaluation platform|eval platform|continuous evaluation|offline eval|online eval|hybrid eval|benchmark suite|eval at scale|evalu(ating|ations?) (ai|llm|models?|claude|gpt)|\bevals? for\b|measurement framework|evaluation gauntlet|calibrating.*eval|secure evaluation|blazingly fast.*eval|statistical approach to.*eval|model evaluations?|measure of|benchmarking domain)"),
        ("leaderboards-and-community-evals", r"(leaderboard|community eval|open llm leader|open (asr|arabic|multilingual) leader|top models|chatbot arena|\barena\b|elo\b|ranking (of|llm|model)|wildbench|fixing.*leader|rethinking (llm )?eval|co2 emissions.*leader|\baragen\b|\bbig[- ]?bench\b|\btimescope\b|\bhallucin.*bench)"),
        ("domain-specific-evals", r"(science eval|medical eval|legal eval|clinical eval|biological eval|chemistry eval|math problem|legal benchmark|healthcare benchmark|domain benchmark|enterprise eval|classification|truthful|truthfulqa|truthfulness|evalu(ating|ations?) (bias|fairness|safety|alignment|reasoning|capability|performance|ability|scientific|real.world)|speech recognition benchmark|asr benchmark|auditory|waveform|continual learning benchmark|physical reasoning|action recognition|video object|audio visual|speech translation|knowledge intensive|open world|open benchmark|atari benchmark|facts grounding|reward model benchmark|rewardbench|reward bench|mle.?bench|code generation eval|swe[- ]?lancer|function calling evaluation|cursorbench|paperbench)"),
        ("benchmark-release", r"(new benchmark|introducing .* benchmark|introducing the .* benchmark|a new benchmark|benchmark for|for benchmarking|benchmark dataset|dataset.*benchmark|open dataset|open benchmark|release.*benchmark|benchmark release)"),
        ("fallback-evals", r".*"),
    ],
    "quantization-and-efficiency": [
        ("training-time-quantization", r"\b(fp8 training|int8 training|training (in|with) (fp8|int8|bf16|low.?precision)|mixed precision training|low-precision training)\b"),
        ("post-training-quantization", r"\b(gptq|awq\b|\bptq\b|post.?training quantiz|quantiz (inference|model|serving)|4-bit quantiz|8-bit quantiz|bitsandbytes|bnb|smoothquant|quip\b|hqq)\b"),
        ("parameter-efficient-training", r"\b(lora\b|qlora|\bpeft\b|parameter[- ]efficient|adapter|prefix tuning|prompt tuning|p-tuning|ia3\b|tied embed)\b"),
        ("pruning-and-sparsity", r"\b(pruning|prune|sparsity|sparse model|wanda|sparsegpt|movement pruning|unstructured pruning|2:4 sparsity|model compression)\b"),
        ("fallback-efficiency", r".*"),
    ],
    "agentic-systems": [
        ("coding-agents", r"\b(coding agent|code agent|devin\b|claude code|cursor (agent|composer|bugbot|3)|copilot agent|swe.?grep|aider|cline\b|augment code|claude developer|swe-agent|codex\b|autonomous code|code generation agent|\bcomposer\b)\b"),
        ("multi-agent-orchestration", r"\b(multi[- ]agent|subagent|agent fleet|agent orchestration|agent team|debate agent|agent pool|agent collab|hive agent|scheduling agent|schedule devins|manage devins|managed agent|agent hierarchy|sub[- ]agent)\b"),
        ("computer-use-and-browser-use", r"\b(computer use|computer-use|browser use|browser[- ]use|web agent|desktop agent|gui agent|visual agent|click agent|operator\b|atlas\b|web.?navig|screen (reading|interpret)|control their (own )?computer)\b"),
        ("tool-use-and-function-calling", r"\b(tool use|tool-use|tool calling|function call|function[- ]calling|tool invocation|tool.?integration|api call|api.based agent|responses api|tool integration|writing tools|writing effective tools)\b"),
        ("enterprise-agents", r"\b(enterprise agent|knowledge assistant|data analyst agent|\bkarl\b|business agent|customer support agent|\brag\b agent|sql agent|slack agent|docs agent|data agent|instructed retriever|enterprise knowledge|memory scaling|agentic reasoning in practice)\b"),
        ("embodied-and-simulation", r"\b(embodied|habitat|robot(ic)?|simulation|sim2real|sim-to-real|world model|physics engine|manipulator|dexter|walk|locomotion|embodied ai|household|robot dog|autonomous vehicle|self[- ]driv)\b"),
        ("agent-traces-and-observability", r"\b(agent trace|trajectory|action trace|agent log|observability|telemetry|replay|debug agent|inspection|behaviour model|agent monitor|monitor agents|monitoring agents|observer)\b"),
        ("agent-design-and-patterns", r"(building (effective|better) (ai )?agents?|trustworthy agents?|agent best practices|agent architecture|agent pattern|effective agent|real.world agent|production agent|reliable agent|agent design|designing agents?|mle.?bench|coding agents 101|don.?t build multi|art of .*getting things done|review of .*openai|evaluate coding agents?|monitor .*coding agent|agents? are here|agents? .*misalignment)"),
        ("agent-frameworks-and-tooling", r"(smolagent|transformers agent|agents\.?js|agent framework|open[- ]source (agent|deepresearch)|langchain agent|agent library|agent sdk|agent toolkit|write actions in code|license to call|open coding agent|agents on|deepresearch|introducing agents?)"),
        ("dialogue-and-conversational-agents", r"(dialogue agent|conversational agent|e.?commerce (agent|conversational)|chatbot agent|sparrow|claude assistant|safer dialogue|harmful behavio|detect harmful)"),
        ("game-and-rl-agents", r"(game (agent|playing|world)|video game|atari|starcraft|dota|go\b|chess|capture the flag|rl agent|deep rl|reinforcement learning agent|teach(ing)? agent|generalize to new|new setting|imagination|imagine and plan|\bcthe\b|cooperative agent|self[- ]play|unfamiliar task|emerge from|open[- ]ended play|droidlet|polygames|ai vs\\.? ai|\brle\b|reinforcement learning environment|openenv|gaia2?|openenv in practice|predicting future events|back to the future)"),
        ("agent-research-applications", r"(academic workflow|figure(s)?|peer review|scientific agent|research agent|autonomous.*research|clio|privacy[- ]preserving|robot.*agents?|physics simulator|robotic(s)? agent)"),
        ("agents-general", r"(agent\b|agentic|autonomous|\bai assistant\b|autonomous systems)"),  # broad catch-all
        ("fallback-agents", r".*"),
    ],
    "harness-and-context-engineering": [
        ("mcp-and-tool-protocols", r"\b(\bmcp\b|model context protocol|tool protocol|tool specification|api spec for agents|unified tool|openapi for agents|mcp[- ]?to)\b"),
        ("long-running-harnesses", r"\b(long[- ]running|persistent agent|agent-ops|long horizon|multi.?step|recovery|resume|checkpoint agent|harness design|harness (engineering|design)|managed (agent|harness))\b"),
        ("context-engineering", r"\b(context engineering|context compression|context selection|context (management|window|budget)|prompt compression|summarization for context|retrieval[- ]for[- ]context|self[- ]summariz|chunking|notepad|contextual retrieval|retrieval augmented|\brag\b)\b"),
        ("scaffolding-patterns", r"\b(scaffold|react pattern|chain.of.thought|cot\b|plan.and.execute|tree of thought|self.ask|self.refine|reflexion|\brap\b|\bthink\b tool|stop and think|analogy)\b"),
        ("agent-skills-and-prompt-libraries", r"\b(agent skill|skill libr|prompt libr|prompt template|prompt catalog|prompt reuse|writing prompts|writing (effective )?tools|equipping agents)\b"),
        ("prompt-caching", r"\b(prompt cach|anthropic cache|cache hit|cache key|kv.?cache for prompts)\b"),
        ("codex-and-sora-harness", r"(codex harness|unrolling (the )?codex|codex agent|beyond rate limits|codex app server|sora for|build (chatgpt|atlas)|\bowl\b|c compiler|parallel claudes|postmortem|recent issues|scaling postgresql|in-house data agent)"),
        ("ai-sdk-and-product-tooling", r"(ai sdk( \d)?|\bv0\b|v0 (app|platform|api|ambassador)|durable execution|agents\.md|agent skills explained|mux/ai sdk|how .* uses? (vercel|ai sdk)|how .* shipped|how .* built.*ai|serverless agent|ai[- ]powered (brand|assistant)|agent gateway|ai gateway|zero data retention|unified report|agent responsibl|agentic infrastructure|vibe coding)"),
        ("data-analyst-and-workflow-agents", r"(ai data analyst|data analyst|bugbot|code review|code review agent|self.?improve|file format|disk snapshot|blockdiff)"),
        ("databricks-training-stack-misc", r"(training moes|bringing megablocks|enterprise-grade.*inference|gaudi 2|mi250|streaming dataset|inference performance|turbocharged training|llm foundry|\bmosaic\b.*inference|serving quantized|tensorrt.?llm integration|stable diffusion.*less|\$50k|cloudflare r2|coreweave|\bh100\b|cuda oom|gradient accumulation|image segmentation|benchmarking (large|llms? )?on|setting a baseline)"),
        ("fallback-harness", r".*"),
    ],
}

# Nice-looking display names for subcategories
SUB_TITLES = {
    # Pretraining
    "architectures": "Architectures (MoE, SSMs, attention variants)",
    "scaling-and-training-dynamics": "Scaling laws & training dynamics",
    "data-and-tokenization": "Data & tokenization",
    "training-stack": "Training stack & infrastructure",
    "multimodal-pretraining": "Multimodal pretraining",
    "foundation-model-releases": "Foundation model releases",
    "societal-impact-and-deployment-studies": "Societal impact & deployment studies",
    "research-techniques-and-methods": "Research techniques & methods",
    "model-research-and-applications": "Science-applied AI (AlphaFold, health, climate, etc.)",
    "fallback-architecture": "Other pretraining & architecture",
    # Post-training
    "rlhf-classic": "Classic RLHF (PPO, reward models)",
    "rlvr-verifiable-rewards": "RLVR & verifiable-reward RL",
    "direct-preference": "Direct preference (DPO, KTO, ORPO, SimPO)",
    "sft-and-instruction-tuning": "SFT & instruction tuning",
    "distillation": "Distillation",
    "fallback-post-training": "Other post-training",
    # Alignment
    "constitutional-and-self-critique": "Constitutional methods & self-critique",
    "responsible-scaling-and-policy": "Responsible scaling & safety policy",
    "red-teaming-and-jailbreaking": "Red-teaming & jailbreaking",
    "deceptive-alignment": "Deceptive alignment & scheming",
    "capability-evals-for-safety": "Dangerous-capability evaluations",
    "scalable-oversight": "Scalable oversight & debate",
    "reward-hacking-and-sycophancy": "Reward hacking, monitorability & honesty",
    "safety-research-general": "General safety research",
    "system-cards": "System cards & model cards",
    "fallback-alignment": "Other alignment & safety",
    # Interp
    "saes-and-dictionary-learning": "SAEs & dictionary learning",
    "circuits-and-mechanistic": "Circuits & mechanistic interpretability",
    "feature-viz-and-probing": "Feature viz & probing",
    "steering-and-intervention": "Steering & intervention",
    "attention-and-induction-heads": "Attention patterns & induction heads",
    "fallback-interp": "Other interpretability",
    # Evals
    "coding-evals": "Coding evaluations",
    "reasoning-evals": "Reasoning & math evaluations",
    "agent-evals": "Agent evaluations",
    "multimodal-evals": "Multimodal evaluations",
    "judge-models-and-methodology": "Judge models & eval methodology",
    "benchmark-critique": "Benchmark critique",
    "eval-systems-and-harnesses": "Eval systems & harnesses",
    "leaderboards-and-community-evals": "Leaderboards & community evals",
    "domain-specific-evals": "Domain-specific evals (speech, vision, science, medical)",
    "benchmark-release": "Benchmark releases",
    "fallback-evals": "Other evaluations & benchmarks",
    # Efficiency
    "training-time-quantization": "Training-time quantization",
    "post-training-quantization": "Post-training quantization",
    "parameter-efficient-training": "Parameter-efficient training (LoRA/PEFT)",
    "pruning-and-sparsity": "Pruning & sparsity",
    "fallback-efficiency": "Other efficiency",
    # Agents
    "coding-agents": "Coding agents",
    "multi-agent-orchestration": "Multi-agent orchestration",
    "tool-use-and-function-calling": "Tool use & function calling",
    "computer-use-and-browser-use": "Computer use & browser use",
    "enterprise-agents": "Enterprise agents",
    "embodied-and-simulation": "Embodied agents & simulation",
    "agent-traces-and-observability": "Agent traces & observability",
    "agent-design-and-patterns": "Agent design & patterns / opinion pieces",
    "agent-frameworks-and-tooling": "Agent frameworks & tooling",
    "dialogue-and-conversational-agents": "Dialogue & conversational agents",
    "game-and-rl-agents": "Game-playing & RL agents",
    "agent-research-applications": "Agent research applications (scientific, robotic)",
    "agents-general": "General agentic systems",
    "fallback-agents": "Other agentic systems",
    # Harness
    "context-engineering": "Context engineering",
    "scaffolding-patterns": "Scaffolding patterns",
    "long-running-harnesses": "Long-running harnesses",
    "mcp-and-tool-protocols": "MCP & tool protocols",
    "agent-skills-and-prompt-libraries": "Agent skills & prompt libraries",
    "prompt-caching": "Prompt caching",
    "codex-and-sora-harness": "Product engineering case studies (Codex, Sora, Atlas)",
    "ai-sdk-and-product-tooling": "AI SDK & product tooling (Vercel v0, AI SDK)",
    "data-analyst-and-workflow-agents": "Workflow agents (data analyst, code review, Bugbot)",
    "databricks-training-stack-misc": "Databricks training stack (misplaced; should be pretraining/training-stack)",
    "fallback-harness": "Other harness & context engineering",
}

# Order within each focus area (for H2 section ordering in markdown)
SUB_ORDER = {
    "pretraining-and-architecture": [
        "foundation-model-releases", "architectures", "multimodal-pretraining",
        "scaling-and-training-dynamics", "data-and-tokenization", "training-stack",
        "research-techniques-and-methods", "model-research-and-applications",
        "societal-impact-and-deployment-studies",
        "fallback-architecture",
    ],
    "post-training-and-fine-tuning": [
        "rlvr-verifiable-rewards", "rlhf-classic", "direct-preference",
        "sft-and-instruction-tuning", "distillation", "fallback-post-training",
    ],
    "alignment-and-safety": [
        "system-cards", "responsible-scaling-and-policy", "constitutional-and-self-critique",
        "deceptive-alignment", "capability-evals-for-safety",
        "red-teaming-and-jailbreaking", "scalable-oversight",
        "reward-hacking-and-sycophancy", "safety-research-general",
        "fallback-alignment",
    ],
    "interpretability": [
        "saes-and-dictionary-learning", "circuits-and-mechanistic",
        "steering-and-intervention", "feature-viz-and-probing",
        "attention-and-induction-heads", "fallback-interp",
    ],
    "evals-and-benchmarks": [
        "agent-evals", "coding-evals", "reasoning-evals",
        "leaderboards-and-community-evals", "judge-models-and-methodology",
        "eval-systems-and-harnesses", "benchmark-release",
        "domain-specific-evals", "benchmark-critique", "multimodal-evals",
        "fallback-evals",
    ],
    "quantization-and-efficiency": [
        "training-time-quantization", "post-training-quantization",
        "parameter-efficient-training", "pruning-and-sparsity",
        "fallback-efficiency",
    ],
    "agentic-systems": [
        "coding-agents", "multi-agent-orchestration", "computer-use-and-browser-use",
        "tool-use-and-function-calling", "enterprise-agents",
        "embodied-and-simulation", "game-and-rl-agents",
        "dialogue-and-conversational-agents", "agent-frameworks-and-tooling",
        "agent-research-applications", "agent-traces-and-observability",
        "agent-design-and-patterns", "agents-general",
        "fallback-agents",
    ],
    "harness-and-context-engineering": [
        "mcp-and-tool-protocols", "codex-and-sora-harness", "long-running-harnesses",
        "context-engineering", "scaffolding-patterns", "agent-skills-and-prompt-libraries",
        "prompt-caching", "ai-sdk-and-product-tooling",
        "data-analyst-and-workflow-agents", "databricks-training-stack-misc",
        "fallback-harness",
    ],
}

# Focus area PROMOTION rules — for posts whose title clearly belongs in a different focus area.
# First match wins. Applied BEFORE subcategory classification.
# Each entry: (target_focus_area, title_regex)
FA_PROMOTE = [
    # Interpretability cluster
    ("interpretability", r"(\btrac(e|ing) (the )?thought|crosscoder|dictionary learn(ing)? (feature|classif)|scaling interpretab|circuit-trac|feature (viz|visualiz)|insights? on (cross|circuit))"),
    # Alignment cluster
    ("alignment-and-safety", r"(values? in the wild|auditing (language )?models? for hidden|hidden objective|sycophancy to subterfuge|reward tamper|small number of samples.*poison|claude.?s character|claude.?s extended thinking|persona selection|detecting misbehavior|ai-written critique|truthfulqa|truthful|evaluating fairness|aligning language models|hazard analysis|democratic input|chain[- ]of[- ]thought monitor|claude's.*character|clio.*privacy|productivity gain|economic index|economic impact|country brief|ai fluency|disempowerment)"),
    # Evals cluster (some pretraining-misclassified posts)
    ("evals-and-benchmarks", r"(solving math word|gamepad|theorem proving|evaluating ai.?s? ability|evaluating ai.?s capability|performing scientific research|real[- ]world tasks|measuring ai.?s capab|paperbench|benchmarking (domain|large language|llms?))"),
    # Harness cluster
    ("harness-and-context-engineering", r"(scaling managed agents|effective harnesses? for long)"),
    # Post-training cluster (classical OpenAI RL research)
    ("post-training-and-fine-tuning", r"(meta.?learning|reptile:|imitation learning|iterated amplification|learning complex goals|summarizing books with|human feedback|fine.?grained human feedback|synthetic data)"),
]

def classify_sub(row):
    fa = row.get("focus_area", "")
    if not fa or fa not in SUB_RULES:
        return "", ""  # (new_fa, sub)

    title = row.get("title", "").lower()

    # Focus-area promotion — only for posts currently in fallback paths
    current_sub = row.get("subcategory", "")
    # Try promotion regardless, but low-confidence — only promote if we see a strong match
    promoted_fa = None
    for target_fa, rx in FA_PROMOTE:
        if re.search(rx, title, re.I):
            promoted_fa = target_fa
            break

    effective_fa = promoted_fa or fa

    text = f"{row.get('title', '')} {row.get('id', '')} {row.get('techniques', '')}".lower()
    for sub, rx in SUB_RULES.get(effective_fa, []):
        if re.search(rx, text, re.I):
            return (promoted_fa or "", sub)
    return (promoted_fa or "", "")

def main():
    master_path = DATA / "master.csv"
    rows = list(csv.DictReader(open(master_path)))
    fields = list(rows[0].keys())
    if "subcategory" not in fields:
        fields.insert(fields.index("focus_area") + 1, "subcategory")

    counts = Counter()
    by_fa_sub = Counter()

    promoted_count = 0
    for r in rows:
        r.setdefault("subcategory", "")
        if r.get("in_scope") == "TRUE" and r.get("dropped_in_v2") == "FALSE" and r.get("focus_area"):
            new_fa, sub = classify_sub(r)
            if new_fa and new_fa != r["focus_area"]:
                r["focus_area"] = new_fa
                promoted_count += 1
            r["subcategory"] = sub
            counts[sub] += 1
            by_fa_sub[(r["focus_area"], sub)] += 1
    print(f"Promoted {promoted_count} posts to new focus area based on title.")

    with open(master_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)

    print(f"Assigned subcategories to {sum(counts.values())} in-scope rows\n")
    for fa, subs in SUB_ORDER.items():
        fa_total = sum(by_fa_sub[(fa, s)] for s in subs)
        print(f"{fa} ({fa_total})")
        for s in subs:
            c = by_fa_sub.get((fa, s), 0)
            if c:
                print(f"  {SUB_TITLES.get(s, s):50} {c}")
        print()

if __name__ == "__main__":
    main()
