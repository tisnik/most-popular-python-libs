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

from funcy import curry


def add3(x, y, z):
    return x + y + z


curried = curry(add3)

print(curried)
print(curried(1))
print(curried(1)(2))      # pozor na umístění závorek!
print(curried(1)(2)(3))   # pozor na umístění závorek!
