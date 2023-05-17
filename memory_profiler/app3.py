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
    l = []
    for i in range(10000000):
        l.append(i)
        if i % 100000 == 0:
            sleep(0.05)

    for i in range(10000000, 0, -1):
        del l[i-1]
        if i % 100000 == 0:
            sleep(0.05)

    sleep(2)


sleep(2)
foo_construct()
sleep(2)
