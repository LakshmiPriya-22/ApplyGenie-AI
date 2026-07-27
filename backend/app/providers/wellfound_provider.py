from app.providers.base_provider import BaseProvider


class WellfoundProvider(BaseProvider):
    """
    Fetch startup jobs from Wellfound.
    """

    def discover_jobs(self) -> list[dict]:

        print("Searching Wellfound...")

        jobs = []

        return jobs