# Specifikace kroku při provádění řezů - matice

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.reshape(numpy.arange(0, 25), (5, 5))

# tisk původního pole
print(a)

# řez s uvedením kroku
print(a[0:5:2])
print(a[1::2])
