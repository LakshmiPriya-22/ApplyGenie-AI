from langchain_core.documents import Document


class CitationService:

    @staticmethod
    def format_sources(documents: list[Document]) -> str:
        """
        Extract unique source information from retrieved documents.
        """

        if not documents:
            return "No sources available."

        sources = []

        for doc in documents:

            metadata = doc.metadata

            page = metadata.get("page", "Unknown")

            source = metadata.get("source", "Resume")

            text = f"{source} (Page {page})"

            if text not in sources:
                sources.append(text)

        return "\n".join(
            f"• {item}"
            for item in sources
        )