from decouple import config

DATABASE_URL = config("DATABASE_URL")
TABLE_NAME = config("TABLE_NAME")