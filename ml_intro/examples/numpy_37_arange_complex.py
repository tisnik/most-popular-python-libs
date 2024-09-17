# Funkce numpy.arange
#
# nemusíme zůstat pouze u celých čísel, protože pracovat je možné i s hodnotami
# typu float a complex

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole - pozor na krok v reálné složce
a = numpy.arange(0 + 0j, 10 + 10j, 0 + 2j)

# tisk obsahu pole na standardní výstup
print(a)
