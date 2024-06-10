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

from random import randrange

from toolz.itertoolz import frequencies, unique

values = [randrange(1, 11, 1) for _ in range(30)]
print(frequencies(values))

values2 = unique(values)
print(frequencies(values2))
