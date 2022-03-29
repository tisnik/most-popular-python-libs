import curio


async def task(name, n, s):
    print(f"{name} task started")

    for i in range(n):
        print(f"{name} {i+1}/{n}")
        await curio.sleep(s)

    print(f"{name} task finished")


async def main():
    print("main started")
    task1 = await curio.spawn(task, "1st", 10, 5)
    task2 = await curio.spawn(task, "2nd", 10, 5)
    task3 = await curio.spawn(task, "3rd", 10, 5)

    await task1.join()
    await task2.join()
    await task3.join()

    print("done")


curio.run(main(), with_monitor=True)
