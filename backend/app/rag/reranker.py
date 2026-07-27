from langchain_core.documents import Document
from sentence_transformers import CrossEncoder


class CrossEncoderReranker:

    _model = None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            cls._model = CrossEncoder(
                "cross-encoder/ms-marco-MiniLM-L-6-v2"
            )
        return cls._model

    @classmethod
    def rerank(
        cls,
        query: str,
        documents: list[Document],
        top_k: int = 4
    ) -> list[Document]:

        if not documents:
            return []

        model = cls.get_model()

        pairs = [
            (query, doc.page_content)
            for doc in documents
        ]

        scores = model.predict(pairs)

        ranked = sorted(
            zip(documents, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [doc for doc, _ in ranked[:top_k]]