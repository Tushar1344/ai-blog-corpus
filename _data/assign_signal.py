#!/usr/bin/env python3
"""Assign signal scores on 3 dimensions: learning, novelty, actionability.

Each: H / M / L
Overall score = sum(H=3, M=2, L=1) → range 3-9
Priority rank = custom weighting (novelty 1.2x, learning 1.1x, actionability 1.0x)

Learning: does this teach a fundamental concept or build your mental model?
Novelty: is this a new idea, method, finding, or architecture vs. rehash/explainer?
Actionability: can you directly apply this? (code, recipe, technique, clear takeaway)
"""
import csv
import re
from pathlib import Path
from collections import Counter

DATA = Path(__file__).parent

# =====================================================================
# Scoring heuristics
# =====================================================================

# Patterns that indicate HIGH LEARNING (fundamental concepts, theory, deep explanation)
LEARNING_H = re.compile(
    r"\b(technical report|scaling laws?|mathematical framework|theoretical|theory of|"
    r"primer|fundament|first principles|deriv|proof|"
    r"why (language|transformer|model)|how (transform|attention|rlhf|rl) works|"
    r"understanding |interpret|circuit|monosemantic|feature viz|"
    r"(new )?(architecture|arch|attention mechanism|layer design)|"
    r"deep dive|technical deep|comprehensive|"
    r"on the (importance|role|nature|design) of|"
    r"teaching |explain(ing|er)?|foundational)\b",
    re.I,
)
LEARNING_L = re.compile(
    r"\b(now available|announcing|ga release|launching|partners?with|"
    r"customer (stor|success|spotlight)|we're hiring|join us|"
    r"monthly (digest|recap)|press release|funding|acquired|we raised|"
    r"hello\b|welcome\b|^introducing (langsmith|langgraph|langchain))\b",
    re.I,
)

# Patterns indicating HIGH NOVELTY (new methods, findings, architectures)
NOVELTY_H = re.compile(
    r"\b(new method|novel|first[- ](ever|time)|we (introduce|propose|present|develop)|"
    r"state[- ]of[- ]the[- ]art|sota|"
    r"new (architecture|attention|layer|benchmark|dataset|algorithm|framework)|"
    r"(new|our|a)\s+(benchmark|eval|dataset)|we find (that|a)|finding that|discover|"
    r"breaking (the barrier|new ground)|breakthrough|beyond|outperform|"
    r"mamba|\bssm\b|state space|hyena|rwkv|mixattention|warp decode|multi-head latent|"
    r"rlvr|verifiable rewards|on-policy distillation|"
    r"alignment faking|sleeper agent|deceptive alignment|"
    r"circuits update|sparse autoencoder|\bsae\b|monosemantic|"
    r"the ai scientist|transformer squared|continuous thought|namm|"
    r"gspo|qwen3|mixtral|dbrx|\br1\b|deepseek[- ](v\d|r\d|prover|moe)|"
    r"jamba|olmo|tulu|dolma|fineweb|cosmopedia|smollm|gato|alpha(fold|geom|proof|evolve|zero|go)|"
    r"v-?jepa|\bjepa\b|\bsam2\b|segment anything|dino|"
    r"don.?t build multi|why swe-bench|evaluations? don.?t|infrastructure noise|eval awareness|"
    r"constitutional (ai|classifier)|responsible scaling|preparedness|frontier safety|"
    r"harness (design|engineering)|context engineering|multi[- ]agent research)\b",
    re.I,
)
NOVELTY_L = re.compile(
    r"\b(tutorial|getting started|how to (use|install|deploy|run|setup|build.*app)|"
    r"walkthrough|integration|\bsdk\b|partnership|case stud|"
    r"(\d+ )?ways to|\btips\b|checklist|roundup|recap|digest|"
    r"what is |an? introduction to |overview of|primer on|glossary|"
    r"using (x|\w+) with (y|\w+)|(with|for) (pinecone|weaviate|qdrant|chroma|snowflake)|"
    r"announcing (our|the)?|now (available|live|generally))\b",
    re.I,
)

# Patterns indicating HIGH ACTIONABILITY (recipes, how-we-built, specific techniques)
ACTION_H = re.compile(
    r"\b(how we (built|trained|use|made|shipped|deploy)|recipe|best practice|"
    r"step[- ]by[- ]step|playbook|guide to|we open[- ]source|releasing|available (on|at)|"
    r"technical (report|guide)|model card|hyperparameter|configuration|"
    r"training (setup|recipe|procedure)|code (release|repo|available)|"
    r"lessons (learned|from)|postmortem|retro|"
    r"template|framework (for building|to build)|"
    r"production (agent|system)|in production|at scale|"
    r"benchmark (release|code)|open[- ]source (implementation|code)|github)\b",
    re.I,
)
ACTION_L = re.compile(
    r"\b(responsible (ai|scaling)|safety policy|position|perspective|our (view|stance|approach)|"
    r"policy|governance|societal impact|economic (index|impact)|"
    r"community spotlight|event|meetup|conference summary|invited talk|"
    r"labor market|usage study|who uses|how (australia|india|uk|us) uses|country brief)\b",
    re.I,
)

