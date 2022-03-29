import curio


async def task(n, s):
    print("task started")

    for i in range(n):
        print(f"{i+1}/{n}")
        await curio.sleep(s)

    print("task finished")


def main():
    print("main started")
    curio.run(task, 10, 1)
    print("done")


main()
