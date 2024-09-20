# Operátory
# pole op pole

# import hlavního balíčku knihovny Numpy
import numpy

# první pole
a1 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# druhé pole
a2 = numpy.eye(3)

# součet prvek po prvku
c = a1 + a2

# tisk nového pole
print(c)
