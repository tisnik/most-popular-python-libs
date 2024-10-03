# - funkce s uvedením typových informací
# - použití zobecněného typu Union
# - úprava pro Python 3.10 a vyšší
# - zavolání této funkce pro různé typy argumentů


def add(a: int | float, b: int | float) -> int | float:
    """Funkce s typovými anotacemi."""
    return a + b


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add(1.1, 2))
print(add(1.1, 2.2))
