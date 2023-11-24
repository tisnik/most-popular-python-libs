#!/usr/bin/env python

# import funkce, která vrátí obrázky pro práci
from sklearn.datasets import load_digits

# načtení obrázků, s nimiž budeme dále pracovat
digits_data = load_digits()

# zjištění základních informací o obrázcích
print("Description:", digits_data.DESCR)

print("Data:", digits_data.data.shape)
print("Obrázky:", digits_data.images.shape)

# výpis informací o obrázcích
for i in range(0, 10):
    print(f"Image #{i}:")
    print("Data:\n", digits_data.data[i])
    print("Image:\n", digits_data.images[i])
    print("Target:\n", digits_data.target[i])
    print()

# finito
