# Načtení datové sady a zjištění základních údajů o načteném datovém rámci
#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#
#
# Tento demonstracni priklad je pouzity v serialu o datove analyze
# s vyuzitim programovaciho jazyka Python:
# https://www.root.cz/serialy/datova-analyza-s-vyuzitim-jazyka-python/
#


import pandas as pd 

# načtení tabulky do datového rámce, specifikace kódování souboru
spam = pd.read_csv("spam.csv", encoding="latin1")

# základní informace o datovém rámci
print(spam.describe())
