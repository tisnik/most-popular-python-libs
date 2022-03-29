import curio


async def task():
    print("task started")
    await curio.sleep(5)
    print("task finished")


def main():
    print("main started")
    curio.run(task)
    print("done")


main()
