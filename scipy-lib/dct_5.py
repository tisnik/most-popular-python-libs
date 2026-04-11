from scipy.fft import dct

import numpy as np
import matplotlib.pyplot as plt

# signál
t = np.cos(np.linspace(0, 2.0*np.pi, 100)) - 0.5*np.cos(np.linspace(0, 20*np.pi, 100))

# vykreslení signálu
plt.plot(t)

# uložení grafu s průběhem signálu
plt.savefig("dct_5.png")
