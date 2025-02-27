# - návratové typy jsou kovariantní

from typing import Callable


class Ovoce:
    """Třída, která je předkem tříd Hruska i Jablko."""


class Hruska(Ovoce):
    """Potomek třídy Ovoce."""

    def __repr__(self) -> str:
        """Tisk 'hodnoty' objektu."""
        return "Hruska"


class Jablko(Ovoce):
    """Potomek třídy Ovoce."""

    def __repr__(self) -> str:
        """Tisk 'hodnoty' objektu."""
        return "Jablko"


def utrhni(f: Callable[[], Ovoce]) -> Ovoce:
    """Zavolá funkci, která získá jeden kus ovoce a vrátí ho."""
    ovoce = f()
    return ovoce


print(utrhni(Hruska))
print(utrhni(Jablko))
