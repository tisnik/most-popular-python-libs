#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

@micropython.viper
def add(x: int, y: int) -> int:
    return x+y


import utime

t1 = utime.ticks_us()

x: int = 0
for i in range(10000):
    x = add(x, 10)

print(x)
t2 = utime.ticks_us()
print(utime.ticks_diff(t2, t1))
