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

from multiprocessing import Process, Pipe
import time


def worker(name, conn):
    while True:
        cmd = conn.recv()
        print("{} received {}".format(name, cmd))
        if cmd == "quit":
            return
        else:
            conn.send("{} accepted {}".format(name, cmd))
        time.sleep(1)


def main():
    parent_conn, child_conn = Pipe()

    p = Process(target=worker, args=("Worker", child_conn))
    p.start()

    for i in range(10):
        parent_conn.send("command {}".format(i))
        print(parent_conn.recv())

    parent_conn.send("quit")

    p.join()


if __name__ == "__main__":
    main()
