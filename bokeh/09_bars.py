#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2022  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

# naimportujeme vybrané funkce z knihovny `bokeh.plotting`

from bokeh.plotting import figure, show

# hodnoty na x-ové a y-ové ose
x = range(10)
y = [1, 2, 7, 7, 4, 5, -5, 0, 2, 1]

# plocha pro graf
p = figure(title="Naměřené hodnoty", x_axis_label="x", y_axis_label="y")

# vykreslení průběhu naměřených hodnot
p.vbar(x, top=y, width=0.7, legend_label="Napětí", line_width=2)

# vykreslení grafu do plochy webové stránky
show(p)
