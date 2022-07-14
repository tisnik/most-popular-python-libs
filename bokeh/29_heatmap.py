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

factors = ["a", "b", "c"]
x = ["a"] * 3 + ["b"] * 3 + ["c"] * 3
y = factors * 3

print(factors)
print(x)
print(y)

# barvy jednotlivých čtverečků
colors = [
    "#0B486B",
    "#79BD9A",
    "#CFF09E",
    "#79BD9A",
    "#0B486B",
    "#79BD9A",
    "#CFF09E",
    "#79BD9A",
    "#0B486B",
]

# plocha pro graf
p = figure(
    title="Categorical Heatmap",
    tools="hover",
    toolbar_location=None,
    x_range=factors,
    y_range=factors,
)

# vykreslení heatmapy
p.rect(x, y, color=colors, width=1, height=1)

# vykreslení grafu do plochy webové stránky
show(p)
