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
# Clanek, kde je tento demonstracni priklad pouzit:
# Datová analýza s využitím nástroje scikit-learn: první kroky
# https://www.root.cz/clanky/datova-analyza-s-vyuzitim-nastroje-scikit-learn-prvni-kroky/#k19
#

from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

# jakeho typu je vlastne datova sada?
print(type(iris))

print("-" * 100)

# dostupne atributy a metody
print(dir(iris))

