#!/usr/bin/env python3
"""Build the four enum CSV files from data already gathered."""
import csv
import os
import re
import subprocess
from datetime import datetime

OUT_DIR = "/Users/tushar.madan/work_agent/ai-blog-corpus/_data"
os.makedirs(OUT_DIR, exist_ok=True)

HEADER = ["id", "company", "track", "title", "url", "publish_date", "authors", "in_scope", "scope_reason"]


def _ym_to_iso(datestr):
    """Convert 'April 14, 2026' -> '2026-04-14'."""
    if not datestr:
        return ""
    try:
        return datetime.strptime(datestr, "%B %d, %Y").date().isoformat()
    except ValueError:
        return ""


# ---------- Databricks ----------
DBX_LIVE = [
    # (slug, title, date, authors, track_override)
    ("agentic-reasoning-practice-making-sense-structured-and-unstructured-data", "Agentic Reasoning in Practice: Making Sense of Structured and Unstructured Data", "April 14, 2026", ["The Databricks AI Research Team"], None),
    ("memory-scaling-ai-agents", "Memory Scaling for AI Agents", "April 10, 2026", ["The Databricks AI Research Team"], None),
    ("meet-karl-faster-agent-enterprise-knowledge-powered-custom-rl", "Meet KARL: A Faster Agent for Enterprise Knowledge, powered by custom RL", "March 5, 2026", ["The Databricks AI Research Team"], None),
    ("memalign-building-better-llm-judges-human-feedback-scalable-memory", "MemAlign: Building Better LLM Judges From Human Feedback With Scalable Memory", "February 3, 2026", ["The Databricks AI Research Team"], None),
    ("scaling-small-llms-nvidia-mps", "Scaling Small LLMs with NVIDIA MPS", "January 26, 2026", ["The Databricks AI Research Team"], None),
    ("instructed-retriever-unlocking-system-level-reasoning-search-agents", "Instructed Retriever: Unlocking System-Level Reasoning in Search Agents", "January 6, 2026", ["The Databricks AI Research Team"], None),
    ("introducing-officeqa-benchmark-end-to-end-grounded-reasoning", "Introducing OfficeQA: A Benchmark for End-to-End Grounded Reasoning", "December 9, 2025", ["The Databricks AI Research Team"], None),
    ("databricks-neurips-2025", "Databricks at NeurIPS 2025", "December 1, 2025", ["Sam Plecque"], None),
    ("pilot-production-custom-judges", "From Pilot to Production with Custom Judges", "November 4, 2025", ["The Databricks AI Research Team"], None),
    ("fast-peft-serving-scale", "Fast PEFT Serving at Scale", "October 21, 2025", ["The Databricks AI Research Team"], "engineering"),
    ("building-state-art-enterprise-agents-90x-cheaper-automated-prompt-optimization", "Building State-of-the-Art Enterprise Agents 90x Cheaper with Automated Prompt Optimization", "September 24, 2025", ["The Databricks AI Research Team"], None),
    ("judging-confidence-meet-pgrm-promptable-reward-model", "Judging with Confidence: Meet PGRM, the Promptable Reward Model", "August 12, 2025", ["The Databricks AI Research Team"], None),
    ("agent-learning-human-feedback-alhf-databricks-knowledge-assistant-case-study", "Agent Learning from Human Feedback (ALHF): A Databricks Knowledge Assistant Case Study", "August 4, 2025", ["The Databricks AI Research Team"], None),
    ("power-rlvr-training-leading-sql-reasoning-model-databricks", "The Power of RLVR: Training a Leading SQL Reasoning Model on Databricks", "July 30, 2025", ["The Databricks AI Research Team"], None),
    ("power-fine-tuning-your-data-quick-fixing-bugs-llms-never-ending-learning-nel", "The Power of Fine-Tuning on Your Data: Quick Fixing Bugs with LLMs via Never Ending Learning (NEL)", "April 8, 2025", ["Samantha Banchik","Ta-Chung Chi","Sam Havens","Dipendra Misra","Will Tipton","Jan van der Vegt","Matei Zaharia","Emanuel Zgraggen"], None),
    ("tao-using-test-time-compute-train-efficient-llms-without-labeled-data", "TAO: Using test-time compute to train efficient LLMs without labeled data", "March 25, 2025", ["The Databricks AI Research Team"], None),
    ("benchmarking-domain-intelligence", "Benchmarking Domain Intelligence", "December 17, 2024", ["Pallavi Koppol","Erica Ji Yuen","Kartik Sreenivasan","Andy Zhang","Sam Havens","Michael Carbin","Matei Zaharia","Jonathan Frankle"], None),
    ("databricks-neurips-2024", "Databricks at NeurIPS 2024", "December 9, 2024", ["Sam Plecque","Kobie Crawford","Emily Hutson"], None),
    ("characterizing-datasets-and-building-better-models-continued-pre-training", "Characterizing Datasets and Building Better Models with Continued Pre-Training", "November 21, 2024", ["Mansheej Paul","Brett Larsen","Connor Jennings","Cody Blakeney"], None),
    ("long-context-rag-capabilities-openai-o1-and-google-gemini", "The Long Context RAG Capabilities of OpenAI o1 and Google Gemini", "October 8, 2024", ["Quinn Leng","Jacob Portes","Sam Havens","Matei Zaharia","Michael Carbin"], None),
    ("mixattention", "Inference-Friendly Models with MixAttention", "September 18, 2024", ["Shashank Rajput","Ying Sheng (Stanford University)","Sean Owen","Vitaliy Chiley"], None),
    ("unpacking-function-calling-eval", "Beyond the Leaderboard: Unpacking Function Calling Evaluation", "August 16, 2024", ["Kartik Sreenivasan","Jeffrey Chen","Pallavi Koppol","Eitan Turok","Bay Foley-Cox","Asfandyar Qureshi","Sam Havens"], None),
    ("long-context-rag-performance-llms", "Long Context RAG Performance of LLMs", "August 12, 2024", ["Quinn Leng","Jacob Portes","Sam Havens","Matei Zaharia","Michael Carbin"], None),
    ("how-long-should-you-train-your-language-model", "How Long Should You Train Your Language Model?", "July 19, 2024", ["Nikhil Sardana","Jacob Portes","Sasha Doubov"], None),
    ("training-moes-scale-pytorch-and-databricks", "Training MoEs at Scale with PyTorch and Databricks", "July 1, 2024", ["Brian Chu","Mihir Patel","Vitaliy Chiley","Evan Racah"], "engineering"),
    ("optimizing-databricks-llm-pipelines-dspy", "Optimizing Databricks LLM Pipelines with DSPy", "May 23, 2024", ["Arnav Singhvi","Daniel Pechi (JetBlue)"], None),
    ("mosaic-ai-training-capabilities", "Building DBRX-class Custom LLMs with Mosaic AI Training", "May 14, 2024", ["Anna Pfohl","Cheng Li","Mihir Patel","Wai Wu","Will Gleich","Ajay Saini","Hagay Lupesko"], "engineering"),
    ("calibrating-mosaic-evaluation-gauntlet", "Calibrating the Mosaic Evaluation Gauntlet", "April 30, 2024", ["Tessa Barton"], None),
    ("bringing-megablocks-databricks", "Bringing MegaBlocks to Databricks", "April 9, 2024", ["Mihir Patel","Trevor Gale","Vitaliy Chiley"], "engineering"),
    ("dspy-databricks", "DSPy on Databricks", "April 8, 2024", ["Arnav Singhvi","Michael Carbin","Matei Zaharia"], None),
    ("introducing-dbrx-new-state-art-open-llm", "Introducing DBRX: A New State-of-the-Art Open LLM", "March 27, 2024", ["The Databricks AI Research Team"], None),
    ("turbocharged-training-optimizing-databricks-mosaic-ai-stack-fp8", "Turbocharged Training: Optimizing the Databricks Mosaic AI Stack With FP8", "March 21, 2024", ["Mihir Patel","Cheng Li","Davis Blalock","Saaketh Narayan"], "engineering"),
    ("fast-secure-and-reliable-enterprise-grade-llm-inference", "Fast, Secure and Reliable: Enterprise-grade LLM Inference", "March 20, 2024", ["Linden Li","Jeffrey Chen","Megha Agarwal","Margaret Qian","Daya Khudia"], "engineering"),
    ("fine-grained-human-feedback", "Fine-Grained Human Feedback", "February 27, 2024", ["Prithviraj (Raj) Ammanabrolu"], None),
    ("limit-less-more-instruction-tuning", "LIMIT: Less Is More for Instruction Tuning", "February 10, 2024", ["Aditi Jha","Jacob Portes"], None),
    ("ai2-olmo-is-here", "OLMo Is Here, Powered by Databricks", "February 1, 2024", ["Jonathan Frankle"], None),
    ("serving-quantized-llms-nvidia-h100-tensor-core-gpus", "Serving Quantized LLMs on NVIDIA H100 Tensor Core GPUs", "January 31, 2024", ["Nikhil Sardana","Julian Quevedo","Daya Khudia"], "engineering"),
    ("llm-training-and-inference-intel-gaudi2-ai-accelerators", "LLM Training and Inference with Intel Gaudi 2 AI Accelerators", "January 4, 2024", ["Abhi Venigalla","Daya Khudia"], "engineering"),
    ("Integrating-NVIDIA-TensorRT-LLM", "Integrating NVIDIA TensorRT-LLM with the Databricks Inference Stack", "December 21, 2023", ["Linden Li","Megha Agarwal","Kobie Crawford","Daya Khudia"], "engineering"),
    ("patronus-ai-using-llms-to-detect-business-sensitive-information", "Patronus AI: Using LLMs to Detect Business-Sensitive Information", "November 1, 2023", ["Emily Hutson"], None),
    ("training-llms-scale-amd-mi250-gpus", "Training LLMs at Scale with AMD MI250 GPUs", "October 30, 2023", ["Abhi Venigalla"], "engineering"),
    ("llm-training-unity-catalog-data-mosaicml-streaming-dataset", "LLM Training on Unity Catalog data with MosaicML Streaming Dataset", "October 17, 2023", ["Xiaohan Zhang","Maddie Dawson","Karan Jariwala"], "engineering"),
    ("llm-inference-performance-engineering-best-practices", "LLM Inference Performance Engineering: Best Practices", "October 12, 2023", ["Megha Agarwal","Asfandyar Qureshi","Nikhil Sardana","Linden Li","Julian Quevedo","Daya Khudia"], "engineering"),
    ("llama2-inference", "Introducing Llama2-70B-Chat with MosaicML Inference", "August 24, 2023", ["Hagay Lupesko","Margaret Qian","Daya Khudia","Sam Havens","Daniel King","Erica Ji Yuen"], None),
    ("secure-code-evaluation", "End-to-End Secure Evaluation of Code Generation Models", "August 10, 2023", ["Rishab Parthasarathy"], None),
    ("long-context-mpt-7b-8k", "Announcing MPT-7B-8K: 8K Context Length for Document Understanding", "July 18, 2023", ["Sam Havens","Erica Ji Yuen"], None),
    ("amd-mi250", "Training LLMs with AMD MI250 GPUs and MosaicML", "June 30, 2023", ["Abhi Venigalla"], "engineering"),
    ("mpt-30b", "MPT-30B: Raising the bar for open-source foundation models", "June 22, 2023", ["The Databricks AI Research Team"], None),
    ("introducing-ai2-olmo", "Introducing AI2 OLMo (Open Language Model)", "June 2, 2023", ["Jonathan Frankle"], None),
    ("cloudflare-r2-mosaicml", "Cloudflare R2 and MosaicML: Train LLMs on Any Compute with Zero Switching Costs", "May 23, 2023", ["Abhinav Venigalla"], "engineering"),
    ("mpt-7b", "Introducing MPT-7B: A New Standard for Open-Source, Commercially Usable LLMs", "May 5, 2023", ["The Databricks AI Research Team"], None),
    ("diffusion", "How We Trained Stable Diffusion for Less than $50k (Part 3)", "April 28, 2023", ["Mihir Patel","Erica Ji Yuen","Cory Stephenson","Landan Seguin"], None),
    ("coreweave-nvidia-h100-part-1", "Benchmarking Large Language Models on NVIDIA H100 GPUs with CoreWeave (Part 1)", "April 27, 2023", ["Daya Khudia","Vitaliy Chiley"], "engineering"),
    ("stable-diffusion-2", "Training Stable Diffusion from Scratch for <$50k with MosaicML (Part 2)", "April 26, 2023", ["Mihir Patel","Cory Stephenson","Landan Seguin","Austin Jacobson","Erica Ji Yuen"], None),
    ("mosaicbert", "MosaicBERT: Pretraining BERT from Scratch for $20", "March 9, 2023", ["Jacob Portes","Alex Trott","Daniel King","Sam Havens","Erica Ji Yuen"], None),
    ("mosaicml-streamingdataset", "MosaicML StreamingDataset: Fast, Accurate Streaming of Training Data from Cloud Storage", "February 9, 2023", ["James Knighton","Karan Jariwala","Davis Blalock","Erica Ji Yuen"], "engineering"),
    ("llm-evaluation-for-icl", "Blazingly Fast LLM Evaluation for In-Context Learning", "February 2, 2023", ["Jeremy Dohmann"], None),
    ("mosaic-image-segmentation", "5x Faster Image Segmentation Training with MosaicML Recipes", "November 17, 2022", ["Landan Seguin","Cory Stephenson","Erica Ji Yuen"], None),
    ("mlperf-nlp-nov2022", "MosaicML Delivers Leading NLP Performance in MLPerf v2.1", "November 9, 2022", ["Daya Khudia","Nikhil Sardana","Sam Havens","Alex Trott","Erica Ji Yuen"], None),
    ("gpt-3-quality-for-500k", "Mosaic LLMs: GPT-3 quality for <$500k", "September 29, 2022", ["Abhi Venigalla","Linden Li"], None),
    ("billion-parameter-gpt-training-made-easy", "Mosaic LLMs (Part 1): Billion-Parameter GPT Training Made Easy", "August 11, 2022", ["Abhi Venigalla","Linden Li"], "engineering"),
    ("behind-the-scenes", "Behind the Scenes: Setting a Baseline for Image Segmentation Speedups", "July 28, 2022", ["Landan Seguin"], None),
    ("mosaic-resnet-deep-dive", "Mosaic ResNet Deep Dive", "July 18, 2022", ["Matthew Leavitt"], None),
    ("mlperf-2022", "MosaicML Satisfies the Need for Speed with MLPerf Results", "June 29, 2022", ["Bandish Shah","Daya Khudia","Hanlin Tang"], None),
    ("farewell-oom", "Farewell, CUDA OOM: Automatic Gradient Accumulation", "June 23, 2022", ["Mihir Patel","Erica Ji Yuen"], "engineering"),
    ("mosaic-resnet", "Blazingly Fast Computer Vision Training with the Mosaic ResNet and Composer", "June 9, 2022", ["Matthew Leavitt","Erica Ji Yuen","Kobie Crawford"], None),
    ("efficiently-estimating-pareto-frontiers", "Efficiently Estimating Pareto Frontiers with Cyclic Learning Rate Schedules", "April 8, 2022", ["Jacob Portes"], None),
]

