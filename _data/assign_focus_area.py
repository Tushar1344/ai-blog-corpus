#!/usr/bin/env python3
"""Assign focus_area (1-of-8) + set dropped_in_v2 flag for out-of-scope posts.

Focus areas:
  1. pretraining-and-architecture
  2. post-training-and-fine-tuning
  3. alignment-and-safety
  4. interpretability
  5. evals-and-benchmarks
  6. quantization-and-efficiency
  7. agentic-systems
  8. harness-and-context-engineering

v2 drops (dropped_in_v2=TRUE):
  - inference optimization (speculative decoding, Flash Attention internals, KV cache, serving latency)
  - kernel-level work (CUDA, Triton, NCCL)
  - hardware benchmarks (AMD/NVIDIA/Gaudi) unless framed as training-efficiency
  - serving infra (auto-scaling, deployment, postgres scaling)
  - applied product case studies without methodology (most Vercel v0/AI-SDK posts)
"""
import csv
import re
from pathlib import Path

DATA = Path(__file__).parent

# Drop rules — matches title/slug/existing domain against out-of-scope patterns
DROP_RULES = [
    # Inference optimization
    (r"\b(speculative decod|kv cache|paged attention|flash attention|flashattention|continuous batch|dynamic batch|inference latency|inference throughput|serving latency|inference perform|serving perform)\b", "v2-drop-inference-optim"),
    # Kernel-level
    (r"\b(cuda kernel|triton kernel|nccl|gpu kernel|ptx|warp|memory coales)\b", "v2-drop-kernel"),
    # Hardware benchmarks without training framing
    (r"\b(h100|a100|mi250|gaudi|tensor core|amd mi|intel gaudi)\b", "v2-drop-hardware-benchmark"),
    # Serving infra
    (r"\b(auto[- ]?scal|postgres|model serving endpoint|serving infra|deployment pipeline|k8s|kubernetes)\b", "v2-drop-serving-infra"),
    # TensorRT / runtime
    (r"\b(tensorrt|vllm|tgi|text-generation-inference)\b", "v2-drop-inference-runtime"),
    # Pure enterprise/product integrations (ALH, governance, customer case studies)
    (r"\b(general availability|now available|press release|pricing|quarterly|fiscal|earnings|we're hiring|join our team|partnership)\b", "v2-drop-non-technical"),
]

