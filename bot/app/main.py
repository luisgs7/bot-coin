"""Main project file."""
import sched
from decouple import config

scheduler = sched.scheduler()


BOT: str = config("HELLO")


def hello() -> None:
    """Function Main"""
    print(f"{BOT * 3}...")
    scheduler.enter(delay=(2), priority=0, action=hello)
    print("BOT Waiting: 2 seconds...")


hello()

scheduler.run(blocking=True)
