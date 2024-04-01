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

from functools import reduce

n = range(0, 11)

factorials = map(lambda n: reduce(lambda a, b: a*b, range(1, n+1), 1), n)

print(list(factorials))
