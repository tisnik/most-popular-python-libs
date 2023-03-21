#!/usr/bin/env python3

#
#  (C) Copyright 2022  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import time
import threading
import queue


# vytvoření fronty
q = queue.Queue()


# simulace konzumenta
def consumer():
    name = threading.current_thread().name
    while True:
        job = q.get()
        print(f"{name} thread: Starting consuming {job}")
        time.sleep(0.4)
        print(f"{name} thread: Consumed {job}")
        q.task_done()


# spuštění konzumentů
threading.Thread(target=consumer, daemon=True, name="1st").start()
threading.Thread(target=consumer, daemon=True, name="2nd").start()
threading.Thread(target=consumer, daemon=True, name="3rd").start()

# vytvoření úloh v producentovi
for job in range(10):
    print(f"Producing {job}")
    q.put(job)

# čekání na zpracování všech zpráv ve frontě
q.join()
print("Done")
