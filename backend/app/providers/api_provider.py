from app.providers.base_provider import BaseProvider


class APIProvider(BaseProvider):
    """
    Fetch jobs using official Job APIs.
    """

    def discover_jobs(self) -> list[dict]:

        print("Searching jobs from Official APIs...")

        jobs = []

        # Future:
        # Greenhouse API
        # Lever API
        # Ashby API

        return jobs