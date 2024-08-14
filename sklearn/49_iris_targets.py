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

print(dir(iris))

print("-" * 100)

# jmena atributu
print("Feature names:")
print(iris["feature_names"])

print("-" * 100)

# vazba mezi numerickou hodnotou a lidskym vyjadrenim hodnoty
# atributu
print("Target names:")
print(iris["target_names"])

print("-" * 100)

# druhy rostlin z datove sady v numericke podobe
print("Targets:")
print(iris["target"])

