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

from toolz.itertoolz import first, iterate, take


def one_step(p):
    return (p[1], p[0]+p[1])


sequence = iterate(one_step, (0, 1))
sequence = take(10, sequence)
print(list(map(first, sequence)))
