import scipy.datasets as datasets
import matplotlib.pyplot as plt

# načtení signálu
ekg = datasets.electrocardiogram()

# zobrazení části signálu
plt.plot(ekg[0:1000])

# uložení grafu s průběhem signálu
plt.savefig("ekg_2.png")

# zobrazení grafu
plt.show()
