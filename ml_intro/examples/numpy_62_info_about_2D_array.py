# Zjištění počtu dimenzí tvaru 2D pole

# import hlavního balíčku knihovny Numpy
import numpy

# dvourozměrné pole
a = numpy.eye(5)

# počet dimenzí vektoru
print(a.ndim)

# tvar vektoru
print(a.shape)

# typ prvků
print(a.dtype.name)

# velikost prvků v bajtech
print(a.itemsize)

# velikost pole (počet prvků)
print(a.size)
