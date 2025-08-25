import subprocess
import datetime
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')  

base_dir = os.path.dirname(__file__)

# 1. Fetch articles
subprocess.run(
    ["python", os.path.join(base_dir, "ingestion", "fetch_rss.py")],
    check=True,
    stdout=sys.stderr,  # كل الطباعة للـstderr لتجنب stdout
    stderr=sys.stderr
)

# 2. Summarize with LLM
subprocess.run(
    ["python", os.path.join(base_dir, "processing", "llm_summarize_ollama.py")],
    check=True,
    stdout=sys.stderr,
    stderr=sys.stderr
)

# 3. Generate PowerPoint
subprocess.run(
    ["python", os.path.join(base_dir, "presentation", "advanced_ppt_ollama.py")],
    check=True,
    stdout=sys.stderr,
    stderr=sys.stderr
)

# مسار الملف النهائي فقط في stdout
output_pptx = os.path.join(base_dir, "presentation", f"FT_Summary_4Slides_{datetime.date.today()}.pptx")
print(output_pptx)


