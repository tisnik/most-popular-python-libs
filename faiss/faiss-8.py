# Knihovna FAISS
#
# - benchmark rychlosti nalezení nejpodobnějších vektorů
# - výpis výsledků v tabulkové formě
# - vizualizace výsledků formou grafu

from time import time
import faiss
import numpy as np

import matplotlib.pyplot as plt


def similarity_search(n, k):
    DIMENSIONS=128

    t1 = time()

    # nahodne vektory
    data = np.random.rand(n, 128).astype('float32')

    t2 = time()

    # konstrukce indexu pro vyhledavani na zaklade vzdalenosti
    index = faiss.IndexFlatL2(DIMENSIONS)
    index.add(data)

    t3 = time()

    # vektor, ke kteremu budeme pocitat vzdalenost
    query_vector = np.random.rand(1, DIMENSIONS).astype("float32")

    # pocet nejblizsich bodu
    distances, indices = index.search(query_vector, k)
    t4 = time()
    assert len(distances) == k
    assert len(indices) == k

    return n, t2-t1, t3-t2, t4-t3


ns = []
ts_rand = []
ts_index = []
ts_search = []

for n in np.linspace(1000000, 10000000, 10):
    print(n)
    n, t_rand, t_index, t_search = similarity_search(int(n), 1)
    ns.append(n)
    ts_rand.append(t_rand)
    ts_index.append(t_index)
    ts_search.append(t_search)


plt.plot(ns, ts_rand, "r-", label="numpy.random.rand")
plt.plot(ns, ts_index, "b-", label="index creation")
plt.plot(ns, ts_search, "m-", label="similarity search")

# přidání legendy
plt.legend(loc="upper left")

# povolení zobrazení mřížky
plt.grid(True)

plt.savefig("faiss_benchmark_2.png")

# zobrazení grafu
plt.show()
