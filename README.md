# AI Blog Corpus

A cross-indexed library of research and engineering blog posts from Anthropic, OpenAI, Databricks Mosaic AI, Cursor, Vercel, Cognition, and Thinking Machines. All-time, technical-substance-filtered, re-sliceable across multiple categorization axes.

## Artifacts

1. **Google Sheet** — master index (one row per post). Source of truth. Sort, filter, pivot.
2. **Markdown library** (this directory) — canonical 3-5 bullet summaries per post, plus cross-references by axis.
3. **Google Doc** — opinionated executive synthesis: cross-company themes, standout posts, temporal arc, gaps.

## Directory structure

```
by-company/           # Canonical full entries. Each post appears here exactly once.
by-technical-domain/  # Cross-refs — pretraining, post-training, inference, agents, interpretability, safety, multimodal, evals, training-infra, serving-infra, applied
by-contribution-type/ # Cross-refs — new-method, empirical-study, dataset-benchmark, retrospective-case-study, infra-release, interpretability-finding, position-policy
by-year/              # Cross-refs — 2020 … 2026
by-technique/         # Cross-refs — SAE.md, MoE.md, speculative-decoding.md, RLHF.md, RLVR.md, etc.
_data/                # Raw CSVs from enumeration phase (inputs to the sheet)
index.md              # Master cross-cutting index
```

The `by-company/*.md` files are canonical — summaries live there. Every other file is a one-line cross-reference pointing back to the `by-company` anchor.

## Categorization axes

- **Axis A — Contribution type** (single): new-method, empirical-study, dataset-benchmark, retrospective-case-study, infra-release, interpretability-finding, position-policy
- **Axis B — Technical domain** (single, primary): pretraining, post-training, inference, agents, interpretability, safety-alignment, multimodal, evals-benchmarks, training-infra, serving-infra, applied-product
- **Axis C — Track** (single): research, engineering, applied
- **Axis D — Year** (derived from publish date)
- **Axis E — Techniques** (multi): MoE, SAE, speculative-decoding, chain-of-thought, RLHF, RLVR, constitutional-AI, DPO, long-context, RoPE, Flash-Attention, KV-cache, quantization, distillation, tool-use, computer-use, coding-agents, prompt-caching, context-engineering, test-time-compute, reward-modeling, red-teaming, jailbreak, steering, probing, scaling-laws, retrieval-augmentation, and named evals (SWE-bench, Tau-Bench, MMLU, HumanEval, etc.)

## ID convention

`{company-abbrev}-{track-abbrev}-{slug}` — e.g. `ant-r-circuits-updates-oct-2025`, `oai-e-scaling-postgresql`, `dbx-r-dbrx-technical`, `tm-r-defeating-nondeterminism-inference`.

Company abbreviations: `ant` (Anthropic), `oai` (OpenAI), `dbx` (Databricks Mosaic AI), `cur` (Cursor), `vcl` (Vercel), `cog` (Cognition), `tm` (Thinking Machines).

Track abbreviations: `r` (research), `e` (engineering), `a` (applied).

## Iteration workflow

- **Add a source** → drop rows into the Sheet, re-run Phase 4 script to regenerate cross-refs.
- **Change categorization** → edit column in Sheet, re-run Phase 4.
- **Rewrite a summary** → edit the `by-company/*.md` entry (canonical). Cross-refs link to the anchor, so they auto-update.
- **New axis** → add a column, add `by-{axis}/` dir, populate via Phase 4.
- **Refresh** → cron: poll each feed weekly, diff against Sheet, summarize and categorize new posts only.
