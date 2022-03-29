import curio


async def task(name, n, s):
    print(f"{name} task started")

    for i in range(n):
        print(f"{name} {i+1}/{n}")
        await curio.sleep(s)

    print(f"{name} task finished")


async def main():
    print("main started")
    task1 = await curio.spawn(task, "1st", 10, 1)
    task2 = await curio.spawn(task, "2nd", 10, 1)
    task3 = await curio.spawn(task, "3rd", 10, 1)
    print("done")


curio.run(main())
