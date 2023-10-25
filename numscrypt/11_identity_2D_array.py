# Knihovna Numpy
#
# Příklady použití konstruktoru numpy.ones
#
# matice se třemi řádky a čtyřmi sloupci

# import hlavního balíčku knihovny Numpy
if __envir__.executor_name == __envir__.transpiler_name:
    import numscrypt as np

# import pro CPython
__pragma__ ('skip')
import numpy as np
__pragma__ ('noskip')

# konstrukce pole
a = np.identity(10)

# tisk obsahu pole na standardní výstup
print(a)
