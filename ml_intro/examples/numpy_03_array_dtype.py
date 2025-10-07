# Konstrukce jednorozměrného pole konstruktorem numpy.array()
#
# explicitní specifikace typu všech prvků pole
# (interně se provádí přetypování)

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.array(range(10), dtype=float)

# tisk obsahu pole na standardní výstup
print(a)
