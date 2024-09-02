import numpy as np

# počet vzorků v mřížce
VALUES = 5

# X je matice vytvořená z mřížky
# dvojice vektorů pro konstrukci mřížky
x1 = np.linspace(0, 100, VALUES)
x2 = np.linspace(0, 100, VALUES)

print("x1:", x1)
print("x2:", x2)
print()

# konstrukce mřížky
grid = np.meshgrid(x1, x2)

print("grid #1:\n", grid[0])
print()
print("grid #2:\n", grid[1])
print()

# změna tvaru na matici se dvěma sloupci
X = np.vstack([grid[0].flatten(), grid[1].flatten()]).T

print("X shape:", X.shape)
print(X)
print()

# y je vektor
y = (grid[0] + grid[1]).flatten()

print("y shape:", y.shape)
print(y)

