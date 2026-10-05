import matplotlib.pyplot as plt
import scipy.datasets as datasets

# načtení signálu
ekg = datasets.electrocardiogram()

# zobrazení části signálu
plt.plot(ekg[0:1000])

# uložení grafu s průběhem signálu
plt.savefig("ekg_2.png")

# zobrazení grafu
plt.show()
