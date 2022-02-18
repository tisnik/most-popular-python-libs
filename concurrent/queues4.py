#!/usr/bin/env python3

import time
import threading
import queue


# vytvoření fronty
q = queue.Queue()


# simulace producenta
def producer():
    name = threading.current_thread().name
    for job in range(1000):
        print(f'{name} thread: Starting producing {job}')
        q.put(job)
        time.sleep(0.3)
        print(f'{name} thread: Produced {job}')


# simulace konzumenta
def consumer():
    name = threading.current_thread().name
    while True:
        job = q.get()
        print(f'{name} thread: Starting consuming {job}')
        time.sleep(0.4)
        print(f'{name} thread: Consumed {job}')
        q.task_done()


# spuštění konzumentů
threading.Thread(target=consumer, daemon=True, name="1st").start()
threading.Thread(target=consumer, daemon=True, name="2nd").start()
threading.Thread(target=consumer, daemon=True, name="3rd").start()

# spuštění producentů
threading.Thread(target=producer, daemon=True, name="1st").start()
threading.Thread(target=producer, daemon=True, name="2nd").start()
threading.Thread(target=producer, daemon=True, name="3rd").start()
threading.Thread(target=producer, daemon=True, name="3rd").start()

# čekání na zpracování všech zpráv ve frontě
q.join()
print('Done')
