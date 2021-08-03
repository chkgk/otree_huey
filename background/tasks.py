from huey import SqliteHuey
import time

huey = SqliteHuey()

@huey.task()
def add(a, b):
    # make this task longer than it really is
    time.sleep(3)
    return a+b
