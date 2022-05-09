import trio


async def task(name, n, s):
    print(f"{name} task started")

    for i in range(n):
        print(f"{name} {i+1}/{n}")
        await trio.sleep(s)

    print(f"{name} task finished")


async def main():
    print("main started")
    async with trio.open_nursery() as nursery:
        print(nursery.start_soon(task, "1st", 10, 1))
        print(nursery.start_soon(task, "2nd", 10, 1))
        print(nursery.start_soon(task, "3rd", 10, 1))
    print("done")


trio.run(main)
