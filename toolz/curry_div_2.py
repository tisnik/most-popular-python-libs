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

from toolz import curry, iterate, take


def inc(x):
    return x+1


@curry
def divisible_by(y, x):
    return x % y == 0


even = divisible_by(2)


sequence = iterate(inc, 0)
evens = filter(even, sequence)

sequence = take(10, evens)
print(list(sequence))

