# naimportujeme vybrané funkce z knihovny `bokeh.plotting`

from bokeh.plotting import figure, show

# taktéž budeme potřebovat některé funkce z knihovny `numpy`
import numpy as np

# vykreslení průběhu funkce sin

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(x)

# plocha pro graf
p = figure(title="sin(x)", x_axis_label='x', y_axis_label='sin(x)')

# vykreslení průběhu
p.line(x, y, legend_label="sin(x)", line_width=2)

# vykreslení grafu do plochy webové stránky
show(p)
