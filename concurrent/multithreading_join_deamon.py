#!/usr/bin/env python3

import threading
import time


def worker():
    threadName = threading.current_thread().name
    delay = 1
    n = 10
    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))


# vytvoření a spuštění trojice vláken v režimu daemon
t1 = threading.Thread(target=worker, daemon=True)
t2 = threading.Thread(target=worker, daemon=True)
t3 = threading.Thread(target=worker, daemon=True)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
