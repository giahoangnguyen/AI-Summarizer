# AI Summarizer
Turn any web page into a clean, structured summary using your local LLM via Ollama. Includes a simple Python CLI and (optional) Streamlit UI.

## Quick Start

1) Requirements
- Python 3.9–3.12
- Ollama (local model runtime): https://ollama.com/download

2) Required Installation
```bash
pip install -U requests beautifulsoup4 ollama ipython streamlit
```

3) Ollama Set up
```bash
ollama pull llama3.2
```
- You can use any compatible chat model (e.g., llama3.1, qwen2.5, etc). Update MODEL = "your-model-name" in the script if you change it.

4) Run service
```bash
streamlit run app.py
```
- Open the local URL Streamlit prints (usually http://localhost:8501).
