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

from toolz.itertoolz import nth

values = [chr(i) for i in range(ord("A"), ord("Z")+1)]

print(values)
print(nth(0, values))
print(nth(25, values))
print(nth(26, values))