# Lost MosaicML posts (404 on databricks.com), recovered via Wayback.
# Filter obvious customer/company-news/launches.
DBX_LOST = [
    # (slug, likely_title, track, in_scope, scope_reason)
    ("5-best-practices-for-efficient-model-training", "5 Best Practices for Efficient Model Training", "research", True, ""),
    ("ai-models-critical-ip-1", "AI Models are Critical IP (Part 1)", "research", False, "company-news"),
    ("ai-models-critical-ip-2", "AI Models are Critical IP (Part 2)", "research", False, "company-news"),
    ("aws-composer", "Composer on AWS", "engineering", True, ""),
    ("best-practices-dec-2021", "Best Practices (Dec 2021)", "research", True, ""),
    ("build-ai-models-on-any-cloud-in-your-secure-environment", "Build AI Models on Any Cloud in Your Secure Environment", "engineering", False, "product-launch"),
    ("comet", "Comet Integration", "engineering", False, "product-launch"),
    ("composer-0-10-release", "Composer 0.10 Release", "engineering", True, ""),
    ("composer-0-11-release", "Composer 0.11 Release", "engineering", True, ""),
    ("composer-0-9-release", "Composer 0.9 Release", "engineering", True, ""),
    ("composer-ffcv-faster-together", "Composer + FFCV: Faster Together", "engineering", True, ""),
    ("dream3d", "Dream3D", "research", True, ""),
    ("founders-blog", "Founders Blog", "research", False, "company-news"),
    ("genai-mosaicml-and-oracle", "GenAI: MosaicML and Oracle", "engineering", False, "company-news"),
    ("inference-launch", "Inference Launch", "engineering", False, "product-launch"),
    ("introducing-mosaicml-cloud", "Introducing MosaicML Cloud", "engineering", False, "product-launch"),
    ("introducing-pubmed-gpt", "Introducing PubMed GPT", "research", True, ""),
    ("making-ml-training-efficient-algorithmically", "Making ML Training Efficient Algorithmically", "research", True, ""),
    ("metadialog-customer-spotlight", "MetaDialog Customer Spotlight", "research", False, "customer-story"),
    ("methodology", "Methodology", "research", True, ""),
    ("mosaicml-cloud-demo", "MosaicML Cloud Demo", "engineering", False, "product-launch"),
    ("mosaicml-databricks-generative-ai-for-all", "MosaicML + Databricks: Generative AI for All", "research", False, "company-news"),
    ("natural-synthetics", "Natural Synthetics", "research", True, ""),
    ("othersideai-customer-spotlight", "OthersideAI Customer Spotlight", "research", False, "customer-story"),
    ("personal-ai-customer-spotlight", "Personal AI Customer Spotlight", "research", False, "customer-story"),
    ("replit", "Replit Customer Spotlight", "research", False, "customer-story"),
    ("stable-diffusion-1", "How We Trained Stable Diffusion for Less than $50k (Part 1)", "research", True, ""),
    ("stable-diffusion-part-3", "Training Stable Diffusion from Scratch (Part 3)", "research", True, ""),
    ("stardog-customer-spotlight", "Stardog Customer Spotlight", "research", False, "customer-story"),
    ("supercharge-training-composer", "Supercharge Training with Composer", "engineering", True, ""),
    ("train-custom-gpt-diffusion-models", "Train Custom GPT + Diffusion Models", "research", True, ""),
    ("training-stable-diffusion-from-scratch-costs-160k", "Training Stable Diffusion from Scratch Costs $160k", "research", True, ""),
    ("training-stable-diffusion-from-scratch-part-2", "Training Stable Diffusion from Scratch (Part 2)", "research", True, ""),
    ("twelve-labs", "Twelve Labs Customer Spotlight", "research", False, "customer-story"),
]


