# Knihovna Numpy
#
# Příklady použití funkce numpy.array
#
# vytvoření dvourozměrné matice

# import hlavního balíčku knihovny Numpy
if __envir__.executor_name == __envir__.transpiler_name:
    import numscrypt as np

# import pro CPython
__pragma__ ('skip')
import numpy as np
__pragma__ ('noskip')

# konstrukce pole
a = np.array([[1, 2, 3], [4, 5, 6]])

# tisk obsahu pole na standardní výstup
print(a)
