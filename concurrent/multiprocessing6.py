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

import time


def worker(name, dictionary):
    dictionary[name] = "ok"
    print("hello", name)
    time.sleep(5)
    print("done", name)


def main():
    d = {}

    for name in ("foo", "bar", "baz", "other"):
        worker(name, d)

    print(d)


if __name__ == "__main__":
    print("Running main")
    main()
