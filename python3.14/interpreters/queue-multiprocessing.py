# Multiprocesing a multithreading v Pythonu:
# - spuštění více úloh v nových procesech
# - komunikace mezi procesy s využitím fronty

import time
from multiprocessing import Process, Queue, freeze_support


def worker(name, q):
    """Worker spuštěný několikrát v samostatných procesech."""
    while True:
        # čtení příkazů z fronty
        cmd = q.get()
        print(f"Process '{name}' received command '{cmd}'")
        if cmd == "quit":
            print(f"Process '{name}' is about to quit")
            return
        time.sleep(1)


if __name__ == "__main__":
    print("Starting")
    freeze_support()

    # vytvoření fronty pro komunikaci mezi procesy
    q = Queue()

    # vytvoření tří procesů
    names = ("foo", "bar", "baz")
    ps = [Process(target=worker, args=(name, q)) for name in names]

    # spuštění tří procesů
    for p in ps:
        p.start()

    print("Sending data to other processes")

    # komunikace s procesy přes frontu
    for i in range(10):
        print(f"Sending 'command {i}'")
        q.put("command {}".format(i))

    print("Asking other processes to finish")

    # příkaz pro ukončení procesů
    for i in range(3):
        q.put("quit")

    print("Waiting for other processes")

    # čekání na ukončení procesů
    for p in ps:
        p.join()

    print("All work done!")
