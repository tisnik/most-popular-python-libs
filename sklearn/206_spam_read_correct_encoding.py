# Načtení datové sady a zjištění základních údajů o načteném datovém rámci

import pandas as pd 

# načtení tabulky do datového rámce, specifikace kódování souboru
spam = pd.read_csv("spam.csv", encoding="latin1")

# základní informace o datovém rámci
print(spam.describe())
