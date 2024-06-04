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

from toolz import compose

composed = compose(
        lambda x: -x if x<0 else x,
        lambda x: x*2,
        lambda x, y: x+y)

print(composed(2, 3))
print(composed(-2, -3))
