# Knihovna FAISS
#
# - vyhledání a vykreslení nejvíce NEpodobných vektorů
# - vykreslení těchto vektorů
# - složky všech vektorů jsou typu float32

import faiss
import numpy as np

import matplotlib.pyplot as plt


# pocet slozek vektoru
DIMENSIONS=2

# pocet vektoru
N=1000

# pocet nejpodobnejsich vektoru, ktere se maji nalezt
K=100

# náhodné vektory v rovině [0,0] - [1,1]
vectors = np.random.rand(N, DIMENSIONS).astype("float32")

normalized = np.matrix.copy(vectors)

# normalizace vektorů
for i in range(len(vectors)):
   vector = vectors[i]
   norm = np.linalg.norm(vector)
   normalized[i] = vector / norm

# konstrukce indexu pro vyhledávání na základě skalárního součinu
index = faiss.IndexFlatIP(DIMENSIONS)
index.add(normalized)

# vektor, ke kterému budeme počítat vzdálenost
query_vector = np.array([[0.5, 0.5]])
norm = np.linalg.norm(query_vector)
normalized_query_vector = query_vector / norm

# najít K nejbližších vektorů
distances, indices = index.search(-normalized_query_vector, K)

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
plt.savefig("faiss-G.png")

# zobrazení grafu
plt.show()