# ============================================================
# Per-focus-area + subcategory overrides
# ============================================================

SUB_BIAS = {
    # (dimension, bias): sub → delta
    # Boost or penalty on specific subcategories
    "research-techniques-and-methods": {"learning": +1, "novelty": +1},
    "architectures":                   {"learning": +1, "novelty": +1, "actionability": +1},
    "foundation-model-releases":       {"learning": +1, "novelty": 0, "actionability": +1},
    "scaling-and-training-dynamics":   {"learning": +1, "novelty": 0},
    "data-and-tokenization":           {"learning": +1, "actionability": +1},
    "training-stack":                  {"actionability": +1},
    "multimodal-pretraining":          {"novelty": 0, "actionability": 0},

    "rlvr-verifiable-rewards":         {"learning": +1, "novelty": +1, "actionability": +1},
    "rlhf-classic":                    {"learning": +1},
    "direct-preference":               {"learning": +1, "novelty": +1},
    "distillation":                    {"learning": +1, "novelty": +1},

    "circuits-and-mechanistic":        {"learning": +1, "novelty": +1},
    "saes-and-dictionary-learning":    {"learning": +1, "novelty": +1},
    "steering-and-intervention":       {"novelty": +1},

    "deceptive-alignment":             {"learning": +1, "novelty": +1},
    "constitutional-and-self-critique":{"learning": +1},
    "capability-evals-for-safety":     {"learning": +1},
    "red-teaming-and-jailbreaking":    {"novelty": 0, "actionability": 0},
    "scalable-oversight":              {"learning": +1},

    "benchmark-critique":              {"learning": +1, "novelty": +1},
    "benchmark-release":               {"actionability": +1, "novelty": 0},
    "judge-models-and-methodology":    {"learning": +1, "actionability": +1},
    "eval-systems-and-harnesses":      {"actionability": +1},

    "context-engineering":             {"learning": +1, "actionability": +1},
    "long-running-harnesses":          {"actionability": +1},
    "mcp-and-tool-protocols":          {"actionability": +1},
    "codex-and-sora-harness":          {"actionability": +1},

    "coding-agents":                   {"actionability": +1},
    "multi-agent-orchestration":       {"novelty": 0, "actionability": 0},
    "computer-use-and-browser-use":    {"novelty": +1},
    "agent-frameworks-and-tooling":    {"actionability": +1},
    "agent-design-and-patterns":       {"learning": +1},
    "game-and-rl-agents":              {"learning": +1},

    # Penalties
    "societal-impact-and-deployment-studies": {"learning": -1, "actionability": -1},
    "system-cards":                    {"learning": -1, "novelty": -1, "actionability": 0},
    "responsible-scaling-and-policy":  {"actionability": -1},
    "ai-sdk-and-product-tooling":      {"learning": -1},
    "databricks-training-stack-misc":  {"actionability": +1},
    "data-analyst-and-workflow-agents":{"learning": -1},
    "safety-research-general":         {},
    "leaderboards-and-community-evals":{},
    "agents-general":                  {"learning": -1, "novelty": -1},
    "dialogue-and-conversational-agents":{"novelty": -1},

    # Fallbacks — usually low-signal
    "fallback-architecture":           {"learning": -1, "novelty": -1},
    "fallback-alignment":              {"novelty": -1},
    "fallback-agents":                 {"novelty": -1},
    "fallback-harness":                {"novelty": -1},
    "fallback-evals":                  {"novelty": -1},
    "fallback-post-training":          {"novelty": 0},
    "fallback-interp":                 {},
    "fallback-efficiency":             {},
}

# Company biases (publication pedigree)
# High novelty labs publish more novel research than framework companies.
COMPANY_BIAS = {
    "thinking-machines": {"novelty": +1, "learning": +1},
    "deepseek": {"novelty": +1, "learning": +1},
    "sakana": {"novelty": +1},
    "anthropic": {"learning": +1},  # Strong on fundamentals + interpretability
    "ai2": {"actionability": +1},    # Full recipe/data published
    "cognition": {"actionability": +1},
    "cursor": {"actionability": +1, "learning": +1},
    "qwen": {"actionability": +1},
    "mistral": {"actionability": +1},
    "moonshot": {"novelty": +1},
    "openai": {"learning": +1},      # Historical RL/GAN research is high learning
    "deepmind": {"novelty": +1, "learning": +1},
    "meta-fair": {"novelty": 0},
    "huggingface": {"actionability": +1},
    "ai21": {"novelty": +1},         # Jamba + Mamba-hybrid work
    "langchain": {"actionability": +1, "novelty": -1},  # Framework, strong on how-to, less novel
    "databricks": {"actionability": +1},
    "vercel": {"actionability": +1, "novelty": -1},
    "google-research": {"novelty": 0},
}

def score_to_letter(score):
    """Calibrated: 3-4 → L, 5-6 → M, 7+ → H."""
    if score >= 7:
        return "H"
    if score >= 5:
        return "M"
    return "L"

