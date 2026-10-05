import matplotlib.pyplot as plt
import scipy.datasets as datasets

# načtení signálu
ekg = datasets.electrocardiogram()

# zobrazení signálu
plt.plot(ekg)

# uložení grafu s průběhem signálu
plt.savefig("ekg_1.png")

# zobrazení grafu
plt.show()
