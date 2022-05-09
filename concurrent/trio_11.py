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
        for i in range(100):
            nursery.start_soon(task, f"Task {i}", 1, 100)
    print("done")


trio.run(main)
