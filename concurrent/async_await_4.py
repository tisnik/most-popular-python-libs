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


async def task(name):
    print(f"{name} task started")
    await asyncio.sleep(5)
    print(f"{name} task finished")
    return name[::-1]


async def main():
    task1 = asyncio.create_task(task("first"))
    print("first task created")

    task2 = asyncio.create_task(task("second"))
    print("second task created")

    task3 = asyncio.create_task(task("third"))
    print("third task created")

    print("result of task #1:", await task1)
    print("result of task #2:", await task2)
    print("result of task #3:", await task3)

    print("done")


asyncio.run(main())
