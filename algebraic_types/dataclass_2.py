# Algebraické datové typy v Pythonu
#
# - definice datové třídy
# - konstrukce instance této třídy
# - použití nekorektního parametru předaného do konstruktoru

from dataclasses import dataclass


@dataclass
class Rectangle:
    width: float
    height: float


rectangle_shape = Rectangle(height="foo", width=3)
