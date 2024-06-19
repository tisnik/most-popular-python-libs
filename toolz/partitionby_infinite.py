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

from toolz.itertoolz import iterate, take
from toolz.recipes import partitionby


def inc(x):
    return x+1


values = iterate(inc, 0)

values2 = partitionby(lambda x: x % 2 == 0, values)

print(list(take(10, values2)))
