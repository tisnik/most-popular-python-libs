import curio


async def task(name, queue):
    while not queue.empty():
        param = await queue.get()
        print(f"Task named {name} started with parameter {param}")
        await curio.sleep(1)
        print(f"{name} task finished")


async def main():
    print("main started")

    queue = curio.UniversalQueue()

    for i in range(20):
        await queue.put(i)

    task1 = await curio.spawn(task, "1st", queue)
    task2 = await curio.spawn(task, "2nd", queue)
    task3 = await curio.spawn(task, "3rd", queue)
    task4 = await curio.spawn(task, "4th", queue)

    await task1.join()
    await task2.join()
    await task3.join()
    await task4.join()

    print("done")


curio.run(main(), with_monitor=True)
