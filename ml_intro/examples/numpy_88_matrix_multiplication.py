# Násobení matic
# - Maticový součin

# import hlavního balíčku knihovny Numpy
import numpy

# původní matice
a1 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# původní matice
a2 = numpy.eye(3)

# maticový součin
c = a1 @ a2

# tisk výsledku operace
print(c)
