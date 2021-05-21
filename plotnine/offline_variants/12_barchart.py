#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from plotnine.data import mpg
from plotnine import ggplot, aes, geom_bar

g = (ggplot(mpg) + aes(x="class") + geom_bar())

g.save("12.png")
