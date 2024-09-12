# - jednoduchý histogram

import numpy as np
import matplotlib.pyplot as plt

# náhodné hodnoty
y = np.random.normal(0, 0.1, 10000)

plt.hist(y, bins=30, range=None, density=True)

# zobrazení grafu
plt.show()
