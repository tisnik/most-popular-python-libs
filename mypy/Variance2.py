from typing import List


class Ovoce:
    pass


class Hruska(Ovoce):
    def __repr__(self):
        return "Hruska"


class Jablko(Ovoce):
    def __repr__(self):
        return "Jablko"


def smichej(kosik : List[Ovoce]):
    kosik.append(Hruska())
    kosik.append(Jablko())


kosik : List[Hruska] = []

smichej(kosik)

for ovoce in kosik:
    print(ovoce)
