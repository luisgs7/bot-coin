'''Clean up the data provided by the API'''
from typing import Dict
from data_save.data_connect import DataConnect
from data_cleaning import data_format
from data_save import data_save


class cleaning_data():
    def __init__(self, data: dict):
        self.data = data
        self.keys = ['USD', 'EUR', 'CAD', 'JPY']
        self.btc = ['mercadobitcoin']

    def clear_curencies(self):
        result: Dict = []
        sum: int = 1
        for key in self.keys:
            result.append(self.data['currencies'][key]['name'])
            result.append(self.data['currencies'][key]['buy'])
            result.append(self.data['currencies'][key]['sell'])
            result.append(self.data['currencies'][key]['variation'])
            
            result = data_format.data_format(result)
            print(f"Result: {result}")

            data_save.data_save(data=result, id_key=sum)
            result.clear()
            sum+=1

        return None

    def clear_btc(self):
        result: Dict = []
        sum: int = 5
        for btc in self.btc:
            result.append(self.data['bitcoin'][btc]['name'])
            result.append(self.data['bitcoin'][btc]['buy'])
            result.append(self.data['bitcoin'][btc]['sell'])
            result.append(self.data['bitcoin'][btc]['variation'])
            
            result = data_format.data_format(result)
            print(f"Result: {result}")

            data_save.data_save(data=result, id_key=sum)
            result.clear()
            sum+=1

        return None