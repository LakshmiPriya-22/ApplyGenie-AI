from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Base class for every job provider.
    """

    @abstractmethod
    def discover_jobs(self) -> list[dict]:
        """
        Returns a list of jobs.

        Every provider must implement this.
        """
        pass