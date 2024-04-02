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

from plotnine import aes, geom_point, geom_smooth, ggplot, xlab, ylab
from plotnine.data import economics

g = (
    ggplot(economics)
    + aes(x="date", y="uempmed")
    + geom_point()
    + geom_smooth(color="red", span=0.1)
    + xlab("date (year)")
    + ylab("unemploynment")
)

g.save("20.png")
