from app.rag.retriever import ResumeRetriever
from app.rag.llm import llm
from app.rag.prompts import PromptTemplates
from app.rag.query_rewriter import QueryRewriter
from app.rag.memory import ConversationMemory
from app.rag.citations import CitationService
import json
import re


class RAGService:

    @staticmethod
    def _get_context(
        user_id: int,
        resume_id: int,
        query: str
    ) -> tuple[str, list]:
        """
        Rewrite the query before retrieving relevant resume chunks.
        Returns both the context string and retrieved documents.
        """

        rewritten_query = QueryRewriter.rewrite(query)

        documents = ResumeRetriever.retrieve(
            query=rewritten_query,
            user_id=user_id,
            resume_id=resume_id
        )

        if not documents:
            return "", []

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        return context, documents

    @staticmethod
    def resume_analysis(
        user_id: int,
        resume_id: int
    ) -> str:

        context, documents = RAGService._get_context(
            user_id=user_id,
            resume_id=resume_id,
            query="Analyze this resume completely."
        )

        prompt = PromptTemplates.resume_analysis(
            context=context
        )

        answer = llm.generate(prompt)

        sources = CitationService.format_sources(documents)

        return f"{answer}\n\nSources:\n{sources}"

    @staticmethod
    def ats_analysis(
        user_id: int,
        resume_id: int,
        job_description: str
    ) -> str:

        context, documents = RAGService._get_context(
            user_id=user_id,
            resume_id=resume_id,
            query=job_description
        )

        prompt = PromptTemplates.ats_analysis(
            context=context,
            job_description=job_description
        )

        answer = llm.generate(prompt)

        sources = CitationService.format_sources(documents)

        return f"{answer}\n\nSources:\n{sources}"

    @staticmethod
    def job_match(
        user_id: int,
        resume_id: int,
        job_description: str
    ) -> dict:
        """
        Compare the uploaded resume with a job description
        and return structured JSON.
        """

        context, documents = RAGService._get_context(
            user_id=user_id,
            resume_id=resume_id,
            query=job_description
        )

        prompt = PromptTemplates.job_match(
            context=context,
            job_description=job_description
        )

        response = llm.generate(prompt)

        if not response:
            raise ValueError("LLM returned an empty response.")

        response = response.strip()

        # Remove Markdown code fences if present
        response = re.sub(
            r"^```(?:json)?",
            "",
            response,
            flags=re.IGNORECASE
        )

        response = re.sub(
            r"```$",
            "",
            response
        ).strip()

        try:
            data = json.loads(response)

        except json.JSONDecodeError as e:

            raise ValueError(
                f"Invalid JSON returned by LLM:\n\n{response}"
            ) from e

        return data

    @staticmethod
    def job_recommendation(
        user_id: int,
        resume_id: int
    ) -> str:

        context, documents = RAGService._get_context(
            user_id=user_id,
            resume_id=resume_id,
            query="Recommend suitable jobs."
        )

        prompt = PromptTemplates.job_recommendation(
            context=context
        )

        answer = llm.generate(prompt)

        sources = CitationService.format_sources(documents)

        return f"{answer}\n\nSources:\n{sources}"

    @staticmethod
    def interview_questions(
        user_id: int,
        resume_id: int
    ) -> str:

        context, documents = RAGService._get_context(
            user_id=user_id,
            resume_id=resume_id,
            query="Generate interview questions."
        )

        prompt = PromptTemplates.interview_questions(
            context=context
        )

        answer = llm.generate(prompt)

        sources = CitationService.format_sources(documents)

        return f"{answer}\n\nSources:\n{sources}"

    @staticmethod
    def cover_letter(
        user_id: int,
        resume_id: int,
        company: str,
        role: str
    ) -> str:

        context, documents = RAGService._get_context(
            user_id=user_id,
            resume_id=resume_id,
            query=f"{company} {role}"
        )

        prompt = PromptTemplates.cover_letter(
            context=context,
            company=company,
            role=role
        )

        answer = llm.generate(prompt)

        sources = CitationService.format_sources(documents)

        return f"{answer}\n\nSources:\n{sources}"

    @staticmethod
    def resume_chat(
        user_id: int,
        resume_id: int,
        question: str
    ) -> str:

        history = ConversationMemory.get_history(user_id)

        context, documents = RAGService._get_context(
            user_id=user_id,
            resume_id=resume_id,
            query=question
        )

        prompt = PromptTemplates.resume_chat(
            context=context,
            history=history,
            question=question
        )

        answer = llm.generate(prompt)

        ConversationMemory.add_message(
            user_id=user_id,
            role="User",
            content=question
        )

        ConversationMemory.add_message(
            user_id=user_id,
            role="Assistant",
            content=answer
        )

        sources = CitationService.format_sources(documents)

        return f"{answer}\n\nSources:\n{sources}"

    @staticmethod
    def resume_optimizer(
        user_id: int,
        resume_id: int,
        job_description: str
    ) -> dict:
        """
        Optimize the uploaded resume for a specific job description.
        Returns structured JSON.
        """

        context, documents = RAGService._get_context(
            user_id=user_id,
            resume_id=resume_id,
            query=job_description
        )

        prompt = PromptTemplates.resume_optimizer(
            context=context,
            job_description=job_description
        )

        response = llm.generate(prompt)

        if not response:
            raise ValueError("LLM returned an empty response.")

        response = response.strip()

        response = re.sub(
            r"^```(?:json)?",
            "",
            response,
            flags=re.IGNORECASE
        )

        response = re.sub(
            r"```$",
            "",
            response
        ).strip()

        try:
            data = json.loads(response)
        except json.JSONDecodeError as e:
            raise ValueError(
                f"Invalid JSON returned by LLM:\n\n{response}"
            ) from e

        return data

    @staticmethod
    def clear_chat(
        user_id: int
    ):
        """
        Clear chat history for a user.
        """
        ConversationMemory.clear(user_id)