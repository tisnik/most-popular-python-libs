import trio


async def producer(send_channel):
    for i in range(1, 1000):
        message = f"message {i}"
        print(f"Producer: {message}")
        await send_channel.send(message)


async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(10)
        nursery.start_soon(producer, send_channel)


trio.run(main)
