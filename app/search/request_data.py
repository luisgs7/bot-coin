'''Class to perform API calls sent via the url parameter.'''
import requests

class RequestData:
    '''Class RequestData'''

    def __init__(self, url: str):
        self.url = url

    def data(self):
        ''''Method that returns all API data'''
        data = requests.get(self.url).json()
        print(data)
