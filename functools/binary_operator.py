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

def calc(operator, x, y):
    return operator(x, y)


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def less_than(x, y):
    return x < y


z = calc(add, 10, 20)
print(z)

z = calc(mul, 10, 20)
print(z)

z = calc(less_than, 10, 20)
print(z)
