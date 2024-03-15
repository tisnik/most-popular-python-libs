import redis
import time


redis_client = redis.StrictRedis(
    host="localhost",
    port="6379",
    decode_responses=True,
)

key = "bar"
expected_value = "^$"
sleep_time = 0.01

start_time = time.perf_counter()

errors = 0

while True:
    value = redis_client.get(key)
    if value == "that's me":
        continue
    last_chars = value[-2:]
    if last_chars != expected_value:
        errors += 1
        now = time.perf_counter()
        duration = now - start_time
        frequency = errors / duration
        print(f"{last_chars:3} {errors:3}  {duration:6.3}  {frequency:4.3}")
    time.sleep(sleep_time)
