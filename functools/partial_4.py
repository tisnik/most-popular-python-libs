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

import operator
from functools import partial, reduce


def mul(*args):
    return reduce(operator.mul, args, 1)


print(mul(2, 3, 7))


print()


doubler = partial(mul, 2)


for i in range(11):
    print(i, doubler(i, 10))


print()


doubleDoubler = partial(mul, 2, 2)


for i in range(11):
    print(i, doubleDoubler(i, 10))
