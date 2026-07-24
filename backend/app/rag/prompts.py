class PromptTemplates:
    """
    Centralized prompt templates for all RAG-powered AI features.
    """

    @staticmethod
    def resume_analysis(context: str) -> str:
        return f"""
You are an expert Resume Analyzer.

Analyze ONLY the resume information provided below.

Resume:
{context}

Generate a professional analysis with the following sections:

1. Professional Summary
2. Technical Skills
3. Soft Skills
4. Strengths
5. Weaknesses
6. Missing Skills
7. Career Suggestions
8. Overall Resume Score (out of 100)

Return the response in clean Markdown.
"""

    @staticmethod
    def ats_analysis(
        context: str,
        job_description: str
    ) -> str:
        return f"""
You are an ATS Resume Evaluator.

Resume:
{context}

Job Description:
{job_description}

Provide:

1. ATS Match Score (0-100)
2. Matching Skills
3. Missing Skills
4. Keyword Suggestions
5. Resume Improvement Suggestions
6. Final Verdict

Return the response in Markdown.
"""

    @staticmethod
    def job_recommendation(context: str) -> str:
        return f"""
You are an AI Career Advisor.

Resume:
{context}

Recommend:

1. Best Job Roles
2. Suitable Career Paths
3. Skills to Learn
4. Certifications
5. Next Learning Roadmap

Return the response in Markdown.
"""

    @staticmethod
    def interview_questions(context: str) -> str:
        return f"""
You are an Interview Preparation Expert.

Resume:
{context}

Generate:

1. HR Questions
2. Technical Questions
3. Project-based Questions
4. Coding Questions
5. Behavioral Questions

Return the response in Markdown.
"""

    @staticmethod
    def cover_letter(
        context: str,
        company: str,
        role: str
    ) -> str:
        return f"""
You are a Professional Cover Letter Writer.

Resume:
{context}

Company:
{company}

Role:
{role}

Write a personalized professional cover letter.

Return only the cover letter.
"""

    @staticmethod
    def resume_chat(
        context: str,
        history: str,
        question: str
    ) -> str:
        return f"""
You are an AI Resume Assistant.

Conversation History:

{history}

Resume Context:

{context}

Current Question:

{question}

Instructions:

- Use BOTH the conversation history and the resume.
- Never make up information.
- If the answer is not present in the resume, reply exactly:

"I could not find this information in the uploaded resume."

Return only the answer.
"""

    @staticmethod
    def job_match(
        context: str,
        job_description: str
    ) -> str:
        return f"""
You are an ATS Resume Expert.

Resume:

{context}

Job Description:

{job_description}

Compare the resume with the job description.

Generate:

# ATS Score (0-100)

# Matching Skills

# Missing Skills

# Strengths

# Weaknesses

# Resume Improvement Suggestions

# Learning Roadmap

# Final Verdict

Return the answer in Markdown.
"""

    @staticmethod
    def resume_optimizer(
        context: str,
        job_description: str
    ) -> str:
        return f"""
You are an expert Resume Optimizer and ATS specialist.

Resume:
{context}

Target Job Description:
{job_description}

Analyze the resume against the job description and optimize it.

IMPORTANT INSTRUCTIONS:

- Return ONLY valid JSON.
- Do NOT return Markdown.
- Do NOT return explanations.
- Do NOT wrap the JSON inside ```json or ``` blocks.
- Do NOT include any text before or after the JSON.
- Do NOT invent projects, certifications, companies, skills, education, or experience.
- Rewrite the existing content professionally using ATS-friendly language.
- Use keywords from the job description whenever appropriate.

Return JSON in EXACTLY this format:

{{
    "name": "",
    "email": "",
    "phone": "",
    "linkedin": "",
    "github": "",

    "summary": "",

    "skills": [
        ""
    ],

    "projects": [
        {{
            "title": "",
            "description": "",
            "technologies": ""
        }}
    ],

    "education": "",

    "certifications": [
        ""
    ],

    "achievements": [
        ""
    ],

    "ats_score": 0,

    "missing_skills": [
        ""
    ],

    "suggestions": [
        ""
    ]
}}

Rules:

1. Keep all existing truthful information.
2. Never invent information.
3. Rewrite the professional summary.
4. Improve project descriptions.
5. Extract all technical skills into the skills array.
6. Calculate ATS score between 0 and 100.
7. Include missing skills based on the job description.
8. Give practical resume improvement suggestions.
9. Every field must be present.
10. Return ONLY the JSON object.
"""