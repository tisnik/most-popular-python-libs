import curio


async def task(name, a, b):
    try:
        print(f"{name} task started")

        assert isinstance(a, int)
        assert isinstance(b, int)
        result = a * b

        print(f"{name} task finished")
        return result

    except curio.CancelledError:
        print("Timeouting...")
        raise


async def main():
    print("main started")

    task1 = await curio.spawn(task, "1st", 2, "foo")

    try:
        result = await curio.timeout_after(1, task1.join)
        print(result)
    except curio.TaskTimeout as e:
        print("Timeout!")
        await task1.cancel()

    print("done")


curio.run(main())
