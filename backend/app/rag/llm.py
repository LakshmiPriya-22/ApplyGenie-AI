from groq import Groq

from app.config.settings import settings


class GroqLLM:
    """
    Wrapper class for interacting with the Groq LLM.
    """

    def __init__(self):
        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )
        self.model = settings.LLM_MODEL

    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        temperature: float = 0.2,
        max_tokens: int = 1024
    ) -> str:
        """
        Generate a response from Groq.
        """

        if system_prompt is None:
            system_prompt = (
                "You are an expert AI career assistant. "
                "Answer ONLY using the provided resume context. "
                "If the answer cannot be found in the context, "
                "say that the information is not available."
            )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content.strip()


llm = GroqLLM()