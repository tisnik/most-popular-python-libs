"""Načtení více matic ze standardního binárního souboru."""

import numpy as np

# načtení souboru s větším množstvím matic
npzfile = np.load("matrix.npz")

# tisk názvů souborů
print(npzfile.files)

# přístup k jednotlivým maticím
for f in npzfile.files:
    m = npzfile[f]
    print(m)
