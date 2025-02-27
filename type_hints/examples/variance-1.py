# - hierarchie tříd Ovoce <- Hruska a Ovoce <- Jablko
# - funkce `smichej` akceptuje seznam s ovocem
# - přidá do tohoto seznamu Hrusku a Jablko
# - funkci `smichej` voláme s prázdným seznamem pro Ovoce

from typing import List


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


def smichej(kosik: List[Ovoce]) -> None:
    """Do košíku se přidá jedna hruška a jedno jablko."""
    kosik.append(Hruska())
    kosik.append(Jablko())


# košík, který může obsahovat hrušky i jablka
kosik: List[Ovoce] = []

smichej(kosik)

for ovoce in kosik:
    print(ovoce)
