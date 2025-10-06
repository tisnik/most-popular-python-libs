# Knihovna FAISS
#
# - vizualizace koncových bodů vektorů v rovině

import matplotlib.pyplot as plt
import numpy as np

# pocet slozek vektoru
DIMENSIONS=2

# pocet vektoru
N=1000

# pocet nejpodobnejsich vektoru, ktere se maji nalezt
K=100

# náhodné vektory v rovině [0,0] - [1,1]
vectors = np.random.rand(N, DIMENSIONS).astype("float32")

# velikost grafu
plt.figure(figsize=(8, 8), dpi=80)

# vykreslení všech náhodně vygenerovaných bodů
plt.plot(vectors[:,0], vectors[:,1], "+k", label="original vectors", markersize=5)

# přidání legendy
plt.legend(loc="upper left")

# povolení zobrazení mřížky
plt.grid(True)

# vykreslení grafu do souboru
plt.savefig("faiss-9.png")

# zobrazení grafu
plt.show()
