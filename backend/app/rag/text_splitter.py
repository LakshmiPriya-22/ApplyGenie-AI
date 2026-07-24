from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.rag.config import CHUNK_SIZE, CHUNK_OVERLAP


class TextSplitter:
    """
    Split PDF pages into smaller chunks while preserving metadata.
    """

    @staticmethod
    def split_documents(
        documents: list[Document]
    ) -> list[Document]:

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

        chunks = splitter.split_documents(documents)

        print("\n========== Text Splitter ==========")
        print(f"Input Pages : {len(documents)}")
        print(f"Output Chunks : {len(chunks)}")
        print("===================================\n")

        return chunks