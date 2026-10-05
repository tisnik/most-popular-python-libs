import matplotlib.pyplot as plt
import scipy.datasets as datasets

# načtení signálu
ekg = datasets.electrocardiogram()

# zobrazení části signálu
plt.plot(ekg[::200])

# uložení grafu s průběhem signálu
plt.savefig("ekg_3.png")

# zobrazení grafu
plt.show()
