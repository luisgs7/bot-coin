'''Clean up the data provided by the API'''
from typing import Dict


class cleaning():
    def __init__(self, data: dict):
        self.data = data
        self.keys = ['USD', 'EUR', 'CAD']
        self.btc = ['mercadobitcoin']

    def clear_curencies(self):
        result: Dict = []
        for key in self.keys:
            result.append(self.data['currencies'][key]['name'])
            result.append(self.data['currencies'][key]['buy'])
            result.append(self.data['currencies'][key]['sell'])
            result.append(self.data['currencies'][key]['variation'])

        return result

    def clear_btc(self):
        result: Dict = []
        for btc in self.btc:
            result.append(self.data['bitcoin'][btc]['name'])
            result.append(self.data['bitcoin'][btc]['buy'])
            result.append(self.data['bitcoin'][btc]['sell'])
            result.append(self.data['bitcoin'][btc]['variation'])

        return result
