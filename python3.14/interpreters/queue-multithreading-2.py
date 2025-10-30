# Multiprocesing a multithreading v Pythonu:
# - spuštění více úloh v nových vláknech
# - komunikace mezi vlákny s využitím fronty


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
            q.task_done()
            return
        time.sleep(1)
        q.task_done()


if __name__ == "__main__":
    print("Starting")

    # vytvoření fronty pro komunikaci mezi vlákny
    q = Queue()

    # spuštění tří vláken
    names = ("foo", "bar", "baz")
    ts = [Thread(target=worker, daemon=True, name=name, args=[name, q]) for name in names]

    # spuštění tří vláken
    for t in ts:
        t.start()

    print("Sending data to other threads")

    # komunikace s vlákny přes frontu
    for i in range(10):
        print(f"Sending 'command {i}'")
        q.put("command {}".format(i))

    print("Asking other threads to finish")

    # příkaz pro ukončení vláken
    for i in range(3):
        q.put("quit")

    print("Waiting for other threads")

    # čekání na zpracování všech zpráv ve frontě
    q.join()

    print("All work done!")
