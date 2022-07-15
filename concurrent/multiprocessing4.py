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

from multiprocessing import Process, Queue
import time


def worker(name, q):
    while True:
        cmd = q.get()
        print(name, cmd)
        if cmd == "quit":
            print("Quitting")
            return
        time.sleep(1)


def main():
    q = Queue()

    ps = [Process(target=worker, args=(name, q)) for name in ("foo", "bar", "baz")]

    for p in ps:
        p.start()

    for i in range(10):
        q.put("command {}".format(i))

    for i in range(3):
        q.put("quit")

    for p in ps:
        p.join()


if __name__ == "__main__":
    print("Running main")
    main()
