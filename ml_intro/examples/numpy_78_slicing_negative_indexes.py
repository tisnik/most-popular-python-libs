# Řezy a záporné indexy

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.arange(12)

# provedení prvního řezu polem
print(a[-6:-4])

# provedení druhého řezu polem
print(a[-6:])

# provedení třetího řezu polem
print(a[:-4])
