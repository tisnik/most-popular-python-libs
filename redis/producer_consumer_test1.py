import multiprocessing
import time
import redis


PRODUCER_CYCLES = 100
CONSUMER_CYCLES = 100
KEY = "foo"
PRODUCER_SLEEP_TIME = 0.1
CONSUMER_SLEEP_TIME = 0.1


def producer(cycles, key, sleep_time):
    print(f"Running producer: changing {key} {cycles} times with {sleep_time}s pauses")
    redis_client = redis.StrictRedis(
        host="localhost",
        port="6379",
        decode_responses=True,
    )

    for i in range(cycles):
        v = "^"
        redis_client.set(key, v)
        time.sleep(sleep_time)
        v = "^$"
        redis_client.set(key, v)
        time.sleep(sleep_time)


def consumer(cycles, key, sleep_time, result_queue):
    print(f"Running consumer: checking {key} {cycles} times with {sleep_time}s pauses")
    redis_client = redis.StrictRedis(
        host="localhost",
        port="6379",
        decode_responses=True,
    )

    expected_value = "^$"
    errors = 0

    for i in range(cycles):
        value = redis_client.get(key)
        if value != expected_value:
            errors += 1
        time.sleep(sleep_time)
    result_queue.put(errors)


def main():
    queue = multiprocessing.Queue()

    producer_process = multiprocessing.Process(target=producer, args=(PRODUCER_CYCLES, KEY, PRODUCER_SLEEP_TIME))
    consumer_process = multiprocessing.Process(target=consumer, args=(CONSUMER_CYCLES, KEY, CONSUMER_SLEEP_TIME, queue))

    start_time = time.perf_counter()

    # start both consumer and producer
    consumer_process.start()
    producer_process.start()

    print("Waiting for producer and consumer to finish")
    consumer_process.join()
    producer_process.join()

    end_time = time.perf_counter()

    errors = queue.get()

    # compute duration and error frequency
    duration = end_time - start_time
    frequency = errors / duration

    print(f"Errors:   {errors}")
    print(f"Duration: {duration:4.3} seconds")
    print(f"Error frequency: {frequency:4.3} per second")


if __name__ == "__main__":
    print("Running main")
    main()
