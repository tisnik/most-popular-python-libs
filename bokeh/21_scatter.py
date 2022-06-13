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

x = radius * np.sin(theta)

y = radius * np.cos(theta)

# plocha pro graf
p = figure(title="Spiral", x_axis_label="x", y_axis_label="y")

# vykreslení průběhu
p.scatter(x, y, size=5, color="blue")

# vykreslení grafu do plochy webové stránky
show(p)
