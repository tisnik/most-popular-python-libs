"""Načtení obsahu vektoru z textového souboru se specifikací oddělovače."""

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#


import numpy as np

v = np.fromfile("vector1.txt", sep=",")
print(v)
