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
#
# link to source:
# https://github.com/tisnik/most-popular-python-libs/blob/master/asizeof/asizeof10.py
# 
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/asizeof/asizeof10.html

from pympler import asizeof


def print_sizeof(value):
    typename = "{:8}".format(type(value).__name__)
    print(asizeof.asizeof(value, code=True), "\t", typename, "\t", value)


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
