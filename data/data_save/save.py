'''Module Save Data'''
from data_cleaning.cleaning import CleaningData


def present_data_save(data):
    '''Function present data saved'''
    try:
        CleaningData(data).clear_currencies()
        CleaningData(data).clear_btc()
    except Exception: # noqa pylint: disable=broad-except
        print("Data not saved")
