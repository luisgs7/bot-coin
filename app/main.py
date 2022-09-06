'''Main project file.'''
from data_request.search import request_data
from utils import constants
from data_cleaning.cleaning import cleaning


def main() -> None:
    '''Function Main'''
    result = request_data.RequestData(url=constants.URL).data()
    data = cleaning(result).clear_cureencies()
    print(data)

main()
