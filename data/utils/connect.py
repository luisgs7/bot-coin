'''Connect Database Module'''
import psycopg2
from utils import constants


def link():
    '''Function responsibility connects Database'''
    try:
        data_connect = psycopg2.connect(constants.BASE_URL)
    except Exception: # noqa pylint: disable=broad-except
        data_connect = None
    return data_connect
