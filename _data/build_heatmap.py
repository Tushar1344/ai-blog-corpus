#!/usr/bin/env python3
"""Build an interactive HTML heatmap dashboard of the corpus.

Generates:
  visualizations/heatmap.html   — interactive dashboard (Plotly)
  visualizations/heatmap.png    — static preview for README
"""
import csv
import json
from collections import defaultdict, Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = Path(__file__).parent
VIS = ROOT / "visualizations"
VIS.mkdir(exist_ok=True)

FOCUS_AREAS = [
    "pretraining-and-architecture",
    "post-training-and-fine-tuning",
    "alignment-and-safety",
    "interpretability",
    "evals-and-benchmarks",
    "quantization-and-efficiency",
    "agentic-systems",
    "harness-and-context-engineering",
]
FOCUS_AREA_TITLES = {
    "pretraining-and-architecture": "Pretraining & Architecture",
    "post-training-and-fine-tuning": "Post-training & Fine-tuning",
    "alignment-and-safety": "Alignment & Safety",
    "interpretability": "Interpretability",
    "evals-and-benchmarks": "Evals & Benchmarks",
    "quantization-and-efficiency": "Quantization & Efficiency",
    "agentic-systems": "Agentic Systems",
    "harness-and-context-engineering": "Harness & Context Engineering",
}

COMPANY_TITLES = {
    "anthropic": "Anthropic",
    "openai": "OpenAI",
    "databricks": "Databricks Mosaic",
    "cursor": "Cursor",
    "vercel": "Vercel",
    "cognition": "Cognition",
    "thinking-machines": "Thinking Machines",
    "google-research": "Google Research",
    "deepmind": "DeepMind",
    "meta-fair": "Meta FAIR",
    "huggingface": "Hugging Face",
    "ai2": "AI2",
    "deepseek": "DeepSeek",
    "sakana": "Sakana AI",
    "qwen": "Qwen (Alibaba)",
    "mistral": "Mistral AI",
    "ai21": "AI21 Labs",
    "langchain": "LangChain",
    "moonshot": "Moonshot (Kimi)",
}

COUNTRY_ORDER = ["USA", "China", "France", "UK", "Japan", "Israel"]
COUNTRY_COLORS = {
    "USA": "#3b82f6",
    "China": "#ef4444",
    "France": "#8b5cf6",
    "UK": "#10b981",
    "Japan": "#f59e0b",
    "Israel": "#06b6d4",
}

# Company colors (inspired by brand colors where possible)
COMPANY_COLORS = {
    "anthropic": "#CC785C",  # Anthropic terracotta
    "openai": "#10A37F",     # OpenAI green
    "databricks": "#FF3621", # Databricks red
    "cursor": "#000000",     # Cursor black
    "vercel": "#666666",     # Vercel gray
    "cognition": "#A855F7",  # purple
    "thinking-machines": "#06B6D4",  # cyan
    "google-research": "#4285F4",    # Google blue
    "deepmind": "#3E71E3",   # DeepMind blue
    "meta-fair": "#0866FF",  # Meta blue
    "huggingface": "#FFD21E",  # HF yellow
    "ai2": "#0A8754",        # AI2 green
    "deepseek": "#4D6BFE",   # DeepSeek blue
    "sakana": "#EC4899",     # Sakana pink
    "qwen": "#DC2626",       # Qwen red
    "mistral": "#F97316",    # Mistral orange
    "ai21": "#14B8A6",       # AI21 teal
    "langchain": "#1C1917",  # LangChain dark
    "moonshot": "#9333EA",   # Moonshot purple
}

def load_rows():
    rows = [r for r in csv.DictReader(open(DATA / "master.csv"))
            if r.get("in_scope") == "TRUE" and r.get("dropped_in_v2") == "FALSE"]
    return rows

def aggregate(rows):
    """Return dict of (year_month, focus_area, company) -> list of posts."""
    cells = defaultdict(list)
    for r in rows:
        date = r.get("publish_date", "")
        if not date or len(date) < 7:
            continue
        year_month = date[:7]
        fa = r["focus_area"]
        co = r["company"]
        cells[(year_month, fa, co, r.get("country", ""))].append({
            "id": r["id"],
            "title": r["title"],
            "url": r["url"],
            "date": date,
        })
    return cells

