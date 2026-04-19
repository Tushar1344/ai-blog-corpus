#!/usr/bin/env python3
"""Heuristically assign contribution_type, technical_domain, techniques based on title/slug/company/track.

Run on master.csv after consolidation. Writes back to master.csv.
These are first-pass tags — summarization agents will refine them with full content.
"""
import csv
import re
from pathlib import Path

DATA = Path(__file__).parent

# ---- Axis A: Contribution type ----
CONTRIB_RULES = [
    # Order matters - first match wins
    ("dataset-benchmark", r"\b(benchmark|eval\b|evals\b|evaluation set|dataset|harness|test suite|mmlu|swe-bench|tau-bench|humaneval|browsecomp|gpqa|officeqa|agentcompany)\b"),
    ("interpretability-finding", r"\b(interpretab|circuits?|feature|attention|neuron|probe|probing|steering|sae\b|sparse autoencoder|activation|mechanistic|find[s]? that .* inside|monosemantic)\b"),
    ("infra-release", r"\b(release|library|framework|toolkit|open-source|open source|composer|llm foundry|streaming dataset|vllm|tokenkit|tinker|sdk|we open source|we're open)\b"),
    ("retrospective-case-study", r"\b(postmortem|retro(spective)?|how we built|how we trained|how we use|how we deployed|lessons|we learned|case study|in production|shipping|behind the scenes|in-house|scaling \w+ \w+ in production)\b"),
    ("position-policy", r"\b(policy|responsible|transparency|governance|frontier (safety|policy|ai)|alignment (plan|faking|roadmap)|constitution|constitutional (ai|approach)|rsp\b|safeguards|misuse|threat model|our (approach|view|commitment|stance)|responsible scaling|core views)\b"),
    ("new-method", r"\b(introducing|propose|new method|novel|we develop|we introduce|we present|new (approach|technique|algorithm)|a better|improved|learning from|training on|reward|rlhf|rlvr|dpo\b|distillation|fine-tun|speculative decoding|model merging)\b"),
    ("empirical-study", r"\b(study|investigation|analysis|examining|we analyze|we find|find[s]? that|evaluating|empirical|impact of|effect of|correlates|measuring|predicting|in the wild|across models|systematically)\b"),
]

# ---- Axis B: Technical domain ----
DOMAIN_RULES = [
    ("interpretability", r"\b(interpretab|circuits?|feature viz|sae\b|sparse autoencoder|mechanistic|attention pattern|probing|neuron|dictionary learning|monosemantic)\b"),
    ("safety-alignment", r"\b(alignment|safety|misalign|jailbreak|red[- ]team|adversarial|constitutional|rlhf|rlaif|reward hack|sycophan|deceptive|sandbag|eval awareness|refuse|policy|rsp|safeguard|harm|misuse|threat)\b"),
    ("agents", r"\b(agent|agentic|tool use|tool-use|tool calling|browser use|computer use|coding agent|devin|cursor agent|claude code|multi-agent|subagent|task planning|autonomous)\b"),
    ("evals-benchmarks", r"\b(benchmark|swe-bench|tau-bench|humaneval|gpqa|mmlu|browsecomp|officeqa|agentcompany|eval\b|evals\b|evaluation|test suite)\b"),
    ("pretraining", r"\b(pretrain|pre-train|training from scratch|scaling laws?|chinchilla|data mix|tokeniz|curriculum|moe\b|mixture of experts|architecture|foundation model|from scratch|dense model|mpt-|dbrx|composer|llm foundry)\b"),
    ("post-training", r"\b(post-train|post train|rlhf|rlaif|dpo\b|rlvr|constitutional|fine-tun|sft\b|instruction tuning|reward model|preference|distillation|on-policy|off-policy|kl penalty|ppo\b|reward hack)\b"),
    ("inference", r"\b(inference|decoding|speculative|quantiz|kv cache|attention optimization|flash attention|long context|long-context|serving latency|batch|throughput|compile|tensor parallel|pipeline parallel|inference time|test[- ]time compute|warp decode)\b"),
    ("multimodal", r"\b(multi[- ]?modal|vision|image|audio|video|speech|whisper|dall-e|sora|text-to-image|diffusion|image generation|vision-language|vlm\b|clip)\b"),
    ("training-infra", r"\b(training infrastructure|distributed training|mosaic|streaming|gpu|cluster|nccl|deepspeed|fsdp|megatron|pytorch|tpu|a100|h100|compute utilization|mfu\b)\b"),
    ("serving-infra", r"\b(serving|deployment|production|auto-?scaling|k8s|kubernetes|reliability|latency|edge|runtime|streaming|load balanc|postgres|cache|model serving|inference endpoint)\b"),
    ("applied-product", r"\b(copilot|chatgpt|claude code|cursor|devin|github copilot|v0|ai sdk|mcp\b|integration|workflow|use case|real[- ]world|enterprise)\b"),
]

