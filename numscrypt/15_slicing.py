# Knihovna Numpy
#
# Slicing - vynechání indexu/indexů

# import hlavního balíčku knihovny Numpy
if __envir__.executor_name == __envir__.transpiler_name:
    import numscrypt as np

# import pro CPython
__pragma__ ('skip')
import numpy as np
__pragma__ ('noskip')

# původní pole
a = np.array([1,2,3,4,5,6,7,8,9,10])

# tisk původního pole
print(a)

# slicing
b = a[3:7]

# tisk nového pole
print(b)
