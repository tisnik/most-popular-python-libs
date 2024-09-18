# Příklady použití konstruktoru numpy.matrix
#
# matice s rozměry 2x2 prvky

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce matice
a = numpy.matrix("1 2; 3 4")

# vytvoření pole z matice
b = numpy.array(a)

# tisk obsahu matice na standardní výstup
print(type(a))
print(a)

# tisk obsahu pole na standardní výstup
print(type(b))
print(b)
