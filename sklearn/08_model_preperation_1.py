#!/usr/bin/env python

# import funkce, která vrátí obrázky pro práci
from sklearn.datasets import load_digits

# načtení obrázků, s nimiž budeme dále pracovat
digits_data = load_digits()

# vytvoření seznamu, které použijeme
images = list(zip(digits_data.target, digits_data.images))

# nebudeme vyposovat tisíce údajů - postačí prvních dvacet
shortened = images[:20]

# výpis dat použitých pro tvorbu modelu
for i, (label, image) in enumerate(shortened):
    print(f"i={i}  label={label}\n", image, "\n")

# finito
