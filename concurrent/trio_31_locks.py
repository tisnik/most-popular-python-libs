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


num_workers = 10


async def worker(id, lock):
    while True:
        async with lock:
            print(f"Worker #{id}: acquires lock")
            await trio.sleep(1)


async def main():
    async with trio.open_nursery() as nursery:
        lock = trio.Lock()
        for id in range(num_workers):
            nursery.start_soon(worker, id, lock)


trio.run(main)
