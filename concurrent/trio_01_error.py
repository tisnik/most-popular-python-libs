import trio


async def task():
    print("task started")
    trio.sleep(5)
    print("task finished")


def main():
    print("main started")
    trio.run(task)
    print("done")


main()
