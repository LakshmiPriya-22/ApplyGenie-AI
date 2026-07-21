import json

from app.llm.groq_client import client


class LLMService:

    @staticmethod
    def parse_resume(text: str):

        prompt = f"""
You are an expert ATS Resume Parser.

Extract the following information from the resume.

Return ONLY valid JSON.

JSON format:

{{
    "name": "",
    "email": "",
    "phone": "",
    "skills": [],
    "education": [],
    "projects": [],
    "certifications": []
}}

Resume:

{text}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        result = response.choices[0].message.content.strip()

        # Remove markdown code fences if present
        if result.startswith("```json"):
            result = result.replace("```json", "", 1)

        if result.startswith("```"):
            result = result.replace("```", "", 1)

        if result.endswith("```"):
            result = result[:-3]

        result = result.strip()

        try:
            return json.loads(result)
        except json.JSONDecodeError:
            return {
                "error": "Invalid JSON returned by LLM",
                "raw_response": result
            }
