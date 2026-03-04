# Algebraické datové typy v Pythonu
#
# - definice datové třídy
# - konstrukce instance této třídy
# - použití nekorektních parametrů předaných do konstruktoru

from dataclasses import dataclass


@dataclass
class Rectangle:
    width: float
    height: float


rectangle_shape = Rectangle(height=2, width=3)
