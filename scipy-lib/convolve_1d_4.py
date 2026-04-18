import scipy.datasets as datasets
import scipy.signal as signal

import matplotlib.pyplot as plt

# načtení signálu
ekg = datasets.electrocardiogram()

# jen prvních 1000 vzorků
ekg = ekg[0:1000]

# filtry
win1 = signal.windows.triang(50)
win2 = signal.windows.hann(50)

# výpočet konvoluce
filtered1 = signal.convolve(ekg, win1, mode="same") / sum(win1)
filtered2 = signal.convolve(ekg, win2, mode="same") / sum(win2)

plt.plot(filtered1, "b")
plt.plot(filtered2, "r")

# uložení grafu s průběhem signálu
plt.savefig("convolve_1d_4.png")

# zobrazení grafu
plt.show()
