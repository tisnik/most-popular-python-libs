# Zjištění počtu dimenzí tvaru 1D pole

# import hlavního balíčku knihovny Numpy
import numpy

# jednorozměrný vektor
a = numpy.array([1, 2, 3])

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
