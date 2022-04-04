import curio


async def task(name, a, b):
    print(f"{name} task started")

    result = a * b
    await curio.sleep(100)

    print(f"{name} task finished")
    return result


async def main():
    print("main started")
    task1 = await curio.spawn(task, "1st", 2, 3)

    try:
        result = await curio.timeout_after(1, task1.join)
        print(result)
    except curio.TaskTimeout as e:
        print("Timeout!")
        await task1.cancel()

    print("done")


curio.run(main())
