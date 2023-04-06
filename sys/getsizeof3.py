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
    typename = "{:8}".format(type(value).__name__)
    print(getsizeof(value), "\t", typename, "\t", value)


print_sizeof(())
print_sizeof((1,))
print_sizeof((1, 2))
print_sizeof((1, 2, 3))
print_sizeof((1, 2, 3, 4))
print_sizeof((1, 2, 3, 4, 5))
print_sizeof((1, 2, 3, 4, 5, 6))
print()

print_sizeof([])
print_sizeof([1])
print_sizeof([1, 2])
print_sizeof([1, 2, 3])
print_sizeof([1, 2, 3, 4])
print_sizeof([1, 2, 3, 4, 5])
print_sizeof([1, 2, 3, 4, 5, 6])
print()

print_sizeof({})
print_sizeof({1: 1})
print_sizeof({1: 1, 2: 2})
print_sizeof({1: 1, 2: 2, 3: 3})
print_sizeof({1: 1, 2: 2, 3: 3, 4: 4})
print_sizeof({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})
print_sizeof({1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6})
