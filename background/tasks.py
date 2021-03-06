from huey import SqliteHuey, RedisHuey
import time
import os

# setup
REDIS_URL = os.environ.get("REDIS_URL", None)
if not REDIS_URL:
    huey = SqliteHuey()
else:
    huey = RedisHuey(url=REDIS_URL)

# Task definitions
@huey.task()
def add(a, b):
    # make this task longer than it really is
    time.sleep(3)
    return a+b
