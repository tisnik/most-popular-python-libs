# - hierarchie tříd Ovoce <- Hruska a Ovoce <- Jablko
# - funkce `tiskni` akceptuje neměnitelnou sekvenci s ovocem
# - samotný seznam se přitom ve funkci nemění (jen se čte)
# - funkci `tiskni` voláme s prázdným seznamem pro Hrušky
# - tisk anotace funkce `tiskni`

from typing import Sequence


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


def tiskni(kosik: Sequence[Ovoce]) -> None:
    """Vytiskne obsah košíku s ovocem."""
    for ovoce in kosik:
        print(ovoce)


# košík, který může obsahovat pouze hrušky
kosik: Sequence[Hruska] = []

tiskni(kosik)

# tisk anotace funkce `tiskni`
print(tiskni.__annotations__)
