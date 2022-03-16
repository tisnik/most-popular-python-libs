from concurrent.futures.thread import ThreadPoolExecutor
import time


def worker(threadName, delay, n):
    result = 0

    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))
        result += delay

    print("{}: DONE!".format(threadName))
    return result


workers = 10

with ThreadPoolExecutor(max_workers=3) as executor:
    results = [executor.submit(worker, "Thread-{}".format(w + 1), 0.5 + w / 10.0, 10) for w in range(workers)]

print("Computing finished")

for result in results:
    print(result.result())

print("Done!")
