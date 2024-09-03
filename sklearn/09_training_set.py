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

# budeme provádět vykreslování de facto standardní knihovnou Matplotlib

# import funkce, která vrátí obrázky pro práci
from sklearn.datasets import load_digits

# načtení obrázků, s nimiž budeme dále pracovat
digits_data = load_digits()

# celkový počet vzorků
samples = len(digits_data.images)
print("Vzorků celkem:", samples)

# počet vzorků pro trénink
for_training = samples // 2
print("Vzorků pro trénink:", for_training)

# obrázky (ve formě vektoru) a jejich označení
training_images = digits_data.data[:for_training]
training_labels = digits_data.target[:for_training]

# finito
