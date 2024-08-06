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
# https://github.com/tisnik/most-popular-python-libs/blob/master/asizeof/asizeof12.py
#
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/asizeof/asizeof12.html

from pympler import asizeof


def print_sizeof(value):
    typename = "{:8}".format(type(value).__name__)
    print(asizeof.asizeof(value, code=True), "\t", typename)


print_sizeof((1, 2))
print_sizeof((1, "?" * 1000000))
print()

print_sizeof([1, 2])
print_sizeof([1, "?" * 1000000])
print()

print_sizeof({1: 1, 2: 2})
print_sizeof({1: 1, 2: "?" * 1000000})
