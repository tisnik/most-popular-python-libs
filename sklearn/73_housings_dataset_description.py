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

print(dir(housings))

print("-" * 100)

# podrobny popis datove sady
print(housings["DESCR"])
