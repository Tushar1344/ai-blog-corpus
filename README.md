# AI Blog Corpus (v2)

A cross-indexed library of research and engineering blog posts from **12 AI organizations**, categorized around **8 focus areas** as the primary axis, with secondary cross-references by company, year, contribution type, and technique.

## v2 scope

**IN-SCOPE** — core model training, post-training & fine-tuning, alignment & safety, interpretability, evaluations, quantization/efficiency, agentic systems, harness & context engineering.

**OUT-OF-SCOPE** (v2 filter) — inference optimization (speculative decoding, KV cache, Flash Attention internals), kernel work (CUDA/Triton), hardware benchmarks (H100/Gaudi comparisons), general serving infra, applied product stories without methodology.

## Stats

- **695 in-scope posts** (v1 had 548 across 7 companies; v2 adds 247 from 5 new labs after tighter filter)
- **12 organizations**: Anthropic, OpenAI, Databricks Mosaic AI, Cursor, Vercel, Cognition, Thinking Machines, Google Research, Google DeepMind, Meta FAIR, Hugging Face, Allen Institute for AI (AI2), DeepSeek
- **8 focus areas** × 5 axes of secondary categorization

## Artifacts

1. **Google Sheet** — [Master Index](https://docs.google.com/spreadsheets/d/1td1T6wCEnw4EeG05I_hH1dK1aNkLR5HJZZ-4jr-Du9A/edit) (source of truth, one row per post; filter by `focus_area`, `company`, `year`, etc.)
2. **Markdown library** (this repo) — canonical 3-5 bullet summaries organized by focus area, cross-linked to company/year/technique indexes
3. **Google Doc synthesis** — opinionated executive narrative (cross-company themes, standout posts, divergences, gaps)

## Directory structure

```
by-focus-area/        # CANONICAL — 8 focus area files, each contains full per-post entries
by-company/           # Cross-reference — 13 company files, one-line entries linking to canonical
by-contribution-type/ # Cross-reference by contribution kind
by-year/              # Cross-reference by publish year
by-technique/         # Cross-reference by technique tag (SAE, MoE, RLHF, etc.)
_data/                # Source CSVs + scripts
index.md              # Master nav
```

Each post has a unique ID (`{company}-{track}-{slug}`) and appears as a full entry in exactly one `by-focus-area/*.md` file. Every other file cross-references via the ID anchor.

## Focus areas

1. **pretraining-and-architecture** (271 posts) — MoE, SSMs, hybrids, scaling laws, new attention variants, data mixes, tokenizers, foundation models
2. **post-training-and-fine-tuning** (34 posts) — RLHF, RLAIF, RLVR, DPO, SFT, LoRA, on-policy distillation, reward modeling
3. **alignment-and-safety** (95 posts) — constitutional methods, RSP/safety policy, red-teaming, jailbreaking, alignment faking, safeguards, system cards
4. **interpretability** (17 posts) — SAE, circuits, steering, probing, dictionary learning, feature viz, monosemanticity
5. **evals-and-benchmarks** (77 posts) — SWE-bench, Tau-Bench, BrowseComp, GPQA, HELM, eval methodology
6. **quantization-and-efficiency** (20 posts) — FP8/INT8 training, post-training quantization, LoRA/PEFT
7. **agentic-systems** (112 posts) — agents, tool use, multi-agent, computer use, coding agents
8. **harness-and-context-engineering** (69 posts) — scaffolding, context engineering, long-running harnesses, MCP, agent skills

## Contributing companies

| Company | Posts | Primary strengths |
|---|---|---|
| OpenAI | 187 | System cards, agent/harness engineering, research breadth |
| Anthropic | 125 | Alignment, interpretability, harness/context engineering, Claude Code |
| Hugging Face | 115 | Applied engineering, reproductions, open models, datasets |
| Databricks Mosaic AI | 76 | DBRX, MPT, training infra transparency, enterprise agents |
| Meta FAIR | 61 | Llama, SAM, V-JEPA, multimodal, embodied AI |
| Google DeepMind | 34 | AlphaFold/Geometry/Proof, Gemini safety, foundation for science |
| Vercel | 32 | Agent infrastructure, v0, AI SDK |
| AI2 | 18 | OLMo, Tulu, Dolma — full-stack open-source |
| Cursor | 14 | Composer, coding agent research, agent sandboxing |
| DeepSeek | 13 | V3/R1/MoE technical reports, every release is methodologically dense |
| Cognition | 11 | SWE-bench, Devin engineering, Agent Trace |
| Google Research | 5 | (Most non-LLM work filtered out in v2) |
| Thinking Machines | 4 | Connectionism research (Defeating Nondeterminism, LoRA Without Regret, On-Policy Distillation, Modular Manifolds) |

## ID convention

`{company-abbrev}-{track-abbrev}-{slug}`

| Company | Abbrev |
|---|---|
| Anthropic | `ant` |
| OpenAI | `oai` |
| Databricks Mosaic | `dbx` |
| Cursor | `cur` |
| Vercel | `vcl` |
| Cognition | `cog` |
| Thinking Machines | `tm` |
| Google Research | `gr` |
| Google DeepMind | `dm` |
| Meta FAIR | `meta` |
| Hugging Face | `hf` |
| AI2 | `ai2` |
| DeepSeek | `dsk` |

Track: `r` (research), `e` (engineering), `a` (applied).

## Iteration workflow

- **Add a source** → drop rows into the Sheet, re-run `_data/generate_markdown_v2.py`.
- **Re-categorize** → edit `focus_area` column in Sheet, re-run the generator.
- **Rewrite a summary** → edit the entry in `by-focus-area/*.md` (canonical); cross-refs still resolve.
- **New axis** → add a column, add `by-{axis}/` dir, extend generator.
- **Refresh** → weekly cron: poll feeds, diff against Sheet, summarize + categorize new posts.

## Scripts (all in `_data/`)

- `parse_feeds.py` — v1 RSS/sitemap parsers
- `enumerate_tier1.py` — v2 Tier 1 crawler (Google Research, Meta, HF, DeepSeek)
- `assign_focus_area.py` — per-post focus-area classifier
- `consolidate_v2.py` — merges all enum files, applies v2 filter + classification
- `heuristic_tag.py` — legacy tag assignments (kept for compatibility)
- `generate_markdown_v2.py` — writes all markdown (by-focus-area canonical)
- `upload_sheet.py` — pushes master.csv to the Google Sheet

## Known limitations (v2)

1. **Classification is heuristic.** 271 posts land in pretraining-and-architecture; ~40% of those could fit better in post-training or other areas once summaries are available.
2. **Per-post 3-5 bullet summaries pending.** Every entry currently shows "Summary pending" — the main remaining work.
3. **Meta / DeepMind / Google Research titles are slug-derived** (Wayback-based enumeration). Can be enriched by fetching post pages via headless browser.
4. **AI2 and DeepMind under-representation.** Tight filter currently keeps 18 and 34 respectively; looser rules could bring these to 80-100 each.

## v1 → v2 changes

- Primary axis flipped from `by-company/` (canonical in v1) to `by-focus-area/` (canonical in v2)
- Added 5 frontier labs: DeepMind, Meta FAIR, Hugging Face, AI2, DeepSeek
- Tightened scope filter to drop inference/kernel/serving-infra posts (~99 v1 posts re-classified as out-of-scope in v2)
- `by-technical-domain/` retired (superseded by `by-focus-area/`)
- Sheet has new columns: `focus_area`, `dropped_in_v2`
