"""Zobrazení počtu referencí na řetězec."""

import sys

# více referencí na řetězec
x = "Test!"
y = x
z = y

print(sys.getrefcount("foo"))
print(sys.getrefcount("Test!"))
print(sys.getrefcount(x))
print(sys.getrefcount(y))
print(sys.getrefcount(z))
