import subprocess
import os
from datetime import datetime

base_dir = os.path.dirname(__file__)
today = datetime.today().date().isoformat()

# 1. Fetch articles
subprocess.run(["python", os.path.join(base_dir, "ingestion", "fetch_rss.py")])

# 2. Summarize with LLM
subprocess.run(["python", os.path.join(base_dir, "processing", "llm_summarize_ollama.py")])

# 3. Generate PPT
subprocess.run(["python", os.path.join(base_dir, "presentation", "advanced_ppt_ollama.py")])

print(f"✅ Daily run completed for {today}")
