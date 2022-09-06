'''This file contains constants used in the project.'''
from decouple import config


__SECRET_KEY: str = config('SECRET_KEY')

URL = f'https://api.hgbrasil.com/finance?key={__SECRET_KEY}'
