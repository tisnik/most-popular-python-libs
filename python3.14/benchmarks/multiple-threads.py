# Multiprocesing a multithreading v Pythonu:
# - spuštění více úloh v nových vláknech
# - komunikace mezi vlákny s využitím fronty

CONCURRENCY_LEVEL = 100
TASKS = 1000
WAIT_FOR_KEY = False
SLEEP_AMOUNT = 1


from queue import Queue
from threading import Thread
import time


def worker(name, q):
    """Worker spuštěný několikrát v samostatných vláknech."""
    while True:
        # čtení příkazů z fronty
        cmd = q.get()
        print(f"Thread '{name}' received command '{cmd}'")
        if cmd == "quit":
            print(f"Thread '{name}' is about to quit")
            return
        if SLEEP_AMOUNT > 0:
            time.sleep(SLEEP_AMOUNT)


if __name__ == "__main__":
    t1 = time.time()

    print("Starting")

    # vytvoření fronty pro komunikaci mezi vlákny
    q = Queue()

    ts = []
    # vytvoření procesů
    for i in range(CONCURRENCY_LEVEL):
        name = f"Thread #{i}"
        ts.append(Thread(target=worker, daemon=True, name=name, args=[name, q]))

    # spuštění vláken
    for t in ts:
        t.start()

    print("Sending data to other threads")

    # komunikace s vlákny přes frontu
    for i in range(TASKS):
        print(f"Sending 'command {i}'")
        q.put("command {}".format(i))

    if WAIT_FOR_KEY:
        input()

    print("Asking other threads to finish")

    # příkaz pro ukončení vláken
    for i in range(CONCURRENCY_LEVEL):
        q.put("quit")

    print("Waiting for other threads")

    # čekání na zpracování všech zpráv ve frontě
    for t in ts:
        t.join()

    print("All work done!")

    t2 = time.time()

    print(f"Elapsed time: {t2-t1}")
