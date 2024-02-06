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
def loop():
    x = 0
    for i in range(1000):
        for j in range(1000):
            x+=1
    return x


import utime

t1 = utime.ticks_us()
loop()
t2 = utime.ticks_us()
print(utime.ticks_diff(t2, t1))
