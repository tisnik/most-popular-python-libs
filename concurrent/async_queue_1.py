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

    for n in range(1, 2):
        asyncio.create_task(task(f"{n}", queue))


asyncio.run(main())
