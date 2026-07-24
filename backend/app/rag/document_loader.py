import os
import pdfplumber

from langchain_core.documents import Document


class DocumentLoader:
    @staticmethod
    def load_pdf(file_path: str) -> list[Document]:
        """
        Load a PDF and return one Document per page with metadata.
        """

        documents = []

        filename = os.path.basename(file_path)

        with pdfplumber.open(file_path) as pdf:

            for page_number, page in enumerate(pdf.pages, start=1):

                page_text = page.extract_text()

                if not page_text:
                    continue

                documents.append(
                    Document(
                        page_content=page_text,
                        metadata={
                            "source": filename,
                            "page": page_number
                        }
                    )
                )

        print(f"\nLoaded {len(documents)} pages from {filename}")

        return documents