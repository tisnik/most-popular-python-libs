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
from bokeh.io import show
from bokeh.plotting import figure

# jména na X-ové ose
languages = [
    "Python",
    "C++",
    "C#",
    "Visual Basic",
    "JavaScript",
    "SQL",
    "Assembly",
    "Java",
    "C",
    "Swift",
]

# hodnoty na Y-ové ose
ratings = [12.20, 9.63, 6.12, 5.42, 2.09, 1.94, 1.85, 10.47, 11.91, 1.55]

sorted_ratings = sorted(languages, key=lambda x: ratings[languages.index(x)])

# plocha pro graf
p = figure(
    x_range=sorted_ratings,
    height=350,
    title="TIOBE index",
    toolbar_location=None,
    tools="",
)

# vykreslení průběhu hodnot
p.vbar(x=languages, top=ratings, width=0.9)

# styl vykreslení
p.xgrid.grid_line_color = None
p.y_range.start = 0

# vykreslení grafu do plochy webové stránky
show(p)
