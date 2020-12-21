"""Zobrazení počtu referencí řetězce 'Test!'."""

import sys

# nová reference na řetězec
x = "Test!"

# počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))
