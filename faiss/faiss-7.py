# Knihovna FAISS
#
# - nalezení nejpodobnějších vektorů
# - použití metriky založené na skalárním součinu
# - výpis souřadnic nejpodobnějších vektorů
# - vektory jsou normalizovány

import faiss
import numpy as np

# x-ove souradnice bodu v rovine
x = [-5, -4, -3,    3,  4,  5,   3, 3, 3,  4, 4, 4,  5, 5, 5]

# y-ove souradnice bodu v rovine
y = [ 5,  3,  5,   -5, -3, -5,   3, 4, 5,  3, 4, 5,  3, 4, 5]

# konstrukce 2D matice, v niz kazdy radek obsahuje souradnice jednoho bodu v
# rovine
points = np.column_stack((x,y)).astype("float32")
print(points)

# normalizace
for i in range(len(points)):
   vector = points[i]
   normalized = np.linalg.norm(vector)
   vector /= normalized
   points[i] = vector

print()
print("Normalized:")
print(points)

# konstrukce indexu pro vyhledavani na zaklade vzdalenosti
index = faiss.IndexFlatIP(2)
index.add(points)

print()
print("Dimension(s):         ", index.d)
print("Total values in index:", index.ntotal)
print("Is index trained:     ", index.is_trained)

# vektor, ke kteremu budeme pocitat vzdalenost
query_vector = np.array([[3, 3]]).astype("float32")
normalized = np.linalg.norm(query_vector)
query_vector /= normalized
print(query_vector)

# pocet nejblizsich bodu
k = len(x)
distances, indices = index.search(query_vector, k)

# tisk vysledku
print("Nearest neighbors:")
print("neighbour  distance  coordinates  ")
print("----------------------------------")
for i in range(k):
    print(f"{i+1:3}      {distances[0][i]:+7.4f}     {points[indices[0][i]]}")
