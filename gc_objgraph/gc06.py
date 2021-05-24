"""Zobrazení počtu referencí na řetězec."""

import sys

# více referencí na řetězec
x = "Test!"

# počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

# více referencí na řetězec
y = [x, "Test!"]

# nový počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

del y[1]

# nový počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

del y[0]

# nový počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

x = None

# nový počet referencí na řetězec 'Test!'
print(sys.getrefcount("Test!"))
