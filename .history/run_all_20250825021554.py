import subprocess
import datetime
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')  

today = datetime.date.today().isoformat()
base_dir = os.path.dirname(__file__)

# 1. Fetch articles
subprocess.run(["python", os.path.join(base_dir, "ingestion", "fetch_rss.py")], check=True)

# 2. Summarize with LLM
subprocess.run(["python", os.path.join(base_dir, "processing", "llm_summarize_ollama.py")], check=True)

# 3. Generate PowerPoint
output_pptx = os.path.join(base_dir, "presentation", f"FT_Summary_4Slides_{datetime.date.today()}.pptx")
subprocess.run(["python", os.path.join(base_dir, "presentation", "advanced_ppt_ollama.py")], check=True)


print(output_pptx)

