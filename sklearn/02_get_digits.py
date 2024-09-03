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
#
# Tento demonstracni priklad je pouzity v serialu o datove analyze
# s vyuzitim programovaciho jazyka Python:
# https://www.root.cz/serialy/datova-analyza-s-vyuzitim-jazyka-python/
#

# import funkce, která vrátí obrázky pro práci
from sklearn.datasets import load_digits

# načtení obrázků, s nimiž budeme dále pracovat
digits_data = load_digits()

# zjištění základních informací o obrázcích
print("Description:", digits_data.DESCR)

print("Data:", digits_data.data.shape)
print("Obrázky:", digits_data.images.shape)

# výpis informací o obrázcích
for i in range(10):
    print(f"Image #{i}:")
    print("Data:\n", digits_data.data[i])
    print("Image:\n", digits_data.images[i])
    print("Target:\n", digits_data.target[i])
    print()

# finito
