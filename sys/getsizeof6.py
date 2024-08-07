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

from sys import getsizeof


def print_sizeof(value):
    typename = f"{type(value).__name__:8}"
    print(getsizeof(value), "\t", typename, "\t", value)


class C4:
    def __init__(self):
        pass

    def foo(self, x):
        self.x = x


o4 = C4()

print_sizeof(C4)
print_sizeof(o4)

o4.foo(o4)

print_sizeof(C4)
print_sizeof(o4)
