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

# import tridy realizujici vyber atributu
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

from sklearn import linear_model

# import funkce pro nacteni datove sady, kterou pouzijeme
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import cross_val_score

# nacteni datove sady
housings = fetch_california_housing()

# jmena jednotlivych atributu
feature_names = housings["feature_names"]

# X je matice (feature matrix)
X = housings.data

# y je vektor (response vector)
y = housings.target

for k_best in range(1, len(feature_names)+1):
    # provest filtering dat
    sel = SelectKBest(f_classif, k=k_best)
    X_new = sel.fit_transform(X, y)

    # konstrukce modelu pro regresi
    lr = linear_model.LinearRegression()
    scores = cross_val_score(lr, X_new, y, cv=10, scoring="r2")

    print(k_best, X_new.shape, sel.get_feature_names_out(input_features=feature_names), scores.mean())
