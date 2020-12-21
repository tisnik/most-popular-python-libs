"""Zobrazení počtu referencí řetězce 'Test!'."""

import sys

# počet referencí na řetězec 'Test!'
print(sys.getrefcount('Test!'))
