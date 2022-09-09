'''This file contains constants used in the project.'''
from decouple import config
from typing import List


SECRET_KEY: str = config('SECRET_KEY')

COINS: List[str] = ['USD', 'EUR', 'CAD', 'JPY']
BTC: List[str] = ['mercadobitcoin']
LENGHT: int = len(COINS + BTC)

URL = f'https://api.hgbrasil.com/finance?key={SECRET_KEY}'

# URL = f'https://api.hgbrasil.com/finance?format=json&key={SECRET_KEY}'
