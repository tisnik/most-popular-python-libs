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

import random
from array import array
from time import perf_counter

size = 10000

a = array("I", [random.randrange(0, 10000) for i in range(size)])

t1 = perf_counter()

for i in range(size - 1, 0, -1):
    for j in range(0, i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

t2 = perf_counter()

print(f"Sorted in {t2-t1} seconds:")

print("\nBegins with:")
print(a[:100])

print("\nEnds with:")
print(a[-100:])
