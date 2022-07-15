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
    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(processName, counter, n, time.ctime(time.time())))


with ProcessPoolExecutor(max_workers=3) as executor:
    executor.submit(worker, "Process-1", 0.5, 10)
    executor.submit(worker, "Process-2", 1.0, 10)
    executor.submit(worker, "Process-3", 1.5, 10)


print("Done!")
