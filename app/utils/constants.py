"""This file contains constants used in the project."""
from typing import List
from decouple import config


SECRET_KEY: str = config("SECRET_KEY")
URL = f"https://api.hgbrasil.com/finance?key={SECRET_KEY}"
TIME: int = int(config("TIME"))

TABLE_NAME: str = config("TABLE_NAME")
BASE_URL: str = config("DATABASE_URL")


COINS: List[str] = ["USD", "EUR", "CAD", "JPY"]
BTC: List[str] = ["mercadobitcoin"]
LENGHT: int = len(COINS + BTC)
