import sqlite3
from pathlib import Path
import json
import ollama

DB = Path(__file__).resolve().parents[1] / "articles.db"
OUTPUT = Path(__file__).resolve().parents[1] / "processing/cluster_summaries_ollama.json"

def fetch_articles(limit=10):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT title, summary, link FROM articles LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    return [{"title": r[0], "summary": r[1], "link": r[2]} for r in rows]

def generate_summary_and_theme(article):
    prompt = f"""
You are an AI assistant. Analyze the following article:

Title: {article['title']}
Content: {article['summary']}

1. Generate a 3-5 sentence summary.
2. Identify a main Theme for the article (1-5 words).
Return as JSON with keys: 'summary' and 'theme'.
"""
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    try:
        return json.loads(response["message"]["content"])
    except:
        return {"summary": response["message"]["content"], "theme": "Miscellaneous"}

if __name__ == "__main__":
    articles = fetch_articles(limit=10)
    for article in articles:
        llm_result = generate_summary_and_theme(article)
        article["llm_summary"] = llm_result["summary"]
        article["theme"] = llm_result["theme"]

    output_data = {
        "summary": "This file contains summarized articles with AI-generated themes.",
        "articles": articles
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Processing complete. JSON saved to {OUTPUT}")



