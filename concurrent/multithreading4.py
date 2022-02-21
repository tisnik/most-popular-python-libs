#!/usr/bin/env python3
 
"""Multithreading."""
 
import threading
import time
 
class X():

    def __init__(self):
        print("X constructed")

    def __del__(self):
        print("X destructed")

 
def worker():
    print("thread started")
    time.sleep(10)
    print("thread finished")
 
 
print("main started")
 
x = X()

# vytvoření a spuštění trojice vláken
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()

print("main finished")
