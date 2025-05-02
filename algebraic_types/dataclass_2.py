from dataclasses import dataclass


@dataclass
class Rectangle:
    width: float
    height: float


rectangle_shape = Rectangle(height="foo", width=3)
