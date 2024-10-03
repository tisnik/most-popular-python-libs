# - funkce s uvedením typových informací
# - zavolání této funkce pro argumenty typu bool a int
# - (ekvivalence mezi True a 1 i False a 0)


def add(a: int, b: int) -> int:
    """Funkce s typovými anotacemi."""
    return a + b


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add(1, True))
print(add(1, False))
