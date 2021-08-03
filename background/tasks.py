from huey import SqliteHuey, RedisHuey
import time
import os

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
huey = RedisHuey(url=REDIS_URL)

@huey.task()
def add(a, b):
    # make this task longer than it really is
    time.sleep(3)
    return a+b
