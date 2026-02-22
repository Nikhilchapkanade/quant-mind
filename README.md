<p align="center">
  <h1 align="center">📈 QuantMind AI</h1>
  <p align="center"><strong>Financial agent that predicts stocks with deep learning, running straight inside Claude</strong></p>
  <p align="center"><em>LSTM neural network for price prediction + RAG for analyst sentiment — all via MCP.</em></p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/MCP-Server-7C3AED?style=flat-square"/>
  <img src="https://img.shields.io/badge/TensorFlow-LSTM-FF6F00?style=flat-square&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/ChromaDB-RAG-FF6B6B?style=flat-square"/>
  <img src="https://img.shields.io/badge/Claude-Desktop-000000?style=flat-square&logo=anthropic&logoColor=white"/>
</p>

---

## 🧠 What Is This?

Most AI just reads text. QuantMind actually **does math**. It's a financial analyst that lives on your laptop, exposing two MCP tools to Claude:

| Tool | Brain | What It Does |
|------|-------|-------------|
| `predict_stock_trend` | 🔢 **Quantitative** (LSTM) | Fetches live data from Yahoo Finance, trains a neural network in real-time, predicts next-day price |
| `consult_analyst_notes` | 📝 **Qualitative** (RAG) | Searches analyst reports via vector similarity to explain *why* the stock is moving |

---

## ⚡ Architecture

```
 Claude Desktop App
        │
        │ MCP (stdio)
        ▼
 ┌──────────────────┐
 │   server.py       │  FastMCP Server
 │   (2 tools)       │
 └──┬──────────┬─────┘
    │          │
    ▼          ▼
 brain_dl    brain_rag
 (LSTM)      (RAG)
    │          │
    ▼          ▼
 Yahoo       ChromaDB
 Finance     Vector Store
```

### The Quantitative Brain (`brain_dl.py`)
- Downloads **2 years** of historical price data from Yahoo Finance
- Trains a **TensorFlow LSTM** model in real-time on your machine
- Predicts next-day closing price and trend direction

### The Qualitative Brain (`brain_rag.py`)
- Ingests financial analyst reports into **ChromaDB** with sentence embeddings
- Retrieves relevant context for any ticker using vector similarity search
- Returns sentiment analysis with supporting evidence

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/Nikhilchapkanade/quant-mind.git
cd quant-mind

# 2. Setup environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3. Install
pip install -r requirements.txt
```

### Connect to Claude Desktop

Add to your Claude config (`%APPDATA%\Claude\claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "quant-mind": {
      "command": "python",
      "args": ["path/to/quant-mind/server.py"]
    }
  }
}
```

---

## 💬 Usage

Open Claude Desktop and ask:

> *"Predict the stock trend for Tesla (TSLA) and consult analyst notes."*

**What happens:**
1. Downloads last 2 years of TSLA data from Yahoo Finance
2. Trains an LSTM neural network on your GPU/CPU
3. Searches analyst reports for context
4. Returns: `📊 PREDICTION FOR TSLA: DOWNWARD TREND 📉`

---

## 📁 Project Structure

```
quant-mind/
├── server.py        # MCP server — exposes 2 tools to Claude
├── brain_dl.py      # LSTM price predictor (TensorFlow)
├── brain_rag.py     # RAG analyst sentiment (ChromaDB)
└── requirements.txt
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| AI Protocol | Model Context Protocol (MCP) |
| Deep Learning | TensorFlow / Keras (LSTM) |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| Market Data | Yahoo Finance API |
| Client | Claude Desktop |
