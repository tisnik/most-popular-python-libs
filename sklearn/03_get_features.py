#!/usr/bin/env python

# import funkce, která vrátí obrázky pro práci
from sklearn.datasets import load_digits

# načtení obrázků, s nimiž budeme dále pracovat
digits_data = load_digits()

# zjištění základních informací o obrázcích
print("Description:", digits_data.DESCR)

print("Data:", digits_data.data.shape)
print("Obrázky:", digits_data.images.shape)

print("Feature names")
for feature_name in digits_data.feature_names:
    print(feature_name)

print()

print("Target names")
for target_name in digits_data.target_names:
    print(target_name)

# finito
