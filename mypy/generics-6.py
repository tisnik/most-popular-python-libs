from typing import Tuple, TypeVar

T = TypeVar('T')


def pair(first: T, second: T) -> Tuple[T, T]:
    x = (first, second)
    return x


reveal_type(pair(1, 2))
reveal_type(pair(0, "B"))
reveal_type(pair("A", 42))
reveal_type(pair("A", "B"))
