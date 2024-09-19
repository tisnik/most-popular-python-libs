# Výběr prvků v poli

# import hlavního balíčku knihovny Numpy
import numpy

# dvourozměrná pole - matice
a = numpy.reshape(numpy.arange(12), (3, 4))

# tisk původního pole
print(a)

# přístup k prvkům: řádek/sloupec
print(a[0][2])

# přístup k prvkům: řádek/sloupec
print(a[2][0])
