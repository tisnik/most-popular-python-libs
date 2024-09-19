# Výběr prvků pomocí indexů uložených v jiném poli
# dtto ale s dvourozměrným polem

# import hlavního balíčku knihovny Numpy
import numpy

a = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# pro nové pole s prohozenými řádky
b = numpy.array([0, 2, 1])

# tisk pole
print(a[b])
