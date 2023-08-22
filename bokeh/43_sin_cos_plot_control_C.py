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
from bokeh.layouts import row
from bokeh.models import Slider, ColumnDataSource, CustomJS

# taktéž budeme potřebovat některé funkce z knihovny `numpy`
import numpy as np

# vykreslení průběhu funkce sin

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose
y1 = np.sin(x)

# hodnoty na y-ové ose
y2 = np.cos(x)

# zdroj dat
source = ColumnDataSource(data={"x": x, "y": y1})

# plocha pro graf
p = figure(title="sin(x) a cos(x)", x_axis_label="x", y_axis_label="sin(x) a cos(x)")

# vykreslení průběhu
p.line(source=source, line_width=2, color="#00a0a0")
p.line(x, y2, legend_label="cos(x)", line_width=2, color="#a0a000")

# callback zavolaný po změně souřadnic posuvníku
on_amplitude_change = CustomJS(
    args={"source": source},
    code="""
    const data = source.data;
    const a = cb_obj.value
    const x = data['x']
    const y = data['y']
    for (let i = 0; i < x.length; i++) {
        y[i] = a*Math.sin(x[i])
    }
    source.change.emit();
""",
)


# posuvník pro změnu amplitudy
amplitude_slider = Slider(start=-1, end=1, value=1, step=0.05, title="Amplitude")
amplitude_slider.js_on_change("value", on_amplitude_change)

# vykreslení grafu do plochy webové stránky
show(row(p, amplitude_slider))
