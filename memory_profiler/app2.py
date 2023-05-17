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

from time import sleep


def foo_construct():
    x = "*foo*"

    sleep(2)

    y = ""
    for i in range(20000000):
        y += x

    print(len(y))


def bar_construct():
    x = bytearray(100000000)
    print(len(x))
    sleep(2)


sleep(2)
foo_construct()
sleep(2)
bar_construct()
sleep(2)
