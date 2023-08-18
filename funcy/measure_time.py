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

from funcy import decorator
import time


@decorator
def measure_time(func):
    t = time.time()
    res = func()
    print("Function took " + str(time.time() - t) + " seconds to run")
    return res


@measure_time
def tested_function(n):
    print(f"Sleeping for {n} seconds")
    time.sleep(n)


tested_function(1)
tested_function(2)
