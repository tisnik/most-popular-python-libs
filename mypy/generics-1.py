from typing import Tuple


def pair[T](first: T, second: T) -> Tuple[T, T]:
    x = (first, second)
    return x


print(pair("A", "B"))
