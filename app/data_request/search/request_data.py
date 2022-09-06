'''Class to perform API calls sent via the url parameter.'''
import requests
from utils.mock import DATA_MOCK


class RequestData:
    '''Class RequestData'''

    def __init__(self, url: str):
        self.url = url

    def data(self):
        ''''Method that returns all API data'''
        data: str = self.mock_data()
        print(data)

    def filter_request_data(self):
        '''Filter request the API'''
        result: str = requests.get(self.url).json()['results']
        return result

    def mock_data(self):
        return DATA_MOCK
