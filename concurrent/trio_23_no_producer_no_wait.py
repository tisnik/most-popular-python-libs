import trio


async def consumer(receive_channel):
    while True:
        value = receive_channel.receive_nowait()
        print(f"Consumer: received{value!r}")
        await trio.sleep(1)


async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(0)
        nursery.start_soon(consumer, receive_channel)


trio.run(main)
