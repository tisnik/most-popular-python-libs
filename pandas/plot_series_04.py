#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import numpy as np
import pandas
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
r = np.linspace(0, 2*np.pi, 20)

# konstrukce datové struktury Series
s = pandas.Series(data=np.sin(r), index=r)

# tisk obsahu Series
print(s)

# vytvoření grafu
s.plot.barh(grid=True)

# uložení grafu
plt.savefig("series_plot_04.png")

# vykreslení grafu
plt.show()
