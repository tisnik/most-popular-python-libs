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

from funcy import first, iterate, take


def one_step(p):
    return (p[1], p[0]+p[1])


sequence = iterate(one_step, (0, 1))

slice = take(20, sequence)
print(list(map(first, slice)))
