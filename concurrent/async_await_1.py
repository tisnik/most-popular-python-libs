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


async def task():
    print("task started")
    await asyncio.sleep(5)
    print("task finished")


def main():
    task1 = asyncio.create_task(task())
    print("task created")

    await task1

    print("done")


main()
