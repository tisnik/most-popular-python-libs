#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import numpy as np
import pandas
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
r = np.linspace(0, 2 * np.pi, 100)

# konstrukce datové struktury Series
s = pandas.Series(data=np.sin(r), index=r)

s2 = s.map(lambda x: x + np.random.rand() / 2)

# tisk obsahu Series
print(s2)

# vytvoření grafu
s2.plot(grid=True)

# uložení grafu
plt.savefig("series_plot_07.png")

# vykreslení grafu
plt.show()
