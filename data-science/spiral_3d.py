import matplotlib.pyplot as plt
import numpy as np

# celkový počet vypočtených bodů na Lorenzově atraktoru
n = 10000

t = np.linspace(0, np.pi*5, 1000)

# prozatím prázdné pole připravené pro výpočet
x = np.sin(t)
y = np.cos(t)
z = t

fig2 = plt.figure("3D Coordinates", figsize=(8, 10))
plt.subplot(3, 2, 1)
plt.plot(y, x, linewidth=0.75)
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(3, 2, 2)
plt.plot(y, z, linewidth=0.75)
plt.grid()
plt.xlabel("Z")
plt.ylabel("Y")

plt.subplot(3, 2, 3)
plt.plot(z, x, linewidth=0.75)
plt.grid()
plt.xlabel("X")
plt.ylabel("Z")

ax = fig2.add_subplot(3, 2, 4, projection="3d")
ax.plot(x, y, z, linewidth=0.7)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.subplot(3, 2, 5)
plt.plot(t, x, t, y, t, z)
plt.grid()
plt.tight_layout()

# uložení grafu
plt.savefig("lorenz_2.png")

# zobrazení grafu
plt.show()
