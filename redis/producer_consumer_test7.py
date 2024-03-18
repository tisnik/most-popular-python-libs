import multiprocessing
import time
import redis


PRODUCER_CYCLES = 100
CONSUMER_CYCLES = 200
KEY = "foo"
PRODUCER_SLEEP_TIME = 0.1
CONSUMER_SLEEP_TIME = 0.1


def producer_1(cycles, key, sleep_time):
    print(f"Running producer: changing {key} {cycles} times with {sleep_time}s pauses")
    redis_client = redis.StrictRedis(
        host="localhost",
        port="6379",
        decode_responses=True,
    )

    error_count = 0

    for i in range(cycles):
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


def producer_2(cycles, key, sleep_time):
    redis_client = redis.StrictRedis(
        host="localhost",
        port="6379",
        decode_responses=True,
    )

    for i in range(cycles):
        redis_client.set(key, "that's me")
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
        if value == "that's me":
            continue
        last_chars = value[-2:]
        if last_chars != expected_value:
            errors += 1
        time.sleep(sleep_time)
    result_queue.put(errors)


def main():
    queue = multiprocessing.Queue()

    producer_1_process = multiprocessing.Process(target=producer_1, args=(PRODUCER_CYCLES, KEY, PRODUCER_SLEEP_TIME))
    producer_2_process = multiprocessing.Process(target=producer_2, args=(PRODUCER_CYCLES, KEY, PRODUCER_SLEEP_TIME*2))
    consumer_process = multiprocessing.Process(target=consumer, args=(CONSUMER_CYCLES, KEY, CONSUMER_SLEEP_TIME, queue))

    start_time = time.perf_counter()

    # start both consumer and producer
    consumer_process.start()
    producer_1_process.start()
    producer_2_process.start()

    print("Waiting for producer and consumer to finish")
    consumer_process.join()
    producer_1_process.join()
    producer_2_process.join()

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
