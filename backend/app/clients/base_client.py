import requests


class BaseClient:

    def get(self, url: str):

        response = requests.get(
            url,
            timeout=20
        )

        response.raise_for_status()

        return response.json()