"""Grafické zobrazení referencí."""

import objgraph

class A():
    def __init__(self, other):
        self.other = other

# tři objekty, které na sebe navzájem ukazují
x = A(None)
y = A(x)
z = A(y)
x.other=z

# cyklické reference mezi objekty
objgraph.show_refs([x, y, z], filename='objgraph7.png')
