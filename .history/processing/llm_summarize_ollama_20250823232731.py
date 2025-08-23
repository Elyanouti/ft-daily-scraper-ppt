import json
from pathlib import Path
# من المفترض أنك تستخدم Ollama أو أي LLM محلي
# import ollama

INPUT_DB = "articles.db"
OUTPUT_JSON = "processing/cluster_summaries_ollama.json"

def generate_summaries(articles):
    summarized_articles = []
    for article in articles:
        title = article.get("title")
        link = article.get("link")
        content = article.get("content", "")
        # هنا مكان استدعاء LLM
        summary = f"Auto-generated summary for {title}..."
        # يمكن إضافة theme عبر LLM:
        theme = "Miscellaneous"
        summarized_articles.append({
            "title": title,
            "link": link,
            "summary": summary,
            "theme": theme
        })
    return summarized_articles

if __name__ == "__main__":
    # Load articles from DB or ملف JSON مؤقت
    articles_file = Path("processing/articles.json")
    if not articles_file.exists():
        raise FileNotFoundError("❌ Articles file not found.")
    with open(articles_file, "r", encoding="utf-8") as f:
        articles = json.load(f)

    summaries = generate_summaries(articles)
    os.makedirs("processing", exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump({"articles": summaries}, f, indent=2, ensure_ascii=False)
    print(f"✅ Summaries saved to {OUTPUT_JSON}")
