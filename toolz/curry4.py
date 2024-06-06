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

from toolz import curry


@curry
def add3(x, y, z):
    return x + y + z


print(add3)
print(add3(1))
print(add3(1)(2))      # pozor na umístění závorek!
print(add3(1)(2)(3))   # pozor na umístění závorek!
