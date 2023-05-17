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


@profile
def foo_construct():
    x = "*foo*"

    y = ""
    for i in range(200000):
        y += x

    print(len(y))

    del x
    del y


@profile
def bar_construct():
    x = bytearray(10000000)
    print(len(x))
    del x


foo_construct()
bar_construct()
