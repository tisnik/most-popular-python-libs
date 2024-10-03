# - funkce s uvedením typových informací
# - použití zobecněného typu Union
# - zavolání této funkce pro různé typy argumenů

from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Funkce s typovými anotacemi."""
    return a + b


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add(1.1, 2))
print(add(1.1, 2.2))
