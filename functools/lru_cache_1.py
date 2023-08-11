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

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


max_n = 40

for _ in range(10):
    start = time()
    result = fib(max_n)
    end = time()
    print(result, end - start)