# Focus-area rules — ORDER MATTERS; first match wins
FOCUS_AREA_RULES = [
    # 4. Interpretability (most specific — pattern tokens are unambiguous)
    ("interpretability",
     r"\b(interpretab|circuit(s)?\b|sae\b|sparse autoencoder|dictionary learn|monosemanti|feature viz|probing|probe\b|mechanistic|neuron|attention pattern|steering|activation steering|residual stream|induction head|superposition|activation patching)\b"),

    # 3. Alignment & safety (broadened)
    ("alignment-and-safety",
     r"\b(alignment|constitutional|rsp\b|responsible scaling|safeguard|red[- ]team|adversarial (prompt|example)|jailbreak|sandbag|deceptive|sycophan|reward hack|misalign|scheming|frontier safety|threat model|pre-deployment|evals? awareness|harm|misuse|safety policy|refusal|policy violation|alignment faking|claude\'s character|persona|model welfare|catastrophic|preparedness|monitorab|instruction hierarchy|model spec|confession|honest|chain.of.thought monitor|scalable oversight|faithful(ness)? of (reasoning|model)|sleeper agent|simple probes|influence functions|sabotag|treacherous|bioweapon|biosecur|cyber|cbrn|responsible.ai|responsible disclosure|dangerous capability)\b"),

    # 4. Evaluations & benchmarks
    ("evals-and-benchmarks",
     r"\b(benchmark|swe-bench|tau-bench|humaneval|gpqa|mmlu|browsecomp|officeqa|agentcompany|eval\s*(harness|suite|set)|evaluation (framework|suite|methodology)|leaderboard|helm\b|\bevals?\b|evmbench|gpqa|cybench|aisi|frontiermath|arc-agi|measuring (ai|model|the performance)|judge\b|reward model(ing)?|scoring|grading|rating|custom judges?)\b"),

    # 8. Harness & context engineering (before agentic, as it's more specific)
    ("harness-and-context-engineering",
     r"\b(harness|scaffolding|context engineering|prompt caching|agent skills|writing (tools|prompts) for|mcp\b|model context protocol|long[- ]running (agent|app|loop)|agent orchestration|agent-ops|system prompt)\b"),

    # 7. Agentic systems
    ("agentic-systems",
     r"\b(agent\b|agents\b|agentic|tool[- ]use|tool calling|function call|computer use|computer-use|browser[- ]use|coding agent|multi[- ]agent|subagent|autonomous|claude code|devin|cursor agent|copilot agent|claude opus.*(agent|ability)|agent trace|agent loop|agent benchmark|desktop agent|web agent)\b"),

    # 6. Quantization & efficiency
    ("quantization-and-efficiency",
     r"\b(quantiz|int8|int4|fp8|fp16|bitsandbytes|awq\b|gptq|bnb|8-bit|4-bit|lora\b|qlora|peft\b|parameter[- ]efficient|adapter|pruning|sparsity|model compression)\b"),

    # 2. Post-training & fine-tuning (broadened)
    ("post-training-and-fine-tuning",
     r"\b(rlhf|rlaif|rlvr|dpo\b|ppo\b|grpo|orpo|sft\b|instruction tuning|fine[- ]tun|post[- ]train|reward model|preference (model|optim)|distillation|on[- ]policy|off[- ]policy|reinforcement learning from|synthetic (data|preference)|kto\b|simpo|self-play|rejection sampling|human feedback|learn(ing)? from (human|preferences)|summariz(e|ation) with|iterated amplification|meta.learning|reptile|imitation learning|test.?time compute|tao\b|continued pre[- ]?train|post[- ]training|quick fix|best[- ]of[- ]n|process reward|step[- ]level reward)\b"),

    # 1. Pretraining & architecture (catch-all for training & model work)
    ("pretraining-and-architecture",
     r"\b(pretrain|pre[- ]train|scaling laws?|chinchilla|data mix|tokeniz|curriculum|moe\b|mixture of experts|mixtral|mamba|state space|ssm\b|hyena|rwkv|s4\b|architecture|new (attention|layer|model)|from scratch|foundation model|dbrx|mpt-|olmo|tulu|gemini|llama|mistral|grok|gpt-[0-9]|claude [0-9]|sonnet|opus|haiku|deepseek|training (data|dataset|from scratch)|loss (curve|landscape)|dense model|transformer improvement)\b"),
]

# Title-based hints that bump to specific focus_area even if other rules match first
TITLE_OVERRIDES = [
    # e.g., system cards -> safety-alignment (OVERRIDE agentic-systems)
    (r"system card", "alignment-and-safety"),
    (r"(threat model|misuse|red.?team|jailbreak|sabotage)", "alignment-and-safety"),
    (r"\b(olmo|tulu|mpt|dbrx|gemma|llama \d)\b.*(technical report|training|recipe)", "pretraining-and-architecture"),
    (r"\bmultimodal\b|\bvision\b.*(foundation|pretrain|architecture)", "pretraining-and-architecture"),
]

