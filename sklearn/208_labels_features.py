# Načtení datové sady, charakteristiky sloupců s návěstím a vlastním textem

import pandas as pd 

# načtení tabulky do datového rámce, specifikace kódování souboru
spam = pd.read_csv("spam.csv", encoding="latin1")

# hodnocení (spam/ham)
labels = spam.v1.values

# vlastní text SMS
features = spam.v2.values

# hodnoty použité později pro trénink modelu
print("Labels:")
print(labels)
print("Number of labels:", len(labels))
print()

print("Features:")
print(features)
print("Number of features:", len(features))
