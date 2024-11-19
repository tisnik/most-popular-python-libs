#!/usr/bin/env python

"""Vizualizace obsahu matice stupni šedi."""

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
#
# Tento demonstracni priklad je pouzity v serialu o datove analyze
# s vyuzitim programovaciho jazyka Python:
# https://www.root.cz/serialy/datova-analyza-s-vyuzitim-jazyka-python/
#

# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

# import funkce, která vrátí obrázky pro práci
from sklearn.datasets import load_digits

# načtení obrázků, s nimiž budeme dále pracovat
digits_data = load_digits()

# zjištění základních informací o obrázcích
print(digits_data.data.shape)

# vykreslení a uložení prvních deseti obrázků
for i in range(10):
    plt.matshow(digits_data.images[i])
    # převod na stupně šedi
    plt.gray()

    plt.savefig(f"Grayscale image #{i}.png")

    # vykreslení na obrazovku
    plt.show()

# finito
