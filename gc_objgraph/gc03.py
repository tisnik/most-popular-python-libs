"""Zobrazení počtu referencí na malé celé číslo."""

import sys

# nová reference na malé celé číslo
x = 10

# počet referencí na malé celé číslo
print(sys.getrefcount(x))
