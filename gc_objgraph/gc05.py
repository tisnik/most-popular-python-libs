"""Reference na seznam."""

import sys

x = []
print(sys.getrefcount(x))
print(sys.getrefcount([]))
