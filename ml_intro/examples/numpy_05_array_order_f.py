# Konstrukce jednorozměrného pole konstruktorem numpy.array()
#
# explicitní specifikace uspořádání prvků pole
# (nemá velký význam pro 1D pole=vektory)

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.array(range(10), order="F")

# tisk obsahu pole na standardní výstup
print(a)
