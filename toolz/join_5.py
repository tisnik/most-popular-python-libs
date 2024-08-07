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

from toolz.itertoolz import join

names = [
    (0, "Alice"),
    (1, "Bob"),
    (2, "Charlie"),
    (3, "Zdenek"),
]

phones = [
    ("Alice",   "555-1234"),
    ("Bob",     "555-5678"),
    ("Charlie", "555-9999"),
    ("Martin",  "000-0000"),
]

for item in join(1, names, 0, phones, left_default=(0, "Nikdo"), right_default=("Neznamy", "111-1111")):
    print(item[0][0], item[0][1], item[1][0], item[1][1])
