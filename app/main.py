'''Main project file.'''
from search import request_data
import utils


request_data.RequestData(url=utils.constants.URL).data()
