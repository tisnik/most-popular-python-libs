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
]

phones = [
    ("Alice",   "555-1234"),
    ("Bob",     "555-5678"),
    ("Charlie", "555-9999"),
]

for item in join(1, names, 0, phones): 
    print(item)
