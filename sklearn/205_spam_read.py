# Pokus o načtení datové sady a zjištění základních údajů

import pandas as pd 

# načtení tabulky do datového rámce
spam = pd.read_csv("spam.csv")

# základní informace o datovém rámci
print(spam.describe())
