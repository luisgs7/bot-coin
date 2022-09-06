'''Clean up the data provided by the API'''

class cleaning():
    def __init__(self, data: dict):
        self.data = data
        self.keys = ['USD', 'EUR', 'CAD']
        self.btc = ['']

    def clear_cureencies(self):
        result = []
        for key in self.keys:
            result.append(self.data['currencies'][key]['name'])
            result.append(self.data['currencies'][key]['buy'])
            result.append(self.data['currencies'][key]['sell'])
            result.append(self.data['currencies'][key]['variation'])

        return result
    
    def clear_btc(self):
        pass