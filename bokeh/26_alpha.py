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
from bokeh.layouts import grid

# taktéž budeme potřebovat některé funkce z knihovny `numpy`
import numpy as np


# funkce pro výpočet dalšího bodu Lorenzova atraktoru
def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot


# krok (změna času)
dt = 0.01

# celkový počet vypočtených bodů na Lorenzově atraktoru
n = 10000

# prozatím prázdné pole připravené pro výpočet
x = np.zeros((n,))
y = np.zeros((n,))
z = np.zeros((n,))

# počáteční hodnoty
x[0], y[0], z[0] = (0.0, 1.0, 1.05)

# vlastní výpočet atraktoru
for i in range(n - 1):
    x_dot, y_dot, z_dot = lorenz(x[i], y[i], z[i])
    x[i + 1] = x[i] + x_dot * dt
    y[i + 1] = y[i] + y_dot * dt
    z[i + 1] = z[i] + z_dot * dt

# plocha pro první graf
p1 = figure(
    title="Lorenz attractor", x_axis_label="x", y_axis_label="y", width=300, height=300
)

# vykreslení průběhu
p1.scatter(x, y, size=0.5, color="blue", alpha=0.4)

# plocha pro druhý graf
p2 = figure(
    title="Lorenz attractor", x_axis_label="x", y_axis_label="z", width=300, height=300
)

# vykreslení průběhu
p2.scatter(x, z, size=0.5, color="darkred", alpha=0.4)

# plocha pro třetí graf
p3 = figure(
    title="Lorenz attractor", x_axis_label="y", y_axis_label="z", width=300, height=300
)

# vykreslení průběhu
p3.scatter(y, z, size=0.5, color="darkgreen", alpha=0.4)

# vykreslení grafu do plochy webové stránky
show(grid([[p2, p3], p1]))
