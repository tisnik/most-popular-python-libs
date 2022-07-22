"""Přečtení obsahu matice ze standardního binárního souboru."""

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

# použití režimu mmap
m = np.load("matrix3.npy", mmap_mode="r")

# zobrazení dalších informací o matici
print("Dimensions:", m.ndim)
print("Data type:", m.dtype)
print("Item size:", m.itemsize, "bytes")
print("Array size:", m.size, "items")
