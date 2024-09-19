# Výběr řádku pole

# import hlavního balíčku knihovny Numpy
import numpy

# dvourozměrné pole - matice
a = numpy.reshape(numpy.arange(12), (3, 4))

# tisk původního pole
print(a)

# první řádek pole
b = a[0]
print(b)

# druhý řádek pole
b = a[1]
print(b)

# poslední řádek pole
b = a[-1]
print(b)
