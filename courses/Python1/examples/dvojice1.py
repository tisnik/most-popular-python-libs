#!/usr/bin/env python


class Dvojice:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Dvojice: {} {}".format(self.x, self.y)


d1 = Dvojice(1, 2)
d2 = Dvojice(3, 4)

print(d1)
print(d2)
