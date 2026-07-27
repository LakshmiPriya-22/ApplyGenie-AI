from app.providers.base_provider import BaseProvider


class UnstopProvider(BaseProvider):
    """
    Fetch internships from Unstop.
    """

    def discover_jobs(self) -> list[dict]:

        print("Searching Unstop...")

        jobs = []

        return jobs