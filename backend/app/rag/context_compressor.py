from langchain_core.documents import Document


class ContextCompressor:

    @staticmethod
    def compress(
        query: str,
        documents: list[Document]
    ) -> list[Document]:

        if not documents:
            return []

        compressed = []

        keywords = [
            word.lower()
            for word in query.split()
            if len(word) > 2
        ]

        for doc in documents:

            sentences = doc.page_content.split(".")

            important = []

            for sentence in sentences:

                lower = sentence.lower()

                if any(k in lower for k in keywords):
                    important.append(sentence.strip())

            if important:

                compressed.append(
                    Document(
                        page_content=". ".join(important),
                        metadata=doc.metadata
                    )
                )

            else:

                compressed.append(doc)

        return compressed