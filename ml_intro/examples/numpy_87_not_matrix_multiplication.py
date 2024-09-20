# Násobení matic
# - Operátor @, nikoli *

# import hlavního balíčku knihovny Numpy
import numpy

# původní matice
a1 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# původní matice
a2 = numpy.eye(3)

# - Násobení prvek po prvku
c = a1 * a2

# tisk výsledku operace
print(c)
