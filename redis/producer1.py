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
    time.sleep(sleep_time)
    v = "^$"
    redis_client.set(key, v)
    time.sleep(sleep_time)
