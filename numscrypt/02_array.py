# Knihovna Numpy a Numscrypt
#
# Konstrukce jednorozměrného pole konstruktorem numpy.array()
#
# vytvoření pole se čtyřmi prvky

# import hlavního balíčku knihovny Numpy
if __envir__.executor_name == __envir__.transpiler_name:
    import numscrypt

# import pro CPython
__pragma__ ('skip')
import numpy
__pragma__ ('noskip')

# konstrukce pole
a = numpy.array([1, 2, 3, 4])

# tisk obsahu pole na standardní výstup
print(a)
