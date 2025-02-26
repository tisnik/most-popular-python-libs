#
#  (C) Copyright 2025  Pavel Tisnovsky
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
import matplotlib.pyplot as plt
from scipy import signal


def plot(x, y, filename, title):
    # nastaveni os
    plt.xticks(ticks=np.floor(np.linspace(0, 511, 9)))
    plt.yticks(ticks=np.linspace(-1.5, 1.5, 7))
    plt.xlim([0, 511])
    plt.ylim([-1.5, 1.5])

    # vykresleni
    plt.plot(x, y)

    # mrizka a dalsi parametry grafu
    plt.grid()
    plt.title(title)

    # ulozeni na disk
    plt.savefig(filename)

    # zobrazeni
    plt.show()

    plt.clf()


# prubeh vlny
x = np.linspace(0, 511, 200)
y = np.sin(x * 2 * np.pi / 256.0)
plot(x, y, "waveform_0.png", "Tvar vlny #0: sinus")

# vynulovat zaporne hodnoty
y[y < 0] = 0
plot(x, y, "waveform_1.png", "Tvar vlny #1: polovicni sinus")

y = np.abs(np.sin(x * 2 * np.pi / 256.0))
plot(x, y, "waveform_2.png", "Tvar vlny #2: absolutni hodnoty sinu")

y = np.abs(np.sin(x * 2 * np.pi / 256.0))
y2 = signal.square(4 * np.pi / 256.0 * x)
y3 = y * y2
y3[y3 < 0] = 0
plot(x, y3, "waveform_3.png", "Tvar vlny #3: pulsní varianta")

y = np.sin(x * 4 * np.pi / 256.0)
y2 = signal.square(2 * np.pi / 256.0 * x)
y2[y2 < 0] = 0
y3 = y * y2
plot(x, y3, "waveform_4.png", "Tvar vlny #4: jen sudé vlny")

y = np.abs(np.sin(x * 4 * np.pi / 256.0))
y2 = signal.square(2 * np.pi / 256.0 * x)
y2[y2 < 0] = 0
y3 = y * y2
plot(x, y3, "waveform_5.png", "Tvar vlny #5: jen sudé vlny, abs sin")

y = signal.square(2 * np.pi / 256.0 * x)
plot(x, y, "waveform_6.png", "Tvar vlny #6: obdélník")
