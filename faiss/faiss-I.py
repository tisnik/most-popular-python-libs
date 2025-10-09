# Knihovna FAISS
#
# - benchmark rychlosti nalezení nejpodobnějších vektorů
# - vizualizace výsledků formou grafu
# - porovnání float16 a float32

from time import time

import faiss
import matplotlib.pyplot as plt
import numpy as np


def similarity_search(n, k, float_type):
    """Nalezeni k nejblizsich vektoru v mnozine n vektoru."""
    # pocet dimenzi vektoru
    DIMENSIONS=128

    # nahodne vektory
    data = np.random.rand(n, 128).astype(float_type)

    # konstrukce indexu pro vyhledavani na zaklade vzdalenosti
    index = faiss.IndexFlatL2(DIMENSIONS)
    index.add(data)

    t1 = time()

    # vektor, ke kteremu budeme pocitat vzdalenost
    query_vector = np.random.rand(1, DIMENSIONS).astype(float_type)

    # pocet nejblizsich bodu
    distances, indices = index.search(query_vector, k)
    t2 = time()

    return n, t2-t1


def benchmark(from_n, to_n, steps, float_type):
    ns = []
    ts_search = []

    for n in np.linspace(from_n, to_n, steps):
        print(n)
        n, t_search = similarity_search(int(n), 1, float_type)
        ns.append(n)
        ts_search.append(t_search)

    return ns, ts_search


#for n in np.linspace(1000000, 10000000, 10):
from_n = 1000000
to_n = 10000000
steps = 10

ns, float16_times = benchmark(from_n, to_n, steps, "float16")
_, float32_times = benchmark(from_n, to_n, steps, "float32")

plt.plot(ns, float16_times, "r-", label="float16")
plt.plot(ns, float32_times, "b-", label="float32")

# přidání legendy
plt.legend(loc="upper left")

# povolení zobrazení mřížky
plt.grid(True)

plt.savefig("faiss_benchmark_3.png")

# zobrazení grafu
plt.show()

