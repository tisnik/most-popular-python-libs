#!/usr/bin/env python

# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

# import funkce, která vrátí obrázky pro práci
from sklearn.datasets import load_digits

# načtení obrázků, s nimiž budeme dále pracovat
digits_data = load_digits()

# vytvoření seznamu, které použijeme 
images = list(zip(digits_data.target, digits_data.images))

# vykreslení tréninkových číslic
for i, (label, image) in enumerate(images[:15]):
	plt.subplot(3, 5, i+1)
	plt.imshow(image, cmap=plt.cm.gray_r) #, interpolation='nearest')
	plt.title(f"číslice {label}")

# uložení a vykreslení výsledku
plt.savefig("training_set.png")
plt.show()

# finito
