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

from funcy import autocurry


def pow(x, y):
    return x ** y


n_pow = autocurry(pow)
powX = n_pow()
pow2 = n_pow(2)
pow10 = n_pow(10)
pow3to3 = n_pow(3, 3)

print(powX(3, 3))
print(pow2(2))
print(pow10(2))
print(pow3to3)
