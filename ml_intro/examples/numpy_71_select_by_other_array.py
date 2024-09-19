# Výběr prvků pomocí indexů uložených v jiném poli
# (kladné indexy)

# import hlavního balíčku knihovny Numpy
import numpy

# jednorozměrná pole - vektory
a = numpy.arange(12)

# tisk původního pole
print(a)

# pole indexů
b = numpy.array([1, 2, 9, 8, 5])

# výběr celým polem
print(a[b])
