# Použití funkce numpy.linspace
#
# zde explicitně specifikujeme, že výsledný vektor má mít deset prvků
# (tím, že se začíná od nuly, získáme krok 0.11111111...)

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.linspace(0, 1, 10)

# tisk obsahu pole na standardní výstup
print(a)
