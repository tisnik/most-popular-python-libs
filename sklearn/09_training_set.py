#!/usr/bin/env python

# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

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
