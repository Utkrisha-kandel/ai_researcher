# AI Researcher

A research agent that finds papers on ArXiv, reads them, and writes new ones — exported as a PDF. You chat with it, pick a topic, and it does the rest.

---

## What it does

You tell it what field you want to explore. It searches ArXiv, summarizes what it finds, and lets you pick a paper to go deeper on. Once you've read through the ideas together, you pick a direction and it writes a full research paper — with equations — and exports it as a PDF.

---

## Stack

- **LangGraph** — agent logic
- **Gemini 2.5 Flash** — the LLM
- **Streamlit** — the UI
- **ArXiv API** — paper search
- **ReportLab** — PDF export

---

## Setup

```bash
git clone https://github.com/Utkrisha-kandel/ai_researcher.git
cd ai_researcher
pip install -r requirements.txt
```

Add a `.env` file:
Get a free key at [aistudio.google.com](https://aistudio.google.com).

Then run:

```bash
streamlit run frontend.py
```

---

## Project files
├── ai_researcher.py   # agent + graph
├── frontend.py        # streamlit UI
├── arxiv_tool.py      # arxiv search
├── read_pdf.py        # pdf reader
├── write_pdf.py       # pdf writer
└── output/            # generated papers
