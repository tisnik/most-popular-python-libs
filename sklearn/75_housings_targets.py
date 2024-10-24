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

from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

# jmena atributu
print("Feature names:")
print(housings["feature_names"])

print("-" * 100)

# vazba mezi numerickou hodnotou a lidskym vyjadrenim hodnoty
# atributu
print("Target names:")
print(housings["target_names"])

print("-" * 100)

# druhy rostlin z datove sady v numericke podobe
print("Targets:")
print(housings["target"])
