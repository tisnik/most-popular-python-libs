import matplotlib.pyplot as plt
import scipy.datasets as datasets
import scipy.signal as signal

import numpy as np

# načtení signálu
ekg = datasets.electrocardiogram()

# jen prvních 250 vzorků
ekg = ekg[0:250]

# resampling
resampled = signal.resample(ekg, 50)

# vykreslení výsledného signálu
plt.plot(np.linspace(0, 1000, len(ekg)), ekg, "b")
plt.plot(np.linspace(0, 1000, len(resampled)), resampled, "r")

# uložení grafu s průběhem signálu
plt.savefig("resample_2.png")

# zobrazení grafu
plt.show()
