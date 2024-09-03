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

# celkový počet vzorků
samples = len(digits_data.images)
print("Vzorků celkem:", samples)

# vytvoření seznamu, které použijeme
images = list(zip(digits_data.target, digits_data.images))

# počet vzorků pro trénink
for_training = samples // 2
print("Vzorků pro trénink:", for_training)

# obrázky (ve formě vektoru) a jejich označení
training_images = digits_data.data[:for_training]
training_labels = digits_data.target[:for_training]

# provést klasifikaci
from sklearn import svm

classify = svm.SVC(gamma=0.001)
classify.fit(training_images, training_labels)

# očekávané výsledky vs. výsledky modelu
expexted_labels = digits_data.target[for_training:]
predicted_labels = classify.predict(digits_data.data[for_training:])

# jak je náš model úspěšný?
total = 0
same = 0

for (expected, predicted) in zip(expexted_labels, predicted_labels):
    print(expected, predicted)
    if expected==predicted:
        same+=1
    total+=1

print("Total:", total)
print("Same:", same)
print("Precision:", 100.0*same/total)

# finito
