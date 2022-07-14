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

# vykreslení průběhu funkce sin

# hodnoty na x-ové ose
x = np.linspace(-5, 5, 100)

# hodnoty na y-ové ose
y1 = x

# hodnoty na y-ové ose
y2 = x ** 2

# hodnoty na y-ové ose
y3 = x ** 3

# hodnoty na y-ové ose
y4 = 2 ** x

# plocha pro graf
p = figure(
    title="Functions", x_axis_label="x", y_axis_label="Functions", y_axis_type="log"
)

# vykreslení průběhu
p.line(x, y1, legend_label="x", line_width=2, color="#00a0a0")
p.line(x, y2, legend_label="x^2", line_width=2, color="#a0a000")
p.line(x, y3, legend_label="x^3", line_width=2, color="#00a0a0")
p.line(x, y4, legend_label="2^x", line_width=2, color="#a000a0")

# vykreslení grafu do plochy webové stránky
show(p)
