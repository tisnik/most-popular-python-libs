"""Grafické zobrazení referencí."""

import objgraph


class A():
    """An object with one attribute containing reference to some (other) object."""

    def __init__(self, other):
        """Constructor."""
        self.other = other


# tři objekty, které na sebe navzájem ukazují
x = A(None)
y = A(x)
z = A(y)
x.other = z

# zobrazení cyklické reference mezi objekty
objgraph.show_refs([x, y, z], filename='objgraph7.png')
