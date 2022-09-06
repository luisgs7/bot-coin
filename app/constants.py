'''This file contains constants used in the project.'''
import os


__my_apikye = os.getenv("APIKYE")

URL = f'https://api.hgbrasil.com/finance?key={__my_apikye}'