def build_databricks():
    rows = []
    for slug, title, date, authors, track_override in DBX_LIVE:
        track = track_override or "research"
        iso = _ym_to_iso(date)
        # Scope filter: skip "customer" posts, obvious company-news
        in_scope = True
        reason = ""
        low = title.lower()
        if "neurips" in low and "2024" in low or "neurips" in low and "2025" in low:
            # conference recap - light content but still research-related
            in_scope = True
        if "patronus" in slug:
            in_scope = False
            reason = "customer-story"
        prefix = "dbx-e" if track == "engineering" else "dbx-r"
        rows.append([
            f"{prefix}-{slug.lower()}", "databricks", track, title,
            f"https://www.databricks.com/blog/{slug}", iso,
            "|".join(authors), "TRUE" if in_scope else "FALSE", reason
        ])
    # MosaicML lost posts
    for slug, title, track, in_scope, reason in DBX_LOST:
        prefix = "dbx-e" if track == "engineering" else "dbx-r"
        rows.append([
            f"{prefix}-{slug.lower()}", "databricks", track, title,
            f"https://web.archive.org/web/2023/https://www.mosaicml.com/blog/{slug}", "",
            "", "TRUE" if in_scope else "FALSE",
            "migrated-lost" if in_scope else reason
        ])
    out = os.path.join(OUT_DIR, "enum-databricks.csv")
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        w.writerows(rows)
    return out, len(rows), rows


