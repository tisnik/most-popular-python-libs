# naimportujeme vybrané funkce z knihovny `bokeh.plotting`

from bokeh.plotting import figure, show

# taktéž budeme potřebovat některé funkce z knihovny `numpy`
import numpy as np

# vykreslení průběhu funkce sin

# počet bodů na spirále
points = 150

# úhel v polárním grafu
theta = np.linspace(0.01, 8 * np.pi, points)

# koeficient spirály
k = 0.15

# funkce: vzdálenost od středu
radius = np.exp(k * theta)

y1 = radius * np.sin(theta)

y2 = radius * np.cos(theta)

# plocha pro graf
p = figure(title="Spiral", x_axis_label="x", y_axis_label="y")

# vykreslení průběhu
p.line(y1, y2, line_width=2, color="blue")

# vykreslení grafu do plochy webové stránky
show(p)
