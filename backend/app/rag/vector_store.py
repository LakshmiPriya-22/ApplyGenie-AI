from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.rag.config import CHROMA_PATH
from app.rag.embeddings import EmbeddingModel


class VectorStore:

    _db = None

    @classmethod
    def get_db(cls):
        """
        Load or create the Chroma database.
        """

        if cls._db is None:
            cls._db = Chroma(
                persist_directory=CHROMA_PATH,
                embedding_function=EmbeddingModel.get_embeddings()
            )

        return cls._db

    @classmethod
    def add_documents(
        cls,
        documents: list[Document]
    ):
        """
        Store document chunks into ChromaDB.
        """

        db = cls.get_db()

        ids = [
            f"{doc.metadata['resume_id']}_{doc.metadata['chunk_number']}"
            for doc in documents
        ]

        db.add_documents(
            documents=documents,
            ids=ids
        )

        print("\n========== Vector Store ==========")
        print(f"Stored Documents : {len(documents)}")
        print("==================================")

    @classmethod
    def similarity_search(
        cls,
        query: str,
        k: int = 5,
        filter_dict: dict | None = None
    ) -> list[Document]:
        """
        Retrieve top-k documents using vector search.
        """

        db = cls.get_db()

        documents = db.similarity_search(
            query=query,
            k=k,
            filter=filter_dict
        )

        return documents

    @classmethod
    def get_documents(
        cls,
        filter_dict: dict | None = None
    ) -> list[Document]:
        """
        Retrieve all documents for BM25 retrieval.
        """

        db = cls.get_db()

        if filter_dict:
            data = db._collection.get(where=filter_dict)
        else:
            data = db._collection.get()

        documents = []

        for text, metadata in zip(
            data["documents"],
            data["metadatas"]
        ):
            documents.append(
                Document(
                    page_content=text,
                    metadata=metadata
                )
            )

        return documents

    @classmethod
    def delete_resume(
        cls,
        resume_id: str
    ):
        """
        Delete all chunks belonging to a resume.
        """

        db = cls.get_db()

        db.delete(
            where={
                "resume_id": resume_id
            }
        )

    @classmethod
    def debug_collection(cls):
        """
        Print Chroma collection details.
        """

        db = cls.get_db()

        collection = db._collection

        print("\n========== CHROMA DEBUG ==========")
        print("Collection Count:", collection.count())

        data = collection.get()

        for i in range(len(data["ids"])):

            print("\n--------------------------------")
            print("ID:", data["ids"][i])
            print("Metadata:", data["metadatas"][i])

            preview = data["documents"][i][:150].replace("\n", " ")
            print("Preview:", preview)

        print("==================================\n")