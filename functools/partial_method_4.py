from functools import partialmethod


class Point:
    def __init__(self):
        self._x = 0
        self._y = 0

    def move_to(self, x, y):
        self._x = x
        self._y = y

    to_origin = partialmethod(move_to, 0, 0)

    def __str__(self):
        return f"Point[{self._x}, {self._y}]"


point = Point()
print(point)

point.move_to(1, 2)
print(point)

point.to_origin()
print(point)
