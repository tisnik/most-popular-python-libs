# Knihovna FAISS
#
# - benchmark rychlosti nalezení nejpodobnějších vektorů
# - je použit index IVFFlat
# - počet regionů je konstantní (1000)
# - postupně se zvyšuje počet sousedních regionů, které se prohledávají
# - výpis výsledků v tabulkové formě
# - vizualizace výsledků formou grafu

from time import time
import faiss
import numpy as np

import matplotlib.pyplot as plt


def similarity_search(n, k, nlist=1000, nprobe=1):
    """Nalezeni k nejblizsich vektoru v mnozine n vektoru."""
    # pocet slozek vektoru
    DIMENSIONS=128

    t1 = time()

    # nahodne vektory
    data = np.random.rand(n, 128).astype('float32')

    t2 = time()

    # konstrukce indexu pro vyhledavani na zaklade vzdalenosti
    quantizer = faiss.IndexFlatL2(DIMENSIONS)
    index = faiss.IndexIVFFlat(quantizer, DIMENSIONS, nlist)

    index.train(data)
    index.add(data)
    index.nprobe=nprobe

    t3 = time()
    REP_COUNT = 1000

    for _ in range(REP_COUNT):
        # vektor, ke kteremu budeme pocitat vzdalenost
        query_vector = np.random.rand(1, DIMENSIONS).astype("float32")

        # pocet nejblizsich bodu
        distances, indices = index.search(query_vector, k)

        # test, kolik vektoru se nalezlo
        assert len(distances) == k
        assert len(indices) == k

    t4 = time()

    return n, t2-t1, t3-t2, (t4-t3)/REP_COUNT


ns = []
ts_search = []

N = 1000000
for n_probe in np.linspace(1, 15, 15):
    print(n_probe)
    n, t_rand, t_index, t_search = similarity_search(N, 1, 20, int(n_probe))
    ns.append(n_probe)
    ts_search.append(t_search)


plt.xlabel("# n_probe")
plt.ylabel("Time/sec")
plt.plot(ns, ts_search, "m-", label="similarity search")

# přidání legendy
plt.legend(loc="upper left")

# povolení zobrazení mřížky
plt.grid(True)

plt.savefig("faiss_benchmark_9.png")

# zobrazení grafu
plt.show()
