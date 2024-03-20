import time

import redis

redis_client = redis.StrictRedis(
    host="localhost",
    port="6379",
    decode_responses=True,
)

key = "bar"
sleep_time = 0.18

while True:
    redis_client.set(key, "that's me")
    time.sleep(sleep_time)
