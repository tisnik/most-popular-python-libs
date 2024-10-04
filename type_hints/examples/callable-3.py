# - funkci printIsPositive lze předat jinou funkci
# - parametr "condition" má zapsán datový typ
# - testování typu variance

from typing import Callable


def printIsPositive(x: float, condition: Callable[[float], bool]) -> None:
    if condition(x):
        print("Positive")
    else:
        print("Negative")


def positiveFloat(x: float) -> bool:
    return x > 0.0


def positiveInt(x: int) -> bool:
    return x > 0


printIsPositive(4, positiveFloat)
printIsPositive(-0.5, positiveFloat)
printIsPositive(1, positiveInt)
printIsPositive(1, positiveInt)
