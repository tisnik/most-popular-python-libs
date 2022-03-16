from concurrent.futures.thread import ThreadPoolExecutor
import time


def worker(threadName, delay, n):
    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))


with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(worker, "Thread-1", 0.5, 10)
    executor.submit(worker, "Thread-2", 1.0, 10)
    executor.submit(worker, "Thread-3", 1.5, 10)


print("Done!")
