#!/usr/bin/env python3

import time
import threading
import queue


# vytvoření fronty
q = queue.Queue()


# simulace konzumenta
def consumer():
    while True:
        job = q.get()
        print(f"Starting consuming {job}")
        time.sleep(0.4)
        print(f"Consumed {job}")
        q.task_done()


# spuštění konzumenta
threading.Thread(target=consumer, daemon=True, name="první").start()

# vytvoření úloh v producentovi
for job in range(10):
    print(f"Producing {job}")
    q.put(job)

# čekání na zpracování všech zpráv ve frontě
q.join()
print("Done")