# ---------- Cognition ----------
def build_cognition():
    import xml.etree.ElementTree as ET
    rss_path = os.path.join(OUT_DIR, "cognition_rss.xml")
    # Fallback: /tmp/cognition-rss.xml
    if not os.path.exists(rss_path):
        rss_path = "/tmp/cognition-rss.xml"
    tree = ET.parse(rss_path)
    root = tree.getroot()
    rows = []

    # Classify as research/engineering vs launches/customer-stories.
    # Defaults come from guidance: research-flavored posts = TRUE; pure launches/customer = FALSE.
    CATEGORY_OVERRIDES = {
        # slug : (track, in_scope, reason)
        "introducing-devin": ("research", True, ""),  # launch but foundational method disclosure
        "swe-bench-technical-report": ("research", True, ""),
        "devin-generally-available": ("engineering", False, "product-launch"),
        "june-24-product-update": ("engineering", False, "product-launch"),
        "sept-24-product-update": ("engineering", False, "product-launch"),
        "devin-crowdstrike-outage": ("research", False, "customer-story"),
        "evaluating-coding-agents": ("research", True, ""),
        "dec-24-product-update": ("engineering", False, "product-launch"),
        "dec-24-product-update-2": ("engineering", False, "product-launch"),
        "cognition-open-source-initiative": ("engineering", False, "company-news"),
        "devin-101-automatic-pr-reviews-with-the-devin-api": ("engineering", True, ""),  # tutorial with real detail
        "linktree": ("research", False, "customer-story"),
        "jan-25-product-update": ("engineering", False, "product-launch"),
        "devin-february-25-product-update": ("engineering", False, "product-launch"),
        "crossmint-devin": ("research", False, "customer-story"),
        "devin-2": ("engineering", False, "product-launch"),
        "deepwiki": ("engineering", False, "product-launch"),
        "kevin-32b": ("research", True, ""),
        "devin-2-1": ("engineering", False, "product-launch"),
        "open-source-initiative-is-back": ("engineering", False, "company-news"),
        "deepwiki-mcp-server": ("engineering", False, "product-launch"),
        "dont-build-multi-agents": ("research", True, ""),
        "blockdiff": ("engineering", True, ""),
        "coding-agents-101-the-art-of-actually-getting-things-done": ("research", True, ""),
        "windsurf": ("engineering", False, "company-news"),
        "mcp-marketplace": ("engineering", False, "product-launch"),
        "from-jenkins-to-github-actions": ("engineering", False, "marketing"),
        "ai-data-analyst": ("engineering", True, ""),  # includes methodology
        "how-eight-sleep-uses-devin-as-a-data-analyst": ("research", False, "customer-story"),
        "funding-growth-and-the-next-frontier-of-ai-coding-agents": ("research", False, "company-news"),
        "devin-sonnet-4-5-lessons-and-challenges": ("engineering", True, ""),
        "devin-agent-preview-sonnet-4-5": ("engineering", False, "product-launch"),
        "swe-grep": ("research", True, ""),
        "dotnet-migration-with-devin": ("research", False, "customer-story"),
        "swe-1-5": ("research", True, ""),
        "codemaps": ("engineering", False, "product-launch"),
        "devin-annual-performance-review-2025": ("research", False, "company-news"),
        "infosys-cognition": ("research", False, "company-news"),
        "devin-review": ("engineering", False, "product-launch"),
        "cognition-london": ("engineering", False, "company-news"),
        "cognizant-cognition": ("engineering", False, "company-news"),
        "agent-trace": ("research", True, ""),
        "closing-the-agent-loop-devin-autofixes-review-comments": ("engineering", True, ""),
        "introducing-devin-2-2": ("engineering", False, "product-launch"),
        "cognition-for-government": ("engineering", False, "company-news"),
        "how-cognition-uses-devin-to-build-devin": ("engineering", True, ""),
        "swe-1-6-preview": ("research", True, ""),
        "devin-can-now-manage-devins": ("engineering", False, "product-launch"),
        "devin-can-now-schedule-devins": ("engineering", False, "product-launch"),
        "swe-1-6": ("research", True, ""),
        "how-devin-is-modernizing-cobol-at-fortune-500-companies": ("research", False, "customer-story"),
        "launching-in-japan": ("engineering", False, "company-news"),
        "new-self-serve-plans-for-devin": ("engineering", False, "product-launch"),
        "swe-check-10x-faster": ("research", True, ""),
        "devin-in-windsurf": ("engineering", False, "product-launch"),
    }

    for item in root.iter("item"):
        title = item.findtext("title", "").strip()
        link = item.findtext("link", "").strip()
        pub = item.findtext("pubDate", "").strip()
        slug = link.rstrip("/").split("/")[-1]
        iso = ""
        if pub:
            try:
                iso = datetime.strptime(pub, "%a, %d %b %Y %H:%M:%S %Z").date().isoformat()
            except ValueError:
                try:
                    iso = datetime.strptime(pub[:16], "%a, %d %b %Y").date().isoformat()
                except ValueError:
                    iso = ""
        override = CATEGORY_OVERRIDES.get(slug)
        if override:
            track, in_scope, reason = override
        else:
            # default: engineering, FALSE unless categorized
            track, in_scope, reason = "engineering", False, "unclassified"
        prefix = "cog-e" if track == "engineering" else "cog-r"
        rows.append([
            f"{prefix}-{slug}", "cognition", track, title, link, iso,
            "", "TRUE" if in_scope else "FALSE", reason
        ])
    out = os.path.join(OUT_DIR, "enum-cognition.csv")
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        w.writerows(rows)
    return out, len(rows), rows


