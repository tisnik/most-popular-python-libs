"""Zobrazení počtu referencí na řetězec."""

import sys


def foo(ref):
    print(sys.getrefcount(ref))


# reference na řetězec
x = "Test!"
print(sys.getrefcount(x))

# předání reference
foo(x)
