import os
import sys
import logging
import warnings

# --- 1. NUCLEAR SILENCE PROTOCOL (Must be first) ---
# Silence TensorFlow and Warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
warnings.filterwarnings("ignore") # <--- Kills the np.object warning

# Mute the specific libraries causing your issues
logging.getLogger('sentence_transformers').setLevel(logging.CRITICAL)
logging.getLogger('chromadb').setLevel(logging.CRITICAL)
logging.getLogger('tensorflow').setLevel(logging.CRITICAL)
logging.getLogger('huggingface_hub').setLevel(logging.CRITICAL)
logging.basicConfig(level=logging.CRITICAL)

# --- 2. NOW we import the heavy libraries ---
from mcp.server.fastmcp import FastMCP
from brain_dl import PricePredictor
from brain_rag import FinancialAnalyst

# Initialize MCP
mcp = FastMCP("Quant-Mind")

# Initialize Brains
dl_brain = PricePredictor()
rag_brain = FinancialAnalyst()

# Pre-load data
rag_brain.ingest_dummy_data()

@mcp.tool()
def predict_stock_trend(ticker: str) -> str:
    """Uses Deep Learning to predict stock price movement."""
    try:
        result = dl_brain.predict_next_price(ticker)
        return f"📊 PREDICTION FOR {ticker}: {result['trend']}\nCurrent: ${result['current_price']:.2f} -> Next: ${result['predicted_next_close']:.2f}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def consult_analyst_notes(ticker: str) -> str:
    """Uses RAG to find analyst notes."""
    try:
        return rag_brain.analyze_sentiment(ticker)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport='stdio')