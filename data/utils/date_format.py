'''Module Date Format Present'''
from datetime import datetime, timezone, timedelta


def date_present():
    '''Function present DateTime'''
    difference = timedelta(hours=-3)
    time_zone = timezone(difference)
    date_now = datetime.now()
    date_and_time_sp = date_now.astimezone(time_zone)
    return date_and_time_sp.strftime("%d/%m/%Y %H:%M")
