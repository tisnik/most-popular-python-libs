#!/usr/bin/env python

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
