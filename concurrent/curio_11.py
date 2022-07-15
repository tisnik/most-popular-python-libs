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


async def task(name, a, b):
    print(f"{name} task started")

    result = a * b

    print(f"{name} task finished")
    return result


async def main():
    print("main started")
    task1 = await curio.spawn(task, "1st", 2, 3)
    task2 = await curio.spawn(task, "2nd", 4, 5)
    task3 = await curio.spawn(task, "3rd", 6, 7)

    print(await task1.join())
    print(await task2.join())
    print(await task3.join())

    print("done")


curio.run(main())
