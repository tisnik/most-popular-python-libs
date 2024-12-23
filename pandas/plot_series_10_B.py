#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import matplotlib.pyplot as plt
import numpy as np
import pandas

# hodnoty na x-ové ose
r = np.linspace(0, 2 * np.pi, 100)

# konstrukce datové struktury Series
s = pandas.Series(data=np.sin(r), index=r)

s2 = np.random.rand(100) / 2
s2 = s + s2

s3 = s2.rolling(10, win_type="gaussian").sum(std=3)

# tisk obsahu Series
print(s3)

# vytvoření grafu
s3.plot(grid=True)

# uložení grafu
plt.savefig("series_plot_10_B.png")

# vykreslení grafu
plt.show()
