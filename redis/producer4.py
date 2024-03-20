import time

import redis

redis_client = redis.StrictRedis(
    host="localhost",
    port="6379",
    decode_responses=True,
)

key = "bar"
sleep_time = 0.1

while True:
    v = redis_client.get(key) or ""
    v += "^"
    redis_client.set(key, v)
    # time.sleep(1.4)
    v += "$"
    redis_client.set(key, v)
    time.sleep(sleep_time)
    print(v)
