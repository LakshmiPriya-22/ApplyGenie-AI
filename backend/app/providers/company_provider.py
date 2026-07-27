from app.providers.base_provider import BaseProvider


class CompanyProvider(BaseProvider):
    """
    Mock Company Careers Provider.

    Later this provider will fetch jobs from
    company career pages or official APIs.
    """

    def discover_jobs(self):

        jobs = [

            {
                "title": "Python Backend Developer Intern",
                "company": "Google",
                "location": "Bangalore",
                "employment_type": "Internship",
                "experience_level": "Fresher",
                "salary": "₹40,000/month",
                "description": (
                    "Develop backend APIs using Python."
                ),
                "requirements": (
                    "Python, FastAPI, PostgreSQL"
                ),
                "skills": (
                    "Python, FastAPI, PostgreSQL, Git"
                )
            },

            {
                "title": "Software Engineer Intern",
                "company": "Microsoft",
                "location": "Hyderabad",
                "employment_type": "Internship",
                "experience_level": "Fresher",
                "salary": "₹50,000/month",
                "description": (
                    "Work on cloud-based software products."
                ),
                "requirements": (
                    "Java, Python, SQL"
                ),
                "skills": (
                    "Java, Python, SQL, Git"
                )
            }

        ]

        return jobs