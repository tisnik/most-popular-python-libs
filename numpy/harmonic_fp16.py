"""Investigation of basic properties of float16 floating point numbers."""

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import numpy as np

h1 = np.float16(0)
h2 = np.float16(0)

n = 1

while True:
    h2 = h1 + np.float16(1) / np.float16(n)
    print(h1, h2, h2 - h1, n)
    if h1 == h2:
        break
    h1 = h2
    n += 1
