# Knihovna Numpy a Numscrypt
#
# Konstrukce jednorozměrného pole konstruktorem numpy.array()
#
# vytvoření pole se čtyřmi prvky

# import hlavního balíčku knihovny Numpy
if __envir__.executor_name == __envir__.transpiler_name:
    import numscrypt as np

# import pro CPython
__pragma__ ('skip')
import numpy as np
__pragma__ ('noskip')

# konstrukce pole
a = np.array([1, 2, 3, 4])

# tisk obsahu pole na standardní výstup
print(a)
