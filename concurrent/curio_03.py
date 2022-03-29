import curio


async def task(name, n, s):
    print(f"{name} task started")

    for i in range(n):
        print(f"{name} {i+1}/{n}")
        await curio.sleep(s)

    print(f"{name} task finished")


def main():
    print("main started")
    curio.run(task, "1st", 10, 1)
    curio.run(task, "2nd", 10, 1)
    curio.run(task, "3rd", 10, 1)
    print("done")


main()
