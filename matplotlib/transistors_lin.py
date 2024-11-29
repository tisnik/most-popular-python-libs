"""Transistors counts in Intel CPUs in the first four x86 generations."""

import matplotlib.pyplot as plt

transistors = [
    [1978, 29000],
    [1979, 29000],
    [1982, 134000],
    [1985, 275000],
    [1988, 275000],
    [1989, 1200000],
    [1991, 1185000],
    [1992, 1185000],
    [1994, 1600000],
]

moore_25000 = [
    [1978, 25000],
    [1980, 50000],
    [1982, 100000],
    [1984, 200000],
    [1986, 400000],
    [1988, 800000],
    [1990, 1600000],
    [1992, 3200000],
    [1994, 6400000],
]

moore_10000 = [
    [1978, 10000],
    [1980, 20000],
    [1982, 40000],
    [1984, 80000],
    [1986, 160000],
    [1988, 320000],
    [1990, 640000],
    [1992, 1280000],
    [1994, 2560000],
]

# hodnoty na x-ové ose
x1 = [t[0] for t in transistors]
y1 = [t[1] for t in transistors]
x2 = [t[0] for t in moore_25000]
y2 = [t[1] for t in moore_25000]
x3 = [t[0] for t in moore_10000]
y3 = [t[1] for t in moore_10000]

plt.plot(x1, y1, "b-", label="Intel CPUs")
plt.plot(x2, y2, "r-", label="Moore law @ 25000")
plt.plot(x3, y3, "y-", label="Moore law @ 10000")

# přidání legendy
plt.legend(loc="upper left")

# povolení zobrazení mřížky
plt.grid(True)

plt.savefig("transistors_lin.png")

# zobrazení grafu
plt.show()
