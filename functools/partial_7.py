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


f1 = mul
reveal_type(f1)

f2 = partial(mul, 2)
reveal_type(f2)

f3 = partial(mul, 2, 3)
reveal_type(f3)

f4 = partial(mul, 2, 3, 4)
reveal_type(f4)

f5 = partial(mul, 2, 3, 4, 5)
reveal_type(f5)

f6 = partial(mul, 2, 3, 4, 5, 6)
reveal_type(f6)
