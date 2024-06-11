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

from toolz.itertoolz import interleave, iterate, take


def inc(x):
    return x+1


values1 = iterate(inc, 0)
values2 = ["odd", "even"]*5
interleaved = interleave((values1, values2))

print(list(take(20, interleaved)))
