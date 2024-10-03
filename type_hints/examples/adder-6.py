# - funkce s uvedením typových informací
# - zavolání této funkce pro argumenty typu bool a int


def add(a: bool, b: bool) -> bool:
    """Funkce s typovými anotacemi."""
    return a and b


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add(1, True))
print(add(1, False))
print(add(True, False))
