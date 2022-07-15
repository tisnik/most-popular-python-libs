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


async def task(n, s):
    print("task started")

    for i in range(n):
        print(f"{i+1}/{n}")
        await curio.sleep(s)

    print("task finished")


def main():
    print("main started")
    curio.run(task, 10, 1)
    print("done")


main()
