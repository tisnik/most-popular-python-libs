# Načtení datové sady do datového rámce a zjištění statistiky o ohodnocení textu

import pandas as pd 

# načtení tabulky do datového rámce, specifikace kódování souboru
spam = pd.read_csv("spam.csv", encoding="latin1")

# početm spamů a hamů
print(spam.v1.value_counts())
