import requests


class GreenhouseClient:

    BASE_URL = "https://boards-api.greenhouse.io/v1/boards"

    def get_jobs(self, company: str):

        url = f"{self.BASE_URL}/{company}/jobs"

        response = requests.get(
            url,
            headers={
                "User-Agent": "ApplyGenie-AI"
            },
            timeout=20
        )

        response.raise_for_status()

        return response.json()