# - funkci printIsPositive lze předat jinou funkci
# - parametr "condition" nemá zapsán datový typ


def printIsPositive(x: float, condition) -> None:
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
