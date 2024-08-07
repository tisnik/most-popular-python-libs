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


class C1:
    pass


class C2:
    def __init__(self):
        pass


class C3:
    def __init__(self):
        pass

    def foo(self, x):
        self.x = x

    def bar(self, y):
        self.y = y


o1 = C1()
o2 = C2()
o3 = C3()

print_sizeof(C1)
print_sizeof(o1)

print_sizeof(C2)
print_sizeof(o2)

print_sizeof(C3)
print_sizeof(o3)

o3.foo(42)

print_sizeof(C3)
print_sizeof(o3)

o3.bar(0)

print_sizeof(C3)
print_sizeof(o3)
