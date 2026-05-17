# 🔬 AI Researcher

An AI-powered research agent that searches academic papers on ArXiv, reads and analyzes them, and writes new research papers — complete with LaTeX-rendered PDFs. Built with LangGraph, Google Gemini, and Streamlit.

## How it works

1. **Explore** — Discuss a research topic and search ArXiv for recent papers
2. **Read** — Fetch and analyze the full content of papers you select
3. **Ideate** — Identify promising future research directions from the literature
4. **Write** — Draft a new research paper with mathematical equations
5. **Export** — Render the paper as a LaTeX PDF

## Project structure

\```
ai-researcher/
├── ai_researcher.py    # LangGraph agent + graph definition
├── frontend.py         # Streamlit chat UI
├── arxiv_tool.py       # ArXiv search tool
├── read_pdf.py         # PDF reading utility
├── write_pdf.py        # LaTeX PDF generation
├── .env                # API keys (not committed)
└── output/             # Generated papers (not committed)
\```

## Getting started

\```bash
git clone https://github.com/Utkrisha-kandel/ai_researcher.git
cd ai_researcher
pip install -r requirements.txt
\```

Create a `.env` file:
\```
GEMINI_API=your_google_gemini_api_key
\```

Then run:
\```bash
streamlit run frontend.py
\```

## Tech stack

- [LangGraph](https://github.com/langchain-ai/langgraph) — agent orchestration
- [Google Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/) — LLM backbone
- [Streamlit](https://streamlit.io) — chat UI
- [ArXiv API](https://arxiv.org/help/api) — academic paper search
- [ReportLab](https://www.reportlab.com) — PDF generation