def classify_or_drop(row):
    """Returns (focus_area, dropped_in_v2, scope_reason)."""
    text = f"{row.get('title', '')} {row.get('id', '')} {row.get('url', '')} {row.get('technical_domain', '')}".lower()
    title = row.get('title', '').lower()

    # Drop rules first — but don't drop if post is primarily an agent / alignment / eval post
    # Safety check: if title has agent/alignment/eval keywords, keep it even if drop rule matches
    agent_safety_keywords = re.search(
        r"\b(agent|alignment|eval|benchmark|interpretab|rlhf|training|constitut|safety|harness|context engineering|system card)\b",
        title
    )

    for drop_rx, reason in DROP_RULES:
        if re.search(drop_rx, text, re.I):
            if not agent_safety_keywords:
                return (None, True, reason)

    # Company-specific Vercel filter: keep only agent/harness posts
    if row.get("company") == "vercel":
        is_agent_or_harness = re.search(
            r"\b(agent|agentic|tool|mcp|harness|context|workflow engine|durable execution|ai sdk|coding agent|agent infrastructure|sandbox)\b",
            text
        )
        if not is_agent_or_harness:
            return (None, True, "v2-drop-vercel-product")

    # Check title overrides first
    for override_rx, area in TITLE_OVERRIDES:
        if re.search(override_rx, title, re.I):
            return (area, False, "")

    # Focus area rules
    for area, rx in FOCUS_AREA_RULES:
        if re.search(rx, text, re.I):
            return (area, False, "")

    # Fallback: if title has 'how we built' or 'engineering' -> harness; else treat as ambiguous
    if re.search(r"\b(how we built|how we trained|how we use|lessons|retrospective|postmortem)\b", text, re.I):
        return ("harness-and-context-engineering", False, "")

    # If track is engineering or applied, default to harness; research defaults to pretraining
    track = row.get("track", "")
    if track in ("engineering", "applied"):
        return ("harness-and-context-engineering", False, "v2-default-harness")
    else:
        return ("pretraining-and-architecture", False, "v2-default-pretraining")


def main():
    master_path = DATA / "master.csv"
    rows = list(csv.DictReader(open(master_path)))
    fields = list(rows[0].keys())

    # Add new columns if missing
    if "focus_area" not in fields:
        fields.insert(fields.index("techniques") + 1, "focus_area")
    if "dropped_in_v2" not in fields:
        fields.insert(fields.index("in_scope") + 1, "dropped_in_v2")

    # Process only in-scope rows
    n_dropped = 0
    from collections import Counter
    by_area = Counter()

    for r in rows:
        # Ensure new cols exist on every row
        r.setdefault("focus_area", "")
        r.setdefault("dropped_in_v2", "FALSE")

        if r.get("in_scope") != "TRUE":
            r["focus_area"] = ""
            r["dropped_in_v2"] = "FALSE"  # irrelevant for out-of-scope v1 rows
            continue

        area, dropped, reason = classify_or_drop(r)
        if dropped:
            r["dropped_in_v2"] = "TRUE"
            r["focus_area"] = ""
            # Preserve v1 scope_reason, append v2 reason
            v1_reason = r.get("scope_reason", "")
            r["scope_reason"] = (v1_reason + "; " if v1_reason else "") + reason
            n_dropped += 1
        else:
            r["dropped_in_v2"] = "FALSE"
            r["focus_area"] = area
            by_area[area] += 1

    # Write back
    with open(master_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)

    print(f"Retagged master.csv: {len(rows)} total rows")
    print(f"  In-scope v1: {sum(1 for r in rows if r.get('in_scope') == 'TRUE')}")
    print(f"  Dropped in v2: {n_dropped}")
    print(f"  Still in-scope v2: {sum(1 for r in rows if r.get('in_scope') == 'TRUE' and r.get('dropped_in_v2') == 'FALSE')}")
    print(f"\nBy focus area:")
    for a, c in by_area.most_common():
        print(f"  {a:40} {c}")

    # By company after v2 filter
    by_co_v2 = Counter()
    for r in rows:
        if r.get("in_scope") == "TRUE" and r.get("dropped_in_v2") == "FALSE":
            by_co_v2[r.get("company", "?")] += 1
    print("\nBy company (v2 in-scope):")
    for co, c in by_co_v2.most_common():
        print(f"  {co:25} {c}")

if __name__ == "__main__":
    main()
