# Podíl prvek po prvku

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.reshape(numpy.arange(25), (5, 5))

# provedení operace
b = a % 2

# tisk původního pole
print(a)

# tisk nového pole
print(b)
