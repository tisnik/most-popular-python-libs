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


async def task(name, n, s):
    print(f"{name} task started")

    for i in range(n):
        print(f"{name} {i+1}/{n}")
        await trio.sleep(s)

    print(f"{name} task finished")


async def main():
    print("main started")

    async with trio.open_nursery() as nursery:
        nursery.start_soon(task, "1st", 10, 1)

    async with trio.open_nursery() as nursery:
        nursery.start_soon(task, "2nd", 10, 1)

    async with trio.open_nursery() as nursery:
        nursery.start_soon(task, "3rd", 10, 1)

    print("done")


trio.run(main)
