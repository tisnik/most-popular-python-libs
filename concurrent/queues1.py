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
