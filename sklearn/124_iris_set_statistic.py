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

import numpy as np

# import funkce pro nacteni datove sady, kterou pouzijeme
from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

# precteni dat z datove sady
data = iris["data"]

# nadpis tabulky
print("Feature                     Min          Max          Avg         Std          Var")

# zakladni statisticke informace o jednotlivych atributech
for i in range(len(iris["feature_names"])):
    column = data[:, i]
    feature = iris.feature_names[i]
    print(f"{feature:20}   {column.min():10.3f}   {column.max():10.3f}   {np.mean(column):10.3f}  {np.std(column):10.3f}  {np.var(column):11.3f}")
