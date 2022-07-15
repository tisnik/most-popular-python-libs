#!/usr/bin/env python3
# vim: set fileencoding=utf-8

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

import curio


async def producer(id, queue, n):
    for i in range(n):
        message = f"message #{i} from producer {id}"
        await queue.put(message)
        await curio.sleep(0.3)


async def consumer(id, queue):
    print(f"consumer {id} started")
    while True:
        message = await queue.get()
        print(f"consumer {id} received {message}")
        await curio.sleep(0.4)


async def main():
    print("main started")

    queue = curio.Queue()
    async with curio.TaskGroup() as g:
        await g.spawn(producer, 1, queue, 10)
        await g.spawn(producer, 2, queue, 10)
        await g.spawn(producer, 3, queue, 10)
        await g.spawn(consumer, 1, queue)
        await g.spawn(consumer, 2, queue)
        await g.spawn(consumer, 3, queue)

    print("done")


curio.run(main(), with_monitor=True)
