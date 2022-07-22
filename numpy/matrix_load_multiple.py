"""Načtení více matic ze standardního binárního souboru."""

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

# načtení souboru s větším množstvím matic
npzfile = np.load("matrix.npz")

# tisk názvů souborů
print(npzfile.files)

# přístup k jednotlivým maticím
for f in npzfile.files:
    m = npzfile[f]
    print(m)
