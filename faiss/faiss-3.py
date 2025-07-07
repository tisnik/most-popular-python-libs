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

# konstrukce indexu pro vyhledavani na zaklade vzdalenosti
index = faiss.IndexFlatL2(2)
index.add(points)

print()
print("Dimension(s):         ", index.d)
print("Total values in index:", index.ntotal)
print("Is index trained:     ", index.is_trained)
