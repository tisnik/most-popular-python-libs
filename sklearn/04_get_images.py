#!/usr/bin/env python

# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

# import funkce, která vrátí obrázky pro práci
from sklearn.datasets import load_digits

# načtení obrázků, s nimiž budeme dále pracovat
digits_data = load_digits()

# zjištění základních informací o obrázcích
print(digits_data.data.shape)

# vykreslení a uložení prvních deseti obrázků
for i in range(0, 10):
    plt.matshow(digits_data.images[i])
    plt.savefig(f"Image #{i}.png")
    plt.show()

# finito
