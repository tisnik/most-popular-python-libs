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

key = "foo"
sleep_time = 0.1

while True:
    v = "^"
    redis_client.set(key, v)
    v = "^$"
    redis_client.set(key, v)
    time.sleep(sleep_time)
