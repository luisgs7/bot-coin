"""This file contains constants used in the project."""
from typing import List
from decouple import config


DB_USER = config("DB_USER")
DB_PASS = config("DB_PASS")
DB_NAME = config("DB_NAME")
DB_HOST = config("DB_HOST")

SECRET_KEY: str = "f2fcc2cc"
URL = f"https://api.hgbrasil.com/finance?key={SECRET_KEY}"
TIME: int = int(config("TIME"))

TABLE_NAME: str = config("TABLE_NAME")
BASE_URL: str = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"


COINS: List[str] = ["USD", "EUR", "CAD", "JPY"]
BTC: List[str] = ["mercadobitcoin"]
LENGHT: int = len(COINS + BTC)
