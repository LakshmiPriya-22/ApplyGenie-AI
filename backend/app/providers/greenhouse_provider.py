from app.providers.base_provider import BaseProvider

from app.clients.greenhouse_client import GreenhouseClient

from app.normalizers.job_normalizer import JobNormalizer

from app.config.company_list import GREENHOUSE_COMPANIES


class GreenhouseProvider(BaseProvider):

    def __init__(self):

        self.client = GreenhouseClient()

    def discover_jobs(self):

        jobs = []

        for company in GREENHOUSE_COMPANIES:

            try:

                response = self.client.get_jobs(company)

                for job in response.get("jobs", []):

                    jobs.append(

                        JobNormalizer.greenhouse(
                            company,
                            job
                        )

                    )

            except Exception as e:

                print(
                    f"{company}: {e}"
                )

        return jobs