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

import asyncio
import time


async def task(name, queue):
    while not queue.empty():
        param = await queue.get()
        print(f"Task named {name} started with parameter {param}")
        await asyncio.sleep(5)
        print(f"{name} task finished")


async def main():
    queue = asyncio.Queue()

    for i in range(20):
        await queue.put(i)

    await asyncio.gather(
        asyncio.create_task(task(1, queue)),
        asyncio.create_task(task(2, queue)),
        asyncio.create_task(task(3, queue)),
        asyncio.create_task(task(4, queue)),
    )


asyncio.run(main())
