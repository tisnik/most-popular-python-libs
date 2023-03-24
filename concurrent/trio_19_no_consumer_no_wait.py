#
#  (C) Copyright 2022  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import trio


async def producer(send_channel):
    for i in range(1, 1000):
        message = f"message {i}"
        print(f"Producer: {message}")
        send_channel.send_nowait(message)


async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(10)
        nursery.start_soon(producer, send_channel)


trio.run(main)
