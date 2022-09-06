'''Class to perform API calls sent via the url parameter.'''
import requests

class RequestData:
    '''Class RequestData'''

    def __init__(self, url: str):
        self.url = url

    def data(self):
        ''''Method that returns all API data'''
        data: str = self.filter_request_currencies()
        print(data)

    def filter_request_currencies(self):
        '''Filter request the API'''
        result: str = requests.get(self.url).json()['results']['currencies']
        return result

    def filter_request_bitcoin(self):
        result: str = requests.get(self.url).json()['results']['bitcoin']
        return result