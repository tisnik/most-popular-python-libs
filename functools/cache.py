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
from functools import cache

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


max_n = 300

for i in range(20):
    if i % 5 == 0:
        fib.cache_clear()
    print(fib.cache_info())
    start = time()
    result = fib(max_n)
    end = time()
    print(result, end - start)
