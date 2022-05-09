import trio


async def task(name, n, s):
    print(f"{name} task started")

    for i in range(n):
        print(f"{name} {i+1}/{n}")
        await trio.sleep(s)

    print(f"{name} task finished")


def main():
    print("main started")
    trio.run(task, "1st", 10, 1)
    trio.run(task, "2nd", 10, 1)
    trio.run(task, "3rd", 10, 1)
    print("done")


main()
