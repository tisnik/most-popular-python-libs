import trio


num_producers = 5
num_consumers = 20
consumer_timeout = 2
producer_timeout = 2


async def producer(id, send_channel):
    for i in range(1, 10):
        message = f"message {i}"
        print(f"Producer #{id}: {message}")
        with trio.move_on_after(producer_timeout):
            await send_channel.send(message)


async def consumer(id, receive_channel):
    while True:
        print(f"Consumer #{id}: trying to receive message")
        with trio.move_on_after(consumer_timeout):
            value = await receive_channel.receive()
            print(f"Consumer #{id}: received{value!r}")
            await trio.sleep(1)


async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(0)
        for id in range(num_producers):
            nursery.start_soon(producer, id, send_channel)
        for id in range(num_consumers):
            nursery.start_soon(consumer, id, receive_channel)


trio.run(main)
