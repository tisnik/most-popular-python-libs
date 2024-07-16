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

data = range(11)

filtered = filter(lambda value : value %2 == 1, data)
print(list(filtered))

filtered = filter(lambda value : value %2 == 0, data)
print(list(filtered))
