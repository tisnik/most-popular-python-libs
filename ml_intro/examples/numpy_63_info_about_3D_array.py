# Zjištění počtu dimenzí tvaru 3D pole

# import hlavního balíčku knihovny Numpy
import numpy

# trojrozměrné pole
a = numpy.ones((3, 4, 5), dtype=int)

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
