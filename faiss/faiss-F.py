# Knihovna FAISS
#
# - nalezení nejpodobnějších vektorů získaných na základě skalárního součinu
# - vektory jsou normalizovány
# - vykreslení všech vektorů po normalizaci formou orientovaných šipek

import faiss
import numpy as np

import matplotlib.pyplot as plt


DIMENSIONS=2
N=100
K=10

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
distances, indices = index.search(normalized_query_vector, K)

# --- graf ---

# velikost grafu
plt.figure(figsize=(8, 8), dpi=80)

# vykreslení všech náhodně vygenerovaných vektorů
for i in range(vectors.shape[0]):
    plt.arrow(0, 0, normalized[i, 0], normalized[i, 1], head_width=0.02, head_length=0.02, color="black")

# vykreslení nejpodobnějších vektorů
xs = normalized[:,0][indices][0]
ys = normalized[:,1][indices][0]
for i in range(xs.shape[0]):
    plt.arrow(0, 0, xs[i], ys[i], head_width=0.02, head_length=0.02, color="red")

# vykreslení vektoru, ke kterému hledáme K nejbližších vektorů
x = normalized_query_vector[0][0]
y = normalized_query_vector[0][1]
plt.arrow(0,0, x, y, head_width=0.03, head_length=0.03, color="blue")

# přidání legendy
plt.legend(loc="upper left")

# povolení zobrazení mřížky
plt.grid(True)

# vykreslení grafu do souboru
plt.savefig("faiss-F.png")

# zobrazení grafu
plt.show()
