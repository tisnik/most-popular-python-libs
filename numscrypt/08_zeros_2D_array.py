# Knihovna Numpy
#
# Příklady použití konstruktoru numpy.zeros
#
# matice o velikosti 5x5 prvků, každý prvek je typu float

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

# konstrukce pole
a = np.zeros((5, 5))

# tisk obsahu pole na standardní výstup
print(a)
