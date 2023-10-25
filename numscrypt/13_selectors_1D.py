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

# jednorozměrná pole - vektory
a = np.array([1,2,3,4,5,6,7,8,9,10])

# tisk původního pole
print(a)

# indexování prvků od nuly
print(a[0])

# indexování prvků od nuly
print(a[5])

# indexovat lze i od konce pole
print(a[-1])

# indexovat lze i od konce pole
print(a[-5])
