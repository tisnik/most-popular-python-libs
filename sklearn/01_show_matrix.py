#!/usr/bin/env python

# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

import numpy as np

# vytvoření matice, kterou budeme vizualizovat
array = np.random.rand(10, 10)

# vykreslení
plt.matshow(array)

# uložení vizualizované matice
plt.savefig("random.png")

# vizualizace na obrazovku
plt.show()

# finito
