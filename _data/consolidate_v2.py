#!/usr/bin/env python3
"""Consolidate v1 master + Tier 1 additions into unified master.csv.

Inputs:
- master.csv (v1 + v2 retagged, 1054 rows)
- enum-google-research.csv (107)
- enum-meta-fair.csv (600)
- enum-huggingface.csv (691)
- enum-deepseek.csv (20)
- enum-deepmind.csv (320)
- enum-ai2.csv (139)

Applies v2 substance filter + focus_area to new rows, merges, writes back master.csv.
"""
import csv
import re
from pathlib import Path
from collections import Counter

DATA = Path(__file__).parent

FIELDS = ["id", "company", "track", "title", "url", "publish_date", "authors",
          "in_scope", "dropped_in_v2", "scope_reason", "summary", "contribution_type",
          "technical_domain", "techniques", "focus_area", "year", "md_anchor", "notes"]

# v2 drop patterns (same as assign_focus_area.py)
DROP_RX = re.compile(
    r"\b(speculative decod|kv cache|paged attention|flash attention|flashattention|continuous batch|dynamic batch|inference latency|inference throughput|serving latency|inference perform|serving perform"
    r"|cuda kernel|triton kernel|nccl|gpu kernel|ptx|warp|memory coales"
    r"|h100|a100|mi250|gaudi|tensor core|amd mi|intel gaudi"
    r"|auto[- ]?scal|postgres|model serving endpoint|serving infra|deployment pipeline|k8s|kubernetes"
    r"|tensorrt|\bvllm\b|\btgi\b|text-generation-inference"
    r"|general availability|now available|press release|pricing|quarterly|fiscal|earnings|we're hiring|join our team|partnership"
    r")\b", re.I)

# For new companies — extra drop patterns specific to non-AI content
NON_AI_DROP_RX = re.compile(
    r"\b(covid|crisis|disaster|social good|climate|earthquake|humanitarian|public health|2africa"
    r"|connectivity|subsea cable|internet access|partnership with unicef"
    r"|anniversary"
    r"|quantum (computing|neural network|algorithm|processor|supremacy)|qubit|superconducting"
    r"|advertising|ad tech|metaverse|vr headset|horizon worlds"
    r"|diversity|inclusion program|internship|we're hiring|join us"
    r"|sponsoring|interviewed|keynote"
    r"|getting started with|how to (use|install|deploy|run|setup)|tutorial|walkthrough"
    r"|welcome to|announces partnership|in conversation with"
    r"|employee spotlight|life at|meet the team|we're excited to|we are excited to"
    r"|community (highlights|spotlight)|community (roundup|digest)"
    r"|bold science|health equity|workforce|fashion app|canopy height"
    r"|5g|millimeter wave|wireless|mobile network|telecom"
    r")", re.I)

# Focus area rules — abbreviated version of assign_focus_area.py
FA_RULES = [
    ("interpretability", r"\b(interpretab|circuit(s)?\b|sae\b|sparse autoencoder|dictionary learn|monosemanti|feature viz|probing|mechanistic|steering|residual stream|induction head|superposition|activation patching)\b"),
    ("alignment-and-safety", r"\b(alignment|constitutional|rsp\b|responsible scaling|safeguard|red[- ]team|adversarial prompt|jailbreak|sandbag|deceptive|sycophan|reward hack|misalign|scheming|frontier safety|threat model|pre-deployment|harm|misuse|safety policy|alignment faking|sleeper agent|monitorab|preparedness|dangerous capability|bioweapon|biosecur|cbrn|cyber safety|weaponiz|responsible.ai)\b"),
    ("evals-and-benchmarks", r"\b(benchmark|swe-bench|tau-bench|humaneval|gpqa|mmlu|browsecomp|officeqa|agentcompany|eval\s*(harness|suite|set)|evaluation (framework|suite|methodology)|leaderboard|helm\b|\bevals?\b|frontiermath|arc-agi|measuring (ai|model)|judge\b|custom judges?|paloma)\b"),
    ("harness-and-context-engineering", r"\b(harness|scaffolding|context engineering|prompt caching|agent skills|writing (tools|prompts) for|\bmcp\b|model context protocol|long[- ]running (agent|app|loop)|agent orchestration|agent-ops|system prompt)\b"),
    ("agentic-systems", r"\b(agent\b|agents\b|agentic|tool[- ]use|tool calling|function call|computer use|browser[- ]use|coding agent|multi[- ]agent|subagent|autonomous|claude code|devin|cursor agent|copilot agent|agent trace|agent loop|agent benchmark|desktop agent|web agent|embodied ai|habitat|simulator)\b"),
    ("quantization-and-efficiency", r"\b(quantiz|int8|int4|fp8|fp16|bitsandbytes|awq\b|gptq|bnb|8-bit|4-bit|lora\b|qlora|peft\b|parameter[- ]efficient|adapter|pruning|sparsity|model compression)\b"),
    ("post-training-and-fine-tuning", r"\b(rlhf|rlaif|rlvr|\bdpo\b|\bppo\b|grpo|orpo|\bsft\b|instruction tuning|fine[- ]tun|post[- ]train|reward model|preference (model|optim)|distillation|on[- ]policy|off[- ]policy|rl from|synthetic (data|preference)|\bkto\b|simpo|self-play|rejection sampling|human feedback|learn(ing)? from (human|preferences)|summariz(e|ation) with|iterated amplification|meta.learning|reptile|imitation learning|test.?time compute|\btao\b|continued pre[- ]?train|process reward|step[- ]level reward|tulu)\b"),
    ("pretraining-and-architecture", r"\b(pretrain|pre[- ]train|scaling laws?|chinchilla|data mix(ing|ture)|tokeniz|curriculum learning|\bmoe\b|mixture of experts|mixtral|mamba|state space model|\bssm\b|hyena|rwkv|\bs4\b|from scratch|foundation model|\bdbrx\b|\bmpt\b|\bolmo\b|gemini (technical|\d)|llama [\d.]+\s*(technical|paper|model|release|3|4)|mistral|grok-\d|gpt-[0-9](\.\d+)?(\s+(technical|system))?|claude [234]|opus (\d|4)|sonnet \d|haiku \d|deepseek-(v\d|r\d|coder|math|prover|moe|vl|llm)|training (dataset|from scratch|recipe)|loss landscape|dense model|new transformer|new (attention|layer|architecture|model architecture)|dolma|fineweb|cosmopedia|smollm|ultrachat|ultrafeedback|tulu|finepdfs|linear attention|sliding window attention|rotary embed|rope|hybrid architecture|diffusion model|vjepa|v-jepa|\bjepa\b|dinov|\bsam\b|\bsam2\b|segment anything|image pretrain|video pretrain|multimodal pretrain|encoder-only|decoder-only|tokenizer)\b"),
]

