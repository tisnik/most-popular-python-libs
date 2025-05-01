from math import pi
from dataclasses import dataclass


@dataclass
class Square:
    size: float


@dataclass
class Rectangle:
    width: float
    height: float


@dataclass
class Circle:
    radius: float


Shape = Square | Rectangle | Circle


def area(shape: Shape) -> float:
    """Výpočet plochy geometrického tvaru."""
    match shape:
        case Square(size):
            return size**2
        case Rectangle(width, height):
            return width * height


square_shape = Square(size=10)
square_area = area(square_shape)
print(f"Area of square: {square_area} units")

rectangle_shape = Rectangle(height=2, width=3)
rectangle_area = area(rectangle_shape)
print(f"Area of rectangle: {rectangle_area} units")

circle_shape = Circle(radius=10)
circle_area = area(circle_shape)
print(f"Area of circle: {circle_area} units")
