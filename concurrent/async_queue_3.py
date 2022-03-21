import asyncio
import time


async def task(name, queue):
    while not queue.empty():
        param = await queue.get()
        print(f"Task named {name} started with parameter {param}")
        await asyncio.sleep(5)
        print(f"{name} task finished")


async def main():
    queue = asyncio.Queue()

    for i in range(20):
        await queue.put(i)

    await asyncio.gather(
            asyncio.create_task(task(1, queue)),
            asyncio.create_task(task(2, queue)),
            asyncio.create_task(task(3, queue)),
            asyncio.create_task(task(4, queue)))


asyncio.run(main())
