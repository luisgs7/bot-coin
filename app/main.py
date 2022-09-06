'''Main project file.'''
from search import request_data
import constants


request_data.RequestData(url=constants.URL).data()
