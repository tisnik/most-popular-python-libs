from dataclasses import dataclass


@dataclass
class Rectangle:
    width: float
    height: float


rectangle_shape = Rectangle(height=2, width=3)
