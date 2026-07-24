from rank_bm25 import BM25Okapi
from langchain_core.documents import Document


class BM25Retriever:
    """
    Performs keyword-based retrieval using BM25.
    """

    @staticmethod
    def retrieve(
        query: str,
        documents: list[Document],
        k: int = 5
    ) -> list[Document]:
        """
        Retrieve the top-k most relevant documents using BM25.
        """

        if not documents:
            return []

        # Tokenize document contents
        corpus = [
            doc.page_content.lower().split()
            for doc in documents
        ]

        # Build BM25 index
        bm25 = BM25Okapi(corpus)

        # Tokenize query
        tokenized_query = query.lower().split()

        # Compute scores
        scores = bm25.get_scores(tokenized_query)

        # Sort document indices by score
        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )

        # Return top-k documents
        results = []

        for index in ranked_indices[:k]:
            results.append(documents[index])

        return results