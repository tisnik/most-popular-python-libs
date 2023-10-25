# Knihovna Numpy
#
# Výběr prvků v poli

# import hlavního balíčku knihovny Numpy
if __envir__.executor_name == __envir__.transpiler_name:
    import numscrypt as np

# import pro CPython
__pragma__ ('skip')
import numpy as np
__pragma__ ('noskip')

# dvourozměrná pole - matice
a = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10],[11,12,13,14]])

b = np.identity(4)

# tisk původního pole
print(a)

# tisk původního pole
print(b)

# operace nad celou maticí
__pragma__ ('opov')
c = a + b
__pragma__ ('noopov')

print(c)
