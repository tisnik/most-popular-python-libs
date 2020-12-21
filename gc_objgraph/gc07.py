"""Zobrazení počtu referencí na řetězec."""

import sys

# více referencí na řetězec
x = "Test!"
print(x)

# počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

y = (x, x, x)
print(y)

# počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

z = (y, y)
print(z)

# počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

y = None
z = None

# nový počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))
