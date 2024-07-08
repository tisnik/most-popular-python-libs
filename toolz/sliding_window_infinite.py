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

from toolz.itertoolz import iterate, sliding_window, take


def inc(x):
    return x+1


values = iterate(inc, 10)

sw = sliding_window(5, values)

for window in take(20, sw):
    print(window)
