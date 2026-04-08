import numpy as np
import scipy.datasets as datasets
import scipy.signal as signal

import matplotlib.pyplot as plt

# načtení signálu
ekg = datasets.electrocardiogram()

# jen prvních 250 vzorků
ekg = ekg[0:250]

# resampling
resampled = signal.resample(ekg, 50)

# vykreslení výsledného signálu
plt.plot(np.linspace(0, 1000, len(ekg), endpoint=False), ekg, "b")
plt.plot(np.linspace(0, 1000, len(resampled), endpoint=False), resampled, "r")

# uložení grafu s průběhem signálu
plt.savefig("resample_3.png")

# zobrazení grafu
plt.show()
