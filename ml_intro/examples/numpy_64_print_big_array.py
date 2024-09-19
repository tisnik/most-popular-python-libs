# Tisk velkých polí

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce velkého pole
a = numpy.arange(10000).reshape(100, 100)

# tisk velkého pole
print(a)
