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
s3 = s2 - s

# vytvoření grafu
plt.subplot(221)
plt.plot(s)

plt.subplot(222)
plt.plot(s2)

plt.subplot(223)
plt.plot(s3)

# uložení grafu
plt.savefig("series_plot_12.png")

# vykreslení grafu
plt.show()
