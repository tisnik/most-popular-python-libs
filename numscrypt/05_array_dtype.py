# Knihovna Numpy a Numscrypt
#
# Konstrukce jednorozměrného pole konstruktorem numpy.array()
#
# explicitní specifikace typu všech prvků pole
# (interně se provádí přetypování)

#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

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
