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

from toolz.recipes import partitionby

values = [randrange(1, 11, 1) for _ in range(30)]
print(values)

values2 = partitionby(lambda x: x < 5, values)
print(list(values2))
