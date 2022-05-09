import trio


async def task(name, n, s):
    print(f"{name} task started")

    for i in range(n):
        print(f"{name} {i+1}/{n}")
        await trio.sleep(s)

    raise Exception(name)
    print(f"{name} task finished")


async def main():
    print("main started")
    try:
        async with trio.open_nursery() as nursery:
            nursery.start_soon(task, "1st", 10, 0.3)
            nursery.start_soon(task, "2nd", 10, 0.3)
            nursery.start_soon(task, "3rd", 10, 0.3)
    except Exception as e:
        print("Caught", e)
    print("done")


trio.run(main)
