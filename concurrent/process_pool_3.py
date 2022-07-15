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

from concurrent.futures import ProcessPoolExecutor
import time


def worker(processName, delay, n):
    result = 0

    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(processName, counter, n, time.ctime(time.time())))
        result += delay

    print("{}: DONE!".format(processName))
    return result


workers = 10

with ProcessPoolExecutor(max_workers=workers) as executor:
    results = [
        executor.submit(worker, "Process-{}".format(w + 1), 0.5 + w / 10.0, 10)
        for w in range(workers)
    ]

print("Computing finished")

for result in results:
    print(result.result())

print("Done!")
