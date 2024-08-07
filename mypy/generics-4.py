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
U = TypeVar("U")


def pair(first: T, second: U) -> Tuple[T, U]:
    x = (first, second)
    return x


reveal_type(pair(1, 2))
reveal_type(pair(0, "B"))
reveal_type(pair("A", 42))
reveal_type(pair("A", "B"))
