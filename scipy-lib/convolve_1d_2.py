import scipy.datasets as datasets
import scipy.signal as signal

import matplotlib.pyplot as plt

# načtení signálu
ekg = datasets.electrocardiogram()

# jen prvních 1000 vzorků
ekg = ekg[0:1000]

# filtr
win = signal.windows.hann(50)

# výpočet konvoluce
filtered = signal.convolve(ekg, win, mode="same") / sum(win)

# vykreslení původního i výsledného signálu
plt.plot(ekg)
plt.plot(filtered, "r")

# uložení grafu s průběhem signálu
plt.savefig("convolve_1d_2.png")

# zobrazení grafu
plt.show()
