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
    try:
        print(f"{name} task started")

        result = a * b
        await curio.sleep(100)

        print(f"{name} task finished")
        return result

    except curio.CancelledError:
        print("Timeouting...")
        raise


async def main():
    print("main started")
    task1 = await curio.spawn(task, "1st", 2, 3)

    try:
        result = await curio.timeout_after(1, task1.join)
        print(result)
    except curio.TaskTimeout as e:
        print("Timeout!")
        await task1.cancel()

    print("done")


curio.run(main())
