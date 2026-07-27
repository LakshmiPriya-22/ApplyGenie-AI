from app.rag.document_loader import DocumentLoader
from app.rag.text_splitter import TextSplitter
from app.rag.vector_store import VectorStore


class ResumeIndexer:

    @staticmethod
    def index_resume(
        filepath: str,
        resume_id: int,
        user_id: int,
        filename: str
    ):
        """
        Extract PDF pages, split into chunks while preserving page metadata,
        attach resume metadata, and store in ChromaDB.
        """

        print("=" * 70)
        print("Starting Resume Indexing...")

        # Load PDF as Documents (one per page)
        documents = DocumentLoader.load_pdf(filepath)

        if not documents:
            raise Exception("No text could be extracted from the PDF.")

        print(f"Loaded Pages: {len(documents)}")

        # Split into chunks
        chunks = TextSplitter.split_documents(documents)

        print(f"Total Chunks: {len(chunks)}")

        # Add metadata to every chunk
        for index, chunk in enumerate(chunks):

            chunk.metadata.update(
                {
                    "resume_id": str(resume_id),
                    "user_id": str(user_id),
                    "filename": filename,
                    "chunk_number": index
                }
            )

            print(f"\nChunk {index}")
            print(f"Page: {chunk.metadata.get('page')}")
            print(chunk.page_content[:200])

        print(f"\nCreated {len(chunks)} chunks")

        # Store in ChromaDB
        VectorStore.add_documents(chunks)

        print("\nResume Indexed Successfully")

        VectorStore.debug_collection()

        print("=" * 70)

    @staticmethod
    def delete_resume(
        resume_id: int
    ):

        VectorStore.delete_resume(str(resume_id))