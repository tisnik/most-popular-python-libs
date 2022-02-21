#!/usr/bin/env python3

"""Multithreading."""

import threading
import time


def worker(threadName, delay, n):
    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))


# vytvoření trojice vláken
t1 = threading.Thread(target=worker, args=("Thread-1", 0.5, 10))
t2 = threading.Thread(target=worker, args=("Thread-2", 1.0, 10))
t3 = threading.Thread(target=worker, args=("Thread-3", 1.5, 10))

# spuštění všech vláken
t1.start()
t2.start()
t3.start()

# čekání na dokončení všech vláken
t1.join()
t2.join()
t3.join()

print("Done!")
