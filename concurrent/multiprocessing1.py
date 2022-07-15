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

from multiprocessing import Process


def worker(name):
    print("hello", name)


def main():
    p = Process(target=worker, args=("foo",))
    p.start()
    p.join()


if __name__ == "__main__":
    print("Running main")
    main()
