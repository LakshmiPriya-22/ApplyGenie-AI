class PromptTemplates:
    """
    Centralized prompt templates for all RAG-powered AI features.
    """

    @staticmethod
    def resume_analysis(context: str) -> str:
        return f"""
You are an expert Resume Analyzer.

Resume:
{context}

IMPORTANT:

- Return ONLY valid JSON.
- Do NOT return Markdown.
- Do NOT wrap the JSON inside ```json.
- Do NOT include explanations.

Return JSON in EXACTLY this format:

{{
    "professional_summary": "",
    "technical_skills": [],
    "soft_skills": [],
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "career_suggestions": [],
    "resume_score": 0
}}

Rules:

- resume_score must be between 0 and 100.
- Return ONLY the JSON object.
"""

    @staticmethod
    def ats_analysis(context: str, job_description: str) -> str:
        return f"""
You are an ATS Resume Evaluator.

Resume:
{context}

Job Description:
{job_description}

IMPORTANT:

- Return ONLY valid JSON.
- No Markdown.
- No explanations.

Return JSON:

{{
    "ats_score": 0,
    "matching_skills": [],
    "missing_skills": [],
    "keyword_suggestions": [],
    "resume_improvements": [],
    "final_verdict": ""
}}

Rules:

- ats_score must be between 0 and 100.
- Return ONLY JSON.
"""

    @staticmethod
    def job_recommendation(context: str) -> str:
        return f"""
You are an AI Career Advisor.

Resume:
{context}

Return ONLY valid JSON.

Format:

{{
    "recommended_roles": [],
    "career_paths": [],
    "skills_to_learn": [],
    "certifications": [],
    "learning_roadmap": []
}}
"""

    @staticmethod
    def interview_questions(context: str) -> str:
        return f"""
You are an Interview Preparation Expert.

Resume:
{context}

Return ONLY valid JSON.

Format:

{{
    "hr_questions": [],
    "technical_questions": [],
    "project_questions": [],
    "coding_questions": [],
    "behavioral_questions": []
}}
"""

    @staticmethod
    def cover_letter(context: str, company: str, role: str) -> str:
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
    def resume_chat(context: str, history: str, question: str) -> str:
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
    def job_match(context: str, job_description: str) -> str:
        return f"""
You are an expert ATS Resume Matcher and Senior Technical Recruiter.

Your task is to compare the candidate's resume with the given job description
and produce an accurate ATS-style evaluation.

==================================================
RESUME
==================================================
{context}

==================================================
JOB DESCRIPTION
==================================================
{job_description}

IMPORTANT INSTRUCTIONS

- Return ONLY valid JSON.
- Do NOT return Markdown.
- Do NOT wrap JSON inside ```json.
- Do NOT include explanations.
- Do NOT invent skills or experience.
- Base every decision ONLY on the resume and job description.

Scoring Criteria (100 points)

1. Technical Skills Match (40%)
   - Required languages
   - Frameworks
   - Libraries
   - Databases
   - Cloud
   - DevOps

2. Projects & Experience (25%)
   - Similar projects
   - Domain knowledge
   - Practical implementation

3. Education & Certifications (10%)

4. Keyword Match (15%)
   - ATS keywords
   - Technologies
   - Responsibilities

5. Achievements & Extras (10%)
   - Coding profiles
   - Certifications
   - Open Source
   - Leadership

Scoring Guide

95-100 = Exceptional Match

85-94 = Strong Match

70-84 = Good Match

55-69 = Moderate Match

40-54 = Weak Match

0-39 = Poor Match

VERY IMPORTANT

The score MUST depend on the job description.

Examples:

If the job requires

- FastAPI
- Docker
- Kubernetes
- AWS

and the resume has only

- Python
- Django
- React

then the score SHOULD NOT exceed 65.

If almost every required technology is present,
the score should be above 85.

Return JSON EXACTLY like this:

{{
    "match_score": 0,
    "strengths": [],
    "missing_skills": [],
    "recommendations": [],
    "summary": ""
}}

Rules

1. match_score must be an integer from 0-100.
2. strengths should list technologies already present in the resume.
3. missing_skills should contain ONLY skills required by the job but absent from the resume.
4. recommendations should be specific and actionable.
5. summary should clearly explain WHY the score was assigned in 2-3 professional sentences.
6. Return ONLY the JSON object.
"""

    @staticmethod
    def resume_optimizer(context: str, job_description: str) -> str:
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

    @staticmethod
    def generate_interview(
        resume_analysis: dict,
        job_title: str,
        company: str,
        job_description: str,
        match_score: float,
        interview_type: str,
        difficulty: str,
    ) -> str:
        return f"""
You are an expert Technical Interviewer.

Candidate Resume Analysis:
{resume_analysis}

Company:
{company}

Job Title:
{job_title}

Job Description:
{job_description}

Resume Match Score:
{match_score}

Interview Type:
{interview_type}

Difficulty:
{difficulty}

Generate interview questions based on the resume and job description.

Return ONLY valid JSON.

Format:

{{
    "questions":[
        {{
            "question":"",
            "category":"Technical"
        }}
    ],

    "tips":[
        ""
    ],

    "roadmap":[
        ""
    ],

    "summary":""
}}

Rules

1. Generate 10-15 interview questions.
2. Mix Technical, HR, Coding, Behavioural and Project questions.
3. Questions must match the job requirements.
4. Do not invent resume details.
5. Return ONLY JSON.
"""

    @staticmethod
    def evaluate_interview(questions: list, answers: list) -> str:
        return f"""
You are a Senior Software Engineering Interviewer.

Interview Questions:

{questions}

Candidate Answers:

{answers}

Evaluate every answer.

Return ONLY valid JSON.

Format:

{{
    "score":0,

    "feedback":{{
        "strengths":[
            ""
        ],

        "weaknesses":[
            ""
        ],

        "suggestions":[
            ""
        ],

        "overall_feedback":""
    }}
}}

Rules

1. Score must be between 0 and 100.
2. Judge technical accuracy.
3. Judge communication.
4. Judge confidence.
5. Give constructive feedback.
6. Return ONLY JSON.
"""