def classify(row):
    """Return (focus_area, dropped, reason)."""
    text = f"{row.get('title','')} {row.get('id','')} {row.get('url','')} {row.get('technical_domain','')}".lower()
    title = (row.get('title') or '').lower()
    company = row.get('company', '')

    # Check for agent/alignment/eval keywords to protect from drops
    protection = re.search(r"\b(agent|alignment|eval|benchmark|interpretab|rlhf|training|constitut|safety|harness|context engineering|system card|olmo|llama|dbrx|mpt|gemini|gemma|deepseek|tulu|dolma|fineweb)\b", title)

    # v2 drop — inference/kernel/serving
    if DROP_RX.search(text) and not protection:
        return (None, True, "v2-drop-inference-kernel-serving")

    # Non-AI content drop (Meta/Google specific)
    if company in ("meta-fair", "google-research") and NON_AI_DROP_RX.search(text):
        return (None, True, "v2-drop-non-ai")

    # Title overrides (high priority)
    if re.search(r"system card|preparedness framework|threat model|frontier safety", title):
        return ("alignment-and-safety", False, "")

    for area, rx in FA_RULES:
        if re.search(rx, text, re.I):
            return (area, False, "")

    # No specific rule matched — DROP as unclassifiable (don't default to pretraining)
    # Exception: existing v1 companies keep their default behavior (they were manually reviewed)
    if company in ("anthropic", "openai", "databricks", "cursor", "vercel", "cognition", "thinking-machines"):
        track = row.get("track", "")
        if track in ("engineering", "applied"):
            return ("harness-and-context-engineering", False, "v2-default-harness")
        return ("pretraining-and-architecture", False, "v2-default-pretraining")
    # New companies: drop if unclassifiable
    return (None, True, "v2-drop-unclassifiable")

def main():
    master_path = DATA / "master.csv"
    rows = list(csv.DictReader(open(master_path)))
    print(f"Loaded master: {len(rows)} existing rows")

    # Normalize fields on existing rows
    for r in rows:
        for f in FIELDS:
            r.setdefault(f, "")

    existing_ids = {r["id"] for r in rows}

    # Merge in Tier 1 files
    new_files = [
        ("enum-google-research.csv", "google-research"),
        ("enum-meta-fair.csv", "meta-fair"),
        ("enum-huggingface.csv", "huggingface"),
        ("enum-deepseek.csv", "deepseek"),
        ("enum-deepmind.csv", "deepmind"),
        ("enum-ai2.csv", "ai2"),
    ]
    added = 0
    for fn, co in new_files:
        path = DATA / fn
        if not path.exists():
            print(f"SKIP {fn}")
            continue
        for r in csv.DictReader(open(path)):
            if r["id"] in existing_ids:
                continue
            out = {k: r.get(k, "") for k in FIELDS}
            out["in_scope"] = r.get("in_scope", "TRUE")
            out["dropped_in_v2"] = "FALSE"
            # Classify
            area, dropped, reason = classify(out)
            if dropped:
                out["dropped_in_v2"] = "TRUE"
                out["focus_area"] = ""
                out["scope_reason"] = reason
            else:
                out["focus_area"] = area
            if out.get("publish_date"):
                out["year"] = out["publish_date"][:4]
            # md_anchor
            company_file = {
                "google-research": "google-research",
                "meta-fair": "meta-fair",
                "huggingface": "huggingface",
                "deepseek": "deepseek",
                "deepmind": "deepmind",
                "ai2": "ai2",
            }.get(out["company"], out["company"])
            out["md_anchor"] = f"by-company/{company_file}.md#{out['id']}"
            rows.append(out)
            added += 1

    # Write back
    with open(master_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)

    print(f"\nAdded {added} new rows. Total master: {len(rows)}")

    # Reports
    from collections import Counter
    in_scope_v2 = [r for r in rows if r["in_scope"] == "TRUE" and r["dropped_in_v2"] == "FALSE"]
    print(f"\nIn-scope v2: {len(in_scope_v2)}")

    print("\nBy company:")
    by_co = Counter(r["company"] for r in in_scope_v2)
    for co, c in by_co.most_common():
        print(f"  {co:25} {c}")

    print("\nBy focus area:")
    by_fa = Counter(r["focus_area"] for r in in_scope_v2)
    for fa, c in by_fa.most_common():
        print(f"  {fa:40} {c}")

    print("\nDropped in v2:")
    by_drop = Counter(r["scope_reason"] for r in rows if r["dropped_in_v2"] == "TRUE")
    for reason, c in by_drop.most_common()[:10]:
        print(f"  {reason[:60]:60} {c}")

if __name__ == "__main__":
    main()
