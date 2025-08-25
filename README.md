# FT Daily Scraper & PPT Summarizer

This project implements an automated pipeline to scrape freely accessible articles from **FT.com**, summarize them using an Opensource **LLM**, and generate a **PowerPoint presentation** with thematic insights. The workflow is fully automated using **n8n**, including email delivery of the generated report.

---

## Features

* **Scraping**: Python-based pipeline fetching freely accessible FT articles on a daily schedule.
* **Data Storage**: Articles are stored in a local SQLite database (`articles.db`).
* **Summarization**: Uses **Ollama LLM** to cluster articles by themes and generate concise summaries.
* **Presentation Generation**: Automatically produces PowerPoint reports (`FT_Summary_4Slides_DATE.pptx`) with references.
* **Automation**: Scheduling and email delivery are managed via **n8n workflow automation**.
* **Version Control**: All scripts, workflows, and resources are maintained in this GitHub repository.

---

## Project Structure

```
ft-llm-demo/
│
├─ ingestion/
│   └─ fetch_rss.py           # Scrapes free FT articles
│
├─ processing/
│   ├─ llm_summarize_ollama.py  # Summarizes articles using LLM
│   └─ cluster_summaries_ollama.json # Output summaries
│
├─ presentation/
│   ├─ advanced_ppt_ollama.py     # Generates PPT from summaries
│   └─ FT_Summary_4Slides_*.pptx # Sample reports
│
├─ run_all.py                  # Main script to execute entire workflow
├─ articles.db                 # Local SQLite database
├─ Dockerfile                  # Optional: containerized setup
└─ .github/workflows/daily.yml # n8n workflow or GitHub Actions setup
```

---

## Usage

1. **Setup environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```

2. **Run the workflow manually**

   ```bash
   python run_all.py
   ```

3. **Automation (n8n)**

   * The workflow is configured to run daily and automatically generate + email the PowerPoint report.
   * Video demonstration of the workflow is included in the repository.

---

## Ethical Note

For compliance and ethical reasons, the pipeline **only scrapes freely accessible FT.com articles**. No attempts are made to bypass paywalls or violate terms of service.

---


## Author

**ELYANOUTI ABDELOUADOUD**
AI AUTOMATION ENGINEER/AI AGENT

---
