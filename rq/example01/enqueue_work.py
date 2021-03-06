# vim: set fileencoding=utf-8

# This script is used and described in the following article:
# https://www.root.cz/clanky/pouziti-nastroje-rq-redis-queue-pro-spravu-uloh-zpracovavanych-na-pozadi/

from redis import Redis
from rq import Queue

from worker import do_work


q = Queue(connection=Redis())

result = q.enqueue(do_work)
print(result)