# ---------- Cursor ----------
def build_cursor():
    # Research slugs (track=research, in_scope=TRUE)
    research_slugs = [
        "agent-sandboxing", "better-models-ambitious-work", "composer-1-5", "composer-2",
        "composer-2-technical-report", "cursorbench", "fast-regex-search", "multi-agent-kernels",
        "real-time-rl-for-composer", "self-driving-codebases", "self-summarization", "warp-decode",
    ]
    # Product slugs — judgement call per guidance
    product_classifications = {
        # slug : (in_scope, reason)
        "agent-computer-use": (True, ""),   # has methodology
        "automations": (False, "product-launch"),
        "bugbot-autofix": (True, ""),
        "bugbot-learning": (True, ""),   # methodology-heavy
        "canvas": (False, "product-launch"),
        "cursor-3": (False, "product-launch"),
        "jetbrains-acp": (False, "product-launch"),
        "long-running-agents": (True, ""),
        "marketplace": (False, "product-launch"),
        "new-plugins": (False, "product-launch"),
        "security-agents": (True, ""),
        "self-hosted-cloud-agents": (False, "product-launch"),
    }
    # Main blog extras (from /blog root)
    main_blog = [
        # slug, title (from page), date (unknown without visit)
        ("amplitude", "Amplitude", None),
        ("box", "Box", None),
        ("cursor-3", "Cursor 3", None),
        ("bugbot-learning", "Bugbot Learning", None),
    ]

    # Try to read the pre-fetched Cursor blog pages for dates & titles
    # SSR HTML nests <h2> or <h3> title within the anchor. Extract that if present.
    MONTH_RE = re.compile(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4}", re.IGNORECASE)

    def parse_blog_page(path):
        posts = {}
        if not os.path.exists(path):
            return posts
        with open(path) as f:
            html = f.read()
        for m in re.finditer(r'<a[^>]+href="(/blog/[a-z0-9\-]+)"[^>]*>(.*?)</a>', html, re.DOTALL):
            slug = m.group(1).split("/")[-1]
            raw = m.group(2)
            # Prefer an <h2>/<h3> inside the anchor
            title_m = re.search(r'<h[1-6][^>]*>([\s\S]*?)</h[1-6]>', raw)
            if title_m:
                title = re.sub(r'<[^>]+>', ' ', title_m.group(1))
                title = re.sub(r'\s+', ' ', title).strip()
            else:
                # Best-effort: strip tags, remove leading date + "Research/research" label, remove trailing author " 5m"
                flat = re.sub(r'<[^>]+>', ' ', raw)
                flat = re.sub(r'\s+', ' ', flat).strip()
                flat = MONTH_RE.sub('', flat, count=1).strip()
                flat = re.sub(r'^[·\s]*(?:Research|research|Product|product|Company|company)\s+', '', flat)
                flat = re.sub(r'\s+\d+m(\s+.*)?$', '', flat)
                title = flat.strip()
            if title:
                title = title.replace('&amp;', '&').replace('&#x27;', "'").replace('&quot;', '"').strip()
            date_m = MONTH_RE.search(raw)
            iso = ""
            if date_m:
                for fmt in ("%b %d, %Y", "%B %d, %Y"):
                    try:
                        iso = datetime.strptime(date_m.group(0), fmt).date().isoformat()
                        break
                    except ValueError:
                        continue
            # Try to separate the trailing author name from the title.
            author = ""
            if title:
                # Look for "<Title> <FirstName Last>" or "<Title> <A, B & C>" appended
                # where authors block starts with a capital letter, contains "&" "," or is "FirstName LastName"
                m3 = re.search(r'^(.+?)\s+((?:[A-Z][A-Za-z\-]+\s+[A-Z][A-Za-z\-]+(?:\s+[A-Z][A-Za-z\-]+)?)|(?:[A-Z][A-Za-z\-]+(?:,\s*[A-Z][A-Za-z\-]+)*\s*&\s*[A-Z][A-Za-z\-]+))\s*$', title)
                if m3 and len(m3.group(1)) > 10:
                    title = m3.group(1).strip()
                    author = m3.group(2).strip()
            if slug not in posts or (posts[slug][0] and len(title or "") < len(posts[slug][0]) and title):
                posts[slug] = (title or posts.get(slug, (slug.replace('-', ' ').title(), ''))[0], iso or (posts.get(slug, ('', ''))[1]), author)
            elif slug in posts and not posts[slug][2] and author:
                posts[slug] = (posts[slug][0], posts[slug][1], author)
        return posts

    titles = {}
    for p in ["/tmp/cursor-blog.html", "/tmp/cursor-research.html", "/tmp/cursor-product.html"]:
        for k, v in parse_blog_page(p).items():
            if k not in titles or (not titles[k][1] and v[1]):
                titles[k] = v

    def meta(slug):
        if slug in titles:
            return titles[slug]
        return (slug.replace("-", " ").title(), "", "")

    rows = []
    seen = set()
    # Research first
    for slug in research_slugs:
        seen.add(slug)
        t, d, a = meta(slug)
        rows.append([
            f"cur-r-{slug}", "cursor", "research", t,
            f"https://cursor.com/blog/{slug}", d, a, "TRUE", ""
        ])
    # Product (engineering)
    for slug, (in_scope, reason) in product_classifications.items():
        if slug in seen:
            continue
        seen.add(slug)
        t, d, a = meta(slug)
        rows.append([
            f"cur-e-{slug}", "cursor", "engineering", t,
            f"https://cursor.com/blog/{slug}", d, a, "TRUE" if in_scope else "FALSE", reason
        ])
    # Extras from main blog
    for slug, title, _ in main_blog:
        if slug in seen:
            continue
        seen.add(slug)
        t, d, a = meta(slug)
        rows.append([
            f"cur-e-{slug}", "cursor", "engineering", t,
            f"https://cursor.com/blog/{slug}", d, a, "FALSE", "unclassified-cursor-blog"
        ])
    out = os.path.join(OUT_DIR, "enum-cursor.csv")
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        w.writerows(rows)
    return out, len(rows), rows


