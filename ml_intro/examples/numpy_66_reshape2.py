# Změna tvaru pole
# zde vlastně dostaneme původní matici

# import hlavního balíčku knihovny Numpy
import numpy

# běžná matice se dvěma řádky a třemi sloupci
a = numpy.array([[1, 2, 3], [4, 5, 6]])

# změna tvaru matice na 3x2 prvky
b = numpy.reshape(a, (2, 3))

# tisk původní matice
print(a)

# tisk nové matice
print(b)
