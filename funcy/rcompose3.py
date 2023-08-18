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

from funcy import rcompose


def add(x, y):
    return x+y


def double(x):
    return 2*x


def abs(x):
    if x < 0:
        return -x
    return x


composed = rcompose(add, double, abs)

print(composed(2, 3))
print(composed(-2, -3))
