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
plt.plot(s, "--", s2, "-", s3, "-")

# uložení grafu
plt.savefig("series_plot_11.png")

# vykreslení grafu
plt.show()