def build_month_range(rows):
    dates = [r["publish_date"][:7] for r in rows if r.get("publish_date") and len(r["publish_date"]) >= 7]
    if not dates:
        return []
    start = min(dates)
    end = max(dates)
    y1, m1 = int(start[:4]), int(start[5:7])
    y2, m2 = int(end[:4]), int(end[5:7])
    months = []
    y, m = y1, m1
    while (y, m) <= (y2, m2):
        months.append(f"{y:04d}-{m:02d}")
        m += 1
        if m > 12:
            m = 1
            y += 1
    return months

def build_html(rows, cells, months):
    """Build self-contained HTML with Plotly heatmaps."""
    # Primary heatmap: focus_area × month, cell = count
    fa_month_count = defaultdict(int)
    fa_month_top_co = defaultdict(lambda: Counter())
    fa_month_posts = defaultdict(list)
    for (ym, fa, co, country), posts in cells.items():
        fa_month_count[(fa, ym)] += len(posts)
        fa_month_top_co[(fa, ym)][co] += len(posts)
        fa_month_posts[(fa, ym)].extend(posts)

    z_primary = []
    text_primary = []
    hover_primary = []
    for fa in FOCUS_AREAS:
        z_row = []
        text_row = []
        hover_row = []
        for ym in months:
            c = fa_month_count.get((fa, ym), 0)
            z_row.append(c)
            text_row.append(str(c) if c > 0 else "")
            if c > 0:
                top_cos = fa_month_top_co[(fa, ym)].most_common(3)
                top_str = "<br>".join(f"  {COMPANY_TITLES.get(co, co)}: {n}" for co, n in top_cos)
                samp = fa_month_posts[(fa, ym)][:3]
                post_lines = "<br>".join(f"  • {p['title'][:70]}" for p in samp)
                hover_row.append(f"<b>{FOCUS_AREA_TITLES[fa]}</b><br>{ym}<br><br><b>{c} posts</b><br><br>Top contributors:<br>{top_str}<br><br>Sample:<br>{post_lines}")
            else:
                hover_row.append(f"{FOCUS_AREA_TITLES[fa]} — {ym}<br>no posts")
        z_primary.append(z_row)
        text_primary.append(text_row)
        hover_primary.append(hover_row)

    # Company heatmap: company × month, cell = count
    co_month = defaultdict(int)
    co_month_top_fa = defaultdict(lambda: Counter())
    for (ym, fa, co, country), posts in cells.items():
        co_month[(co, ym)] += len(posts)
        co_month_top_fa[(co, ym)][fa] += len(posts)
    companies = sorted(set(r["company"] for r in rows), key=lambda c: -sum(co_month[(c, m)] for m in months))
    z_co = []
    hover_co = []
    text_co = []
    for co in companies:
        z_row = []
        text_row = []
        h_row = []
        for ym in months:
            c = co_month.get((co, ym), 0)
            z_row.append(c)
            text_row.append(str(c) if c > 0 else "")
            if c > 0:
                top = co_month_top_fa[(co, ym)].most_common(3)
                top_str = "<br>".join(f"  {FOCUS_AREA_TITLES.get(f, f)}: {n}" for f, n in top)
                h_row.append(f"<b>{COMPANY_TITLES.get(co, co)}</b><br>{ym}<br><br><b>{c} posts</b><br><br>Top focus areas:<br>{top_str}")
            else:
                h_row.append(f"{COMPANY_TITLES.get(co, co)} — {ym}<br>no posts")
        z_co.append(z_row)
        hover_co.append(h_row)
        text_co.append(text_row)

    # Country heatmap: country × month
    country_month = defaultdict(int)
    country_month_top = defaultdict(lambda: Counter())
    for (ym, fa, co, country), posts in cells.items():
        if country:
            country_month[(country, ym)] += len(posts)
            country_month_top[(country, ym)][co] += len(posts)
    countries = [c for c in COUNTRY_ORDER if any(country_month[(c, m)] for m in months)]
    z_country = []
    hover_country = []
    text_country = []
    for ctry in countries:
        z_row = []
        h_row = []
        t_row = []
        for ym in months:
            c = country_month.get((ctry, ym), 0)
            z_row.append(c)
            t_row.append(str(c) if c > 0 else "")
            if c > 0:
                top = country_month_top[(ctry, ym)].most_common(3)
                top_str = "<br>".join(f"  {COMPANY_TITLES.get(x, x)}: {n}" for x, n in top)
                h_row.append(f"<b>{ctry}</b><br>{ym}<br><br><b>{c} posts</b><br><br>Top orgs:<br>{top_str}")
            else:
                h_row.append(f"{ctry} — {ym}<br>no posts")
        z_country.append(z_row)
        hover_country.append(h_row)
        text_country.append(t_row)

    # Stacked stream chart: total posts per month, stacked by focus_area
    fa_monthly = defaultdict(lambda: [0] * len(months))
    month_idx = {m: i for i, m in enumerate(months)}
    for (ym, fa, co, country), posts in cells.items():
        if ym in month_idx:
            fa_monthly[fa][month_idx[ym]] += len(posts)

    # Build Plotly traces for stacked area
    stream_traces = []
    for fa in FOCUS_AREAS:
        stream_traces.append({
            "x": months,
            "y": fa_monthly.get(fa, [0] * len(months)),
            "name": FOCUS_AREA_TITLES[fa],
            "mode": "lines",
            "stackgroup": "one",
            "type": "scatter",
            "line": {"width": 0.5},
            "hoverinfo": "x+y+name",
        })

    # Company over time (stacked by company)
    co_monthly = defaultdict(lambda: [0] * len(months))
    for (ym, fa, co, country), posts in cells.items():
        if ym in month_idx:
            co_monthly[co][month_idx[ym]] += len(posts)

    # Country over time (stacked by country)
    country_monthly = defaultdict(lambda: [0] * len(months))
    for (ym, fa, co, country), posts in cells.items():
        if ym in month_idx and country:
            country_monthly[country][month_idx[ym]] += len(posts)
    country_stream_traces = []
    for ctry in countries:
        country_stream_traces.append({
            "x": months,
            "y": country_monthly.get(ctry, [0] * len(months)),
            "name": ctry,
            "mode": "lines",
            "stackgroup": "one",
            "type": "scatter",
            "line": {"width": 0.5, "color": COUNTRY_COLORS.get(ctry, "#888")},
            "fillcolor": COUNTRY_COLORS.get(ctry, "#888") + "CC",
        })

    co_stream_traces = []
    for co in companies:
        co_stream_traces.append({
            "x": months,
            "y": co_monthly.get(co, [0] * len(months)),
            "name": COMPANY_TITLES.get(co, co),
            "mode": "lines",
            "stackgroup": "one",
            "type": "scatter",
            "line": {"width": 0.5, "color": COMPANY_COLORS.get(co, "#888")},
            "fillcolor": COMPANY_COLORS.get(co, "#888") + "CC",
        })

    # Write HTML
    total_posts = len(rows)
    dated_posts = sum(1 for r in rows if r.get("publish_date"))
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>AI Blog Corpus — Temporal Heatmap</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
  body {{ font-family: -apple-system, system-ui, sans-serif; max-width: 1400px; margin: 20px auto; padding: 0 20px; color: #222; }}
  h1 {{ font-size: 28px; margin-bottom: 4px; }}
  .sub {{ color: #666; margin-bottom: 24px; }}
  .chart {{ margin-bottom: 48px; }}
  .stats {{ background: #f5f5f5; padding: 12px 16px; border-radius: 6px; margin-bottom: 24px; font-size: 14px; }}
  .stats b {{ color: #111; }}
  .foot {{ color: #888; font-size: 12px; margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd; }}
  .focus-list {{ color: #666; font-size: 13px; line-height: 1.6; }}
</style>
</head>
<body>
<h1>AI Blog Corpus — Temporal Heatmap</h1>
<p class="sub">Research &amp; engineering posts across 13 AI organizations, organized by 8 focus areas. Hover for details; click legend to toggle series. All-time.</p>

<div class="stats">
  <b>{total_posts}</b> in-scope posts · <b>{dated_posts}</b> with publish date ({100*dated_posts//total_posts}% coverage) · date range <b>{months[0] if months else '?'}</b> → <b>{months[-1] if months else '?'}</b>
</div>

<h2>Focus area × month — what got published when</h2>
<div id="heatmap-fa" class="chart" style="height: 560px;"></div>

<h2>Country × month — where the research came from</h2>
<div id="heatmap-country" class="chart" style="height: 400px;"></div>

<h2>Company × month — who was active when</h2>
<div id="heatmap-co" class="chart" style="height: 680px;"></div>

<h2>Focus areas over time (stacked volume)</h2>
<div id="stream-fa" class="chart" style="height: 400px;"></div>

<h2>Countries over time (stacked volume)</h2>
<div id="stream-country" class="chart" style="height: 400px;"></div>

<h2>Companies over time (stacked volume)</h2>
<div id="stream-co" class="chart" style="height: 480px;"></div>

<p class="foot">Corpus at <a href="https://github.com/Tushar1344/ai-blog-corpus">Tushar1344/ai-blog-corpus</a>. Source of truth: <a href="https://docs.google.com/spreadsheets/d/1td1T6wCEnw4EeG05I_hH1dK1aNkLR5HJZZ-4jr-Du9A/edit">Google Sheet</a>. Coverage gap: ~310 posts (Meta / OpenAI / DeepMind / AI2) are missing dates due to Cloudflare/Facebook gates on Wayback. Those counts aren't represented here.</p>

<script>
const HEATMAP_COLOR = [
  [0.0, '#f7fbff'],
  [0.01, '#deebf7'],
  [0.1, '#9ecae1'],
  [0.3, '#4292c6'],
  [0.7, '#08519c'],
  [1.0, '#08306b']
];

Plotly.newPlot('heatmap-fa', [{{
  z: {json.dumps(z_primary)},
  x: {json.dumps(months)},
  y: {json.dumps([FOCUS_AREA_TITLES[f] for f in FOCUS_AREAS])},
  text: {json.dumps(text_primary)},
  hoverinfo: 'text',
  hovertext: {json.dumps(hover_primary)},
  type: 'heatmap',
  colorscale: HEATMAP_COLOR,
  showscale: true,
  colorbar: {{ title: 'Posts', len: 0.7, x: 1.02 }},
  xgap: 1, ygap: 1
}}], {{
  margin: {{ l: 220, r: 80, t: 20, b: 80 }},
  xaxis: {{ title: '', tickangle: -60, type: 'category', tickfont: {{ size: 10 }}, nticks: 30 }},
  yaxis: {{ title: '', autorange: 'reversed', tickfont: {{ size: 12 }} }},
  plot_bgcolor: 'white'
}}, {{ displaylogo: false, responsive: true }});

Plotly.newPlot('heatmap-country', [{{
  z: {json.dumps(z_country)},
  x: {json.dumps(months)},
  y: {json.dumps(countries)},
  text: {json.dumps(text_country)},
  hoverinfo: 'text',
  hovertext: {json.dumps(hover_country)},
  type: 'heatmap',
  colorscale: HEATMAP_COLOR,
  showscale: true,
  colorbar: {{ title: 'Posts', len: 0.7, x: 1.02 }},
  xgap: 1, ygap: 1
}}], {{
  margin: {{ l: 120, r: 80, t: 20, b: 80 }},
  xaxis: {{ title: '', tickangle: -60, type: 'category', tickfont: {{ size: 10 }}, nticks: 30 }},
  yaxis: {{ title: '', autorange: 'reversed', tickfont: {{ size: 12 }} }},
  plot_bgcolor: 'white'
}}, {{ displaylogo: false, responsive: true }});

Plotly.newPlot('stream-country', {json.dumps(country_stream_traces)}, {{
  margin: {{ l: 60, r: 30, t: 20, b: 80 }},
  xaxis: {{ title: '', tickangle: -60, type: 'category', nticks: 30 }},
  yaxis: {{ title: 'Posts per month' }},
  legend: {{ orientation: 'v', x: 1.02, y: 1 }},
  showlegend: true,
  plot_bgcolor: 'white'
}}, {{ displaylogo: false, responsive: true }});

Plotly.newPlot('heatmap-co', [{{
  z: {json.dumps(z_co)},
  x: {json.dumps(months)},
  y: {json.dumps([COMPANY_TITLES.get(c, c) for c in companies])},
  text: {json.dumps(text_co)},
  hoverinfo: 'text',
  hovertext: {json.dumps(hover_co)},
  type: 'heatmap',
  colorscale: HEATMAP_COLOR,
  showscale: true,
  colorbar: {{ title: 'Posts', len: 0.7, x: 1.02 }},
  xgap: 1, ygap: 1
}}], {{
  margin: {{ l: 180, r: 80, t: 20, b: 80 }},
  xaxis: {{ title: '', tickangle: -60, type: 'category', tickfont: {{ size: 10 }}, nticks: 30 }},
  yaxis: {{ title: '', autorange: 'reversed', tickfont: {{ size: 11 }} }},
  plot_bgcolor: 'white'
}}, {{ displaylogo: false, responsive: true }});

Plotly.newPlot('stream-fa', {json.dumps(stream_traces)}, {{
  margin: {{ l: 60, r: 30, t: 20, b: 80 }},
  xaxis: {{ title: '', tickangle: -60, type: 'category', nticks: 30 }},
  yaxis: {{ title: 'Posts per month' }},
  legend: {{ orientation: 'v', x: 1.02, y: 1 }},
  showlegend: true,
  plot_bgcolor: 'white'
}}, {{ displaylogo: false, responsive: true }});

Plotly.newPlot('stream-co', {json.dumps(co_stream_traces)}, {{
  margin: {{ l: 60, r: 30, t: 20, b: 80 }},
  xaxis: {{ title: '', tickangle: -60, type: 'category', nticks: 30 }},
  yaxis: {{ title: 'Posts per month' }},
  legend: {{ orientation: 'v', x: 1.02, y: 1 }},
  showlegend: true,
  plot_bgcolor: 'white'
}}, {{ displaylogo: false, responsive: true }});
</script>
</body>
</html>"""
    out = VIS / "heatmap.html"
    out.write_text(html)
    print(f"Wrote {out}")
    return out

def build_static_preview(rows, cells, months):
    """Generate static SVG heatmaps for README (no external deps)."""
    fa_month_count = defaultdict(int)
    for (ym, fa, co, country), posts in cells.items():
        fa_month_count[(fa, ym)] += len(posts)

    co_month_count = defaultdict(int)
    for (ym, fa, co, country), posts in cells.items():
        co_month_count[(co, ym)] += len(posts)

    country_month_count = defaultdict(int)
    for (ym, fa, co, country), posts in cells.items():
        if country:
            country_month_count[(country, ym)] += len(posts)

    companies = sorted(set(r["company"] for r in rows),
                       key=lambda c: -sum(co_month_count[(c, m)] for m in months))

    # Color helper
    def heat_color(val, vmax):
        if val == 0:
            return "#f7fbff"
        # Map to a 6-step blue scale
        stops = ["#deebf7", "#c6dbef", "#9ecae1", "#6baed6", "#4292c6", "#2171b5", "#08519c", "#08306b"]
        # Log scale feels better for heavy skew
        import math
        t = math.log1p(val) / math.log1p(max(vmax, 1))
        idx = min(int(t * (len(stops) - 1)), len(stops) - 1)
        return stops[idx]

    # ---------- Focus area heatmap ----------
    def render_heatmap(z_rows, row_labels, title, filename, row_label_width=260):
        vmax = max((max(row) if row else 0) for row in z_rows) or 1
        cell_w = 12
        cell_h = 22
        n_cols = len(months)
        top_pad = 100
        left_pad = row_label_width
        right_pad = 30
        bottom_pad = 90
        width = left_pad + cell_w * n_cols + right_pad
        height = top_pad + cell_h * len(z_rows) + bottom_pad

        svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" font-family="-apple-system, system-ui, Helvetica, sans-serif">']
        svg.append(f'<rect width="{width}" height="{height}" fill="white"/>')
        svg.append(f'<text x="{left_pad}" y="30" font-size="18" font-weight="600" fill="#111">{title}</text>')
        svg.append(f'<text x="{left_pad}" y="52" font-size="11" fill="#666">Posts per month; darker = more. Hover the interactive HTML for post lists.</text>')

        # Month labels (every Nth)
        step = max(1, n_cols // 30)
        for i, m in enumerate(months):
            if i % step == 0:
                x = left_pad + i * cell_w + cell_w / 2
                svg.append(f'<text x="{x}" y="{top_pad - 8}" font-size="8" fill="#555" text-anchor="end" transform="rotate(-60 {x} {top_pad - 8})">{m}</text>')

        # Year markers (faint vertical lines at January of each year)
        for i, m in enumerate(months):
            if m.endswith("-01"):
                x = left_pad + i * cell_w
                svg.append(f'<line x1="{x}" y1="{top_pad}" x2="{x}" y2="{top_pad + cell_h * len(z_rows)}" stroke="#ddd" stroke-width="1"/>')
                yr = m[:4]
                svg.append(f'<text x="{x + 4}" y="{top_pad + cell_h * len(z_rows) + 14}" font-size="10" fill="#999">{yr}</text>')

        # Cells
        for i, row in enumerate(z_rows):
            y = top_pad + i * cell_h
            svg.append(f'<text x="{left_pad - 10}" y="{y + cell_h / 2 + 4}" font-size="11" fill="#222" text-anchor="end">{row_labels[i]}</text>')
            for j, v in enumerate(row):
                x = left_pad + j * cell_w
                c = heat_color(v, vmax)
                svg.append(f'<rect x="{x}" y="{y}" width="{cell_w - 1}" height="{cell_h - 1}" fill="{c}" stroke="#fff" stroke-width="0.5"/>')
                if v > 0 and cell_w >= 12:
                    text_color = "white" if v > vmax * 0.4 else "#333"
                    svg.append(f'<text x="{x + cell_w / 2}" y="{y + cell_h / 2 + 3}" font-size="8" fill="{text_color}" text-anchor="middle">{v}</text>')

        # Legend
        legend_y = height - 50
        svg.append(f'<text x="{left_pad}" y="{legend_y}" font-size="10" fill="#666">Posts/month:</text>')
        stops = ["#f7fbff", "#deebf7", "#c6dbef", "#9ecae1", "#6baed6", "#4292c6", "#2171b5", "#08519c", "#08306b"]
        for i, s in enumerate(stops):
            svg.append(f'<rect x="{left_pad + 80 + i * 18}" y="{legend_y - 10}" width="18" height="14" fill="{s}" stroke="#ccc"/>')
        svg.append(f'<text x="{left_pad + 80}" y="{legend_y + 20}" font-size="9" fill="#666">0</text>')
        svg.append(f'<text x="{left_pad + 80 + len(stops) * 18 - 5}" y="{legend_y + 20}" font-size="9" fill="#666">{vmax}+</text>')

        svg.append("</svg>")
        out = VIS / filename
        out.write_text("\n".join(svg))
        return out

    # Focus area heatmap
    z_fa = [[fa_month_count.get((fa, m), 0) for m in months] for fa in FOCUS_AREAS]
    p1 = render_heatmap(
        z_fa, [FOCUS_AREA_TITLES[f] for f in FOCUS_AREAS],
        "AI Blog Corpus — Focus area × month",
        "heatmap-focus-area.svg", row_label_width=280,
    )
    print(f"Wrote {p1}")

    # Company heatmap
    z_co = [[co_month_count.get((co, m), 0) for m in months] for co in companies]
    p2 = render_heatmap(
        z_co, [COMPANY_TITLES.get(c, c) for c in companies],
        "AI Blog Corpus — Company × month",
        "heatmap-company.svg", row_label_width=200,
    )
    print(f"Wrote {p2}")

    # Country heatmap
    countries_static = [c for c in COUNTRY_ORDER if any(country_month_count[(c, m)] for m in months)]
    z_ctry = [[country_month_count.get((c, m), 0) for m in months] for c in countries_static]
    p3 = render_heatmap(
        z_ctry, countries_static,
        "AI Blog Corpus — Country × month",
        "heatmap-country.svg", row_label_width=120,
    )
    print(f"Wrote {p3}")

    return [p1, p2, p3]

def main():
    rows = load_rows()
    cells = aggregate(rows)
    months = build_month_range(rows)
    print(f"Aggregated {sum(len(v) for v in cells.values())} posts into {len(cells)} cells across {len(months)} months")
    build_html(rows, cells, months)
    build_static_preview(rows, cells, months)

if __name__ == "__main__":
    main()
