from app.rag.llm import llm


class QueryRewriter:
    """
    Rewrites user queries into detailed search queries
    to improve retrieval quality.
    """

    @staticmethod
    def rewrite(question: str) -> str:

        prompt = f"""
You are an expert query rewriting assistant for a Resume RAG system.

Your task is ONLY to rewrite the user's question into a clear,
self-contained search query suitable for semantic retrieval.

Rules:
- Do NOT answer the question.
- Do NOT explain anything.
- Return ONLY the rewritten query.
- Preserve the original intent.
- Expand vague questions into detailed resume search queries.

Examples:

User:
Skills?

Output:
What technical skills, programming languages, frameworks, databases, tools, and technologies are mentioned in the candidate's resume?

-------------------------

User:
Projects?

Output:
What projects are described in the candidate's resume, including technologies used, responsibilities, and achievements?

-------------------------

User:
Education?

Output:
What educational qualifications, degrees, college information, and academic achievements are mentioned in the candidate's resume?

-------------------------

User:
Internship?

Output:
What internships, work experience, responsibilities, and accomplishments are mentioned in the candidate's resume?

-------------------------

User Question:
{question}

Rewritten Query:
"""

        rewritten_query = llm.generate(
    prompt=prompt,
    system_prompt=(
        "You are a query rewriting assistant. "
        "Rewrite search queries only. "
        "Never answer the question."
    ),
    temperature=0.0,
    max_tokens=150
)

        print("\n========== Query Rewriter ==========")
        print("Original :", question)
        print("Rewritten:", rewritten_query)
        print("====================================\n")

        return rewritten_query.strip()