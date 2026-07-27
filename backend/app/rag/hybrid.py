from langchain_core.documents import Document

from app.rag.bm25 import BM25Retriever
from app.rag.vector_store import VectorStore
from app.rag.reranker import CrossEncoderReranker
from app.rag.config import TOP_K


class HybridRetriever:

    @staticmethod
    def retrieve(
        query: str,
        user_id,
        resume_id,
        k: int = TOP_K
    ) -> list[Document]:

        print("\n========== Hybrid Retriever ==========")

        # Convert IDs to string (metadata is stored as strings in Chroma)
        user_id = str(user_id)
        resume_id = str(resume_id)

        print("Query:", query)
        print("User:", user_id)
        print("Resume:", resume_id)

        filter_dict = {
            "$and": [
                {"user_id": user_id},
                {"resume_id": resume_id}
            ]
        }

        print("Filter:", filter_dict)

        # -----------------------------
        # Step 1: Vector Search
        # -----------------------------
        vector_results = VectorStore.similarity_search(
            query=query,
            k=k,
            filter_dict=filter_dict
        )

        print("Vector Results:", len(vector_results))

        # -----------------------------
        # Step 2: Load all documents
        # -----------------------------
        all_documents = VectorStore.get_documents(
            filter_dict=filter_dict
        )

        print("All Documents:", len(all_documents))

        # -----------------------------
        # Step 3: BM25 Search
        # -----------------------------
        bm25_results = BM25Retriever.retrieve(
            query=query,
            documents=all_documents,
            k=k
        )

        print("BM25 Results:", len(bm25_results))

        # -----------------------------
        # Step 4: Merge Results
        # -----------------------------
        merged = []
        seen = set()

        for doc in vector_results + bm25_results:
            if doc.page_content not in seen:
                merged.append(doc)
                seen.add(doc.page_content)

        print("Merged Results:", len(merged))

        # -----------------------------
        # Step 5: Cross Encoder Re-ranking
        # -----------------------------
        print("Before Re-ranking:", len(merged))

        reranked = CrossEncoderReranker.rerank(
            query=query,
            documents=merged,
            top_k=k
        )

        print("After Re-ranking:", len(reranked))
        print("=======================================\n")

        return reranked