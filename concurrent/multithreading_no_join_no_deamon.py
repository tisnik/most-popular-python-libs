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


# vytvoření a spuštění trojice vláken
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()

# automaticky se čeká na dokončení vláken
