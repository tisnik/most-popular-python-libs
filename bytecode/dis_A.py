async def producer(send_channel):
    for i in range(1, 10):
        message = f"message {i}"
        print(f"Producer: {message}")
        await send_channel.send(message)


async def consumer(receive_channel):
    async for value in receive_channel:
        print(f"Consumer: received{value!r}")
        await trio.sleep(1)


async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(0)
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)


from dis import dis

print("\nproducer")
dis(producer)

print("\nconsumer")
dis(consumer)

print("\nmain")
dis(main)
