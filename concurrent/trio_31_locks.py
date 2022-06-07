import trio


num_workers = 10


async def worker(id, lock):
    while True:
        async with lock:
            print(f"Worker #{id}: acquires lock")
            await trio.sleep(1)


async def main():
    async with trio.open_nursery() as nursery:
        lock = trio.Lock()
        for id in range(num_workers):
            nursery.start_soon(worker, id, lock)


trio.run(main)
