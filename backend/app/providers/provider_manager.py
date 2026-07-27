from app.providers.greenhouse_provider import GreenhouseProvider
from app.providers.api_provider import APIProvider
from app.providers.company_provider import CompanyProvider
from app.providers.unstop_provider import UnstopProvider
from app.providers.wellfound_provider import WellfoundProvider


class ProviderManager:

    def __init__(self):

        self.providers = [
            GreenhouseProvider(),
            APIProvider(),
            CompanyProvider(),
            UnstopProvider(),
            WellfoundProvider()
        ]

    def discover_jobs(self):

        jobs = []

        for provider in self.providers:

            try:

                provider_jobs = provider.discover_jobs()

                if provider_jobs:
                    jobs.extend(provider_jobs)

            except Exception as e:

                print(
                    f"{provider.__class__.__name__} failed: {e}"
                )

        return jobs