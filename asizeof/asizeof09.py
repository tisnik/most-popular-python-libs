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

from pympler import asizeof


def print_sizeof(value):
    typename = "{:8}".format(type(value).__name__)
    print(asizeof.asizeof(value, code=True), "\t", typename, "\t", value)


def foo():
    pass


def bar(x, y):
    return x + y


def baz(x=0, y=1):
    print(x)
    print(y)
    return x + y


print_sizeof(print)
print_sizeof(foo)
print_sizeof(bar)
print_sizeof(baz)
