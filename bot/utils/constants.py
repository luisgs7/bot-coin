'''This module contains important project constants.'''
from decouple import config

DATABASE_URL = config("DATABASE_URL")
TABLE_NAME = config("TABLE_NAME")

TOKEN: str = config("TELEGRAM_BOT_TOKEN")
TELEGRAM_URL = f'https://api.telegram.org/bot{TOKEN}/'
MESSAGE_ABOUT = config("MESSAGE_ABOUT")
