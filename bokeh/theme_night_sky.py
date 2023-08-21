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
from bokeh.io import curdoc

# taktéž budeme potřebovat některé funkce z knihovny `numpy`
import numpy as np

# nastavení tématu
curdoc().theme = "night_sky"

# vykreslení průběhu funkce sin

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose
y1 = np.sin(x)

# hodnoty na y-ové ose
y2 = np.cos(x)

# plocha pro graf
p = figure(title="sin(x) a cos(x)", x_axis_label="x", y_axis_label="sin(x) a cos(x)")

# vykreslení průběhu
p.line(x, y1, legend_label="sin(x)", line_width=2, color="#0aa")
p.line(x, y2, legend_label="cos(x)", line_width=2, color="#aa0")

# vykreslení grafu do plochy webové stránky
show(p)
