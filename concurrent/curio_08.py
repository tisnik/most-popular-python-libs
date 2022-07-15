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


async def task(name, queue):
    while not queue.empty():
        param = await queue.get()
        print(f"Task named {name} started with parameter {param}")
        await curio.sleep(5)
        print(f"{name} task finished")


async def main():
    print("main started")

    queue = curio.Queue()

    for i in range(20):
        await queue.put(i)

    task1 = await curio.spawn(task, "1st", queue)
    task2 = await curio.spawn(task, "2nd", queue)
    task3 = await curio.spawn(task, "3rd", queue)
    task4 = await curio.spawn(task, "4th", queue)

    await task1.join()
    await task2.join()
    await task3.join()
    await task4.join()

    print("done")


curio.run(main(), with_monitor=True)
