# Multiprocesing a multithreading v Pythonu:
# - spuštění více úloh v nových interpretrech
# - komunikace mezi interpretry s využitím fronty

import time
from concurrent import interpreters


def worker(name, q):
    """Worker spuštěný několikrát v samostatných interpretrech."""
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

    # vytvoření fronty pro komunikaci mezi interpretry
    q = interpreters.create_queue()

    # vytvoření tří procesů
    names = ("foo", "bar", "baz")
    ins = [interpreters.create().call_in_thread(worker, name, q) for name in names]

    print("Sending data to other interpreters")

    # komunikace s interpretry přes frontu
    for i in range(10):
        print(f"Sending 'command {i}'")
        q.put("command {}".format(i))

    print("Asking other interpreters to finish")

    # příkaz pro ukončení procesů
    for i in range(3):
        q.put("quit")

    print("Waiting for other interpreters")

    # čekání na ukončení interpretrů
    for i in ins:
        i.join()

    print("All work done!")
