import trio


class AsyncContext:
    def __init__(self):
        print("Context: init")

    def __aenter__(self):
        print("Context: aenter")
        return trio.sleep(2)

    def __aexit__(self, type, value, traceback):
        print("Context: aexit", type, value, traceback)
        return self

    def __await__(self):
        print("Context: await")
        return None


async def main():
    print("Before with block")

    async with AsyncContext() as c:
        print("Inside with block")
        print(c)

    print("After with block")


trio.run(main)
