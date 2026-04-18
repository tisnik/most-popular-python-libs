import scipy.datasets as datasets
import scipy.signal as signal

import matplotlib.pyplot as plt

# načtení signálu
ekg = datasets.electrocardiogram()

# jen prvních 1000 vzorků
ekg = ekg[0:1000]

# filtr
win = signal.windows.triang(50)

# výpočet konvoluce
filtered = signal.convolve(ekg, win, mode="same") / sum(win)

plt.plot(filtered, "r")

# uložení grafu s průběhem signálu
plt.savefig("convolve_1d_3.png")

# zobrazení grafu
plt.show()
