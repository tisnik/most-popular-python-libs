from typing import Tuple


def pair[T, U](first: T, second: U) -> Tuple[T, U]:
    x = (first, second)
    return x


print(pair("A", "B"))
