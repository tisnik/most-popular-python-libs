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
        q.task_done()
        print(f"Thread '{name}' received command '{cmd}'")
        if cmd == "quit":
            print(f"Thread '{name}' is about to quit")
            return
        time.sleep(1)


def producer(name, q):
    for job in range(10):
        print(f"{name} thread: Starting producing {job}")
        q.put(job)
        time.sleep(0.3)
        print(f"{name} thread: Produced {job}")


if __name__ == "__main__":
    print("Starting")

    # vytvoření fronty pro komunikaci mezi vlákny
    q = Queue()

    # spuštění čtyř producentů
    names = ("1st", "2nd", "3rd", "4th")
    ps = [Thread(target=producer, daemon=True, name=name, args=[name, q]) for name in names]

    # spuštění producentů
    for p in ps:
        p.start()

    # spuštění tří vláken
    names = ("foo", "bar", "baz")
    ts = [Thread(target=worker, daemon=True, name=name, args=[name, q]) for name in names]

    # spuštění tří vláken
    for t in ts:
        t.start()

    print("Asking other threads to finish")

    # čekání na dokončení producentů
    for p in ps:
        p.join()

    # příkaz pro ukončení vláken
    for i in range(3):
        q.put("quit")

    print("Waiting for other threads")

    # čekání na zpracování všech zpráv ve frontě
    q.join()

    print("All work done!")
