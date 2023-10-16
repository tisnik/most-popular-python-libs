import asyncio
import time


async def task():
    print("task started")
    await asyncio.sleep(5)
    print("task finished")


def main():
    task1 = asyncio.create_task(task())
    print("task created")

    await task1

    print("done")


main()
