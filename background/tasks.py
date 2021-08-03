from huey import SqliteHuey, RedisHuey
import time

huey = RedisHuey()

@huey.task()
def add(a, b):
    # make this task longer than it really is
    time.sleep(3)
    return a+b
