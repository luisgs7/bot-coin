'''Main project file.'''
from data_request.search import request_data
from utils import constants
from data_cleaning.cleaning import cleaning


def main() -> None:
    '''Function Main'''
    result = request_data.RequestData(url=constants.URL).data()
    data = cleaning(result).clear_curencies()
    btc = cleaning(result).clear_btc()
    print(f"Data: {data}")
    print(f"BTC: {btc}")

main()
