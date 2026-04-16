from scipy.fft import dst

import numpy as np
import matplotlib.pyplot as plt

# signál
t = np.cos(np.linspace(0, 2.0*np.pi, 100)) + 0.5*np.cos(np.linspace(0, 20*np.pi, 100))

# diskrétní sinová transformace
f = dst(t)

# vykreslení výsledného signálu
plt.plot(f)

# uložení grafu s průběhem signálu
plt.savefig("dst_1.png")
