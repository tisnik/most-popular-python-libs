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
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

# tisk původního pole
print(a)

# přístup k prvkům: řádek/sloupec
print(a[0][2])

# přístup k prvkům: řádek/sloupec
print(a[2][0])
