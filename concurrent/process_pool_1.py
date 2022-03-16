from concurrent.futures import ProcessPoolExecutor
import time


def worker(processName, delay, n):
    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(processName, counter, n, time.ctime(time.time())))


with ProcessPoolExecutor(max_workers=3) as executor:
    executor.submit(worker, "Process-1", 0.5, 10)
    executor.submit(worker, "Process-2", 1.0, 10)
    executor.submit(worker, "Process-3", 1.5, 10)


print("Done!")
