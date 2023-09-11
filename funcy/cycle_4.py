#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from funcy import count, cycle, take, repeat

suits = ["♠", "♥", "♦", "♣"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

seq1 = cycle(suits)
seq2 = cycle(values)

zipped = zip(seq1, seq2)

slice = take(len(suits)*len(values), zipped)

for key, val in slice:
    print(f"{key}{val}")
