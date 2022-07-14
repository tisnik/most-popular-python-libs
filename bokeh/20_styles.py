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

# taktéž budeme potřebovat některé funkce z knihovny `numpy`
import numpy as np

values = 50

# hodnoty na x-ové ose
x = np.linspace(0, 100, values)

# hodnoty na y-ové ose
y1 = np.full(values, 10)
y2 = np.full(values, 9)
y3 = np.full(values, 8)
y4 = np.full(values, 7)
y5 = np.full(values, 6)
y6 = np.full(values, 5)
y7 = np.full(values, 4)
y8 = np.full(values, 3)
y9 = np.full(values, 2)
y10 = np.full(values, 1)

# plocha pro graf
p = figure(title="Styly vykreslení", x_axis_label="x", y_axis_label="y")

# vykreslení průběhů
p.square_dot(x, y1, legend_label="square_dot", line_width=3, color="#f00000")
p.circle(x, y2, legend_label="circle", line_width=3, color="#f00020")
p.asterisk(x, y3, legend_label="asterisk", line_width=3, color="#e00040")
p.circle_cross(x, y4, legend_label="circle_cross", line_width=3, color="#c00060")
p.circle_dot(x, y5, legend_label="circle_dot", line_width=3, color="#a00080")
p.cross(x, y6, legend_label="cross", line_width=3, color="#8000a0")
p.dot(x, y7, legend_label="dot", line_width=3, color="#6000c0")
p.plus(x, y8, legend_label="plus", line_width=3, color="#4000e0")
p.dash(x, y9, legend_label="dash", line_width=3, color="#2000f0")
p.line(x, y10, legend_label="line", line_width=3, color="#0000f0")

# vykreslení grafu do plochy webové stránky
show(p)
