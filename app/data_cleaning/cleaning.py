'''Clean up the data provided by the API'''
from typing import Dict
from data_save.data_connect import DataConnect


class cleaning_data():
    def __init__(self, data: dict):
        self.data = data
        self.keys = ['USD', 'EUR', 'CAD']
        self.btc = ['mercadobitcoin']

    def clear_curencies(self):
        result: Dict = []
        sum: int = 1
        for key in self.keys:
            result.append(self.data['currencies'][key]['name'])
            result.append(self.data['currencies'][key]['buy'])
            result.append(self.data['currencies'][key]['sell'])
            result.append(self.data['currencies'][key]['variation'])
            
            count = 0
            for data in result:
                if data == None or data == null:
                    result[count] = 0
                    print(f"NONE == {data}")
                count+=1
            print(f"Result: {result}")
            

            #DataConnect().update_coin(id=sum, name=result[0], buy=result[1], sell=result[2], variation=result[3])
            result.clear()
            sum+=1

        return None

    def clear_btc(self):
        result: Dict = []
        sum: int = 4
        for btc in self.btc:
            result.append(self.data['bitcoin'][btc]['name'])
            result.append(self.data['bitcoin'][btc]['buy'])
            result.append(self.data['bitcoin'][btc]['sell'])
            result.append(self.data['bitcoin'][btc]['variation'])
            
            count = 0
            for data in result:
                if data == None or data == null:
                    result[count] = 0
                    print(f"NONE == {data}")
                count+=1
            print(f"Result: {result}")

            DataConnect().update_coin(id=sum, name=result[0], buy=result[1], sell=result[2], variation=result[3])
            result.clear()
            sum+=1

        return None
