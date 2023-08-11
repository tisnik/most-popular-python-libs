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

from time import time
from functools import cached_property, lru_cache


class FibonacciNumber:
    def __init__(self, n):
        self._n = n

    @cached_property
    def value(self):
        return FibonacciNumber.compute(self._n)

    @staticmethod
    @lru_cache
    def compute(n):
        if n < 2:
            return n
        return FibonacciNumber.compute(n-1) + FibonacciNumber.compute(n-2)


f = FibonacciNumber(40)

for _ in range(10):
    start = time()
    result = f.value
    end = time()
    print(result, end - start)
