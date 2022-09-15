"""Class to perform API calls sent via the url parameter."""
import requests
from utils.mock import DATA_MOCK


class RequestData:
    """Class RequestData"""

    def __init__(self, url: str):
        self.url = url

    def data(self):
        """'Method that returns all API data"""
        data: str = self.filter_request_data()
        return data

    def filter_request_data(self):
        """Filter request the API"""
        result: str = requests.get(self.url).json()["results"] # noqa pylint: disable= missing-timeout
        return result

    def mock_data(self):
        """Data Mock Test"""
        return DATA_MOCK
