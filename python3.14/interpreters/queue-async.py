# Multiprocesing a multithreading v Pythonu:
# - spuštění více úloh asynchronně
# - komunikace mezi procesy s využitím fronty

from asyncio import Queue, sleep, run, gather, create_task


async def worker(name, q):
    """Worker spuštěný několikrát asynchronně."""
    while not q.empty():
        # čtení příkazů z fronty
        cmd = await q.get()
        print(f"Task '{name}' received command '{cmd}'")
        await sleep(1)


async def main():
    print("Starting")

    # vytvoření fronty pro komunikaci mezi úlohami
    queue = Queue()

    print("Sending data to async tasks")

    # komunikace s úlohami přes frontu
    for i in range(10):
        print(f"Sending 'command {i}'")
        await queue.put("command {}".format(i))

    print("Waiting for all tasks")

    await gather(
        create_task(worker("foo", queue)),
        create_task(worker("bar", queue)),
        create_task(worker("baz", queue)),
    )

    print("All work done!")


run(main())
