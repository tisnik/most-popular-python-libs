from typing import TypeVar, Tuple

T = TypeVar('T')


def pair(first: T, second: T) -> Tuple[T, T]:
    x = (first, second)
    return x


p = pair(0, "B")
print(type(p[0]))
print(type(p[1]))
