# Použití funkce numpy.geomspace
#
# zde explicitně specifikujeme, že výsledný vektor má mít šest prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.geomspace(1, 100000, 6)

# tisk obsahu pole na standardní výstup
print(a)
