# Multiprocesing a multithreading v Pythonu:
# - spuštění více úloh asynchronně
# - komunikace mezi procesy s využitím fronty

CONCURRENCY_LEVEL = 100
TASKS = 1000
WAIT_FOR_KEY = False


import random
from asyncio import Queue, sleep, run, gather, create_task
import time


def bubble_sort(size):
    a = [random.randrange(0, 10000) for i in range(size)]

    for i in range(size - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


async def worker(name, q):
    """Worker spuštěný několikrát asynchronně."""
    while not q.empty():
        # čtení příkazů z fronty
        cmd = await q.get()
        print(f"Task '{name}' received command '{cmd}'")
        bubble_sort(1000)


async def main():
    t1 = time.time()

    print("Starting")

    # vytvoření fronty pro komunikaci mezi úlohami
    queue = Queue()

    print("Sending data to async tasks")

    # komunikace s úlohami přes frontu
    for i in range(TASKS):
        print(f"Sending 'command {i}'")
        await queue.put("command {}".format(i))

    print("Waiting for all tasks")

    aws = [create_task(worker(f"Task #{i}", queue)) for i in range(CONCURRENCY_LEVEL)]
    await gather(*aws)

    print("All work done!")

    t2 = time.time()

    print(f"Elapsed time: {t2-t1}")

run(main())
