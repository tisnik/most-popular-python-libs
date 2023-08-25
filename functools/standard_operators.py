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

from operator import add, mul, pow, lt, gt


def get_operator(symbol):
    operators = {
            "+": add,
            "*": mul,
            "^": pow,
            "<": lt,
            ">": gt,
    }
    return operators[symbol]


def calc(operator, x, y):
    return operator(x, y)


z = calc(get_operator("+"), 10, 20)
print(z)

z = calc(get_operator("*"), 10, 20)
print(z)

z = calc(get_operator("^"), 10, 20)
print(z)

z = calc(get_operator("<"), 10, 20)
print(z)

z = calc(get_operator(">"), 10, 20)
print(z)
