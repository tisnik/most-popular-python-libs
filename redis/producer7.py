#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import time

import redis

redis_client = redis.StrictRedis(
    host="localhost",
    port="6379",
    decode_responses=True,
)

key = "bar"
sleep_time = 0.1

error_count = 0

while True:
    pipeline = redis_client.pipeline(transaction=True)
    try:
        print("transaction started...", end="")
        pipeline.watch(key)
        v = redis_client.get(key) or ""
        v += "^"
        pipeline.multi()
        pipeline.set(key, v)
        time.sleep(sleep_time)
        v += "$"
        pipeline.set(key, v)
        pipeline.execute()
        pipeline.unwatch()
        print("...commited")
        time.sleep(sleep_time)
    except redis.WatchError as err:
        error_count += 1
        print(f"Watch error #{error_count}:", err)
print(v)
