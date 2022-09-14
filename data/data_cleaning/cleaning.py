"""Clean up the data provided by the API"""
from typing import Dict
from data_save import data_save
from utils import constants
from data_cleaning import data_format


class CleaningData:
    """Class responsible for cleaning the data received from the API."""

    def __init__(self, data: dict):
        self.data = data
        self.keys = constants.COINS
        self.btc = constants.BTC
        self.lenght = constants.LENGHT

    def clear_currencies(self):
        """Method responsible for cleaning coin data."""
        result: Dict = []
        sum: int = 1  # pylint: disable=redefined-builtin

        for key in self.keys:
            result.append(self.data["currencies"][key]["name"])
            result.append(self.data["currencies"][key]["buy"])
            result.append(self.data["currencies"][key]["sell"])
            result.append(self.data["currencies"][key]["variation"])

            result = data_format.data_format(result)

            data_save.data_save(data=result, id_key=sum)
            result.clear()
            sum += 1

    def clear_btc(self):
        """Method responsible for cleaning cryptocurrency data."""
        result: Dict = []
        sum: int = self.lenght  # pylint: disable=redefined-builtin

        for btc in self.btc:
            result.append(self.data["bitcoin"][btc]["name"])
            result.append(self.data["bitcoin"][btc]["buy"])
            result.append(self.data["bitcoin"][btc]["sell"])
            result.append(self.data["bitcoin"][btc]["variation"])

            result = data_format.data_format(result)

            data_save.data_save(data=result, id_key=sum)
            result.clear()
            sum += 1