def classify_signals(row):
    """Return (learning, novelty, actionability, summary_note)."""
    title = row.get("title", "") or ""
    text = f"{title} {row.get('id', '')}".lower()
    sub = row.get("subcategory", "")
    fa = row.get("focus_area", "")
    co = row.get("company", "")
    summary = (row.get("summary", "") or "").lower()
    full_text = f"{title} {summary} {row.get('id', '')}".lower()

    # Base score 5 (borderline M)
    L = N = A = 5

    # Apply big signal regexes
    if LEARNING_H.search(full_text):
        L += 2
    if LEARNING_L.search(full_text):
        L -= 2
    if NOVELTY_H.search(full_text):
        N += 2
    if NOVELTY_L.search(full_text):
        N -= 2
    if ACTION_H.search(full_text):
        A += 2
    if ACTION_L.search(full_text):
        A -= 2

    # Subcategory bias
    bias = SUB_BIAS.get(sub, {})
    L += bias.get("learning", 0)
    N += bias.get("novelty", 0)
    A += bias.get("actionability", 0)

    # Company bias
    cb = COMPANY_BIAS.get(co, {})
    L += cb.get("learning", 0)
    N += cb.get("novelty", 0)
    A += cb.get("actionability", 0)

    # Penalize posts with no date (likely slug-derived, low signal)
    if not row.get("publish_date"):
        L -= 1
        N -= 1
        A -= 1

    # Penalize posts with tiny title (likely stub)
    if len(title) < 15:
        L -= 1
        N -= 1
        A -= 1

    # Bonus: posts with content summary (we read them)
    if row.get("summary"):
        L += 1  # reading gave us actual content to grade

    # Clamp 3..10
    L = max(3, min(10, L))
    N = max(3, min(10, N))
    A = max(3, min(10, A))

    return score_to_letter(L), score_to_letter(N), score_to_letter(A), f"L{L}N{N}A{A}"

def main():
    path = DATA / "master.csv"
    rows = list(csv.DictReader(open(path)))
    fields = list(rows[0].keys())

    # Add signal columns if missing
    for col in ["signal_learning", "signal_novelty", "signal_actionability", "signal_overall", "signal_priority"]:
        if col not in fields:
            # Insert after subcategory (before year)
            idx = fields.index("subcategory") if "subcategory" in fields else len(fields) - 3
            fields.insert(idx + 1, col)

    scored = 0
    for r in rows:
        if r.get("in_scope") != "TRUE" or r.get("dropped_in_v2") == "TRUE":
            for col in ["signal_learning", "signal_novelty", "signal_actionability", "signal_overall", "signal_priority"]:
                r[col] = r.get(col, "")
            continue
        l, n, a, debug = classify_signals(r)
        # Overall signal — balanced distribution target: ~15% H / ~45% M / ~40% L
        letters = [l, n, a]
        nH = letters.count("H")
        nM = letters.count("M")
        nL = letters.count("L")
        if nH >= 2:
            overall = "H"
        elif nH == 1 and nL == 0:
            overall = "H"  # e.g. HMM
        elif nH == 1 and nL >= 1:
            overall = "M"  # e.g. HML
        elif nL >= 2 and nH == 0:
            overall = "L"
        else:
            overall = "M"
        # Priority = weighted sum (novelty 1.2x, learning 1.1x, action 1.0x) → raw 0–10
        wL = {"H": 3, "M": 2, "L": 1}
        priority = round(wL[n] * 1.2 + wL[l] * 1.1 + wL[a] * 1.0, 1)

        r["signal_learning"] = l
        r["signal_novelty"] = n
        r["signal_actionability"] = a
        r["signal_overall"] = overall
        r["signal_priority"] = f"{priority}"
        scored += 1

    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)

    print(f"Scored {scored} in-scope posts\n")
    in_scope = [r for r in rows if r.get("in_scope") == "TRUE" and r.get("dropped_in_v2") == "FALSE"]

    print("signal_overall distribution:")
    for k, v in Counter(r["signal_overall"] for r in in_scope).most_common():
        print(f"  {k}: {v} ({100*v/len(in_scope):.0f}%)")

    print("\nHigh-signal by company:")
    h_by_co = Counter(r["company"] for r in in_scope if r["signal_overall"] == "H")
    total_by_co = Counter(r["company"] for r in in_scope)
    for co, c in h_by_co.most_common():
        pct = 100 * c / total_by_co[co] if total_by_co[co] else 0
        print(f"  {co:25} {c}/{total_by_co[co]} ({pct:.0f}% high-signal)")

    print("\nHigh-signal by focus area:")
    h_by_fa = Counter(r["focus_area"] for r in in_scope if r["signal_overall"] == "H")
    for fa, c in h_by_fa.most_common():
        total = sum(1 for r in in_scope if r["focus_area"] == fa)
        print(f"  {fa:40} {c}/{total} ({100*c/total:.0f}%)")

    print("\nTop 20 posts by priority (novelty + learning + action):")
    ranked = sorted(in_scope, key=lambda r: -float(r["signal_priority"] or 0))
    for r in ranked[:20]:
        print(f"  [{r['signal_overall']}] {r['signal_priority']:4} | {r['company']:18} | {r['title'][:80]}")

if __name__ == "__main__":
    main()