# ---- Axis E: Techniques (multi-select) ----
TECH_RULES = {
    "SAE": r"\b(sae\b|sparse autoencoder)\b",
    "MoE": r"\b(moe\b|mixture of experts|mixtral)\b",
    "speculative-decoding": r"\b(speculative (decoding|sampling)|warp decode|draft model)\b",
    "chain-of-thought": r"\b(chain[- ]of[- ]thought|cot\b|scratchpad|reasoning trace)\b",
    "RLHF": r"\b(rlhf|reward model|preference model|helpful, harmless)\b",
    "RLVR": r"\b(rlvr|reinforcement learning with verifiable rewards|verifiable rewards)\b",
    "constitutional-AI": r"\b(constitutional ai|constitutional approach)\b",
    "DPO": r"\b(dpo\b|direct preference optimization)\b",
    "long-context": r"\b(long[- ]context|long context|100k|200k|1m context|million[- ]token|context window)\b",
    "flash-attention": r"\b(flash attention|flash-attention|flashattention)\b",
    "KV-cache": r"\b(kv cache|kv-cache|key-value cache|paged attention|vllm)\b",
    "quantization": r"\b(quantiz|int8|int4|fp8|bitsandbytes|awq|gptq)\b",
    "distillation": r"\b(distillation|student model|teacher model|on-policy distillation)\b",
    "tool-use": r"\b(tool use|tool-use|tool calling|function calling|mcp\b)\b",
    "computer-use": r"\b(computer use|computer-use|desktop agent|claude computer)\b",
    "coding-agents": r"\b(coding agent|code agent|devin|claude code|cursor|swe-bench|code generation)\b",
    "prompt-caching": r"\b(prompt cach|anthropic cache|cache hit)\b",
    "context-engineering": r"\b(context engineering|context engineerin|prompt engineering|prompt design)\b",
    "test-time-compute": r"\b(test[- ]time compute|test-time scaling|inference[- ]time scaling|best[- ]of[- ]n|majority vote|o1\b)\b",
    "reward-modeling": r"\b(reward model|reward modeling|reward hacking|reward function)\b",
    "red-teaming": r"\b(red[- ]team|red team|red-team|adversarial prompt)\b",
    "jailbreak": r"\b(jailbreak|jail-break|many-shot jailbreak)\b",
    "steering": r"\b(steer(ing)?|activation steering|vector steering|residual stream)\b",
    "probing": r"\b(probing|probe\b|linear probe|concept probing)\b",
    "scaling-laws": r"\b(scaling laws?|chinchilla|compute optimal)\b",
    "retrieval-augmentation": r"\b(rag\b|retrieval[- ]augmented|retrieval augmentation|retriever|embedder)\b",
    "SWE-bench": r"\b(swe-bench|swe bench|swebench)\b",
    "Tau-Bench": r"\b(tau-bench|tau bench|taubench)\b",
    "BrowseComp": r"\b(browsecomp|browse comp)\b",
    "circuits": r"\b(circuits?|induction head|attention circuit|monosemantic)\b",
    "interpretability-features": r"\b(feature viz|monosemantic|superposition|dictionary learning)\b",
    "MCP": r"\b(mcp\b|model context protocol)\b",
    "evals-eval-harness": r"\b(evals?|eval harness|evaluation suite|benchmark)\b",
    "alignment-faking": r"\b(alignment faking|deceptive alignment|sandbagging)\b",
    "sycophancy": r"\b(sycophan|sycophantic|flattery)\b",
    "multi-agent": r"\b(multi[- ]agent|subagent|orchestration|agent fleet)\b",
    "fine-tuning": r"\b(fine[- ]tun|sft\b|instruction tuning|lora\b)\b",
    "training-dynamics": r"\b(loss curve|training dynamics|gradient|optimizer|adam|sgd|muon)\b",
    "synthetic-data": r"\b(synthetic data|self[- ]instruct|self-play)\b",
    "safety-evals": r"\b(safety eval|capability eval|evals for (safety|misalignment))\b",
}

def tag_row(row):
    text = f"{row.get('title', '')} {row.get('id', '')} {row.get('url', '')}".lower()

    # Contribution type
    for ct, rx in CONTRIB_RULES:
        if re.search(rx, text, re.I):
            row["contribution_type"] = ct
            break
    if not row.get("contribution_type"):
        row["contribution_type"] = "empirical-study"  # default

    # Technical domain
    for d, rx in DOMAIN_RULES:
        if re.search(rx, text, re.I):
            row["technical_domain"] = d
            break
    if not row.get("technical_domain"):
        # Infer from track
        track = row.get("track", "")
        if track == "engineering":
            row["technical_domain"] = "applied-product"
        else:
            row["technical_domain"] = "applied-product"

    # Techniques (multi)
    techniques = []
    for t, rx in TECH_RULES.items():
        if re.search(rx, text, re.I):
            techniques.append(t)
    row["techniques"] = "|".join(techniques)

    return row

def main():
    master_path = DATA / "master.csv"
    rows = list(csv.DictReader(open(master_path)))
    for r in rows:
        if r["in_scope"] == "TRUE":
            tag_row(r)

    fieldnames = list(rows[0].keys())
    with open(master_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)

    # Report
    from collections import Counter
    ct = Counter(r["contribution_type"] for r in rows if r["in_scope"] == "TRUE")
    td = Counter(r["technical_domain"] for r in rows if r["in_scope"] == "TRUE")
    all_tech = []
    for r in rows:
        if r["in_scope"] == "TRUE" and r["techniques"]:
            all_tech.extend(r["techniques"].split("|"))
    tc = Counter(all_tech)

    print("Contribution type:")
    for k, v in ct.most_common():
        print(f"  {k:30} {v}")
    print("\nTechnical domain:")
    for k, v in td.most_common():
        print(f"  {k:30} {v}")
    print("\nTop techniques:")
    for k, v in tc.most_common(20):
        print(f"  {k:30} {v}")

if __name__ == "__main__":
    main()
