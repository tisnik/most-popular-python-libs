# - zobrazení 3D grafu funkce typu z=f(x,y)

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection="3d")

delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R = np.sqrt(X * X + Y * Y)

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R) / R

# zobrazení 3D grafu formou plochy
ax.plot_surface(
    X, Y, Z, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth=0, antialiased=False
)

# zobrazení grafu
plt.show()
