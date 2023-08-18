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

from funcy import compose


def add(x, y):
    return x+y


def double(x):
    return 2*x


composed = compose(double, add)

print(composed(2, 3))
print(composed(-2, -3))
