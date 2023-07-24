from typing import Callable


def calc(operator: Callable[[int, int], int], x: int, y: int) -> int:
    return operator(x, y)


def add(x: int, y: int) -> int:
    return x + y


def mul(x: int, y: int) -> int:
    return x * y


def less_than(x: int, y: int) -> bool:
    return x < y


z = calc(add, 10, 20)
print(z)

z = calc(mul, 10, 20)
print(z)

z = calc(less_than, 10, 20)
print(z)
