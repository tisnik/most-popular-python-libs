# naimportujeme vybrané funkce z knihovny `bokeh.plotting`

from bokeh.plotting import figure, show

# taktéž budeme potřebovat některé funkce z knihovny `numpy`
import numpy as np

# vykreslení průběhu funkce sin

# hodnoty parametrické křivky
t = np.linspace(0, 2 * np.pi, 100)

y1 = np.sin(t)

y2 = np.cos(t)

# plocha pro graf
p = figure(title="Circle", x_axis_label="x", y_axis_label="y")

# vykreslení průběhu
p.line(y1, y2, line_width=2, color="blue")

# vykreslení grafu do plochy webové stránky
show(p)
