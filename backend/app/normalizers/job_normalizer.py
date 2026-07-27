class JobNormalizer:

    @staticmethod
    def greenhouse(company: str, job: dict):

        return {

            "title": job.get("title"),

            "company": company.title(),

            "location": job.get(
                "location",
                {}
            ).get(
                "name",
                "Remote"
            ),

            "employment_type": "Unknown",

            "experience_level": "Unknown",

            "salary": None,

            "description": job.get(
                "content",
                ""
            ),

            "requirements": "",

            "skills": "",

            "apply_url": job.get(
                "absolute_url"
            ),

            "source": "Greenhouse"
        }