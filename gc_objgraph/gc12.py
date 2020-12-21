"""Cyklické reference na různé hodnoty."""

import sys
import pprint

x = {}
y = {}

pprint.pprint(x)
pprint.pprint(y)
print(sys.getrefcount(x))
print(sys.getrefcount(y))
print()

x["1"] = y

pprint.pprint(x)
pprint.pprint(y)
print(sys.getrefcount(x))
print(sys.getrefcount(y))
print()

y["2"] = x

pprint.pprint(x)
pprint.pprint(y)
print(sys.getrefcount(x))
print(sys.getrefcount(y))
print()

del x["1"]

pprint.pprint(x)
pprint.pprint(y)
print(sys.getrefcount(x))
print(sys.getrefcount(y))
print()

del y["2"]

pprint.pprint(x)
pprint.pprint(y)
print(sys.getrefcount(x))
print(sys.getrefcount(y))
print()
