# Přetypování
#
# konstrukce pole přetypováním jiného pole

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce zdrojového pole
a = numpy.linspace(0, 1, 10)

# přetypování na vektor celých čísel (povšimněte si výsledků)
b = numpy.int32(a)

# tisk typu a obsahu původního pole
print(type(a))
print(a)

# tisk typu a obsahu vytvořeného pole
print(type(b))
print(b)
