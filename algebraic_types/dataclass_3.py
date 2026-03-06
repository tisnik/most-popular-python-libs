# Algebraické datové typy v Pythonu
#
# - definice datové třídy
# - konstrukce instance této třídy
# - volání konstruktoru bez parametrů (nekorektní)

from dataclasses import dataclass


@dataclass
class Rectangle:
    width: float
    height: float


rectangle_shape = Rectangle()
