from scipy.interpolate import CubicSpline

import numpy as np

import matplotlib.pyplot as plt


# hodnoty na x-ové ose
pts = np.array([[-1, 0],
       [0, 1],
       [1, 0],
       [0, -1],
       [-1, 0]])

t = np.arange(0, 5)

xs = np.linspace(0, 4, 100)

# vytvoření spline
spline = CubicSpline(t, pts, bc_type="periodic")

# rozměry grafu při uložení: 640x640 pixelů
fig, ax = plt.subplots(1, figsize=(6.4, 6.4))

# vykreslení bodů
ax.plot(pts[:, 0], pts[:, 1], 'o', label="data")

xs = np.linspace(0, 6.28, 100)

# vykreslení kružnice
ax.plot(np.cos(xs), np.sin(xs), "b-", label="circle");

# vykreslení křivky
ax.plot(spline(xs)[:, 0], spline(xs)[:, 1], "r-", label='spline')

plt.legend()

# uložení grafu do rastrového obrázku
plt.savefig("cubic_spline_5.png")

# zobrazení grafu
plt.show()
