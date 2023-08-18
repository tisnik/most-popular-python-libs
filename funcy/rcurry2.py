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

from funcy import rcurry


def div(x, y):
    return x / y


curried = rcurry(div)

print(curried)
print(curried(1))
print(curried(1)(2))  # pozor na umístění závorek!
