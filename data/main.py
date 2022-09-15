"""Main project file."""
import sched
from datetime import datetime, timezone, timedelta
from data_request import request_data
from utils import constants
from data_cleaning.cleaning import CleaningData

scheduler = sched.scheduler()

difference = timedelta(hours=-3)
time_zone = timezone(difference)
date_now = datetime.now()
date_and_time_sp = date_now.astimezone(time_zone)
date_now_text = date_and_time_sp.strftime("%d/%m/%Y %H:%M")


def main() -> None:
    """Function Main"""
    print("App running...")
    result = request_data.RequestData(url=constants.URL).data()
    if result is None:
        print(f"Problems with the API: {date_now_text}")
    else:
        CleaningData(result).clear_currencies()
        CleaningData(result).clear_btc()
    print("END.")
    scheduler.enter(delay=(constants.TIME), priority=0, action=main)
    print(f"Waiting: {constants.TIME} seconds...")


main()

scheduler.run(blocking=True)
