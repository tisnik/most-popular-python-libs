from math import pi


class Square:
    def __init__(self, size):
        self.size = size


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


def area(shape):
    """Výpočet plochy geometrického tvaru."""
    match shape:
        case Square(size=size):
            return size**2
        case Rectangle(width=width, height=height):
            return width * height
        case Circle(radius=radius):
            return pi * radius**2
        case _:
            raise TypeError(f"Unknown type '{type(shape).__name__}'")


square_shape = Square(10)
square_area = area(square_shape)
print(f"Area of square: {square_area} units")

rectangle_shape = Rectangle(2, 3)
rectangle_area = area(rectangle_shape)
print(f"Area of rectangle: {rectangle_area} units")

circle_shape = Circle(10)
circle_area = area(circle_shape)
print(f"Area of circle: {circle_area} units")
