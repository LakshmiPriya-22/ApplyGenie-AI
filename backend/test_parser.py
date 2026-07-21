from app.services.llm_service import LLMService

resume_text = """
John Doe

Email: john@example.com

Phone: 9876543210

Skills:
Python
Java
SQL

Education:
B.Tech Computer Science

Projects:
Library Management System

Certificates:
AWS Cloud Practitioner
"""

result = LLMService.parse_resume(resume_text)

print("\n========== RETURNED RESULT ==========")
print(result)
print("=====================================")