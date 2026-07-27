import os

CHROMA_PATH = "database/chroma_db"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_MODEL = "llama-3.3-70b-versatile"

CHUNK_SIZE = 800

CHUNK_OVERLAP = 150

TOP_K = 5

GROQ_API_KEY = os.getenv("GROQ_API_KEY")