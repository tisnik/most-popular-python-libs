"""Reference na různé hodnoty."""

import sys

x = "foobar"
y = 0
z = True
w = None
lst = []

print(sys.getrefcount("foo"))
print(sys.getrefcount("foobar"))

print(sys.getrefcount(x))
print(sys.getrefcount(y))
print(sys.getrefcount(z))
print(sys.getrefcount(w))
print(sys.getrefcount(lst))
print(sys.getrefcount([]))
