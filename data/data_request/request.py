'''Python Module Request Data API'''
from data_request import request_data
from utils import constants, date_format


def present_data_request():
    '''The function's responsibility is to request the data,
       and send it to the later layer of the application.'''
    try:
        result = request_data.RequestData(url=constants.URL).data()
    except Exception: # noqa pylint: disable=broad-except
        print(f"Problems with the API: {date_format.date_present()}")
    return result
