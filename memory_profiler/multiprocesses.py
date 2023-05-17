#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from multiprocessing import Process
from time import sleep


def worker(r):
    x = "*foo*"

    y = ""
    for i in range(r):
        y += x

    print(len(y))
    sleep(1)
    del y
    sleep(1)


def main():
    ps = []

    for r in (10000000, 20000000, 30000000, 10000000):
        p = Process(target=worker, args=(r,))
        p.start()
        ps.append(p)
        sleep(0.2)

    for p in ps:
        p.join()

    sleep(2)


if __name__ == "__main__":
    print("Running main")
    main()
