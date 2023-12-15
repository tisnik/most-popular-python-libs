from typing import TypeVar, Tuple

T = TypeVar('T')


def pair(first: T, second: T) -> Tuple[T, T]:
    x = (first, second)
    return x


print(pair("A", 42))
