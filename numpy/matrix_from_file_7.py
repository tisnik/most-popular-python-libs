"""Načtení obsahu matice z binárního souboru se specifikací formátu a offsetu."""

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

# první řádek matice načtený z binárního souboru
first_row = 200

# poslední řádek matice načtený z binárního souboru
last_row = 350

# počet sloupců matice
columns = 5

# platformově nezávislé získání počtu bajtů pro každý prvek typu integer
item_size = np.dtype("i").itemsize

# výpočet offsetu při čtení řádků od first_row z binárního souboru
offset = first_row * columns * item_size
count = (last_row - first_row) * columns

print("offset=", offset, "bytes")
print("count=", count, "items")
print()

# načtení prvků matice z binárního souboru a konstrukce matice
m = np.fromfile("matrix3.bin", dtype="i", offset=offset, count=count).reshape(
    last_row - first_row, columns
)

# výpis obsahu právě zkonstruované matice
print(m)
