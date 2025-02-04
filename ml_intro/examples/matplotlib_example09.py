# - základní polární graf

import matplotlib.pyplot as plt
import numpy as np

# úhel v polárním grafu
theta = np.linspace(0.01, 2 * np.pi, 150)

# vzdálenost od středu
radius = np.log(theta)

ax = plt.subplot(111, projection="polar")

# vykreslit průběh funkce
# v polárním grafu
ax.plot(theta, radius)

# zobrazení grafu
plt.show()
