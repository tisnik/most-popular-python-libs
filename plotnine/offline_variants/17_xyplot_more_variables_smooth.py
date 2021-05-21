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
from plotnine import ggplot, aes, facet_grid, labs, geom_point, stat_smooth

g = (ggplot(mpg)
     + facet_grid(facets="year~class")
     + aes(x="displ", y="hwy")
     + labs(
         x="Engine Size",
         y="Miles per Gallon",
         title="Miles per Gallon for Each Year and Vehicle Class")
     + geom_point()
     + stat_smooth(method='lm'))

g.save("17.png")
