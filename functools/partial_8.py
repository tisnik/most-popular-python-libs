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

from functools import partial


def mul(x, y, z, w):
    return x * y * z * w


def displayInfo(name, obj):
    print("name:      ", name)
    print("function:  ", obj.func)
    print("arguments: ", obj.args)
    print("keywords:  ", obj.keywords)
    print()


#f1 = mul
#displayInfo(f1)

f2 = partial(mul, 2)
displayInfo("f2", f2)

f3 = partial(mul, 2, 3)
displayInfo("f3", f3)

f4 = partial(mul, 2, 3, 4)
displayInfo("f4", f4)

f5 = partial(mul, 2, 3, 4, 5)
displayInfo("f5", f5)

f6 = partial(mul, 2, 3, 4, 5, 6)
displayInfo("f6", f6)
