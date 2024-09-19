# Specifikace kroku při provádění řezů - vektory

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.arange(1, 11)

# první řez polem: krok=1
print(a[1:10:1])

# druhý řez polem: krok=2
print(a[1:10:2])

# třetí řez polem: krok=3
print(a[1:10:3])

# čtvrtý řez polem - pouze uvedení kroku
a[::3]
