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

from typing import Callable


def get_operator(symbol: str) -> Callable[[int, int], int]:
    operators = {
            "+": add,
            "*": mul,
    }
    return operators[symbol]


def calc(operator: Callable[[int, int], int], x: int, y: int) -> int:
    return operator(x, y)


def add(x: int, y: int) -> int:
    return x + y


def mul(x: int, y: int) -> int:
    return x * y


def less_than(x: int, y: int) -> bool:
    return x < y


z = calc(get_operator("+"), 10, 20)
print(z)

z = calc(get_operator("*"), 10, 20)
print(z)

z = calc(less_than, 10, 20)
print(z)
