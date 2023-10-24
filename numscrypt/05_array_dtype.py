# Knihovna Numpy a Numscrypt
#
# Konstrukce jednorozměrného pole konstruktorem numpy.array()
#
# explicitní specifikace typu všech prvků pole
# (interně se provádí přetypování)

# import hlavního balíčku knihovny Numpy
if __envir__.executor_name == __envir__.transpiler_name:
    import numscrypt as np

# import pro CPython
__pragma__ ('skip')
import numpy as np
__pragma__ ('noskip')

def construct_array():
    # konstrukce pole
    a = np.array(range(10), dtype=np.float)

    # tisk obsahu pole na webovou stránku
    document.getElementById("output").innerHTML = str(a)


construct_array()