# ---------- Vercel ----------
def build_vercel():
    import xml.etree.ElementTree as ET
    atom_path = os.path.join(OUT_DIR, "vercel_atom.xml")
    if not os.path.exists(atom_path):
        atom_path = "/tmp/vercel-atom.xml"
    tree = ET.parse(atom_path)
    root = tree.getroot()
    ns = {"a": "http://www.w3.org/2005/Atom"}

    AI_PATTERNS = [
        r"\bai\b", r"llm", r"agent", r"model", r"embedding", r"rag", r"v0",
        r"ai-sdk", r"chatbot", r"inference", r"prompt", r"mcp", r"reasoning",
        r"copilot", r"vector", r"fluid", r"gpt", r"claude", r"genera(tive|tion)"
    ]
    ai_re = re.compile("|".join(AI_PATTERNS), re.IGNORECASE)

    rows = []
    in_scope_n = 0
    for entry in root.iter("{http://www.w3.org/2005/Atom}entry"):
        link_el = entry.find("a:link", ns)
        if link_el is None:
            continue
        url = link_el.attrib.get("href", "")
        if "/blog/" not in url or "/changelog/" in url:
            continue
        title = entry.findtext("a:title", "", ns).strip()
        pub = entry.findtext("a:published", "", ns) or entry.findtext("a:updated", "", ns)
        iso = pub[:10] if pub else ""
        # authors
        authors = []
        for a in entry.findall("a:author/a:name", ns):
            if a.text:
                authors.append(a.text.strip())
        # categories
        cats = [c.attrib.get("term", "") for c in entry.findall("a:category", ns)]
        slug = url.rstrip("/").split("/")[-1]
        # Scope filter
        text_for_match = f"{slug} {title}".lower()
        is_ai = bool(ai_re.search(text_for_match))
        is_eng = any(c.lower() in ("engineering", "eng") for c in cats)

        if is_ai:
            track = "applied" if ("v0" in slug or "ai-sdk" in slug) else "engineering"
            in_scope, reason = True, ""
        elif is_eng:
            track = "engineering"
            in_scope, reason = True, ""
        else:
            track = "engineering"
            in_scope, reason = False, "not-ai-engineering"

        prefix = "vcl-a" if track == "applied" else "vcl-e"
        rows.append([
            f"{prefix}-{slug}", "vercel", track, title, url, iso,
            "|".join(authors), "TRUE" if in_scope else "FALSE", reason
        ])
        if in_scope:
            in_scope_n += 1

    out = os.path.join(OUT_DIR, "enum-vercel.csv")
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        w.writerows(rows)
    return out, len(rows), rows


if __name__ == "__main__":
    for name, fn in [("databricks", build_databricks), ("cognition", build_cognition), ("cursor", build_cursor), ("vercel", build_vercel)]:
        path, n, rows = fn()
        in_scope = sum(1 for r in rows if r[7] == "TRUE")
        dates = [r[5] for r in rows if r[5]]
        earliest = min(dates) if dates else ""
        latest = max(dates) if dates else ""
        print(f"{name}: {n} rows, in_scope={in_scope}, earliest={earliest}, latest={latest}  -> {path}")
