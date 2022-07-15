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

import trio


class AsyncContext:
    def __init__(self):
        print("Context: init")

    def __aenter__(self):
        print("Context: aenter")
        return trio.sleep(2)

    def __aexit__(self, type, value, traceback):
        print("Context: aexit", type, value, traceback)
        return self

    def __await__(self):
        print("Context: await")
        return None


async def main():
    print("Before with block")

    async with AsyncContext() as c:
        print("Inside with block")
        print(c)

    print("After with block")


trio.run(main)
