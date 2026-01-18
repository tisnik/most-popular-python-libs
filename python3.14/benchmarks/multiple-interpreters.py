# Multiprocesing a multithreading v Pythonu:
# - spuštění více úloh v nových interpretrech
# - komunikace mezi interpretry s využitím fronty

CONCURRENCY_LEVEL = 100
TASKS = 1000
WAIT_FOR_KEY = False
SLEEP_AMOUNT = 1


import time
from concurrent import interpreters


def worker(name, q):
    """Worker spuštěný několikrát v samostatných interpretrech."""
    while True:
        # čtení příkazů z fronty
        cmd = q.get()
        print(f"Interpreter '{name}' received command '{cmd}'")
        if cmd == "quit":
            print(f"Interpreter '{name}' is about to quit")
            return
        if SLEEP_AMOUNT > 0:
            time.sleep(SLEEP_AMOUNT)


if __name__ == "__main__":
    t1 = time.time()

    print("Starting")

    # vytvoření fronty pro komunikaci mezi interpretry
    q = interpreters.create_queue()

    ins = []
    # vytvoření interpretrů
    for i in range(CONCURRENCY_LEVEL):
        name = f"Interpreter #{i}"
        ins.append(interpreters.create().call_in_thread(worker, name, q))

    print("Sending data to other interpreters")

    # komunikace s interpretry přes frontu
    for i in range(TASKS):
        print(f"Sending 'command {i}'")
        q.put("command {}".format(i))

    if WAIT_FOR_KEY:
        input()

    print("Asking other interpreters to finish")

    # příkaz pro ukončení procesů
    for i in range(CONCURRENCY_LEVEL):
        q.put("quit")

    print("Waiting for other interpreters")

    # čekání na ukončení interpretrů
    for i in ins:
        i.join()

    print("All work done!")

    t2 = time.time()

    print(f"Elapsed time: {t2-t1}")
