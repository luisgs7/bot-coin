'''This file contains constants used in the project.'''
from decouple import config


_SECRET_KEY: str = config('SECRET_KEY')

URL = f'https://api.hgbrasil.com/finance?key={_SECRET_KEY}'

# URL = f'https://api.hgbrasil.com/finance?format=json&key={_SECRET_KEY}'
