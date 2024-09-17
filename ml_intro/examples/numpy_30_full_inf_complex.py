# Příklady použití konstruktoru numpy.full
#
# matice s rozměry 3x4x5 prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.full((3, 4, 5), numpy.inf, dtype=numpy.complex)

# tisk obsahu pole na standardní výstup
print(a)
