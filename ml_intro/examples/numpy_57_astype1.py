# Přetypování
#
# konstrukce pole přetypováním jiného pole

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce zdrojového pole
a = numpy.arange(0, 10)

# konverze
b = a.astype(numpy.complex64)

# tisk typu a obsahu původního pole
print(type(a))
print(a.dtype)
print(a)

# tisk typu a obsahu zkonvertovaného pole
print(type(b))
print(b.dtype)
print(b)
