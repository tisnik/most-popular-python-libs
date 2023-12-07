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

# knihovnu Pandas využijeme pro načtení datového rámce
import pandas as pd

df = pd.read_csv("particles.csv")

# vykreslení bodů v rovině
plt.scatter(df["x"], df["y"], s=1)

# uložení grafu do souboru
plt.savefig("particles.png")

# vykreslení na obrazovku
plt.show()
