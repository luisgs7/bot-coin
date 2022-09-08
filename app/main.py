'''Main project file.'''
from data_request.search import request_data
from utils import constants
from data_cleaning.cleaning import cleaning_data


def main() -> None:
    '''Function Main'''
    print("App running...")
    result = request_data.RequestData(url=constants.URL).data()
    data = cleaning_data(result).clear_curencies()
    btc = cleaning_data(result).clear_btc()
    print("Updated data.")

main()
