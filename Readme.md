# Combining Huey and oTree

## Info
This allows to run long-running tasks in the background and communicate the result back to oTree.

## Notes
- when the environment variable REDIS_URL is not set, huey is run from an SQLite database. This is fine for developping.
- when REDIS_URL is set, huey will run with redis as the result store

## Heroku
- to run this on heroku, add the "redis" add-on
- also turn on the second dyno for "worker"
- optionally: install the "papertrail" add-on to monitor your log files.
