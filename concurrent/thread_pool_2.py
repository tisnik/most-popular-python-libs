from concurrent.futures.thread import ThreadPoolExecutor
import time


def worker(threadName, delay, n):
    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))
    print("{}: DONE!".format(threadName))


workers = 10

with ThreadPoolExecutor(max_workers=workers) as executor:
    for w in range(workers):
        executor.submit(worker, "Thread-{}".format(w + 1), 0.5 + w / 10.0, 10)


print("Done!")
