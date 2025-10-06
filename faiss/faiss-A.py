# Knihovna FAISS
#
# - vykreslení nejpodobnějších vektorů získaných na základě L2 metriky
# - vektory nejsou normalizovány

import faiss
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

# konstrukce indexu pro vyhledávání na základě vzdáleností
index = faiss.IndexFlatL2(DIMENSIONS)
index.add(vectors)

# vektor, ke kterému budeme počítat vzdálenost
query_vector = np.array([[0.5, 0.5]]).astype("float32")

# najít K nejbližších vektorů
distances, indices = index.search(query_vector, K)

# --- graf ---

# velikost grafu
plt.figure(figsize=(8, 8), dpi=80)

# vykreslení všech náhodně vygenerovaných bodů
plt.plot(vectors[:,0], vectors[:,1], "+k", label="original vectors", markersize=5)

# vykreslení nejbližších bodů
xs = vectors[:,0][indices][0]
ys = vectors[:,1][indices][0]
plt.plot(xs, ys, "+r", label="nearest vectors", markersize=5)

# vykreslení koncového bodu vektoru, ke kterému hledáme K nejbližších vektorů
x = query_vector[0][0]
y = query_vector[0][1]
plt.plot(x, y, "ob", label="query vector", markersize=10)

# přidání legendy
plt.legend(loc="upper left")

# povolení zobrazení mřížky
plt.grid(True)

# vykreslení grafu do souboru
plt.savefig("faiss-A.png")

# zobrazení grafu
plt.show()
