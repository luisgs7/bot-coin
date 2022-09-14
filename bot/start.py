"""Main project file."""
import sched
scheduler = sched.scheduler()


def hello() -> None:
    """Function Main"""
    print("BOT BOT BOT...")
    scheduler.enter(delay=(2), priority=0, action=hello)
    print("BOT Waiting: 2 seconds...")


hello()

scheduler.run(blocking=True)

