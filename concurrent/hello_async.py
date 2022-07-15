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

import dis
import asyncio


async def say_hello():
    print("Hello world")


async def main():
    t = asyncio.create_task(say_hello())
    await t


asyncio.run(main())

print("say_hello")
dis.dis(say_hello)

print("main")
dis.dis(main)
