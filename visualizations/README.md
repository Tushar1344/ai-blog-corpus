# Visualizations

Temporal heatmaps showing what got published when, across focus areas and companies.

## Interactive dashboard

Open **[heatmap.html](heatmap.html)** in a browser for the full interactive dashboard:

- **Focus area × month** heatmap — hover shows top contributing companies and sample post titles
- **Company × month** heatmap — hover shows top focus areas that company worked on that month
- **Focus areas over time** stacked area chart
- **Companies over time** stacked area chart (brand-colored)

## Static previews

### Focus area × month

![Focus area heatmap](heatmap-focus-area.svg)

### Company × month

![Company heatmap](heatmap-company.svg)

## What the heatmaps show

- **2017–2019** — Early classical ML research (mostly OpenAI + DeepMind + FAIR), dominated by `pretraining-and-architecture/research-techniques-and-methods`: GANs, RL fundamentals, meta-learning.
- **2020–2022** — First wave of LLM safety papers (Anthropic founding era), RLHF becomes a named technique at OpenAI, MosaicML efficiency work begins.
- **2023** — Explosion: DBRX/MPT releases, Llama 2, Zephyr, first Circuits posts, system cards as a genre.
- **2024** — Agents go production. DeepSeek-V2/Coder-V2/R1 ship. OLMo-1. Cosmopedia/FineWeb. First explicit RLVR work.
- **2025** — Test-time compute era. R1. Thinking Machines launches. Claude Code. Agent harness emerges as a discipline.
- **2026 YTD** — Dense and broad. Agent infra, enterprise agents, multi-agent debates, eval-awareness research.

## Coverage gaps

The heatmaps only show the ~385 in-scope posts that have publish dates. ~310 posts are missing dates because their source pages are blocked by Cloudflare (OpenAI) or Facebook login (Meta AI via Wayback). Those are still in the Sheet and markdown library — they just don't appear in the temporal view.

## Regeneration

```bash
python3 _data/build_heatmap.py
```
