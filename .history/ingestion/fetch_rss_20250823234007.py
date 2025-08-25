import feedparser
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parents[1] / "articles.db"
RSS_URL = "https://www.ft.com/?format=rss"  # قانوني ومجاني

def create_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        summary TEXT,
        link TEXT
    )
    """)
    conn.commit()
    conn.close()

def fetch_and_store():
    feed = feedparser.parse(RSS_URL)
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    for entry in feed.entries[:10]:  # demo محدود
        c.execute("""
        INSERT INTO articles (title, summary, link) VALUES (?, ?, ?)
        """, (entry.title, getattr(entry, 'summary', ''), entry.link))
    conn.commit()
    conn.close()
    print(f"✅ Stored {len(feed.entries[:10])} articles in {DB}")

if __name__ == "__main__":
    create_db()
    fetch_and_store()
