from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
# Updated import for text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
# FIX: Updated import for Document class
from langchain_core.documents import Document
import os
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

class FinancialAnalyst:
    def __init__(self):
        # Initialize Embeddings (Silent)
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # Initialize Vector Database
        self.db_path = "./chroma_db"
        self.vector_store = Chroma(
            persist_directory=self.db_path, 
            embedding_function=self.embeddings
        )

    def ingest_dummy_data(self):
        """Creates dummy financial reports."""
        texts = [
            "APPLE (AAPL): Strong iPhone 16 sales projected. Supply chain in India is stable. Risks: High valuation.",
            "TESLA (TSLA): Robotaxi launch delayed. Margins compressing due to price cuts. Battery tech is improving.",
            "NVIDIA (NVDA): AI chip demand is infinite. Blackwell chips are sold out until 2026. No competitors nearby.",
            "MICROSOFT (MSFT): Copilot revenue growing 30% QoQ. Azure cloud taking market share from AWS.",
            "GOOGLE (GOOGL): Ad revenue stable. Facing regulatory pressure in EU. Gemini model integration is key focus."
        ]
        
        docs = [Document(page_content=t) for t in texts]
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        splits = text_splitter.split_documents(docs)
        
        self.vector_store.add_documents(splits)

    def analyze_sentiment(self, query):
        """Retrieves relevant docs."""
        results = self.vector_store.similarity_search(query, k=2)
        
        if not results:
            return "No relevant internal reports found."
            
        context = "\n".join([doc.page_content for doc in results])
        return f"🔎 RAG RETRIEVAL:\n{context}"