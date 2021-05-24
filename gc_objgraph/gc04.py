"""Zobrazení počtu referencí na hodnotu True."""

import sys

# nová reference na hodnotu True
x = True

# počet referencí na hodnotu True
print(sys.getrefcount(x))
