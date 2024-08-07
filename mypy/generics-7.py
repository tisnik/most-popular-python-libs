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

from typing import Tuple, TypeVar

T = TypeVar("T")


def pair(first: T, second: T) -> Tuple[T, T]:
    x = (first, second)
    return x


p = pair(0, "B")
print(type(p[0]))
print(type(p[1]))
