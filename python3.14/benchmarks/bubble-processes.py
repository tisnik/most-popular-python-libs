# Multiprocesing a multithreading v Pythonu:
# - spuštění více úloh v nových procesech
# - komunikace mezi procesy s využitím fronty

CONCURRENCY_LEVEL = 100
TASKS = 1000
WAIT_FOR_KEY = False
SLEEP_AMOUNT = 1


import random
import time
from multiprocessing import Process, Queue, freeze_support


def bubble_sort(size):
    a = [random.randrange(0, 10000) for i in range(size)]

    for i in range(size - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def worker(name, q):
    """Worker spuštěný několikrát v samostatných procesech."""
    while True:
        # čtení příkazů z fronty
        cmd = q.get()
        print(f"Process '{name}' received command '{cmd}'")
        if cmd == "quit":
            print(f"Process '{name}' is about to quit")
            return
        bubble_sort(1000)


if __name__ == "__main__":
    t1 = time.time()

    print("Starting")
    freeze_support()

    # vytvoření fronty pro komunikaci mezi procesy
    q = Queue()

    ps = []
    # vytvoření procesů
    for i in range(CONCURRENCY_LEVEL):
        name = f"Process #{i}"
        ps.append(Process(target=worker, args=(name, q)))

    # spuštění procesů
    for p in ps:
        p.start()

    print("Sending data to other processes")

    # komunikace s procesy přes frontu
    for i in range(TASKS):
        print(f"Sending 'command {i}'")
        q.put("command {}".format(i))

    if WAIT_FOR_KEY:
        input()

    print("Asking other processes to finish")

    # příkaz pro ukončení procesů
    for i in range(CONCURRENCY_LEVEL):
        q.put("quit")

    print("Waiting for other processes")

    # čekání na ukončení procesů
    for p in ps:
        p.join()

    print("All work done!")

    t2 = time.time()

    print(f"Elapsed time: {t2-t1}")
