import trio


async def task1():
    dct = {}
    return dct["foo"]


async def task2():
    l = []
    return l[10]


async def task3():
    x = 0
    return 1/x


async def main():
    print("main started")
    async with trio.open_nursery() as nursery:
        nursery.start_soon(task1)
        nursery.start_soon(task2)
        nursery.start_soon(task3)
    print("done")


trio.run(main)
