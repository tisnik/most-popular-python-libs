# naimportujeme vybrané funkce z knihovny `bokeh.plotting`

from bokeh.plotting import figure, show
from bokeh.layouts import row
from bokeh.models import Slider

# taktéž budeme potřebovat některé funkce z knihovny `numpy`
import numpy as np

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
p.line(x, y1, legend_label="sin(x)", line_width=2, color="#00a0a0")
p.line(x, y2, legend_label="cos(x)", line_width=2, color="#a0a000")

# posuvník pro změnu amplitudy
amplitude_slider = Slider(start=-1, end=1, value=1, step=0.05, title="Amplitude")

# vykreslení grafu do plochy webové stránky
show(row(p, amplitude_slider))
