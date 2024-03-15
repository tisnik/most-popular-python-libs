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
    pipeline = redis_client.pipeline(transaction=True)
    error_count = 0
    v = redis_client.get(key) or ""
    v += "^"
    pipeline.set(key, v)
    time.sleep(sleep_time)
    v += "$"
    pipeline.set(key, v)
    pipeline.execute()
    time.sleep(sleep_time)
    print(v)
