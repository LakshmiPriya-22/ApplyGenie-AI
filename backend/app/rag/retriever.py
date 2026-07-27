from langchain_core.documents import Document

from app.rag.hybrid import HybridRetriever
from app.rag.context_compressor import ContextCompressor


class ResumeRetriever:
    """
    Retrieves relevant resume chunks using:
    1. Hybrid Retrieval (Vector + BM25)
    2. Context Compression
    """

    @staticmethod
    def retrieve(
        query: str,
        user_id: str,
        resume_id: str,
        k: int = 5
    ) -> list[Document]:

        print("\n========== ResumeRetriever ==========")
        print("Query:", query)
        print("=====================================\n")

        # Step 1: Hybrid Retrieval
        documents = HybridRetriever.retrieve(
            query=query,
            user_id=user_id,
            resume_id=resume_id,
            k=k
        )

        print("\n======= Context Compressor =======")
        print(f"Retrieved Documents : {len(documents)}")

        # Step 2: Context Compression
        compressed_documents = ContextCompressor.compress(
            query=query,
            documents=documents
        )

        print(f"Compressed Documents: {len(compressed_documents)}")
        print("==================================\n")

        return compressed_documents