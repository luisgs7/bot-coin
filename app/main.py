"""Main project file."""
import sched
from data_request.search import request_data
from utils import constants
from data_cleaning.cleaning import CleaningData

scheduler = sched.scheduler()


def main() -> None:
    """Function Main"""
    print("App running...")
    result = request_data.RequestData(url=constants.URL).data()
    CleaningData(result).clear_currencies()
    CleaningData(result).clear_btc()
    print("END.")
    scheduler.enter(delay=(constants.TIME), priority=0, action=main)
    print(f"Waiting: {constants.TIME} seconds...")


main()

scheduler.run(blocking=True)
