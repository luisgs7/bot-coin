"""Main project file."""
import sched
from data_request import request
from data_save import save, start_data
from utils import constants

scheduler = sched.scheduler()

start_data.start_table()

def main() -> None:
    """Function Main"""
    print("App running...")
    result = request.present_data_request()
    save.present_data_save(result)
    print("END.")
    scheduler.enter(delay=(constants.TIME), priority=0, action=main)
    print(f"Waiting: {constants.TIME} seconds...")


main()

scheduler.run(blocking=True)
