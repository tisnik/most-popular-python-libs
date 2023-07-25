from operator import *


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
