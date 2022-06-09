# naimportujeme vybrané funkce z knihovny `bokeh.plotting`

from bokeh.plotting import figure, show

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
p.vbar(
    x, top=y1, bottom=y2, width=0.01, legend_label="sin(x)", line_width=2, color="blue"
)

# vykreslení grafu do plochy webové stránky
show(p)
