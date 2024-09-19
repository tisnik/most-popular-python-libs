# Změna tvaru pole - vytvoření matice s jediným sloupcem

# import hlavního balíčku knihovny Numpy
import numpy

# běžná matice se dvěma řádky a třemi sloupci
a = numpy.array([[1, 2, 3], [4, 5, 6]])

# změna tvaru matice na jediný sloupec
b = numpy.reshape(a, (6, 1))

# tisk původní matice
print(a)

# tisk nové matice
print(b)
