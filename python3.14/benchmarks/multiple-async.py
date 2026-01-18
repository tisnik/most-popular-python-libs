# Multiprocesing a multithreading v Pythonu:
# - spuštění více úloh asynchronně
# - komunikace mezi procesy s využitím fronty

CONCURRENCY_LEVEL = 100
TASKS = 1000
WAIT_FOR_KEY = False
SLEEP_AMOUNT = 0

from asyncio import Queue, sleep, run, gather, create_task
import time


async def worker(name, q):
    """Worker spuštěný několikrát asynchronně."""
    while not q.empty():
        # čtení příkazů z fronty
        cmd = await q.get()
        print(f"Task '{name}' received command '{cmd}'")
        await sleep(SLEEP_AMOUNT)


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

    if WAIT_FOR_KEY:
        input()

    print("All work done!")

    t2 = time.time()

    print(f"Elapsed time: {t2-t1}")

run(main())
