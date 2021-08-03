# Combining Huey and oTree

## Info
This allows to run long-running tasks in the background and communicate the result back to oTree.

## Notes
- mind the updated Procfile! You will have to turn on the second dyno "worker" on heroku!
- For developping, "SqliteHuey" in background/tasks.py is fine. 
- For production use, I suggest to add the redis add-on to heroku and switch to "RedisHuey"
