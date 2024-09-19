# Řezy vícerozměrných polí

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.reshape(numpy.arange(25), (5, 5))

# řez dvojrozměrným polem
print(a[2:4, 3])

# další řez dvojrozměrným polem
print(a[2:4, 3:5])

# třetí řez dvojrozměrným polem
print(a[1:4, 1:4])

# čtvrtý řez dvojrozměrným polem
print(a[-4:-2, -4:-2])
